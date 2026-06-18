---
name: ui-designer
description: "Choose the best UI design system, or a deliberate combination of systems, for web or app interfaces. Use for dashboards, admin panels, internal tools, CMS, SaaS, websites, component theming, color systems, and frontend visual direction across Ant Design, Fluent, Carbon, Atlassian, Apple HIG, Material You, Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Swiss, Swiss-Archival, and related systems. Also supports brand-cloning via getdesign.md DESIGN.md files (328+ real-world brands: Stripe, Vercel, Linear, Notion, Tesla, Spotify, etc.)."
entry: SKILL.md
resources:
  guide: QUICK_REFERENCE.md
  icons: references/icon-guide.md
  tokens: references/design-tokens.md
  systems: references/
  archetypes: assets/archetypes/
  palettes: assets/palettes.json
  script: scripts/apply_ui_rules.py
---

# UI Designer Skill

Use this skill when the user needs interface direction, design-system selection, theming, or visual/product UX structure before or during implementation.

## MCP Tools (`mcp__the-designer__*`)

When the `the-designer` MCP server is available, prefer calling these tools directly over manual subprocess invocations.

| Tool | When to Call |
|------|--------------|
| **`evaluate_style`** | **FIRST STEP** — Score styles against product context, returns ranked recommendations + workflow |
| `list_options` | List all available systems, palettes, archetypes, hybrids |
| `validate_combo` | Check that a style+palette+hybrid is valid before generating |
| `generate_rules` | Generate design rules for a style+palette+archetype combo → `.cursorrules` or JSON |
| `generate_tailwind_config` | Generate ready-to-use tailwind.config.js for a style+palette |
| `generate_template` | Generate full HTML starter page for style+palette+archetype |
| `get_component` | Get production-ready component snippet (button, card, nav, hero, etc.) |
| `get_cross_cutting_rules` | Get standalone rules (accessibility, motion, icons, tokens, responsive) |
| `generate_palette_variants` | Generate light/dark/high-contrast variants from hex colors |
| `export_project` | Export full project scaffold (config + HTML + components) |
| `get_reference` | Pull full content of any reference doc (ant-design, accessibility, etc.) |
| `palette_fetch` | Fetch live palettes from Color Hunt (trending/popular/theme/query) |
| `palette_convert` | Convert palette JSON to CSS / Tailwind / SCSS / Figma / Android / Swift |
| `brand_fetch_design_md` | Download DESIGN.md for a real brand (stripe, vercel, notion, claude…) |
| `brand_list` | List all 328+ brands by category |
| `list_installed_skills` | Detect installed skill submodules |

**MANDATORY Workflow with MCP:**

```
1. evaluate_style({ description: "..." })  ← ALWAYS START HERE
   → returns: recommended style, palette, archetype, workflow steps

2. validate_combo({ style, palette })      ← confirm valid
3. brand_fetch_design_md({ brand })        ← if brand reference needed
4. generate_rules({ style, palette, archetype })  ← get design rules
5. get_reference({ name })                 ← deep-dive as needed
6. generate_template({ style, palette, archetype })  ← starter HTML
7. get_component({ component, style })     ← individual components
8. export_project({ style, palette, archetype })     ← full scaffold
```

**NEVER skip step 1.** The evaluation engine scores all 17 styles against your product context to find the best match. Do not default to a style without evaluation.

## Operating Rules

- **MANDATORY: Core Design Principles**
  - **UI**: Structural, clear, and tidy; Clear and understandable; Consistent and coherent; Purposeful and relevant; Adaptable and responsive.
  - **UX**: Intuitive and user-friendly; Easy to learn and use; Consistent around the UI; Accessible and inclusive; Efficient and effective.
- **MANDATORY: Design Flow**
  - **1. Wireframe**: Focus on structure and hierarchy.
  - **2. Prototype**: Functional implementation.
  - **3. Test**: Accessibility and responsiveness validation.
- **MANDATORY: Good Design Criteria**
  - Emphasis; Alignment/Balance; Contrast; Consistency/Repetition; White Space; Hierarchy; Unity/Cohesion.
- **FORBIDDEN: Beginner Mistakes**
  - Skipping flow; Excessive complexity/detail/color; No hierarchy/purpose; Poor usability/spacing; Aesthetic > Usability.
- **CRITICAL: Icon Sources** — NEVER use icons from unapproved sources. Only these 6 are allowed: Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, Heroicons. See `references/icon-guide.md`.
- Choose systems from product context first, not visual mood first.
- Choose the best system for the job. Use a combination only when there is a clear reason and the roles of each system are explicit.
- Prefer predictable, reusable patterns over novelty when the product is operational or workflow-heavy.
- Avoid generic AI aesthetics: no default purple/indigo gradients, no glossy filler, no emoji in functional UI.
- When the user asks to clone/match/reference a real brand's look, use `brand_fetch_design_md` (MCP) or `npx getdesign@latest add <brand>` (CLI). See `references/getdesign-md.md`.
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

### Standard (system-first)

1. Identify product type, platform, UX density
2. Score candidates via `QUICK_REFERENCE.md`
3. Choose system or hybrid
4. Open matching `references/<system>.md` (or call `get_reference` via MCP)
5. Open matching `assets/archetypes/<page-type>.md` if page type known
6. Apply tokens from `references/design-tokens.md`
7. Follow component patterns from `references/component-patterns.md`
8. Apply responsive layout from `references/responsive-layout.md`
9. Validate accessibility from `references/accessibility.md`
10. Add motion from `references/motion-design.md`

### Brand Reference (DESIGN.md-first)

When user wants to match a real brand's look:

1. Call `brand_fetch_design_md({ brand })` (MCP) OR run `npx getdesign@latest add <brand>` (CLI)
2. Parse DESIGN.md front matter — extract colors, typography, rounded, spacing, components
3. Map brand aesthetic to closest structural system (see table in `references/getdesign-md.md`)
4. Open that system's reference file for layout/behavior patterns
5. Override all visual tokens with DESIGN.md values
6. Note any Known Gaps from DESIGN.md and surface them to user
7. Validate accessibility from `references/accessibility.md`

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
- `references/getdesign-md.md` — DESIGN.md brand reference system (328+ brands via getdesign.md)

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
