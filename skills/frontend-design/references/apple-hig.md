# Apple Human Interface Guidelines, distilled for the web

Source: https://developer.apple.com/design/human-interface-guidelines/ (Design principles,
Layout, Typography, Color, Materials, Motion, Buttons). This is a paraphrased digest for building
web UI that *feels* considered in an Apple way. It is not a substitute for the HIG when shipping
native apps, and it never means copying Apple's visuals, icons or fonts.

## The principles behind it

Apple's current HIG frames design around eight ideas. In short:

- **Purpose**: decide what matters most to the people using it and make that part excellent.
  Cut the rest.
- **Agency**: people stay in control; they are informed about what is happening and can undo.
- **Responsibility**: earn trust through safety, privacy and being clear about what the
  product does.
- **Familiarity**: build on patterns people already know, and use them consistently.
- **Flexibility**: work for many people, devices, inputs and contexts, with equal care.
- **Simplicity**: be clear and direct; remove what is not needed; concise words.
- **Craft**: care about each detail; iterate and test; keep it current after launch.
- **Delight**: make it human, with satisfying moments that never get in the way of the task.

The older, still useful shorthand is **clarity** (legible text, precise icons, obvious function),
**deference** (the UI recedes so content leads), and **depth** (layering and motion convey
hierarchy and place).

What this means in practice for a web page:

- Content first, chrome second. Toolbars and navigation are quiet; the user's data is the
  loudest thing on screen.
- One clearly preferred action per view. Restraint is the aesthetic.
- Hierarchy is built with size, weight and color together, plus generous space, not with
  boxes and borders.

## Layout and hierarchy

- Put the most important content at the top and the leading edge, in reading order.
- Group related items with space first, then a container shape, then a separator line.
- Use alignment to show relationships, and indentation to show subordination.
- Use progressive disclosure (disclosure rows, menus, detail views) instead of showing every
  option at once.
- Keep controls and essential content inside safe areas. On the web this means
  `env(safe-area-inset-*)` with `viewport-fit=cover`, and nothing critical in the very bottom
  edge of a scrolling page behind a browser toolbar.
- Readable width: long text should sit in a comfortable column, not span a wide window.

## Typography

- Legibility first. Prefer Regular, Medium, Semibold and Bold; avoid Ultralight, Thin and Light
  at text sizes.
- Use as few typefaces as possible; build hierarchy with weight, size and color.
- When users enlarge text, the content they came to read grows first. On the web: size in
  `rem`, never lock containers to text height, let lines wrap, and reduce columns at large
  text sizes instead of truncating.
- Apple's iOS default text styles (default Dynamic Type size) are a well-tested ramp to borrow
  proportions from:

| Style | Size / leading (pt) | Weight |
|---|---|---|
| Large Title | 34 / 41 | Regular (Bold when emphasized) |
| Title 1 | 28 / 34 | Regular |
| Title 2 | 22 / 28 | Regular |
| Title 3 | 20 / 25 | Regular |
| Headline | 17 / 22 | Semibold |
| Body | 17 / 22 | Regular |
| Callout | 16 / 21 | Regular |
| Subhead | 15 / 20 | Regular |
| Footnote | 13 / 18 | Regular |
| Caption 1 | 12 / 16 | Regular |
| Caption 2 | 11 / 13 | Regular |

  Platform defaults/minimums: iOS 17 / 11 pt, macOS 13 / 10 pt, visionOS 17 / 12 pt.
- Web translation: 1pt on iOS is about 1 CSS px. A 17px body with ~1.3 leading for UI text and
  ~1.5 for long reading works well. For the font, use the system stack
  (`system-ui, -apple-system, ...`) which renders SF on Apple devices. SF Pro and New York are
  licensed for Apple platforms; do not self-host them on a website.
- Large titles that collapse into a compact sticky header on scroll are a recognizable,
  useful pattern for long lists.

## Touch targets and buttons

- Hit regions at least **44×44 pt** (visionOS 60×60). On the web, 44×44 CSS px for touch.
- Mark the most likely action with a prominent style, and keep prominent buttons to one, at most
  two, per view. Differentiate choices with style, not size.
- Never make a destructive action the prominent default, even if it is likely; people press
  prominent buttons without reading. Show destructive actions in the danger color.
- Labels start with a verb and are short ("Add to Cart", "Share Link"). Use a familiar symbol,
  text, or both; prefer text when a symbol is ambiguous.
- Custom buttons need a visible pressed state, or they feel broken.
- Space buttons so each is clearly separate from its neighbors.

## Color

- Define colors by role (background levels, label levels, separator, link), not by appearance,
  and do not reuse a role for something else (no separator color as text).
- Primary / secondary / tertiary levels for backgrounds and labels create hierarchy without
  extra hues. This maps directly to `--surface`, `--surface-sunken`, `--text`, `--text-muted`,
  `--text-subtle` in `tokens.md`.
- Every custom color has light, dark, and increased-contrast variants. On the web, support
  `prefers-contrast: more` by strengthening borders and muted text.
- Use the accent consistently: if it marks interactivity, do not also use it for static text.
- In colorful content (photos, media), keep toolbars monochrome so the accent stays legible.
- Never rely on color alone; color meanings differ across cultures (red is "up" in some
  markets).

## Materials and depth

- Translucent materials separate a **functional layer** (navigation, toolbars, controls)
  floating above a **content layer**. Apple's Liquid Glass belongs to the functional layer only
  and should be used sparingly; content backgrounds use standard, more opaque materials.
- Thicker (more opaque) materials when text is small or detailed; thinner when keeping the
  background visible matters more. Over bright media, add a dark dimming layer under clear
  glass so controls stay legible.
- Respect reduced transparency and increased contrast settings.
- Web translation: `backdrop-filter: blur(16-24px) saturate(1.5)` with a background of at least
  70–80% opacity on a sticky header or sheet; solid fallback via `@supports not
  (backdrop-filter: blur(1px))` and under `prefers-reduced-transparency: reduce`. Never on
  content cards.

## Motion

- Motion is for feedback and orientation, not decoration. Gratuitous motion distracts and can
  make people physically uncomfortable.
- Keep feedback animations brief and tied to the action. Do not add custom motion to very
  frequent interactions.
- Motion is consistent with direction: what slides in from the top leaves toward the top.
- People can interrupt animations and never wait for one to finish to act.
- Motion is never the only carrier of information; honor reduced-motion settings.
- Web translation: springy but short transitions (~200–300ms with a soft ease-out), sheets
  that slide up from the bottom on mobile, scale-from-origin for popovers.

## Writing

- Clear, direct and brief. Speak to the user ("your files"), use their vocabulary, not the
  system's.
- Title-style capitalization is Apple's convention for button labels; on the web, follow the
  product's existing convention and be consistent.

## Quick "feels like Apple" checklist (without imitating Apple)

- Content is the hero; chrome is light, neutral and recedes.
- One accent color, used for interactive things only.
- Generous whitespace; few borders; grouped lists with inset dividers.
- System font stack, strong weight contrast between title and body.
- 44px touch targets, visible pressed states, smooth but brief motion.
- Light and dark appearances both designed, plus an increased-contrast pass.
