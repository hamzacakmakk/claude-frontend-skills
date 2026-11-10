# Components: do and don't

Patterns that hold up across Apple HIG, Material 3, GitHub Primer, Fluent 2 and Vercel's
guidelines. Use the project's component library if it has one; these rules still apply to how
you configure it. Values refer to `tokens.md`.

## Buttons

Hierarchy: **primary** (filled accent, one per view or region), **secondary** (neutral fill or
outline), **tertiary/ghost** (text only, for low-emphasis actions), **danger** (for destructive
confirmations only).

Sizes: small 32px, medium 36–40px, large 44–48px high. Horizontal padding about 1.5–2x the
vertical. Touch layouts use 44px+.

Do:
- Label with a verb + object: "Create invoice", "Send invite".
- Keep width stable while loading: show a spinner inside or in place of an icon, keep the label
  (or switch to "Saving..."), and disable only while the request is in flight.
- Place the primary action where the eye ends (end of a form, bottom-right of a dialog on
  desktop; full-width at the bottom on mobile). Be consistent across the product.
- Icon + label: icon at 16–20px, 6–8px gap, optically centered.

Don't:
- Two filled primary buttons side by side.
- A destructive action as the default/primary button of a dialog that is not explicitly about
  deletion.
- Disabled buttons with no explanation of why. Prefer enabled + validation message, or a
  visible hint.
- `<div onClick>` or `<a>` without `href` as buttons.
- Gradient fills, glows, or hover effects that move the button more than 1px.

## Links

- Links look like links in body text (underline or clear color + underline on hover). In
  navigation and lists, a row hover state can replace the underline.
- Link text describes the destination ("View billing history"), never "click here".
- External links that open new tabs say so (icon with accessible text).

## Text inputs

- Visible label above the field (most robust layout); optional hint below the label; error
  below the field replacing or adding to the hint.
- Height matches buttons of the same size so they align in a row. Border uses
  `--border-strong` (3:1). Focus: border to accent + focus ring.
- Mark optional fields ("Optional") rather than starring every required field, when most are
  required. Be consistent.
- Width hints at the expected input: a ZIP code field is not full-width.
- Error state: border in danger color + icon + message; never color alone.

Don't: floating labels that shrink to unreadable size, placeholder-as-label, inputs with no
visible border on a white background, validating while the user is still typing the first
characters.

## Selection controls

- Checkbox for independent options and for "I agree". Radio for one-of-a-few (2–5) visible
  options. Select/combobox for many options. Switch for an immediate on/off setting that takes
  effect without a Save button.
- Segmented control for 2–4 mutually exclusive views of the same content.
- The label is clickable and part of the target.

## Forms (layout)

- Single column. Group related fields under small section headings. Keep the label-to-field
  gap small (4–8px) and the field-to-field gap larger (16–24px).
- Order fields the way people think about the information. Ask only for what you need.
- Primary action at the end, aligned with the fields. Secondary "Cancel" as a ghost button.
- Long forms: sticky action bar, save progress, and an error summary on submit.

## Tables and lists

- Left-align text, right-align numbers (with `tabular-nums`), align headers with their data.
- Row height: 40px compact, 48px regular, 56px+ with secondary lines. Use zebra striping or
  dividers, not both.
- Sticky header for long tables; horizontal scroll inside the table container on small screens,
  or switch to a stacked card layout below ~640px.
- Sorting is shown in the header with direction; sort, filter and page are in the URL.
- Row actions: a visible primary action or an overflow menu ("More actions" accessible name);
  bulk actions appear when rows are selected.
- Empty table: keep headers, show an empty state inside the body.
- Truncate long cells with an ellipsis and expose the full value (title attribute is not
  enough on touch; provide a detail view or wrap).

## Cards

- Use a card when the item is a self-contained, often clickable object. Do not wrap every
  section in a card.
- If the whole card is clickable, make it one link (stretched link pattern) with any inner
  buttons layered above; do not nest interactive elements inside an `<a>`.
- Padding 16–24px; inner radius concentric with the card's radius.
- Vary card size or emphasis to show priority. A grid of identical cards is a list, design it
  like one.

## Dialogs (modal)

- For decisions that must be made now, or short focused tasks. Not for content people need to
  reference while working elsewhere (use a side panel / drawer instead).
- Title states the question or task ("Delete project?"). Body explains the consequence in one or
  two sentences. Actions name the outcome ("Delete project" / "Cancel").
- Width 400–560px for confirmations, up to ~720px for forms; full-screen sheet on mobile.
- Focus moves into the dialog (to the first field or the least destructive action), is trapped,
  Escape closes, focus returns to the trigger. Backdrop uses `--overlay`.
- Never stack dialogs. Never open a dialog on page load uninvited.

## Drawers / side panels / sheets

- For detail views, filters, and editing while keeping context. Width 360–480px on desktop.
- The underlying list stays visible; the selected row is highlighted; the URL reflects the open
  item.

## Menus and popovers

- Open from their trigger, aligned to it, with `transform-origin` at the trigger.
- Menu items: icon (optional), label, shortcut (right-aligned, muted). Destructive items last,
  separated, in danger color.
- Keyboard: arrows move, Enter selects, Escape closes and refocuses the trigger, typeahead
  jumps to items.

## Tabs and navigation

- Tabs switch between views of the same object; they do not navigate to different sections of
  the app (use navigation for that). Selected tab is clearly marked with more than color
  (indicator bar, weight).
- Primary navigation: 5–7 top-level items maximum. Current location is indicated
  (`aria-current="page"`).
- Mobile: bottom tab bar for 3–5 primary destinations in app-like products; a menu button for
  content sites.
- Breadcrumbs for deep hierarchies; the last item is the current page and not a link.

## Toasts and notifications

- For brief confirmation of something the user just did ("Invoice sent"), optionally with one
  action ("Undo", "View").
- Bottom center on mobile, bottom or top corner on desktop; one position for the whole product.
- Auto-dismiss after ~4–6s, longer if there is an action; pause on hover and focus; never
  auto-dismiss errors that need action.
- Announced via a polite live region. Do not put critical errors or required decisions in a
  toast; use inline messages or a dialog.

## Tooltips

- Short label for icon-only controls or to reveal a keyboard shortcut. Appear on hover and
  focus after a short delay (~300–500ms), only the first in a group is delayed.
- Never contain interactive content or essential information.

## Badges, tags, status

- Status uses color + text (+ icon): "Active", "Failed", "Pending". Use the `-subtle` fill with
  the semantic color text from `tokens.md`.
- Keep them small (20–24px high) and few; a badge on everything is noise.

## Empty states

- Three kinds, designed separately:
  1. **First use**: explain the value of the feature and give the primary action that starts it.
  2. **No results**: echo the query/filters, offer to clear or broaden them.
  3. **Cleared/done**: a calm confirmation ("All caught up").
- Optional simple illustration or icon; no stock "empty box" clip art at huge size.

## Loading

- Skeletons match the real layout (same row heights, same column widths), animate subtly
  (shimmer or pulse at low contrast), and are replaced without layout shift.
- Button-level spinners for actions; page-level progress bar for navigations that take more
  than ~300ms.
- Never block the whole screen for a background refresh.

## Avatars and images

- Fixed aspect ratios, `object-fit: cover`, reserved space, a neutral fallback (initials on a
  tinted background derived from the name).
- Meaningful images have `alt` text describing their content; decorative ones `alt=""`.

## Icons

- One set, one stroke width (1.5 or 2px at 24px), one corner style. Sizes 16, 20, 24.
- Icons support labels; they rarely replace them. Icon-only only for universally understood
  actions (close, search, more, menu) and always with an accessible name.
- Align icons to text optically; center them on the cap height, not the line box.
