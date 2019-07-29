Il controllo errori sugli oggetti consiste in una serie di elaborazioni previste e relative consultazioni per gli output che con una gestione centralizzata permettono di identificare e gestire gli errori, visualizzarne la documentazione, fornire una traccia alla loro stesura, come eventuali suggerimenti per azioni rivolte alla loro correzione.


## Obiettivo
L'obiettivo primario del controllo errori è validare le informazioni di qualsiasi oggetto applicativo, sia per singola istanza di oggetto che in maniera massiva, in un'ottica sia di verifica immediata che di mantenimento della validazione nel tempo.

## Controlli interattivi
Il controllo errori sugli oggetti è una funzionalità rilasciata nella voce di menù properties "Controllo errori" sia in loocup che in webup ed è richiamabile per una classe, una lista o per una singola istanza di oggetto.
Nei primi 2 casi, trattandosi di validazione massiva, si appoggia ad una costruzione fonte (LOA15_A3), mentre per la singola istanza vengono effettuati controlli immediati tramite la scheda ed il servizio specifici del controllo errori (B£UTIL_01), con la visualizzazione dell'elenco errori dell'istanza e la possibilità di richiamare il LOA36 per la gestione dei soli campi in errore.

## Controlli schedulati
Oltre ai controlli puntuali di cui sopra dal menù properties, il controllo può essere soprattutto utile in modo schedulato.
L'approccio dovrebbe essere questo :  definire le liste degli oggetti più "sensibili" per l'azienda e decidere per ciascuna ogni quanto il sistema del controllo errori la deve elaborare.
Nello specifico, il LOA15_A3 del controllo errori può essere inserito in un flusso (LOA11) in modo che ogni notte vengano controllati per esempio degli oggetti di una classe con stato attivo e l'elenco degli errori risultanti venga inviato via mail al relativo responsabile.

## Struttura
La struttura del controller ne eredita la struttura dalla K89, pertanto è suddivisa in 3 livelli : 
### Livello1
A questo livello sono controllate le informazioni di base dell'oggetto selezionato. Attraverso la tipizzazione dei campi, descritta sul database, come nella definizione dei parametri espliciti, viene verificata la consistenza del dato segnalando l'inconsistenza qualora la stessa non fosse più valida.
### Livello 2
A questo livello vengono estesi i controlli al programma specifico standard dell'oggetto, per esempio l'obbligatorietà dei campi o la dipendenza da altri oggetti.
### Livello 3
A questo livello vengono estesi i controlli anche all'eventuale exit, dove vengono verificati i controlli relativi alle specificità del cliente.
Si fa notare che nella exit non deve essere presente l'apertura di un video, pena il malfunzionamento del controllore.



## Consultazione
La scheda di consultazione (B£UTIL_01) elenca l'oggetto contenente l'inconsistenza e il motivo della stessa. Partendo dal cruscotto che permette di consultare in modo riepilogativo gli errori è possibile procedere alla schede di navigazione degli oggetti errati che permettono di arrivare alla consultazione del singolo dato errato ed alla relativa voce di documentazione.

## Simulazione
E' possibile arrivare alla simulazione del controller, sempre attraverso la scheda B£UTIL_01.


