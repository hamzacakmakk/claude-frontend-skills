---
name: frontend-design
description: Design and build distinctive, accessible, production-grade web interfaces (pages, apps, dashboards, landing pages, components) in HTML/CSS, React, Vue, Svelte or Tailwind. Use whenever the user asks to create, restyle, polish or "make it look good/professional" for any frontend UI. Commits to a design direction before coding, applies a token system, covers every interaction state, and actively avoids the generic look of AI-generated UI.
---

# Frontend Design

You are designing an interface a careful senior product designer would sign off on. The bar is
not "it renders" but "nothing here looks like a default". Every value (a color, a radius, a gap,
a word of copy) should be a decision you could defend.

The rules below are a synthesis of Apple's Human Interface Guidelines, Meta's Horizon OS and
accessibility guidance, Vercel's Web Interface Guidelines, Material 3, GitHub Primer, Microsoft
Fluent 2, Refactoring UI and WCAG 2.2. They are opinionated defaults: follow them unless the
project's existing design system or the user says otherwise. When they conflict, the project wins.

## Reference files (read on demand, not up front)

| Read this | When |
|---|---|
| `references/tokens.md` | Starting any UI without an existing token set. Copy the CSS variables. |
| `references/components.md` | Building buttons, forms, tables, dialogs, menus, toasts, empty states. |
| `references/web-interface-guidelines.md` | Anything interactive: focus, keyboard, forms, loading, URLs, motion. |
| `references/review-checklist.md` | Before you report the work as done. Always. |
| `references/apple-hig.md` | User wants an Apple / iOS / macOS feel, or you are building for Safari/iOS-heavy audiences. |
| `references/meta.md` | Social / consumer feed products, Quest / Horizon OS web apps, or a Meta-style storefront. |
| `references/dashboards.md` | Analytics, admin panels, data-dense screens, KPI views. |
| `references/reference-analysis.md` | The user supplies a screenshot, URL, Figma frame or "make it like X". |

## Workflow

### 1. Read before you design

- Look for an existing system first: CSS variables, `tailwind.config` / `@theme`, a `theme.ts`,
  a component library (shadcn/ui, Radix, MUI, Chakra), existing pages. Reuse it. Inventing a
  second button style in a codebase that already has one is a bug, not a design choice.
- Identify the stack and keep to it. Do not add a UI library or font the project does not need.
- Find out what the screen is *for*: who uses it, the one task they came to do, and what they
  do next. If the brief is vague, infer a concrete answer and state it in one line.

### 2. Write a design brief before writing code

Output these six lines (briefly, in your reply or as a code comment) before the first component:

1. **Job**: the primary task and the single most important action on the screen.
2. **Tone**: one or two words chosen on purpose (e.g. calm-utilitarian, editorial, technical,
   warm-consumer, playful, luxurious). The tone drives every later choice.
3. **Type**: font family (or system stack) and the scale you will use.
4. **Color**: one neutral ramp + one accent, plus semantic colors. Name the accent hue and why.
5. **Density and shape**: compact / regular / airy; radius family (sharp 0–4px, soft 6–10px,
   round 12–16px), used consistently.
6. **Signature**: one deliberate, memorable element (a typographic treatment, a layout move, a
   data visual, an illustration style). Exactly one. Everything else stays quiet.

Check the brief against the anti-slop list below. If any line matches a default, change it.

### 3. Structure, then style

- Start from semantic HTML and real content hierarchy. Headings in order, landmarks
  (`header`, `nav`, `main`, `footer`), lists that are lists, buttons that are `<button>`,
  navigation that is `<a href>`.
- Write real copy for the actual product. No lorem ipsum, no "Feature One", no invented
  testimonials or metrics. If data is unknown, use clearly plausible sample data that matches
  the domain, and say it is sample data.
- Then apply tokens (`references/tokens.md`). No raw hex values or one-off pixel values inside
  components; everything comes from a variable or the scale.

### 4. Every state, every size

- Each interactive element gets: default, hover, focus-visible, active/pressed, disabled, and
  where relevant loading, selected, invalid.
- Each data region gets: loading, empty (first use and no-results are different), error,
  partial, and overflowing (long names, 0 items, 10,000 items).
- Check at 320, 768, 1280 and 1600+ px wide. Nothing scrolls horizontally except things meant
  to (tables, code, carousels), and those scroll inside their own container.

### 5. Review, fix, then report

Run `references/review-checklist.md` against the result. Fix what fails before you answer.
In the reply, give the brief, what you built, and any deliberate trade-offs. Do not claim
contrast or accessibility you did not check.

## Anti-slop rules

These patterns make output instantly recognizable as machine-made. They are banned by default.
Use one only if the user asks for it or the existing brand already uses it, and say so.

1. **No purple-to-blue (or pink-to-orange) gradients** as the default brand look. No gradient
   text on headlines. A single flat accent color is almost always stronger.
2. **No glow.** No colored `box-shadow` halos, neon outlines, or blurred colored blobs behind
   content. Shadows are neutral, soft and layered (see tokens).
3. **No gratuitous glassmorphism.** `backdrop-filter` blur only on floating chrome (sticky
   header, popover, sheet) over scrolling content, with a solid fallback and enough opacity to
   keep text at contrast. Never on cards in the content flow.
4. **No emoji as icons** in UI chrome, feature lists or buttons. Use one consistent SVG icon
   set (Lucide, Heroicons, Phosphor, Material Symbols, or the project's own) at one stroke width.
5. **No fake numbers.** No "10,000+ happy customers", "99.9% uptime", star ratings, logos
   walls or testimonials that the user did not provide. Leave a clearly marked slot instead.
6. **No default hero formula**: centered headline + subtext + two buttons + three identical
   feature cards with icons in tinted circles. If a hero is needed, design it around the
   product's actual content (a screenshot, a live demo, real data, a strong typographic idea).
7. **No identical card grids** as the answer to every layout. Vary scale and weight to show
   priority; not every item deserves a box.
8. **No decorative eyebrow labels** (tiny uppercase tracking-wide text above every heading),
   no accenting one random word of a headline in a different color, no arrows appended to
   every link.
9. **No inconsistent shape language.** One radius family. Nested radii are concentric
   (inner radius = outer radius minus padding). Pills only for pills (tags, toggles) or by
   brand decision.
10. **No spacing by feel.** Every gap is a step on the 4px scale. Related things sit closer
    than unrelated things; section gaps are clearly larger than item gaps.
11. **No center-aligned body text.** Center only short, isolated lines. Long text is left
    aligned (start-aligned in RTL) with a 60–75 character measure.
12. **No gray-on-gray low-contrast "elegance".** Secondary text still passes 4.5:1.
13. **No animation on everything.** No fade-up on every section, no hover lift on every card,
    no infinite floating elements. One orchestrated moment at most, plus functional feedback.
14. **No generic font choice by reflex.** Choose type for the tone. A well-tuned system stack
    is a valid choice; three novelty fonts are not.
15. **No placeholder-quality copy**: "Unlock the power of", "Seamless", "Revolutionize",
    "Elevate your workflow", "Get started today" on every button. Say what the thing does.
16. **No dead UI.** Every visible control does something, or it is not there.

## Defaults

### Typography

- One family is enough; two only if they contrast clearly (e.g. a serif display with a sans
  body). Prefer variable fonts; load at most 2–3 weights; `font-display: swap` with a metric-
  matched fallback to avoid layout shift.
- Body 16px minimum on the web (17px is a good reading size; inputs must be at least 16px on
  mobile or iOS zooms). Line height 1.5–1.6 for body, 1.1–1.25 for large headings.
- Use a modular scale (1.2 for dense apps, 1.25 for general product UI, 1.333+ for editorial
  and marketing). Hierarchy comes from size *and* weight *and* color, not size alone.
- Avoid thin and light weights below ~24px. Use 400/500 for text, 600/700 for emphasis.
- Tighten letter-spacing slightly on large display sizes (around -0.01 to -0.02em); never add
  tracking to body text. `font-variant-numeric: tabular-nums` for any number that is compared,
  totals, tables and timers.
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs where supported.

### Space and layout

- 4px base unit; use the scale 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
- Group by proximity first, then alignment, then subtle surface change, and only then borders.
  Fewer boxes, more whitespace.
- Pick a content width (e.g. 1120–1280px for apps, 680–760px for reading) and a consistent
  page gutter (16px mobile, 24–32px tablet, 32–64px desktop). Respect `env(safe-area-inset-*)`.
- Use CSS grid and flex with intrinsic sizing (`minmax`, `clamp`, `auto-fit`); avoid JavaScript
  layout measurement. Container queries for components that live in different widths.
- Put the most important content at the top and leading edge. Indentation shows subordination.

### Color

- Neutrals do most of the work. One accent, used for the primary action, links, focus and
  selection, and almost nothing else. If the accent is everywhere, nothing is emphasized.
- Use semantic tokens (`--text`, `--text-muted`, `--surface`, `--border`, `--accent`), never
  raw colors in components. Define light and dark together; dark mode is not inverted light
  mode (raise surfaces with lighter grays instead of shadows; desaturate the accent slightly).
- Avoid pure `#000` backgrounds and pure `#fff` text on dark; use near-black and off-white.
- Tint neutrals very slightly toward the accent or a warm/cool bias for cohesion.
- Never communicate with color alone: pair status color with an icon, label or shape.

### Depth, borders, radius

- Elevation means something: flat for content, raised for interactive cards, floating for
  menus, popovers, dialogs. Max three levels on a screen.
- Shadows: two layers (a tight contact shadow plus a soft ambient one), neutral or tinted
  toward the background hue, low opacity. Borders: 1px, low-contrast, or a semi-transparent
  border combined with the shadow for crisp edges.
- Child radius never exceeds parent radius.

### Motion

- Motion explains change (where did this come from, what did my action do). It is not decor.
- Durations: 100–150ms for small state changes (hover, press), 200–250ms for elements
  entering, 150–200ms for exits (exits are faster), up to ~350ms for large surfaces.
- Ease-out for entering, ease-in for leaving, ease-in-out for moving on screen. Animate only
  `transform` and `opacity`. Never `transition: all`. Animations must be interruptible.
- Honor `prefers-reduced-motion: reduce`: replace movement with opacity or nothing.

### Copy

- Labels are specific verbs: "Save changes", "Invite member", "Delete project", not "Submit"
  or "OK". The button that confirms a dialog repeats the action in the dialog title.
- Sentence case for UI text unless the existing product uses title case.
- Errors say what happened and how to fix it, in plain language, next to the cause.
- Empty states say what goes here and offer the action that fills it.

## Accessibility floor (non-negotiable)

- Contrast: text 4.5:1 (3:1 for text 24px+ or 18.66px+ bold); icons, input borders, focus
  indicators and other meaningful non-text UI 3:1 against adjacent colors (WCAG 2.2 AA).
- Visible focus on every focusable element via `:focus-visible`, at least 2px, 3:1 against the
  surface, never removed without a replacement, never hidden under sticky headers.
- Everything works with a keyboard in a logical order; dialogs trap and restore focus; Escape
  closes overlays.
- Pointer targets at least 24×24 CSS px (WCAG minimum); 44×44 for touch-first and primary
  controls (Apple's 44pt, Material and Meta's 48dp are the same idea). Extend small icons'
  hit area with padding or a pseudo-element.
- Every input has a visible `<label>`; icon-only buttons have an accessible name; images have
  meaningful `alt` or `alt=""` if decorative.
- Never disable zoom. Layout works at 320px wide and at 200% text size.
- Drag, swipe and pinch always have a click/tap/keyboard alternative.

## Platform flavor

If the user names a reference ("like Apple", "like Linear", "like Instagram"), extract the
principles, not the pixels: hierarchy, density, type behavior, color restraint, motion
character. Never copy logos, proprietary fonts (SF Pro is licensed for Apple platforms only;
use `system-ui` / `-apple-system` stacks instead), product names, or distinctive brand assets.
See `references/reference-analysis.md`.
