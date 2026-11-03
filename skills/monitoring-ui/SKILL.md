---
name: monitoring-ui
description: "Design operational monitoring screens for service health, alerts, incidents and live logs. Use for current-state triage and response, including freshness and connection failures."
license: MIT
---

# Monitoring UI

Read [design-core](../design-core/SKILL.md) once. Own operational truth and response flow. Use [dashboard-design](../dashboard-design/SKILL.md) for analytical chart decisions and [data-table-design](../data-table-design/SKILL.md) for substantial incident/log lists.

## Make operational meaning explicit

Identify the operator, service scope, environment/region, expected update cadence and the decision after an alert. Separate current health, historical performance and incident lifecycle. Acknowledged does not mean resolved; no telemetry does not mean healthy; muted does not mean fixed.

Define status vocabulary from the actual system: healthy, degraded, failed, unknown, maintenance, for example. Pair status colors with text/symbols. Show severity, affected scope, start time, last observation and owner/escalation path where available. Rank by actionable impact, not just most recent timestamp.

## Freshness and live updates

- Show last successful observation and timezone, plus connection state. Define when data becomes stale from the source's cadence or SLA; do not invent a universal threshold.
- Distinguish transport connected from telemetry fresh. A heartbeat can succeed while a source stops emitting data.
- Preserve last-known values with a stale/unknown marker during disconnects; do not turn missing samples into zero or an all-green screen.
- Specify pause/resume and manual refresh behavior. Pausing the display must not imply the source stopped collecting. Show how far behind the paused view is.
- Keep focused/selected rows stable during updates. Buffer incoming items and offer “new events” when reordering would disrupt reading. Do not move focus or announce every streamed sample.
- Reconnect with bounded backoff and a visible retry path; clean up polling/streams on navigation. Reconcile duplicates and out-of-order events using stable IDs and timestamps. Show gaps rather than hiding missed intervals.

## Triage to action

Support overview → affected service → correlated incident/logs → appropriate action → verified outcome. Keep environment, time window and filters across drill-down. Show alert source and threshold/duration when known so operators can assess meaning.

Acknowledgment, assignment, mute/snooze, resolution and destructive remediation are separate operations. Mutes show scope, duration and expiry. Permission-check operational actions and display pending/failure honestly; never claim remediation succeeded just because a button was clicked. Use confirmation appropriate to impact and show the target environment.

For logs, provide time range, level/service filters, search and a follow-tail toggle. Preserve scroll when follow-tail is off and indicate unread events. Wrap or horizontally scroll long lines without blowing out the page; support copying relevant content with secrets redacted according to product rules.

## Attention and accessibility

Use restrained alerts so critical events stand out. Avoid flashing dashboards, auto-playing sounds and constant whole-screen animation. For wallboards, increase viewing-distance legibility; for operators, preserve dense but readable controls. Announce meaningful summarized status changes rather than saturating live regions. Keep pause and scope controls accessible on narrow screens.

## Acceptance walkthrough

Exercise healthy → degraded → acknowledged → resolved using known fixture transitions. Disconnect the feed, exceed the stale threshold, reconnect with duplicate/out-of-order events, then pause/resume while reading a log. Confirm unknown never appears healthy, timestamps and selected scope survive drill-down, focus does not jump, and failed mute/remediation remains visibly unsuccessful. Report simulated transitions separately from verified live integrations.
