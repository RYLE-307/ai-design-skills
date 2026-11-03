# Choosing visual direction

Read for a new product, requested redesign or unresolved brand decision. Skip for a local fix in an established system.

Write a short direction record in the existing design notes, or in the response if no artifact is needed:

```text
Audience and core task:
Existing brand / references / constraints:
Direction and why it fits:
Typography and density:
Composition and surfaces:
Accent and semantic status colors:
Motion and imagery:
One signature detail:
```

Choose a coherent combination, not a random “style”. Consider two plausible directions internally and select the better fit; show alternatives only when the user needs to decide.

| Context | Possible direction | Functional consequence |
|---|---|---|
| Scheduling for small studios | Warm editorial, expressive headings, cream surfaces, restrained terracotta | More explanatory spacing, human examples, approachable onboarding |
| Developer workflow tool | Precise utilitarian sans, compact rows, cool neutrals, restrained cyan | Dense legible data, tabular numerals, fast feedback, strong focus |
| Research analytics | Quiet report-like composition, typographic hierarchy, low decoration | Comparisons and methodology stay prominent; restrained chart palette |
| Creative collaboration | Bold display type, vivid accent, generous canvas | Work artifacts are the focal point, controls stay predictable |

These are examples, not presets to rotate through. A developer tool can be light; a financial interface need not be blue. Distinguish projects through several meaningful dimensions: composition, typography, density, shape, imagery and motion, not just accent color. Keep the same product coherent across marketing and application surfaces while adapting density to the job.

Define a small reusable set of semantic roles in the existing theme mechanism. Map brand color to accessible action and focus colors; status colors are separate meanings. Verify actual combinations, including muted text, selected rows, disabled hints, charts and any gradients. Do not assume a palette is accessible because its hex values look dark.

Use a compact spacing and type scale suited to content. Fluid headings are useful on marketing pages; compact data screens need stable row rhythm and readable labels. Font pairing, italics, gradients, straight corners and system fonts are legitimate choices when they support the direction. Load only needed font weights, preserve readable fallbacks, and reserve image geometry to avoid layout shifts.

Use motion to explain continuity or action feedback. Frequent product operations should feel immediate; do not inherit a slow marketing reveal for every click. Reduced motion may remove movement entirely. An optional visual effect must not be necessary to find content or complete a task.

Review the result in grayscale and with long content: hierarchy should survive without color and ideal-length text. If two unrelated projects have the same centered hero, rounded cards, font, sidebar and glow, reconsider the composition against their different tasks. Do not force difference when a shared brand or explicit reference requires consistency.
