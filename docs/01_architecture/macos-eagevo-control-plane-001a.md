# macOS-eagevo Control Plane 001A

## Kontrollplanets rolle

macOS-eagevo skal fungere som et read-only eller eksplisitt styrt kontrollplan over macOS-baserte arbeidsflater og systemkomponenter. macOS utfører tekniske operasjoner. macOS-eagevo samler, klassifiserer, vurderer, dokumenterer og gjør kontrollstatus etterprøvbar.

## Arkitekturprinsipp

Kontrollplanet skal ikke ukritisk bli en enforcement-mekanisme. Før enforcement eventuelt vurderes i senere steg, skal prosjektet ha eksplisitte kontrakter for informasjonsobjekter, aktører, klassifikasjon, autorisasjon, evidens, audit og beslutningsansvar.

## Kontrollplanstatus

Kontrollplanstatus kan beskrive om komponenter, kontrakter, evidens og auditkjede fremstår konsistente. Den kan ikke beskrive at systemet er godkjent.

## Lokale kontrollflater

macOS-eagevo kan senere lese eller produsere lokal evidens om:

- systemidentitet
- komponentstatus
- baseline-manifest
- adaptere
- audit chain
- kontrolltester
- dokumenterte avvik
- endringsvurderinger
- godkjenningspakker

Dette konseptsteget endrer ingen slike systemflater.
