---
name: ui-designer
description: Choose the best UI design system, or a deliberate combination of systems, for web or app interfaces. Use for dashboards, admin panels, internal tools, CMS, SaaS, websites, component theming, color systems, and frontend visual direction across Ant Design, Fluent, Carbon, Atlassian, Apple HIG, Material You, Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Swiss, Swiss-Archival, and related systems.
---

# UI Designer Skill

Use this skill when the user needs interface direction, design-system selection, theming, or visual/product UX structure before or during implementation.

## Operating Rules

- **CRITICAL: Icon Sources** — NEVER use icons from unapproved sources. Only these 6 are allowed: Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, Heroicons. See `references/icon-guide.md`.
- Choose systems from product context first, not visual mood first.
- Choose the best system for the job. Use a combination only when there is a clear reason and the roles of each system are explicit.
- Prefer predictable, reusable patterns over novelty when the product is operational or workflow-heavy.
- Avoid generic AI aesthetics: no default purple/indigo gradients, no glossy filler, no emoji in functional UI.
- When building with Tailwind CSS, follow `references/tailwind-integration.md`.
- Always check `references/accessibility.md` before finalizing any design.
- All animations must respect `prefers-reduced-motion`. See `references/motion-design.md`.

## Decision Flow

1. **Classify the product.**
   - Enterprise/admin/CMS/dashboard: `ant`, `carbon`, or `atlassian`
   - Windows/Microsoft: `fluent`
   - Apple platform: `apple-hig`
   - Android/adaptive: `material`
   - Commerce: `polaris`
   - Content/editorial/portfolio: `minimal`, `swiss`, `swiss-archival`
   - Expressive/experimental: `neo-brutalism`, `glass`, `claymorphism`, `neo-m3`

2. **Check complexity.**
   - Form-heavy, multi-role, operational → `ant`, `carbon`, `atlassian`
   - Data density > brand → `ant` or `carbon`
   - Brand expression central → expressive systems

3. **Decide single vs hybrid.**
   - Single: one system handles behavior + visual tone
   - Hybrid: define explicit ownership (structure vs brand)
   - No arbitrary mashups

4. **Use the map** — `references/../QUICK_REFERENCE.md`

## Workflow

1. Identify product type, platform, UX density
2. Score candidates via `QUICK_REFERENCE.md`
3. Choose system or hybrid
4. Open matching `references/<system>.md`
5. Open matching `assets/archetypes/<page-type>.md` if page type known
6. Apply tokens from `references/design-tokens.md`
7. Follow component patterns from `references/component-patterns.md`
8. Apply responsive layout from `references/responsive-layout.md`
9. Validate accessibility from `references/accessibility.md`
10. Add motion from `references/motion-design.md`

## Reference Files

### Core References
- `QUICK_REFERENCE.md` — System scoring map and fast routing
- `references/icon-guide.md` — 6 approved icon sources with CDN, packages, usage
- `references/component-patterns.md` — Forms, tables, nav, modals, buttons, cards
- `references/design-tokens.md` — Color, spacing, typography, radius, shadows, z-index
- `references/responsive-layout.md` — Grid, breakpoints, mobile patterns, safe areas
- `references/accessibility.md` — WCAG AA, focus, ARIA, keyboard nav, semantic HTML
- `references/motion-design.md` — Durations, easing, animations, reduced motion
- `references/tailwind-integration.md` — Tailwind config, component classes, dark mode

### System References
- `references/ant-design.md`
- `references/carbon-design.md`
- `references/fluent-design.md`
- `references/atlassian-design.md`
- `references/apple-hig.md`
- `references/material-you.md`
- `references/shopify-polaris.md`
- `references/minimalism.md`
- `references/swiss-design.md`
- `references/swiss-archival.md`
- `references/neo-brutalism.md`
- `references/glassmorphism.md`
- `references/claymorphism.md`
- `references/skeuomorphism.md`
- `references/neo-m3-hybrid.md`
- `references/m3-pastel-glass.md`

### Page Archetypes
- `assets/archetypes/dashboard.md`
- `assets/archetypes/settings.md`
- `assets/archetypes/table-detail.md`
- `assets/archetypes/marketing-hero.md`
- `assets/archetypes/editorial-landing.md`

### Palettes
- `assets/palettes/swiss-archival/` — Swiss-Archival palette source (PNG, SVG, ASE, SCSS, TXT, Tailscale JSON)
- `assets/palettes/m3-pastel/` — M3 Pastel candidate swatches (1–4)
- `assets/palettes.json` — All palettes index
