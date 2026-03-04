# UI Designer Skill

> Comprehensive design system library with 16+ modern design languages for building beautiful, accessible interfaces.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Design Systems](https://img.shields.io/badge/Design%20Systems-16-brightgreen.svg)]()
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-Ready-38bdf8.svg)]()
[![WCAG 2.1 AA](https://img.shields.io/badge/WCAG-2.1%20AA-green.svg)]()

Expert design guidance for creating aesthetically pleasing, user-centric interfaces across multiple design languages. Production-ready components, accessibility-first approach, and comprehensive documentation.

## Features

- **16 Design Systems**: From enterprise (Fluent, Carbon, Ant) to creative (Neumorphism, Neo-Brutalism)
- **Production-Ready Components**: Copy-paste Tailwind CSS examples
- **Accessibility-First**: WCAG 2.1 AA compliance guidelines for every system
- **Comprehensive Documentation**: Color systems, typography, spacing, shadows, components
- **Tailwind Config Extensions**: Ready-to-use configuration for each design system
- **Platform-Specific**: Apple HIG, Shopify Polaris, and more

## Design Systems Library

### Enterprise & Corporate
| System | Best For | Documentation |
|--------|----------|---------------|
| **Fluent Design** (Microsoft) | Windows apps, enterprise software | [View →](references/fluent-design.md) |
| **Ant Design** | Admin panels, B2B products | [View →](references/ant-design.md) |
| **Carbon Design** (IBM) | Enterprise tools, data visualization | [View →](references/carbon-design.md) |
| **Atlassian Design** | Team collaboration, project management | [View →](references/atlassian-design.md) |

### Platform-Specific
| System | Best For | Documentation |
|--------|----------|---------------|
| **Apple HIG** | iOS, macOS, native experiences | [View →](references/apple-hig.md) |
| **Shopify Polaris** | E-commerce, merchant interfaces | [View →](references/shopify-polaris.md) |

### Modern Aesthetic
| System | Best For | Documentation |
|--------|----------|---------------|
| **Material You (M3)** | Android, modern web apps | [View →](references/material-you.md) |
| **Glassmorphism** | Hero sections, modern dashboards | [View →](references/glassmorphism.md) |
| **Neumorphism** | Creative projects, minimal interfaces | [View →](references/neumorphism.md) |
| **Neo-Brutalism** | Bold brands, artistic portfolios | [View →](references/neo-brutalism.md) |
| **Claymorphism** | Playful apps, consumer products | [View →](references/claymorphism.md) |

### Classic & Timeless
| System | Best For | Documentation |
|--------|----------|---------------|
| **Minimalism** | Content-focused sites, portfolios | [View →](references/minimalism.md) |
| **Swiss Design** | Professional services, typography-focused | [View →](references/swiss-design.md) |
| **Skeuomorphism** | Luxury products, nostalgic themes | [View →](references/skeuomorphism.md) |

### Hybrid Styles
| System | Combines | Documentation |
|--------|----------|---------------|
| **M3 Pastel Glass** | Material + Glassmorphism | [View →](references/m3-pastel-glass.md) |
| **Neo-M3 Hybrid** | Brutalism + Material | [View →](references/neo-m3-hybrid.md) |

## Quick Start

### 1. Installation

Clone the repository:
```bash
git clone https://github.com/1999AZZAR/ui-designer-skill.git
cd ui-designer-skill
```

### 2. Apply Design System

Use the automation script to inject design rules into your project:

```bash
python3 scripts/apply_ui_rules.py \
  --style fluent \
  --palette pastel
```

**Available Styles:**
`fluent`, `ant`, `carbon`, `atlassian`, `apple-hig`, `polaris`, `material`, `minimal`, `glass`, `neumorphism`, `neo-brutalism`, `claymorphism`, `skeuomorphism`, `swiss`, `m3-pastel`, `neo-m3`

**Available Palettes:**
`pastel`, `dark`, `vibrant`, `mono`

### 3. Use Components

Browse the reference files for copy-paste ready Tailwind CSS components:

```html
<!-- Example: Fluent Design Button -->
<button class="
  px-5 py-2.5 
  bg-[#0078D4] hover:bg-[#005A9E]
  text-white font-semibold text-sm
  rounded
  shadow-[0_0.3px_0.9px_rgba(0,0,0,0.1),0_1.6px_3.6px_rgba(0,0,0,0.13)]
  hover:shadow-[0_1.2px_3.6px_rgba(0,0,0,0.11),0_6.4px_14.4px_rgba(0,0,0,0.13)]
  transition-all duration-300
  active:scale-[0.98]
">
  Primary Action
</button>
```

## Documentation Structure

Each design system reference includes:

1. **Core Principles** - Design philosophy and guidelines
2. **Color System** - Complete palettes with hex codes
3. **Typography** - Font families, scales, weights
4. **Spacing System** - Consistent spacing tokens
5. **Border Radius** - Standard radii
6. **Elevation & Shadow** - Shadow systems with CSS
7. **Component Examples** - Tailwind CSS implementations
8. **Accessibility Guidelines** - WCAG compliance
9. **Best Practices** - Implementation recommendations
10. **Tailwind Config Extension** - Ready-to-use config

## Component Coverage

Every design system includes examples for:

- Buttons (primary, secondary, tertiary, danger, ghost)
- Cards
- Input fields
- Select dropdowns
- Toggle switches
- Navigation bars
- Alerts/Banners (success, error, warning, info)
- Data tables
- Progress bars
- Breadcrumbs
- Search bars
- And more...

## Choosing a Design System

### By Product Type
- **Enterprise Software** → Fluent, Ant, Carbon, Atlassian
- **E-commerce** → Shopify Polaris
- **Mobile Apps** → Apple HIG (iOS), Material You (Android)
- **Creative/Portfolio** → Neo-Brutalism, Glassmorphism, Neumorphism
- **Professional Services** → Minimalism, Swiss Design
- **Luxury Products** → Skeuomorphism

### By Aesthetic
- **Modern & Trendy** → Material You, Glassmorphism, Neumorphism
- **Bold & Artistic** → Neo-Brutalism, Claymorphism
- **Classic & Timeless** → Minimalism, Swiss Design
- **Realistic & Tactile** → Skeuomorphism
- **Corporate & Professional** → Fluent, Carbon, Atlassian

### By Platform
- **Windows/Microsoft** → Fluent Design
- **iOS/macOS** → Apple HIG
- **Android** → Material You
- **Cross-platform** → Ant, Carbon, Material

## Resources

- **[Quick Reference Guide](QUICK_REFERENCE.md)** - Fast lookup for all design systems
- **[Enhancement Summary](ENHANCEMENT_SUMMARY.md)** - Detailed changelog and improvements
- **[Reference Files](references/)** - Comprehensive documentation for each system

## Accessibility Standards

All design systems include:

- WCAG 2.1 AA compliance guidelines
- Color contrast requirements (4.5:1 minimum)
- Focus state specifications
- Keyboard navigation patterns
- Screen reader considerations
- Touch target sizing (44pt minimum)
- Motion preference support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for Contribution
- Additional design systems
- More component examples
- Framework-specific implementations (React, Vue, Svelte)
- Dark mode variants
- Animation examples
- Real-world project showcases

## License

MIT License - feel free to use in personal and commercial projects.

## Credits

Created and maintained by [Azzar](https://github.com/1999AZZAR)

Design system documentation based on:
- Microsoft Fluent Design System
- Ant Design by Alibaba
- IBM Carbon Design System
- Atlassian Design System
- Apple Human Interface Guidelines
- Shopify Polaris
- Google Material Design
- And other open design systems

## Support

- GitHub Issues: [Report bugs or request features](https://github.com/1999AZZAR/ui-designer-skill/issues)
- Discussions: [Ask questions and share ideas](https://github.com/1999AZZAR/ui-designer-skill/discussions)

---

**Made with precision and care** | 16 Design Systems | Production-Ready | Accessibility-First
