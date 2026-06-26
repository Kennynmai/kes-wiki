# Amazon Reviews With Images Archive - Bathtub Filter

Date: 2026-06-02

Scope: actual customer-uploaded Amazon image assets from `Reviews with images`, archived for bathtub-filter benchmark products that were available without relying on sample purchase.

Filterbaby `B0FNVDJRSQ` was previously included here as a premium adjacent benchmark. On 2026-06-03 it was split out to `raw/products/shower-filter/` because it is a shower filter / showerhead inline product, not a bathtub filter.

## Evidence boundary

- This is a customer-image archive, not a sample teardown and not a lab test.
- The files are actual Amazon customer image assets saved from product review image areas. Exact image URLs are in `download-manifest.csv`.
- Obvious face/body/skin closeups were excluded. Kept images focus on installation, hanging method, packaging, manual/box contents, filter body, visible media, refill packet, and water-flow path.
- The direct Amazon media-review URL forced sign-in and browser automation was unstable. The final archived images came from Amazon product pages where the `Reviews with images` customer image assets were exposed.
- File names are descriptive labels for internal indexing. Treat the image itself and source URL as the evidence, not the file name.

## Source pages and counts

| Brand / route | ASIN used | Amazon source page | Saved images |
|---|---|---|---:|
| Canopy premium tub-spout route | `B0GFQ1JRSK` corpus row; product page variant `B0FLN3N4T1` | https://www.amazon.com/Canopy-Baby-Bath-Tub-Filter/dp/B0FLN3N4T1 | 11 |
| Santevia soft-hanging cloth route | `B0742KFY9R` | https://www.amazon.com/dp/B0742KFY9R | 4 |
| Crystal Quest bath-ball route | `B008A4AG2U` | https://www.amazon.com/dp/B008A4AG2U | 12 |

## Visual findings

### Canopy

Actual customer images show a soft silicone body covering the tub spout like a bumper, with a lower cartridge/filter section and visible front outlet. Packaging evidence includes a kraft box, molded cardboard tray, manual booklet, QR-labeled part, and adapter/insert pieces.

Representative images:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/01-installed-grey-on-tub-spout.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/04-unboxed-tray-parts.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/08-box-and-product.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/11-packaging-box-exterior.jpg]]

Files:

| File | What it shows |
|---|---|
| `canopy/01-installed-grey-on-tub-spout.jpg` | Grey Canopy installed on tub spout; spout-cover / bumper geometry. |
| `canopy/02-review-image-product-card.jpg` | Product/review image card. |
| `canopy/03-handheld-spout-fit.jpg` | Handheld view of spout fit / filter body. |
| `canopy/04-unboxed-tray-parts.jpg` | Box open, molded tray, manual, adapter/insert pieces, QR-labeled part. |
| `canopy/05-installed-white-on-tub-spout.jpg` | White Canopy installed on tub spout. |
| `canopy/06-label-open-back-filter-door.jpg` | Label / back-door or lower filter-area detail. |
| `canopy/07-installed-bath-toy-context.jpg` | Installed context around tub. |
| `canopy/08-box-and-product.jpg` | Product, manual booklet, QR-labeled part. |
| `canopy/09-water-test-strip-photo.jpg` | Water test strip photo from customer review; do not treat as Canopy manual evidence. |
| `canopy/10-product-in-molded-box.jpg` | Product in box/tray. |
| `canopy/11-packaging-box-exterior.jpg` | Exterior kraft box with Canopy branding. |

### Moved Out: Filterbaby

Filterbaby customer images were moved to the shower-filter project:

`raw/products/shower-filter/2026-06-02-amazon-review-images/filterbaby/`

Reason: actual customer images show inline shower installation on shower arm / hose / showerhead, not bathtub-spout installation.

### Santevia

Actual customer images show a soft cloth/mesh hanging route rather than a rigid housing. The strongest visual evidence is the cotton bag, loofah-like mesh element, drawstring pouch, and hanging over faucet.

Representative images:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/santevia/01-bag-hanging-on-faucet.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/santevia/02-bag-loofah-filter-parts.jpg]]

Files:

| File | What it shows |
|---|---|
| `santevia/01-bag-hanging-on-faucet.jpg` | Cloth bag hanging from faucet. |
| `santevia/02-bag-loofah-filter-parts.jpg` | Bag, loofah-like mesh, drawstring pouch, soft components. |
| `santevia/03-filter-bag-closeup.jpg` | Filter bag closeup. |
| `santevia/04-loofah-and-filter-bag.jpg` | Loofah-like element and filter bag. |

### Crystal Quest

Actual customer images show a bath-ball style unit hanging by cords under a tub spout, water flowing through the top grille, visible top media/grille details, refill packets, and box.

Representative images:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/crystal-quest/01-hanging-on-square-tub-spout.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/crystal-quest/06-top-filter-media-view.jpg]]

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/crystal-quest/05-refill-packets-and-box.jpg]]

Files:

| File | What it shows |
|---|---|
| `crystal-quest/01-hanging-on-square-tub-spout.jpg` | Bath-ball unit hanging from square tub spout. |
| `crystal-quest/02-water-flow-through-filter.jpg` | Water flowing through filter. |
| `crystal-quest/03-mounted-on-spout-running-water.jpg` | Mounted under spout with running water. |
| `crystal-quest/04-black-version-hanging-on-spout.jpg` | Black version hanging from spout. |
| `crystal-quest/05-refill-packets-and-box.jpg` | Refill / hard-handle packets and box context. |
| `crystal-quest/06-top-filter-media-view.jpg` | Top grille / visible media area under spout. |
| `crystal-quest/07-before-after-water-glasses.jpg` | Customer before/after water-glass comparison. |
| `crystal-quest/08-open-top-hanging-cords.jpg` | Open top and hanging cords. |
| `crystal-quest/09-handheld-bathroom-context.jpg` | Handheld bathroom context. |
| `crystal-quest/10-ball-body-closeup.jpg` | Ball body closeup. |
| `crystal-quest/11-top-grille-under-spout.jpg` | Top grille directly under spout. |
| `crystal-quest/12-water-running-installed.jpg` | Installed with water running. |

## Remaining gaps

- This archive does not cover all 11 ASINs. It covers the bathtub-filter benchmark products available from the current pass: Canopy, Santevia, Crystal Quest.
- Filterbaby was moved to `raw/products/shower-filter/` and should not be counted as bathtub-filter image evidence.
- Tubo, SHLLKTTRY, JYFJYF and other PDP-only / low-price routes still have review-image leads from the corpus, but their actual image assets are not archived in this folder.
- Real return rate, refund reason, customer-service tickets, and measured leak/overflow/chlorine/flow data remain unavailable from public pages and should not be treated as web-research tasks.
