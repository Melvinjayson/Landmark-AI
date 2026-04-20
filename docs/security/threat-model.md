# Threat Model (MVP Baseline)

## Scope

- API gateway, vault service, document processing pipeline, trust score service.
- PII-bearing flows: owner identity references, consent records, document metadata.

## Primary assets

- Vault ownership records
- Consent artifacts and timestamps
- Document extraction outputs
- Trust score factor payloads

## Top risks and controls

1. **Unauthorized data access**
   - Control: JWT auth at gateway + role scopes.
   - Control: least-privilege service credentials.
2. **PII leakage in logs**
   - Control: strict redaction middleware for identifiers and document references.
3. **Tampered trust score responses**
   - Control: signed audit events and immutable recompute records.
4. **Replay / duplicate submission attacks**
   - Control: idempotency keys for POST operations.
5. **Supply-chain compromise**
   - Control: CI dependency scanning + pinned lockfiles.

## Abuse scenarios to test continuously

- High-volume invalid payload flooding on `/documents`.
- Cross-tenant object reference attempts on `/vaults/{vaultId}`.
- Unauthorized trust score recompute attempts.
