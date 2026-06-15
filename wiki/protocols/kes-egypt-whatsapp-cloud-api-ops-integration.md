---
type: protocol
status: active
created: 2026-05-22
updated: 2026-05-22
tags: [kes, egypt, whatsapp, cloud-api, ops, crm, ecommerce]
domain: ecommerce
domains: [ecommerce, operations, crm, whatsapp, egypt, kes, sales]
source_count: 5
confidence: medium
review_cycle: monthly
verification_status: spot-checked
related:
  - ../syntheses/kes-egypt-ecommerce-entry-strategy-2026-05-22.md
---

# KES Egypt WhatsApp Cloud API to Ops Integration Protocol

## Purpose

Implement a WhatsApp Business Platform / Cloud API channel for the KES Egypt operation, from phone-number preparation to ops-system integration.

The goal is not a chatbot-first system. The first production version should create a reliable sales inbox that captures WhatsApp leads into ops, supports human replies, records quote/order context, and sends a small set of utility templates.

## Phase 0 - Decide the number strategy

Use a dedicated Egypt business number for the API channel.

Requirements:
- controlled by the company, not a personal staff number;
- able to receive SMS or voice verification during setup;
- not reused for ordinary WhatsApp unless intentionally migrating or using an officially supported coexistence path;
- printed consistently on catalog, cards, showroom, website, social pages, and ads.

Recommended structure:
- one public sales number for Egypt inbound sales;
- later, separate project/B2B number only if volume or team separation requires it.

Avoid:
- using a personal number as the API number;
- using a number that cannot be recovered if a staff member leaves;
- spreading customers across many unmanaged numbers.

## Phase 1 - Business and Meta setup

Prepare:
- Meta Business Portfolio / Business Manager;
- Egypt company legal name, address, website or landing page, email, and documents;
- Facebook Page and Instagram account if they will be used for click-to-WhatsApp ads;
- payment method for WhatsApp Business Platform billing;
- admin access policy: at least two company-controlled admins.

Steps:
1. Create or confirm the Meta Business Portfolio.
2. Add company assets: Facebook Page, Instagram, domain, ad account if relevant.
3. Complete business verification if required for production scale, display-name confidence, or higher messaging limits.
4. Create a Meta Developer app with WhatsApp enabled.
5. Create or attach a WhatsApp Business Account.

## Phase 2 - Cloud API test environment

Use Meta's temporary test number first.

This phase can be done from Hong Kong before the Egypt company phone number is ready. The test sender number is provided by Meta, and the recipient can be Kenny's Hong Kong WhatsApp number or another verified test recipient added in the Meta Developer console.

Minimum test:
- send a text message to an allowed recipient;
- receive an inbound message via webhook;
- receive delivery/read status webhooks;
- send one image or document;
- send the default test template.

Do not add the real public number until webhook and logging are working.

Execution steps:
1. Create a Meta Developer account or use an existing company-controlled Meta login.
2. Create a Meta Developer app.
3. Add the WhatsApp product.
4. Select or create a Meta Business Account.
5. Open `WhatsApp > API Setup` or `WhatsApp > Quickstart`.
6. Copy the temporary access token, test sender phone number, phone number ID, and WABA ID.
7. Add a personal WhatsApp number as a test recipient and complete OTP verification.
8. Send the first test message from Meta's console.
9. Create a public HTTPS webhook endpoint in the ops staging environment.
10. Configure the callback URL and verify token in the Meta app.
11. Subscribe the app to WhatsApp message events.
12. Reply from the test recipient's WhatsApp app and confirm the inbound webhook appears in ops logs.
13. Send a reply from ops through Cloud API and confirm delivery in WhatsApp.
14. Store message IDs and update message statuses from webhook callbacks.

## Phase 3 - Production phone number onboarding

Add the dedicated phone number to the WhatsApp Business Account.

Production setup checklist:
- display name submitted and approved;
- business profile set: name, description, address, email, website, vertical;
- two-step verification PIN stored securely;
- phone number ID and WABA ID recorded in secrets / ops configuration;
- access token generated through a system user, not a personal user token;
- webhook subscribed to the relevant WABA events.

Important number rule:
- if the number is already used in WhatsApp or WhatsApp Business App, plan the migration carefully; do not assume chat history and app behavior will transfer cleanly into the API channel.

## Phase 4 - Ops data model

The ops system needs five core objects.

1. WhatsApp contact
- wa_id;
- phone number;
- display name from webhook when available;
- language preference;
- source channel;
- consent / opt-in evidence if marketing is planned.

2. Conversation
- contact_id;
- channel = whatsapp;
- phone_number_id;
- open / pending / closed status;
- assigned agent;
- last customer message time;
- 24-hour service-window state;
- last message category.

3. Message
- Meta message ID;
- direction: inbound / outbound;
- type: text, image, document, template, interactive;
- body / media reference;
- status: sent, delivered, read, failed;
- timestamp;
- raw payload reference for audit.

4. Lead / quote
- source keyword or campaign;
- category: curtains, curtain hardware, bathroom hardware, project, B2B;
- room/window dimensions or requested SKU;
- budget band;
- next action;
- lost reason if not converted.

5. Order / appointment
- quote ID;
- order status;
- measurement appointment;
- installation appointment;
- payment status;
- delivery status;
- after-sales notes.

## Phase 5 - Webhook and API implementation

Inbound webhook:
- verify GET challenge from Meta;
- validate request signature;
- parse messages and statuses;
- deduplicate by message ID;
- store raw payload before business logic;
- create/update contact;
- open/update conversation;
- create lead when the first message includes a source keyword or product intent.

Outbound API:
- send free-form replies inside the customer-service window;
- block free-form replies outside the window and require an approved template;
- support text, image, document, and template messages in v1;
- record outbound messages before sending and update status by webhook;
- expose failure reason to agent.

Security:
- system-user token stored in a secret manager;
- webhook verify token not reused elsewhere;
- role-based access in ops;
- audit log for agent replies and template sends;
- no personal admin token in production.

## Phase 6 - Agent inbox

First version inbox requirements:
- conversation list by status and assigned agent;
- customer profile panel;
- lead / quote fields beside the chat;
- quick replies for common questions;
- template sender for approved templates;
- media upload for quote sheets, photos, and installation examples;
- handoff / assign / close actions;
- lost-reason capture.

Do not build a complex chatbot first. Use human agents and structured data capture.

## Phase 7 - Template plan

Start with utility templates, not marketing templates.

Initial templates:
- quote received confirmation;
- measurement appointment confirmation;
- appointment reminder;
- order confirmation;
- delivery / installation schedule confirmation;
- after-installation follow-up;
- payment received confirmation if relevant.

Languages:
- Arabic first for Egypt customers;
- English version for expat / B2B / international customers.

Marketing templates should wait until opt-in, segmentation, and economics are proven.

## Phase 8 - Attribution and entry points

Every entry point should include a source keyword.

Examples:
- `IG_CURTAIN_01`
- `NOON_TRACK_01`
- `SHOWROOM_QR`
- `B2B_DECORATOR`
- `FB_AD_BLACKOUT`

Entry points:
- website WhatsApp button;
- Facebook Page CTA;
- Instagram profile link;
- QR code on sample cards;
- marketplace insert cards if allowed by platform policy;
- Click-to-WhatsApp ads.

Ops should store the first source keyword and the latest campaign keyword separately.

## Phase 9 - Go-live gates

Do not go live until:
- webhook receive/send works in staging;
- production number can send and receive messages;
- message status updates are stored;
- at least three utility templates are approved;
- support agents can reply from ops;
- failed-message cases are visible;
- daily backup/export exists for conversations and leads;
- admin access is controlled by company accounts.

## Phase 10 - Metrics

Daily:
- inbound conversations;
- source split;
- first response time;
- quote requests;
- appointments booked;
- orders;
- lost reasons;
- failed outbound messages.

Weekly:
- conversion by source;
- conversion by category;
- average response time;
- quote-to-order conversion;
- top customer questions;
- template send volume and cost;
- after-sales / complaint rate.

## Recommended first release

Build:
- inbound webhook capture;
- agent inbox;
- manual human replies;
- contact / lead / quote creation;
- utility template sender;
- source keyword tracking.

Defer:
- chatbot automation;
- marketing broadcasts;
- product catalog sync;
- payment collection inside WhatsApp;
- advanced routing;
- AI sales assistant.

## Sources

- [WhatsApp Business Platform](https://whatsappbusiness.com/products/business-platform/)
- [WhatsApp Business Platform Pricing](https://whatsappbusiness.com/products/platform-pricing/)
- [WhatsApp Business App](https://whatsappbusiness.com/products/business-app/)
- [Meta Developers WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)
- [Meta Developers WhatsApp Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/)
