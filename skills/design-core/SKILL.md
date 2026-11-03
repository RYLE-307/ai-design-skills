---
name: design-core
description: "Establish shared UX, visual direction, accessibility, responsive behavior and implementation checks for web UI work. Use as the foundation for specialized design skills or standalone UI component work."
license: MIT
---

# Design core

Make the user's task understandable, possible and recoverable. Apply this once per task; specialists add domain decisions rather than restating these foundations.

## Understand before changing

Inspect the relevant routes, components, design tokens, dependencies, data contracts and existing checks. Identify the audience, primary task, frequency, data sensitivity, device constraints and success condition. Use existing context first. Ask only about missing information that changes the outcome; record reasonable assumptions briefly and keep moving.

For an existing product, preserve its navigation, vocabulary, brand and working behavior unless the request changes them. A targeted fix does not require a new design brief. For a new screen, describe the main task, information hierarchy and action in a few lines before implementing.

## Give each project a reasoned visual direction

For new visual systems, use [visual-direction.md](references/visual-direction.md). Pick typography, density, composition, surface treatment and motion to support the product and audience. Commit to reusable tokens rather than copying a universal theme. Do not randomize styling between screens of the same product.

Keep design decisions small and concrete: a short direction note plus semantic tokens for text, surfaces, borders, actions, status, spacing, type and shape. Respect the existing naming scheme. No required font family, icon vendor, framework, light/dark mode, hero gradient, card grid or animation.

## Interaction and content

- Put the primary action where users need it. Use verbs that explain the result. Distinguish navigation links from actions; do not make generic containers behave like buttons.
- Use domain content with realistic lengths, dates, units, names and edge values. Mark prototype data as demo data. Never invent customer endorsements, prices, guarantees, security certifications or performance claims for a real product. Missing facts are explicit content gaps, not plausible lies.
- Show status and consequences near the action. Avoid success messages before an operation succeeds. Keep unsaved input and selection on recoverable failure.
- Prefer undo for reversible changes; use a proportionate confirmation for consequential destructive actions. Surface the affected object and scope.
- Implement every visible control or clearly communicate its unavailable/demo state. Do not create decorative controls, fake links or fake production integrations.

## Shared state contract

Model relevant states at the region or operation level, not as a full-page replacement every time. A static content section does not need artificial loading or empty states.

| State | Required behavior when applicable |
|---|---|
| Initial loading | Explain what is loading, reserve useful geometry; use skeletons for known structure or labeled progress for operations |
| Refreshing | Retain valid data and context, show refresh status without blocking unrelated work |
| First-use empty | Explain the object and provide a permitted next step |
| No results | Preserve the query/filter and offer reset or adjustment; distinguish from first-use empty |
| Error | Say what failed, keep inputs/data when safe, offer a meaningful retry or next step |
| Partial/stale/offline | Identify the affected region, age or connection status; do not present unknown data as current |
| Success | Confirm the actual result in context, without stealing focus unnecessarily |
| Disabled/read-only/forbidden | Explain availability or permission where needed, without leaking restricted data |

Controls also need visible focus, hover where supported, pressed/selected state where meaningful, and pending feedback for asynchronous work. Prevent accidental duplicate submissions. For details on accessibility and test evidence, read [verification.md](references/verification.md).

## Responsive and accessible by construction

Start with semantic HTML and established accessible components. Preserve logical reading and focus order when layouts change. On narrow screens, prioritize the task and progressively disclose secondary content; do not merely shrink desktop UI. Test text expansion, long names and zoom, not only ideal English copy. Support the requested language and locale; use logical layout properties when RTL is in scope.

Choose breakpoints where content stops working. Check a narrow viewport around 390px, a tablet layout around 768px and desktop around 1440px; additionally check reflow at 320 CSS px and 200% text zoom. Tables or canvases may need contained two-dimensional scrolling; keep page-level navigation and controls usable.

Keyboard use, visible unobscured focus, useful labels, readable contrast and non-color status cues are acceptance requirements. Honor reduced motion; reveal content without animation when it is disabled or fails. Do not hide essential content pending a scroll animation.

## Implementation and finish

Use the existing stack and components. Do not add a library solely to satisfy a preferred visual style. Keep data operations separate from display state, honor server authorization, use stable identifiers, and clean up listeners/timers and obsolete requests. Choose mock adapters explicitly when a backend is absent. A UI permission check does not secure an API.

Build the smallest complete user flow, then add its recovery paths and responsive behavior. Reuse components for repeated behavior; avoid a speculative component framework. Check asset size, layout shift and unnecessary rendering for the actual page; use available performance tooling when the change warrants it.

Before finishing, run the relevant project checks and the applicable steps in [verification.md](references/verification.md). Fix failures introduced by the work. Report what changed, what was exercised, and any unverified behavior or remaining dependency. Never label a screenshot, static lint result or mocked integration as production verification.
