# Accessibility

WCAG 2.1 AA compliance patterns for all UI designs.

## Core Principles (POUR)

1. **Perceivable** — Information must be presentable in ways users can perceive
2. **Operable** — UI components must be operable via various input methods
3. **Understandable** — Information and UI operation must be understandable
4. **Robust** — Content must be robust enough for diverse user agents

---

## Color & Contrast

### Minimum Contrast Ratios
| Element | Ratio | Example |
|---------|-------|---------|
| Normal text (<24px) | 4.5:1 | Body text, labels |
| Large text (≥24px or ≥18.66px bold) | 3:1 | Headings, buttons |
| UI components & graphics | 3:1 | Icons, borders, form controls |
| Focus indicators | 3:1 | Focus rings |

### Color Usage Rules
- Never use color alone to convey information (add icon, text, or pattern)
- Error states: red + icon + text message
- Success states: green + icon + text
- Links: underline or distinct style, not just color change

### Testing Tools
- Chrome DevTools → Rendering → Emulate vision deficiencies
- Contrast checker: webaim.org/resources/contrastchecker

---

## Focus Management

### Focus Ring Styling
```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* High contrast mode support */
@media (forced-colors: active) {
  :focus-visible {
    outline: 2px solid LinkText;
  }
}
```

### Focus Order
- Logical tab order: top → bottom, left → right
- Skip navigation link (first element in DOM)
- Modal: trap focus inside, return focus on close
- Dropdown: arrow keys navigate options

### Skip Navigation
```html
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <nav>...</nav>
  <main id="main-content">...</main>
</body>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px 16px;
  background: var(--color-primary);
  color: white;
  z-index: 1000;
  transition: top 0.2s;
}
.skip-link:focus {
  top: 0;
}
</style>
```

---

## Semantic HTML

### Required Landmarks
```html
<header>     <!-- Site/app header -->
<nav>        <!-- Navigation -->
<main>       <!-- Primary content (one per page) -->
<aside>      <!-- Sidebar/complementary -->
<footer>     <!-- Site/app footer -->
<section>    <!-- Thematic grouping -->
<article>    <!-- Self-contained content -->
```

### Heading Hierarchy
```
h1: Page title (one per page)
  h2: Major sections
    h3: Subsections
      h4: Sub-subsections
```
- Never skip heading levels (h1 → h3)
- Use headings for structure, not styling

### Lists
- Navigation items: `<ul>` or `<ol>`
- Repeated items: `<ul>` (settings, features, etc.)
- Step-by-step: `<ol>`

---

## Forms & Inputs

### Labels
```html
<!-- Every input MUST have a visible label -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" required>

<!-- Placeholder is NOT a substitute for label -->
<input type="text" placeholder="Email">  <!-- BAD -->
```

### Error Handling
```html
<div class="form-field" role="group" aria-labelledby="email-label">
  <label id="email-label" for="email">
    Email address <span aria-hidden="true">*</span>
  </label>
  <input
    type="email"
    id="email"
    aria-required="true"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <span id="email-error" role="alert" class="error">
    Please enter a valid email address
  </span>
</div>
```

### Required Fields
- Visual indicator: `*` or "(Required)"
- `aria-required="true"` on input
- Don't rely on color alone for required indicator

### Fieldsets
```html
<fieldset>
  <legend>Shipping address</legend>
  <!-- address fields -->
</fieldset>
```

---

## ARIA Patterns

### Live Regions (Dynamic Content)
```html
<!-- Status updates -->
<div role="status" aria-live="polite">
  3 results found
</div>

<!-- Error alerts -->
<div role="alert" aria-live="assertive">
  Form submission failed
</div>

<!-- Loading states -->
<div role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  Loading...
</div>
```

### Common ARIA Attributes
| Attribute | Usage |
|-----------|-------|
| `aria-label` | Label when visible text isn't available |
| `aria-labelledby` | References visible text as label |
| `aria-describedby` | Additional description |
| `aria-hidden="true"` | Hide decorative elements from screen readers |
| `aria-expanded` | Toggle state (dropdowns, accordions) |
| `aria-selected` | Selected state (tabs) |
| `aria-current="page"` | Current page in navigation |

### Icon Buttons
```html
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>
```

### Modals
```html
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-desc"
>
  <h2 id="modal-title">Confirm deletion</h2>
  <p id="modal-desc">This action cannot be undone.</p>
</div>
```

---

## Keyboard Navigation

### Standard Interactions
| Key | Action |
|-----|--------|
| Tab | Move to next focusable element |
| Shift+Tab | Move to previous |
| Enter/Space | Activate buttons, links |
| Arrow keys | Navigate within groups (tabs, menus, radios) |
| Escape | Close modals, dropdowns, menus |
| Home | First item in list/grid |
| End | Last item in list/grid |

### Custom Components
- Tabs: arrow keys switch tabs, Tab moves into panel
- Menus: arrow keys navigate items, Escape closes
- Combobox: type to filter, arrow keys select
- Tree view: arrow keys navigate, expanded with Enter

---

## Images & Media

### Images
```html
<img src="photo.jpg" alt="Team meeting in conference room" />
<img src="chart.png" alt="" role="presentation" />  <!-- Decorative -->
```

**Alt text rules**:
- Informative images: descriptive alt text
- Decorative images: `alt=""` or `aria-hidden="true"`
- Complex images (charts, graphs): alt + long description

### Video/Audio
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" />
</video>
```
- Always include captions for video
- Provide transcripts for audio
- No auto-play with sound

---

## Tables

```html
<table>
  <caption>Quarterly sales by region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Q1</th>
      <th scope="col">Q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>$10,000</td>
      <td>$12,000</td>
    </tr>
  </tbody>
</table>
```

- Always include `<caption>` or `aria-label`
- Use `scope="col"` on column headers
- Use `scope="row"` on row headers
- Complex tables: `headers` attribute

---

## Motion & Animation

### Reduced Motion
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

**Rules**:
- Respect `prefers-reduced-motion` for all animations
- No flashing content (3 flashes per second max)
- Provide pause/stop controls for auto-updating content

---

## Testing Checklist

- [ ] All images have appropriate alt text
- [ ] All form inputs have visible labels
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 UI)
- [ ] All interactive elements are keyboard accessible
- [ ] Focus order is logical
- [ ] Skip navigation link present
- [ ] ARIA attributes used correctly
- [ ] Headings are in logical order
- [ ] Tables have headers and captions
- [ ] Reduced motion preferences respected
- [ ] Screen reader tested (VoiceOver/NVDA)
- [ ] No keyboard traps
- [ ] Error messages are associated with inputs
