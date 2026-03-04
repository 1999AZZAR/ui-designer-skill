# Reference File Template (80-100 lines max)

## Design Principles (3-5 bullet points)
- Core principle 1
- Core principle 2
- Core principle 3

## Color System (Table format)

| Type | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Blue | #0000FF | Actions, links |
| Secondary | Gray | #808080 | Backgrounds |
| Success | Green | #00FF00 | Success states |
| Error | Red | #FF0000 | Error states |

## Typography (Table format)

| Scale | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| H1 | 32px | 600 | 40px | Page titles |
| Body | 16px | 400 | 24px | Content |
| Caption | 12px | 400 | 16px | Labels |

## Spacing (Single line)
Base: 4px | Scale: 4, 8, 12, 16, 24, 32, 48, 64

## Shadows (2-3 examples max)
```css
sm: 0 1px 2px rgba(0,0,0,0.1)
md: 0 4px 6px rgba(0,0,0,0.1)
lg: 0 10px 15px rgba(0,0,0,0.1)
```

## Border Radius
Small: 4px | Medium: 8px | Large: 16px | Full: 9999px

## Quick Component Examples (3-4 only, reference assets/ for more)

### Button
```html
<button class="px-4 py-2 bg-blue-500 text-white rounded">Primary</button>
```
See `assets/components/[system]-buttons.md` for all variants.

### Card  
```html
<div class="p-6 bg-white rounded-lg shadow-md">Card</div>
```
See `assets/components/[system]-cards.md` for all variants.

## Accessibility
- WCAG 2.1 AA: 4.5:1 text contrast minimum
- Focus: 2px solid ring, offset 2px
- Touch targets: 44px minimum

## Tailwind Config
```js
colors: { primary: '#0000FF' }
spacing: { '128': '32rem' }
```

## Reference
Full components: `assets/components/[system]-*.md`
