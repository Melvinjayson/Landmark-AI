# ADR 0002: PII Redaction and Auditability Baseline

- **Status**: Accepted
- **Date**: 2026-04-20

## Context

Landmark-AI processes personally identifiable information and trust-sensitive records.

## Decision

Adopt mandatory PII redaction in structured logs and persist immutable audit events for all trust score recompute requests.

## Consequences

- Lower compliance and breach risk.
- Additional implementation and observability cost.
