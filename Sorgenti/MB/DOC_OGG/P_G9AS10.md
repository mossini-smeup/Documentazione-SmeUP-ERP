# Situazione entrate fornitori
Questa funzione permette di listare le entrate da fornitori comprese in un dato intervallo di tempo, di calcolarne il prezzo medio e di confrontarlo con un costo di riferimento.

## Formato di lancio
![G9AS10_01](http://localhost:3000/immagini/MBDOC_OGG-P_G9AS10/G9AS10_01.png)
Nel formato si impostano i tipi costo / livello di riferimento rispettivamente per le entrate di acquisto e per quelle di conto lavoro, si può scegliere se considerare o meno le note di credito.

La lista ottenuta può assumere diverse forme o ordinamenti in funzione di come vengono compilati i corrispondenti campi di selezione.

Le bolle entrata merci considerate dipendono sia dalla selezione sullo stato bolla che dalle parzializzazioni impostate.

# Aggiornamento costo medio
La funzione di analisi entrate può anche aggiornare il costo medio degli articoli, inoltre il costo medio entrato può essere anche pesato verso una giacenza, valorizzata, iniziale presa dall'archivio del  magazzino fiscale (GMSIAN).

## Ponderazione con giacenza inizio periodo
Per ponderare il costo medio delle entrate fornitori con la giacenza di inizio periodo, sul formato guida bisogna selezionare il campo "Ripresa valori inizio periodo" ed impostare opportunamente i campi della finestra seguente : 
![G9AS10_02](http://localhost:3000/immagini/MBDOC_OGG-P_G9AS10/G9AS10_02.png)in pratica bisogna inserire l'esercizio di cui si vuole considerare la giacenza valorizzata di inizio.

## Impostazioni di salvataggio costo medio
Il costo medio (ponderato o meno verso la giacenza iniziale) viene memorizzato secondo le impostazioni presenti in una seconda finestra che si apre selezionando il campo "Aggiorna costo medio", vedi esempio seguente : 
![G9AS10_03](http://localhost:3000/immagini/MBDOC_OGG-P_G9AS10/G9AS10_03.png)
## Impostazioni struttura di salvataggio costo medio
Per memorizzare correttamente i dati di costo medio la struttura dei campi del file dei costi (tabelle specifiche IGIxx) deve essere come da sempio seguente : 
![G9AS10_04](http://localhost:3000/immagini/MBDOC_OGG-P_G9AS10/G9AS10_04.png)
Il sistema memorizza i costi medi di acquisto a fronte del contesto articolo, mentre i costi medi di conto lavoro vengono memorizzati per articolo e in un tema che deve avere come "codice 1" la fase del ciclo di lavorazione dell'articolo.
