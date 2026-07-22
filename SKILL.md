---
name: ui-designer
description: "Choose the best UI design system, or a deliberate combination of systems, for web or app interfaces. Use for dashboards, admin panels, internal tools, CMS, SaaS, websites, component theming, color systems, and frontend visual direction across Ant Design, Fluent, Carbon, Atlassian, Apple HIG, Material You, Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Swiss, Swiss-Archival, and related systems. Also supports brand-cloning via getdesign.md DESIGN.md files (328+ real-world brands: Stripe, Vercel, Linear, Notion, Tesla, Spotify, etc.). Features anti-slop quality gates, pre-flight project scanning, genre-aware theme catalog, and 8-state component verification."
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

# UI Designer Skill (v2)

Use this skill when the user needs interface direction, design-system selection, theming, or visual/product UX structure before or during implementation.

## MCP Tools (`mcp__the-designer__*`)

### Core Design Flow
| Tool | When to Call |
|------|--------------|
| **`evaluate_style`** | **FIRST STEP** — Score styles against product context, returns ranked recommendations + workflow |
| **`detect_genre`** | Detect design genre (editorial / modern-minimal / atmospheric / playful) from brief |
| **`pre_flight_scan`** | Scan existing project for framework, fonts, palette, motion libs before designing |
| `list_options` | List all available systems, palettes, archetypes, hybrids |
| `validate_combo` | Check that a style+palette+hybrid is valid before generating |
| `generate_rules` | Generate design rules for a style+palette+archetype combo |
| `generate_tailwind_config` | Generate ready-to-use tailwind.config.js |
| `generate_template` | Generate full HTML starter page |
| `get_component` | Get production-ready component snippet (button, card, nav, hero, etc.) |
| `get_cross_cutting_rules` | Get standalone rules (accessibility, motion, icons, tokens, responsive) |
| `generate_palette_variants` | Generate light/dark/high-contrast variants from hex colors |
| `export_project` | Export full project scaffold |

### Ellis UI Templates (Bespoke Systems)
| Tool | When to Call |
|------|--------------|
| **`list_ellis_ui_designs`** | List all 24 bespoke Ellis UI design templates (e.g., Swiss Archival, Vintage Airmail, Brutalist). |
| **`get_ellis_ui_template`** | Fetch the HTML structure and CSS rules for a specific Ellis UI design system. Use this as a structural foundation for highly thematic, anti-slop designs. |

### Theme & Token System
| Tool | When to Call |
|------|--------------|
| **`generate_tokens`** | Generate complete OKLCH token system (tokens.css) with named theme or genre |
| **`list_themes`** | List all 16 curated themes with OKLCH values, fonts, axis metadata |
| `get_reference` | Pull full content of any reference doc |
| `brand_fetch_design_md` | Download DESIGN.md for a real brand |
| `brand_list` | List all 328+ brands by category |

### Color & Palette
| Tool | When to Call |
|------|--------------|
| `palette_fetch` | Fetch live palettes from Color Hunt |
| `palette_convert` | Convert palette JSON to CSS / Tailwind / SCSS / Figma / Android / Swift |

### Quality Gates (NEW in v2)
| Tool | When to Call |
|------|--------------|
| **`anti_pattern_check`** | Run 35-gate slop test on output — detects italic headers, fake chrome, fabricated metrics, etc. |
| **`self_critique`** | Score output on 6 quality axes (P-H-E-S-R-V) before shipping — anything < 3 triggers revision |
| **`generate_8state_component`** | Generate demo page with all 8 interactive states (hover, focus, active, disabled, loading, error, success) |

### Utility
| Tool | When to Call |
|------|--------------|
| `list_installed_skills` | Detect installed skill submodules |
| **`generate_motion_snippet`** | Generate a ready-to-paste **anime.js v4** snippet (CDN + code + usage hint) for any animation category (`entrance`, `micro`, `stagger`, `scroll`, `loader`, `transition`, `counter`, `typewriter`) matched to the current design style's easing/duration character. All snippets include `prefers-reduced-motion` guards. Call after `generate_template` or `get_component` whenever motion is needed. |

## MANDATORY Workflow (v2)

```
PHASE 0: DISCOVERY
  1. detect_genre({ brief })                                ← classify genre from brief
  2. pre_flight_scan({ project_path })                      ← if existing project, scan context
  3. evaluate_style({ description })                        ← score style match

PHASE 1: WIREFRAME
  4. list_themes({ genre })                                 ← pick from genre-scoped themes
  5. generate_tokens({ genre, theme_name })                 ← generate OKLCH token system
  6. validate_combo({ style, palette })                     ← confirm valid combo
  7. generate_rules({ style, palette, archetype })          ← get design rules

PHASE 2: PROTOTYPE
  8. generate_template({ style, palette, archetype })       ← starter HTML
  9. get_component({ component, style })                    ← individual components
  10. generate_8state_component({ kind })                   ← if interactive component needed

PHASE 3: QUALITY
  11. anti_pattern_check({ content, genre })                ← run slop test on output
  12. self_critique({ content })                           ← score 6 quality axes
  13. fix any gate failures (anti-pattern < 3, self-critique < 3)
  14. export_project({ style, palette, archetype })         ← full scaffold when ready
```

**NEVER skip Phase 0.** The evaluation engine scores all 17 styles. Pre-flight scan prevents stomping on existing tokens. Genre detection scopes which themes and slop gates apply.

**NEVER skip Phase 3.**
- `anti_pattern_check` catches AI-slop tells: italic headers, fake browser chrome, fabricated testimonials/metrics, emoji in UI, 3-col-grid default, specimen fall-through, missing focus-visible, no prefers-reduced-motion.
- `self_critique` scores Philosophy, Hierarchy, Execution, Specificity, Restraint, Variety. Any < 3 = revision pass before shipping.

## Anti-Slop Design Philosophy

These rules hold across every workflow:

1. **Structural variety.** Two pages for different briefs must not share the same hero → 3-feature → CTA → footer rhythm. Use different macrostructures, not different color swaps of the same template.

2. **Locked tokens.** Every color and font-family must reference a named CSS custom property (`var(--color-accent)`). No inline OKLCH/hex values bypassing the token block.

3. **No fabricated content.** If the user did not supply a metric, do not invent one. Stat-led layouts and proof bars must use real numbers or labeled placeholders. Same rule for testimonials, logos, and case-study counts.

4. **No re-drawn chrome.** No fake browser bars, phone frames, code-block title bars. Use real screenshots in a `<figure>` or omit chrome entirely.

5. **Typography purity.** Headings are always roman (`font-style: normal`). Italic survives only as body-copy emphasis inside running paragraphs.

6. **Mobile-responsiveness hard floor.** Every output must render at 320/375/414/768px. No horizontal scroll. No two-line clickable text. Section heads collapse to single column on mobile.

7. **Component 8-state discipline.** Every interactive component must style all 8 states: default, hover, focus-visible, active, disabled, loading, error, success.

8. **No default purple gradient.** Avoid the LLM-trained default of purple-blue gradients without brief justification.

## Operating Rules

- **MANDATORY: Core Design Principles**
  - **UI**: Structural, clear, and tidy; Clear and understandable; Consistent and coherent; Purposeful and relevant; Adaptable and responsive.
  - **UX**: Intuitive and user-friendly; Easy to learn and use; Consistent around the UI; Accessible and inclusive; Efficient and effective.
- **MANDATORY: Design Flow** — Wireframe → Prototype → Test (Phase 0-3 above)
- **MANDATORY: Good Design Criteria** — Emphasis; Alignment/Balance; Contrast; Consistency/Repetition; White Space; Hierarchy; Unity/Cohesion.
- **FORBIDDEN: Beginner Mistakes** — Skipping flow; Excessive complexity/detail/color; No hierarchy/purpose; Poor usability/spacing; Aesthetic > Usability.
- **CRITICAL: Icon Sources** — NEVER use icons from unapproved sources. Only 6 allowed: Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, Heroicons. See `references/icon-guide.md`.
- Choose systems from product context first, not visual mood first.
- Use a combination only when there is a clear reason and the roles are explicit.
- Prefer predictable, reusable patterns over novelty for operational/workflow-heavy products.
- Avoid generic AI aesthetics: no default purple/indigo gradients, no glossy filler, no emoji in functional UI.
- When cloning/matching a real brand, use `brand_fetch_design_md` (MCP) or `npx getdesign@latest add <brand>` (CLI).
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

2. **Detect genre.**
   - `editorial` — default, canonical anti-slop voice
   - `modern-minimal` — Stripe/Linear school (SaaS, enterprise, B2B)
   - `atmospheric` — dark AI-tool school (generative, music, video, late-night)
   - `playful` — post-Linear soft school (consumer, casual, community)

3. **Run pre-flight scan** on existing project to detect framework, font stack, palette, motion stance.

4. **Choose theme from catalog** via `list_themes({ genre })` → `generate_tokens({ theme_name })` for OKLCH tokens.

5. **Check complexity.** Form-heavy, multi-role, operational → `ant`, `carbon`, `atlassian`. Data density > brand → `ant` or `carbon`. Brand expression central → expressive systems.

6. **Decide single vs hybrid.** Single: one system handles behavior + visual tone. Hybrid: define explicit ownership. No arbitrary mashups.

7. **Build with quality gates.** Generate → anti-pattern check → self-critique → fix → ship.

## Workflow

### Standard (system-first)
1. Identify product type, platform, UX density
2. Run `detect_genre` + `pre_flight_scan` + `evaluate_style`
3. Choose theme via `list_themes` + `generate_tokens`
4. Score candidates via `QUICK_REFERENCE.md`
5. Choose system or hybrid
6. Call `generate_rules` for design rules
7. Call `generate_template` for starter HTML
8. Call `get_component` for individual components
9. Call `anti_pattern_check` on output + fix failures
10. Call `self_critique` — revision if any < 3
11. Validate accessibility from `references/accessibility.md`

### Brand Reference (DESIGN.md-first)
When user wants to match a real brand's look:
1. Call `brand_fetch_design_md({ brand })` (MCP) OR run `npx getdesign@latest add <brand>` (CLI)
2. Parse DESIGN.md front matter — extract colors, typography, rounded, spacing, components
3. Map brand aesthetic to closest structural system (see table in `references/getdesign-md.md`)
4. Generate tokens via `generate_tokens` — override with brand values
5. Call `generate_rules` + `generate_template` + components
6. Run quality gates (`anti_pattern_check` + `self_critique`)
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
- `references/getdesign-md.md` — DESIGN.md brand reference system (328+ brands)

### Genre References
- `references/genre-editorial.md` — Editorial genre (default, content-driven)
- `references/genre-modern-minimal.md` — Modern-minimal genre (SaaS, enterprise, B2B)
- `references/genre-atmospheric.md` — Atmospheric genre (dark, AI-tool, immersive)
- `references/genre-playful.md` — Playful genre (consumer, casual, community)

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
- `assets/palettes/swiss-archival/` — Swiss-Archival palette source
- `assets/palettes/m3-pastel/` — M3 Pastel candidate swatches
- `assets/palettes.json` — All palettes index
