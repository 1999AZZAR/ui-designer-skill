# Icon Sources Guide

ALL icons in any UI design MUST come exclusively from these 6 approved sources. Never use icons from unapproved sources.

## Approved Sources

### 1. Phosphor Icons — phosphoricons.com

- **Count**: 9,000+ icons
- **Weights**: thin, light, regular, bold, fill, duotone
- **License**: MIT
- **Best for**: Flexible family with duotone support, multiple weights

**CDN**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/bold/style.css" />
<i class="ph-bold ph-house"></i>

<!-- All weights -->
<script src="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2"></script>
<i class="ph-light ph-house"></i>
<i class="ph ph-house"></i>        <!-- regular -->
<i class="ph-bold ph-house"></i>
<i class="ph-fill ph-house"></i>
<i class="ph-duotone ph-house"></i>
```

**Packages**: `@phosphor-icons/react`, `@phosphor-icons/vue`, community Svelte packages

---

### 2. Font Awesome 6 — fontawesome.com

- **Count**: 2,000+ free (6,000+ with Pro)
- **Styles**: solid, regular, brands (free); light, thin, duotone (pro)
- **License**: Free tier available, Pro required for advanced styles
- **Best for**: Brand logos, comprehensive general coverage

**CDN (Free)**:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<i class="fa-solid fa-house"></i>
<i class="fa-regular fa-house"></i>
<i class="fa-brands fa-github"></i>
```

**Packages**: `@fortawesome/react-fontawesome`, `@fortawesome/vue-fontawesome`, `@fortawesome/angular-fontawesome`

---

### 3. Google Material Symbols — fonts.google.com/icons

- **Count**: 3,000+ icons
- **Variants**: Outlined, Rounded, Sharp
- **Variable axes**: optical size, weight, fill, grade
- **License**: Apache 2.0
- **Best for**: Material Design projects, adaptive UI

**CDN**:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
<span class="material-symbols-outlined">home</span>

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Filled" />
<span class="material-symbols-filled">home</span>
```

**Variable Axes**:
- `opsz`: Optical size (20–48)
- `wght`: Weight (100–700)
- `FILL`: Fill (0–1)
- `GRAD`: Grade (-200 to 150)

**Package**: `@mui/icons-material`

---

### 4. Tabler Icons — tabler.io/icons

- **Count**: 6,100+ icons
- **Styles**: Outline, Filled
- **Grid**: 24x24, 2px stroke
- **License**: MIT
- **Best for**: Large consistent collection, dashboards

**CDN**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css" />
<i class="ti ti-home"></i>
<i class="ti ti-home-filled"></i>
```

**Inline SVG**:
```html
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M5 12l-2 0l9 -9l9 9l-2 0" />
  <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
</svg>
```

**Packages**: `@tabler/icons-react`, `@tabler/icons-vue`, `@tabler/icons-svelte`, `angular-tabler-icons`

---

### 5. Lucide — lucide.dev

- **Count**: 1,700+ icons
- **Grid**: 24x24, customizable stroke
- **License**: ISC
- **Best for**: Lightweight, tree-shakable, Feather Icons fork

**CDN**:
```html
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="home"></i>
<script>lucide.createIcons();</script>
```

**Packages**: `lucide-react`, `lucide-vue`, `lucide-svelte`, `lucide-angular`

**Features**: Tree-shakable, smallest bundle size, consistent design language.

---

### 6. Heroicons — heroicons.com

- **Count**: 316 icons
- **Variants**: Outline (24x24), Solid (24x24), Mini (20x20), Micro (16x16)
- **License**: MIT
- **Best for**: Tailwind CSS projects, clean minimal design

**Inline SVG**:
```html
<svg class="size-6 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
</svg>
```

**Packages**: `@heroicons/react`, `@heroicons/vue`

---

## Selection Guide

| Use Case | Recommended Source |
|----------|-------------------|
| General UI | Phosphor, Lucide, Tabler |
| Brand logos | Font Awesome |
| Material Design | Google Material Symbols |
| Tailwind projects | Heroicons |
| Dashboard/admin | Tabler, Phosphor |
| Mobile/Flutter | Phosphor, Material |
| Duotone/two-tone | Phosphor |
| Lightweight/critical | Lucide |

## Naming Convention

Reference icons using this format in specs and designs:

```
[library]/[icon-name]
```

Examples:
- `phosphor/house`, `phosphor/house-bold`
- `fontawesome/house`, `fontawesome/solid/house`
- `material/home`, `material-outlined/home`
- `tabler/home`, `tabler/home-filled`
- `lucide/home`
- `heroicons/home`, `heroicons/home-solid`
