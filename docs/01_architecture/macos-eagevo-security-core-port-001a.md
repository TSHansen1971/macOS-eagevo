# macOS-eagevo Security Core-port 001A

## Formål

Dette dokumentet porter Security Core-prinsipper fra OS eagevo inn i macOS-eagevo som konsept og kontrakt. Porten er ikke enforcement og innfører ingen produktkode.

## Prinsipper

Security Core for macOS-eagevo skal bygge på følgende prinsipper:

- informasjonsobjekter må klassifiseres og semantisk plasseres
- aktører må være eksplisitte systemobjekter
- klarering er separat fra autorisasjon
- klarering gir ikke tilgang
- klassifikasjon gir ikke tilgang
- autorisasjon er tilgangsbeslutningen
- default authorization er deny
- personvern er en parallell styringsakse
- compliance er en maskinlesbar krav-, mapping- og evidensmodell

## macOS-spesifikk port

Security Core skal ikke portere Debian-filbaner eller Linux-antakelser ukritisk til macOS. macOS-eagevo må ha egne kontrakter for macOS-filer, app-bundles, launchd, sandbox, TCC, local user context og Apple-plattformspesifikke kontrollflater.

## Konseptobjekter

Security Core-porten skal kunne modellere:

- aktør
- rolle
- klarering
- autorisasjon
- informasjonsobjekt
- klassifikasjon
- beskyttelsesbehov
- personvernprofil
- sikkerhetskrav
- tiltak
- kontrollresultat
- evidensreferanse
- audit-hendelse

## Avgrensning

Dette steget etablerer begreps- og kontraktsgrunnlag. Det innfører ingen policy enforcement, ingen tilgangskontrollmotor og ingen runtime-integrasjon.
