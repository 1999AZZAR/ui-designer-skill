# Quick Reference - Design System Scoring Map

Use this file as the main map. Do not pick a system from visual taste alone. Score candidates from product needs, then open only the best matching reference file or files.

## Core Design Principles

### UI Principles
1. **Structural, Clear, and Tidy**: Logical hierarchy, alignment, and grouping.
2. **Clear and Understandable**: Purposeful elements, identifiable functions.
3. **Consistent and Coherent**: Shared patterns and styles across the UI.
4. **Purposeful and Relevant**: User-goal focused, no fluff.
5. **Adaptable and Responsive**: Seamless across devices and orientations.

### UX Principles
1. **Intuitive and User-Friendly**: Natural interactions, follows user mental models.
2. **Easy to Learn and Use**: Low cognitive load, clear navigation.
3. **Consistent around the UI**: Predictable behavior across all surfaces.
4. **Accessible and Inclusive**: Works for everyone, regardless of ability.
5. **Efficient and Effective**: Optimized for speed and accuracy.

## Design Flow
1. **Wireframe**: Establish structure, hierarchy, and flow before visual polish.
2. **Prototype**: High-fidelity implementation with interaction and logic.
3. **Test**: Validate against accessibility, responsiveness, and user goals.

## Scoring Rubric

Score each candidate from `1` to `5` on:

- `Product fit`: does it match the product category and workflow type?
- `Task density`: does it handle light, medium, or dense UI well?
- `Platform fit`: does it match native or expected platform patterns?
- `Brand fit`: does it support the needed level of distinctiveness?
- `Scalability`: will it hold up as screens, states, and roles grow?
- `Implementation fit`: is it realistic for the current codebase and team?

Use this decision rule:
- Pick a single system when one candidate clearly wins.
- Pick a hybrid only when one system wins structure/behavior and another wins brand/visual tone.
- If using a hybrid, explicitly assign ownership:
  - structure and layout
  - components and behavior
  - brand accents and hero surfaces

## Fast Routing

| Context | Strong Candidates | First File |
|---------|-------------------|------------|
| Windows or Microsoft-adjacent product | `fluent`, `carbon` | `references/fluent-design.md` |
| iOS or macOS-native feel | `apple-hig` | `references/apple-hig.md` |
| Android or adaptive modern app | `material`, `m3-pastel` | `references/material-you.md` (material), `references/m3-pastel-glass.md` (m3-pastel) |
| Admin panel, CMS, internal tool, back-office | `ant`, `carbon`, `atlassian` | `references/ant-design.md` |
| Collaboration or project management | `atlassian`, `carbon` | `references/atlassian-design.md` |
| Merchant or commerce operations | `polaris`, `ant` | `references/shopify-polaris.md` |
| Content, editorial, portfolio, typography-led site | `minimal`, `swiss`, `swiss-archival`, `neo-m3` | `references/minimalism.md` |
| Digital archive, museum, academic, research platform | `swiss-archival`, `swiss` | `references/swiss-archival.md` |
| Expressive or experimental brand surface | `neo-brutalism`, `glass`, `claymorphism`, `neo-m3` | `references/neo-brutalism.md` |
| Luxury, nostalgic, tactile product | `skeuomorphism` | `references/skeuomorphism.md` |

## Density And Behavior Matrix

| System | Product Fit | Density | Brand Intensity | Scalability | Notes |
|--------|-------------|---------|-----------------|-------------|-------|
| `ant` | admin, CMS, dashboard, ops | high | low-medium | high | strongest for workflow scaffolding and predictable behavior |
| `carbon` | enterprise, data-heavy, analytical | high | low | high | strongest for structure, alignment, and rigor |
| `atlassian` | collaboration, teamwork, project flows | medium-high | low-medium | high | strongest for shared task context |
| `fluent` | Windows-like enterprise apps | medium-high | low-medium | medium-high | best when Microsoft patterns matter |
| `apple-hig` | Apple-platform apps | medium | medium | medium | best for native-feeling calm interfaces |
| `polaris` | merchant tools, commerce admin | medium-high | medium | medium-high | friendly operations UI |
| `material` | adaptive app UI, modern product UI | medium | medium | medium-high | good default for modern app surfaces |
| `m3-pastel` | soft SaaS, creative tools | medium | medium-high | medium | material structure with gentler tone |
| `minimal` | content, portfolio, clean SaaS | low-medium | medium | medium | strongest when restraint matters |
| `swiss` | editorial, professional typography systems | low-medium | high | medium | strongest for grid and type clarity |
| `swiss-archival` | digital archive, museum, academic, research | medium | very high | medium | museum-grade tactile aesthetic with dual-font system, noise texture, and keyboard-first interaction |
| `glass` | hero, marketing, modern branded UI | low-medium | high | low-medium | poor choice for dense workflows alone |
| `neumorphism` | tactile niche controls | low | medium | low | do not use for dense enterprise UI |
| `claymorphism` | playful consumer UI | low | high | low-medium | use for simple friendly surfaces |
| `neo-brutalism` | artistic or loud digital brands | low-medium | very high | low-medium | brand-first, not workflow-first |
| `neo-m3` | editorial tech product, bold product branding | medium | high | medium | useful hybrid partner with structured systems |
| `skeuomorphism` | luxury, retro, tactile themes | low | very high | low | use narrowly and intentionally |

## Hybrid Patterns

Use these only when the split is explicit:

- `ant` + `neo-m3`
  - `ant` owns tables, forms, filters, drawers, notifications
  - `neo-m3` owns hero sections, high-level brand surfaces, special callouts

- `ant` + `glass`
  - `ant` owns product workflows
  - `glass` owns landing, dashboard highlight cards, atmospheric shells

- `carbon` + `minimal`
  - `carbon` owns dense operational components
  - `minimal` softens outer layout and marketing surfaces

- `material` + `m3-pastel`
  - `material` owns structure and behavior
  - `m3-pastel` softens color and surface language

- `polaris` + `swiss`
  - `polaris` owns commerce workflows, forms, tables, merchant operations
  - `swiss` owns typography system, editorial layout, grid rigor, brand expression
  - Best for: Commerce platforms that want editorial polish (luxury e-commerce, design-forward merchant tools)

- `polaris` + `swiss-archival`
  - `polaris` owns commerce operations, product management, order flows
  - `swiss-archival` owns brand surface, product storytelling, visual hierarchy, archival product catalogs
  - Best for: Heritage brands, artisan marketplaces, curated commerce with provenance/origin focus

## Page Archetype Routing

After choosing a system, route to the closest page archetype:

- Overview, KPI, analytics, product home: `assets/archetypes/dashboard.md`
- Preferences, account, configuration, permissions: `assets/archetypes/settings.md`
- List plus record inspection/editing: `assets/archetypes/table-detail.md`
- Landing page, campaign, splash, launch: `assets/archetypes/marketing-hero.md`
- Story-led, content-led, typography-first page: `assets/archetypes/editorial-landing.md`

## Cross-Cutting References

Apply these to ALL design system choices:

| Topic | Reference | When to Check |
|-------|-----------|---------------|
| Icons | `references/icon-guide.md` | Always (6 approved sources only) |
| Components | `references/component-patterns.md` | When building forms, tables, nav, modals |
| Tokens | `references/design-tokens.md` | When defining colors, spacing, type |
| Responsive | `references/responsive-layout.md` | When structuring layouts, breakpoints |
| Accessibility | `references/accessibility.md` | Before finalizing any design |
| Motion | `references/motion-design.md` | When adding animations, transitions |
| Tailwind | `references/tailwind-integration.md` | When using Tailwind CSS |

## Anti-Misuse Checks

- **NEVER use icons from unapproved sources.** Only use icons from: Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, or Heroicons. See `references/icon-guide.md`.
- Do not use `glass`, `claymorphism`, `neumorphism`, or `skeuomorphism` as the sole system for dense back-office workflows.
- Do not use `ant` or `carbon` alone when the product clearly depends on strong brand expression unless that restraint is intentional.
- Do not create hybrids with no ownership split.
- Do not pick a system only because it is trendy.
- Do not skip accessibility checks.
- Do not ignore `prefers-reduced-motion`.

## Brand Reference (DESIGN.md)

When the user wants to match a specific real-world brand's visual language, use **getdesign.md** instead of (or layered on top of) a system file.

### Fetch a Brand

```bash
# downloads DESIGN.md to project root
npx getdesign@latest add <brand>

# then tell agent: "use DESIGN.md as design reference"
```

### Brand → System Mapping (quick routing)

| Brand | Fetch Slug | Structural Backbone |
|-------|------------|---------------------|
| Vercel | `vercel` | `minimal` |
| Linear | `linear.app` | `minimal` |
| Stripe | `stripe` | `minimal` |
| Notion | `notion` | `ant` / `atlassian` |
| Figma | `figma` | `minimal` / `neo-m3` |
| Supabase | `supabase` | `carbon` |
| Raycast | `raycast` | `minimal` |
| Framer | `framer` | `minimal` |
| Claude | `claude` | custom editorial |
| Discord | `discord` | `glassmorphism` + `material` |
| Spotify | `spotify` | `glassmorphism` + `material` |
| Slack | `slack` | `atlassian` |
| Tesla | `tesla` | `swiss-archival` |
| SpaceX | `spacex` | `swiss` |
| Nike | `nike` | `swiss` |
| Shopify | `shopify` | `polaris` |
| Apple | `apple` | `apple-hig` |
| IBM | `ibm` | `carbon` |
| Coinbase | `coinbase` | `minimal` |
| Stripe | `stripe` | `minimal` |
| Warp | `warp` | `neo-brutalism` / `carbon` |
| Cursor | `cursor` | `minimal` |

Browse all 328 brands: `https://getdesign.md/design-md`

### How DESIGN.md and System Files Interact

**System file** provides: structural layout, density rules, grid, navigation patterns, component behavior
**DESIGN.md** overrides: all color tokens, typography scale, border-radius, spacing, component visual specs

When both are available, DESIGN.md tokens win on visual properties; the system file wins on structural decisions.

Full reference: `references/getdesign-md.md`

## Apply Command

```bash
python3 scripts/apply_ui_rules.py --style [fluent|ant|carbon|atlassian|apple-hig|polaris|material|minimal|glass|neumorphism|neo-brutalism|claymorphism|skeuomorphism|swiss|swiss-archival|m3-pastel|neo-m3] --palette [pastel|dark|vibrant|mono]
```

## Palette Sourcing

Optional. When the project needs a fresh swatch (or wants to explore alternatives to a built-in palette), invoke the **`color-palette-hunter`** skill (Color Hunt scraper; supports `--trending`, `--popular`, `--random`, `--theme <name>`, `--query <text>`, output `json|css|tailwind|html`). The skill is **not required** — if it is not installed in the current environment, skip the step and continue with the built-in palette for the chosen system.

Quick usage (path resolved by the skill loader):

```bash
# trending
color-palette-hunter/scripts/fetch-palette.sh --trending --limit 5

# by theme (modern, pastel, vibrant, dark, ...)
color-palette-hunter/scripts/fetch-palette.sh --theme pastel --limit 10

# free-form query
color-palette-hunter/scripts/fetch-palette.sh --query "warm archival" --format tailwind

# save as CSS variables
color-palette-hunter/scripts/fetch-palette.sh --trending --format css --output palette.css
```

Pick a winner, drop the hex list into `assets/palettes.json` under `systems.<style>`, and update the matching `references/<style>.md` color table. For Swiss-Archival specifically, also write the candidate into `assets/palettes/swiss-archival/` in the same shape (PNG / SVG / ASE / SCSS / TXT / Tailscale) so the loader index stays consistent. For M3 Pastel, write the candidate into `assets/palettes/m3-pastel/<n>/` (one numbered folder per candidate swatch: SVG / ASE / SCSS / TXT).
