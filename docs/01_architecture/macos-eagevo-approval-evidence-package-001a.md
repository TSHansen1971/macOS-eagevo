# macOS-eagevo Approval Evidence Package 001A

## Formål

Approval Evidence Package er macOS-eagevo sin strukturerte modell for beslutningsgrunnlag. En pakke skal samle systemomfang, informasjonsverdier, klassifikasjon, personvern, aktørmodell, autorisasjonsmodell, sikkerhetskrav, tiltak, kontrollresultater, risikovurdering, restrisiko, evidens og auditspor.

## Pakketyper

macOS-eagevo skal minimum kunne beskrive følgende pakker:

- First Approval Package
- Reapproval Package
- Significant Change Package
- Minor Change Record
- Temporary Use Permit Package
- System Owner Risk Acceptance Record

## Felles felter

Hver pakke bør kunne beskrive:

- `system_scope`
- `system_owner`
- `information_values`
- `classification_profile`
- `privacy_profile`
- `actor_model`
- `clearance_model`
- `authorization_model`
- `security_requirements`
- `implemented_measures`
- `control_test_results`
- `risk_assessment`
- `residual_risk`
- `evidence_references`
- `change_assessment`
- `approval_decision`
- `validity_period`
- `limitations`
- `audit_trail`

## Beslutningsfelt

`approval_decision` skal ikke autogenereres som godkjenning. Feltet skal enten være tomt, markert som beslutning kreves, eller vise eksplisitt registrert beslutning fra systemeier.

## Maskinlesbarhet

Pakkemodellen bør senere få JSON Schema eller tilsvarende maskinlesbar kontrakt. Dette steget etablerer bare dokumentert konsept.
