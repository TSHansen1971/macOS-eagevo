# macOS-eagevo Approval Package Contract 001A

## Formål

Dette steget etablerer første maskinlesbare kontrakt for macOS-eagevo som Approval Evidence Package Engine.

Kontrakten er beslutningsstøtte. Den er ikke godkjenning, sertifisering eller enforcement.

## Opprettede kontrakter

- `schemas/approval/eagevo-approval-evidence-package.schema.json`
- `schemas/approval/eagevo-approval-decision-record.schema.json`
- `schemas/approval/eagevo-change-assessment.schema.json`
- `schemas/approval/eagevo-temporary-use-permit.schema.json`

## Eksempel

- `examples/approval/first-approval-package.example.json`

Eksempelet er strukturelt og gjør ingen reell godkjenningspåstand.

## Pakketyper

Hovedskjemaet modellerer disse pakkene:

- `first_approval_package`
- `reapproval_package`
- `significant_change_package`
- `minor_change_record`
- `temporary_use_permit_package`
- `system_owner_risk_acceptance_record`

## Beslutningsskille

`approval_decision` kan være `null` eller et separat beslutningsobjekt. Feltet skal ikke autogenereres som godkjenning. Godkjenning krever eksplisitt systemeierbeslutning.

## Security Core-prinsipper i kontrakten

Kontrakten viderefører disse prinsippene:

- klassifikasjon gir ikke tilgang
- klarering gir ikke tilgang
- autorisasjon er tilgangsbeslutningen
- default authorization er `deny`
- personvern er en parallell styringsakse
- evidens og auditspor er eksplisitte objekter

## Avgrensning

Dette er contract/model-only.

Ingen produktkode, installerte systemfiler, audit append, baseline-manifest-oppdatering, control-plane-index-oppdatering, LaunchDaemon, LaunchAgent, enforcement, MDM, AI-runtime, modellnedlasting eller runtime-integrasjon er innført.
