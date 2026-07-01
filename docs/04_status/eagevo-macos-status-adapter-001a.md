# EAGEVO-MACOS-STATUS-ADAPTER-001A

## Formål

Oppdatere `eagevo-status` slik at statusaggregatoren viser samme operative kontrollflate som control-plane-index etter at macOS-adapteren er innlemmet.

## Endring

`eagevo-status` får egne seksjoner for:

- control-plane-index
- macos-adapter

## Verifisering

Statusaggregatoren kontrollerer:

- control-plane-index finnes på begge installerte stier
- control-plane-index har paritet mellom `/usr/local/lib/eagevo` og `/Library/Eagevo`
- control-plane-index har minst 6 komponenter
- `eagevo-control-plane` er kjørbar
- macOS-adapterens kontrakt, CLI og evidensfiler finnes
- adapter-evidens har paritet mellom installerte stier
- `eagevo-macos-adapter verify` er grønn
- audit-kjeden er grønn
- ingen Eagevo LaunchDaemon eller LaunchAgent finnes

## Sikkerhetsgrense

Dette er en read-only statusaggregatoroppdatering. Den aktiverer ikke LaunchDaemon, LaunchAgent, enforcement, MDM, AI-runtime, agent-autonomi, agent tool execution, automatisk innsamling eller ekstern logging.

## Audit

Steget legger inn én eksplisitt audit-hendelse for at statusaggregatoren er oppdatert til å vise adapter og control-plane-index eksplisitt.
