# Bathtub Filter — Marketplace Negative Review Signals (2026-04-13)

## Purpose
Capture directional marketplace-native complaint signals tied to public search-visible snippets, especially around fit, slip, chlorine-removal credibility, and expectation mismatch.

## Method
- Brave web search
- query: `site:amazon.com bathtub filter review leak fit slow flow chlorine bath ball Canopy Santevia Sprite Crystal Quest`
- use visible Amazon snippets only in this pass

## Extracted signals
### Crystal Quest Premium Bath Ball Water Filter — Amazon snippet signal
URL:
- https://www.amazon.com/Crystal-Quest-CQE-SP-00808-White-Filter/dp/B008A4AG2U

Visible snippet signal:
- functionality and value receive mixed feedback
- some users say it filters many contaminants
- others say it does not remove chlorine
- some say it hangs well
- others report it slips off the faucet

Working interpretation:
- this is exactly the kind of mixed marketplace-native pattern that matters for KES
- complaint clusters are not only about efficacy, but also attachment stability
- “slips off the faucet” is especially important because it links compatibility and trust failure in one phrase

### Crystal Quest bundle / related listing — Amazon snippet signal
URL:
- https://www.amazon.com/Crystal-Quest-Replacement-Filter-Cartridge/dp/B0D2JB8VBN

Visible snippet signal:
- some reviews say water feels softer
- some mention chlorine smell reduction

Working interpretation:
- positive conversion language is still dominated by perceptible sensory cues
- this strengthens the view that the category sells on sensory reassurance, while complaints may center on attachment and proof mismatch

## Cross-signal implication
Even this shallow marketplace-native pass already suggests a practical split:
- positive language = softer feel, less chlorine smell
- negative language = doesn’t remove chlorine, slips off faucet

That is commercially important because the exact same SKU can attract both perceived-benefit praise and product-reality complaints.

## Caveats
- this is a search-snippet pass, not a full exported review dataset
- complaint-frequency cannot be quantified from snippets alone
- deeper SKU-level extraction is still needed
