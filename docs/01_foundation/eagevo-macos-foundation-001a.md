# EAGEVO-MACOS-FOUNDATION-001A

## Formål

Etablere første contract-only Eagevo foundation på macOS.

## Avgrensning

Steget etablerer lokal katalogstruktur, maskinlesbar foundation-kontrakt og to lokale statuskommandoer.

Steget aktiverer ikke enforcement, LaunchDaemon, LaunchAgent, MDM, AI-runtime, agent-autonomi, agent tool execution, ekstern logging eller offensive sikkerhetsverktøy.

## macOS-rolle

macOS utfører.

Eagevo klassifiserer, vurderer, dokumenterer, auditerer og styrer.

## Installerte systemstier

- `/Library/Eagevo`
- `/Library/Application Support/Eagevo`
- `/Library/Logs/Eagevo`
- `/usr/local/lib/eagevo`
- `/usr/local/bin/eagevo-status`
- `/usr/local/bin/eagevo-baseline`

## Verifikasjon

- `eagevo-status`
- `eagevo-baseline verify`

Forventet resultat er `overall: GREEN`.
