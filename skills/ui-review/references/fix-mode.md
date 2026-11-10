# Fix mode: refactoring UI code

Use after an audit when the user wants the changes made. The goal is a cleaner, more consistent,
more accessible interface with the same behavior.

## Order of work

1. **Protect behavior.** Note the component's public API (props, events, routes, test ids) and
   keep it. If tests exist, run them before and after.
2. **Fix P0 issues first**: contrast, labels, keyboard and focus, semantics, mobile reflow.
3. **Introduce tokens** before restyling: replace hard-coded colors, spacing, radii, shadows and
   font sizes with variables (use the project's system, or the `frontend-design` tokens). This
   step alone usually removes most inconsistency.
4. **Fix structure**: semantic elements (`button` for actions, `a` for navigation, `label` for
   inputs, landmarks, heading order); remove wrapper `div` nesting that exists only for styling;
   use grid/flex with `gap` instead of margins on children.
5. **Restore hierarchy**: one primary action, clear section rhythm (group gaps larger than item
   gaps), type scale applied, muted secondary text.
6. **Add missing states**: hover, focus-visible, active, disabled, loading; empty, error and
   loading for data regions.
7. **Remove generic-AI decoration**: default gradients, glows, glass on content, emoji icons,
   filler copy, motion on every element. Replace with restraint, not with a different
   decoration.
8. **Re-audit** the result with the review rubric and report what changed.

## Modern CSS you may use

- `gap` on flex and grid; `minmax()`, `auto-fit`, `clamp()` for fluid sizing.
- Container queries for components that appear in different widths.
- `:focus-visible`, `:focus-within`, `:has()`, `:is()`, `:where()` (low specificity resets).
- Logical properties (`margin-inline`, `padding-block`, `inset-inline-start`) for RTL safety.
- `color-mix()` and relative colors for hover/subtle variants derived from tokens.
- `text-wrap: balance | pretty`, `aspect-ratio`, `accent-color` for native controls.
- `@media (prefers-reduced-motion)`, `(prefers-color-scheme)`, `(prefers-contrast: more)`.

Check the project's browser support targets before using the newest features; provide a fallback
when needed.

## Framework notes

- **React**: do not create components inside render; lift state only as far as needed; derive
  instead of storing; keep inputs uncontrolled where possible for performance; memoize only
  measured hot paths.
- **Tailwind**: replace arbitrary values (`p-[13px]`, `text-[#333]`) with scale/theme values;
  extract repeated class strings into components, not `@apply` soup; map tokens in the theme.
- **Component libraries**: configure through the library's theme and variants instead of
  overriding internals with high-specificity CSS.

## Report

List what changed by category (accessibility, tokens, structure, hierarchy, states, cleanup),
anything intentionally left alone and why, and any follow-ups that need a product decision.
