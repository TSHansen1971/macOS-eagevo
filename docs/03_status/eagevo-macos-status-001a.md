# EAGEVO-MACOS-STATUS-001A

## Formål

Etablere første read-only status-aggregator for macOS-eagevo.

## Modell

`eagevo-status` samler status for:

- foundation
- audit-core
- status-core-kontrakt
- launchd-sikkerhetsgrense

## Avgrensning

Status-core leser og verifiserer. Den skriver ikke audit-hendelser, aktiverer ikke automatisk innsamling, installerer ikke LaunchDaemon eller LaunchAgent, håndhever ikke policy, starter ikke AI-runtime og utfører ikke agenthandlinger.

## Verifikasjon

- `eagevo-status`
- `eagevo-baseline verify`
- `eagevo-audit verify`

Forventet resultat er `overall: GREEN` og `audit_verify: GREEN`.
