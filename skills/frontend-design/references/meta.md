# Meta: what its public design guidance emphasizes

Meta does not publish one public HIG for Facebook, Instagram, WhatsApp or Threads; its product
design systems are internal. The public, citable guidance comes from a handful of places, and
together they describe a consistent philosophy. Sources (all paraphrased here):

- Meta Horizon OS design guidelines, including 2D panels and web apps (PWAs):
  https://developers.meta.com/horizon/design/ , https://developers.meta.com/horizon/design/pwa/
- Hit targets: https://developers.meta.com/horizon/design/styles_inputs_hit_targets/
- Accessibility: https://developers.meta.com/horizon/design/accessibility/
- React (created at Meta), "Thinking in React": https://react.dev/learn/thinking-in-react
- StyleX, Meta's styling system used across its web products: https://stylexjs.com/
- Design at Meta hub: https://www.meta.com/design-at-meta/
- Community analysis of meta.com's visual language in VoltAgent/awesome-design-md:
  https://github.com/VoltAgent/awesome-design-md (entry: Meta)

## 1. Design for the least precise input

Meta's interfaces run on phones, desktops, controllers, hands and eyes. The guidance that
follows from this is useful for any web UI:

- Size targets for the clumsiest input you support, not the most precise one. Minimum
  comfortable target **48×48 dp**; primary controls **60×60 dp** when hand tracking matters.
- When the visible control must be small (a standard button, an inline icon), add invisible
  **hit slop** so the interactive area is larger than the drawing.
- Space components so their hit areas, including slop, never overlap; overlapping slop causes
  accidental taps.
- Test on the real device and input, then adjust by feel.

Web translation: 44–48px targets on touch layouts, padding or a transparent `::after` to extend
small icon buttons, and at least 8px between adjacent targets.

## 2. Legibility in imperfect conditions

From the guidance for 2D panels and web apps shown in a headset (useful well beyond VR):

- Sans-serif faces with a generous x-height. Text no smaller than 14px, and 18px or more for
  comfortable reading.
- Heavier weights read better than light or thin ones; if a light weight is unavoidable,
  make it larger.
- Avoid pure white and pure black. Use light and dark grays; keep light backgrounds soft
  rather than glaring.
- Support both light and dark themes and follow the system preference
  (`prefers-color-scheme`).
- Colors can look more saturated on some displays; check on the target hardware.
- Design responsively: the window can be resized between small and large sizes, so layouts
  must reflow rather than assume one viewport.
- Icons: simple shapes on a 24-unit grid, no hairline strokes that break up at small sizes.

## 3. Accessibility as a default, not a mode

- Contrast at WCAG AA: 4.5:1 for normal text, 3:1 for large text and for UI components.
- Never use color as the only signal; add icons, patterns or labels. Consider a high-contrast
  theme.
- Use scalable text units and let containers grow with the text; test at the smallest and
  largest text settings.
- Captions for speech, readable on a background box, short line lengths, user-adjustable size.
- Fewer simultaneous inputs, remappable controls, one-handed and seated use, voice and gaze
  alternatives. On the web: everything works with a keyboard and with a single pointer.

## 4. Components that do one thing (React's way of thinking)

React's "Thinking in React" describes how Meta engineers turn a mockup into UI. It is a design
discipline as much as an engineering one:

1. Draw boxes around every part of the mockup and name them; each component should have one
   job. If it does several, split it.
2. Build a static version from data first, with no interactivity.
3. Find the minimal state: anything that can be computed from props or other state is derived,
   not stored.
4. Put each piece of state in the closest common parent of the components that use it.
5. Pass callbacks down so children can request changes; data flows one way.

Design consequence: the visual system should be made of a small set of composable pieces with
clear variants, not dozens of one-off sections.

## 5. Styles that scale with the codebase (StyleX)

StyleX reflects how Meta keeps large UIs consistent:

- Styles are colocated with the component that uses them, so nobody needs to know a distant
  global stylesheet.
- Output is atomic, so CSS size stays flat as the product grows.
- Predictability over cleverness: no specificity wars; the last style applied wins.
- Design tokens and themes are defined as variables and swapped as a set (light/dark, brand
  themes).

Design consequence: keep tokens as CSS variables, avoid deep selector chains and `!important`,
and make overrides explicit props or variants rather than cascade accidents.

## 6. The consumer-brand surface (meta.com)

The awesome-design-md analysis of meta.com describes a retail surface that is photography-
first and product-forward, with a binary light/dark surface system, a single brand blue
reserved for calls to action, and pill-shaped CTA buttons. The transferable lessons:

- Let real product imagery carry the page; keep UI chrome neutral around it.
- Reserve the brand color for the action you want taken. If everything is blue, nothing is.
- Commit to one shape language for actions (Meta's is the pill) and apply it everywhere.

## Applying this

When the user wants a social, feed-based or consumer product, or a Quest/Horizon web app:

- Large, forgiving targets with hit slop; nothing important under 14px.
- Soft neutrals instead of pure black/white; both themes from day one.
- A single accent for actions; imagery and user content provide the color.
- Composable components with derived state; tokens as variables; no cascade surprises.
- Do not copy Meta's logos, product names, iconography or the exact brand blue. Choose an
  accent for the product being built.
