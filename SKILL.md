---
name: ui-designer
description: Choose the best UI design system, or a deliberate combination of systems, for web or app interfaces. Use for dashboards, admin panels, internal tools, CMS, SaaS, websites, component theming, color systems, and frontend visual direction across Ant Design, Fluent, Carbon, Atlassian, Apple HIG, Material You, Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Swiss, Swiss-Archival, and related systems.
---

# UI Designer Skill

Use this skill when the user needs interface direction, design-system selection, theming, or visual/product UX structure before or during implementation.

## Operating Rules

- **CRITICAL: Icon Sources** — NEVER use icons from any source outside the 6 approved icon libraries listed below. Any icon not from Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, or Heroicons must be rejected.
- Choose systems from product context first, not visual mood first.
- Choose the best system for the job. Use a combination only when there is a clear reason and the roles of each system are explicit.
- Prefer predictable, reusable patterns over novelty when the product is operational or workflow-heavy.
- Avoid generic AI aesthetics: no default purple/indigo gradients, no glossy filler, no emoji in functional UI.
- For **Swiss-Archival** specimen decorators, follow the **geometry ruleset** in `assets/decorators/swiss-archival-specimen-decorator.md` (seed, superformula paths, layers, orbits, captions); implement however you like, but preserve that logic for the decorator SVG.
- For **Swiss-Archival** color tokens, source hex values from `assets/palettes/swiss-archival/` (Coolors palette + Tailscale 50–950 ramps). Do not invent ad-hoc lighten/darken — pick a Tailscale stop. The `assets/palettes/swiss-archival/README.md` is the loader index (SCSS / CSS vars / ASE / Tailscale JSON).
- For **M3 Pastel** candidate swatches, source hex values from `assets/palettes/m3-pastel/<n>/` (Coolors palette 1–4). Pick one candidate that matches the project's mood (studio mix, warm blush, soft studio, soft cream) and wire its tokens into the M3 Pastel Glass system. The `assets/palettes/m3-pastel/README.md` is the loader index.
- For **palette sourcing** (a fresh swatch for a new project, refreshing the colors of a chosen system, or exploring alternatives before locking in), invoke the **`color-palette-hunter`** skill (Color Hunt scraper; `--trending|--popular|--theme|--query`, output `json|css|tailwind|html`). Optional: skip the step cleanly if the skill is not installed. Use it to propose 2–3 candidate palettes, then drop the winner into `assets/palettes.json` and into the chosen system's `references/` doc.

## Decision Flow

1. Classify the product.
- Enterprise/admin/internal/CMS/dashboard/data-heavy: prefer `ant`, `carbon`, or `atlassian`.
- Windows/Microsoft-like enterprise: prefer `fluent`.
- Apple platform-native feel: prefer `apple-hig`.
- Android or modern adaptive UI: prefer `material`.
- Commerce and merchant tooling: prefer `polaris`.
- Content, editorial, portfolio, typography-led: prefer `minimal`, `swiss`, or `swiss-archival`.
- Digital archives, museum sites, academic platforms, research tools: prefer `swiss-archival`.
- Expressive or experimental branding: prefer `neo-brutalism`, `glass`, `claymorphism`, `skeuomorphism`, or `neo-m3`.

2. Check complexity.
- If the product is form-heavy, multi-role, repeat-use, or operational, score `ant`, `carbon`, and `atlassian` first.
- If clarity and data density matter more than brand distinctiveness, score `ant` or `carbon` higher.
- If strong brand expression is central, score expressive systems higher and avoid flattening the product into enterprise-safe UI.

3. Decide single system vs hybrid.
- Choose a single system when one design language can handle both behavior and visual tone cleanly.
- Choose a hybrid only when the product clearly needs one system for structure and another for brand expression.
- For hybrids, define the split explicitly.
  - Example: `ant` for layout, forms, tables, and feedback.
  - Example: `neo-m3` or `glass` for hero, marketing surface, or brand accents.
- Do not create arbitrary mashups. Mixed systems must still feel coherent.

4. Use the map.
- Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md) as the main map for fast system selection.
- Then open only the relevant file in `references/`.
 - If the page type is obvious, open the matching file in `assets/archetypes/`.

## Selection Standard

Choose the system that best fits:
- product type
- task density
- platform expectation
- brand intensity
- implementation consistency
- long-term scalability

If a hybrid is better than a single system, state why and define which system owns:
- layout and spacing
- components and interaction behavior
- visual language and brand accents

## Ant Design Evaluation

When Ant is a candidate, evaluate it as a behavior system, not just a look.

Check:
- `Natural`: is the flow obvious and low-friction?
- `Certain`: are hierarchy, spacing, states, and behavior consistent?
- `Meaningful`: does each control support the task flow?
- `Growing`: will the structure hold as features, data, and roles expand?

If Ant wins, use it for:
- workflow scaffolding
- forms and tables
- status and feedback patterns
- dense but readable operational UI

## Workflow

1. Identify the product type, platform, and UX density.
2. Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md) as the map.
3. Choose the best single system or deliberate hybrid.
4. Open only the matching reference file or files.
5. If the page type is known, open the matching archetype file in `assets/archetypes/`.
6. Define color direction, typography direction, spacing behavior, and component style.
7. Translate the chosen system into page structure and component rules.
8. If needed, run the automation script to append design rules.

## Automation

Use `scripts/apply_ui_rules.py` when the project needs persistent `.cursorrules` guidance.

```bash
python3 scripts/apply_ui_rules.py --style [fluent|ant|carbon|atlassian|apple-hig|polaris|material|minimal|glass|neumorphism|neo-brutalism|claymorphism|skeuomorphism|swiss|swiss-archival|m3-pastel|neo-m3] --palette [pastel|dark|vibrant|mono]
```

## Icon Sources Reference

### 1. Phosphor Icons (phosphoricons.com)

**Best for**: Flexible icon family with multiple weights, duotone support

**CDN Usage**:
```html
<!-- Single weight -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/bold/style.css" />
<i class="ph-bold ph-house"></i>

<!-- All weights -->
<script src="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2"></script>
<i class="ph-light ph-house"></i>
<i class="ph-bold ph-house"></i>
<i class="ph-fill ph-house"></i>
<i class="ph-duotone ph-house"></i>
```

**Weights**: `thin`, `light`, `regular` (use `.ph`), `bold`, `fill`, `duotone`

**Framework Packages**:
- React: `@phosphor-icons/react`
- Vue: `@phosphor-icons/vue`
- Svelte: Community packages available

**Styling**: Icons are font-based, style with `color`, `font-size`, `background` etc.

---

### 2. Font Awesome 6 (fontawesome.com)

**Best for**: General-purpose icons, brand logos, comprehensive coverage

**CDN Usage** (Free tier):
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<!-- Solid -->
<i class="fa-solid fa-house"></i>
<!-- Regular -->
<i class="fa-regular fa-house"></i>
<!-- Brands -->
<i class="fa-brands fa-github"></i>
```

**Styles**: `fa-solid` (free), `fa-regular` (free), `fa-brands` (free), `fa-light`, `fa-thin`, `fa-duotone` (pro)

**Framework Packages**:
- React: `@fortawesome/react-fontawesome`
- Vue: `@fortawesome/vue-fontawesome`
- Angular: `@fortawesome/angular-fontawesome`

**Kit Method**: Create a kit at fontawesome.com for custom builds.

---

### 3. Google Material Symbols (fonts.google.com/icons)

**Best for**: Adaptive UI, Material Design projects, variable icon font

**CDN Usage**:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
<span class="material-symbols-outlined">home</span>

<!-- Filled variant -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Filled" />
<span class="material-symbols-filled">home</span>
```

**Variable Axes**:
- `opsz`: Optical size (20-48)
- `wght`: Weight (100-700)
- `FILL`: Fill (0-1)
- `GRAD`: Grade (-200 to 150)

**Variants**: `Outlined`, `Rounded`, `Sharp`

**React**: `@mui/icons-material` (Material UI package)

---

### 4. Tabler Icons (tabler.io/icons)

**Best for**: Large collection, consistent 24px grid, 2px stroke

**CDN Usage**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css" />
<i class="ti ti-home"></i>
<i class="ti ti-home-filled"></i>
```

**Styles**: Outline (default), Filled (suffix `-filled`)

**Framework Packages**:
- React: `@tabler/icons-react`
- Vue: `@tabler/icons-vue`
- Svelte: `@tabler/icons-svelte`
- Angular: `angular-tabler-icons`

**Inline SVG**:
```html
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M5 12l-2 0l9 -9l9 9l-2 0" />
  <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
</svg>
```

---

### 5. Lucide (lucide.dev)

**Best for**: Lightweight, consistent, tree-shakable, forks of Feather Icons

**CDN Usage**:
```html
<script src="https://unpkg.com/lucide@latest"></script>
<!-- Or specific version -->
<script src="https://unpkg.com/lucide@0.344.0/dist/umd/lucide.min.js"></script>
```

**Vanilla JS**:
```html
<i data-lucide="home"></i>
<script>lucide.createIcons();</script>
```

**Framework Packages**:
- React: `lucide-react`
- Vue: `lucide-vue`
- Svelte: `lucide-svelte`
- Angular: `lucide-angular`

**Styling**:
```css
.lucide {
  color: currentColor;
  width: 24px;
  height: 24px;
}
```

**Features**: Tree-shakable, customizable stroke width, consistent 24px grid.

---

### 6. Heroicons (heroicons.com)

**Best for**: Tailwind CSS projects, clean minimal design, by Tailwind team

**CDN/Inline Usage**:
```html
<!-- Inline SVG - Outline (24x24, 1.5px stroke) -->
<svg class="size-6 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
</svg>
```

**Framework Packages**:
- React: `@heroicons/react`
- Vue: `@heroicons/vue`

**Import Paths**:
```javascript
// React
import { HomeIcon } from '@heroicons/react/24/outline'
import { HomeIcon } from '@heroicons/react/24/solid'
import { HomeIcon } from '@heroicons/react/20/solid'
import { HomeIcon } from '@heroicons/react/16/solid'
```

**Variants**: Outline (24x24), Solid (24x24), Mini (20x20), Micro (16x16)

---

### Icon Selection Guide

| Use Case | Recommended Source | Why |
|----------|-------------------|-----|
| General UI | Phosphor, Lucide, Tabler | Large coverage, consistent |
| Brand logos | Font Awesome | Best brand icon collection |
| Material Design | Google Material Symbols | Native Material integration |
| Tailwind projects | Heroicons | Made by Tailwind team |
| Dashboard/admin | Tabler, Phosphor | Comprehensive, professional |
| Mobile/flutter | Phosphor, Material | Good framework support |
| Duotone/two-tone | Phosphor, Font Awesome Pro | Unique visual style |
| Lightweight/critical | Lucide | Smallest bundle, tree-shakable |

### Icon Naming Conventions

When referencing icons in designs, use this format:
```
[library]/[icon-name]
```

Examples:
- `phosphor/house` or `phosphor/house-bold`
- `fontawesome/house` or `fa-solid/house`
- `material/home` or `material-symbols-outlined/home`
- `tabler/home` or `tabler/home-filled`
- `lucide/home`
- `heroicons/home` or `heroicons/home-solid`

---

## References

- Main map: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- System details: `references/ant-design.md`, `references/carbon-design.md`, `references/fluent-design.md`, `references/atlassian-design.md`, `references/apple-hig.md`, `references/material-you.md`, `references/shopify-polaris.md`, `references/minimalism.md`, `references/swiss-design.md`, `references/swiss-archival.md`, `references/neo-brutalism.md`, `references/glassmorphism.md`, `references/claymorphism.md`, `references/skeuomorphism.md`, `references/neo-m3-hybrid.md`, `references/m3-pastel-glass.md`
- Page archetypes: `assets/archetypes/dashboard.md`, `assets/archetypes/settings.md`, `assets/archetypes/table-detail.md`, `assets/archetypes/marketing-hero.md`, `assets/archetypes/editorial-landing.md`
- Swiss-Archival palette source files: `assets/palettes/swiss-archival/` — see `assets/palettes/swiss-archival/README.md` for the loader index (PNG, SVG, ASE, SCSS, TXT, Tailscale JSON).
- M3 Pastel palette source files: `assets/palettes/m3-pastel/` (4 candidate swatches in `1/`, `2/`, `3/`, `4/`) — see `assets/palettes/m3-pastel/README.md` for the loader index.
- Swiss-Archival decorators: `assets/decorators/swiss-archival-specimen-decorator.md`
