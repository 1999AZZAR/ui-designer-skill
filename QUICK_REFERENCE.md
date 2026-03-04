# UI Designer Skill - Quick Reference

## Available Design Systems (16 Total)

### Enterprise & Corporate
| System | Best For | Key Color | Border Radius | Grid |
|--------|----------|-----------|---------------|------|
| **Fluent Design** | Windows apps, Microsoft 365 | Blue #0078D4 | 2-12px | Flexible |
| **Ant Design** | Admin panels, B2B | Blue #1677FF | 2-8px | 12-column |
| **Carbon Design** | Enterprise tools, IBM products | Blue #0F62FE | 0-8px | 16-column |
| **Atlassian** | Team collaboration, Jira-like | Blue #0052CC | 3-8px | 8-column |

### Platform-Specific
| System | Best For | Key Color | Border Radius | Special Features |
|--------|----------|-----------|---------------|------------------|
| **Apple HIG** | iOS, macOS apps | Blue #007AFF | 8-16px | 44pt touch targets |
| **Shopify Polaris** | E-commerce, merchant tools | Teal #008060 | 4-12px | Merchant-focused |

### Modern Aesthetic
| System | Best For | Key Trait | Shadow Style |
|--------|----------|-----------|--------------|
| **Material You** | Android, modern web | Dynamic color | Soft elevation |
| **Glassmorphism** | Hero sections, dashboards | Blur effects | Ambient |
| **Neumorphism** | Creative projects | Soft 3D | Dual (light+dark) |
| **Neo-Brutalism** | Bold brands, artistic | Thick borders | Hard offset |
| **Claymorphism** | Playful apps | Inflated 3D | Double inner |

### Classic & Timeless
| System | Best For | Key Trait | Notable |
|--------|----------|-----------|---------|
| **Minimalism** | Content sites, portfolios | Whitespace | Typography-driven |
| **Swiss Design** | Professional services | Grid system | No shadows |
| **Skeuomorphism** | Luxury products | Realistic textures | Rich gradients |

### Hybrid Styles
| System | Combines | Best For |
|--------|----------|----------|
| **M3 Pastel Glass** | Material + Glass | Modern SaaS |
| **Neo-M3** | Brutalism + M3 | Editorial/tech media |

## Quick Command

```bash
# Apply design system to project
python3 ./.agents/skills/ui-designer/scripts/apply_ui_rules.py \
  --style [design-system] \
  --palette [pastel|dark|vibrant|mono]
```

## Design System Selection Guide

**Need to choose?** Answer these:

1. **What's your product type?**
   - Enterprise software → Fluent, Ant, Carbon, Atlassian
   - E-commerce → Polaris
   - Mobile app → Apple HIG (iOS), Material (Android)
   - Creative/Portfolio → Neo-Brutalism, Glassmorphism
   - Professional service → Minimalism, Swiss

2. **What's your aesthetic preference?**
   - Modern & trendy → Material You, Glassmorphism, Neumorphism
   - Bold & artistic → Neo-Brutalism, Claymorphism
   - Classic & timeless → Minimalism, Swiss Design
   - Realistic & tactile → Skeuomorphism
   - Corporate & professional → Fluent, Carbon, Atlassian

3. **What's your target platform?**
   - Windows/Microsoft → Fluent Design
   - iOS/macOS → Apple HIG
   - Android → Material You
   - Web (any platform) → Any system
   - Cross-platform → Ant, Carbon, Material

## Reference Files Location

```
.agents/skills/ui-designer/references/
├── fluent-design.md
├── ant-design.md
├── carbon-design.md
├── atlassian-design.md
├── apple-hig.md
├── shopify-polaris.md
├── neumorphism.md
├── skeuomorphism.md
├── material-you.md
├── minimalism.md
├── glassmorphism.md
├── neo-brutalism.md
├── claymorphism.md
├── swiss-design.md
├── m3-pastel-glass.md
└── neo-m3-hybrid.md
```

## Common Use Cases

### Scenario-Based Recommendations

**Building a project management tool?**
→ Atlassian Design or Carbon Design

**Building an iOS app?**
→ Apple HIG

**Building a Shopify app?**
→ Shopify Polaris

**Building a creative portfolio?**
→ Neo-Brutalism or Glassmorphism

**Building enterprise dashboard?**
→ Fluent Design, Ant Design, or Carbon Design

**Building a content blog?**
→ Minimalism or Swiss Design

**Building a game UI?**
→ Skeuomorphism or Claymorphism

**Building modern SaaS product?**
→ Material You, M3 Pastel Glass, or Glassmorphism

## Component Coverage

Every design system reference includes Tailwind CSS examples for:

✔️ Buttons (primary, secondary, tertiary, danger, ghost)
✔️ Cards
✔️ Input fields
✔️ Select dropdowns
✔️ Toggle switches
✔️ Navigation bars
✔️ Alerts/Banners (success, error, warning, info)
✔️ Data tables
✔️ Progress bars
✔️ Breadcrumbs
✔️ Search bars
✔️ And more...

## Accessibility Standards

All design systems include:

- WCAG 2.1 AA compliance guidelines
- Color contrast requirements
- Focus state specifications
- Keyboard navigation patterns
- Screen reader considerations
- Touch target sizing
- Motion preferences

## Need Help?

1. Read the full reference file for detailed implementation
2. Check the Tailwind config extensions
3. Review component examples with copy-paste code
4. Follow accessibility guidelines
5. Apply best practices section

---

**Pro Tip**: Start with the design system that matches your platform or industry, then customize based on brand requirements.
