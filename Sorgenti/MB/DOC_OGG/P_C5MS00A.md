## Obiettivo

Questo programma si occupa della lettura dei dati contabili relativi alle operazioni svolte con soggetti di nazionalità San Marino.
In particolare verranno prese in considerazione tutte le le operazioni di San Marino di tipo reverse
charge

Per tutte le registrazioni contabili come riferimento temporale viene elaborata la data registrazione.

## Formato guida

![C5C020_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5MS00A/C5C020_001.png)
All'interno del formato guida è necessario impostare i seguenti campi : 
 * Modalità esecuzione. Questo campo può essere compilato con : 
 ** 1 - Stampa ed Esecuzione :  questa modalità consente di ottenere una stampa dei dati estratti, con eventuale segnalazione di errori e dati incompleti, e la popolazione del file dei movimenti San Marino.
 ** Bianco - Solo stampa :  questa modalità consente di ottenere una stampa dei dati estraibili con eventuale segnalazione di errori e dati incompleti.
 * Tipo ripresa. Questo campo può essere compilato con : 
 ** V - Scrivi tutti :  effettua una pulizia del file all'interno del periodo indicato in basso e riscrive i dati rilevati all'interno del periodo stesso. Se ne sconsiglia, quindi, l'utilizzo nel caso in cui si siano già apportate modifiche a movimenti appartenenti al periodo indicato.
 ** Bianco - Scrivi solo mancanti :  effettua un aggiornamento del file inserendo i soli movimenti non ancora estratti. In caso di aggiornamento dei dati della contabilità, quindi, se il record era già stato precedentemente estratto all'interno dei movimenti San Marino eseguendo la ripresa con questa tipologia il record non verrà aggiornato.
 * Periodo. All'interno di questi campi è possibile impostare un range temporale all'interno del quale analizzare i dati per la ripresa. Impostando una data inizio e una data fine verranno analizzate solo le registrazioni contabili per le quali la data registrazione ricade in questo intervallo.
 * Assoggettamenti da escludere. All'interno di questo campo è possibile impostare una lista di codici IVA da escludere dalla ripresa.
 * Tipi Registrazione escludere. All'interno di questo campo è possibile impostare una lista di tipi registrazione da escludere dalla ripresa.
 * Clienti da escludere. All'interno di questo campo è possibile impostare una lista di clienti da escludere dalla ripresa.
 * Fornitori da escludere. All'interno di questo campo è possibile impostare una lista di fornitori da escludere dalla ripresa.

Per confermare l'esecuzione del programma è necessario digitare il comando F6 da tastiera o il relativo pulsante.

All'interno del formato guida sono disponibili le memorizzazioni che consentono di salvare i dati impostati. Per maggiori informazioni sull'utilizzo delle memorizzazioni si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

## Stampa di controllo

Il lancio dell'estrazione movimenti produce una stampa che riporta i dati estratti/estraibili e gli errori eventualmente rilevati : 
![C5C020_009](http://localhost:3000/immagini/MBDOC_OGG-P_C5MS00A/C5C020_009.png)
All'interno della stampa sono riportati : 
 * Numero movimento San Marino
 * Numero riga all'intenro della registrazione contabile
 * Numero registrazione contabile
 * Codice tabella e codice CVS della nazione del soggetto
 * Tipologia di soggetto
 * Codice e descrizione soggetto
 * Partita IVA e Codice Fiscale
 * Tipo e numero protocollo
 * Data movimento San Marino
 * Codice e aliquota percentuale assoggettamento IVA
 * Imponibile e Imposta
 * S = Segno (+ per fatture, - per note)
 * T =Tipologia di esenzione (N per non imponibili, E per esenti, S per non soggette, Vuoto per imponibili)
 * N = Natura operazione (1 per Servizi, 2 per Merci)

Come evidenziato  nell'immagine all'interno della stampa sono riportati anche gli errori eventualmente rilevati che possono essere : 
 * Errori sulla natura dell'assoggettamento IVA :  in questo caso il sistema indica che all'interno della tabella IVA per l'elemento riportato nella colonna As non è compilata la natura dell'operazione.


