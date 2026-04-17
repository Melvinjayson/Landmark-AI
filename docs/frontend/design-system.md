# LandMark AI Frontend Design System (v0)

## Principles

1. **Trust-first UI**: every screen should communicate confidence and auditability.
2. **Operational clarity**: legal/property workflows must be scannable under pressure.
3. **Accessible by default**: WCAG 2.2 AA baseline.
4. **Composable primitives**: design tokens and components shared across web/mobile.

## Technology baseline

- React + TypeScript (web), React Native + TypeScript (mobile)
- Tailwind CSS (web styling)
- Shared package: `packages/ui`
- State/data: React Query + Zustand
- Form handling: React Hook Form + Zod

## Token system

## Color tokens

- `--lm-bg`: `#0B1020`
- `--lm-surface`: `#121A2E`
- `--lm-surface-muted`: `#1A2440`
- `--lm-text-primary`: `#F6F8FF`
- `--lm-text-secondary`: `#A9B4D0`
- `--lm-accent`: `#3A86FF`
- `--lm-success`: `#2EC27E`
- `--lm-warning`: `#F5A524`
- `--lm-danger`: `#EF4444`

## Typography

- Font stack: `Inter, ui-sans-serif, system-ui`
- Sizes:
  - `display`: 36/44
  - `h1`: 30/38
  - `h2`: 24/32
  - `h3`: 20/28
  - `body`: 16/24
  - `caption`: 13/20

## Spacing scale

- `1`: 4px
- `2`: 8px
- `3`: 12px
- `4`: 16px
- `5`: 20px
- `6`: 24px
- `8`: 32px
- `10`: 40px
- `12`: 48px

## Radii and shadows

- Radius: `sm=6px`, `md=10px`, `lg=14px`, `xl=20px`
- Shadow:
  - `surface`: `0 4px 20px rgba(0, 0, 0, 0.18)`
  - `elevated`: `0 8px 32px rgba(0, 0, 0, 0.26)`

## Component inventory (MVP)

## Primitives

- `Button` (primary, secondary, ghost, danger)
- `Input`, `Textarea`, `Select`, `Checkbox`, `Radio`
- `Badge` (status-aware)
- `Card`
- `Modal`, `Drawer`
- `Tabs`
- `Table`
- `Tooltip`
- `Skeleton`

## Domain components

- `TrustScoreGauge` (0–100, with band labels)
- `RiskFactorList` (sortable factor rows)
- `DocumentStatusTimeline`
- `VerificationPill`
- `ConsentAuditPanel`
- `MapParcelPreview`

## State model UX standards

- **Loading**: skeletons for cards/tables + optimistic interaction only where safe.
- **Empty**: instructive empty states with primary CTA.
- **Error**: user-friendly message, retry action, tracking ID.
- **Partial failure**: preserve successful segments; annotate stale portions.

## Layout standards

- Page shell: left nav + header + context panel on desktop.
- Mobile-first cards for field ops.
- Max content width: `1280px`.
- 12-column responsive grid (web):
  - `sm`: 4 columns
  - `md`: 8 columns
  - `lg`: 12 columns

## Governance

- Component proposals require:
  1. UX rationale
  2. Accessibility checklist
  3. API spec (props/events)
  4. Usage examples (happy path + error state)
- Breaking changes in shared UI package require migration notes.
