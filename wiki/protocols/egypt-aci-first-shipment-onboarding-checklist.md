---
type: protocol
status: active
created: 2026-05-05
updated: 2026-05-06
tags: [egypt, customs, import, aci, nafeza, acid, cargox, first-shipment]
domain: operations
domains: [operations, manufacturing, cross-border, logistics, compliance]
confidence: medium
verification_status: unverified
related:
  - ../source-summaries/egypt-aci-nafeza-acid-cargox.md
  - ../source-summaries/egypt-first-batch-equipment-material-list-2026-05-09.md
  - ../protocols/egypt-rented-factory-launch-checklist.md
---

# Egypt ACI First-Shipment Onboarding Checklist

## Scope
Use this when both sides are first-time users:
- Egyptian importer is a newly formed Egypt subsidiary;
- foreign exporter/supplier is not yet registered or verified on CargoX;
- the shipment will enter Egypt under ACI/NAFEZA.

This is an execution checklist, not legal advice. Confirm the current details with the Egyptian customs broker, NAFEZA/MTS, GOEIC, the Egyptian Customs Authority, and CargoX before shipment.

## Critical sequence
1. Egypt company obtains/validates core company and tax documents.
2. Egypt company obtains customs/trade registrations needed for the intended import type.
3. Egypt company creates and activates NAFEZA commercial account.
4. Egypt company obtains e-Token/e-signature for the person signing/approving NAFEZA documents.
5. Foreign exporter creates CargoX account, buys units from its own company bank account, and completes company verification.
6. Exporter sends verified CargoX company details to Egypt importer.
7. Egypt importer creates shipment in NAFEZA and requests ACID before shipment.
8. Exporter files ACI envelope through CargoX before shipment.
9. Forwarder/carrier includes ACID in transport documents and shipment data.
10. Broker tracks customs release, inspection, duty/VAT, and regulatory approvals after arrival.

## Current status: only tax card obtained
If the only confirmed document is the Egypt tax card, the importer is not yet operationally ready for ACI/NAFEZA first shipment.

Immediate dependency chain:
1. Confirm whether commercial register has been issued. If not, this is the next blocker.
2. Confirm VAT registration certificate or Form 8 / official VAT-status document.
3. Confirm the intended import basis: import for production, import for trade/resale, or import for private/company use.
4. Obtain customs trader registration / Customs Dealer's Card under the correct import basis.
5. If importing factory inputs, equipment, fabrics, accessories, or spare parts for production, evaluate GOEIC Production Supplies Registry before the first shipment.
6. Activate NAFEZA commercial account and match company data at a logistics services center.
7. Obtain and test e-Token for the person who will sign/approve NAFEZA documents.

Practical order:
- Day 0: assemble company file and appoint broker/lawyer to confirm import basis.
- Days 0-2: verify commercial register, VAT status, authorized signer, company address, and activity wording.
- Days 1-5: start e-Token and NAFEZA commercial account activation in parallel.
- Days 1-10: start customs trader registration and GOEIC route if production imports are involved.
- Only after NAFEZA/e-Token/customs trader registration are usable should the importer request the first ACID.

## First shipment timeline
For a first China-to-Egypt shipment of equipment and raw materials where both sides are first-time users, do not plan around the bare 48-hour ACI minimum. Start 3-4 weeks before intended shipment.

Recommended timeline:
- T-4 weeks: exporter confirms export entity and official English company details; Egypt importer confirms commercial register, tax card, VAT/Form 8, authorized signer, address, and activity wording.
- T-3.5 weeks: exporter registers CargoX, enters company details, and creates blockchain key; Egypt importer confirms whether the first shipment is import for production, trade/resale, or company/private use and asks the broker to pre-check HS codes.
- T-3 weeks: exporter buys CargoX units and pays from its own company bank account; Egypt importer starts customs trader registration / Customs Dealer's Card and, if importing equipment or inputs for production, asks GOEIC/consultant about the Production Supplies route.
- T-2 weeks: exporter waits for CargoX bank verification and completes third-party verification; Egypt importer activates NAFEZA commercial account, completes logistics-center data matching, and obtains e-Token.
- T-10 to T-7 days: exporter sends verified CargoX company details to Egypt importer; Egypt importer enters shipment data in NAFEZA and requests ACID.
- T-7 to T-5 days: exporter prepares invoice PDF, NAFEZA structured invoice, packing list, certificate of origin, and any equipment/raw-material certificates; Egypt importer checks NAFEZA data, HS codes, certificates, regulatory approvals, and import permits.
- T-5 to T-3 days: after ACID is issued, exporter composes and submits the CargoX ACI envelope; Egypt importer validates ACID and has broker/freight forwarder check data consistency.
- T-3 to T-1 days: exporter confirms the CargoX envelope is sent and ensures the forwarder/carrier includes ACID on transport documents; Egypt importer confirms the documents are visible/usable in NAFEZA.
- T-0: ship only after ACID is valid, ACI envelope has been sent, and transport data/documents include ACID.

Hard latest dates:
- CargoX registration and first bank-wire purchase: no later than T-3 weeks.
- Egypt customs trader / NAFEZA / e-Token onboarding: no later than T-3 weeks.
- ACID request: no later than T-7 days.
- CargoX ACI envelope filing: no later than T-3 days for a first shipment.
- Official minimum: ACI data/documents at least 48 hours before shipment from export country, but first shipments should not be run against this minimum.

## Egypt importer onboarding

### 1. Company base documents
Minimum file:
- commercial register;
- tax card;
- VAT registration certificate or official VAT-status document when applicable;
- articles/incorporation or investment/company formation documents;
- legal representative/passport/ID and signing authority evidence;
- lease/factory address documents if needed for production registration.

Dependency:
- Tax card alone is not enough.
- Commercial register and VAT status are needed for customs trader registration.
- For e-Token/electronic seal, ITIDA lists recent commercial registry, valid tax card, company gazette/articles or contract, and legal representative ID/passport.
- For production-import treatment, the company must be able to prove productive/industrial/service activity or have the GOEIC production-supplies/needs card.

Estimated timing:
- GAFI states incorporation services have a one-business-day frame and, for LLCs through ISC, commercial registry, tax registration number, VAT registration number, and insurance number are normally received within one business day after completion. This does not mean later customs/GOEIC/NAFEZA registrations are one day.
- If only the tax card is available but commercial register or VAT status is missing, treat those as same-week blockers.

### 2. Customs Dealer's Card / customs trader registration
NAFEZA FAQ states that documents required for NAFEZA registration include Commercial Register, Tax Card, and Customs Dealer's Card.

Egyptian Customs states that customs procedures and release generally require registration in the customs dealers register, except personal-use imports. For import for production, the listed documents include tax card, sales/VAT registration, and an official document proving productive/industrial/service activity or a GOEIC needs/production-supplies card.

Dependency:
- Import for trade/resale requires importer-register card, tax card, VAT/Form 8, and commercial register.
- Import for production requires tax card, VAT/Form 8, commercial register, and either official activity proof or GOEIC requirements/production-supplies card.
- Customs electronic-service registration also requires a customs card with tax number and customs activity registered.

Estimated timing:
- No fixed universal public SLA found on the customs pages checked.
- Customs rules allow temporary registration at the relevant customs site's discretion while registration documents are being completed, provided VAT-related proof is submitted. Treat this as a fallback, not the base plan.

### 3. GOEIC import route decision
Decide with broker/lawyer which route applies:
- import for trade/resale: Importers Register card, generally valid for five years if approved;
- import for production inputs: Production Supplies Registry card, issued to factories/establishments based on activity proof and valid until expiry of the activity document;
- investment/manufacturing project imports: confirm whether the Investment Law/GAFI route removes ordinary importer-register requirements for specific equipment or inputs, but do not assume it removes NAFEZA/customs dealer registration.

For a new factory importing equipment, fabric, accessories, and spare parts, the production-input route is likely important even if ordinary trading imports are not the base case.

Dependency:
- GOEIC commercial e-services account for companies generally requires visiting a GOEIC branch to create/verify the commercial account.
- Production Supplies Registry depends on a document proving industrial/agricultural/tourism or productive/service activity.
- If the factory is not licensed or activity proof is not ready, production-supplies registration may become the long pole.

Estimated timing:
- GOEIC pages checked did not publish a fixed SLA for Production Supplies registration.
- GOEIC's general factory/trademark registration under Decree 43 has a 15-day completion rule after documents are complete, but that is a different registry and should not be treated as the production-supplies SLA.

### 4. NAFEZA commercial account activation
Steps:
- create a NAFEZA account;
- select/upgrade to commercial account;
- complete data entry;
- visit a NAFEZA logistics services center to match data and finalize registration;
- test login and ACI functions before the first shipment.

Dependency:
- NAFEZA public page says commercial customers must upgrade the account and go to a logistics services center to match data and finalize registration.
- NAFEZA FAQ identifies Commercial Register, Tax Card, and Customs Dealer's Card as importer registration documents.
- Do not assume a NAFEZA login alone means the company can request ACID.

Estimated timing:
- No fixed public SLA found for first commercial account activation.
- Base plan: do this only after the commercial register, tax card, VAT status, and customs dealer/trader path are clear; start the online account immediately, but expect the logistics-center visit and data matching to be the gating step.

### 4A. Timing from signed factory lease to usable NAFEZA registration
Signing a factory lease does not itself register the company on NAFEZA. It only helps if the lease is needed to update the company/factory address, support production activity proof, or support customs/GOEIC/IDA registrations.

Practical timing:
- if commercial register, tax card, VAT/Form 8, Customs Dealer's Card, authorized signatory, and e-Token are already ready: NAFEZA account activation/data matching can often be planned as a same-day to 3-business-day task, subject to logistics-center appointment and data match;
- if the lease triggers an address/activity update in the commercial register or tax/VAT file: plan 1-3 weeks before NAFEZA is cleanly usable;
- if the company also needs customs dealer registration under "import for production" and must prove productive/industrial activity: plan 2-6 weeks;
- if GOEIC production-supplies route, IDA operating-license path, or IDA import-invoice approvals are required before the broker will accept the import basis: plan 4-8+ weeks, and do not treat NAFEZA account creation as import readiness.

Minimum "NAFEZA registration complete" definition for this project:
- NAFEZA commercial account exists and is activated;
- company data has been matched/finalized at a NAFEZA logistics services center;
- Commercial Register, Tax Card, and Customs Dealer's Card are accepted;
- e-Token/electronic seal works for the actual signer;
- the company can request ACID and the broker can see/use the importer record.

The lease should be completed before the registration package if the company will import as a production/factory project and the factory address must appear consistently in commercial register, tax/VAT, customs trader, IDA/GOEIC, invoices, and NAFEZA data.

## After NAFEZA registration: importer-side execution steps
Once the Egypt importer has a usable NAFEZA commercial account, Customs Dealer's Card, and e-Token, the next task is not immediate shipping. The importer must turn the intended purchase into an ACI-ready shipment file.

### 1. Freeze the import basis and release route
Before requesting ACID, the Egypt importer, broker, and lawyer should classify each shipment line:
- production line / machinery;
- startup raw materials;
- spare parts;
- finished goods or trade/resale goods;
- samples or company-use goods.

For the factory project, the key question is whether the release route requires:
- IDA import-invoice approval for production lines/equipment;
- IDA import-invoice approval for startup raw materials/production supplies;
- GOEIC production-supplies/needs registration;
- importer-register card for trade/resale imports;
- other agency approvals, certificates, or inspection files for the HS codes.

Do not let the supplier ship until the broker confirms the release route for machines and raw materials separately.

### 2. Pre-check HS codes, descriptions, and documents
The importer should create a pre-clearance matrix:
- HS code;
- Arabic/English item description;
- quantity, net/gross weight, unit, package count;
- country of origin;
- value and currency;
- whether new/used machinery;
- whether the item is raw material, accessory, part, or finished product;
- required certificates or approvals;
- duty/VAT estimate;
- whether the item is covered by IDA/GOEIC production-import basis.

This matrix should be shared with the exporter before final invoice and packing list are issued.

### 3. Coordinate exporter CargoX readiness
The importer must obtain from the exporter:
- CargoX-verified company name and registration details;
- exporter tax/VAT/registration number used in CargoX;
- exact address and country;
- authorized CargoX user contact;
- confirmation that the exporter has enough CargoX units and can submit documents before shipment.

NAFEZA has warned that ACID issuance/release can be blocked where the exporter has not complied with CargoX/ACI rules.

### 4. Prepare proforma/final data for ACID request
In NAFEZA, the importer requests ACID by entering importer/exporter and shipment data. NAFEZA's ACI steps list required data categories including:
- foreign exporter data;
- key shipment data;
- inventory/item data, including customs system, submission system, arrival customs, customs item number, description, origin, statistical quantity, and weight;
- initial bill of lading data, if available;
- invoice data, including invoice/PO number, invoice date, contract type, value, currency, exporter nationality, tariff item, item description, weights, quantities, and item price.

For a first shipment, enter data from a checked proforma invoice and draft packing list, not from informal WhatsApp or spreadsheet descriptions.

### 5. Request ACID before shipment
After key data are complete, the importer requests ACID in NAFEZA.

Planning rule:
- official ACI timing requires cargo data/documents at least 48 hours before shipment from the export country;
- for first shipments, request ACID 7-10 days before planned loading, not at the 48-hour minimum;
- if customs rejects the HS code or ACID application, NAFEZA FAQ states a new application is required.

Once ACID is issued, it is emailed/available to the Egyptian importer and foreign exporter. The importer should immediately send it to the exporter, freight forwarder, shipping line/agent, and broker.

### 6. Ensure ACID appears on all shipment documents
Before loading, the importer must check that the exporter and forwarder put ACID on:
- commercial invoice;
- packing list;
- bill of lading / airway bill;
- certificate of origin where applicable;
- any regulatory certificates or shipping instructions where relevant.

Mismatch between NAFEZA data, CargoX documents, and transport documents can delay or block release.

### 7. Exporter submits CargoX ACI envelope
The importer monitors and confirms:
- invoice and structured invoice data are uploaded through CargoX;
- packing list and other required documents are uploaded;
- documents are sent to the correct ACID;
- documents are visible/accepted in NAFEZA before shipment departs.

Paper documents alone are not sufficient for ACI.

### 8. Pre-arrival customs file and payment planning
Before cargo arrival, the importer/broker should prepare:
- customs declaration strategy;
- duty/VAT/payment method;
- bank import payment file, if payment/FX control is involved;
- original or electronic certificates required for release;
- IDA/GOEIC letters or approvals;
- inspection plan and inland transport to factory.

### 9. Arrival and release
After arrival, the broker uses the NAFEZA/ACI file for customs clearance, inspection, payment, and release. For machinery and raw materials, the importer should make sure the release address and final delivery address match the industrial facility address used in IDA/GOEIC/invoice approvals.

### 5. e-Token / digital signature
NAFEZA requires an electronic signature token for signing/approving electronic documents and transactions.

Steps:
- apply with an ITIDA-licensed provider, such as MCDR, Egypt Trust, El Delta Trust, or Fixed/Fedis Egypt;
- prepare company documents and legal representative ID/passport;
- receive and activate the token;
- link/test the token on NAFEZA;
- issue a separate token/account if more than one person will use NAFEZA.

The person entering/signing pre-shipment data should be the person whose e-signature is used, or a separate signature should be issued for the actual signer.

Dependency:
- For a company electronic seal, ITIDA requires recent commercial registry, valid tax card or ETA taxpayer basic data card, company gazette/articles or contract, and legal representative ID/passport.
- If a delegate attends, ITIDA describes additional delegation requirements with bank-certified signatures.
- For a foreign legal representative, confirm valid passport and residence/work-permit requirements with the provider before booking.

Estimated timing:
- ITIDA states the service is immediate once all required procedures are completed and no second visit is needed for receipt.
- In practice, schedule this as a same-day service after the documents and legal representative/delegate authority are complete.

## Foreign exporter CargoX onboarding

### 1. Account and company profile
Steps:
- create a CargoX account;
- create company profile exactly matching official registry/bank records;
- add registration number and tax/VAT number if available;
- assign user permissions, including ACI envelope permissions.

Dependency:
- Foreign exporters register only on CargoX, not on NAFEZA.
- The company account is created once per company; CargoX says this takes only a few minutes.
- Company name, address, ZIP/postal code, city, country/location, VAT number, and national company registration number should match the official company registry.
- Use an internationally readable English/ASCII format. This is important for Dun & Bradstreet matching and for the Egyptian importer copying the details into NAFEZA.
- If the company already has a CargoX account, do not create a duplicate company account; ask the existing company admin to add the user.

Estimated timing:
- Account creation: a few minutes if email verification works.
- Data cleanup before verification: same day if registry details are clear.
- If company details are changed after verification, CargoX may reset verification and require re-verification.

Pre-check:
- official English company name;
- official registered address in English;
- national company registration number;
- tax/VAT number if applicable;
- DUNS/LEI/EORI if available;
- company bank account name and address as shown on bank wire records.

### 2. Buy CargoX units and bank verification
CargoX company verification starts with bank verification:
- buy CargoX units through platform billing;
- pay by bank wire from the same company's bank account;
- do not pay from a parent company, sister company, trading partner, or personal account.

Dependency:
- First purchase must be by bank wire because bank verification is part of company verification.
- CargoX credits units and marks the company bank-verified only after it receives and matches the bank payment.
- The payer information must match the CargoX company details. Mismatches are a common reason for verification failure.
- For SWIFT payments, CargoX recommends SHA fee option and notes that intermediary bank fees can reduce the amount CargoX receives. Buy extra units if timing matters.

Estimated timing:
- SEPA EUR payment: up to 3 business days.
- International USD SWIFT payment: up to 5-7 business days.
- For China/Hong Kong suppliers using SWIFT, plan around the 5-7 business day window unless the bank confirms faster settlement.

Minimum first purchase logic:
- Verification requires 15 units.
- A typical sea ACI filing costs 175 units: 160 filing + up to 15 document transfer.
- A typical air ACI filing costs 95 units during the current reduced-price period: 80 filing + up to 15 document transfer.
- First sea shipment should therefore buy at least 190 units if one wants to cover verification plus one sea ACI filing, and preferably more to absorb SWIFT fee shortfalls or refiling.

### 3. Third-party verification
After bank verification:
- initiate third-party verification;
- CargoX uses Dun & Bradstreet to match company name, address, registration number, and tax/VAT number;
- verification costs 15 units according to CargoX's checked help page;
- changing company name, address, registration number, or tax/VAT number can void verification and require re-verification.

Dependency:
- Can only start after bank verification is complete and units are available.
- Details in CargoX must match official registry records.
- If the first attempt fails, correct CargoX company details and try again after the change is activated.
- If the second attempt fails, CargoX asks for an official government-issued company document showing company name, address, registration number, and tax number if applicable. The document must be in English or translated into English by a court-appointed judicial translator or notary.

Estimated timing:
- If data matches: CargoX says results appear within a few seconds.
- If data fails: same-day correction may be possible, but manual document review is not a guaranteed same-day path. Treat it as a multi-day risk.

### 4. Share exporter details with importer
Exporter should copy company details from CargoX and send them to the Egyptian importer. The importer uses this data in NAFEZA to request ACID.

Dependency:
- Company must be verified before the importer can complete a usable ACI/ACID process.
- Exporter should use CargoX's "Copy company details" function, not a manually typed email, to reduce mismatch risk.
- Egyptian importer should enter the exporter details in NAFEZA exactly as received.

Estimated timing:
- Same day after verification.

### 5. Blockchain key and signing readiness
CargoX requires an active blockchain key to perform blockchain actions such as sending documents in envelopes.

Steps:
- create or link the first user's blockchain key;
- store the key file/text and password securely;
- confirm the key is active;
- if adding extra users, have an existing authorized user approve their blockchain keys;
- make sure the user who will submit ACI has both an active key and ACI envelope transfer permission.

Dependency:
- Account setup can be started without creating the blockchain key, but ACI filing transfer cannot be completed without digital signing readiness.
- Never share the key file or password between staff.

Estimated timing:
- Same day if the first account admin is available.
- Additional users may be delayed if no existing admin/key manager is available to approve their keys.

### 6. ACI envelope permissions and user structure
CargoX ACI filing requires the right company/user permissions.

Minimum roles:
- one administrator/legal representative who can manage company details and accept terms;
- one finance user who can buy units;
- one operations user who can create/upload ACI documents;
- one authorized user who can transfer ACI envelopes and sign with an active blockchain key.

Dependency:
- With a Basic/free setup, CargoX indicates users may be broad administrators by default; with a Standard plan there are granular permissions.
- If a freight forwarder will file on behalf of the exporter, the delegation/representative path must be set up before shipment.

Estimated timing:
- Same day if the company admin is available.
- Do not wait until ACID is issued to discover the operating user cannot transfer ACI envelopes.

### 7. Receive ACID notification
After the Egyptian importer registers the shipment in NAFEZA using exporter details, the exporter receives an ACI notification containing ACID and shipment data in CargoX and by email.

Dependency:
- Egyptian importer must have active NAFEZA access and must enter the verified CargoX exporter details.
- Exporter should compare ACID notification data against invoice, packing list, and booking details before filing.

Estimated timing:
- After NAFEZA approves/returns the ACID. No CargoX-side fixed SLA; the timing depends on NAFEZA/importer data.

### 8. Prepare and upload shipment documents
The exporter uploads documents into the Egypt ACI envelope.

Usually required:
- bill of lading copy or air waybill copy;
- packing list PDF;
- commercial invoice PDF;
- commercial invoice in NAFEZA structured XML or Excel format;
- certificate of origin PDF.

Rules:
- each document must be uploaded separately;
- document type must be correct;
- do not merge multiple invoices or certificates into one file;
- per-document size limit is 5 MB;
- Egypt ACI envelope limit is 100 MB;
- invoice must include importer and exporter tax/VAT IDs where applicable and match NAFEZA data.

Dependency:
- Final invoice data must match the data the importer used in NAFEZA.
- BL/AWB copy may depend on freight forwarder/carrier issuing draft transport document.
- Certificates may require external lead time before CargoX filing.

Estimated timing:
- Upload itself: same day.
- Document preparation: depends on certificate of origin, inspection, fumigation/MSDS/testing requirements. For first shipment, pre-clear the document list before booking.

### 9. Seal, transfer, and digitally sign the ACI envelope
Steps:
- open the ACI notification or manually compose Egypt ACI envelope with ACID;
- upload/choose documents;
- fill mandatory document properties;
- save properties;
- seal the envelope;
- transfer the envelope;
- digitally sign with blockchain key;
- verify sent status in Sent folder.

Dependency:
- Envelope can only be sealed when mandatory fields are filled.
- Promotional units cannot be used for Egypt ACI filings.
- Enough paid units must be available.

Estimated timing:
- Same day if documents, units, permissions, and blockchain key are ready.
- Base control: file before goods leave the export country, not after sailing.

### 10. Refile missing or invalid documents
If the ACI envelope was already sent, CargoX states there is no recall/undo. Corrections are made by composing a new Egypt ACI envelope under the same ACID.

Cost/timing:
- The ACI filing fee is not charged again for the same ACID.
- Document transfer fee may apply, 3 units per document capped at 15 units per ACID.
- Same day if corrected documents are ready and units are available.

Failure modes:
- wrong ACID;
- exporter identity mismatch;
- invoice mismatch between CargoX and NAFEZA;
- missing structured invoice;
- document type wrong;
- insufficient units;
- inactive blockchain key or missing transfer permission.

## Per-shipment ACI/ACID workflow

### Before requesting ACID
Prepare:
- pro forma/commercial invoice data;
- exporter legal name, address, registration number, tax/VAT number, CargoX details;
- importer tax ID and NAFEZA identity;
- HS codes and item descriptions;
- origin country;
- invoice number/date/value/currency;
- gross/net weight, package count, statistical quantity;
- port/airport of loading and arrival;
- carrier/shipping line/airline and forwarder details;
- draft bill of lading or air waybill data if available.

### ACID request in NAFEZA
The Egyptian importer logs into NAFEZA and enters:
- exporter data;
- key shipment data;
- inventory/item data;
- initial bill of lading or air waybill data if available;
- invoice data and invoice item data.

NAFEZA then emails/sends the ACID to importer and exporter if approved.

### CargoX filing
Exporter must:
- open the ACI notification in CargoX, or compose Egypt ACI envelope manually with the ACID;
- upload required documents as separate files;
- set document types and mandatory fields;
- validate/use the NAFEZA structured invoice format;
- seal the envelope;
- transfer and digitally sign the envelope.

## Documents for first shipment
Usually required:
- commercial invoice PDF;
- structured commercial invoice in NAFEZA Excel/XML format;
- packing list PDF;
- bill of lading copy for sea or air waybill copy for air;
- certificate of origin PDF.

Possible additional documents:
- bill of materials;
- certificate of analysis;
- fumigation certificate;
- inspection certificate;
- insurance certificate;
- delivery note;
- EUR.1 movement certificate;
- halal certificate;
- health certificate;
- MSDS;
- phytosanitary certificate;
- veterinary certificate;
- other cargo-specific documents.

CargoX states that documents must be uploaded separately with correct document type, not merged into one file. Per-document max is 5 MB and ACI envelope max is 100 MB.

## Timing rules
- Sea ACI is mandatory and cargo data/documents should be submitted at least 48 hours before shipment from export country.
- Air ACI is mandatory from 2026-01-01 according to NAFEZA/CargoX pages.
- ACID must be obtained before ACI envelope filing and before shipment.
- Exporter CargoX verification should be completed before the importer tries to request a usable ACID.
- For first shipment, start onboarding at least 2-3 weeks before planned shipment; the official sources do not guarantee a single fixed timeline for all registrations.

## Cost assumptions
CargoX checked pricing:
- sea ACI filing: 160 units per ACID;
- air ACI filing: 80 units per ACID from 2026-01-01 to 2026-06-30;
- document transfer: 3 units per document, capped at 15 units per ACID envelope;
- company verification: 15 units for the third-party verification step, plus units purchased for bank verification.

Other costs to budget:
- e-Token/e-signature provider fees;
- NAFEZA/logistics center or service fees if applicable;
- GOEIC/customs dealer/import or production-supplies registration costs;
- broker service fee;
- certificates of origin, inspection, fumigation/MSDS/testing/certification as needed;
- duty, VAT, port, storage, demurrage, and inspection charges.

## First-shipment control points
- Run a dry run with broker before goods leave China.
- Do not ship until ACID is valid and visible to all parties.
- Make invoice, NAFEZA entry, CargoX invoice, packing list, and transport document match exactly.
- Put ACID on bill of lading/air waybill where required by the carrier/NAFEZA process.
- Ask broker to pre-check HS codes, permits, standards, and certificate requirements.
- Keep shipment small for the first pilot if possible.

## Sources
- NAFEZA, "Advance Cargo Information System": https://www.nafeza.gov.eg/en/pages/15
- NAFEZA, "Advance Cargo Information System (Aviation)": https://www.nafeza.gov.eg/en/pages/39
- NAFEZA, "Advance Cargo Information (ACI) Phase 1 Steps": https://www.nafeza.gov.eg/en/pages/16
- NAFEZA, "Documents required to create an ACI file": https://www.nafeza.gov.eg/en/pages/32
- NAFEZA, "Digital Signature": https://nafeza.gov.eg/en/pages/17
- NAFEZA FAQ, importer registration documents: https://www.nafeza.gov.eg/en/faq/%D9%87%D9%84%20%D9%87%D9%86%D8%A7%D9%83%20%D9%85%D8%B3%D8%AA%D9%86%D8%AF%D8%A7%D8%AA%20%D9%84%D9%84%D8%AF%D9%84%D8%A7%D9%84%D8%A9%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D9%88%D8%B1%D8%AF%20%D8%9F/57
- NAFEZA FAQ, e-Token providers: https://www.nafeza.gov.eg/en/faq/Where%20can%20I%20get%20the%20e-Token%20and%20the%20names%20of%20the%20companies%20that%20deal%20with%20it/70
- ITIDA, digital signature and electronic seal: https://www.itida.gov.eg/English/Pages/E-Signature.aspx
- CargoX, "About Egypt ACI": https://cargox.help/en/articles/418312-about-egypt-aci
- CargoX, "Company verification": https://cargox.help/en/articles/398290-company-verification
- CargoX, "Process of acquiring the ACID number": https://cargox.help/en/articles/398403-process-of-acquiring-the-acid-number
- CargoX, "How to compose and send an ACI envelope": https://cargox.help/en/articles/398404-how-to-compose-and-send-an-aci-envelope
- CargoX, "Required documents and formats": https://cargox.help/en/articles/398410-required-documents-and-formats
- CargoX, "Egypt ACI pricing": https://cargox.help/en/articles/398409-egypt-aci-pricing
- GOEIC, "Importers": https://www.goeic.gov.eg/en/pages/default/view/id/185/m/6-114
- GOEIC, "Production Supplies": https://www.goeic.gov.eg/en/pages/default/view/id/188/m/6-117
- Egyptian Customs, trader registration procedures: https://custom-web.azurewebsites.net/Legislations/Procedures/Registration_Licensing
