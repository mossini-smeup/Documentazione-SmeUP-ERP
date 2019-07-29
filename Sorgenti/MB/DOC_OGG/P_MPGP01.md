## Manutenzione manuale Piano
Con questa funzione si possono eseguire le opzioni consuete (inserimento, modifica, copia, cancellazione, interrogazione) di Sme.up sugli elementi di una vista piano.
Il formato di partenza è il seguente : 

![MP_001_06](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_06.png)
Quando si sceglie un'opzione di manutenzione manuale, il sistema presenta lo schermo seguente : 

![MP_001_07](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_07.png)
In modalità inserimento le colonne "Quantità" e Quantità Variazione" si presentano vuote e, man mano che vengono inserite le quantità nei campi di input, il sistema compila la colonna "Quantità Variazione".
In funzione del valore del campo Variazione è possibile operare variazioni in modalità : 
 * __incremento__ (1), con cui le quantità inserite vengono sommate algebricamente alle quantità precedenti (è possibile inserire variazioni negative);
 * __sostituzione__ (2), con cui le quantità inserite sostituiscono quelle precedenti.

Possono essere inserite quantità giornaliere, settimanali o mensili, le cui variazioni vengono automaticamente distribuite sui giorni lavorativi.

>N.B. :  se la periodicità del piano prevede solo periodi mensili, le quantità possono essere solo inserite a livello mensile e, ad ogni variazione, il sistema calcolerà e visualizzerà nel campo "Quantità Variazione" la nuova quantità (che sostituirà quella attuale della vista piano).
Per registrare le variazioni inserite è necessario utilizzare il comando F6, oppure tornare allo schermo guida con il comando funzione F12.
Utilizzando il campo opzione (colonna di sinistra), è possibile forzare, per i periodi selezionati, la quantità del piano di variazione a : 
 * zero con l'azione A = Azzera;
 * uguale alla quantità del piano di riferimento (quantità originale della vista piano) con l'azione R = Reinserimento.

![MP_001_08](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_08.png)
Oltre alle classiche opzioni di gestione di Sme.up, ne esistono di specifiche sviluppate per MPS : 
 * Gestione in lista, che permette di inserire o modificare direttamente, a parità di codice 2, tutti i valori inseriti nei vari periodi per tutti i codici 1 della vista piano;
 * Analisi delta, che permette di confrontare una vista con un'altra a parità di codice 1 e codice 2;
 * Analisi grafica, che visualizza graficamente i valori presenti nella vista, segnalando i periodi in cui la quantità è massima e quelli in cui la quantità è minima.

## Gestione in Lista
Quando si lancia la gestione in lista, fissato il "codice2" si presenta il seguente formato in cui viene presentata la lista seguente con tutti i codici 1 : 

![MP_001_10](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_10.png)
La funzione F15 calcola e visualizza i totali per colonna, mentre la funzione F14 emette la descrizione dei codici 1 : 

![MP_001_11](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_11.png)
Con la funzione F18 si attiva la sintesi delle quantità, permettendo di raggruppare più periodi e sommare le relative quantità. Il sistema presenta la lista di tutti i periodi che costituiscono la vista
piano : 

![MP_001_12](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_12.png)
Nel campo selezione, definendo il periodo iniziale (>I) e quello finale (>F) del raggruppamento, il sistema calcola e visualizza data iniziale, data finale e il numero di giorni per il periodo raggruppato.
La sintesi può essere memorizzata utilizzando la funzione delle memorizzazioni multiple.
Con la funzione F9 si può selezionare una delle sintesi di periodo standard per le quali è già stata preparata la definizione : 

![MP_001_13](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_13.png)
Con F6 si confermano i periodi sintetizzati e il sistema ritorna alla lista precedente, visualizzando solo i periodi sintetizzati e le relative quantità : 

![MP_001_14](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_14.png)
## Analisi Delta
Quando viene lanciata l'Analisi Delta si presenta lo schermo seguente (se non viene inserito si assume che il piano non cambi) : 

![MP_001_15](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_15.png)
Possono essere inserite delle viste da confrontare con quella di partenza, è possibile inserire un segno di confronto (quando è "-" tutte le quantità della vista vengono cambiate di segno) oppure un codice di raggruppamento (campo R) con viste aventi il medesimo.
Il risultato dell'elaborazione viene presentato nella videata seguente : 

![MP_001_16](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP01/MP_001_16.png)