---
name: design-system-generator
description: Create or extend a token-based design system (color, type, spacing, radius, elevation, motion) with light and dark themes, verified contrast, component guidelines and documentation, delivered as CSS variables, Tailwind theme config or JSON tokens. Use when the user asks for a design system, theme, style guide, tokens, brand palette or "consistent styling" across an app.
---

# Design System Generator

Build the smallest system that makes the product consistent. A design system is a set of
decisions, not a large set of values: fewer, well-named tokens beat exhaustive scales nobody uses.

If the `frontend-design` skill is installed, `frontend-design/references/tokens.md` contains a
complete, contrast-checked starter set; start from it and adapt.

## 1. Inputs

- Read what exists: current CSS, Tailwind config, theme files, component library, brand assets.
  Inventory actual values in use (colors, font sizes, spacing, radii) and how often each occurs.
- Clarify (or infer and state) the product's tone, platforms (web, iOS, Android), density, and
  whether dark mode and high-contrast mode are required.

## 2. Architecture: three layers

1. **Primitive tokens**: raw values with neutral names. `--gray-50 ... --gray-950`,
   `--blue-600`, `--space-4`, `--radius-md`. Never used directly in components.
2. **Semantic tokens**: purpose-based aliases. `--bg`, `--surface`, `--surface-sunken`,
   `--border`, `--border-strong`, `--text`, `--text-muted`, `--text-subtle`, `--accent`,
   `--accent-fg`, `--accent-subtle`, `--focus-ring`, `--success`, `--warning`, `--danger`,
   `--info` (+ `-subtle` variants). Themes swap these.
3. **Component tokens** (only when needed): `--button-height-md`, `--input-border`,
   `--card-padding`. Add them when a component needs to be themed independently.

Naming: `category-role-variant-state` (`--text-muted`, `--accent-hover`). No color names in
semantic tokens (`--accent`, not `--blue`).

## 3. Decisions to make

- **Spacing**: 4px base. Scale 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
  (Fluent 2 and Material both build on 4px; Tailwind's default scale is 4px-based.)
- **Type**: one or two families; a modular scale (1.2 dense, 1.25 product, 1.333+ editorial);
  roles rather than sizes (display, title, heading, body, label, caption, code); line heights
  per role; fluid `clamp()` only for display sizes.
- **Color**: neutral ramp of 10–12 steps (slightly warm or cool, chosen on purpose), one accent
  ramp, four semantic hues. Generate ramps in OKLCH for even perceptual steps.
- **Radius**: one family (sharp, soft or round) with 3–4 steps plus `full`.
- **Elevation**: 3 levels at most (raised, floating, overlay), two-layer neutral shadows; in
  dark mode prefer lighter surfaces over heavier shadows.
- **Motion**: 3 durations (fast ~140ms, base ~220ms, slow ~320ms), 3 easings (out, in,
  in-out), and a reduced-motion rule.
- **Layers**: a small z-index scale (sticky, dropdown, overlay, dialog, toast, tooltip).
- **Breakpoints**: content-driven; a common set is 640, 768, 1024, 1280, 1536.

## 4. Themes and contrast

- Define light and dark together. Dark mode: near-black background (not #000), off-white text
  (not #fff), lighter surfaces for elevation, accent lightened and slightly desaturated.
- Add a `prefers-contrast: more` variant that strengthens borders and muted text.
- **Verify every text/background pairing** with the WCAG 2 formula and publish the ratios:
  text 4.5:1, large text and meaningful UI (input borders, icons, focus rings) 3:1. Include the
  numbers in the docs; do not state "AA compliant" without computing it.

## 5. Deliverables

Produce, in the project's stack:

1. `tokens.css` (CSS custom properties, light + dark + high-contrast), and/or the Tailwind
   theme mapping (`@theme` in v4, `theme.extend` in v3), and/or `tokens.json` in the W3C Design
   Tokens Community Group format if a pipeline (Style Dictionary) is used.
2. A short `DESIGN.md` documenting: principles (3–5 lines), the token tables with contrast
   ratios, type roles, spacing usage rules, and do/don't for the core components (button,
   input, card, dialog, table, toast).
3. Optionally a single `styleguide.html` / story page rendering every token and component state
   in both themes, so the system can be checked visually.

## 6. Migration (existing products)

- Map existing values to the nearest token; list values that disappear and why.
- Replace in order: colors, then spacing, then type, then radii and shadows.
- Keep a temporary alias layer for old names if the codebase is large.

## Checklist

- [ ] Primitive, semantic and (only where needed) component layers are separate.
- [ ] Components reference semantic tokens only.
- [ ] Light, dark and high-contrast themes exist and every pairing has a computed ratio.
- [ ] Spacing is 4px-based; one radius family; at most three elevation levels.
- [ ] Type roles cover display through caption; at most two families, three weights.
- [ ] Motion tokens include a reduced-motion rule.
- [ ] Documentation explains when to use each token, not only its value.
