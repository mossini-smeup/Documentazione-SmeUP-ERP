# M5ANT     -  ANTICIPO TEMPI PER NON LOTTIZZARE
Definisce le varie modalità con cui è possibile forzare l'arrotondamento al lotto minimo/multiplo se un consiglio di
pianificazione sfonda nel passato.
Lo scopo è di non produrre una disponibilità eccessiva irrealistica nel passato.
NB :  la suddivisione per lotto massimo viene sempre comunque eseguita.

## VALORI POSSIBILI

### ' ' NESSUNO
Il consiglio viene sempre lottizzato.

### '1' DATA PIANIFICAZIONE
Il consiglio non viene lottizzato se la data fonte è minore della data di pianificazione.

### '2' DATA PIANIFICAZIONE + TEMPO DI APPROVVIGIONAMENTO FISSO
Il consiglio non viene lottizzato se la data fonte è minore della data di pianificazione sommata al tempo di
approvvigionamento fisso dell'articolo, relativo al tipo ordine che si sta pianificando (produzione, acquisto,
lavorazione).
Vengono applicati gli eventuali tempi specifici se i parametri di pianificazione sono per riferimento (ente, commessa,
configurazione).

### '3' DATA PIANIFICAZIONE + TEMPO DI APPROVVIG.FISSO E RETTIFICA
E' come il caso precedente con la differenza che viene considerato anche il tempo di approvvigionamento di rettifica.

### 'A' CORRISPONDE A '1' MA VIENE DATA SOLO SEGNALAZIONE

### 'B' CORRISPONDE A '2' MA VIENE DATA SOLO SEGNALAZIONE

### 'C' CORRISPONDE A '3' MA VIENE DATA SOLO SEGNALAZIONE
