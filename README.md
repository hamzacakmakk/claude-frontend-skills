# Frontend Skills for Claude Code

Agent Skills that make Claude Code design interfaces the way a careful product designer would:
decide on a direction first, build on a token system, cover every state, meet accessibility
requirements, and avoid the look that gives AI-generated UI away.

The rules are distilled from public design guidance by Apple, Meta, Vercel, Google (Material 3),
GitHub (Primer), Microsoft (Fluent 2), the Refactoring UI book and WCAG 2.2, rewritten into
one opinionated, consistent rule set.

## Why

Ask a coding agent for "a landing page" or "a settings screen" and you tend to get the same
thing: a purple-to-blue gradient, a centered headline over three identical feature cards with
icons in tinted circles, glowing shadows, emoji as icons, invented "10,000+ users" stats, and
gray text that fails contrast. It renders, but it looks like every other generated page, and it
usually skips focus states, empty and error states, and keyboard support.

These skills give the agent what a design team would: a workflow, explicit defaults, a list of
patterns to avoid, ready-made tokens with checked contrast, and a review pass that runs before
the work is reported as done.

## What's inside

```
skills/
├── frontend-design/                 Main skill: build or restyle any web UI
│   ├── SKILL.md                     Workflow, anti-slop rules, defaults, a11y floor
│   └── references/                  Loaded only when relevant
│       ├── tokens.md                CSS variables: spacing, type, radius, shadow, motion,
│       │                            light/dark palettes with measured contrast, accent sets
│       ├── components.md            Do/don't for buttons, inputs, tables, dialogs, toasts...
│       ├── web-interface-guidelines.md  Focus, forms, loading, URL state, motion, layout
│       ├── review-checklist.md      Pre-delivery checklist with blocker items
│       ├── apple-hig.md             Apple HIG distilled for the web
│       ├── meta.md                  What Meta's public design guidance emphasizes
│       ├── dashboards.md            Data-dense screens, metric tiles, charts
│       └── reference-analysis.md    Working from a screenshot or "make it like X"
├── ui-review/                       Audit an existing UI, get prioritized fixes (P0-P3)
│   ├── SKILL.md
│   └── references/fix-mode.md       How to apply the fixes safely
├── design-system-generator/         Token architecture, themes, docs, migration
│   └── SKILL.md
└── frontend-architect/              Component hierarchy, state, folders, budgets
    └── SKILL.md
```

| Skill | Use it when you want to |
|---|---|
| `frontend-design` | Build a page, app screen, dashboard or component, or restyle one |
| `ui-review` | Find out what is wrong with an existing UI and get exact, prioritized fixes |
| `design-system-generator` | Create or extend tokens, themes and a short `DESIGN.md` |
| `frontend-architect` | Structure components, state, data fetching and folders |

Each skill is plain Markdown with YAML frontmatter (`name`, `description`). Claude loads the
`SKILL.md` when a request matches the description and reads reference files only when the task
needs them, so the context cost stays small.

## Install (Claude Code)

Personal install, available in every project:

```bash
git clone https://github.com/hamzacakmakk/claude-frontend-skills.git
mkdir -p ~/.claude/skills
cp -r claude-frontend-skills/skills/* ~/.claude/skills/
```

Project install, shared with your team through the repository:

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-frontend-skills/skills/frontend-design .claude/skills/
cp -r /path/to/claude-frontend-skills/skills/ui-review .claude/skills/
```

On Windows (PowerShell), the personal folder is `$HOME\.claude\skills`:

```powershell
git clone https://github.com/hamzacakmakk/claude-frontend-skills.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse claude-frontend-skills\skills\* "$HOME\.claude\skills\"
```

Restart Claude Code (or start a new session) and run `/skills` to confirm they are listed.

## Use

Describe the work and the matching skill loads on its own:

```
Build the pricing page for our invoicing app in Next.js and Tailwind.
Review src/app/settings and tell me what to fix first.
Set up design tokens for this project with light and dark themes.
```

Or call one explicitly:

```
/frontend-design  an onboarding flow for a team calendar app
/ui-review        src/components/Checkout.tsx
```

## Using it with other agents

Nothing here is specific to one tool. For Cursor, Windsurf, Copilot, Codex, Gemini CLI or any
chat model, paste `skills/frontend-design/SKILL.md` into the project rules or system prompt
(for example `AGENTS.md`, `.cursor/rules/`, or a custom instruction), and add the reference files
you need, such as `tokens.md` and `review-checklist.md`. Remove the frontmatter if the tool does
not understand it.

## Before and after

Prompt: *"Make a landing page for a small accounting tool."*

**Without the skill**, a typical result: a dark hero with a violet-to-blue gradient and gradient
headline text, "Revolutionize your finances" with two centered buttons, three identical glass
cards with emoji icons, a "Trusted by 10,000+ businesses" strip with placeholder logos, every
section fading up on scroll, light gray body text at about 3:1 contrast, and no focus styles.

**With the skill**, the agent first writes a six-line brief (job, tone, type, color, density,
one signature element), for example: calm and precise, system sans with tabular numbers, warm
neutrals with a single forest-green accent, the product's real invoice view as the hero. It then
builds with tokens on a 4px scale, uses real copy about what the tool does, leaves clearly marked
slots instead of invented testimonials, adds focus, empty and error states, checks contrast
numerically, and runs the review checklist before reporting.

## Sources and credits

The rule set is a synthesis written in our own words. Numbers such as target sizes and contrast
ratios come from these sources; the texts themselves belong to their authors.

- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Meta Horizon OS design guidelines: https://developers.meta.com/horizon/design/
  (web apps and panels: https://developers.meta.com/horizon/design/pwa/, hit targets:
  https://developers.meta.com/horizon/design/styles_inputs_hit_targets/, accessibility:
  https://developers.meta.com/horizon/design/accessibility/)
- Design at Meta: https://www.meta.com/design-at-meta/
- React, Thinking in React: https://react.dev/learn/thinking-in-react
- StyleX: https://stylexjs.com/
- Vercel Web Interface Guidelines: https://vercel.com/design/guidelines and
  https://github.com/vercel-labs/web-interface-guidelines
- VoltAgent awesome-design-md (DESIGN.md analyses of Apple, Meta, Stripe, Linear, Vercel and
  others): https://github.com/VoltAgent/awesome-design-md
- Anthropic's `frontend-design` skill: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Material Design 3: https://m3.material.io/
- GitHub Primer: https://primer.style/
- Microsoft Fluent 2 (layout and 4px spacing ramp): https://fluent2.microsoft.design/layout
- Refactoring UI by Adam Wathan and Steve Schoger: https://www.refactoringui.com/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/ and Target Size (Minimum):
  https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/

This project is not affiliated with or endorsed by any of the companies above. Brand names are
used only to identify the guidance being referenced.

## Contributing

Issues and pull requests are welcome, especially rules backed by a public source, corrections to
numbers, and before/after examples. Keep `SKILL.md` files short and move detail into reference
files.

## License

MIT. See [LICENSE](LICENSE).
