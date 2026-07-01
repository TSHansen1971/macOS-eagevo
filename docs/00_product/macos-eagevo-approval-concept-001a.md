# macOS-eagevo godkjenningskonsept 001A

## Premiss

Godkjenning av et informasjonssystem skal forstås som en planlagt, systematisk, risikobasert og forholdsmessig vurdering. macOS-eagevo skal støtte denne vurderingen ved å produsere strukturert, etterprøvbar og maskinlesbar dokumentasjon for systemeiers beslutning.

Dette dokumentet gjengir ikke et juridisk vurderingsnotat som kildeartefakt. Kildehåndtering for juridiske føringer må avklares eksplisitt før slike dokumenter legges inn i repoet.

## Godkjenningsansvar

Systemeier har ansvar for å forstå systemets formål, informasjonsverdier, beskyttelsesbehov, risiko, tiltak, kontrollresultater og restrisiko. macOS-eagevo kan dokumentere og strukturere grunnlaget, men kan ikke overta beslutningsansvaret.

## Beslutningspunkt

En godkjenningsprosess skal ha et eksplisitt beslutningspunkt. Beslutningen må som minimum angi:

- hvilket informasjonssystem beslutningen gjelder
- hvilket omfang beslutningen dekker
- hvilke informasjonsverdier og beskyttelsesbehov som inngår
- hvilke vesentlige forutsetninger og begrensninger som gjelder
- hvilken restrisiko systemeier aksepterer
- gyldighetsperiode eller utløsere for regodkjenning
- hvem som fatter beslutningen

## Ikke-automatisk godkjenning

macOS-eagevo skal ikke konvertere grønn teknisk status til godkjenning. En grønn kontrollstatus kan være evidens i en godkjenningspakke, men er ikke beslutningen.

## Beslutningsspråk

macOS-eagevo bør bruke presise statusbegreper som skiller mellom teknisk tilstand og beslutning:

- `control_status_green`
- `evidence_package_complete`
- `risk_assessment_complete`
- `residual_risk_documented`
- `owner_decision_required`
- `approved_by_system_owner`
- `not_approved`
- `temporary_use_not_recommended`
- `not_allowed_without_security_fix`
