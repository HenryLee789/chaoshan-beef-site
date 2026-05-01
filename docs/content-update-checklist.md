# Content Update Checklist

Use this checklist before publishing public-facing storefront changes.

## Store Details

- Confirm the phone number is current.
- Confirm the street address and nearby landmarks are accurate.
- Confirm opening hours and holiday exceptions.
- Confirm map, route, and visit instructions still match the storefront location.

## Products And Pricing

- Confirm every displayed price with the store owner or latest source.
- Check that promoted products also appear in the price board when appropriate.
- Review product names for consistent wording across hero copy, cards, and price rows.
- Remove or update items that are unavailable for an extended period.

## Images

- Use local image files under `brand-assets/`.
- Check that new images are compressed enough for mobile visitors.
- Keep descriptive `alt` text for every product, poster, and storefront image.
- Avoid replacing photos with assets that hide the actual product or store.

## Review

- Run the site quality check:

```bash
python3 scripts/check_site.py
```

- Preview the page on desktop and mobile widths.
- Verify that text does not overlap product cards, buttons, or contact details.
- Keep the pull request description focused on what changed and how it was checked.
