# Settings Archetype

Use for account settings, preferences, configuration, permissions, and product setup surfaces.

## Best System Fits

- `ant`
- `apple-hig`
- `material`
- `polaris`

## Core Regions

- page header with title and short explanation
- left nav, tabs, or grouped sections
- main form area with strong labels and helper text
- save/reset/footer action region

## Behavior Rules

- Group by user mental model, not backend schema
- Prefer progressive disclosure for advanced settings
- Show validation inline whenever possible
- Keep destructive actions visually separated

## Good Hybrids

- `ant` + `minimal` for clean but capable SaaS settings
- `material` + `m3-pastel` for soft modern onboarding/configuration

## Starter Structure

```text
Header
Section Nav
Grouped Setting Sections
Save/Reset Region
```
