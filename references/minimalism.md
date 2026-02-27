# Minimalism (Functional Elegance)

"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away." — Antoine de Saint-Exupéry. Minimalist design is the art of extreme intentionality.

---

## 🎨 Design DNA

| Property | Value |
|---|---|
| **Border Radius** | Subtle: `6px` – `12px`. Just enough to break the edge. |
| **Borders** | Rare. Use `0.5px` or `1px` with low-contrast colors (e.g., `#f1f1f1`). |
| **Shadows** | **Ambient** only. Very large blur, very low opacity (2%-5%). |
| **Typography** | `Inter`, `Geist`, or `Plus Jakarta Sans`. Strict size scale. |
| **Spacing** | **Generous**. `gap-12`, `p-20`. Spacing *is* the divider. |

---

## 🎨 The "Quiet" Palette

| Name | Hex Code | Tailwind Class |
|---|---|---|
| **Snow White** | `#FFFFFF` | `bg-white` |
| **Paper** | `#FAFAFA` | `bg-zinc-50` |
| **Soft Graphite** | `#18181B` | `bg-zinc-900` |
| **Ghost Text** | `#71717A` | `text-zinc-500` |
| **Deep Ink** | `#09090B` | `bg-zinc-950` |

---

## 🧩 Components

### 1. The "Border-less" Content Section
Don't use boxes. Use hierarchy and space.
```html
<section class="max-w-3xl mx-auto py-32 px-8">
    <span class="text-xs font-bold uppercase tracking-widest text-zinc-400 mb-4 block">Process</span>
    <h2 class="text-4xl font-bold tracking-tight mb-8">Refining the core.</h2>
    <p class="text-lg text-zinc-500 leading-relaxed">
        We strip away the noise until only the essence remains. A design system that feels invisible, allowing content to take the lead.
    </p>
</section>
```

### 2. The "Subtle" Button
Minimalism doesn't mean boring. It means refined.
```css
.btn-minimal {
    padding: 0.75rem 1.5rem;
    border-radius: 99px;
    background: #000;
    color: #fff;
    font-weight: 600;
    transition: opacity 0.2s ease;
}
.btn-minimal:hover {
    opacity: 0.8;
}
.btn-minimal-ghost {
    background: transparent;
    color: #000;
    text-decoration: underline;
    text-underline-offset: 4px;
}
```

### 3. Navigation (Pure Text)
```html
<nav class="flex justify-between items-center py-12 px-20">
    <div class="font-black text-xl tracking-tighter">MEMA.</div>
    <div class="flex gap-12 text-sm font-medium text-zinc-500">
        <a href="#" class="hover:text-black transition-colors">Work</a>
        <a href="#" class="hover:text-black transition-colors">Lab</a>
        <a href="#" class="hover:text-black transition-colors">Contact</a>
    </div>
</nav>
```

---

## 💡 layout Strategy

1. **Focus on the 80/20 Rule** — Only show the 20% of information that provides 80% of the value. Hide everything else in sub-menus or tooltips.
2. **Invisible Dividers** — Use empty columns (margins) instead of horizontal lines to separate content blocks.
3. **Contrast as Guide** — Use varying shades of gray (Zinc 500 to 900) to communicate hierarchy instead of different colors.

---

## 🚫 Anti-Patterns

- ❌ **Drop Shadows with Color**: Shadows should always be neutral/black with very low opacity.
- ❌ **Nested Boxes**: Avoid "a box inside a box inside a box". Use white space.
- ❌ **Icons for Everything**: Only use icons if they are universally understood. Text is often clearer.
- ❌ **Bouncy Animations**: Movement should be linear or subtle ease-in-out.

---

## 💡 Pro-Tip
Use `letter-spacing: -0.02em` on large minimalist headings to make them feel "tighter" and more professionally set.
