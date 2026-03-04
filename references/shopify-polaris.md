# Shopify Polaris Design System

Polaris is Shopify's design system for creating consistent, accessible merchant experiences across the Shopify admin and ecosystem.

## Design Principles

### 1. Fresh
Modern, clean aesthetic that feels current and trustworthy.
- Clean lines and shapes
- Contemporary color palette
- Modern typography
- Professional polish

### 2. Efficient
Optimize for merchant productivity and task completion.
- Streamlined workflows
- Clear hierarchy
- Purposeful interactions
- Reduced cognitive load

### 3. Considerate
Thoughtful, inclusive design for all merchants.
- Accessible by default
- Culturally aware
- Error prevention
- Helpful guidance

### 4. Trustworthy
Reliable, predictable experiences that merchants can depend on.
- Consistent patterns
- Clear feedback
- Transparent actions
- Professional quality

## Color System

### Primary Colors
```
Teal (Brand): #008060
Dark Teal: #004C3F
Ink (Text): #202223
Sky (Background): #F4F6F8
Surface: #FFFFFF
```

### Interactive Colors
```
Interactive (Default): #2C6ECB
Interactive Hover: #1F5199
Interactive Pressed: #103D70
Interactive Disabled: #BFC9D1

Critical (Error): #D82C0D
Critical Hover: #BC1B06
Warning: #FFC453
Success: #008060
Highlight: #5BCDDA
```

### Border Colors
```
Border Default: #C9CCCF
Border Subdued: #E1E3E5
Border Disabled: #D2D5D8
Border Critical: #FD5749
Border Success: #95C9B4
```

### Text Colors
```
Text Primary: #202223
Text Subdued: #6D7175
Text Disabled: #8C9196
Text Critical: #D82C0D
Text Success: #008060
Text Warning: #916A00
```

## Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', 
             Roboto, 'Helvetica Neue', sans-serif;
```

### Type Scale
```
Heading 2XL: 28px / 36px, Semi-bold (600)
Heading XL: 24px / 32px, Semi-bold (600)
Heading LG: 20px / 28px, Semi-bold (600)
Heading MD: 16px / 24px, Semi-bold (600)
Heading SM: 14px / 20px, Semi-bold (600)
Heading XS: 13px / 20px, Semi-bold (600)

Body LG: 16px / 24px, Regular (400)
Body MD: 14px / 20px, Regular (400)
Body SM: 13px / 20px, Regular (400)
Body XS: 12px / 16px, Regular (400)
```

## Spacing System

Polaris uses rem-based spacing with 4px base:
```
0.25rem (4px), 0.5rem (8px), 0.75rem (12px), 1rem (16px),
1.25rem (20px), 1.5rem (24px), 2rem (32px), 2.5rem (40px),
3rem (48px), 4rem (64px), 5rem (80px)
```

### Spacing Tokens
```
space-025: 4px
space-05: 8px
space-1: 16px
space-2: 32px
space-3: 48px
space-4: 64px
space-5: 80px
```

## Border Radius

```
Small: 4px (0.25rem)
Base: 8px (0.5rem)
Large: 12px (0.75rem)
Full: 9999px
```

## Elevation & Shadow

```css
/* Shadow 100 (Card) */
box-shadow: 0 1px 0 0 rgba(0, 0, 0, 0.05);

/* Shadow 200 (Popover) */
box-shadow: 0 3px 6px -3px rgba(23, 24, 24, 0.08),
            0 8px 20px -4px rgba(23, 24, 24, 0.12);

/* Shadow 300 (Modal) */
box-shadow: 0 4px 8px -2px rgba(23, 24, 24, 0.08),
            0 12px 32px -4px rgba(23, 24, 24, 0.12);

/* Shadow 400 (Dropdown) */
box-shadow: 0 8px 16px -4px rgba(23, 24, 24, 0.08),
            0 20px 40px -8px rgba(23, 24, 24, 0.12);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Primary Button -->
<button class="
  px-4 h-9
  bg-[#008060] hover:bg-[#004C3F]
  text-white text-sm font-medium
  rounded-lg
  shadow-[0_1px_0_0_rgba(0,0,0,0.05)]
  hover:shadow-[0_2px_4px_0_rgba(0,0,0,0.1)]
  active:shadow-[inset_0_2px_2px_0_rgba(0,0,0,0.1)]
  focus:outline-none focus:ring-2 focus:ring-[#008060] focus:ring-offset-2
  disabled:bg-[#BFC9D1] disabled:cursor-not-allowed
  transition-all duration-200
">
  Save changes
</button>

<!-- Secondary/Outline Button -->
<button class="
  px-4 h-9
  bg-white hover:bg-[#F4F6F8]
  border border-[#C9CCCF] hover:border-[#8C9196]
  text-[#202223] text-sm font-medium
  rounded-lg
  shadow-[0_1px_0_0_rgba(0,0,0,0.05)]
  focus:outline-none focus:ring-2 focus:ring-[#008060] focus:ring-offset-2
  disabled:bg-[#F4F6F8] disabled:border-[#E1E3E5] disabled:text-[#8C9196] disabled:cursor-not-allowed
  transition-all duration-200
">
  Cancel
</button>

<!-- Plain Button -->
<button class="
  px-4 h-9
  bg-transparent hover:bg-[#F4F6F8]
  text-[#2C6ECB] hover:text-[#1F5199] text-sm font-medium
  rounded-lg
  focus:outline-none focus:ring-2 focus:ring-[#2C6ECB] focus:ring-offset-2
  disabled:text-[#8C9196] disabled:cursor-not-allowed
  transition-all duration-200
">
  View details
</button>

<!-- Critical/Destructive Button -->
<button class="
  px-4 h-9
  bg-[#D82C0D] hover:bg-[#BC1B06]
  text-white text-sm font-medium
  rounded-lg
  shadow-[0_1px_0_0_rgba(0,0,0,0.05)]
  focus:outline-none focus:ring-2 focus:ring-[#D82C0D] focus:ring-offset-2
  transition-all duration-200
">
  Delete
</button>
```

### Card
```html
<div class="
  p-5 rounded-lg
  bg-white border border-[#E1E3E5]
  shadow-[0_1px_0_0_rgba(0,0,0,0.05)]
">
  <h3 class="text-base font-semibold mb-2 text-[#202223]">
    Card Title
  </h3>
  <p class="text-sm text-[#6D7175] leading-relaxed mb-4">
    Card description with Polaris styling. Clean and professional for merchant interfaces.
  </p>
  <button class="text-sm text-[#2C6ECB] hover:text-[#1F5199] font-medium">
    Learn more
  </button>
</div>
```

### Text Field
```html
<div class="space-y-1">
  <label class="block text-sm font-medium text-[#202223]">
    Store name
  </label>
  <input
    type="text"
    placeholder="Enter store name"
    class="
      w-full h-9 px-3
      bg-white border border-[#C9CCCF]
      rounded-lg text-sm text-[#202223]
      hover:border-[#8C9196]
      focus:border-[#2C6ECB] focus:outline-none focus:ring-2 focus:ring-[#2C6ECB] focus:ring-opacity-20
      disabled:bg-[#F4F6F8] disabled:border-[#D2D5D8] disabled:cursor-not-allowed
      placeholder:text-[#8C9196]
      transition-all duration-200
    "
  />
  <div class="text-xs text-[#6D7175]">
    This will be used as your store's display name
  </div>
</div>
```

### Banner (Alert)
```html
<!-- Success Banner -->
<div class="
  p-4 rounded-lg
  bg-[#F1F8F5] border-l-4 border-[#008060]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#008060] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#008060] mb-1">
      Changes saved successfully
    </div>
    <div class="text-sm text-[#202223]">
      Your store settings have been updated.
    </div>
  </div>
</div>

<!-- Critical Banner -->
<div class="
  p-4 rounded-lg
  bg-[#FFF4F4] border-l-4 border-[#D82C0D]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#D82C0D] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#D82C0D] mb-1">
      There was an error
    </div>
    <div class="text-sm text-[#202223]">
      Unable to save changes. Please try again.
    </div>
  </div>
</div>

<!-- Info Banner -->
<div class="
  p-4 rounded-lg
  bg-[#F4F6F8] border-l-4 border-[#2C6ECB]
  flex items-start gap-3
">
  <svg class="w-5 h-5 text-[#2C6ECB] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
  </svg>
  <div>
    <div class="text-sm font-semibold text-[#2C6ECB] mb-1">
      New feature available
    </div>
    <div class="text-sm text-[#202223]">
      Check out the latest updates to your dashboard.
    </div>
  </div>
</div>
```

### Data Table
```html
<div class="overflow-x-auto rounded-lg border border-[#E1E3E5] bg-white">
  <table class="w-full text-sm">
    <thead class="bg-[#F4F6F8] border-b border-[#E1E3E5]">
      <tr>
        <th class="px-4 py-3 text-left text-xs font-semibold text-[#202223] uppercase tracking-wide">
          Product
        </th>
        <th class="px-4 py-3 text-left text-xs font-semibold text-[#202223] uppercase tracking-wide">
          Status
        </th>
        <th class="px-4 py-3 text-right text-xs font-semibold text-[#202223] uppercase tracking-wide">
          Price
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-[#E1E3E5]">
      <tr class="hover:bg-[#F4F6F8] transition-colors">
        <td class="px-4 py-3 text-[#202223] font-medium">Blue T-Shirt</td>
        <td class="px-4 py-3">
          <span class="inline-flex items-center px-2 py-0.5 rounded-full bg-[#F1F8F5] text-[#008060] text-xs font-medium">
            Active
          </span>
        </td>
        <td class="px-4 py-3 text-right text-[#202223]">$29.99</td>
      </tr>
      <tr class="hover:bg-[#F4F6F8] transition-colors">
        <td class="px-4 py-3 text-[#202223] font-medium">Red Hoodie</td>
        <td class="px-4 py-3">
          <span class="inline-flex items-center px-2 py-0.5 rounded-full bg-[#FEF7F0] text-[#916A00] text-xs font-medium">
            Draft
          </span>
        </td>
        <td class="px-4 py-3 text-right text-[#202223]">$59.99</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Checkbox
```html
<label class="inline-flex items-center cursor-pointer">
  <input type="checkbox" class="
    w-5 h-5 
    text-[#008060] 
    border-[#C9CCCF] rounded
    focus:ring-2 focus:ring-[#008060] focus:ring-offset-2
    hover:border-[#8C9196]
    transition-colors
  " />
  <span class="ml-2 text-sm text-[#202223]">
    I agree to the terms and conditions
  </span>
</label>
```

### Select Dropdown
```html
<div class="space-y-1">
  <label class="block text-sm font-medium text-[#202223]">
    Country/Region
  </label>
  <select class="
    w-full h-9 px-3 pr-8
    bg-white border border-[#C9CCCF]
    rounded-lg text-sm text-[#202223]
    hover:border-[#8C9196]
    focus:border-[#2C6ECB] focus:outline-none focus:ring-2 focus:ring-[#2C6ECB] focus:ring-opacity-20
    appearance-none
    bg-[url('data:image/svg+xml;charset=UTF-8,%3csvg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\" fill=\"%236D7175\"%3e%3cpath fill-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" clip-rule=\"evenodd\"/%3e%3c/svg%3e')] bg-[length:20px_20px] bg-[right_8px_center] bg-no-repeat
    transition-all duration-200
  ">
    <option>United States</option>
    <option>Canada</option>
    <option>United Kingdom</option>
  </select>
</div>
```

### Loading Spinner
```html
<div class="inline-flex items-center gap-2">
  <div class="
    w-5 h-5
    border-2 border-[#E1E3E5] border-t-[#008060]
    rounded-full
    animate-spin
  "></div>
  <span class="text-sm text-[#6D7175]">Loading...</span>
</div>
```

## Accessibility

### Focus States
Polaris enforces 2px focus rings:
```css
.focus-visible:focus-visible {
  outline: none;
  ring: 2px solid #008060;
  ring-offset: 2px;
}
```

### Color Contrast
- All text meets WCAG AA standards (4.5:1)
- Interactive elements have 3:1 contrast
- Error/success colors are distinguishable

### Keyboard Navigation
- All components keyboard accessible
- Logical tab order
- Skip links for complex layouts

## Best Practices

1. **Merchant-First**: Always prioritize merchant workflows and efficiency
2. **Consistency**: Use Polaris components to maintain uniformity
3. **Clarity**: Clear labels, helpful errors, obvious actions
4. **Accessibility**: Build inclusive experiences from the start
5. **Performance**: Fast load times and responsive interactions
6. **Mobile-Ready**: Responsive design for all screen sizes
7. **Feedback**: Always provide feedback for user actions

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        polaris: {
          teal: '#008060',
          'teal-dark': '#004C3F',
          ink: '#202223',
          sky: '#F4F6F8',
          surface: '#FFFFFF',
          interactive: '#2C6ECB',
          'interactive-hover': '#1F5199',
          critical: '#D82C0D',
          'critical-hover': '#BC1B06',
          warning: '#FFC453',
          success: '#008060',
          border: '#C9CCCF',
          'border-subdued': '#E1E3E5',
          'text-subdued': '#6D7175',
          'text-disabled': '#8C9196',
        },
      },
      boxShadow: {
        'polaris-card': '0 1px 0 0 rgba(0, 0, 0, 0.05)',
        'polaris-popover': '0 3px 6px -3px rgba(23,24,24,0.08), 0 8px 20px -4px rgba(23,24,24,0.12)',
        'polaris-modal': '0 4px 8px -2px rgba(23,24,24,0.08), 0 12px 32px -4px rgba(23,24,24,0.12)',
      },
    },
  },
};
```
