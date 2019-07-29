# Generalità
La liquidazione è la procedura tramite cui vengono consolidate le elaborazioni del calcolo provvigioni avvenute sui documenti in stato normale, mettendoli in condizione d'attesa fattura.

Se oltre a presentare un importo da liquidare il record risulta anche interamente pagato, verrà messo in stato chiuso e in stato di elaborazione 9 (da non elaborare).

# Formato di lancio
![V5PR04_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5PR04/V5PR04_01.png)Nei parametri di lancio è possibile richiedere l'emissione di una stampa di controllo di tipo : 
 * Estratto conto
 * Con situazione di residuo
![V5PR04_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5PR04/V5PR04_02.png)
# Ritorno all'elaborazione precedente
Ad elaborazione eseguita in definitivo, è possibile ritornare alla situazione preelaborazione tramite un pgm di utility.
_2_Nota, il programma permette di tornare indietro solo rispetto all'ultima elaborazione e non all'infinito.

E' da considerare inoltre che, se dopo la liquidazione era stata eseguita la creazione del piano / documento d'attesa in modo definitivo, dovrà prima essere riportata indietro anche tale elaborazione.
