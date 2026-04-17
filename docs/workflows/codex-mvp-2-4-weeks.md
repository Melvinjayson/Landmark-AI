# Codex-Guided MVP Workflow (2–4 Weeks)

## Objective

Ship a credible MVP for LandMark AI with:

- Vault creation + retrieval
- Document ingestion + extraction status
- Trust score compute + explanation
- Basic operational dashboard UI

## Execution model

- **Cadence**: 4 weekly phases (can compress into 2 intense sprints).
- **Method**: contract-first + vertical slices + hardening gates.
- **Definition of done**: deployed staging environment with test coverage and runbooks.

## Phase plan

### Week 1 — Foundation + Contracts

**Outputs**
- Monorepo scaffold, CI checks, environment templates
- OpenAPI draft approved by backend + frontend
- Postgres schema and first migrations

**Workstreams**
- Platform: CI/CD basics, lint/test/typecheck gates
- Backend: gateway service bootstrap (FastAPI, auth middleware, health)
- Frontend: app shell + auth guard + navigation layout
- Data: vault/document/trust tables (with audit fields)

**Exit criteria**
- PR checks passing
- `/health` live in dev/staging
- Contract mock server available

### Week 2 — Core Vertical Slices

**Outputs**
- Create/get vault endpoints
- Register/get document endpoints with queue job handoff
- Dashboard showing vault list + document status

**Workstreams**
- Backend: service layer + validation + idempotency support
- Workers: async ingestion pipeline skeleton and retry policy
- Frontend: forms, list/detail views, state management
- QA: integration tests for status codes and invalid input

**Exit criteria**
- End-to-end flow from vault creation to document queueing
- Functional demo script with seeded data

### Week 3 — Trust Score + Explainability

**Outputs**
- Trust score recompute endpoint and retrieval endpoint
- Scoring factors and confidence payload
- UI trust score panel + factor drill-down

**Workstreams**
- AI/Rules: deterministic scoring rubric (v1)
- Backend: async recompute orchestration + persistence
- Frontend: trust visualization and error handling
- Observability: structured logs, request IDs, dashboard metrics

**Exit criteria**
- Score recomputation works via API and UI
- Explainability payload visible and test-covered

### Week 4 — Hardening + Release Readiness

**Outputs**
- Security review (PII handling, hashing, consent traces)
- Performance tuning and error budget baseline
- MVP release checklist and rollback plan

**Workstreams**
- Security: secrets policy, PII redaction, audit-log checks
- Reliability: load smoke tests, retry/backoff tuning
- Product: acceptance tests and UX polish
- Ops: runbooks, alerts, staging signoff

**Exit criteria**
- Staging release tagged
- Incident/runbook docs complete
- MVP launch go/no-go decision doc approved

## Backlog structure

## Epic 1: Vault Management

- Story: create vault with consent and parcel metadata
- Story: fetch vault by ID
- Story: list vaults by filters (status/date/agent)

## Epic 2: Document Intelligence

- Story: register encrypted document metadata
- Story: monitor extraction progress
- Story: human review handoff for low confidence

## Epic 3: Trust Score

- Story: trigger recomputation
- Story: retrieve score + risk factors
- Story: render explainability in dashboard

## Epic 4: Platform & Governance

- Story: immutable access logs
- Story: consent record retrieval
- Story: export and soft-delete workflows

## Quality gates per PR

1. Contract updated (if API changed).
2. Unit tests added for business logic changes.
3. Integration tests for new endpoints.
4. Logging + error paths verified.
5. Security implications documented.

## Suggested daily operating loop

1. Generate/refresh plan from accepted stories.
2. Implement one vertical slice (API + service + tests + UI).
3. Run checks locally before PR.
4. Review telemetry and bug reports.
5. Re-plan next day based on blocked risks.
