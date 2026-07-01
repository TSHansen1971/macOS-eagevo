# EAGEVO-MACOS-CONTROL-PLANE-INDEX-ADAPTER-001A

## Formål

Innlemme den etablerte read-only macOS-adapteren i macOS-eagevo control-plane-index.

## Endring

Control-plane-index utvides fra 5 til 6 komponenter:

1. foundation
2. audit-core
3. status-core
4. baseline-manifest
5. control-plane-index
6. macos-adapter-discovery

## Adapterkomponent

Adapterkomponenten peker på:

- /usr/local/bin/eagevo-macos-adapter
- /usr/local/lib/eagevo/macos-adapter/adapter-contract.json
- /usr/local/lib/eagevo/macos-adapter-discovery.json
- /Library/Eagevo/evidence/macos-discovery.json

## Sikkerhetsgrense

Dette er en read-only index-/kontrollplanoppdatering. Den aktiverer ikke LaunchDaemon, LaunchAgent, enforcement, MDM, AI-runtime, agent-autonomi, agent tool execution, automatisk innsamling eller ekstern logging.

## Audit

Steget legger inn én eksplisitt audit-hendelse for at adapteren er indeksert i kontrollplanet.
