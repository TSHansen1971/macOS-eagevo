# EAGEVO-MACOS-AUDIT-CORE-001A

## Formål

Etablere første audit-core for macOS-eagevo.

Audit-core skal gi en lokal, manuell og append-only auditkjede med verifiserbar hash-kjede.

## Avgrensning

Dette steget aktiverer ikke automatisk innsamling, enforcement, LaunchDaemon, LaunchAgent, MDM, AI-runtime, agent-autonomi, agent tool execution, ekstern logging eller offensive sikkerhetsverktøy.

## Modell

Audit-core består av:

- `/usr/local/bin/eagevo-audit`
- `/usr/local/lib/eagevo/audit/audit-core-contract.json`
- `/Library/Eagevo/audit/audit-head.json`
- `/Library/Logs/Eagevo/audit/audit-events.jsonl`

Auditloggen er JSONL. Hver hendelse inneholder forrige hash og egen hash. `eagevo-audit verify` verifiserer sekvens, hash-kjede og head-state.

## Bruk

- `eagevo-audit status`
- `eagevo-audit verify`
- `sudo eagevo-audit append --type <type> --message <message> --payload '{}'`

## Sikkerhetsgrense

Audit-core er dokumenterende og verifiserende. Den håndhever ikke policy og endrer ikke macOS-beskyttelser.
