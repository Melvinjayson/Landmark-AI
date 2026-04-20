# Documentation Index

## Start here

1. [Repository structure](architecture/repository-structure.md)
2. [Security threat model](security/threat-model.md)
3. [Secrets and key management policy](security/secrets-policy.md)
4. [Architecture Decision Records](adr/)
5. [OpenAPI contract](../specs/openapi.yaml)

## Audience map

- **Product and leadership**: ADRs + workflows
- **Backend engineers**: OpenAPI + architecture docs + security controls
- **Frontend engineers**: design system + API examples
- **Platform engineers**: security policy + CI quality gates

## Contribution rules

- Every cross-domain change updates an ADR or references an existing one.
- Any API shape change must modify `specs/openapi.yaml` and include compatibility notes.
- Any data handling change touching PII or consent updates docs in `docs/security/`.
