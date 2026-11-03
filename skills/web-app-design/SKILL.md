---
name: web-app-design
description: "Design task-focused SaaS workspaces, editors, inboxes and daily-use product screens, including navigation and master-detail flows. Use for application work, not public marketing pages."
license: MIT
---

# Web app design

Read [design-core](../design-core/SKILL.md) once. Own the working flow and app shell; leave charts, tables, forms, administration and operations to the relevant specialists when those areas are in scope.

## Task first

Describe the main loop: locate an object → inspect or edit it → act → understand the result. Identify the active workspace/account, object identity, user role, task frequency and information required before action. A workspace is not a marketing page: useful work should occupy the main area, without a hero, testimonials or unrelated KPI tiles.

Choose the least complex structure that supports that loop:

| Pattern | Fits | Watch for |
|---|---|---|
| List and detail | Inbox, runs, tickets, documents | Preserve list filters, selection and scroll after closing detail |
| Focused editor | Writing, automation, configuration | Save state, history and a clear way back; avoid competing primary actions |
| Board | Work moves through meaningful stages | Provide a non-drag move action and useful list alternative |
| Single task page | Infrequent linear work | Do not add a sidebar merely to look like SaaS |

## Shell and navigation

- Group navigation by user goals, not internal services. Show current location and active workspace. Distinguish navigation, filters and local tabs.
- Reuse an existing shell. For a new one, choose sidebar, top navigation or a focused layout based on section count, density and device use; none is mandatory.
- Put page title, scope, local controls and the primary action in a stable hierarchy. Keep global controls from competing with record actions.
- Represent shareable object/filter state in the URL when useful, without secrets. Browser back should restore a useful context. Preserve local drafts independently of transient filters.

## Working behavior

Make selection, editing, saving and execution distinct. Show whether a change is local, saving, saved or failed. Resolve stale async responses so an old request cannot overwrite a newer selection. Clean up subscriptions on navigation.

For editors, decide explicit save versus autosave and explain the choice in the UI. Warn before losing dirty work when needed. Offer a deliberate conflict path if another user changed the object. Do not quietly replace newer server data with an old draft.

For long-running operations, show queued/running/completed/failed states with operation identity; support cancellation only if the service can honor it. Optimistic UI needs rollback and reconciliation, not a success toast alone.

On mobile, a master-detail split usually becomes a sequence. Preserve the selected object and return path. Move secondary tools into accessible disclosure without hiding the main action. A canvas needs zoom/pan controls and a non-spatial way to inspect essential objects when feasible.

## Apply supporting skills only where needed

- Record-heavy lists: [data-table-design](../data-table-design/SKILL.md).
- Settings or substantial editing forms: [forms-settings](../forms-settings/SKILL.md).
- Privileged resource management: [admin-panel-design](../admin-panel-design/SKILL.md).
- Analytical overview: [dashboard-design](../dashboard-design/SKILL.md).
- Live operations: [monitoring-ui](../monitoring-ui/SKILL.md).

## Acceptance walkthrough

Open the workspace, find a specific object, inspect it, perform its main action and return to the same context. Repeat with no objects, a failed request, a read-only role and narrow layout. Verify browser back, unsaved work, focus restoration and an async response arriving after selection changes. Report the implemented flow and any missing backend behavior, not just the shell's appearance.
