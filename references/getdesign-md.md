# DESIGN.md — Brand Reference System

## What It Is

DESIGN.md is a plain-markdown design system format introduced by Google Stitch. A single `.md` file describes a brand's full visual language — colors, typography, spacing, components — in a format AI agents can read and act on directly.

**getdesign.md** is a community-maintained catalog (91k+ GitHub stars) of 328+ DESIGN.md files for real-world brands. Drop one into a project and tell the agent `use DESIGN.md as reference before writing any UI`.

GitHub: `https://github.com/VoltAgent/awesome-design-md`
Web: `https://getdesign.md/`

---

## How to Fetch a Brand

```bash
# fetch to project root (creates DESIGN.md)
npx getdesign@latest add <brand>

# examples
npx getdesign@latest add stripe
npx getdesign@latest add vercel
npx getdesign@latest add linear
npx getdesign@latest add notion
```

After fetching, tell the agent:
> "Use DESIGN.md as the design reference for all UI work."

The agent reads the file before writing any UI — font, color, spacing, component style all come from it rather than from generic defaults.

---

## DESIGN.md File Structure (9 Sections)

A DESIGN.md has two halves: a **YAML front matter block** (structured tokens) and a **prose body** (rationale).

### Front Matter (YAML tokens)

```yaml
---
version: alpha
name: Lumenpath
description: A warm, cream-canvas editorial interface with a single
  Tangerine accent. Hairline borders, modest weights, sparse color.

colors:
  primary: "#F76B1C"
  ink: "#1B1A17"
  body: "#3D3A33"
  muted: "#7A7568"
  canvas: "#FFFAF1"
  surface-card: "#FFFFFF"
  hairline: "#E8E1D2"
  on-primary: "#FFFFFF"

typography:
  display-lg:
    fontFamily: "'Söhne', Inter, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1.8px
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  button:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  sm: 6px
  md: 10px
  lg: 16px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 20px
---
```

### Prose Body Sections

| Section | Answers |
|---------|---------|
| `## Overview` | Why does it look like this? Brand atmosphere, key characteristics |
| `## Colors` | Where does each color apply and why? Grouped: Brand, Surface, Hairlines, Text, Semantic |
| `## Typography` | Font family, full hierarchy table, principles, font substitutes |
| `## Layout` | Spacing system, grid/container widths, whitespace philosophy |
| `## Elevation` | Surface tiers, shadow definitions |
| `## Components` | 1:1 match with YAML components block — surface, type, padding, radius, states |
| `## Responsive Behavior` | Breakpoint table, touch targets, collapsing strategy |
| `## Known Gaps` | What the file does NOT cover (animation, error states, dark mode, etc.) |

Token references use `{colors.primary}`, `{typography.button}`, `{rounded.md}` syntax throughout prose.

---

## Color Token Vocabulary

DESIGN.md uses semantic names, never numeric scales:

| Token Name | Role |
|------------|------|
| `primary` | Brand CTA, accent, links |
| `primary-active` | Pressed/active state of primary |
| `primary-disabled` | Disabled primary |
| `ink` | Darkest text, headings |
| `body` | Default body text |
| `muted` | Subdued/secondary text |
| `muted-soft` | Placeholder, caption |
| `hairline` | Default borders |
| `hairline-soft` | Dividers, subtle separators |
| `canvas` | Page background floor |
| `surface-soft` | Slightly elevated background |
| `surface-card` | Card plates |
| `surface-cream-strong` | Stronger card tint |
| `surface-dark` | Dark-mode base |
| `surface-dark-elevated` | Dark-mode elevated surface |
| `on-primary` | Text on primary-colored surfaces |
| `on-dark` | Text on dark surfaces |

---

## Brand Catalog (328+ entries)

### Productivity & SaaS
`notion`, `airtable`, `cal`, `superhuman`, `miro`, `intercom`, `zapier`, `linear.app`

### Developer Tools
`vercel`, `supabase`, `cursor`, `raycast`, `warp`, `posthog`, `sentry`, `hashicorp`, `expo`, `sanity`, `mintlify`, `framer`, `figma`, `webflow`, `clickhouse`, `mongodb`, `ibm`, `opencode.ai`

### AI & ML
`claude`, `cohere`, `mistral.ai`, `x.ai`, `minimax`, `replicate`, `runwayml`, `elevenlabs`, `together.ai`, `ollama`, `composio`

### Fintech
`stripe`, `coinbase`, `binance`, `kraken`, `revolut`, `wise`, `mastercard`

### Design & Creative
`figma`, `framer`, `clay`, `lovable`, `webflow`, `linear.app`

### E-commerce
`shopify` (use `polaris` system), `nike`, `starbucks`

### Media & Consumer
`spotify`, `discord`, `slack`, `pinterest`, `theverge`, `wired`

### Automotive & Luxury
`tesla`, `spacex`, `ferrari`, `bugatti`, `lamborghini`, `bmw`, `bmw-m`, `renault`, `vodafone`

### Legacy/Archival
`apple`, `dell-1996`, `hp`, `nintendo-2001`

Browse full catalog: `https://getdesign.md/design-md`

---

## Integration with This Skill

### When to Use a DESIGN.md

Use a brand DESIGN.md when the user says one of:
- "Make it look like [Brand]"
- "Give it a [Brand] feel"
- "Inspired by [Brand]"
- "Similar to [Brand] style"
- "Match [Brand]'s design language"

### Mapping DESIGN.md to Skill Systems

After fetching a DESIGN.md, map its aesthetic to the closest skill system for structural guidance:

| Brand Aesthetic | Closest Skill System | Override Source |
|-----------------|----------------------|-----------------|
| Vercel, Linear, Raycast | `minimal` | DESIGN.md colors + type |
| Stripe, Wise | `minimal` or `ant` | DESIGN.md components |
| Notion, Airtable | `ant` or `atlassian` | DESIGN.md colors |
| Figma, Framer | `minimal` or `neo-m3` | DESIGN.md type scale |
| Supabase, Posthog | `carbon` | DESIGN.md color surface |
| Claude, Cohere | custom editorial | full DESIGN.md |
| Spotify, Discord | `glassmorphism` + `material` | DESIGN.md primary accent |
| Nike, Tesla | `swiss` or `swiss-archival` | DESIGN.md type + canvas |

**Rule:** The skill system provides structural patterns (grid, density, behavior). The DESIGN.md overrides all visual tokens (colors, typography, radius, spacing).

### Workflow When DESIGN.md is Present

```
1. Run: npx getdesign@latest add <brand>
2. Parse DESIGN.md front matter — extract colors, typography, rounded, spacing, components
3. Identify closest structural system (see table above)
4. Open that system's reference file for layout + behavior patterns
5. Apply DESIGN.md tokens wherever the system reference uses defaults
6. Apply DESIGN.md component definitions over skill component patterns
7. Note any Known Gaps in the DESIGN.md and flag them to the user
```

### Custom DESIGN.md

If no matching brand exists or the user has a proprietary brand:
- Tell user to run: `npx getdesign@latest` (shows write-your-own guide)
- Or request via: `https://getdesign.md/request`
- Or reference the 9-section structure above and draft one manually

---

## What DESIGN.md Is NOT

- Not a component library (no code, just rules)
- Not a Figma export (carries rationale, not just values)
- Not official brand guidelines (independent analysis of publicly observable patterns)
- Not static (version, PR, diff it like code)

---

## Quick Token Extraction (Shell)

If the agent needs to extract tokens from a DESIGN.md file programmatically:

```bash
# extract colors block from DESIGN.md
awk '/^colors:/,/^[a-z]/' DESIGN.md | head -30

# extract primary color
grep 'primary:' DESIGN.md | head -1

# extract all component names
grep -E '^  [a-z-]+:$' DESIGN.md | grep -A 100 'components:' | grep -E '^  [a-z-]+:$'
```
