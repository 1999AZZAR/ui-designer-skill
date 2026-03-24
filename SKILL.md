---
name: ui-designer
description: Choose the best UI design system, or a deliberate combination of systems, for web or app interfaces. Use for dashboards, admin panels, internal tools, CMS, SaaS, websites, component theming, color systems, and frontend visual direction across Ant Design, Fluent, Carbon, Atlassian, Apple HIG, Material You, Polaris, Minimalism, Glassmorphism, Neo-Brutalism, Swiss, and related systems.
---

# UI Designer Skill

Use this skill when the user needs interface direction, design-system selection, theming, or visual/product UX structure before or during implementation.

## Operating Rules

- Choose systems from product context first, not visual mood first.
- Choose the best system for the job. Use a combination only when there is a clear reason and the roles of each system are explicit.
- Prefer predictable, reusable patterns over novelty when the product is operational or workflow-heavy.
- Avoid generic AI aesthetics: no default purple/indigo gradients, no glossy filler, no emoji in functional UI.
- Use Font Awesome 6 when the project needs a general icon set.

## Decision Flow

1. Classify the product.
- Enterprise/admin/internal/CMS/dashboard/data-heavy: prefer `ant`, `carbon`, or `atlassian`.
- Windows/Microsoft-like enterprise: prefer `fluent`.
- Apple platform-native feel: prefer `apple-hig`.
- Android or modern adaptive UI: prefer `material`.
- Commerce and merchant tooling: prefer `polaris`.
- Content, editorial, portfolio, typography-led: prefer `minimal` or `swiss`.
- Expressive or experimental branding: prefer `neo-brutalism`, `glass`, `claymorphism`, `skeuomorphism`, or `neo-m3`.

2. Check complexity.
- If the product is form-heavy, multi-role, repeat-use, or operational, score `ant`, `carbon`, and `atlassian` first.
- If clarity and data density matter more than brand distinctiveness, score `ant` or `carbon` higher.
- If strong brand expression is central, score expressive systems higher and avoid flattening the product into enterprise-safe UI.

3. Decide single system vs hybrid.
- Choose a single system when one design language can handle both behavior and visual tone cleanly.
- Choose a hybrid only when the product clearly needs one system for structure and another for brand expression.
- For hybrids, define the split explicitly.
  - Example: `ant` for layout, forms, tables, and feedback.
  - Example: `neo-m3` or `glass` for hero, marketing surface, or brand accents.
- Do not create arbitrary mashups. Mixed systems must still feel coherent.

4. Use the map.
- Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md) as the main map for fast system selection.
- Then open only the relevant file in `references/`.

## Selection Standard

Choose the system that best fits:
- product type
- task density
- platform expectation
- brand intensity
- implementation consistency
- long-term scalability

If a hybrid is better than a single system, state why and define which system owns:
- layout and spacing
- components and interaction behavior
- visual language and brand accents

## Ant Design Evaluation

When Ant is a candidate, evaluate it as a behavior system, not just a look.

Check:
- `Natural`: is the flow obvious and low-friction?
- `Certain`: are hierarchy, spacing, states, and behavior consistent?
- `Meaningful`: does each control support the task flow?
- `Growing`: will the structure hold as features, data, and roles expand?

If Ant wins, use it for:
- workflow scaffolding
- forms and tables
- status and feedback patterns
- dense but readable operational UI

## Workflow

1. Identify the product type, platform, and UX density.
2. Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md) as the map.
3. Choose the best single system or deliberate hybrid.
4. Open only the matching reference file or files.
5. Define color direction, typography direction, spacing behavior, and component style.
6. Translate the chosen system into page structure and component rules.
7. If needed, run the automation script to append design rules.

## Automation

Use `scripts/apply_ui_rules.py` when the project needs persistent `.cursorrules` guidance.

```bash
python3 scripts/apply_ui_rules.py --style [fluent|ant|carbon|atlassian|apple-hig|polaris|material|minimal|glass|neumorphism|neo-brutalism|claymorphism|skeuomorphism|swiss|m3-pastel|neo-m3] --palette [pastel|dark|vibrant|mono]
```

## References

- Main map: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- System details: `references/ant-design.md`, `references/carbon-design.md`, `references/fluent-design.md`, `references/atlassian-design.md`, `references/apple-hig.md`, `references/material-you.md`, `references/shopify-polaris.md`, `references/minimalism.md`, `references/swiss-design.md`, `references/neo-brutalism.md`, `references/glassmorphism.md`, `references/claymorphism.md`, `references/skeuomorphism.md`, `references/neo-m3-hybrid.md`, `references/m3-pastel-glass.md`
