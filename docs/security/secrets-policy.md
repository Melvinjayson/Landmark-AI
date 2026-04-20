# Secrets and Key Management Policy

## Principles

- No plaintext secrets in code, commits, or CI logs.
- Environment-specific secret stores only (dev/staging/prod separation).
- Rotation and revocation procedures must be testable and documented.

## Required controls

- CI workflows load credentials through ephemeral OIDC/session tokens whenever possible.
- Application secrets are injected at runtime only.
- Key rotation interval: 90 days maximum for non-ephemeral credentials.
- Access to production secrets requires break-glass audit logging.

## Repository constraints

- `.env` files are never committed.
- Example configuration must use placeholder values.
- New third-party integrations require secret owner + rotation owner in PR description.
