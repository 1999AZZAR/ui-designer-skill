# Quick Reference - Design System Scoring Map

Use this file as the main map. Do not pick a system from visual taste alone. Score candidates from product needs, then open only the best matching reference file or files.

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
| Android or adaptive modern app | `material`, `m3-pastel` | `references/material-you.md` |
| Admin panel, CMS, internal tool, back-office | `ant`, `carbon`, `atlassian` | `references/ant-design.md` |
| Collaboration or project management | `atlassian`, `carbon` | `references/atlassian-design.md` |
| Merchant or commerce operations | `polaris`, `ant` | `references/shopify-polaris.md` |
| Content, editorial, portfolio, typography-led site | `minimal`, `swiss`, `neo-m3` | `references/minimalism.md` |
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

## Page Archetype Routing

After choosing a system, route to the closest page archetype:

- Overview, KPI, analytics, product home: `assets/archetypes/dashboard.md`
- Preferences, account, configuration, permissions: `assets/archetypes/settings.md`
- List plus record inspection/editing: `assets/archetypes/table-detail.md`
- Landing page, campaign, splash, launch: `assets/archetypes/marketing-hero.md`
- Story-led, content-led, typography-first page: `assets/archetypes/editorial-landing.md`

## Anti-Misuse Checks

- Do not use `glass`, `claymorphism`, `neumorphism`, or `skeuomorphism` as the sole system for dense back-office workflows.
- Do not use `ant` or `carbon` alone when the product clearly depends on strong brand expression unless that restraint is intentional.
- Do not create hybrids with no ownership split.
- Do not pick a system only because it is trendy.

## Apply Command

```bash
python3 scripts/apply_ui_rules.py --style [fluent|ant|carbon|atlassian|apple-hig|polaris|material|minimal|glass|neumorphism|neo-brutalism|claymorphism|skeuomorphism|swiss|m3-pastel|neo-m3] --palette [pastel|dark|vibrant|mono]
```
