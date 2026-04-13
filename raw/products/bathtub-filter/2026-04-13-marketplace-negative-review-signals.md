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

## Additional surfaced complaint signals
### Santevia Q&A / Amazon-visible snippet
URL:
- https://www.amazon.com/ask/questions/TxIBJB133QC0JE/

Visible snippet signal:
- “it won't be and shouldn't be as fast as a brita pitcher”
- reports that in some purchases “it wouldn’t filter and water would overflow”
- mentions better support when buying directly versus third-party sellers

Working interpretation:
- fill-speed expectation management is part of the category risk
- overflow is a serious practical failure mode, not just a minor inconvenience
- channel quality / seller quality may affect perceived product reliability

### Generic bathtub-filter Amazon snippet signal
URL:
- https://www.amazon.com/TNEHOD-Filtration-Contaminants-Bathwater-Healthier/dp/B0D9LV6L79

Visible snippet signal:
- one visible review says it is good for a curved faucet
- another says “Slips off no matter what I do.”

Working interpretation:
- curved-faucet compatibility is a real consumer micro-segment
- compatibility success and compatibility failure can coexist sharply even within similar faucet-mount product logic

## Cross-signal implication
Even this shallow marketplace-native pass already suggests a practical split:
- positive language = softer feel, less chlorine smell, works on curved faucet
- negative language = doesn’t remove chlorine, slips off faucet, overflows, too expensive, doesn’t work as advertised

That is commercially important because the exact same SKU or route can attract both perceived-benefit praise and product-reality complaints.

## Caveats
- this is a search-snippet pass, not a full exported review dataset
- complaint-frequency cannot be quantified from snippets alone
- deeper SKU-level extraction is still needed
