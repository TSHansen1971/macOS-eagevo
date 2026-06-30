# EAGEVO-MACOS-BASELINE-MANIFEST-001A

## Formål

Etablere første samlede baseline-manifest for macOS-eagevo.

## Modell

Baseline-manifestet dokumenterer:

- repo-head
- macOS-versjon og build
- foundation-kontrakt
- audit-core-kontrakt
- status-core-kontrakt
- installerte Eagevo-kommandoer
- audit-head
- sikkerhetsgrense

## Installerte manifeststier

- `/usr/local/lib/eagevo/baseline-manifest.json`
- `/Library/Eagevo/baseline-manifest.json`

## Audit

Steget legger inn én eksplisitt audit-hendelse med type `baseline_manifest.initialized`.

## Sikkerhetsgrense

Baseline-manifestet er dokumenterende. Det aktiverer ikke LaunchDaemon, LaunchAgent, enforcement, AI-runtime, agent-autonomi, agent tool execution, automatisk innsamling, MDM eller ekstern logging.
