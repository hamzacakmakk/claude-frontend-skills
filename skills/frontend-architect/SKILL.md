---
name: frontend-architect
description: Plan or restructure frontend architecture - component hierarchy, folder structure, state management, data fetching, styling strategy and performance budgets - for React, Next.js, Vue, Svelte and similar apps. Use when the user asks how to structure a frontend, split components, manage state, organize a growing codebase, or set up a scalable UI foundation.
---

# Frontend Architect

Design the simplest structure that will still make sense when the codebase is five times larger.
Prefer boring, well-understood patterns. Every layer you add must remove more complexity than it
introduces.

## 1. Understand before structuring

- Read the existing app: framework and router, rendering mode (SPA, SSR, RSC, static), data
  sources, current state libraries, styling approach, tests, build tooling.
- Identify the core user flows and the data each needs. Architecture follows the data.
- Note constraints: team size, SEO needs, offline needs, real-time needs, performance budget.

## 2. Components: one job each

Follow the approach React's documentation calls "Thinking in React":

1. Break the UI into a hierarchy; each component does one thing. If a component needs a long
   description, split it.
2. Build a static version from data first.
3. Find the **minimal** state. Anything derivable from props or other state is computed, not
   stored.
4. Put each piece of state in the closest common owner of the components that use it.
5. Pass callbacks down; data flows one way.

Layers of components:

- **Primitives**: Button, Input, Select, Dialog, Tooltip. Accessible, token-styled, no business
  logic. Prefer a headless library (Radix, React Aria, Headless UI, Ark) over hand-rolled
  focus management.
- **Patterns**: FormField, DataTable, EmptyState, PageHeader. Compose primitives.
- **Features**: InvoiceList, BillingSettings. Own data fetching and business rules for one
  domain.
- **Routes/pages**: compose features; handle params, layout and loading boundaries.

Composition over configuration: prefer `children`/slots to components with twenty boolean props.

## 3. State: classify it first

| Kind | Where it lives |
|---|---|
| Server state (data from APIs) | A cache library: TanStack Query, SWR, RTK Query, or framework loaders / server components. Never copied into a global store. |
| URL state (filters, tabs, pagination, selected item) | The URL (search params, route params). |
| Form state | The form library (React Hook Form, Conform, native forms + actions) or uncontrolled inputs. |
| Local UI state (open/closed, hover) | Component state. |
| Shared client state (session, preferences, multi-step drafts) | Context for low-frequency values; Zustand/Jotai/Redux only when many distant components update it often. |

Optimistic updates for low-risk mutations, with rollback on error. Idempotent mutations for
anything a double click could repeat.

## 4. Folder structure

Organize by feature, with a thin shared layer:

```
src/
  app/ or routes/        # routing, layouts, loading/error boundaries
  features/
    billing/
      components/
      api.ts             # queries and mutations for this domain
      hooks.ts
      types.ts
      index.ts           # public surface of the feature
  components/ui/         # primitives and patterns (design system)
  lib/                   # framework-agnostic helpers, api client
  styles/                # tokens.css, global resets
```

Rules: features import from `components/ui` and `lib`, never from another feature's internals
(go through its `index.ts`). No `utils.ts` dumping ground; name helpers by what they do.

## 5. Styling strategy

- Tokens as CSS custom properties are the single source of truth (see the `frontend-design`
  skill's `tokens.md` or the `design-system-generator` skill).
- Pick one styling approach for the codebase: Tailwind mapped to tokens, CSS Modules, or a
  zero-runtime CSS-in-JS / atomic system (vanilla-extract, StyleX, Panda). Avoid runtime
  CSS-in-JS in performance-sensitive or server-rendered apps.
- Keep specificity flat; variants are props, not cascade overrides.

## 6. Performance and quality budgets

- Set budgets: LCP < 2.5s, INP < 200ms, CLS < 0.1 on a mid-range phone; JS per route budget.
- Code-split by route; lazy-load heavy, below-the-fold or interaction-only components.
- Reserve space for async content; virtualize long lists; move heavy work off the main thread.
- Images: modern formats, explicit sizes, responsive `srcset`, priority only for the LCP image.
- Fonts: self-hosted, subset, preloaded sparingly, `font-display: swap`.
- Accessibility is architecture: primitives own focus management and ARIA so features cannot
  get it wrong. Add automated checks (axe in tests, eslint-plugin-jsx-a11y) to CI.
- Error boundaries per route and per independent widget; one failure never blanks the app.

## 7. Output

Deliver: a short architecture summary (stack, rendering mode, state classification), the folder
tree, the component hierarchy for the main flows, the data-fetching approach, and a migration
plan in small, shippable steps if restructuring an existing app. Call out trade-offs and what you
deliberately did not add.

## Checklist

- [ ] Each piece of state has one owner and one kind (server, URL, form, local, shared).
- [ ] Server data is cached, not copied into global stores.
- [ ] Features are isolated behind a public index; primitives have no business logic.
- [ ] One styling approach, driven by tokens.
- [ ] Route-level code splitting and loading/error boundaries exist.
- [ ] Performance budgets and accessibility checks are defined and automated where possible.
