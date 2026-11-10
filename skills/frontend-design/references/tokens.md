# Tokens

Ready-to-paste CSS custom properties. Use them when the project has no token system of its own.
If it has one, map these ideas onto it instead of adding a second set.

Rules for using tokens:

- Components reference **semantic** tokens (`--text-muted`, `--surface-raised`), never raw values.
- Change the look by swapping the accent block or the neutral ramp, not by editing components.
- Add a token only when a value is needed in two or more places.

## 1. Spacing (4px base)

```css
:root {
  --space-0: 0;
  --space-px: 1px;
  --space-0-5: 2px;   /* hairline gaps, icon nudges */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;

  --gutter: clamp(16px, 4vw, 48px);      /* page side padding */
  --section-gap: clamp(48px, 8vw, 128px); /* between page sections */
  --content-max: 1200px;
  --reading-max: 70ch;
}
```

Rule of thumb: inside a component 4–16, between components 16–32, between sections 48–128.
The gap between groups should be clearly larger (at least 1.5–2x) than the gap inside a group.

## 2. Type

```css
:root {
  /* Stacks: system first. Swap --font-sans for a licensed web font if the brand needs one. */
  --font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
               Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  --font-serif: ui-serif, "Iowan Old Style", "Charter", "Georgia", "Times New Roman", serif;
  --font-mono: ui-monospace, "SF Mono", "Cascadia Code", "JetBrains Mono", Menlo, Consolas, monospace;

  /* Scale ~1.25 (major third), anchored at 16px. Display sizes are fluid. */
  --text-xs: 0.75rem;    /* 12 / 16  captions, meta */
  --text-sm: 0.875rem;   /* 14 / 20  secondary, dense UI */
  --text-base: 1rem;     /* 16 / 24  body */
  --text-md: 1.125rem;   /* 18 / 28  lead paragraph, comfortable body */
  --text-lg: 1.25rem;    /* 20 / 28  small headings */
  --text-xl: 1.5rem;     /* 24 / 32  section headings */
  --text-2xl: clamp(1.75rem, 1.4rem + 1.2vw, 2.25rem);  /* 28-36 page title */
  --text-3xl: clamp(2.25rem, 1.6rem + 2.4vw, 3.5rem);   /* 36-56 hero */
  --text-4xl: clamp(2.75rem, 1.8rem + 4vw, 4.5rem);     /* 44-72 display, use once */

  --leading-tight: 1.15;
  --leading-snug: 1.3;
  --leading-normal: 1.5;
  --leading-relaxed: 1.65;

  --tracking-display: -0.02em;
  --tracking-heading: -0.01em;
  --tracking-normal: 0;
  --tracking-caps: 0.06em; /* only for genuinely uppercase short labels */

  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
}

body {
  font-family: var(--font-sans);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
h1, h2, h3 { text-wrap: balance; letter-spacing: var(--tracking-heading); line-height: var(--leading-tight); }
p { text-wrap: pretty; max-width: var(--reading-max); }
.num, td, .stat { font-variant-numeric: tabular-nums; }
```

Dense apps (tables, admin) can use a 1.2 ratio with 14px as the UI base and 16px for reading
text. Editorial and marketing pages can push to 1.333–1.5 for display sizes.

## 3. Radius, borders, shadows

```css
:root {
  /* Pick ONE family and stick to it. Shown: "soft". */
  --radius-xs: 4px;   /* checkboxes, small tags */
  --radius-sm: 6px;   /* inputs, buttons */
  --radius-md: 10px;  /* cards, menus */
  --radius-lg: 14px;  /* dialogs, sheets */
  --radius-full: 9999px; /* pills, avatars, switches */
  /* Sharp family: 0 / 2 / 4 / 6. Round family: 8 / 12 / 16 / 24. */

  --border-width: 1px;
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;

  /* Two layers: contact + ambient. Neutral, low opacity. */
  --shadow-sm: 0 1px 2px rgb(20 20 18 / 0.06), 0 1px 1px rgb(20 20 18 / 0.04);
  --shadow-md: 0 2px 4px rgb(20 20 18 / 0.06), 0 6px 16px rgb(20 20 18 / 0.08);
  --shadow-lg: 0 4px 8px rgb(20 20 18 / 0.06), 0 16px 40px rgb(20 20 18 / 0.14);
}
```

Use `--shadow-sm` for raised interactive cards, `--shadow-md` for menus and popovers,
`--shadow-lg` for dialogs. Content panels usually need no shadow at all.

## 4. Motion

```css
:root {
  --duration-instant: 80ms;
  --duration-fast: 140ms;   /* hover, press, toggles */
  --duration-base: 220ms;   /* enter, expand */
  --duration-slow: 320ms;   /* large surfaces, page-level */
  --ease-out: cubic-bezier(0.2, 0.8, 0.2, 1);     /* entering */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);          /* leaving */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);  /* moving on screen */
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## 5. Layers

```css
:root {
  --z-base: 0;
  --z-sticky: 100;
  --z-dropdown: 200;
  --z-overlay: 300;
  --z-dialog: 400;
  --z-toast: 500;
  --z-tooltip: 600;
}
```

## 6. Color: neutral ramp + one accent, light and dark

Contrast ratios below were computed with the WCAG 2 relative-luminance formula. Body text
needs 4.5:1, large text and meaningful non-text UI (input borders, icons, focus rings) 3:1.

```css
:root {
  color-scheme: light dark;

  /* Neutrals (light) - very slightly warm */
  --bg: #FAFAF9;
  --surface: #FFFFFF;          /* cards, inputs */
  --surface-sunken: #F3F3F1;   /* wells, table headers, code */
  --border: #E3E3DF;           /* dividers, card outlines (decorative) */
  --border-strong: #86867F;    /* input borders, meaningful outlines (3:1+) */
  --text: #1A1A18;
  --text-muted: #55554F;
  --text-subtle: #6B6B65;      /* placeholders, meta; still 4.5:1 on --bg */
  --overlay: rgb(20 20 18 / 0.48);

  /* Accent: Cobalt (swap with a set from the table below) */
  --accent: #2253D1;
  --accent-hover: #1D46B3;
  --accent-fg: #FFFFFF;        /* text on accent */
  --accent-text: #2253D1;      /* links, accent text on --bg */
  --accent-subtle: #EAF0FF;    /* selected rows, soft badges */
  --focus-ring: #2253D1;

  /* Semantic */
  --success: #147A3A;  --success-subtle: #E8F6EC;
  --warning: #975905;  --warning-subtle: #FDF3D7;
  --danger:  #C81E1E;  --danger-subtle:  #FDECEC;
  --info:    #1D4ED8;  --info-subtle:    #E8EEFD;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0E0E10;
    --surface: #161619;
    --surface-sunken: #1D1D21;
    --border: #2A2A30;
    --border-strong: #6E6E79;
    --text: #EDEDEF;
    --text-muted: #A3A3AD;
    --text-subtle: #8C8C96;
    --overlay: rgb(0 0 0 / 0.6);

    --accent: #7FA2FF;
    --accent-hover: #9AB6FF;
    --accent-fg: #0E0E10;
    --accent-text: #7FA2FF;
    --accent-subtle: #1A2440;
    --focus-ring: #7FA2FF;

    --success: #4ADE80;  --success-subtle: #12291B;
    --warning: #FACC15;  --warning-subtle: #2C2408;
    --danger:  #F87171;  --danger-subtle:  #2E1414;
    --info:    #60A5FA;  --info-subtle:    #13203A;

    --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.4);
    --shadow-md: 0 4px 12px rgb(0 0 0 / 0.45);
    --shadow-lg: 0 12px 32px rgb(0 0 0 / 0.55);
  }
}
/* Mirror the dark block under :root[data-theme="dark"] when a manual toggle exists. */
```

Measured contrast (light / dark):

| Pair | Light | Dark |
|---|---|---|
| `--text` on `--bg` | 16.7 | 16.5 |
| `--text-muted` on `--bg` | 7.2 | 7.7 |
| `--text-subtle` on `--bg` | 5.1 | 5.8 |
| `--text-subtle` on `--surface-sunken` | 4.8 | 5.1 |
| `--border-strong` on `--surface` | 3.7 | 3.6 |
| `--accent-fg` on `--accent` (button) | 6.5 | 7.8 |
| `--accent-text` on `--bg` (link) | 6.2 | 7.8 |
| `--danger` on `--bg` | 5.5 | 7.0 |
| `--success` on `--bg` | 5.2 | 11.1 |
| `--warning` on `--bg` | 5.4 | 12.6 |
| Semantic color on its own `-subtle` fill | 5.0 to 5.8 | 6.2 to 10.1 |

### Accent sets (swap the accent block)

Pick the hue for the product's tone, not because it is trendy. Each set keeps white text on
the light accent and near-black text on the dark accent above 4.5:1.

| Set | Tone | Light `--accent` / hover | Dark `--accent` | White on light accent |
|---|---|---|---|---|
| Cobalt | trustworthy, technical | `#2253D1` / `#1D46B3` | `#7FA2FF` | 6.5 |
| Forest | calm, finance, health | `#1E6B47` / `#18583A` | `#5FC995` | 6.5 |
| Teal | clinical, data, utility | `#0F6E73` / `#0B5A5E` | `#4FC7CC` | 6.0 |
| Vermilion | energetic, editorial, food | `#C2410C` / `#A6370A` | `#FF8A5C` | 5.2 |
| Ink | monochrome, premium, tools | `#1A1A18` / `#000000` | `#EDEDEF` | 17.4 |

For `--accent-subtle`, mix the accent into the background at roughly 8–12% in light mode and
15–20% into the surface in dark mode (`color-mix(in oklch, var(--accent) 10%, var(--bg))`).

### Verifying a new color

Do not eyeball contrast. Compute it (WCAG 2 formula) with a quick script or DevTools, e.g.:

```js
const lum = h => { const c = [1,3,5].map(i => parseInt(h.slice(i,i+2),16)/255)
  .map(v => v <= 0.04045 ? v/12.92 : ((v+0.055)/1.055)**2.4);
  return 0.2126*c[0] + 0.7152*c[1] + 0.0722*c[2]; };
const ratio = (a,b) => { const [x,y] = [lum(a),lum(b)].sort((p,q)=>q-p); return (x+0.05)/(y+0.05); };
ratio('#55554F', '#FAFAF9'); // 7.18
```

APCA is a useful second opinion for large or thin text, but WCAG 2 ratios remain the
compliance target.

## 7. Tailwind mapping

Tailwind v4 (`@theme`) can consume the same variables so utilities and custom CSS agree:

```css
@import "tailwindcss";
@theme inline {
  --color-bg: var(--bg);
  --color-surface: var(--surface);
  --color-sunken: var(--surface-sunken);
  --color-border: var(--border);
  --color-border-strong: var(--border-strong);
  --color-fg: var(--text);
  --color-muted: var(--text-muted);
  --color-subtle: var(--text-subtle);
  --color-accent: var(--accent);
  --color-accent-fg: var(--accent-fg);
  --radius-sm: var(--radius-sm);
  --radius-md: var(--radius-md);
  --radius-lg: var(--radius-lg);
}
```

Then write `bg-surface text-fg border-border`, not `bg-white text-gray-900 border-gray-200`.
In Tailwind v3 put the same mapping under `theme.extend.colors` in `tailwind.config`.
