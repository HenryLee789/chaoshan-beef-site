#!/usr/bin/env python3
"""Basic static-site checks for the repository."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_description = False
        self.local_refs: list[tuple[str, str]] = []
        self.images_without_alt: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}

        if tag == "title":
            self.in_title = True

        if tag == "meta" and values.get("name") == "description" and values.get("content"):
            self.meta_description = True

        if tag == "img":
            src = values.get("src", "")
            if src:
                self.local_refs.append(("img", src))
            if not values.get("alt", "").strip():
                self.images_without_alt.append(src or "<missing src>")

        if tag == "link" and values.get("rel") == "stylesheet":
            href = values.get("href", "")
            if href:
                self.local_refs.append(("stylesheet", href))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def is_local_reference(value: str) -> bool:
    parsed = urlparse(value)
    return not parsed.scheme and not parsed.netloc and not value.startswith(("tel:", "mailto:", "#"))


def main() -> int:
    required = [
        ROOT / "index.html",
        ROOT / "styles.css",
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CNAME",
    ]
    missing = [path.relative_to(ROOT) for path in required if not path.exists()]

    html_path = ROOT / "index.html"
    parser = SiteParser()
    parser.feed(html_path.read_text(encoding="utf-8"))

    broken_refs: list[str] = []
    for kind, ref in parser.local_refs:
        if not is_local_reference(ref):
            continue
        target = (ROOT / ref).resolve()
        if ROOT not in target.parents and target != ROOT:
            broken_refs.append(f"{kind}: {ref} escapes repository root")
        elif not target.exists():
            broken_refs.append(f"{kind}: {ref} is missing")

    failures: list[str] = []
    if missing:
        failures.append("Missing required files: " + ", ".join(map(str, missing)))
    if not parser.title.strip():
        failures.append("index.html is missing a title")
    if not parser.meta_description:
        failures.append("index.html is missing a meta description")
    if parser.images_without_alt:
        failures.append("Images missing alt text: " + ", ".join(parser.images_without_alt))
    if broken_refs:
        failures.append("Broken local references: " + "; ".join(broken_refs))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("Site checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
