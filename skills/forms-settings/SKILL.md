---
name: forms-settings
description: "Design data entry, onboarding, authentication, preferences and settings forms with validation, save behavior and recovery. Use for form flows or targeted input improvements."
license: MIT
---

# Forms and settings

Read [design-core](../design-core/SKILL.md) once. Own input structure, validation and saving. Preserve the existing screen shell for a local form change.

## Design the information contract

List the data needed, why it is needed, defaults, optional fields and dependencies. Remove unnecessary collection. Group fields by the user's mental model, not a database schema. Use a single column for ordinary entry; place short related inputs together only when reading order stays clear. Use multiple steps only when they reduce meaningful complexity; preserve progress and provide a review step for consequential submissions.

Persistent visible labels explain the field. Examples and constraints belong in associated help text, not placeholder-only labels. Mark optional/required fields consistently. Choose native control semantics and appropriate input type, autocomplete and mobile keyboard. Keep a text alternative for custom date/picker controls.

## Validation without lost work

- Validate at a helpful moment, usually after interaction or submission; avoid accusing users while they are still typing. Clear obsolete errors when corrected.
- Treat client validation as assistance. Map authoritative server errors back to fields or a form-level error. For multiple failures, use an error summary linking to fields and move focus appropriately after submission.
- Say what to fix, include the constraint, and associate errors programmatically. Never rely solely on red borders.
- Preserve entered values after failure, including hidden-step state where appropriate. Do not persist passwords or sensitive fields in browser storage. Do not repopulate secrets returned from a backend.
- Handle async validation races; a stale response must not invalidate a newer value. State when uniqueness or availability can only be confirmed at save time.

## Saving and settings

Choose explicit save for grouped/important changes; choose autosave for independent low-risk preferences when undo or recovery is available. Show dirty, saving, saved and failed states accurately. Avoid a switch that looks saved while a request has failed.

Prevent duplicate submissions and keep pending status readable. Save buttons reflect meaningful dirty/valid state, with an explanation for unavailable actions when needed. On success keep a useful location; on failure retain the draft and retry path. Warn before leaving unsaved changes when needed, including in-app navigation. Handle version conflicts deliberately rather than silently overwriting.

Separate user preferences, workspace policy and privileged settings. Explain inherited/locked values and who can change them. Distinguish “reset this field”, “discard unsaved edits” and “restore defaults”; show the affected scope.

For authentication, allow paste and password managers, offer show/hide with an accessible label, support expired/reused links and session timeout recovery. Use generic account-existence responses where the product requires privacy. Do not add a memory puzzle as the only authentication path.

For payment/account deletion or other consequential settings, show a clear review of the effect and follow the product's authorization requirements. A mock submit must visibly identify itself as a demo, not claim to charge or update a real account.

## Acceptance walkthrough

Complete the form with keyboard and mobile input. Try missing fields, invalid input, a slow request, server rejection, duplicate submit and retry. Navigate away with a draft, return after success, and test an async response arriving after a value changes. Confirm focus, field associations and preserved input. Check long translated labels and the narrow layout. Add conflict, reset, expired-session or multi-step recovery checks when those behaviors exist.
