# Verification and evidence

Use relevant checks, not a ceremonial checklist. Record pass, fail or not tested with evidence. Automated checks assist manual inspection; they do not prove usability or WCAG conformance.

## Accessibility baseline

Target WCAG 2.2 AA for web work unless the project specifies a stronger target. The following is a working subset, not a complete certification checklist. Source: [W3C WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/).

- Semantic landmarks/headings, accessible names and visible input labels. Meaningful images have useful alternatives; decorative images are ignored.
- Complete the main task by keyboard. Focus is visible, ordered and not hidden by sticky content. Dialogs manage focus, support an appropriate dismissal path and restore focus to a useful place. Do not trap users unintentionally.
- Text contrast: 4.5:1 normally; 3:1 for large text (24 CSS px, or about 18.67px bold). Essential control boundaries and state indicators need 3:1 against adjacent colors. Convey state beyond color.
- Targets meet the 24×24 CSS px AA size/spacing criterion or a documented exception. Prefer around 44×44 for touch comfort. A compact table still needs usable controls.
- Reflow at 320 CSS px and 200% text resize; no clipping or missing actions. Contain necessary table/canvas scrolling. Provide alternatives to drag-only operations.
- Associate errors and hints with fields; expose status messages without over-announcing. Allow paste and password managers in authentication. Avoid unnecessary repeated entry.
- Respect reduced motion. Check that disabled animations or failed scripts do not leave meaningful content invisible.

## Functional walkthrough

Exercise the main task with realistic data and one challenging record. Check pending → success and pending → failure → retry. Confirm inputs survive failure, empty and no-results differ, back navigation works, and permissions affect the actual behavior. Use the specialist's checks for domain-specific edge cases.

Inspect narrow, medium and desktop layouts with keyboard and pointer. Capture screenshots when browser tools exist and inspect them; a capture without inspection is not visual QA. If a browser, screen reader or backend is unavailable, state which checks remain unverified.

Run the repository's relevant lint, type, unit and integration checks. Add behavior tests for risky logic such as selection scope, date comparisons, concurrent saves or authorization-sensitive actions. Do not test incidental markup or copy merely to satisfy a count.

## Simple review rubric

Score each dimension 0 (broken/missing), 1 (usable with a known gap), or 2 (verified for the requested scope):

| Dimension | Evidence for 2 |
|---|---|
| Task and hierarchy | Main task completed without an ambiguous next step |
| States and recovery | Applicable empty, loading, failure and success paths exercised |
| Accessibility | Relevant keyboard, name, contrast, focus and zoom checks passed |
| Responsive behavior | Main flow works at narrow, medium and desktop sizes |
| Visual fit | Coherent tokens and a deliberate direction appropriate to this project |
| Implementation | Controls work; relevant checks pass; mock boundaries are explicit |

A practical review target is at least 10/12, no zero, and no critical blocker. Missing authorization, data loss, a keyboard-blocked main task, unreadable content, fabricated claims or a dead primary action are blockers regardless of score. This rubric is an internal quality aid, not an accessibility compliance claim.
