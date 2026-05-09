# Swiss-Archival Components

Component specifications for the Swiss-Archival design system. All components use CSS custom properties from the system token set.

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
  background: #A02020;
  border-color: #A02020;
}
.btn-primary:active {
  background: #6B1212;
  border-color: #6B1212;
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
  box-shadow: 0 0 0 2px rgba(139, 26, 26, 0.3);
}
.input::placeholder {
  color: #7A7068;
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
  color: #7A7068;
  border-radius: 4px;
}
.tag--accent {
  background: rgba(139, 26, 26, 0.1);
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
.toast--error   { border-left: 3px solid #8B1A1A; }
.toast--warning { border-left: 3px solid #8B6B1A; }
```

---

## Skeleton Loader

```css
.skeleton {
  background: linear-gradient(
    90deg,
    #DDD5C5 25%,
    #EFE9DC 50%,
    #DDD5C5 75%
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
  background: rgba(232, 224, 208, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid #DDD5C5;
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

```css
:root {
  /* Color */
  --color-bg: #E8E0D0;
  --color-fg: #2A2520;
  --color-surface: #EFE9DC;
  --color-accent: #8B1A1A;
  --color-muted: #DDD5C5;
  --color-muted-fg: #7A7068;
  --color-accent-hover: #A02020;
  --color-accent-active: #6B1212;
  --color-success: #3A6B3A;
  --color-warning: #8B6B1A;

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

---

## Parametric specimen decorator

For generative SVG vitrines, the **specimen** shape is defined by the geometry ruleset (superformula layers, interference paths, orbits, deterministic SID) in:

`assets/decorators/swiss-archival-specimen-decorator.md`

Use that asset when Swiss-Archival needs a decorative specimen layer; keep forms, tables, and reading layout on the components above.
