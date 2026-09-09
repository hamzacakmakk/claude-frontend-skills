# Frontend Skills for Claude Code

Seven [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) that push Claude Code toward
production-grade frontend work — premium visual design, scalable architecture, and honest design critique
instead of the generic layouts an LLM reaches for by default.

Each skill is a single `SKILL.md` that Claude loads on demand when your request matches its description.
No dependencies, no build step, nothing to run.

## The skills

| Skill | Use it when you want to… |
|---|---|
| **frontend-designer** | Design a premium interface from scratch — the Apple/Stripe/Linear tier, not the bootstrap tier |
| **frontend-architect** | Structure a codebase: component primitives, state management, data-fetching boundaries |
| **design-system-generator** | Produce a full token-driven design system — color, type, spacing, shadows, plus docs |
| **design-reference-analyzer** | Feed Claude a screenshot or Figma frame and get its design DNA extracted before rebuilding it |
| **dashboard-designer** | Lay out analytics and data-heavy screens with real information hierarchy |
| **product-ui-critic** | Get specific, actionable design critique on UI you already have |
| **ui-refactor** | Turn amateur UI code into production-grade markup and modern CSS |

They compose. A typical run is `design-reference-analyzer` → `design-system-generator` →
`frontend-designer` → `product-ui-critic`.

## What they enforce

Every design and code skill here shares a common bar, so output stays consistent no matter which one fires:

- **Accessibility** — WCAG AA contrast, focus states, semantic markup, keyboard paths
- **Responsive by default** — fluid layouts rather than fixed desktop widths
- **Token discipline** — spacing and color come from a scale, not from magic numbers
- **Motion with intent** — micro-interactions that give feedback, not decoration
- **No generic AI patterns** — the recurring purple-gradient-and-glassmorphism default is explicitly ruled out

## Install

Skills live in `~/.claude/skills/` (personal, all projects) or `.claude/skills/` (checked into one repo).

```bash
# All seven, personal scope
git clone https://github.com/hamzacakmakk/claude-frontend-skills.git /tmp/cfs
mkdir -p ~/.claude/skills
cp -r /tmp/cfs/*/ ~/.claude/skills/
```

Or take just the ones you want:

```bash
cp -r /tmp/cfs/frontend-designer ~/.claude/skills/
```

Verify with `/skills` inside Claude Code — the installed skills appear in the list.

## Use

Invoke one by name:

```
/frontend-designer  a settings page for a subscription billing app
```

Or just describe the work and let Claude pick — the `description` field in each `SKILL.md` is what it
matches against:

```
Here's a screenshot of a dashboard I like. Rebuild the layout in React and Tailwind.
```

## Layout

```
.
├── dashboard-designer/SKILL.md
├── design-reference-analyzer/SKILL.md
├── design-system-generator/SKILL.md
├── frontend-architect/SKILL.md
├── frontend-designer/SKILL.md
├── product-ui-critic/SKILL.md
└── ui-refactor/SKILL.md
```

Each file is plain Markdown with YAML frontmatter (`name`, `description`) followed by the instructions
Claude receives. Editing one is just editing prose — tune the standards to your own taste and the change
takes effect on the next run.

## License

MIT — use them, fork them, rewrite them.
