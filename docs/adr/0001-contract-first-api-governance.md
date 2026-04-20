# ADR 0001: Contract-First API Governance

- **Status**: Accepted
- **Date**: 2026-04-20

## Context

Multiple teams (web, mobile, backend, workers) need parallel delivery with minimal integration churn.

## Decision

Use `specs/openapi.yaml` as source-of-truth for API contracts. Contract breaking changes require:

1. version bump policy update,
2. migration notes,
3. CI-based detection and explicit approval.

## Consequences

- Faster parallel development through stable contracts.
- Slightly higher process overhead for endpoint evolution.
