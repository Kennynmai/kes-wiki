# AGENTS.md — KES Company Wiki

## Purpose
This repository is KES’s shared business knowledge system.

It supports knowledge across:
- platforms
- markets
- products and categories
- projects
- decisions
- playbooks
- risks
- metrics
- meeting outputs
- policies and assumptions

The long-term goal is broad company readability with controlled distributed maintenance.
The organization owns truth, approval, and officiality.
The agent maintains structure, summaries, logs, links, consolidation, and contradiction detection.

---

## Operating workflow
All meaningful work follows this progression:
1. capture
2. classify
3. narrow
4. extract
5. deepen
6. update
7. verify
8. lint

### capture
Receive materials into `inbox/` or `raw/`.

### classify
Before extraction, classify the material by source type.
Examples:
- report
- meeting-note
- transcript
- policy-doc
- market-brief
- data-export
- screenshot-set
- competitor-material
- customer-material
- vendor-material
- internal-doc

### narrow
Use progressive disclosure before deep reading.
Do not begin with full documents when index-level understanding is sufficient.

### extract
Use type-specific extraction. Reports, meeting notes, transcripts, and screenshot sets require different handling.

### deepen
Read deeper only when needed for decision support, contradiction resolution, citation accuracy, verification, or high-stakes interpretation.

### update
Produce two outputs when appropriate:
1. the task deliverable
2. updates to maintained wiki pages

### verify
The human organization owns verification.
The higher the stakes, the stronger the verification expectation.

### lint
Improve trustworthiness, coherence, ownership, and retrievability over time.

---

## Core governance rules
1. Separate `inbox/`, `raw/`, and `wiki/`.
2. Separate facts, judgments, decisions, and procedures.
3. Important pages should have accountability (`owner`, `status`, `officiality`).
4. Good answers should become company assets.
5. Use `domain` / `domains` on maintained pages.
6. Use `source_type` and `extraction_mode` on source-summary pages.
7. Important pages should preserve provenance via `Sources`.
8. Future openness does not mean unrestricted editing of official knowledge.

---

## Roles and operating model
### Reader
Can read, search, and ask questions against the wiki.

### Contributor
Can add materials, submit drafts, provide meeting captures, suggest corrections, and request updates.

### Domain Owner
Can validate pages in their domain, review important updates, and confirm domain-specific judgments.

### Editor / Knowledge Steward
Can maintain naming, metadata, structure, index quality, merges, and lint passes.

### Admin / Executive Owner
Can define governance, assign ownership, determine official boundaries, and approve major operating norms.

### Agent
Supports all layers, but does not independently define official company truth.

---

## Dual-output rule
Every substantive task should be evaluated for two outputs:
1. the immediate deliverable
2. relevant updates to maintained company knowledge

Exceptions:
- trivial one-off chat
- clearly disposable low-value output
- tasks explicitly marked “do not write back”
- tasks where evidence is too weak for safe wiki updates

See `governance/write-back-policy.md`.

---

## Verification and editorial responsibility
The agent is the writer.
The human organization is the editor-in-chief.

High-stakes content requires stronger review, especially:
- decision pages
- market-entry conclusions
- compliance-sensitive claims
- policy-like guidance
- metrics definitions
- process-critical playbooks

Suggested `verification_status` values:
- unverified
- spot-checked
- verified

See `governance/verification-policy.md` and `governance/citation-rules.md`.

---

## Official vs working surfaces
Not all pages carry the same trust level.
Broad company use should preferentially start from official surfaces.
See `governance/official-surface-policy.md`.

---

## Rule of thumb
A page belongs here if it helps answer:
“What does KES as an organization need to know, decide, repeat, explain, or execute well?”
