# ESDIS     -  TIPO ESPLOSIONE DISTINTA
Definisce le modalità di scansione in esplosione di una distinta base, a partire da un tipo distinta, da un assieme, e
da ulteriori condizionamenti (data, configurazione).

## VALORI POSSIBILI

### 1 AL LIVELLO
Viene eseguita la scansione di tutti i componenti legati fisicamente al primo livello con l'assieme. Non vengono
trattati i filtri di data e la configurazione.

### 2 SCALARE
E' come la precedente ma vengono percorsi tutti i rami, fino agli estremi.

### 3 DI PRODUZIONE
E' come la scansione al livello con le seguenti differenze : 
-    se l'assieme ha un gruppo distinta viene scandito quest'ultimo (in questo caso la distinta deve essere di
     articoli)
-    vengono esclusi i legami non validi per data (a meno che sia esplicitamente chiesto di ritornare tutti i legami)
-    viene applicata la configurazione (sia come esclusione di legami, sia come variazione del loro contenuto)
-    se un componente è un fittizio (primo carattere del tipo parte = '0') vengono trattati anche i suoi componenti (e
     così via, ricorsivamente, fino ad incontrare un componente non fittizio) :  anche in questo caso la distinta deve
     essere di articoli

### 4 DI PRODUZIONE TOTALE
E' come la scansione di produzione con la differenza che, per ogni componente non fittizio viene ripetuta una scansione
di produzione, fino agli estremi.

### 5 AI MATERIALI DI BASE
E' una scansione di produzione totale in cui vengono riportati solo gli estremi.

### 6 RIEPILOGATA
E' una scansione di produzione totale in cui vengono sommate le quantità dei codici che appaiono più volte (in rami
diversi, oppure con sequenze diverse nello stesso ramo).

### 7 RIEPOLOGATA AI MATERIALI DI BASE
E' una scansione ai materiali di base in cui vengono sommate le quantità dei codici che appaiono più volte.

### 8 RIEPLIOGATA DI PRODUZIONE
E' una scansione di produzione (non totale) in cui vengono sommate le quantità dei codici che appaiono più volte.
