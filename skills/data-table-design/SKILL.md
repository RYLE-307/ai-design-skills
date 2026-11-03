---
name: data-table-design
description: "Design data-heavy record lists and tables with filtering, sorting, pagination, selection, bulk actions and responsive behavior. Use for record comparison and operations, not decorative pricing tables."
license: MIT
---

# Data table design

Read [design-core](../design-core/SKILL.md) once. Own record finding, comparison, selection and list-state semantics. Use [admin-panel-design](../admin-panel-design/SKILL.md) only when actions are privileged.

## Start with the records and tasks

Identify stable row IDs, the fields needed for decisions, likely row count, sort/filter capabilities, and allowed row/bulk actions. Choose a list when comparison across columns is unnecessary. Do not make a grid simply because the data came from a database.

Put identifying fields first, then decision-critical fields, then secondary metadata/actions. Align numbers consistently, include units, and format dates/numbers for the product locale. Provide access to full truncated values by keyboard as well as pointer. Keep action labels unambiguous for each record.

## Define the interaction contract

- Sorting must be stable and expose direction (`aria-sort` on the relevant header). State default sort and tie handling where it affects predictability. Avoid client-only sorting of one page when users expect the entire dataset.
- Filtering has visible active values, result count when known and clear reset. Distinguish full-text search from field filters. Debounce only when useful; cancel or ignore stale responses.
- Choose server/client pagination based on the data contract and scale. Do not fabricate totals for cursor-based data. Reset or clamp pagination when filters change or records disappear.
- Persist useful view state in the URL or established preference mechanism. Do not put sensitive query contents in shareable URLs.
- Use a semantic table with headers for tabular data. Sorting controls are buttons. Use an ARIA grid only when spreadsheet-style interaction is required and its complete keyboard model is implemented.

## Selection must have a precise scope

Distinguish “select this row”, “select this page” and “select all matching results”. State the count and scope next to bulk actions. Use indeterminate state for a partly selected page. Keep selection by stable ID, never row index.

Decide what happens across pagination and filters. Safe default: retain across pages for the same query, clear on a changed query with feedback; a different policy must be explicit. For server-side “all matching”, use a query snapshot/exclusion model the backend supports, not just the currently loaded IDs. Confirm the actual scope before consequential actions.

After an operation, show successful and failed items, keep useful context, and retry only failures. Revalidate eligibility/permissions on the server. If selected rows disappear or change eligibility, reconcile the selection visibly.

## Scale, states and mobile

Use pagination before adding virtualization unless the task calls for continuous navigation through large lists. Virtualization must preserve accessible names, focus and row identity; validate it with the actual assistive technology support available. Do not assume rendering fewer rows automatically preserves table semantics.

Initial empty, filtered empty, loading, refresh, failure and stale data have different meanings; follow core's contract. Keep column geometry stable while refreshing. A failed filter request must not show old rows as if they matched the new filter.

On narrow screens choose prioritized columns, accessible row details, a list transformation or a labeled contained scroll region. Never hide the identifying field or main action without another path. Sticky headers/columns must not cover focused controls or make zoom unusable.

## Acceptance walkthrough

Find a record via search, sort, filter, change page, inspect details and return. Select across pages, change the query and verify the stated policy. Test partial bulk failure, deletion of the last row on a page, long names, unknown total and an empty result. Check keyboard sorting, checkbox labels, full-value access, mobile overflow and selection consistency after refresh.
