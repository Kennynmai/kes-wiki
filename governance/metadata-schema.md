# Metadata Schema — KES Company Wiki

Recommended fields:
- `type`
- `status`
- `owner`
- `created`
- `updated`
- `visibility`
- `confidence`
- `officiality`
- `domain`
- `domains`
- `aliases`
- `name_zh`
- `name_en`
- `source_count`
- `review_cycle`
- `verification_status`
- `related`

## Common values
### status
- `draft`
- `active`
- `under-review`
- `blocked`
- `archived`

### officiality
- `draft`
- `reviewed`
- `official`

### verification_status
- `unverified`
- `spot-checked`
- `verified`

## Source-summary-specific fields
- `source_type`
- `extraction_mode`
- `source_title`
- `source_date`
- `source_author`
- `raw_path`

## Guidance
- `officiality` = governance state
- `verification_status` = evidence-check state
- use `domain` / `domains` on nearly all maintained pages
- `aliases` should capture common Chinese and English retrieval variants
- prefer `name_zh` for broad internal readability and `name_en` for canonical entity matching
