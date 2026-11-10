# Web Interface Details

The difference between a demo and a product is in these details. This file condenses, in our own
words, the interaction rules from Vercel's Web Interface Guidelines, WCAG 2.2 and the platform
guidelines from Apple, Material and Fluent. Source links are in the repository README.

## Keyboard and focus

- Every action reachable by mouse is reachable by keyboard, in visual order. Do not set
  positive `tabindex`.
- Use `:focus-visible` for the ring (keyboard users) and keep `:focus` free of rings for mouse
  clicks. Use `:focus-within` to highlight a group (search bar with button, segmented control).
- The ring is at least 2px, offset from the element, and 3:1 against what surrounds it. Example:
  `outline: 2px solid var(--focus-ring); outline-offset: 2px;`
- Sticky headers and footers must not cover the focused element. Use `scroll-margin-top` /
  `scroll-padding-top` equal to the sticky height.
- Overlays (dialog, drawer, full-screen menu) move focus in on open, trap it, close on Escape,
  and return focus to the trigger on close. Use native `<dialog>` or a tested primitive (Radix,
  React Aria, Headless UI) instead of hand-rolling.
- Composite widgets (tabs, menus, listboxes, radio groups) follow WAI-ARIA Authoring Practices:
  one tab stop, arrow keys inside.
- Provide a "Skip to content" link as the first focusable element on content-heavy pages.
- Show keyboard shortcuts with the right platform symbol (Cmd on macOS, Ctrl elsewhere).

## Targets and input

- Minimum pointer target 24×24 CSS px; touch-first and primary controls 44×44 or larger.
  If the visible element is smaller (icon button, inline close "x"), grow the hit area with
  padding or a transparent pseudo-element, and keep hit areas from overlapping.
- Labels and their controls share one target: clicking the label focuses or toggles the control.
- Set `touch-action: manipulation` on controls to drop double-tap-zoom delay; style
  `-webkit-tap-highlight-color` deliberately.
- Never disable browser zoom (`user-scalable=no`, `maximum-scale=1`) and never block paste.
- Inputs on mobile use at least 16px font size so iOS does not zoom in on focus.
- Any drag, swipe, pinch or path gesture also has a single-pointer alternative (buttons,
  menu items, keyboard).
- During drag interactions, disable text selection on the page and mark the rest `inert`.
- Make the entire visible affordance clickable: a whole card row, not just its title, if it
  looks like one target. Conversely, nothing that looks clickable is inert.

## Forms

- Every control has a visible label. Placeholders are examples ("e.g. sam@company.com"), not
  labels, and never carry required instructions.
- Use the right `type`, `inputmode` and `autocomplete` (`email`, `tel`, `one-time-code`,
  `current-password`, `new-password`, `street-address`...) and meaningful `name` attributes so
  autofill and password managers work. Disable `spellcheck` / `autocapitalize` on emails, codes
  and usernames.
- Do not block typing to enforce a format; accept, then normalize (trim whitespace, strip
  spaces from card or phone numbers) and validate.
- Validate on blur or submit, not on every keystroke from the first character. Show the error
  next to the field, connected with `aria-describedby`, and on submit move focus to the first
  invalid field (or to an error summary for long forms).
- Keep the submit button enabled until a request is in flight; then disable it, show progress
  inside it while keeping its label, and make the request idempotent so double submits are safe.
- Enter submits single-field forms. In a textarea, Cmd/Ctrl+Enter submits.
- Warn before leaving a page with unsaved changes.
- Do not ask for the same information twice in one flow (WCAG 3.3.7); prefill what you know.
- Authentication does not depend on memorizing or transcribing (allow paste and password
  managers, support passkeys; WCAG 3.3.8).
- Set `color` and `background-color` explicitly on native `<select>` so it stays readable in
  dark themes on Windows.

## Feedback, loading, latency

- Respond to every action within ~100ms: a pressed state, a spinner, an optimistic update.
- Avoid flicker: delay showing a loading indicator ~150–300ms, and once shown keep it at least
  ~300–500ms.
- Prefer skeletons that match the final layout exactly (same heights, same columns) for content
  loads; use spinners only for short, button-scoped waits; use progress bars when you know the
  amount of work.
- Optimistic UI for low-risk actions (like, rename, reorder, toggle): update immediately,
  reconcile with the server, and on failure roll back and say so.
- Destructive actions get either a confirmation that names the object ("Delete 'Q3 report'?")
  or, better for frequent actions, immediate execution plus an Undo window.
- Announce asynchronous results (toasts, inline validation, "Saved") through a polite
  `aria-live` region.
- Menu items and buttons that open a further step end with an ellipsis ("Rename..."); loading
  labels do too ("Saving...").
- Mutations should complete fast; if they cannot, show progress and let people keep working.

## State and URLs

- The URL reflects what the user sees: filters, sort, search query, tab, pagination, selected
  item, open detail panel. Refresh, Back/Forward and sharing a link must reproduce the view.
- Navigation is a real link (`<a href>` / framework `Link`) so it opens in a new tab, can be
  copied and works without JS where possible. Buttons are for actions, links for navigation.
- Restore scroll position on Back/Forward. Keep `<title>` accurate for the current view.
- Do not lose input on hydration, re-render or route change.

## Content and states

- Design the five states of every data view: loading, empty, partial/sparse, ideal, error. And
  the extremes: very long names, missing images, 0, 1 and 10,000 rows.
- Empty states explain what will appear and give the action that creates it. "No results"
  states echo the query and offer to clear filters.
- Error states say what happened, whether data was lost, and what to do next. Never a raw
  stack trace or "Something went wrong" alone.
- Prefer inline help next to the field over tooltips. Tooltips are supplementary, never the
  only place information lives, and never on disabled controls with no other explanation.
- Typography details: real quotes and apostrophes, the ellipsis character, non-breaking space
  between number and unit ("10&nbsp;MB") and in shortcuts, `tabular-nums` for comparable numbers.
- Format numbers, dates, currency and relative times with `Intl` for the user's locale.
- Do not translate brand or code names (`translate="no"`).
- Never rely on color alone; pair with text or iconography.
- Icon-only buttons have an `aria-label`; decorative icons are `aria-hidden="true"`.
- Use one heading hierarchy per page, starting at a single `h1`.

## Motion

- Only animate to explain cause and effect, spatial relationships or state change, or for one
  intentional moment of delight.
- Animate `transform` and `opacity` (compositor-friendly). Avoid animating `width`, `height`,
  `top`, `left`, `box-shadow` on large areas. Never `transition: all`; list properties.
- Set `transform-origin` where the motion physically starts (a menu grows from its trigger).
- Exits mirror entrances (slides in from the right, leaves to the right) and are faster.
- Every animation is interruptible; user input wins over an animation in progress.
- No autoplaying motion longer than 5 seconds without pause/stop. Respect
  `prefers-reduced-motion`.
- Prefer CSS transitions, then the Web Animations API, then a JS library only when needed.

## Layout

- Align every element to something: grid line, baseline, edge, or optical center. Nudge
  optically (often 1px) when a mathematically centered icon looks off.
- Use flex/grid and intrinsic sizing, not JavaScript measurement.
- Respect safe areas on notched devices: `padding: env(safe-area-inset-top) ...` with
  `viewport-fit=cover`.
- Avoid accidental scrollbars: check overflow on every breakpoint; use `overflow-x: auto` only
  on the element that needs it; `overscroll-behavior: contain` inside modals and drawers.
- Test at 320px, tablet, laptop, and an ultra-wide window (or 50% zoom). Content should not
  stretch into 200-character lines on wide screens.
- Reflow: content works at 320 CSS px width without two-dimensional scrolling (WCAG 1.4.10).

## Performance (felt quality)

- Reserve space for images, embeds and ads (`width`/`height` or `aspect-ratio`) to prevent
  layout shift. Lazy-load below-the-fold images; prioritize the hero image.
- Preload only the critical font files; subset; `font-display: swap` with adjusted fallback
  metrics.
- Virtualize long lists (hundreds of rows). Debounce search input; never block the main thread
  for long tasks; move heavy work to a worker.
- Use `<video>` (muted, looping, with poster) instead of large GIFs.
- Test with CPU and network throttling, and in Safari and on a real phone.

## Theme and color mechanics

- Declare `color-scheme: light dark` and a matching `<meta name="theme-color">` per scheme so
  scrollbars, form controls and browser chrome match.
- Respect `prefers-color-scheme` by default; if there is a manual toggle, store the choice and
  apply it before first paint to avoid a flash.
- Hover, active and focus states increase contrast relative to rest; they never reduce it.
- Charts use color-blind-safe palettes and direct labels.
