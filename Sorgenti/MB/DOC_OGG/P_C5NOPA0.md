## Obiettivo
Attraverso questa voce di menù è possibile gestire le pratiche già create e generarne di nuove.

## Formato guida
Alla selezione della voce di menù compare il seguente formato guida : 

![C5D010_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOPA0/C5D010_001.png)
Nel campo 'Modalità'  possibile impostare l'azione da eseguire sull'elenco pratiche :  le opzioni disponibili sono Stampa e Visualizzazione. E' necessario impostare una 'Data pratica iniziale' mentre il campo 'Data pratica finale' è facoltativo.
Attraverso i tasti F13 e F17 è possibile raggiungere la schermata delle parzializzazioni e delle impostazioni rispettivamente. All'interno delle parzializzaioni è possibile impostare il tipo pratica, il numero, la data, il rapporto bancario e/o la banca di presentazione delle distinte restituite. Nelle impostazioni è, invece,  possibile definire alcuni parametri come l'ordinamento delle distinte, la presentazione o meno degli importi e così via.

## Formato lista
Confermando con invio il formato guida verrà restituito il formato lista : 

![C5D010_002](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOPA0/C5D010_002.png)
All'interno del formato lista viene riportato l'elenco delle pratiche generate. Per ognuna di esse vengono visualizzati : 
 * la data di creazione
 * il tipo di pratica
 * il numero di pratica
 * il rapporto bancario con la relativa descrizione
 * il numero di registrazione contabile associata (se presente)
 * la valuta
 * gli importi
 * i campi che identificano lo stato della pratica : 
 ** S :  se uguale a 1 significa che la pratica è già stata stampata
 ** T :  se uguale a 1 significa che la pratica è già stata trasmessa alla banca
 ** C :  se uguale a 1 significa che la pratica è già stata contabilizzata
 ** P :  se uguale a 1 significa che è già stato contabilizzato il portafoglio bancario
 ** K :  se uguale a 1 significa che è già stata contabilizzata la maturazione degli effetti.

Ogni riga della lista identifica una pratica bancaria e per ogni riga sono disponibili diverse opzioni visualizzabili mettendo '?'.

### Opzioni
 * ST Seleziona trasmissione :  indicando questa opzione su più distinte permette di creare un solo file da inviare alla banca contenente le diverse distinte
 * SP Lettera cumulo per pratica :  permette di creare la lettera di cumulo da inviare al cliente
 * 00 Cumula per ente :  permette di lanciare la funzione di cumulo
 * 01 Crea nuova pratica :  permette di creare una nuova distinta della stessa tipologia e con lo stesso rapporto bancario riportato sulla distinta su cui si lancia l'opzione
 * 02 Modifica pratica :  permette di modificare una distinta se non è stata ancora contabilizzata
 * 05 Visualizza pratica :  permette di visualizzare la distinta
 * 08 Crea/Stampa/Contabilizza scadenze :  lancia un flusso di funzioni che permette in sequenza di creare, stampare e contabilizzare una pratica
 * 09 Crea/Trasmetti/Contabilizza scadenze :  lancia un flusso di funzioni che permette in sequenza di creare, generare il file e contabilizzare una pratica
 * 10 Modifica pratica e contabilizza :  permette di modificare e successivamente contabilizzare una pratica
 * 11 Cambio rapporto bancario :  nel caso in cui la distinta non sia stata ancora contabilizzata permette di modificare il rapporto bancario su cui è stata creata
 * 12 Contabilizza scadenze :  permette di contabilizzare la distinta
 * 13 Scontabilizza scadenze :  annulla la contabilizzazione effettuata con l'opzione 12
 * 15 Visualizza testata :  permette di vedere un riassunto della distinta (valori, registrazioni contabili associate, ecc.)
 * 16 Stampa pratica :  permette di stampare l'elenco delle scadenze incluse nella pratica
 * 17 Trasmissione :  permette di generare il file da trasmettere attraverso il proprio sistema di remote banking
 * 18 Stampa e contabilizza scadenze :  permette di stampare e contabilizzare la distinta
 * 19 Trasmetti e contabilizza scadenze :  permette di generare il file da inviare alla banca e contabilizzare la distinta
 * 52 Modifica condizioni anticipo :  sulle pratiche di anticipo permette di modificare le condizioni dell'anticipo
 * 55 Visualizza condizioni anticipo :  sulle pratiche di anticipo permette di visualizzare le condizioni dell'anticipo

## Formato dettaglio
Selezionando con 05 una pratica è possibile visualizzarne il dettaglio : 

![C5D010_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOPA0/C5D010_004.png)
In particolare è possibile visualizzare le singole rate incluse nella pratica, gli enti, gli importi, le date,e tutte le altre informazioni specifiche della distinta. In fondo all'elenco delle rate incluse nella pratica è possibile visualizzare un riassunto della distinta che ne riporta l'importo totale e il numero di rate incluse.

Per maggiori dettagli sulle informazioni riportate nel formato dettaglio si veda il seguente : 
- [Dettaglio pratiche](Sorgenti/MB/DOC_OGG/P_C5RR12K2)
