---
name: ui-designer
description: Design beautiful interfaces using 16+ design systems including Material You, Fluent Design, Apple HIG, Ant Design, Carbon Design, Shopify Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Neumorphism, Skeuomorphism, Claymorphism, Swiss Design, and Atlassian Design. Expert in Tailwind CSS, color harmonics, component theming, and accessibility (WCAG).
---

# UI Designer Skill

Expert design guidance for creating aesthetically pleasing, user-centric interfaces across multiple design languages. This skill focuses on the visual and structural design intent before and during implementation.

## Core Capabilities

### 1. Color Palette Generation
Generate cohesive and harmonic color palettes tailored to the project's vibe.
- Deliverables: HEX codes, Tailwind config extensions, and CSS variables.
- Palettes: Default to high-end pastels, dark luxury, or tonal Material You sets.

### 2. Component Theming
Establish robust theme systems (Light/Dark) through consistent design tokens.
- Define --bg, --text, --accent, and --border variables.
- Ensure unified states (hover, focus, active) across all UI elements.

### 3. Accessibility Audits
Evaluate and refine interfaces for maximum inclusivity and compliance.
- Focus: WCAG AA/AAA contrast ratios, semantic HTML, and intuitive navigation.
- Guidance: ARIA attributes, focus ring management, and screen-reader friendliness.

## Design Systems Library

### Enterprise & Corporate Systems

#### 1. Fluent Design (Microsoft)
- **Key traits:** Light, depth, motion, material, scale; acrylic materials, reveal effects.
- **Best for:** Windows apps, Microsoft 365, enterprise applications.
- **Reference:** [fluent-design.md](references/fluent-design.md)

#### 2. Ant Design
- **Key traits:** Natural, certain, meaningful, growing; enterprise-focused, 8px grid.
- **Best for:** Admin panels, data-heavy applications, B2B products.
- **Reference:** [ant-design.md](references/ant-design.md)

#### 3. Carbon Design (IBM)
- **Key traits:** Clarity, efficiency, consistency, inclusive; 16-column grid, IBM Plex.
- **Best for:** Enterprise software, data visualization, professional tools.
- **Reference:** [carbon-design.md](references/carbon-design.md)

#### 4. Atlassian Design
- **Key traits:** Bold, optimistic, practical; collaboration-focused, 8px grid.
- **Best for:** Team collaboration tools, project management, workflow apps.
- **Reference:** [atlassian-design.md](references/atlassian-design.md)

### Platform-Specific Systems

#### 5. Apple Human Interface Guidelines (HIG)
- **Key traits:** Clarity, deference, depth; SF Pro typography, vibrancy, blur materials.
- **Best for:** iOS, iPadOS, macOS, watchOS apps with native feel.
- **Reference:** [apple-hig.md](references/apple-hig.md)

#### 6. Shopify Polaris
- **Key traits:** Fresh, efficient, considerate, trustworthy; merchant-focused.
- **Best for:** E-commerce, merchant tools, admin interfaces.
- **Reference:** [shopify-polaris.md](references/shopify-polaris.md)

### Modern Aesthetic Trends

#### 7. Material You (M3)
- **Key traits:** Large rounded corners, tonal color palettes, expressive typography.
- **Best for:** Android apps, modern web apps, dynamic color systems.
- **Reference:** [material-you.md](references/material-you.md)

#### 8. Glassmorphism
- **Key traits:** Backdrop blur, thin borders, vibrant background gradients.
- **Best for:** Modern dashboards, creative portfolios, hero sections.
- **Reference:** [glassmorphism.md](references/glassmorphism.md)

#### 9. Neumorphism (Soft UI)
- **Key traits:** Soft 3D depth, dual shadows, monochromatic, extruded surfaces.
- **Best for:** Landing pages, creative projects, minimal interfaces.
- **Reference:** [neumorphism.md](references/neumorphism.md)

#### 10. Neo-Brutalism
- **Key traits:** Thick black borders, hard shadows, vibrant clashing colors, bold typography.
- **Best for:** Creative agencies, bold brands, artistic portfolios.
- **Reference:** [neo-brutalism.md](references/neo-brutalism.md)

#### 11. Claymorphism
- **Key traits:** Soft 3D shapes, double inner shadows, large border radius, playful pastels.
- **Best for:** Playful apps, creative tools, modern consumer products.
- **Reference:** [claymorphism.md](references/claymorphism.md)

### Classic & Timeless Styles

#### 12. Minimalism
- **Key traits:** Generous padding, typography-driven hierarchy, neutral palettes.
- **Best for:** Content-focused sites, portfolios, editorial design.
- **Reference:** [minimalism.md](references/minimalism.md)

#### 13. Swiss Design (International Typographic Style)
- **Key traits:** Strict 12-column grid, massive sans-serif typography, zero border-radius, no shadows, restrained 1–2 color accent palette, asymmetric layouts, whitespace as structure.
- **Best for:** Professional services, Swiss brands, typography-focused designs.
- **Reference:** [swiss-design.md](references/swiss-design.md)

#### 14. Skeuomorphism
- **Key traits:** Realistic textures, materials, shadows; physical object mimicry.
- **Best for:** Luxury products, creative apps, nostalgic/vintage themes.
- **Reference:** [skeuomorphism.md](references/skeuomorphism.md)

### Hybrid Styles

#### 15. M3 Pastel Glass (Hybrid)
- **Key traits:** Pastel Blue/Deep Blue, 28px corners, morphing hover effects.
- **Best for:** Modern SaaS, creative tools with Material You base.
- **Reference:** [m3-pastel-glass.md](references/m3-pastel-glass.md)

#### 16. Neo-M3 Hybrid (Wired/Verge Style)
- **Key traits:** Wired/Verge inspired high-contrast, 3px solid black borders, hard shadows (6px+), 24px rounded corners, tonal pastel accents.
- **Best for:** Tech publications, media sites, bold editorial designs.
- **Reference:** [neo-m3-hybrid.md](references/neo-m3-hybrid.md)

## Automation: Cursor Integration

This skill can automatically update your project's `.cursorrules` to keep the AI aligned with your design goals.

### `apply_ui_rules.py`
Run this script to append design rules to your current directory's .cursorrules.

```bash
python3 $WORKSPACE/skills/ui-designer-skill/scripts/apply_ui_rules.py --style [fluent|ant|carbon|atlassian|apple-hig|polaris|material|minimal|glass|neumorphism|neo-brutalism|claymorphism|skeuomorphism|swiss|m3-pastel|neo-m3] --palette [pastel|dark|vibrant|mono]
```

## Workflows

### 1. Design Conception
When starting a new feature, ask for:
- Primary design language? (Choose from 16+ systems: Fluent, Ant, Carbon, Atlassian, Apple HIG, Polaris, Material You, Glassmorphism, Neumorphism, Neo-Brutalism, Claymorphism, Minimalism, Swiss Design, Skeuomorphism, or hybrid styles)
- Color vibe? (Pastel, Dark, High-Contrast, Monochromatic, Brand-specific)
- Target platform? (Web, iOS, Android, Desktop, Cross-platform)

### 2. Component Architecture
Plan the HTML/React structure with Tailwind classes. Focus on Grid/Flex layouts and responsiveness.

## Best Practices
- **Consistency:** Stick to one design language per project.
- **Accessibility:** Ensure enough contrast for text.
- **Azzar's Rule:** "Just enough engineering to get it done well." (Wong edan mah ajaib).
