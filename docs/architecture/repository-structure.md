# LandMark AI Monorepo Structure (Production-Oriented)

## Goals

- Enable parallel delivery across backend, frontend, AI pipelines, and platform engineering.
- Keep high-cohesion domains grouped while preserving clear service ownership.
- Support MVP velocity now and regulated scale-up later.

## Canonical layout

```text
Landmark-AI/
├── apps/
│   ├── web/                         # React + TypeScript web app (operations, vault, CRM)
│   └── mobile/                      # React Native app (field agents, onboarding, approvals)
├── services/
│   ├── gateway/                     # FastAPI API gateway / BFF / auth boundary
│   ├── trust-score/                 # Trust Score engine service (rules + ML blending)
│   ├── document-ai/                 # OCR/NLP extraction + review workflows
│   ├── spatial/                     # GIS verification and anomaly checks
│   ├── identity/                    # NIN/BVN integrations + consent + hashing
│   ├── notifications/               # WhatsApp/email/SMS outbound + templates
│   └── orchestration/               # Multi-agent workflow coordinator
├── workers/
│   ├── ingestion-worker/            # Queue workers for document and identity jobs
│   ├── scoring-worker/              # Async trust score recomputation jobs
│   └── webhook-worker/              # External callback handling with retries
├── packages/
│   ├── ui/                          # Shared design system components/tokens
│   ├── config/                      # Shared lint, tsconfig, pytest, mypy configs
│   ├── types/                       # Shared API/domain types and schemas
│   └── observability/               # Logging, tracing, metrics setup libraries
├── specs/
│   ├── openapi.yaml                 # Contract-first API definition (source of truth)
│   └── events/                      # Async event contracts (JSON schema)
├── data/
│   ├── migrations/                  # Postgres/PostGIS migrations
│   └── seed/                        # Local/dev seed data
├── infra/
│   ├── terraform/
│   │   ├── modules/                 # Reusable AWS modules
│   │   ├── envs/dev/
│   │   ├── envs/staging/
│   │   └── envs/prod/
│   ├── ci/                          # CI/CD pipelines and policy checks
│   └── runbooks/                    # Incident and operational playbooks
├── docs/
│   ├── architecture/
│   ├── frontend/
│   ├── workflows/
│   └── adr/                         # Architecture decision records
├── scripts/                         # Automation tasks (scaffolding, checks, releases)
├── .github/workflows/               # GitHub Actions pipelines
└── README.md
```

## Service ownership boundaries

- `gateway`: auth, API aggregation, request validation, idempotency keys.
- `document-ai`: extraction pipeline, confidence scoring, human-review routing.
- `trust-score`: deterministic rules + ML inference + explainability bundle.
- `identity`: PII-safe verification adapters, hashed IDs, consent enforcement.
- `spatial`: parcel overlap checks, geofence validation, map-based risk signals.

## Dependency direction rules

1. `apps/*` depend on `packages/*` only (never on `services/*` internals).
2. `services/*` can depend on shared `packages/*` and `specs/*`, not on each other’s private modules.
3. Async inter-service communication must use versioned event contracts in `specs/events`.
4. API compatibility is governed by `specs/openapi.yaml` and contract tests in CI.

## Recommended build/test commands

```bash
# Type checks and lint across frontend packages
pnpm -r lint && pnpm -r typecheck

# Backend service tests
pytest services workers -q

# Contract validation
spectral lint specs/openapi.yaml
```
