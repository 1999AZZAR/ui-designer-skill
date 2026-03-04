# Ant Design System

Ant Design is an enterprise-class UI design language and React component library created by Alibaba, emphasizing natural, efficient, and delightful user experiences.

## Design Principles

### 1. Natural
Inspired by nature's laws, creating familiar and intuitive interfaces.
- Visual feedback follows natural behavior
- Smooth transitions and animations
- Predictable interaction patterns

### 2. Certain
Design decisions grounded in certainty, not ambiguity.
- Clear visual hierarchy
- Consistent interaction patterns
- Predictable component behavior

### 3. Meaningful
Every element serves a purpose in user tasks.
- Task-focused design decisions
- Remove unnecessary elements
- Purposeful visual communication

### 4. Growing
Evolve with user needs and feedback.
- Scalable component architecture
- Flexible customization system
- Continuous improvement

## Color System

### Primary Colors
```
Ant Blue (Primary): #1677FF
Blue-1: #E6F4FF (lightest)
Blue-2: #BAE0FF
Blue-3: #91CAFF
Blue-4: #69B1FF
Blue-5: #4096FF
Blue-6: #1677FF (base)
Blue-7: #0958D9
Blue-8: #003EB3
Blue-9: #002C8C
Blue-10: #001D66 (darkest)
```

### Neutral Colors
```
Gray-1: #FFFFFF
Gray-2: #FAFAFA
Gray-3: #F5F5F5
Gray-4: #F0F0F0
Gray-5: #D9D9D9
Gray-6: #BFBFBF
Gray-7: #8C8C8C
Gray-8: #595959
Gray-9: #434343
Gray-10: #262626
Gray-11: #1F1F1F
Gray-12: #141414
Gray-13: #000000
```

### Functional Colors
```
Success: #52C41A
Warning: #FAAD14
Error: #FF4D4F
Info: #1677FF
Link: #1677FF
```

## Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, 'Noto Sans', sans-serif;
```

### Type Scale
```
H1: 38px / 46px line-height, Semi-bold (600)
H2: 30px / 38px line-height, Semi-bold (600)
H3: 24px / 32px line-height, Semi-bold (600)
H4: 20px / 28px line-height, Semi-bold (600)
H5: 16px / 24px line-height, Semi-bold (600)
Body Large: 16px / 24px line-height, Regular (400)
Body: 14px / 22px line-height, Regular (400)
Caption: 12px / 20px line-height, Regular (400)
```

### Font Weights
```
Regular: 400
Medium: 500
Semi-bold: 600
Bold: 700
```

## Spacing System

Ant Design uses 8px base unit:
```
4px (0.5x), 8px (1x), 12px (1.5x), 16px (2x), 24px (3x),
32px (4x), 40px (5x), 48px (6x), 64px (8x), 80px (10x)
```

## Border Radius
```
Small: 2px
Base: 6px
Large: 8px
Circle: 50%
```

## Layout Grid

12-column responsive grid system:
```
xs: < 576px
sm: ≥ 576px
md: ≥ 768px
lg: ≥ 992px
xl: ≥ 1200px
xxl: ≥ 1600px
```

Gutter spacing: 16px (default), 24px (desktop)

## Elevation & Shadow

```css
/* Shadow 1 (Hover) */
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);

/* Shadow 2 (Card) */
box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03),
            0 1px 6px -1px rgba(0, 0, 0, 0.02),
            0 2px 4px rgba(0, 0, 0, 0.02);

/* Shadow 3 (Dropdown) */
box-shadow: 0 6px 16px 0 rgba(0, 0, 0, 0.08),
            0 3px 6px -4px rgba(0, 0, 0, 0.12),
            0 9px 28px 8px rgba(0, 0, 0, 0.05);

/* Shadow 4 (Modal) */
box-shadow: 0 9px 28px 8px rgba(0, 0, 0, 0.05),
            0 6px 16px 0 rgba(0, 0, 0, 0.08),
            0 3px 6px -4px rgba(0, 0, 0, 0.12);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Primary Button -->
<button class="
  px-4 py-1.5 h-8
  bg-[#1677FF] hover:bg-[#4096FF]
  text-white text-sm font-normal
  rounded-md
  shadow-[0_2px_0_rgba(5,145,255,0.1)]
  hover:shadow-[0_2px_0_rgba(5,145,255,0.15)]
  active:bg-[#0958D9]
  transition-all duration-200
  disabled:bg-[#F5F5F5] disabled:text-[#BFBFBF] disabled:cursor-not-allowed
">
  Primary Button
</button>

<!-- Default Button -->
<button class="
  px-4 py-1.5 h-8
  bg-white hover:bg-white
  border border-[#D9D9D9] hover:border-[#4096FF]
  text-[#000000] hover:text-[#4096FF] text-sm
  rounded-md
  shadow-[0_2px_0_rgba(0,0,0,0.02)]
  hover:shadow-[0_2px_0_rgba(5,145,255,0.1)]
  transition-all duration-200
">
  Default Button
</button>

<!-- Dashed Button -->
<button class="
  px-4 py-1.5 h-8
  bg-white hover:bg-white
  border border-dashed border-[#D9D9D9] hover:border-[#4096FF]
  text-[#000000] hover:text-[#4096FF] text-sm
  rounded-md
  transition-all duration-200
">
  Dashed Button
</button>

<!-- Text Button -->
<button class="
  px-2 py-1.5 h-8
  bg-transparent hover:bg-[#F5F5F5]
  text-[#000000] hover:text-[#1677FF] text-sm
  rounded-md
  transition-all duration-200
">
  Text Button
</button>
```

### Card
```html
<div class="
  p-6 rounded-lg
  bg-white border border-[#F0F0F0]
  shadow-[0_1px_2px_rgba(0,0,0,0.03),0_1px_6px_-1px_rgba(0,0,0,0.02),0_2px_4px_rgba(0,0,0,0.02)]
  hover:shadow-[0_6px_16px_0_rgba(0,0,0,0.08),0_3px_6px_-4px_rgba(0,0,0,0.12),0_9px_28px_8px_rgba(0,0,0,0.05)]
  transition-shadow duration-300
">
  <h3 class="text-base font-semibold mb-2 text-[#000000]">Card Title</h3>
  <p class="text-sm text-[#595959]">
    Card content with Ant Design styling. Clean, professional, and enterprise-ready.
  </p>
</div>
```

### Input Field
```html
<div class="space-y-2">
  <label class="text-sm text-[#000000]">
    Email Address <span class="text-[#FF4D4F]">*</span>
  </label>
  <input
    type="email"
    placeholder="Enter email"
    class="
      w-full h-8 px-3
      bg-white border border-[#D9D9D9]
      rounded-md text-sm text-[#000000]
      hover:border-[#4096FF]
      focus:border-[#4096FF] focus:outline-none focus:ring-2 focus:ring-[#91CAFF] focus:ring-opacity-20
      placeholder:text-[#BFBFBF]
      disabled:bg-[#F5F5F5] disabled:cursor-not-allowed
      transition-all duration-200
    "
  />
</div>
```

### Select Dropdown
```html
<div class="space-y-2">
  <label class="text-sm text-[#000000]">Select Option</label>
  <select class="
    w-full h-8 px-3 pr-8
    bg-white border border-[#D9D9D9]
    rounded-md text-sm text-[#000000]
    hover:border-[#4096FF]
    focus:border-[#4096FF] focus:outline-none focus:ring-2 focus:ring-[#91CAFF] focus:ring-opacity-20
    appearance-none
    bg-[url('data:image/svg+xml;charset=UTF-8,%3csvg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"%3e%3cpolyline points=\"6 9 12 15 18 9\"%3e%3c/polyline%3e%3c/svg%3e')] bg-[length:16px_16px] bg-[right_8px_center] bg-no-repeat
    transition-all duration-200
  ">
    <option>Option 1</option>
    <option>Option 2</option>
    <option>Option 3</option>
  </select>
</div>
```

### Alert Messages
```html
<!-- Success Alert -->
<div class="
  px-4 py-2 rounded-lg
  bg-[#F6FFED] border border-[#B7EB8F]
  flex items-start gap-2
">
  <svg class="w-4 h-4 text-[#52C41A] mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-medium text-[#52C41A]">Success</div>
    <div class="text-sm text-[#000000]">Operation completed successfully!</div>
  </div>
</div>

<!-- Error Alert -->
<div class="
  px-4 py-2 rounded-lg
  bg-[#FFF2F0] border border-[#FFCCC7]
  flex items-start gap-2
">
  <svg class="w-4 h-4 text-[#FF4D4F] mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-medium text-[#FF4D4F]">Error</div>
    <div class="text-sm text-[#000000]">Something went wrong. Please try again.</div>
  </div>
</div>
```

### Table
```html
<div class="overflow-x-auto rounded-lg border border-[#F0F0F0]">
  <table class="w-full text-sm">
    <thead class="bg-[#FAFAFA] border-b border-[#F0F0F0]">
      <tr>
        <th class="px-4 py-3 text-left font-medium text-[#000000]">Name</th>
        <th class="px-4 py-3 text-left font-medium text-[#000000]">Age</th>
        <th class="px-4 py-3 text-left font-medium text-[#000000]">Address</th>
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-[#F0F0F0]">
      <tr class="hover:bg-[#FAFAFA] transition-colors">
        <td class="px-4 py-3 text-[#000000]">John Doe</td>
        <td class="px-4 py-3 text-[#000000]">32</td>
        <td class="px-4 py-3 text-[#595959]">New York, USA</td>
      </tr>
      <tr class="hover:bg-[#FAFAFA] transition-colors">
        <td class="px-4 py-3 text-[#000000]">Jane Smith</td>
        <td class="px-4 py-3 text-[#000000]">28</td>
        <td class="px-4 py-3 text-[#595959]">London, UK</td>
      </tr>
    </tbody>
  </table>
</div>
```

## Accessibility

### Focus States
All interactive elements have clear focus indicators:
```css
.focus-visible:focus-visible {
  outline: 2px solid #1677FF;
  outline-offset: 2px;
}
```

### Color Contrast
- Text on white: Gray-9 (#434343) and darker
- Primary actions: Blue-6 (#1677FF) meets AA standards
- Error states: Error (#FF4D4F) adjusted for readability

### Keyboard Navigation
- Tab order follows visual hierarchy
- All interactive elements keyboard accessible
- Escape key closes modals/dropdowns

## Best Practices

1. **Consistency**: Maintain 8px spacing rhythm throughout
2. **Hierarchy**: Use size and weight to establish importance
3. **Feedback**: Always provide visual feedback for interactions
4. **Efficiency**: Optimize for enterprise workflows and productivity
5. **Accessibility**: Meet WCAG 2.1 AA standards minimum
6. **Responsiveness**: Test across all breakpoints (xs to xxl)

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        ant: {
          blue: {
            1: '#E6F4FF',
            2: '#BAE0FF',
            3: '#91CAFF',
            4: '#69B1FF',
            5: '#4096FF',
            6: '#1677FF',
            7: '#0958D9',
            8: '#003EB3',
            9: '#002C8C',
            10: '#001D66',
          },
          gray: {
            1: '#FFFFFF',
            2: '#FAFAFA',
            3: '#F5F5F5',
            4: '#F0F0F0',
            5: '#D9D9D9',
            6: '#BFBFBF',
            7: '#8C8C8C',
            8: '#595959',
            9: '#434343',
            10: '#262626',
          },
          success: '#52C41A',
          warning: '#FAAD14',
          error: '#FF4D4F',
          info: '#1677FF',
        },
      },
      boxShadow: {
        'ant-hover': '0 2px 8px rgba(0, 0, 0, 0.08)',
        'ant-card': '0 1px 2px rgba(0,0,0,0.03), 0 1px 6px -1px rgba(0,0,0,0.02), 0 2px 4px rgba(0,0,0,0.02)',
        'ant-dropdown': '0 6px 16px 0 rgba(0,0,0,0.08), 0 3px 6px -4px rgba(0,0,0,0.12), 0 9px 28px 8px rgba(0,0,0,0.05)',
      },
      spacing: {
        '0.5': '4px',
        '1.5': '12px',
      },
    },
  },
};
```
