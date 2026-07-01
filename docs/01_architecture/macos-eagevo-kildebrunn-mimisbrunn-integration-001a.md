# macOS-eagevo rollemodell for Kildebrunn, Mimisbrunn, OS eagevo og macOS-eagevo 001A

## Rollemodell

Prosjektene skal forstås med følgende ansvarsdeling:

- Kildebrunn forsyner.
- Mimisbrunn bruker.
- macOS-eagevo kontrollerer.
- OS eagevo formaliserer dyp arkitektur.

## Kildebrunn

Kildebrunn er kilde- og forsyningsledd for kuraterte modeller, artefakter eller kildepakker. Kildebrunns rolle er ikke å godkjenne systembruk.

## Mimisbrunn

Mimisbrunn er lokal applikasjonsbruker av kuraterte lokale modeller og kilder. Mimisbrunn kan være et system eller en komponent som senere inngår i en godkjenningspakke, men Mimisbrunns runtime integreres ikke i dette steget.

## macOS-eagevo

macOS-eagevo kontrollerer, dokumenterer, klassifiserer, vurderer og produserer godkjenningsstøttende evidenspakker for macOS-baserte miljøer.

## OS eagevo

OS eagevo formaliserer dypere arkitektur, Security Core-prinsipper og systemmodeller. macOS-eagevo kan portere prinsipper og kontrakter, men skal ikke kopiere OS- eller Debian-spesifikke implementasjonsdetaljer ukritisk.

## Avgrensning

Dette dokumentet etablerer rollemodell og konseptuell integrasjonsflate. Det innfører ingen Kildebrunn-runtime, Mimisbrunn-runtime, AI-runtime eller modellnedlasting.
