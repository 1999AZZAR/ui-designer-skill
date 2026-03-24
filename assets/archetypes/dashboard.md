# Dashboard Archetype

Use for operational overviews, KPIs, status summaries, and multi-widget product home screens.

## Best System Fits

- `ant`
- `carbon`
- `fluent`
- `m3-pastel`
- `glass` as a supporting accent layer only

## Core Regions

- page header with title, context, and primary action
- KPI strip with 3 to 6 key metrics
- filter or time-range controls
- primary chart/table region
- secondary widgets for alerts, tasks, or recent activity

## Behavior Rules

- Keep the first screen scannable in under 5 seconds
- Prioritize one primary insight, not equal-weight widgets everywhere
- Use cards only when they create grouping clarity
- Handle empty, loading, error, and stale-data states explicitly

## Good Hybrids

- `ant` + `glass` for product dashboards with stronger atmosphere
- `carbon` + `minimal` for analytical dashboards with calmer outer framing

## Starter Structure

```text
Header
KPI Row
Filter/Time Controls
Primary Data Region
Secondary Widgets
```
