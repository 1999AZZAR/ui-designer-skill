# Apple Human Interface Guidelines (HIG)

Apple's design language emphasizing clarity, deference, and depth. Creates intuitive, beautiful experiences across iOS, iPadOS, macOS, watchOS, and visionOS.

## Design Principles

### 1. Clarity
Text is legible, icons are precise, functionality is obvious.
- Sharp, crisp typography
- Ample negative space
- Clear visual hierarchy
- Purposeful use of color

### 2. Deference
Content takes precedence over UI elements.
- Subtle, unobtrusive interface
- Content-first approach
- Translucent backgrounds
- Minimal chrome

### 3. Depth
Visual layers and realistic motion enhance understanding.
- Layered interface elements
- Parallax effects
- Smooth, natural animations
- Spatial relationships

## Color System

### iOS System Colors
```
Blue: #007AFF
Green: #34C759
Indigo: #5856D6
Orange: #FF9500
Pink: #FF2D55
Purple: #AF52DE
Red: #FF3B30
Teal: #5AC8FA
Yellow: #FFCC00

Gray Scale (Light Mode):
Gray: #8E8E93
Gray 2: #AEAEB2
Gray 3: #C7C7CC
Gray 4: #D1D1D6
Gray 5: #E5E5EA
Gray 6: #F2F2F7

Gray Scale (Dark Mode):
Gray: #8E8E93
Gray 2: #636366
Gray 3: #48484A
Gray 4: #3A3A3C
Gray 5: #2C2C2E
Gray 6: #1C1C1E
```

### Semantic Colors
```
Label (Primary Text):
  Light: rgba(0, 0, 0, 1.0)
  Dark: rgba(255, 255, 255, 1.0)

Secondary Label:
  Light: rgba(60, 60, 67, 0.6)
  Dark: rgba(235, 235, 245, 0.6)

System Background:
  Light: #FFFFFF
  Dark: #000000

Secondary System Background:
  Light: #F2F2F7
  Dark: #1C1C1E
```

## Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', sans-serif;
```

### SF Pro Text Scale (≤19pt)
```
Large Title: 34px / 41px, Regular (400)
Title 1: 28px / 34px, Regular (400)
Title 2: 22px / 28px, Regular (400)
Title 3: 20px / 25px, Regular (400)
Headline: 17px / 22px, Semi-bold (600)
Body: 17px / 22px, Regular (400)
Callout: 16px / 21px, Regular (400)
Subhead: 15px / 20px, Regular (400)
Footnote: 13px / 18px, Regular (400)
Caption 1: 12px / 16px, Regular (400)
Caption 2: 11px / 13px, Regular (400)
```

### SF Pro Display Scale (≥20pt)
Used for larger sizes to maintain optical balance.

### Dynamic Type
Text sizes automatically adjust based on user preferences.

## Spacing System

iOS uses points (pt) for consistent spacing:
```
4pt, 8pt, 12pt, 16pt, 20pt, 24pt, 32pt, 44pt (minimum touch target)
```

### Safe Areas
Always respect safe areas on devices:
- Top: Status bar + notch
- Bottom: Home indicator
- Sides: Rounded corners

## Border Radius

### iOS Standard Radii
```
Small: 8pt
Medium: 10pt
Large: 12pt
Extra Large: 16pt
Continuous Curve: Apple's proprietary smooth curve
```

## Vibrancy & Materials

### Blur Effects
```css
/* Light Blur */
backdrop-filter: blur(20px) saturate(180%);
background: rgba(255, 255, 255, 0.72);

/* Dark Blur */
backdrop-filter: blur(20px) saturate(180%);
background: rgba(28, 28, 30, 0.72);

/* Ultra Thin Material */
backdrop-filter: blur(10px) saturate(150%);
background: rgba(255, 255, 255, 0.4);
```

### Shadow System
```css
/* Subtle Elevation */
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12),
            0 1px 2px rgba(0, 0, 0, 0.24);

/* Medium Elevation */
box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15),
            0 2px 4px rgba(0, 0, 0, 0.12);

/* High Elevation (Modal) */
box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15),
            0 3px 6px rgba(0, 0, 0, 0.10);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Filled Button -->
<button class="
  px-6 py-3 rounded-xl
  bg-[#007AFF] active:bg-[#0051D5]
  text-white text-[17px] font-semibold
  transition-colors duration-150
  active:scale-[0.97]
  min-h-[44px]
">
  Continue
</button>

<!-- Tinted Button -->
<button class="
  px-6 py-3 rounded-xl
  bg-[#007AFF]/10 active:bg-[#007AFF]/20
  text-[#007AFF] text-[17px] font-semibold
  transition-all duration-150
  min-h-[44px]
">
  Learn More
</button>

<!-- Borderless Button -->
<button class="
  px-4 py-2
  text-[#007AFF] active:text-[#0051D5] text-[17px]
  active:opacity-40
  transition-all duration-150
  min-h-[44px]
">
  Cancel
</button>
```

### List Item / Row
```html
<div class="
  px-4 py-3 min-h-[44px]
  bg-white dark:bg-[#1C1C1E]
  border-b border-[#C7C7CC]/30 dark:border-[#48484A]/30
  active:bg-[#D1D1D6]/50 dark:active:bg-[#2C2C2E]/50
  flex items-center justify-between
  transition-colors duration-150
  cursor-pointer
">
  <div class="flex items-center gap-3">
    <div class="w-10 h-10 rounded-full bg-[#007AFF] flex items-center justify-center text-white">
      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
        <path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
      </svg>
    </div>
    <div>
      <div class="text-[17px] text-black dark:text-white">John Appleseed</div>
      <div class="text-[15px] text-black/60 dark:text-white/60">Apple ID, iCloud, Media & Purchases</div>
    </div>
  </div>
  <svg class="w-5 h-5 text-[#C7C7CC] dark:text-[#48484A]" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/>
  </svg>
</div>
```

### Card with Blur Material
```html
<div class="
  p-6 rounded-2xl
  bg-white/72 dark:bg-[#1C1C1E]/72
  backdrop-blur-xl backdrop-saturate-[180%]
  shadow-[0_3px_6px_rgba(0,0,0,0.15),0_2px_4px_rgba(0,0,0,0.12)]
">
  <h3 class="text-[22px] font-semibold mb-2 text-black dark:text-white">
    Featured Content
  </h3>
  <p class="text-[17px] text-black/60 dark:text-white/60 leading-snug">
    Beautiful, translucent card with Apple's signature blur material effect.
  </p>
</div>
```

### Text Field
```html
<div class="space-y-2">
  <label class="text-[13px] text-black/60 dark:text-white/60 uppercase tracking-wide">
    Email
  </label>
  <input
    type="email"
    placeholder="name@example.com"
    class="
      w-full px-4 py-3 rounded-xl
      bg-[#F2F2F7] dark:bg-[#1C1C1E]
      text-[17px] text-black dark:text-white
      border border-transparent
      focus:bg-white dark:focus:bg-[#2C2C2E]
      focus:border-[#007AFF] focus:outline-none focus:ring-2 focus:ring-[#007AFF]/20
      placeholder:text-black/30 dark:placeholder:text-white/30
      transition-all duration-200
      min-h-[44px]
    "
  />
</div>
```

### Toggle Switch
```html
<label class="inline-flex items-center cursor-pointer min-h-[44px]">
  <div class="relative">
    <input type="checkbox" class="sr-only peer" />
    <div class="
      w-[51px] h-[31px] rounded-full
      bg-[#C7C7CC] dark:bg-[#48484A]
      peer-checked:bg-[#34C759]
      peer-focus:ring-2 peer-focus:ring-[#34C759]/50
      transition-colors duration-200
    "></div>
    <div class="
      absolute top-[2px] left-[2px]
      w-[27px] h-[27px] rounded-full
      bg-white
      shadow-[0_3px_8px_rgba(0,0,0,0.15),0_1px_1px_rgba(0,0,0,0.16)]
      peer-checked:translate-x-[20px]
      transition-transform duration-200
    "></div>
  </div>
  <span class="ml-3 text-[17px] text-black dark:text-white">
    Enable Notifications
  </span>
</label>
```

### Navigation Bar
```html
<nav class="
  h-[44px] px-4
  bg-white/72 dark:bg-[#1C1C1E]/72
  backdrop-blur-xl backdrop-saturate-[180%]
  border-b border-black/10 dark:border-white/10
  flex items-center justify-between
">
  <button class="text-[#007AFF] text-[17px] active:opacity-40 transition-opacity">
    Cancel
  </button>
  <h1 class="text-[17px] font-semibold text-black dark:text-white">
    Settings
  </h1>
  <button class="text-[#007AFF] text-[17px] font-semibold active:opacity-40 transition-opacity">
    Done
  </button>
</nav>
```

### Segmented Control
```html
<div class="
  inline-flex p-0.5 rounded-lg
  bg-[#E5E5EA] dark:bg-[#2C2C2E]
">
  <button class="
    px-4 py-1.5 rounded-md
    bg-white dark:bg-[#3A3A3C]
    text-[13px] font-semibold text-black dark:text-white
    shadow-[0_1px_3px_rgba(0,0,0,0.12)]
    transition-all duration-200
  ">
    Day
  </button>
  <button class="
    px-4 py-1.5 rounded-md
    text-[13px] font-medium text-black/60 dark:text-white/60
    hover:text-black dark:hover:text-white
    transition-colors duration-200
  ">
    Week
  </button>
  <button class="
    px-4 py-1.5 rounded-md
    text-[13px] font-medium text-black/60 dark:text-white/60
    hover:text-black dark:hover:text-white
    transition-colors duration-200
  ">
    Month
  </button>
</div>
```

### Action Sheet Item
```html
<button class="
  w-full px-4 py-4 min-h-[56px]
  bg-white dark:bg-[#1C1C1E]
  border-b border-[#C7C7CC]/30 dark:border-[#48484A]/30
  text-[20px] text-[#007AFF]
  active:bg-[#D1D1D6]/50 dark:active:bg-[#2C2C2E]/50
  transition-colors duration-150
  text-center
">
  Take Photo
</button>
<button class="
  w-full px-4 py-4 min-h-[56px]
  bg-white dark:bg-[#1C1C1E]
  border-b border-[#C7C7CC]/30 dark:border-[#48484A]/30
  text-[20px] text-[#FF3B30]
  active:bg-[#D1D1D6]/50 dark:active:bg-[#2C2C2E]/50
  transition-colors duration-150
  text-center font-semibold
">
  Delete Photo
</button>
```

## Accessibility

### Dynamic Type
Support user text size preferences:
```css
@supports (font: -apple-system-body) {
  .dynamic-text {
    font: -apple-system-body;
  }
}
```

### VoiceOver Support
- All interactive elements labeled
- Logical navigation order
- Meaningful grouping

### Touch Targets
Minimum 44x44 points for all interactive elements.

### Color Contrast
- Meets WCAG AA standards
- Test in both light and dark modes
- Use semantic colors for adaptability

## Best Practices

1. **Respect Safe Areas**: Always account for notches, home indicators
2. **44pt Minimum**: All touch targets at least 44x44 points
3. **Dynamic Type**: Support user text size preferences
4. **Dark Mode**: Design for both appearances from the start
5. **SF Symbols**: Use Apple's icon system for consistency
6. **Vibrancy**: Leverage blur materials for depth
7. **Animations**: Keep transitions smooth and natural (200-400ms)
8. **Native Feel**: Match platform conventions and behaviors

## Platform-Specific Considerations

### iOS
- Tab bar at bottom
- Navigation bar at top
- Swipe gestures for navigation
- Pull to refresh

### macOS
- Menu bar integration
- Window chrome
- Keyboard shortcuts
- Toolbar patterns

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        ios: {
          blue: '#007AFF',
          green: '#34C759',
          indigo: '#5856D6',
          orange: '#FF9500',
          pink: '#FF2D55',
          purple: '#AF52DE',
          red: '#FF3B30',
          teal: '#5AC8FA',
          yellow: '#FFCC00',
          gray: {
            1: '#8E8E93',
            2: '#AEAEB2',
            3: '#C7C7CC',
            4: '#D1D1D6',
            5: '#E5E5EA',
            6: '#F2F2F7',
          },
        },
      },
      fontFamily: {
        'sf-pro': ['-apple-system', 'BlinkMacSystemFont', 'SF Pro Text', 'SF Pro Display', 'sans-serif'],
      },
      backdropBlur: {
        'apple': '20px',
      },
      backdropSaturate: {
        'apple': '180%',
      },
      minHeight: {
        'touch': '44px', // iOS minimum touch target
      },
      minWidth: {
        'touch': '44px',
      },
    },
  },
};
```
