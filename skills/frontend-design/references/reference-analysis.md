# Working from a reference

Use when the user provides a screenshot, URL, Figma frame or says "make it like X". The goal is to
understand the design system behind the reference and produce something original that shares
its qualities. Never reproduce logos, brand names, proprietary fonts, illustrations, copy or
distinctive trade dress.

## 1. Extract the design DNA

Write a short analysis in this order:

1. **Layout**: grid and columns, content width, alignment axis, how sections are separated.
2. **Spacing**: base unit and the steps you can observe; ratio between inner and section gaps.
3. **Typography**: family category (grotesk, humanist sans, geometric, serif, mono), size ramp,
   weight contrast, line height, letter-spacing on display text, case conventions.
4. **Color**: neutral ramp (warm/cool, how dark the darkest text is), accent hue and where it
   appears, semantic colors, light/dark behavior.
5. **Shape and depth**: radius family, border usage, shadow style, use of materials/blur.
6. **Hierarchy**: what is loudest, how emphasis is created (size, weight, color, space).
7. **Interaction and motion**: hover/press behavior, transitions, density of motion.
8. **Personality**: two or three adjectives that the above adds up to.

If you can see the source (a URL's CSS, a Figma file), measure instead of guessing. If you only
have a screenshot, state values as estimates.

## 2. Translate into tokens

Turn the analysis into the token structure from `tokens.md` (spacing, type scale, radius,
shadows, palette) with your own values, then write the six-line design brief from `SKILL.md`.

## 3. Build original

- Keep the principles (restraint, rhythm, hierarchy, density), change the specifics: a different
  accent hue, your own layout for this product's content, your own copy.
- If the reference has a weakness (low contrast, tiny targets, missing states), do not inherit it.
  Note the improvement in your reply.

## Known reference styles (principles only)

Community DESIGN.md files in https://github.com/VoltAgent/awesome-design-md describe many
products' visual languages; consult them for vocabulary, not for values to copy. Typical
patterns:

- **Productivity tools (Linear-like)**: dark-first, ultra-minimal, very tight type, single cool
  accent, 1px hairline borders, dense lists, keyboard-first, fast subtle motion.
- **Developer platforms (Vercel-like)**: monochrome base, high contrast, strong grotesk type,
  hairline borders and grids, accent used extremely sparingly, technical precision.
- **Fintech (Stripe-like)**: light and airy, refined light-weight display type, careful layered
  shadows, rich but controlled color moments, exceptional documentation-quality detail.
- **Consumer hardware (Apple-like)**: product imagery as hero, huge confident headlines, lots of
  whitespace, neutral chrome, one link color. See `apple-hig.md`.
- **Social/consumer (Meta-like)**: photography and user content carry color, one brand color for
  actions, pill-shaped CTAs, large forgiving targets. See `meta.md`.
