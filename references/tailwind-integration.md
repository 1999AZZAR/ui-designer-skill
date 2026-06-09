# Tailwind CSS Integration

Guidelines for using Tailwind CSS with the ui-designer skill.

## When to Use Tailwind

- Project already uses Tailwind CSS
- Rapid prototyping needed
- Utility-first approach preferred
- Component library (Headless UI, Radix) in stack
- Heroicons in use (native Tailwind integration)

## When NOT to Use Tailwind

- Enterprise systems with strict design tokens (Ant Design, Carbon)
- Design-first systems (Material Design with custom CSS)
- Projects without build tooling
- Static HTML without PostCSS

---

## Tailwind Config Defaults

```javascript
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}'],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      borderRadius: {
        'sm': '0.25rem',
        'md': '0.5rem',
        'lg': '0.75rem',
        'xl': '1rem',
      },
    },
  },
  plugins: [],
};
```

---

## Component Mapping

### Buttons
```html
<!-- Primary -->
<button class="bg-primary-600 text-white px-4 py-2 rounded-lg font-medium
               hover:bg-primary-700 active:bg-primary-800
               focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600
               transition-colors duration-150">
  Button
</button>

<!-- Secondary -->
<button class="border border-gray-300 text-gray-700 bg-white px-4 py-2 rounded-lg font-medium
               hover:bg-gray-50 active:bg-gray-100
               focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600
               transition-colors duration-150">
  Button
</button>

<!-- Ghost -->
<button class="text-gray-600 px-4 py-2 rounded-lg font-medium
               hover:bg-gray-100 active:bg-gray-200
               transition-colors duration-150">
  Button
</button>

<!-- Danger -->
<button class="bg-red-600 text-white px-4 py-2 rounded-lg font-medium
               hover:bg-red-700 active:bg-red-800
               focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-600
               transition-colors duration-150">
  Delete
</button>
```

### Inputs
```html
<div class="space-y-1">
  <label for="email" class="block text-sm font-medium text-gray-700">
    Email address <span class="text-red-500">*</span>
  </label>
  <input
    type="email"
    id="email"
    name="email"
    required
    class="block w-full rounded-lg border border-gray-300 px-3 py-2 text-sm
           placeholder:text-gray-400
           focus:border-primary-500 focus:outline-none focus:ring-1 focus:ring-primary-500
           disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500
           transition-colors duration-150"
  />
  <p class="text-sm text-gray-500">We'll never share your email.</p>
</div>
```

### Cards
```html
<div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm
            hover:shadow-md transition-shadow duration-200">
  <h3 class="text-lg font-semibold text-gray-900">Card Title</h3>
  <p class="mt-2 text-sm text-gray-600">Card description text.</p>
  <div class="mt-4 flex gap-2">
    <button class="text-sm font-medium text-primary-600 hover:text-primary-700">
      Action
    </button>
  </div>
</div>
```

### Modals
```html
<!-- Backdrop -->
<div class="fixed inset-0 z-50 bg-black/50 transition-opacity duration-200"></div>

<!-- Modal -->
<div class="fixed inset-0 z-50 flex items-center justify-center p-4">
  <div class="w-full max-w-md rounded-xl bg-white p-6 shadow-xl
              animate-in fade-in zoom-in-95 duration-200">
    <h2 class="text-lg font-semibold">Title</h2>
    <p class="mt-2 text-sm text-gray-600">Content here.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 rounded-lg">
        Cancel
      </button>
      <button class="px-4 py-2 text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 rounded-lg">
        Confirm
      </button>
    </div>
  </div>
</div>
```

### Tables
```html
<div class="overflow-x-auto rounded-xl border border-gray-200">
  <table class="min-w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
      <tr>
        <th class="px-4 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
          Name
        </th>
        <th class="px-4 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
          Status
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 bg-white">
      <tr class="hover:bg-gray-50 transition-colors duration-100">
        <td class="whitespace-nowrap px-4 py-3 text-sm text-gray-900">Item</td>
        <td class="whitespace-nowrap px-4 py-3 text-sm">
          <span class="inline-flex items-center rounded-full bg-green-50 px-2 py-1 text-xs font-medium text-green-700">
            Active
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## Responsive Classes

```html
<!-- Mobile-first approach -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
  <!-- Cards -->
</div>

<!-- Responsive spacing -->
<div class="p-4 sm:p-6 lg:p-8">
  <!-- Content -->
</div>

<!-- Responsive text -->
<h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold">
  Title
</h1>

<!-- Responsive visibility -->
<div class="hidden sm:block">Visible on tablet+</div>
<div class="sm:hidden">Mobile only</div>
```

---

## Dark Mode

```html
<!-- Class-based dark mode -->
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  <div class="border-gray-200 dark:border-gray-700">
    Content
  </div>
</div>
```

### Dark Mode Config
```javascript
module.exports = {
  darkMode: 'class',
  // ...
};
```

---

## Icon Integration

### Heroicons (Native Tailwind)
```html
<!-- Outline -->
<svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21" />
</svg>

<!-- Solid -->
<svg class="h-5 w-5 text-gray-500" viewBox="0 0 24 24" fill="currentColor">
  <path fill-rule="evenodd" d="M..." clip-rule="evenodd" />
</svg>
```

### Lucide + Tailwind
```html
<!-- Install: npm install lucide -->
<i data-lucide="home" class="h-5 w-5 text-gray-500"></i>
```

### Tabler + Tailwind
```html
<!-- Install: npm install @tabler/icons-webfont -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css" />
<i class="ti ti-home text-gray-500 text-xl"></i>
```

---

## Transitions & Animations

```html
<!-- Standard transition -->
<button class="transition-colors duration-150 hover:bg-gray-100">
  Hover me
</button>

<!-- Transform + shadow -->
<div class="transition-all duration-200 hover:-translate-y-0.5 hover:shadow-md">
  Card
</div>

<!-- Fade in -->
<div class="animate-in fade-in duration-200">
  Appears
</div>

<!-- Slide in from right -->
<div class="animate-in slide-in-from-right duration-300">
  Slides in
</div>

<!-- Spin (loading) -->
<svg class="h-5 w-5 animate-spin text-primary-600" viewBox="0 0 24 24">
  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" />
  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
</svg>
```

---

## Utility Patterns

### Focus Visible
```css
@layer utilities {
  .focus-ring {
    @apply focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600;
  }
}
```

### Truncate Text
```html
<p class="truncate max-w-xs">Long text that gets truncated with ellipsis</p>
```

### Scrollable Containers
```html
<div class="overflow-y-auto max-h-96 scrollbar-thin scrollbar-thumb-gray-300">
  Scrollable content
</div>
```

### Container Queries (Tailwind v3.3+)
```html
<div class="@container">
  <div class="@sm:flex @lg:grid @lg:grid-cols-3">
    Responsive to container width
  </div>
</div>
```
