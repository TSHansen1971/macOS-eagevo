# EAGEVO-MACOS-CONTROL-PLANE-INDEX-001A

## Formål

Etablere første samlede control-plane-indeks for macOS-eagevo.

## Modell

Indeksen dokumenterer eksisterende kontrollplan-komponenter:

- foundation
- audit-core
- status-core
- baseline-manifest
- control-plane-index

## Installerte stier

- `/usr/local/lib/eagevo/control-plane-index.json`
- `/Library/Eagevo/control-plane-index.json`
- `/usr/local/bin/eagevo-control-plane`

## CLI

- `eagevo-control-plane status`
- `eagevo-control-plane verify`
- `eagevo-control-plane index`

## Audit

Steget legger inn én eksplisitt audit-hendelse med type `control_plane_index.initialized`.

## Sikkerhetsgrense

Control-plane-index er dokumenterende og verifiserende. Den aktiverer ikke LaunchDaemon, LaunchAgent, enforcement, AI-runtime, agent-autonomi, agent tool execution, automatisk innsamling, MDM eller ekstern logging.
