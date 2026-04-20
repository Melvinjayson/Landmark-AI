# Landmark-AI

Production-ready monorepo foundation for the LandMark AI / Venus AI ecosystem.

## Why this repository exists

Landmark-AI is a contract-first platform for digitizing land/property verification workflows with explainable trust scoring. The repository is optimized for:

- **Regulated delivery**: clear consent trails, auditable events, and security policy docs.
- **Parallel execution**: backend, frontend, and platform teams can ship independently against shared contracts.
- **Risk-managed scale-up**: ADRs, CI quality gates, and operational runbooks are part of the baseline.

## Quickstart

```bash
# 1) Read the architecture + contracts
open docs/README.md

# 2) Validate API contract quality (when spectral is installed)
spectral lint specs/openapi.yaml

# 3) Inspect ADR decisions before making cross-cutting changes
ls docs/adr
```

## Documentation index

- Central docs index: `docs/README.md`
- Architecture boundaries: `docs/architecture/repository-structure.md`
- Security and governance: `docs/security/`
- Architecture Decision Records (ADRs): `docs/adr/`
- Frontend design system baseline: `docs/frontend/design-system.md`
- Delivery workflow guide: `docs/workflows/codex-mvp-2-4-weeks.md`

## Monorepo layout (scaffold)

```text
apps/
  web/
  mobile/
services/
  gateway/
  trust-score/
  document-ai/
  orchestration/
packages/
  ui/
  config/
  types/
infra/
  terraform/
  ci/
docs/
  architecture/
  frontend/
  security/
  workflows/
  adr/
specs/
```

## Contract-first governance

- `specs/openapi.yaml` is the source of truth for API compatibility.
- Breaking changes must be accompanied by migration notes and client impact analysis.
- Extensions under `x-landmark-*` encode lifecycle, ownership, and data classification metadata used by quality gates.
