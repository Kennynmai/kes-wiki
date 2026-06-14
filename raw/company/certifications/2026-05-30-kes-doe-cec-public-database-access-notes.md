---
source_type: public-record
captured: 2026-05-30
source_title: KES DOE and CEC public database access notes
source_author: agent
classification: public-record
extraction_mode: targeted-public-database-access
verification_status: spot-checked
---

# KES DOE and CEC Public Database Access Notes — 2026-05-30

## Scope
This capture records follow-up access attempts for DOE CCMS and CEC MAEDbS after the main KES certification verification pass.

The goal was to determine whether public KES-specific DOE / CEC rows could be retrieved online, and if not, to preserve the exact official paths and blockers for the next evidence-collection pass.

## DOE CCMS

Attempted official DOE certification-data endpoints:

- <https://www.regulations.doe.gov/certification-data/CCMS-4-Faucets.html>
- <https://www.regulations.doe.gov/certification-data/CCMS-4-Showerheads.html>

Observed result:

- HTTP status: `403`
- Server: `awselb/2.0`
- No KES-specific rows retrieved.

Working interpretation:

- DOE remains internally evidenced only in the local KES register.
- For external claim control, KES still needs CCMS exports, screenshots, or a browser-based public search record for the relevant basic models.

## CEC MAEDbS

Official public surfaces tested:

- Company Search: <https://cacertappliances.energy.ca.gov/Pages/CompanyInfo/CompanyList.aspx>
- Quick Search: <https://cacertappliances.energy.ca.gov/Pages/Search/QuickSearch.aspx>
- Advanced Search: <https://cacertappliances.energy.ca.gov/Pages/Search/AdvancedSearch.aspx>
- Public Search Help PDF: <https://cacertappliances.energy.ca.gov/Help/PublicSearchHelp.pdf>

Observed behavior:

| Surface | Result | KES-specific rows retrieved? |
|---|---|---|
| Quick Search | Redirected to `/Login.aspx?ReturnUrl=%2fPages%2fSearch%2fQuickSearch.aspx` in command-line access | no |
| Advanced Search | Public page loaded without login | no |
| Company Search | Public page loaded; default results showed `566 record(s) found` for `Test Lab` company type | no |

## CEC Advanced Search structure observed

The Advanced Search page text states that it allows narrower search by selecting category, type, additional filters, and result fields. It also links Search Instructions and says questions can be directed to `Appliances@energy.ca.gov` or the Appliances Hotline.

Relevant category / appliance options observed:

| Field | Option | Value observed |
|---|---|---|
| Select Category | `Plumbing Products` | `b00863f1-25d8-40da-87d2-cf092d6c172d` |
| Select Appliance | `Plumbing Fittings` | `4252ccde-29a9-4681-b810-f300c874218d` |
| Select Appliance | `Plumbing Fixtures` | `a4cd35c6-7b76-41c8-a875-cfc68926b5c4` |
| Select Appliance Status | `Approved` | `1b8a27c3-a453-4287-b3ba-ebc403a6406d` |
| Select Appliance Status | `Archived` | `f2c14942-cd42-404f-8921-b023d568b0ae` |

Simulation notes:

- A form post selecting `Plumbing Products` returned a populated appliance dropdown with `Plumbing Fittings` and `Plumbing Fixtures`.
- A subsequent form post selecting `Plumbing Fittings` and `Approved` timed out before returning search results.
- No KES-specific MAEDbS product rows were captured in this pass.

## Evidence boundary

This pass improves the CEC retrieval path but does not prove KES MAEDbS product listing status. The internal source-table `CEC Compliance` status remains the only KES-specific evidence currently recorded in the local wiki.

## Next evidence needed

- Browser-based CEC MAEDbS search screenshots or export for `KES`, `KES HOME`, and known internal model numbers.
- Split by `Plumbing Fittings` and `Plumbing Fixtures`.
- Capture both `Approved` and `Archived` statuses.
- For DOE, capture CCMS basic model exports / screenshots for faucets and showerheads.
