---
name: landing-page-design
description: "Build or improve public landing pages and marketing pages through audience, offer, conversion copy, section structure and visual direction. Use for acquisition surfaces, not authenticated workspaces or application components."
license: MIT
---

# Landing page design

Adapted from Elaya's original skill. Preserve its strategy-first approach: one offer → one audience → one primary conversion. A marketing homepage may serve several audiences; make its hierarchy explicit instead of pretending every homepage is a single-offer campaign.

Read [design-core](../design-core/SKILL.md) once for shared visual direction, implementation, states, responsive behavior and accessibility. This skill owns the marketing argument and conversion path. For the original visual flavor, read [upstream-slate.md](references/upstream-slate.md) only when the user chooses it; it is not a universal design constraint.

## A1. Intake

Use supplied context first: offer, audience, primary action, traffic source, awareness level, main objections, verified proof, brand assets and implementation constraints. Ask only for gaps that materially change the page. State reasonable assumptions and proceed; do not turn a simple page into an intake interview.

Distinguish a draft concept from a real product. Prices, trial terms, guarantees, customer logos and testimonials must be supplied or sourced for a real product. Omit unsupported proof or mark an internal content gap; do not publish an invented claim. Fictional sample content must be visibly identified as demo material.

## A2. Page structure

The hero should make the offer, audience and next step understandable. Use an outcome-focused headline, a clarifying subheadline, one dominant action, a useful visual and verified proof when available. A product screenshot should explain the product, not just decorate a device frame.

Build the rest around actual objections: problem/solution, benefits, how it works, evidence, comparison, pricing, FAQ, risk reduction and a final action. These are candidate sections, not a compulsory twelve-section template. A waitlist can be short; a complex purchase may need a longer argument. Repeat the same conversion intent with context-appropriate wording.

Place evidence beside the claim it supports. Include a risk-reduction statement only when its terms are verified. A tagline section is optional; it must add meaning rather than repeat the hero.

## A3. Layout selection

| Layout | Use when |
|---|---|
| Classic hero and sections | The offer is understandable through a product example |
| Long-form story | Visitors need education and evidence before committing |
| Minimal conversion page | High-intent audience and a narrow offer, such as a download |
| Comparison page | The visitor is evaluating alternatives with verifiable criteria |

Choose and explain the fit in one sentence. Composition, typography and imagery follow the project's direction, not a mandatory centered hero or equal-card grid.

## A4. Conversion logic

Match the promise to the traffic source. Keep the primary CTA visually dominant; a subordinate demo or explanation link may help visitors who are not ready. Explain what happens after the click. Place requested information in proportion to the value offered, and avoid misleading urgency, hidden commitments or preselected consent.

Choose benefit-first copy with evidence rather than vague claims. Do not manufacture precise numbers to make copy sound specific. “See each shift and unresolved coverage gap” is better than an unsupported “Save 80%”. Move objection handling earlier for a high-friction offer.

## A5. Copywriting

Useful starting patterns are “{outcome} without {pain}”, “{category} for {audience}”, or a direct description of the task the product solves. They are prompts, not required headline formulas. Write in the user's language and brand voice.

Keep subheadlines concrete. Use CTA labels that describe the next step: “Start free trial” only when that trial exists, “Request a demo” for a real demo flow. Prefer useful benefit/detail pairs over a feature inventory. Respect normal punctuation and grammar; no blanket ban on hyphens, italics or particular words can replace good writing.

## A6. Build order

For a new page, briefly state the chosen layout, section outline, hero copy, primary action and unresolved content facts. Then build a complete conversion path: hero → action destination/form → result. Add the remaining argument section by section and inspect the result. For a targeted edit, change only the relevant section and its affected flow.

Reuse core's state contract for the CTA/form: pending, success, validation failure and network failure where relevant. A static benefit section does not need a skeleton. For a substantial multi-step signup or onboarding flow, read [forms-settings](../forms-settings/SKILL.md).

## A7. Search and sharing

Decide indexability from the page's purpose and the project's SEO policy. Campaign pages are not automatically noindex. Private, duplicate or temporary content needs an explicit decision; a URL path alone does not prevent indexing. For indexable pages provide an accurate title/description, canonical URL when appropriate, semantic headings and useful internal links.

Use social metadata and a real sharing image when in scope. Structured data must match visible, verified content and applicable search-engine rules; do not promise FAQ rich results or add invented reviews. Make important content readable without relying on animation or delayed script execution.

## B. Visual and shipping decisions

Core owns the visual system. Choose a direction that fits this offer and differs meaningfully from unrelated projects when no shared brand applies. Translate it into reusable type, spacing, surface and action tokens. Build a deliberate hero composition, readable line lengths and meaningful imagery. Do not force an icon library, font, palette, heading gradient, floating navigation or word-by-word reveal.

Motion is optional. If chosen, keep it lightweight and preserve final readable content with reduced motion or script failure. On narrow screens preserve the offer and primary path without forcing everything above an arbitrary fold. Check long CTA labels and real product imagery.

Provide working navigation and conversion destinations, semantic landmarks, suitable alt text and focus behavior. Use actual legal/privacy URLs and consent requirements supplied by the project; do not invent legal text or default to a cookie banner when none is needed. Reuse existing 404, favicon and site metadata; create missing assets/pages only within the agreed scope and identify launch dependencies.

## Acceptance walkthrough

From the hero, explain the offer and complete the primary action with keyboard and touch. Follow every visible link. Exercise any form's invalid, pending, failed and successful states. Inspect mobile navigation, image loading, reduced motion, narrow layout and content truthfulness. Review the page against core's quality rubric. Report verified behavior and content/backend gaps; do not imply conversion gains without measurement.

## Credits

The no invented facts rule and reduced motion support for the tagline reveal were suggested by [@allen-baler](https://github.com/allen-baler) in [#1](https://github.com/elayadesign/ai-design-skills/pull/1).

Parts of this skill were adapted from [taste-skill](https://github.com/Leonxlnx/taste-skill) by Leon Lin ([@LexnLin](https://x.com/LexnLin)), MIT licensed. Its redesign audit structure, content realism checks, and motion and navigation ideas informed the matching sections here, which have since been rewritten.

<details>
<summary>taste-skill license</summary>

```
MIT License

Copyright (c) 2026 Leonxlnx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
</details>
