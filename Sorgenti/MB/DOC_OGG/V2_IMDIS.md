# IMDIS     -  TIPO ESPLOSIONE DISTINTA
Definisce le modalità di scansione in implosione di una distinta base, a partire da un tipo distinta, da un assieme, e
da ulteriori condizionamenti (data, configurazione).

## VALORI POSSIBILI

### 1 AL LIVELLO
Viene eseguita la scansione di tutti i componenti legati fisicamente al primo livello con il componente. Non vengono
tratatti i filtri di data e la configurazione.

### 2 SCALARE
E'come la precedente ma vengono percorsi tutti i rami, fino agli estremi.

### 3 DI PRODUZIONE
E'come la scansione al livello con la seguente differenze : 
-    vengono esclusi i legami non validi per data (a meno che sia esplicitamente chiesto di ritornare tutti i legami)

### 4 DI PRODUZIONE TOTALE
E'come la scansione di produzione con la differenza che, per ogni assieme viene ripetuta una scansione di produzione,
fino agli estremi.

### 5 AI PRODOTTI FINITI
E' una scansione di produzione totale in cui vengono riportati solo gli estremi.

### 6 RIEPILOGATA
E' una scansione di produzione totale in cui vengono sommate le quantità dei codici che appaiono più volte (in rami
diversi, oppure con sequenze diverse nello stesso ramo).

### 7 RIEPOLOGATA AI PRODOTTI FINITI
E' una scansione ai prodotti finiti in cui vengono sommate le quantità dei codici che appaiono più volte.

### 8 RIEPLIOGATA DI PRODUZIONE
E' una scansione di produzione (non totale) in cui vengono sommate le quantità dei codici che appaiono più volte.
