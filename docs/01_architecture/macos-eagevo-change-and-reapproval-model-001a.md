# macOS-eagevo endrings- og regodkjenningsmodell 001A

## Formål

macOS-eagevo skal kunne støtte dokumenterbar vurdering av endringer og behov for regodkjenning. Endringsmodellen skal være konservativ der sikkerhetsrelevans er uklar.

## Endringsklasser

macOS-eagevo skal kunne klassifisere endringer som:

- `no_security_relevance`
- `minor_change`
- `significant_change`
- `requires_reapproval`
- `requires_new_approval`
- `temporary_use_candidate`
- `not_allowed_without_security_fix`

## Vurderingsgrunnlag

Endringsvurderingen bør se på:

- endret systemomfang
- nye eller endrede informasjonsverdier
- endret klassifikasjonsprofil
- endret personvernprofil
- endret aktørmodell
- endret klarerings- eller autorisasjonsmodell
- endrede sikkerhetskrav
- svekkede eller nye tiltak
- nye kontrollresultater
- avvik
- auditspor
- påvirkning på tidligere restrisikoaksept

## Regodkjenning

Regodkjenning skal kreves når endringen påvirker forutsetningene for tidligere godkjenning på en sikkerhetsrelevant måte. macOS-eagevo skal dokumentere grunnlaget for anbefaling, men ikke fatte godkjenningsbeslutningen.

## Mindre endringer

Mindre endringer kan dokumenteres som `Minor Change Record` når de ikke endrer sikkerhetsforutsetningene vesentlig. Også mindre endringer skal ha sporbarhet.
