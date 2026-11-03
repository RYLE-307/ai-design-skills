---
name: dashboard-design
description: "Design analytical dashboards for metrics, trends, comparisons and drill-down decisions. Use when the main task is understanding data; live incident response belongs to monitoring-ui."
license: MIT
---

# Dashboard design

Read [design-core](../design-core/SKILL.md) once. Own metric meaning, visual encoding, analytical controls and drill-down, not the whole app shell.

## Start with decisions

Identify who reads the dashboard, which decision they make, the relevant time horizon and what action follows an unusual result. Put a few decision-relevant metrics first; do not fill a grid with arbitrary counters. Separate summary, explanation and underlying records.

For each metric establish: definition, unit, aggregation, population/denominator, date window, timezone, source and freshness. If unknown, label the assumption or request the definition. A number without a denominator or time window can be actively misleading.

## Encode the question

| Question | Usually useful | Avoid |
|---|---|---|
| How did it change over time? | Line chart with time axis and explicit gaps | Connecting missing samples as known values |
| How do categories compare? | Sorted bars with a common baseline | Truncated bar axes and decorative 3D |
| What is the distribution? | Histogram, box plot or percentile view | Reporting an average as if it described everyone |
| What makes up a total? | Stacked bars or a small labeled part-to-whole chart | Many tiny slices or totals that do not reconcile |
| Which exact records need action? | Ranked table or exception list | A chart that hides object identity |

Show units, axis labels and comparable scales. Explain a nonzero line-chart baseline when needed; bars normally start at zero. Use stable color meanings and labels, not color alone. Provide a readable summary and a table/text alternative for important chart values; hover must not be the only access method.

## Filter and compare honestly

- Keep date range and scope visible. State timezone, include/exclude rules and whether the current interval is incomplete.
- Compare equivalent windows and cohorts. Show the baseline and whether change is absolute, relative percentage or percentage points. Handle a zero baseline without infinity or fake growth.
- Separate no data, zero, missing, partial and stale. A failed source must not become a row of zeros.
- Keep global and local filters distinguishable, reflect active filters, and offer reset. Preserve shareable state in the URL when appropriate.
- Prevent races between filter requests. Show refreshing state while retaining valid data; do not mix charts from different filter versions without marking the difference.
- Make drill-down retain the originating filters/time range and provide a return path. Use [data-table-design](../data-table-design/SKILL.md) for substantial record views.

## Adapt to the screen

Order mobile content by decision value, not desktop coordinates. Reduce tick density and secondary series rather than shrinking chart labels. Keep legends, range controls and summaries usable. Choose aggregation appropriate to the window and data volume; do not silently change the meaning of a metric for performance.

## Acceptance walkthrough

Use a known fixture and check displayed totals against it. Change dates and segments, compare periods, inspect a spike and drill into its records. Exercise zero, missing samples, partial current period, failed source and stale data. Verify keyboard access to controls and important values, and readable mobile charts. State which metric definitions were supplied and which remain assumptions.
