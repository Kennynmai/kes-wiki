# Amazon review images installation / packaging leads - bathtub filter

Date: 2026-06-02

Scope: 11-ASIN Amazon review corpus in `raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`, plus actual Amazon customer image assets archived on 2026-06-02. On 2026-06-03, Filterbaby `B0FNVDJRSQ` was split out to `raw/products/shower-filter/` because it is a shower filter / showerhead inline product, not a bathtub filter.

Evidence boundary: this note now has two levels of evidence.

- **Archived customer images**: actual Amazon `Reviews with images` customer image assets saved under `raw/products/bathtub-filter/2026-06-02-amazon-review-images/`.
- **Remaining review-image leads**: source Excel/CSV records still contain `image_count`, review text, and review links for other ASINs, but not all actual image URLs. These remain leads until opened and archived.

This is not a sample teardown, not a lab test, and not return-rate evidence. Obvious face/body/skin closeups were excluded from the archive; retained files focus on installation, hanging method, packaging, manual/box contents, filter body, visible media, refill packet, and water-flow path.

## Actual Amazon customer images archived

Raw image folder: `raw/products/bathtub-filter/2026-06-02-amazon-review-images/`

Manifest: `raw/products/bathtub-filter/2026-06-02-amazon-review-images/download-manifest.csv`

Index: `raw/products/bathtub-filter/2026-06-02-amazon-review-images/README.md`

| Brand / route | ASIN | Amazon source page | Images saved | Status |
|---|---|---|---:|---|
| Canopy premium tub-spout route | `B0GFQ1JRSK` corpus row; product page variant `B0FLN3N4T1` | https://www.amazon.com/Canopy-Baby-Bath-Tub-Filter/dp/B0FLN3N4T1 | 11 | Archived |
| Santevia soft-hanging cloth route | `B0742KFY9R` | https://www.amazon.com/dp/B0742KFY9R | 4 | Archived |
| Crystal Quest bath-ball route | `B008A4AG2U` | https://www.amazon.com/dp/B008A4AG2U | 12 | Archived |

## Visual findings from archived images

| Brand / route | Actual images show | Product/design implication |
|---|---|---|
| Canopy | Soft silicone body covering the tub spout like a bumper; lower cartridge/filter section; front outlet; kraft box; molded cardboard tray; manual booklet; QR-labeled part; adapter/insert pieces. | This is a spout-cover form, not a simple dangling bag. Packaging is more DTC/premium than low-price bath-ball products. |
| Santevia | Cloth/mesh hanging route; cotton bag, loofah-like mesh element, drawstring pouch, and soft parts. | This route depends heavily on soft-material trust, cleaning, drying, and user belief in internal structure. |
| Crystal Quest | Bath-ball unit hanging by cords under tub spout; water flows through top grille; top media/grille visible; refill / hard-handle packets and box context. | Classic hanging bath-ball route; visual risk centers on hanging stability, bypass/flow path, and refill handling. |

## Representative image embeds

Canopy installed on tub spout:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/01-installed-grey-on-tub-spout.jpg]]

Canopy box / manual / parts:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/canopy/08-box-and-product.jpg]]

Santevia soft bag / loofah-like parts:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/santevia/02-bag-loofah-filter-parts.jpg]]

Crystal Quest hanging bath-ball / top grille:

![[raw/products/bathtub-filter/2026-06-02-amazon-review-images/crystal-quest/06-top-filter-media-view.jpg]]

Filterbaby inline shower images were moved to `raw/products/shower-filter/2026-06-02-amazon-review-images/filterbaby/`.

## Remaining image leads not yet archived

The archive above does **not** cover all active bathtub ASINs. Tubo, SHLLKTTRY, JYFJYF and other PDP-only / low-price routes still have review-image leads in the corpus, especially around overflow, Velcro/string/loop hanging methods, sponge removal, and package-claim mismatch. The sections below retain those leads for future visual follow-up.

## Image-review density by ASIN

| ASIN | Brand / route | Reviews with images in corpus | Priority for visual follow-up |
|---|---|---:|---|
| `B0D3X39378` | SHLLKTTRY / overflow low-price route | 91 | Very high |
| `B0742KFY9R` | Santevia / soft-hanging cloth route | 69 | Very high |
| `B0G5NZBW6W` | Syvahome / KDF55 overflow route | 27 | Medium |
| `B0CXT5KL5Z` | Beati Faucet / low-price bath-ball route | 17 | Medium |
| `B0FL24SLM5` | Yolycen / low-price long-life claim route | 17 | Medium |
| `B0FT7R9ZQ9` | JYFJYF / Velcro strap route | 11 | Medium |
| `B0DTQ8H23D` | Tubo / premium-ish baby route | 9 | High due to attachment failures |
| `B0GFQ1JRSK` | Canopy / premium tub-spout route | 7 | High due to unique silicone cover / temperature strip |
| `B0GKT5CHYL` | Uiuaquas / all-metal tub-spout route | 7 | Medium |
| `B008A4AG2U` | Crystal Quest / bath-ball route | 2 | Low in this corpus, but covered elsewhere |

## High-value review-image leads

| ASIN | Route | Review ID / link | Image clue from review text | What to inspect in images |
|---|---|---|---|---|
| `B0742KFY9R` | Santevia soft-hanging | `R3T4WLH0BIDT4Z` / https://www.amazon.com/gp/customer-reviews/R3T4WLH0BIDT4Z/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0742KFY9R | User says it is "just a shower loofa inside with a little package of balls." 4 images. | Cut/open cloth pouch, loofah-like insert, ball/mineral sachet, perceived non-filter structure. |
| `B0742KFY9R` | Santevia soft-hanging | `RX5OJGPALDS33` / https://www.amazon.com/gp/customer-reviews/RX5OJGPALDS33/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0742KFY9R | Wide faucet did not fit until the user cut a zip tie; user describes black pouf and mineral material inside. 4 images. | Wide faucet workaround, cut/modified tie, internal pouch / pouf / mineral material. |
| `B0742KFY9R` | Santevia soft-hanging | `R31W35XZ8E5IKH` / https://www.amazon.com/gp/customer-reviews/R31W35XZ8E5IKH/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0742KFY9R | User says it is a bag with a bag of white stuff and a scrunchie shower scrubber; inserted two shower filter cartridges as DIY. 2 images. | DIY modification, internal media pouch, replacement cartridge insertion, teardown evidence. |
| `B0742KFY9R` | Santevia soft-hanging | `R3LEZDWUAJWR2` / https://www.amazon.com/gp/customer-reviews/R3LEZDWUAJWR2/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0742KFY9R | Product would not stay on faucet; user tied it with string; water leaked around top/sides. 2 images. | String workaround, attachment to faucet, bypass/leak paths. |
| `B0GFQ1JRSK` | Canopy premium tub-spout | `R279LRBJVL5AJN` / https://www.amazon.com/gp/customer-reviews/R279LRBJVL5AJN/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0GFQ1JRSK | User says whole housing is like soft padding on the spout; diverter reachable; visible colored beads; temperature indicator hard to read. 7 images. | Silicone bumper geometry, tub spout coverage, diverter access, media visibility, temperature strip readability. |
| `B0GFQ1JRSK` | Canopy premium tub-spout | `RCU05OFYRKX5G` / https://www.amazon.com/gp/customer-reviews/RCU05OFYRKX5G/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0FLN3N4T1 | User notes multiple adapters, stickers/labels, slower tub fill, unclear color-changing stripe. 6 images. | Adapter kit, labels, instruction booklet, temperature-stripe placement, installed flow path. |
| `B0DTQ8H23D` | Tubo baby / attachment variants | `R1O89U4AWCZBQL` / https://www.amazon.com/gp/customer-reviews/R1O89U4AWCZBQL/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0DTQ8H23D | Two strap choices; hard plastic handle split during attachment; Velcro failed on faucet without diverter; unit fell into tub; TDS test oddity. 6 images. | Hard handle / split point, Velcro fallback, non-diverter faucet failure, TDS test photo. |
| `B0DTQ8H23D` | Tubo baby / overflow | `R1NEPEOD2VRAJB` / https://www.amazon.com/gp/customer-reviews/R1NEPEOD2VRAJB/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0DTQ8H23D | User removed a small sponge from top so it stopped overflowing; kit has different attachment handles. 2 images. | Sponge / pre-filter piece, overflow path, handle options, modified operating state. |
| `B0D3X39378` | SHLLKTTRY overflow | `R1EC7EV3AZ5BX2` / https://www.amazon.com/gp/customer-reviews/R1EC7EV3AZ5BX2/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0D3X39378 | Silicone loop does not stay on faucet; string does not fit wrap piece; user used longer string and tied it around middle handle; full water flow overflows top. 2 images. | Odd string-to-handle workaround, faucet geometry, overflow at high flow. |
| `B0D3X39378` | SHLLKTTRY overflow | `R1QLLUNH7EJ9WH` / https://www.amazon.com/gp/customer-reviews/R1QLLUNH7EJ9WH/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0D3X39378 | User says listing claims 8 items/stages but box shows only 3 ingredients. 2 images. | Packaging ingredient list, mismatch between PDP claim and box text. |
| `B0FT7R9ZQ9` | JYFJYF Velcro strap | `R1J8Q8SCISJABM` / https://www.amazon.com/gp/customer-reviews/R1J8Q8SCISJABM/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=B0FT7R9ZQ9 | User says adjustable Velcro strap fits tub faucet, no tools, lightweight and portable. 2 images. | Simple Velcro strap geometry, travel/removable use, faucet contact area. |

## Public manuals / instructions surfaced

| Product | Public source | Useful content |
|---|---|---|
| Santevia Bath Filter | https://m.media-amazon.com/images/I/61MT9Yc%2BZ-L.pdf | Amazon-hosted user instructions. Shows two use modes: place under bath water flow or hang on bathtub faucet; after filling, swirl filter in water for 3-5 minutes; rinse and hang to dry after each use. |
| Sprite bath-ball harness | https://m.media-amazon.com/images/I/91YTjoAxPsL.pdf | Amazon-hosted harness-use instructions found in search. Relevant as extra non-11-ASIN benchmark for bath-ball attachment / harness logic. |

## Preliminary design/usage patterns to backfill

1. **Soft hanging pouch route**: Santevia appears in user language as a cloth bag / pouch / loofah-like internal structure, frequently modified with string, zip tie cuts, Velcro, or DIY cartridge insertion.
2. **Silicone spout-cover route**: Canopy is not simply "hanging"; it covers the tub spout like a padded silicone bumper, with visible media/colored beads and a temperature indicator strip.
3. **Multi-strap / handle route**: Tubo and SHLLKTTRY rely on alternative handles, hard plastic clips, silicone loops, strings, and Velcro. These routes generate the most unusual user workarounds.
4. **Overflow-prone top-fill route**: Several low-price/overflow filters appear to fail when full faucet flow exceeds the internal path, leading to top overflow or water bypass.
5. **Moved-out shower inline route**: Filterbaby images were moved to the shower-filter project and should not be used as bathtub spout evidence.
6. **Packaging-claim mismatch route**: SHLLKTTRY review `R1QLLUNH7EJ9WH` is a priority because the user explicitly says the product box contradicts listing-stage claims.

## Follow-up if browser/Amazon access is available

Open the review links above and archive:

- Installed-on-faucet photo.
- Package front/back/sides.
- Instruction booklet / QR code.
- Box ingredient list / claim copy.
- Opened housing / media chamber / visible media.
- Any unusual workaround: string, zip tie cut, Velcro, tied to middle handle, sponge removed, DIY cartridge inserted.
