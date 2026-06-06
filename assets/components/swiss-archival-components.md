# Swiss-Archival Components

Component specifications for the Swiss-Archival design system. All components use CSS custom properties from the system token set. The palette tokens are sourced from `assets/palettes/swiss-archival/` — see that folder's `README.md` for the loader index, Tailscale ramps, and ASE/SCSS exports.

---

## Buttons

### Primary
```css
.btn-primary {
  font-family: var(--font-technical);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.5rem 1rem;
  background: var(--color-accent);
  color: var(--color-bg);
  border: 1px solid var(--color-accent);
  border-radius: 6px;
  cursor: pointer;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: var(--color-accent-hover);
  border-color: var(--color-accent-hover);
}
.btn-primary:active {
  background: var(--color-accent-active);
  border-color: var(--color-accent-active);
}
```

### Ghost
```css
.btn-ghost {
  font-family: var(--font-technical);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.5rem 1rem;
  background: transparent;
  color: var(--color-fg);
  border: 1px solid var(--color-muted);
  border-radius: 6px;
  cursor: pointer;
  transition: all 150ms ease;
}
.btn-ghost:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}
```

---

## Inputs & Forms

```css
.input {
  font-family: var(--font-narrative);
  font-size: 0.875rem;
  padding: 0.5rem 0.75rem;
  background: var(--color-surface);
  color: var(--color-fg);
  border: 1px solid var(--color-muted);
  border-radius: 6px;
  outline: none;
  transition: border-color 150ms ease;
}
.input:focus {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 2px rgba(156, 61, 59, 0.3);
}
.input::placeholder {
  color: var(--color-muted-fg);
}
```

**Label convention:** JetBrains Mono, 0.75rem, uppercase, wide tracking, placed above input with 4px gap.

---

## Cards

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-muted);
  border-radius: 6px;
  padding: 1rem;
  transition: border-color 200ms ease, transform 200ms ease;
}
.card:hover {
  border-color: var(--color-accent);
  transform: translateY(-2px);
}
```

**Structure:**
```
+----------------------------------+
| [LABEL] METADATA                 |  JetBrains Mono, muted-fg
| Title Here                       |  Plus Jakarta Sans, H3
| Short description text...        |  Body Small
|                                  |
| [TAG] [TAG]        [ACTION ->]   |  Labels + Ghost button
+----------------------------------+
```

---

## Tags & Badges

```css
.tag {
  font-family: var(--font-technical);
  font-size: 0.625rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 4px 8px;
  background: var(--color-muted);
  color: var(--color-muted-fg-strong);
  border-radius: 4px;
}
.tag--accent {
  background: rgba(156, 61, 59, 0.1);
  color: var(--color-accent);
}
```

---

## Toast Notifications

```css
.toast {
  font-family: var(--font-technical);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.5rem 1rem;
  background: var(--color-fg);
  color: var(--color-bg);
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.12);
}
.toast--success { border-left: 3px solid #3A6B3A; }
.toast--error   { border-left: 3px solid #9C3D3B; }
.toast--warning { border-left: 3px solid #8B6B1A; }
```

---

## Skeleton Loader

```css
.skeleton {
  background: linear-gradient(
    90deg,
    #CBC3B7 25%,
    #EFE9DC 50%,
    #CBC3B7 75%
  );
  background-size: 200% 100%;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
  border-radius: 6px;
}
@keyframes skeleton-pulse {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

## Glassmorphic Modal

```css
.glass-overlay {
  background: rgba(239, 233, 220, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid #CBC3B7;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.12);
}
```

---

## Empty State

```
[ NO_RESULTS ]
     (icon)
"No entries found matching your query."
[ CLEAR_FILTERS ]
```

Technical label (JetBrains Mono, uppercase) + icon + body text + ghost button.

---

## Error State

```
[ ERROR: 404 ]
"Archive entry not found."
[ RETURN_HOME ]
```

Technical label with error code + body text + ghost button.

---

## Contextual Header

A grid-stack component that swaps site identity with contextual reference on scroll (>400px).

- **Index view:** `[ ARCHIVE_TAGLINE: TEXT ]`
- **Single view:** `[ CATEGORIES: NAME ]` with return-home link

---

## Citation Specimen Utility

Glassmorphic modal with formats: APA, MLA, BibTeX, TECHNICAL_REF.
- Card-level border pulse on copy
- Toast notification with `[ SUCCESS ]` label
- Dark-mode technical help overlay

---

## CSS Custom Properties (Full Set)

Source palette: `assets/palettes/swiss-archival/palette.scss`. Hex values below are pulled from the canonical six-color swatch plus the Tailscale ramps in `assets/palettes/swiss-archival/tailscale.txt`.

```css
:root {
  /* Color — core swatch (assets/palettes/swiss-archival/) */
  --color-bg: #EFE9DC;          /* soft-linen 100 */
  --color-surface: #EEE8DB;     /* soft-linen-2 */
  --color-fg: #2A2520;          /* carbon-black */
  --color-muted: #CBC3B7;       /* dust-grey 100 — borders, dividers */
  --color-muted-fg: #A49C92;    /* grey-olive 100 — large/600-weight labels */
  --color-muted-fg-strong: #6F675D; /* grey-olive 600 — small UI labels (AA) */
  --color-accent: #9C3D3B;      /* brown-red 500 */
  --color-accent-hover: #943A38;/* brown-red 600 (Tailscale) */
  --color-accent-active: #6F2B2A; /* brown-red 700 (Tailscale) */
  --color-success: #3A6B3A;     /* not in core palette — state only */
  --color-warning: #8B6B1A;     /* not in core palette — state only */

  /* Tailscale ramp shortcuts (load via tokens, no inline hex elsewhere) */
  --brown-red-50:  #F8EDED;
  --brown-red-100: #F1DADA;
  --brown-red-200: #E3B6B5;
  --brown-red-300: #D59190;
  --brown-red-400: #C76D6B;
  --brown-red-500: #9C3D3B; /* base */
  --brown-red-600: #943A38; /* hover */
  --brown-red-700: #6F2B2A; /* active */
  --brown-red-800: #4A1D1C;
  --brown-red-900: #250E0E;
  --brown-red-950: #1A0A0A;

  /* Typography */
  --font-narrative: 'Plus Jakarta Sans', sans-serif;
  --font-technical: 'JetBrains Mono', monospace;

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Elevation */
  --elevation-1: 0 1px 3px rgba(42, 37, 32, 0.08);
  --elevation-2: 0 4px 12px rgba(42, 37, 32, 0.12);
  --elevation-3: 0 8px 24px rgba(42, 37, 32, 0.16);

  /* Motion */
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --duration-fast: 150ms;
  --duration-normal: 225ms;
  --duration-slow: 375ms;
  --duration-glacial: 600ms;

  /* Z-Index */
  --z-base: 0;
  --z-card: 10;
  --z-header: 100;
  --z-overlay: 200;
  --z-toast: 300;
  --z-command: 400;
}
```

**Tailscale loader.** For the full 50–950 ramp per color, import the JSON in `assets/palettes/swiss-archival/tailscale.txt` and expose it as a flat `--linen-500`, `--olive-600` style token set, or generate the SCSS partials from the file. Do not hand-roll lighten/darken — they break the warm-archival character.

---

## Parametric specimen decorator

For generative SVG vitrines, the **specimen** shape is defined by the geometry ruleset (superformula layers, interference paths, orbits, deterministic SID) in:

`assets/decorators/swiss-archival-specimen-decorator.md`

Use that asset when Swiss-Archival needs a decorative specimen layer; keep forms, tables, and reading layout on the components above.
