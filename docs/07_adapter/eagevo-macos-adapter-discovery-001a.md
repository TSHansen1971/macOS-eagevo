# EAGEVO-MACOS-ADAPTER-DISCOVERY-001A

## Formål

Etablere første read-only macOS-adapter for macOS-eagevo.

## Modell

Adapteren leser et begrenset sett macOS-kilder og skriver strukturert Eagevo-evidens.

## Kilder

- `sw_vers`
- `uname -a`
- `hostname`
- `id`
- `csrutil status`
- `spctl --status`
- `fdesetup status`
- `launchctl list` som telling

## Installerte stier

- `/usr/local/bin/eagevo-macos-adapter`
- `/usr/local/lib/eagevo/macos-adapter/adapter-contract.json`
- `/usr/local/lib/eagevo/macos-adapter-discovery.json`
- `/Library/Eagevo/evidence/macos-discovery.json`

## CLI

- `eagevo-macos-adapter discover`
- `sudo eagevo-macos-adapter discover --write`
- `eagevo-macos-adapter status`
- `eagevo-macos-adapter verify`
- `eagevo-macos-adapter evidence`

## Sikkerhetsgrense

Adapteren er read-only mot macOS-kilder. Den endrer ikke macOS-konfigurasjon, aktiverer ikke LaunchDaemon, LaunchAgent, enforcement, MDM, AI-runtime, agent-autonomi, agent tool execution, automatisk innsamling eller ekstern logging.
