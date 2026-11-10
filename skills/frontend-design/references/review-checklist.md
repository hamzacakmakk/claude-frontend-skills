# Review checklist

Run this before reporting UI work as done. Check each item against the actual code and, if you
can, a rendered page. Fix failures; do not just list them. Items marked **[blocker]** must pass.

## 1. Direction and hierarchy

- [ ] The primary action of the screen is obvious within two seconds, and there is only one.
- [ ] Squinting at the page shows a clear order: one dominant element, then a few secondary
      ones, then the rest.
- [ ] The design brief's tone is visible: a stranger could guess the product's character.
- [ ] There is exactly one signature element, and everything else is restrained.

## 2. Anti-slop scan

- [ ] No purple/blue default gradients, no gradient text, no glows or neon shadows.
- [ ] No glassmorphism on content; blur only on floating chrome, with a solid fallback.
- [ ] No emoji used as icons; one icon set, one stroke width.
- [ ] No invented metrics, testimonials, logos, ratings or user counts.
- [ ] Not the stock "centered hero + two buttons + three icon cards" layout.
- [ ] No lorem ipsum or generic marketing filler ("seamless", "unlock", "elevate").
- [ ] No decorative eyebrow labels on every section, no single accented headline word.
- [ ] Not everything is a card; not every element animates.

## 3. Tokens and consistency

- [ ] No raw hex/rgb values or arbitrary pixel values inside components; tokens only.
- [ ] Every spacing value is on the 4px scale; group gaps clearly exceed item gaps.
- [ ] One radius family; nested radii are concentric; child radius <= parent radius.
- [ ] Type uses the defined scale; at most two families; at most three weights in use.
- [ ] The accent appears only on interactive or selected things.
- [ ] Repeated elements (buttons, inputs, cards) are the same component, not look-alikes.

## 4. Accessibility

- [ ] **[blocker]** Body text contrast >= 4.5:1, large text >= 3:1, input borders/icons/focus
      rings >= 3:1. Checked with a calculator, not by eye.
- [ ] **[blocker]** Every interactive element is reachable and operable by keyboard, in a
      logical order, with a visible `:focus-visible` style.
- [ ] **[blocker]** Every form control has a label; every icon-only button has an accessible
      name; images have appropriate `alt`.
- [ ] Semantic landmarks and one `h1`; headings do not skip levels.
- [ ] Targets >= 24×24px everywhere, >= 44×44px for touch-first and primary controls.
- [ ] Dialogs trap and restore focus and close on Escape.
- [ ] Information is never conveyed by color alone.
- [ ] `prefers-reduced-motion` is respected; nothing autoplays for more than 5s without control.
- [ ] Zoom is not disabled; page works at 200% text size.

## 5. States

- [ ] Buttons and controls: hover, focus-visible, active, disabled, loading.
- [ ] Data views: loading (skeleton matches layout), empty (first use and no-results),
      error with recovery, long content, many items.
- [ ] Forms: inline validation placed next to fields, focus to first error on submit, submit
      guarded against double clicks.
- [ ] Destructive actions confirm with the object's name or offer Undo.

## 6. Responsive and layout

- [ ] **[blocker]** No horizontal page scroll at 320px; content reflows.
- [ ] Checked at ~375, 768, 1280 and 1600+ px. Reading width stays <= ~75 characters.
- [ ] Tables scroll within their container or collapse to stacked rows on small screens.
- [ ] Safe-area insets respected for fixed/sticky elements on mobile.
- [ ] Sticky elements do not cover focused content or anchors.

## 7. Content

- [ ] Button labels are specific verbs; dialogs repeat the action in the confirm button.
- [ ] Errors explain what happened and how to fix it.
- [ ] Numbers use `tabular-nums` where compared; dates/currency formatted for locale.
- [ ] Copy uses the product's vocabulary consistently (one name per concept).
- [ ] Page `<title>` and meta description are accurate.

## 8. Theme and polish

- [ ] Light and dark both designed (if the product supports both), including focus rings,
      borders, shadows, charts and images.
- [ ] `color-scheme` and `theme-color` set.
- [ ] Shadows are subtle and layered; borders are low-contrast where decorative.
- [ ] Icons optically aligned with text; no 1px misalignments in rows of controls.
- [ ] Transitions list specific properties and use the motion tokens.

## 9. Performance

- [ ] Images have dimensions or `aspect-ratio`; below-the-fold images lazy-load.
- [ ] Fonts: at most 2–3 files preloaded, `font-display: swap`.
- [ ] No layout shift when data, fonts or images arrive.
- [ ] Long lists are virtualized or paginated.

## Reporting

After the pass, tell the user in a few lines: the design brief, what was built, which checks
were verified (and how), and any known gaps. Never claim a check you did not perform.
