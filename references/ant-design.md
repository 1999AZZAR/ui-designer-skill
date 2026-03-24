# Ant Design System

Enterprise-class UI design by Alibaba for natural, efficient experiences. Use this system when the product has dense workflows, repeat use, multiple roles, complex forms, or data-heavy operational tasks.

## Design Principles

- **Natural**: Inspired by nature's laws, familiar interactions
- **Certain**: Grounded decisions, clear hierarchy, predictable behavior
- **Meaningful**: Purpose-driven, task-focused, no waste
- **Growing**: Evolves with feedback, scalable architecture

## Principle Translation

Apply the four values as working rules:

### Natural
- Prefer familiar mental models over novel layouts.
- Reduce cognitive load with clear grouping, obvious labels, and visually scannable hierarchy.
- Use interaction patterns users already expect in enterprise tools: tables, forms, drawers, modals, filters, pagination, tabs.

### Certain
- Keep spacing, typography, status colors, and component states consistent across the product.
- Make interactive outcomes predictable: hover, active, disabled, loading, success, error.
- Default to explicit labels and visible system status rather than cleverness.

### Meaningful
- Each control should map to a real task or decision.
- Decorative motion, copy, and ornamentation should be minimal.
- Feedback should be immediate and useful: validation, progress, empty states, confirmations.

### Growing
- Design information architecture so the system can absorb more data, more user roles, and more advanced workflows without collapsing.
- Reveal advanced functionality progressively instead of front-loading all complexity.
- Favor reusable tokens, components, and page patterns.

## Recommended Usage Heuristics

- Best for: admin panels, CMS, CRMs, dashboards, back-office systems, internal tools, order management, analytics.
- Avoid using it as-is for: highly expressive consumer branding, editorial experiences, or products that depend on strong visual distinctiveness.
- If used for a branded product, keep the Ant behavioral rules and page logic, then layer brand voice carefully on top.

## Color System

| Type | Hex | Usage |
|------|-----|-------|
| Ant Blue 6 | #1677FF | Primary actions |
| Blue 7 | #0958D9 | Hover |
| Blue 8 | #003EB3 | Active |
| Success | #52C41A | Success states |
| Warning | #FAAD14 | Warnings |
| Error | #FF4D4F | Errors |

### Neutrals
Gray 1-10: #FFFFFF → #262626 (10 shades)

## Typography

| Scale | Size | Weight | Usage |
|-------|------|--------|-------|
| H1 | 38px | 600 | Major headings |
| H2 | 30px | 600 | Page titles |
| H3 | 24px | 600 | Sections |
| Body | 14px | 400 | Content |
| Caption | 12px | 400 | Labels |

**Font:** -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif

## Spacing

**Base:** 8px | **Scale:** 4, 8, 12, 16, 24, 32, 40, 48, 64, 80

## Shadows

```css
hover: 0 2px 8px rgba(0,0,0,0.08)
card: 0 1px 2px rgba(0,0,0,0.03), 0 1px 6px -1px rgba(0,0,0,0.02)
dropdown: 0 6px 16px 0 rgba(0,0,0,0.08), 0 3px 6px -4px rgba(0,0,0,0.12)
```

## Border Radius

Small: 2px | Base: 6px | Large: 8px | Circle: 50%

## Grid System

12-column responsive | xs: <576px, sm: ≥576px, md: ≥768px, lg: ≥992px, xl: ≥1200px, xxl: ≥1600px

## Page Structure

A strong default Ant-style page layout:
- Page title and concise context summary
- Primary actions near the title or top-right
- Filters/search before the data region
- Main content in cards, tables, lists, or form sections
- Secondary detail in drawers, side panels, tabs, or expandable rows
- Empty, loading, and error states designed as first-class views

## Quick Examples

### Button
```html
<button class="px-4 h-8 bg-[#1677FF] hover:bg-[#4096FF] text-white 
  rounded-md shadow-[0_2px_0_rgba(5,145,255,0.1)]">
  Primary
</button>
```

### Card
```html
<div class="p-6 bg-white border border-[#F0F0F0] rounded-lg 
  shadow-[0_1px_2px_rgba(0,0,0,0.03)]">
  Card
</div>
```

Full components: `assets/components/ant-*.md`

## Accessibility

- **WCAG 2.1 AA**: 4.5:1 minimum
- **Focus**: 2px solid #1677FF, offset 2px
- **Keyboard**: Tab order follows visual hierarchy

## Behavior Guidance

- Immediate feedback beats delayed surprise.
- Default to inline validation where possible.
- Use modals for confirmation or blocking tasks; use drawers for contextual editing; use toasts/messages for lightweight system feedback.
- Keep action priority obvious: primary, secondary, tertiary, dangerous.

## Tailwind Config

```js
colors: {
  ant: {
    blue: { 1: '#E6F4FF', 6: '#1677FF', 10: '#001D66' },
    gray: { 2: '#FAFAFA', 5: '#D9D9D9', 10: '#262626' }
  }
}
```

## Reference

**Components:** `assets/components/ant-components.md`  
**Official:** https://ant.design
