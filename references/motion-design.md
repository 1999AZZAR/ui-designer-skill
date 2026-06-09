# Motion Design

Animation and transition patterns for UI micro-interactions and page transitions.

## Principles

1. **Purposeful** — Every animation serves a function (feedback, guidance, continuity)
2. **Quick** — Most transitions should be 200–300ms
3. **Smooth** — Use appropriate easing curves
4. **Respectful** — Honor `prefers-reduced-motion`

---

## Duration Scale

| Category | Duration | Usage |
|----------|----------|-------|
| Instant | 100ms | Hover states, toggle switches |
| Fast | 150ms | Button press, small state changes |
| Normal | 200–250ms | Standard transitions, dropdowns |
| Moderate | 300–350ms | Page transitions, modals |
| Slow | 400–500ms | Complex animations, page loads |
| Very slow | 500ms+ | Onboarding walkthroughs only |

**Rule**: If duration > 500ms, show progress indicator.

---

## Easing Curves

```css
:root {
  /* Standard (default for most UI) */
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1);

  /* Entering elements (decelerate) */
  --ease-in: cubic-bezier(0, 0, 0.2, 1);

  /* Exiting elements (accelerate) */
  --ease-out: cubic-bezier(0.4, 0, 1, 1);

  /* State changes (symmetric) */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);

  /* Playful/bounce */
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* Sharp (snappy interactions) */
  --ease-sharp: cubic-bezier(0.4, 0, 0.6, 1);
}
```

### When to Use Each
| Curve | When |
|-------|------|
| `default` | Most transitions, buttons, cards |
| `in` | Elements entering view, modals appearing |
| `out` | Elements exiting view, modals closing |
| `spring` | Playful feedback, celebrations, bounces |
| `sharp` | Toggles, switches, instant feedback |

---

## Common Animations

### Hover Effects
```css
/* Card lift */
.card {
  transition: transform 0.2s var(--ease-default), box-shadow 0.2s var(--ease-default);
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Button scale */
.btn {
  transition: transform 0.1s var(--ease-default);
}
.btn:active {
  transform: scale(0.97);
}

/* Color transition */
.link {
  transition: color 0.15s var(--ease-default);
}
```

### Focus Indicators
```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  transition: outline-offset 0.1s var(--ease-default);
}
```

### Dropdown/Popover
```css
.dropdown-menu {
  opacity: 0;
  transform: translateY(-8px) scale(0.95);
  transition: opacity 0.15s var(--ease-out), transform 0.15s var(--ease-out);
}

.dropdown-menu.open {
  opacity: 1;
  transform: translateY(0) scale(1);
}
```

### Modal
```css
.modal-backdrop {
  opacity: 0;
  transition: opacity 0.2s var(--ease-in);
}

.modal-backdrop.open {
  opacity: 1;
}

.modal-content {
  opacity: 0;
  transform: translateY(16px) scale(0.95);
  transition: opacity 0.2s var(--ease-out), transform 0.2s var(--ease-out);
}

.modal-backdrop.open .modal-content {
  opacity: 1;
  transform: translateY(0) scale(1);
}
```

### Sidebar Expand/Collapse
```css
.sidebar {
  width: 240px;
  transition: width 0.2s var(--ease-in-out);
}

.sidebar.collapsed {
  width: 64px;
}
```

### Accordion
```css
.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.25s var(--ease-in-out);
}

.accordion-content.open {
  max-height: 500px; /* or use auto with JS */
}
```

### Skeleton Loading
```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(90deg, var(--color-bg-secondary) 25%, var(--color-bg-tertiary) 50%, var(--color-bg-secondary) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-md);
}
```

### Spinner
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--color-border);
  border-top-color: var(--color-primary);
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
  animation: fadeIn 0.2s var(--ease-out);
}
```

### Slide In
```css
@keyframes slideInRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}

.slide-in-right {
  animation: slideInRight 0.3s var(--ease-out);
}
```

---

## Page Transitions

### Crossfade
```css
.page-enter {
  opacity: 0;
}
.page-enter-active {
  opacity: 1;
  transition: opacity 0.3s var(--ease-in);
}
.page-exit {
  opacity: 1;
}
.page-exit-active {
  opacity: 0;
  transition: opacity 0.3s var(--ease-out);
}
```

### Slide + Fade
```css
@keyframes pageIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

main {
  animation: pageIn 0.3s var(--ease-out);
}
```

---

## Staggered Animations

For lists and grids, stagger child animations:
```css
@keyframes itemIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.list-item {
  animation: itemIn 0.2s var(--ease-out) backwards;
}

.list-item:nth-child(1) { animation-delay: 0ms; }
.list-item:nth-child(2) { animation-delay: 50ms; }
.list-item:nth-child(3) { animation-delay: 100ms; }
.list-item:nth-child(4) { animation-delay: 150ms; }
.list-item:nth-child(5) { animation-delay: 200ms; }
```

---

## Reduced Motion

Always respect user preferences:
```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

**JavaScript check**:
```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Skip animation, apply final state immediately
}
```

---

## Anti-Patterns

- **No animation**: Don't animate decorative elements without purpose
- **No bouncy/elastic**: Avoid for serious UI; save for celebrations
- **No infinite loops**: Auto-playing animations exhaust users
- **No flashing**: Max 3 flashes per second (seizure risk)
- **No animation > 500ms**: Show progress or simplify
- **No blocking**: Don't prevent interaction during animation
