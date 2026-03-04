# Atlassian Design System

Atlassian's design system for building collaborative, intuitive products across the Atlassian ecosystem including Jira, Confluence, Trello, and Bitbucket.

## Design Principles

### 1. Bold, Optimistic, Practical
Make products feel confident, positive, and useful.
- Clear, decisive design choices
- Optimistic color palette
- Practical, task-focused layouts

### 2. Approachable
Lower barriers and welcome all skill levels.
- Plain language
- Clear visual hierarchy
- Helpful guidance
- Forgiving errors

### 3. Trustworthy
Build confidence through consistency and reliability.
- Predictable patterns
- Consistent behavior
- Transparent feedback
- Professional polish

## Color System

### Primary Colors
```
Blue (Brand): #0052CC
Blue 400: #0065FF
Blue 500: #0052CC (base)
Blue 600: #0747A6

Purple: #5243AA
Teal: #00B8D9
Green: #00875A
Yellow: #FFAB00
Red: #DE350B
```

### Neutral Colors
```
N0 (White): #FFFFFF
N10: #FAFBFC
N20: #F4F5F7
N30: #EBECF0
N40: #DFE1E6
N50: #C1C7D0
N60: #B3BAC5
N70: #A5ADBA
N80: #97A0AF
N90: #8993A4
N100: #7A869A
N200: #6B778C
N300: #5E6C84
N400: #505F79
N500: #42526E
N600: #344563
N700: #253858
N800: #172B4D
N900: #091E42
```

### Semantic Colors
```
Success (Green): #00875A
Success Light: #E3FCEF

Warning (Yellow): #FFAB00
Warning Light: #FFFAE6

Error (Red): #DE350B
Error Light: #FFEBE6

Info (Blue): #0065FF
Info Light: #DEEBFF
```

## Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Oxygen', 'Ubuntu', 'Fira Sans', 'Droid Sans', 
             'Helvetica Neue', sans-serif;
```

### Type Scale
```
Heading XXL: 35px / 40px, Medium (500)
Heading XL: 29px / 32px, Medium (500)
Heading Large: 24px / 28px, Medium (500)
Heading Medium: 20px / 24px, Medium (500)
Heading Small: 16px / 20px, Semi-bold (600)
Heading XSmall: 14px / 16px, Semi-bold (600)

Body: 14px / 20px, Regular (400)
Body Small: 12px / 16px, Regular (400)
Body Large: 16px / 24px, Regular (400)
```

## Spacing System

Atlassian uses 8px grid system:
```
2px, 4px, 6px, 8px, 12px, 16px, 24px, 32px, 40px, 48px
```

### Spacing Tokens
```
space-025: 2px
space-050: 4px
space-075: 6px
space-100: 8px
space-150: 12px
space-200: 16px
space-300: 24px
space-400: 32px
space-500: 40px
space-600: 48px
```

## Border Radius

```
Small: 3px
Default: 3px
Large: 8px
Circle: 50%
```

## Elevation & Shadow

```css
/* Raised */
box-shadow: 0 1px 1px rgba(9, 30, 66, 0.25),
            0 0 1px rgba(9, 30, 66, 0.31);

/* Overflow */
box-shadow: 0 4px 8px -2px rgba(9, 30, 66, 0.25),
            0 0 1px rgba(9, 30, 66, 0.31);

/* Overlay */
box-shadow: 0 8px 12px -4px rgba(9, 30, 66, 0.25),
            0 0 1px rgba(9, 30, 66, 0.31);

/* Dialog */
box-shadow: 0 12px 24px -6px rgba(9, 30, 66, 0.25),
            0 0 1px rgba(9, 30, 66, 0.31);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Primary Button -->
<button class="
  px-4 h-8
  bg-[#0052CC] hover:bg-[#0747A6]
  text-white text-sm font-medium
  rounded-sm
  shadow-[0_1px_1px_rgba(9,30,66,0.25),0_0_1px_rgba(9,30,66,0.31)]
  focus:outline-none focus:ring-2 focus:ring-[#0065FF]
  disabled:bg-[#F4F5F7] disabled:text-[#A5ADBA] disabled:cursor-not-allowed
  transition-all duration-200
">
  Create issue
</button>

<!-- Default Button -->
<button class="
  px-4 h-8
  bg-[#FAFBFC] hover:bg-[#EBECF0]
  text-[#172B4D] text-sm font-medium
  rounded-sm
  shadow-[0_1px_1px_rgba(9,30,66,0.25),0_0_1px_rgba(9,30,66,0.31)]
  focus:outline-none focus:ring-2 focus:ring-[#0065FF]
  transition-all duration-200
">
  Cancel
</button>

<!-- Subtle Button -->
<button class="
  px-4 h-8
  bg-transparent hover:bg-[#EBECF0]
  text-[#42526E] hover:text-[#172B4D] text-sm font-medium
  rounded-sm
  focus:outline-none focus:ring-2 focus:ring-[#0065FF]
  transition-all duration-200
">
  View details
</button>

<!-- Link Button -->
<button class="
  px-2 h-8
  text-[#0052CC] hover:text-[#0747A6] hover:underline text-sm
  focus:outline-none focus:ring-2 focus:ring-[#0065FF] rounded-sm
  transition-colors duration-200
">
  Learn more
</button>

<!-- Danger Button -->
<button class="
  px-4 h-8
  bg-[#DE350B] hover:bg-[#BF2600]
  text-white text-sm font-medium
  rounded-sm
  shadow-[0_1px_1px_rgba(9,30,66,0.25),0_0_1px_rgba(9,30,66,0.31)]
  focus:outline-none focus:ring-2 focus:ring-[#DE350B]
  transition-all duration-200
">
  Delete
</button>
```

### Text Field
```html
<div class="space-y-1">
  <label class="block text-xs font-semibold text-[#42526E] uppercase">
    Summary
  </label>
  <input
    type="text"
    placeholder="Enter issue summary"
    class="
      w-full h-10 px-2
      bg-[#FAFBFC] border-2 border-[#DFE1E6]
      rounded-sm text-sm text-[#172B4D]
      hover:bg-white hover:border-[#B3BAC5]
      focus:bg-white focus:border-[#0052CC] focus:outline-none
      placeholder:text-[#6B778C]
      transition-all duration-200
    "
  />
  <div class="text-xs text-[#6B778C]">
    Brief description of the issue
  </div>
</div>
```

### Select Dropdown
```html
<div class="space-y-1">
  <label class="block text-xs font-semibold text-[#42526E] uppercase">
    Priority
  </label>
  <select class="
    w-full h-10 px-2 pr-8
    bg-[#FAFBFC] border-2 border-[#DFE1E6]
    rounded-sm text-sm text-[#172B4D]
    hover:bg-white hover:border-[#B3BAC5]
    focus:bg-white focus:border-[#0052CC] focus:outline-none
    appearance-none
    bg-[url('data:image/svg+xml;charset=UTF-8,%3csvg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\" fill=\"%236B778C\"%3e%3cpath fill-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" clip-rule=\"evenodd\"/%3e%3c/svg%3e')] bg-[length:20px_20px] bg-[right_4px_center] bg-no-repeat
    transition-all duration-200
  ">
    <option>Highest</option>
    <option>High</option>
    <option>Medium</option>
    <option>Low</option>
    <option>Lowest</option>
  </select>
</div>
```

### Card
```html
<div class="
  p-4 rounded-sm
  bg-white border border-[#DFE1E6]
  shadow-[0_1px_1px_rgba(9,30,66,0.25),0_0_1px_rgba(9,30,66,0.31)]
  hover:shadow-[0_4px_8px_-2px_rgba(9,30,66,0.25),0_0_1px_rgba(9,30,66,0.31)]
  transition-shadow duration-200
">
  <h3 class="text-base font-semibold mb-2 text-[#172B4D]">
    JIRA-1234
  </h3>
  <p class="text-sm text-[#42526E] mb-3">
    Fix authentication issue in user login flow
  </p>
  <div class="flex items-center gap-2">
    <span class="px-2 py-0.5 rounded-sm bg-[#FFEBE6] text-[#DE350B] text-xs font-medium">
      Bug
    </span>
    <span class="px-2 py-0.5 rounded-sm bg-[#DEEBFF] text-[#0052CC] text-xs font-medium">
      High
    </span>
  </div>
</div>
```

### Banner (Inline Message)
```html
<!-- Info Banner -->
<div class="
  px-4 py-3 rounded-sm
  bg-[#DEEBFF] border-l-4 border-[#0052CC]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#0052CC] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#172B4D] mb-1">
      Information
    </div>
    <div class="text-sm text-[#42526E]">
      This is an informational message with helpful context.
    </div>
  </div>
</div>

<!-- Success Banner -->
<div class="
  px-4 py-3 rounded-sm
  bg-[#E3FCEF] border-l-4 border-[#00875A]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#00875A] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#172B4D] mb-1">
      Success
    </div>
    <div class="text-sm text-[#42526E]">
      Your changes have been saved successfully.
    </div>
  </div>
</div>

<!-- Warning Banner -->
<div class="
  px-4 py-3 rounded-sm
  bg-[#FFFAE6] border-l-4 border-[#FFAB00]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#FFAB00] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#172B4D] mb-1">
      Warning
    </div>
    <div class="text-sm text-[#42526E]">
      Please review your changes before proceeding.
    </div>
  </div>
</div>

<!-- Error Banner -->
<div class="
  px-4 py-3 rounded-sm
  bg-[#FFEBE6] border-l-4 border-[#DE350B]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#DE350B] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#172B4D] mb-1">
      Error
    </div>
    <div class="text-sm text-[#42526E]">
      Unable to complete action. Please try again.
    </div>
  </div>
</div>
```

### Toggle Switch
```html
<label class="inline-flex items-center cursor-pointer">
  <div class="relative">
    <input type="checkbox" class="sr-only peer" />
    <div class="
      w-10 h-6 rounded-full
      bg-[#DFE1E6] peer-checked:bg-[#0052CC]
      transition-colors duration-200
    "></div>
    <div class="
      absolute top-1 left-1
      w-4 h-4 rounded-full
      bg-white
      shadow-[0_2px_4px_rgba(9,30,66,0.4)]
      peer-checked:translate-x-4
      transition-transform duration-200
    "></div>
  </div>
  <span class="ml-3 text-sm text-[#42526E]">
    Enable notifications
  </span>
</label>
```

### Progress Bar
```html
<div class="space-y-2">
  <div class="flex justify-between text-sm text-[#42526E]">
    <span>Progress</span>
    <span>7 of 10 complete</span>
  </div>
  <div class="
    h-2 rounded-full
    bg-[#DFE1E6]
    overflow-hidden
  ">
    <div class="
      h-full w-[70%] rounded-full
      bg-[#0052CC]
      transition-all duration-500
    "></div>
  </div>
</div>
```

### Breadcrumb Navigation
```html
<nav class="flex items-center gap-2 text-sm">
  <a href="#" class="text-[#42526E] hover:text-[#0052CC] transition-colors">
    Projects
  </a>
  <svg class="w-4 h-4 text-[#97A0AF]" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/>
  </svg>
  <a href="#" class="text-[#42526E] hover:text-[#0052CC] transition-colors">
    Project Alpha
  </a>
  <svg class="w-4 h-4 text-[#97A0AF]" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/>
  </svg>
  <span class="text-[#172B4D] font-medium">
    Issues
  </span>
</nav>
```

## Accessibility

### Focus States
Clear 2px focus rings:
```css
.focus-visible:focus-visible {
  outline: none;
  ring: 2px solid #0065FF;
}
```

### Color Contrast
- All text meets WCAG AA (4.5:1 minimum)
- Interactive elements have 3:1 contrast
- Status colors distinguishable in grayscale

### Keyboard Navigation
- All interactive elements keyboard accessible
- Logical tab order
- Skip navigation links
- Escape key closes modals/dropdowns

## Best Practices

1. **Consistency**: Use Atlassian components for unified experiences
2. **Clarity**: Clear labels, helpful errors, obvious actions
3. **Efficiency**: Optimize for common workflows
4. **Accessibility**: Build inclusive experiences from start
5. **Collaboration**: Design for team-based workflows
6. **Feedback**: Always provide clear feedback for actions
7. **Hierarchy**: Use spacing and typography to establish importance

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        atlassian: {
          blue: {
            400: '#0065FF',
            500: '#0052CC',
            600: '#0747A6',
          },
          purple: '#5243AA',
          teal: '#00B8D9',
          green: '#00875A',
          yellow: '#FFAB00',
          red: '#DE350B',
          neutral: {
            0: '#FFFFFF',
            10: '#FAFBFC',
            20: '#F4F5F7',
            30: '#EBECF0',
            40: '#DFE1E6',
            50: '#C1C7D0',
            100: '#7A869A',
            200: '#6B778C',
            300: '#5E6C84',
            400: '#505F79',
            500: '#42526E',
            800: '#172B4D',
            900: '#091E42',
          },
        },
      },
      spacing: {
        '0.5': '2px',
        '1.5': '6px',
      },
      boxShadow: {
        'atlassian-raised': '0 1px 1px rgba(9,30,66,0.25), 0 0 1px rgba(9,30,66,0.31)',
        'atlassian-overflow': '0 4px 8px -2px rgba(9,30,66,0.25), 0 0 1px rgba(9,30,66,0.31)',
        'atlassian-overlay': '0 8px 12px -4px rgba(9,30,66,0.25), 0 0 1px rgba(9,30,66,0.31)',
      },
    },
  },
};
```
