# aaa

## Obiettivo
La scheda serve per simulare l'esecuzione di una funzione su un insieme di _x_ oggetti, o l'esecuzione massiva di un considerevole numero di funzioni.
E' divisa in 4 diverse sottosezioni (5 con la presente di documentazione)

### La sezione Da uno script guida
Nella sezione **Esecuzione** sono presenti : 

- L'albero Gruppi di funzioni che contiene una lista di funzioni da eseguire su un insieme di _x_ oggetti. Cliccando su una foglia dell'albero, si apre
- La matrice Funzioni che riporta la funzione associata alla foglia ripetuta per gli _x_ oggetti dell'insieme.
- La matrice Esecuzione serve per eseguire la funzione e misurarne il tempo.
- L'albero Oggetti che contiene l'insieme degli _x_ oggetti su cui è stata eseguita la funzione.

Cliccando su una riga della matrice Funzioni o Esecuzione si ha la possibilità di vedere i risultati prodotti dalla funzione chiamata in una nuova sezione della stessa scheda.
La sezione **Analisi della Memoria** è divisa in 2 sottosezioni :  quella a sinistra contiene la funzione utilizzata per la costruzione dell'Insieme di oggetti, quella a destra contiene l'insieme di oggetti vero e proprio.
Nella sezione **Script Guida** è possibile analizzare dettagliatamente lo script che comanda le varie sezioni descritte sopra. Lo script è LO_VERFUN nel file SCP_SET nella libreria SMEDEV. Questo script viene letto per costruire l'albero Gruppi di Funzioni in cui, a ogni nodo, corrisponde una riga **T.FUN** dello script. Le righe **T.OGG** servono invece per costruire le liste di oggetti su cui eseguire la funzione. Il servizio che interpreta questi script, che si occupa di costruire gli alberi ed eseguire le funzioni è il LOSER_06.

### La sezione Dalle schede
Nelle sezioni **Applicazioni**, **Moduli**, **Oggetti** è presente la lista delle applicazioni-moduli-oggetti.
Cliccando su un nodo di questo albero, viene richiamato il LOSER_04 e la sezione in basso a sinistra viene riempita con una matrice che è la lista degli script che appartengono all'Applicazione/Modulo/Oggetto selezionato. Il click su una riga di questa matrice richiama il LOSER_06 passando il nome del membro di script su cui ho cliccato e va a riempire : 

- La sezione Funzioni con la lista di funzioni presenti nello script (in pratica tutte le righe D.FUN.STD)
- La sezione Esecuzione con la lista sopra ma eseguendo anche la funzione in questione per calcolarne il tempo di esecuzione.


### La sezione Dai servizi
Analogamente alla sezione precedente, Nella sezione **Applicazioni** è presente la lista delle applicazioni.
Cliccando su un nodo di questo albero, viene richiamato il LOSER_03 e la sezione in basso a sinistra viene riempita con una matrice che è la lista di servizi che appartengono all'Applicazione selezionata. Il click su una riga di questa matrice richiama il LOSER_06 passando il nome del servizio su cui ho cliccato e va a riempire le 2 sezioni Funzioni ed Esecuzione con le stesse modalità spiegate per la sezione **Dalle schede**.

### La sezione Analisi di massa
E' divisa in due sottosezioni : 

- Funzioni in tutte le schede contiene la lista di __tutti i richiami di funzione__ presenti negli script di scheda
- Funzioni in tutti i servizi contiene la lista di __tutte le funzioni/metodi di tutti i servizi__

