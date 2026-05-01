# Chaoshan Beef Site

[![Site Quality](https://github.com/HenryLee789/chaoshan-beef-site/actions/workflows/quality.yml/badge.svg)](https://github.com/HenryLee789/chaoshan-beef-site/actions/workflows/quality.yml)

A static GitHub Pages website for a Chaoshan-style fresh beef shop in Zhengzhou, China.

The project keeps the public storefront page, product copy, visual assets, and basic quality checks in one small repository so updates can be reviewed and published transparently.

## Preview

- Production domain: https://test9020.top/
- Main page: `index.html`
- Stylesheet: `styles.css`
- Brand assets: `brand-assets/`

## Features

- Responsive single-page storefront
- Chinese copy for brand positioning, product pricing, and visit information
- Local brand assets for storefront, product, and poster imagery
- Accessible navigation landmarks, image alt text, and semantic sections
- Zero-build deployment through GitHub Pages

## Repository Structure

```text
.
├── CNAME
├── README.md
├── ROADMAP.md
├── brand-assets/
├── index.html
├── scripts/
└── styles.css
```

## Local Development

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

The script verifies that required files exist, referenced local assets are present, images have alt text, and the page includes basic metadata.

## Deployment

The site is designed for GitHub Pages. The `CNAME` file points the Pages deployment to:

```text
test9020.top
```

## Maintenance

Typical maintenance work includes:

- Updating product descriptions, prices, and store information
- Replacing or adding brand images
- Checking mobile layout and accessibility after content changes
- Keeping the README and deployment notes current
- Reviewing local asset references before publishing

See [ROADMAP.md](ROADMAP.md) for planned improvements.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
