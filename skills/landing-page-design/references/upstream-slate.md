# Optional Elaya-inspired visual direction

Read only when the user asks for the original Elaya look or deliberately selects this direction. This is an adapted preset, not a second quality standard. Core accessibility, task needs and the actual brand still apply. The complete original text is preserved in the repository's `docs/upstream/landing-page-design.md` for provenance; do not load that archive as current rules.

- Start with a restrained neutral surface, Geist or Manrope if available, and a single accent. Use Geist Mono only where code/data benefits. Keep system fallbacks and appropriate font licenses.
- A useful initial spacing scale is 0, 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80 and 96px. Map it to the project's tokens; extend deliberately when content needs it.
- Use a compact type scale with named heading/body/label roles. Tailwind's scale is an option, not a dependency. Choose responsive values and readable line height rather than snapping all text downward.
- Use flat layered surfaces. Original dark examples include `#181818`, `#1F1F1F`, `#272727`; verify actual foreground contrast. Light mode is equally valid.
- A hero can use a restrained text gradient and a line length around 680px at desktop. Check contrast across the whole gradient and allow natural narrow-screen wrapping.
- Align nested rounded edges visually. An inner radius near `max(0, outer radius - inset)` can be a starting point, not an override of token or shape requirements.
- Use a consistent existing icon set; Phosphor, Solar and Iconamoon are original options.
- Optional reveal motion can use a decelerating curve such as `cubic-bezier(0.22,1,0.36,1)` with transform/opacity. A compact floating nav or benefit/tagline reveal is appropriate only when it improves the chosen composition.
- Show tagline content at full readable contrast by default. Enhance it with motion only when safe, never make low-opacity text the only readable state. Reduced motion shows the final state immediately.

The original fixed font bans, universal gradient heading, mandatory animated tagline, strict token-only values and full-height mobile menu are not universal requirements in this fork. Preserve a project's existing design system over this preset.
