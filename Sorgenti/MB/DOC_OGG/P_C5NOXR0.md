## Obiettivo
Attraverso questo Set'nPlay è possibile monitorare e gestire tutti i dati relativi alle banche aziendali.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D030_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXR0/C5D030_001.png)
All'interno del formato guida è necessario selezionare l'azienda d'interesse e la modalità di esecuzione della funzione :  le modalità disponibili sono Interrogazione e Stampa che restituiscono lo stesso risultato ripsettivamente in formato video e in spool di stampa.
Digitando il tasto F17 o selezionando il bottone posto in basso a sinistra è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Banca :  è possibile scegliere una specifica banca per la quale si vogliono visualizzare le infomazioni presenti; lasciando blank il campo vengono visualizzati i dati di tutte le banche
 * Riferimenti agenzia :  permette di visualizzare i contatti riportati in anagrafica della banca.
 * Rapporto bancario :  attraverso questo campo è possibile visualizzare solo le informazioni relative a uno specifico rapporto bancario.
 * Informazioni rapporto :  questo campo permette di visualizzare le informazioni associate a ogni specifico rapporto bancario (conto contabile, conto corrente e codice IBAN associato).
 * Condizioni rapporto :  è possibile visualizzare anche le condizioni bancarie associate al rapporto bancario restringendole per data inizio condizioni e per numero (ad esempio è possibile richiedere di visualizzare solo le condizioni valide dal primo gennaio riportando solo le prime 10). E' inoltre possibile richiedere di non visualizzare condizioni ripetute.
 * Operazioni :  questo campo permette di visualizzare le condizioni per operazione definite per ogni rapporto bancario.

Confermando il formato guida è possibile accedere al formato lista.

## Formato lista
All'interno del formato lista è possibile visualizzare le banche aziendali ordinate per codice ABI-CAB. In particolare per ogni ABI è possibile visualizzare i CAB registrati e affianco ad ogni CAB è riportato il codice della tabella C5F che identifica la specifica banca : 

![C5D030_002](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXR0/C5D030_002.png)
Per ogni ABI-CAB è poi possibile individuare i rappporti definiti (elementi della C5J) : 

![C5D030_003](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXR0/C5D030_003.png)
Le informazioni riportate per ogni banca e per ogni rapporto bancario variano in funzione delle impostazioni definite. Nel nostro esempio è stato richiesto di riportare  tutte le informazioni visualizzabili all'interno del formato lista.
Per ogni banca sono visualizzati i contatti riportati in anagrafica della banca. Per ogni rapporto bancario sono invece visualizzate le seguenti informazioni : 
 * Dati del rapporto :  riporta il conto contabile e il conto corrente associati al rapporto bancario. Nel caso in cui il rapporto sia di tipo Conto Corrente è riportato anche il codice IBAN della banca.
 * Condizione :  questa sezione riporta le condizioni bancarie definite per lo specifico rapporto (fido, spese, tassi, ecc.). La loro definizione viene effettuata tramite la voce 'Condizioni generali per rapporto' presente all'intenro del menù della tesoreria.
 * Operazioni bancarie :  sono riportate le informazioni relative alle condizioni per operazione bancaria.

![C5D030_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXR0/C5D030_004.png)
Come è possibile visualizzare dall'immagine sopra per ogni rapporto bancario per cui sia riportato il relativo conto contabile viene eseguito un controllo di corrispondenza tra il rapporto bancario indicato per il conto contabile all'intenro della tabella C5B e il conto contabile riportato sul rapporto bancario all'intenro della tabella C5J. Nel caso in cui le due informazioni non corrispondano viene restituito un messaggio di avvertimento.

## Formato dettaglio
Per ognuna delle righe riportate nel formato lista sono disponibili diverse opzioni che variano al variare del contenuto della riga stessa : 
 * Sulle righe che identificano gli elementi della C5F sono riportate le opzioni disponibili per la tabella stessa (inserimento, modifica, copia, cancellazione, sospensione e riattivazione dell'elemento). Inoltre a partire da queste righe è possibile accedere e modificare l'anagrafica della banca tramite l'opzione 12.
 * Sulle rgihe che identificano i rapporti bancari associati ad ogni banca sono riportate le opzioni disponibili per la tabella C5J (inserimento, modifica, copia, cancellazione, sospensione e riattivazione dell'elemento). Inoltre a partire da queste righe è possibile accedere e modificare le condizioni per operazione associate al rapporto.
 * Sulle righe che identificano il conto contabile associato a un determinato rapporto è disponibile l'opzione di gestione dell'elemento che consente di entrare in modifica del relativo elemento della C5B.
 * Sulle righe che identificano il numero di conto contabile associato a un determinato rapporto è disponibile l'opzione di attribuzione del conto alla banca.
 * Sulle righe che identificano l'IBAN associato a un determinato rapporto è disponibile l'opzione di inserimento e modifica dell'IBAN stesso.
 * Sulle righe che riportano le informazioni relative alle operazioni per rapporto sono disponibili le opzioni di modifica, cancellazione e visualizzazione delle condizioni stesse.
