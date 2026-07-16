# Motion Design

Animation and transition patterns for UI micro-interactions.

## Principles

1. **Purposeful** — Every animation serves a function (feedback, guidance, continuity). Cut motion before adding it. If removing an animation wouldn't lose the user information, remove it.
2. **Quick** — Most transitions: 150-250ms.
3. **Layout-safe** — Animate `transform` and `opacity` only. Never animate layout properties (margin, width, height, padding, top, left).
4. **Respectful** — Honor `prefers-reduced-motion: reduce`. Spatial motion collapses to ≤150ms opacity crossfade.

## Named Easings (only these three)

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in: cubic-bezier(0.4, 0, 0.68, 0.06);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
}
```

| Curve | When |
|-------|------|
| `--ease-out` | Elements entering view, modals appearing (decelerate) |
| `--ease-in` | Elements exiting view, modals closing (accelerate) |
| `--ease-in-out` | State changes, shared transitions |

**Forbidden**: browser default `ease`, bounce/overshoot on UI state transitions. No `--ease-spring` or `--ease-sharp` for functional UI.

## Duration Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--dur-fast` | 150ms | Hover states, micro-interactions |
| `--dur-base` | 250ms | Standard transitions |
| `--dur-slow` | 400ms | Complex animations |

**No animation longer than 500ms without a progress indicator.**

## Common Animations

### Hover Effects
```css
.card {
  transition: transform var(--dur-fast) var(--ease-out),
              box-shadow var(--dur-fast) var(--ease-out);
}
.card:hover {
  transform: translateY(-2px);
}

.btn:active {
  transform: scale(0.97);
}
```

### Focus Indicators
```css
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
/* Never animate the ring's appearance — must show instantly on focus */
```

### Dropdown/Popover
```css
.dropdown-menu {
  opacity: 0;
  transform: translateY(-4px);
  transition: opacity var(--dur-fast) var(--ease-out),
              transform var(--dur-fast) var(--ease-out);
}
.dropdown-menu.open {
  opacity: 1;
  transform: translateY(0);
}
```

### Modal
```css
.modal-backdrop {
  opacity: 0;
  transition: opacity var(--dur-fast) var(--ease-in);
}
.modal-backdrop.open { opacity: 1; }

.modal-content {
  opacity: 0;
  transform: translateY(8px) scale(0.98);
  transition: opacity var(--dur-base) var(--ease-out),
              transform var(--dur-base) var(--ease-out);
}
.modal-content.open {
  opacity: 1;
  transform: translateY(0) scale(1);
}
```

### Skeleton Loading
```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.skeleton {
  background: linear-gradient(90deg, var(--color-paper-2) 25%,
              var(--color-paper-3) 50%, var(--color-paper-2) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
```

### Spinner
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}
.spinner {
  width: 24px; height: 24px;
  border: 3px solid var(--color-border);
  border-top-color: var(--color-accent);
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
```

### Fade In
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in {
  animation: fadeIn var(--dur-base) var(--ease-out);
}
```

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  /* Spatial motion collapses to opacity crossfade ≤150ms */
  .card:hover { transform: none; }
  .modal-content { transform: none; }
  .dropdown-menu { transform: none; }
}
```

JavaScript check:
```javascript
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

## Anti-Patterns

- **Animate layout properties** (margin, width, height, padding, top, left) — use transform instead
- **Bounce/overshoot on UI state** — no `cubic-bezier` with > 1.0 control point
- **Infinite loops** — auto-playing animations exhaust users
- **Flashing content** — max 3 flashes per second (seizure risk)
- **Animation > 500ms** without progress indicator
- **Blocking interaction** during animation
- **Decorative-only motion** with no informational purpose
- **No reduced-motion support** — mandatory
- **Default browser `ease`** — always use named custom properties
- **No animation on focus ring** — must appear instantly

## Microinteraction Patterns

| Pattern | Duration | Easing | Notes |
|---------|----------|--------|-------|
| Button hover | 150ms | ease-out | translateY or color |
| Button active | 100ms | ease-out | scale(0.97) |
| Card hover lift | 150ms | ease-out | translateY(-2px) |
| Dropdown open | 150ms | ease-out | opacity + translateY |
| Dropdown close | 100ms | ease-in | opacity only |
| Modal enter | 250ms | ease-out | opacity + translateY |
| Modal exit | 150ms | ease-in | opacity only |
| Toast in | 250ms | ease-out | translateX + opacity |
| Toast out | 200ms | ease-in | opacity only |
| Toggle switch | 200ms | ease-out | translateX thumb |
| Skeleton shimmer | 1.5s | linear | Infinite loop OK |
