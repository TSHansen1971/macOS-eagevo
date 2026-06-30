# macOS-eagevo 001 - Project Scope

## Formål

macOS-eagevo er en parallell port av Eagevo-modellen til macOS som lokalt kontrollplan, ikke som ny macOS-distribusjon.

## Arkitektur

macOS leverer teknisk plattform:

- kernel
- brukere
- filsystem
- launchd
- TCC
- Gatekeeper
- FileVault
- SIP
- sandbox
- appsignering
- rettigheter
- prosesser
- nettverk

Eagevo leverer kontrollplan:

- classification
- actor
- clearance
- authorization
- privacy
- compliance
- audit
- baseline
- policy
- evidence
- status

## Sikkerhetsgrenser i foundation

- Ingen AI-modell installeres.
- Ingen lokal AI-runtime aktiveres.
- Ingen ekstern AI-API konfigureres.
- Ingen agent-autonomi aktiveres.
- Ingen agent tool execution aktiveres.
- Ingen exploit framework installeres.
- Ingen offensive sikkerhetsverktøy installeres.
- Ingen ekstern logging aktiveres.
- Ingen data sendes ut av macOS-VM-en.
- Ingen MDM-profil installeres.
- Ingen LaunchDaemon eller LaunchAgent aktiveres.
- Ingen enforcement aktiveres.
- Security-core er contract-only.
- Audit-core er append-only og verifiserbar, ikke enforcement.
