# macOS-eagevo Approval Package Validator 001A

Byggesteg: `EAGEVO-MACOS-APPROVAL-PACKAGE-VALIDATOR-001A`

## Formål

Dette byggesteget etablerer første repo-lokale validator for Approval Evidence Package-kontrakten i macOS-eagevo.

Validatoren gjør kontrakten operasjonell ved å kontrollere at en Approval Evidence Package har nødvendig struktur, lovlige kontraktsverdier og sentrale Security Core-prinsipper.

## Produktavgrensning

macOS-eagevo er Eagevo Control Plane for macOS.

macOS utfører. Eagevo klassifiserer, vurderer, dokumenterer, auditerer og styrer.

Validatoren er en del av prosjektets Approval Evidence Package Engine. Den produserer teknisk valideringsgrunnlag, men den godkjenner ikke systemer.

## Validator

Fil:

`tools/approval/validate_approval_package.py`

Kjøring:

    python3 tools/approval/validate_approval_package.py examples/approval/first-approval-package.example.json

Forventet positivt resultat:

    validation: GREEN

Ved kontrollert feil skal validatoren skrive:

    validation: RED

og returnere non-zero exit code.

## Implementasjonsprinsipper

Validatoren bruker kun Python standardbibliotek.

Den krever ikke jsonschema, pip, Homebrew, nettverk, installasjon i `/usr/local/bin`, installasjon i `/usr/local/lib/eagevo`, LaunchDaemon, LaunchAgent eller AI-runtime.

## Kontrakter som leses

Validatoren leser følgende repo-lokale kontrakter:

- `schemas/approval/eagevo-approval-evidence-package.schema.json`
- `schemas/approval/eagevo-approval-decision-record.schema.json`
- `schemas/approval/eagevo-change-assessment.schema.json`
- `schemas/approval/eagevo-temporary-use-permit.schema.json`

Validatoren er ikke en full JSON Schema-motor. Den utfører avgrenset stdlib-basert kontraktsvalidering og eksplisitte macOS-eagevo-kontroller.

## Kontroller

Validatoren kontrollerer JSON-syntaks, kontraktens required-felter, `schema_version = "0.1"`, lovlig `package_type`, lovlig `package_status`, struktur for `approval_decision`, at eksempelpakken ikke hevder godkjenning, at `owner_decision_required` ikke kombineres med akseptert restrisiko, sentrale Security Core-prinsipper, at `information_values` ikke er tom, og at `evidence_references[*].sha256`, når satt, er 64 hex-tegn.

## Sikkerhetsmessig betydning

Validatoren beskytter et sentralt skille i produktstrategien: teknisk kontrollstatus er ikke godkjenning.

En komplett Approval Evidence Package er beslutningsgrunnlag for systemeier. Den er ikke i seg selv en godkjenningsbeslutning.

Systemeiers eksplisitte beslutning må fremgå av en strukturert beslutningspost.
