---
name: admin-panel-design
description: "Design privileged management interfaces for users, roles, resources, moderation and CRUD operations. Use when permissions, destructive changes and administrative auditability shape the workflow."
license: MIT
---

# Admin panel design

Read [design-core](../design-core/SKILL.md) once. Own administrative intent, permissions and consequences. Add [web-app-design](../web-app-design/SKILL.md) only for a new shell, [data-table-design](../data-table-design/SKILL.md) for record lists and [forms-settings](../forms-settings/SKILL.md) for editors.

## Define authority and scope

Map actor → resource → allowed action → affected scope. Distinguish workspace and global administration. Show the active tenant clearly before a consequential operation. Identify view-only, editor and owner/admin capabilities using the real permission model, not guessed roles.

Hiding a button is not authorization. Integrate server enforcement when backend work is in scope; otherwise identify that dependency and keep prototype restrictions explicit. Avoid revealing restricted row data, counts, exports or error details.

## Resource lifecycle

Choose appropriate create, inspect, edit, archive, restore and delete paths. Separate reversible archival from permanent deletion. Keep stable object identity in detail views, and show dependencies that block an action. Do not assume every resource needs every CRUD operation.

Put frequent safe actions near their records. Move rare dangerous actions into a labeled area without making them undiscoverable. Do not rely on red color alone. An unavailable action should explain how to proceed when that explanation does not reveal private information.

## Consequential operations

- Before deletion, role changes, bulk edits or access revocation, summarize objects, tenant, scope and meaningful consequences. Use stronger confirmation for irreversible/high-impact work; avoid typing rituals for ordinary reversible actions.
- Preserve required owners and handle self-demotion or self-removal explicitly according to product policy. Do not invent the policy when it matters.
- Distinguish invitation sent, pending, accepted, expired and revoked. Do not imply a successful invitation before the server confirms it.
- Bulk operations show eligible/ineligible counts, pending progress, per-item failures and retry of failed items. Avoid rerunning successful destructive operations.
- Handle stale versions: explain conflict and offer reload/review rather than overwriting another administrator's changes.
- Provide useful audit context where supported: actor, action, target, timestamp/timezone and outcome. Do not fabricate an audit log or expose secrets in it.

## Acceptance walkthrough

Run the same task as a permitted role and a restricted role. Create or invite, edit, cancel, and perform a permitted reversible operation. Check forbidden access, expired invitation, last-owner/self-removal edge where applicable, stale edits and a bulk operation with partial failure. Ensure confirmation names the actual scope and cancellation has no side effect. Treat missing server authorization as an unresolved dependency, not a passed UI test.
