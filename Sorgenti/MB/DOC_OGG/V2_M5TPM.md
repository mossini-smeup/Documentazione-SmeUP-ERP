# M5TPM     -  MODALITÀ PIANIFICAZIONE MULTIMAGAZZINO
Definisce le varie modalità con cui vieme eseguita la pianificazione materiali in una installazione multimagazzino.

## VALORI POSSIBILI

### ' ' CUMULATA
Le fonti di tutti i magazzini vengono trattate insieme : 
l'ordinamento è soltanto per data. I consigli di pianificazione vengono emessi sul primo magazzino nel gruppo fonti.

### '1' LANCIATA SINGOLARMENTE
Si esegue una pianificazione separata per magazzino :  il gruppo fonti deve contenere un solo magazzino (che è quello di
pianificazione). In questa modalità può essere attiva soltanto una pianificazione alla volta. Per ogni magazzino viene
comunque conservata l'ultima pianificazione eseguita.

### '2' COMPLETA
Si esegue nella stessa sessione la pianificazione per tutti i plant contenuti nel gruppo fonti. Se impostato nei dati di
pianificazione, vengono emessi suggerimenti di trasferimento dal plant di competenza, che è l'ultimo a venire elaborato,
e quindi è in grado di poter soddisfare, tra i suoi fabbisogni, i trasferimenti verso gli altri plant.
