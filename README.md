# Fake Image Site

A minimal GitHub Pages site for showing a responsive Fake WeChat QR profile at `https://test9020.top/`.

## Preview

- Production domain: https://test9020.top/
- Main page: `index.html`
- Stylesheet: `styles.css`
- Source image: `assets/fake-wechat.png`

## Local Preview

Open `index.html` directly in a browser, or serve the folder with any static file server:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Quality Check

Run the repository check before publishing changes:

```bash
python3 scripts/check_site.py
```

The script verifies that required files exist, referenced local assets are present, images have alt text, and the homepage uses `assets/fake-wechat.png` for the responsive profile and QR crops.

## Deployment

The site is designed for GitHub Pages. The `CNAME` file points the Pages deployment to:

```text
test9020.top
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
