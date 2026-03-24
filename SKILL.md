---
name: ui-designer
description: Design beautiful interfaces using 16+ design systems including Material You, Fluent Design, Apple HIG, Ant Design, Carbon Design, Shopify Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Neumorphism, Skeuomorphism, Claymorphism, Swiss Design, and Atlassian Design. Expert in Tailwind CSS, color harmonics, component theming, and accessibility (WCAG).
---

# UI Designer Skill

Expert design guidance for creating aesthetically pleasing, user-centric interfaces across multiple design languages. This skill focuses on the visual and structural design intent before and during implementation.

When a user asks for Ant Design, enterprise UI, admin tools, dashboards, operational software, or high-density workflows, bias toward Ant Design principles as a decision framework, not just a visual style.

## Core Capabilities

### 1. Color Palette Generation
Generate cohesive and harmonic color palettes tailored to the project's vibe.
- Deliverables: HEX codes, Tailwind config extensions, and CSS variables.
- Palettes: Refer to `$WORKSPACE/assets/design-guides/coloring-guide.md` for specific style constraints.

### 2. Component Theming
Establish robust theme systems (Light/Dark) through consistent design tokens.
- Define --bg, --text, --accent, and --border variables.
- **Strictly No generic AI Purple/Indigo gradients.**

### 2.5. Principle-Driven UX
Choose patterns based on product behavior, not just visual taste.
- `Natural`: reduce cognitive load with familiar structure, plain labeling, and interaction flows that match user expectations.
- `Certain`: keep hierarchy, spacing, states, and component behavior predictable across pages.
- `Meaningful`: every surface, control, and motion must support the user task; avoid decorative noise.
- `Growing`: design systems should scale with product complexity and help users discover deeper capability over time.

### 3. Iconography
- **FontAwesome 6**: Use as the primary source for all UI icons.
- **Emoji Usage**: Strictly forbidden in functional UI (buttons, headers, navigation). Use only for content expression when natural.

## Design Systems Library (16 Total)

| Category | System | Key Traits | Best For | Reference |
|----------|--------|------------|----------|-----------|
| **Enterprise** | Fluent Design | Acrylic materials, reveal effects, 5 principles | Windows apps, Microsoft 365, enterprise | [fluent-design.md](references/fluent-design.md) |
| **Enterprise** | Ant Design | Natural, 8px grid, 12-column | Admin panels, B2B, data-heavy apps | [ant-design.md](references/ant-design.md) |
| **Enterprise** | Carbon Design | 16-column grid, IBM Plex, clarity | Enterprise software, data visualization | [carbon-design.md](references/carbon-design.md) |
| **Enterprise** | Atlassian Design | Bold, collaboration-focused, 8px grid | Project management, team tools | [atlassian-design.md](references/atlassian-design.md) |
| **Platform** | Apple HIG | SF Pro, vibrancy, blur materials, 44pt targets | iOS, macOS, native apps | [apple-hig.md](references/apple-hig.md) |
| **Platform** | Shopify Polaris | Merchant-focused, fresh, teal brand | E-commerce, merchant tools | [shopify-polaris.md](references/shopify-polaris.md) |
| **Modern** | Material You | Dynamic color, large corners, tonal palettes | Android, modern web apps | [material-you.md](references/material-you.md) |
| **Modern** | Glassmorphism | Backdrop blur, vibrant gradients | Dashboards, hero sections | [glassmorphism.md](references/glassmorphism.md) |
| **Modern** | Neumorphism | Soft 3D, dual shadows, monochromatic | Creative projects, minimal UI | [neumorphism.md](references/neumorphism.md) |
| **Modern** | Neo-Brutalism | Thick borders, hard shadows, bold colors | Creative agencies, artistic brands | [neo-brutalism.md](references/neo-brutalism.md) |
| **Modern** | Claymorphism | Soft 3D, double inner shadows, playful | Playful apps, consumer products | [claymorphism.md](references/claymorphism.md) |
| **Classic** | Minimalism | Typography-driven, generous padding | Content sites, portfolios | [minimalism.md](references/minimalism.md) |
| **Classic** | Swiss Design | 12-column grid, no shadows, asymmetric | Professional services, typography | [swiss-design.md](references/swiss-design.md) |
| **Classic** | Skeuomorphism | Realistic textures, physical mimicry | Luxury products, vintage themes | [skeuomorphism.md](references/skeuomorphism.md) |
| **Hybrid** | M3 Pastel Glass | Material + Glass, 28px corners | Modern SaaS, creative tools | [m3-pastel-glass.md](references/m3-pastel-glass.md) |
| **Hybrid** | Neo-M3 Hybrid | Brutalism + M3, 3px borders, hard shadows | Tech media, editorial sites | [neo-m3-hybrid.md](references/neo-m3-hybrid.md) |

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
- Primary design language? (Choose from 16+ systems)
- Color vibe? (Pastel, Dark, High-Contrast, Monochromatic, Brand-specific)
- Target platform? (Web, iOS, Android, Desktop, Cross-platform)

If the product is workflow-heavy, multi-role, form-heavy, or data-dense, recommend `Ant Design` by default unless the user has a clear brand/system constraint.

For Ant Design-oriented work, evaluate every proposal against these checks:
- `Natural`: is the flow obvious without explanation?
- `Certain`: are actions, states, and information hierarchy consistent?
- `Meaningful`: does each element earn its place in the task flow?
- `Growing`: will this still work when the product gains more roles, data, or features?

### 2. Component Architecture
Plan the HTML/React structure with Tailwind classes. Focus on Grid/Flex layouts and responsiveness.

For Ant Design-oriented component architecture:
- Prefer clear page scaffolding: page header, filters/actions row, primary content region, secondary detail/supporting region.
- Use an 8px spacing rhythm and restrained radii/shadows.
- Favor familiar enterprise patterns: tables, forms, segmented actions, status tags, empty states, inline validation, and immediate feedback.
- Keep density efficient but readable. Enterprise UI should feel calm, not barren or overloaded.
- Treat motion as functional feedback, not decoration.

## Best Practices
- **Anti-AI Aesthetic**: ABSOLUTELY NO purple/indigo gradients or generic "AI glossy" looks. Avoid excessive emojis in UI; use FontAwesome 6 instead.
- **Coloring**: Refer to `$WORKSPACE/assets/design-guides/coloring-guide.md` for per-style color standards.
- **Consistency**: Stick to one design language per project.
- **Accessibility**: Ensure enough contrast for text.
- **Ant Design Usage**: For enterprise/admin work, optimize for clarity, predictability, and task completion before visual novelty.
- **Azzar's Rule**: "Just enough engineering to get it done well." (Wong edan mah ajaib).
