## Generalità
I modelli dinamici di SmeUp costituiscono un potente e semplice strumento di conoscenza e di indagine sui dati. L'idea prende spunto da alcune intuizioni sviluppate negli studi di intelligenza artificiale e delle reti semantiche.
In sostanza il modello consiste in una sovrastruttura di relazioni significative tra oggetti, stabilite da chi indaga, che si innesta sull'applicativo e che viene archiviata in uno specifico file.
Nei paragrafi successivi vengono definiti con maggiore precisione alcuni concetti astratti come relazione, proposizione, operatore e spiegato in dettaglio come costruire il modello. Vengono inoltre date indicazioni su come creare il programma costruttore e dove collocarlo nell'architettura software, e come utilizzare lo strumento di navigazione nel modello.

## Esempi
Il concetto apparirà più chiaro se facciamo un paio di esempi.

### Esempio 1
Supponiamo di avere la necessità di indagare sugli utenti dell'applicazione SmeUp e che di loro ci interessino le seguenti relazioni : 

- l'utente x ha modificato il programma y
- l'utente x è autorizzato alla funzione y
- l'utente x è capogruppo dell'utente y
- l'utente x ha modificato il file Y
...

Dunque...
gli oggetti in esame sono : 

- gli utenti,
- i programmi,
- i files,
- le autorizzazioni su funzione.

le relazioni significative sono : 

- l'utente ha modificato il file/programma,
- l'utente è autorizzato a... ,
- l'utente è capogruppo di... .


Supponiamo di lanciare un programma in grado di tracciare su un file per ogni singolo utente lo stato delle relazioni al momento del lancio.
Una volta eseguito tale programma, interrogando l'archivio, per ogni utente in tempo reale potremmo sapere quali files e programmi l'utente ha modificato, a quali funzioni è stato abilitato o quali sono gli utenti del suo gruppo... viceversa potremmo per ogni programma sapere quali sono gli utenti che hanno introdotto modifiche, idem per i files o data una funzione conoscere l'insieme degli utenti che ne sono autorizzati all'esecuzione... conoscere i capigruppo... e così via...
Cioè potremmo conoscere tutte le informazioni ricavabili dall'archivio delle relazioni attraverso i comandi sql.

### Esempio 2
Se volessimo indagare sui programmi e ci chiedessimo quali programmi vengono richiamati da un altro programma o quali file vengono da esso letti o aggiornati... o quali sono gli aggiornamenti dei programmi e quando e chi li ha effettuati.  Basterebbe fissare le seguenti relazioni "il programma x richiama il programma y" e "il programma x legge/modifica il file y"  e "il programma x è stato modificato da" e creare un costruttore che, scandendo tutti i programmi, alimenta il files con queste relazioni.
In lettura potremmo tracciare il grafo che descrive le chiamate tra programmi e tra files... e navigare in esso con gli strumenti visuali dell'interfaccia grafica.

Esempi più strutturati ed esistenti in SmeUp sono riportati in una sezione a parte... in questa sede  ci interessa far capire le potenzialità di un modello dinamico ancora embrionale come quello proposto che si limita per ora a tracciare in un archivio semplici proposizioni tra oggetti.

## Vantaggi

- Immediata fruibilità delle relazioni significative;
- Staticità strutturale :  la creazione di un nuovo modello richiede in sostanza lo studio delle relazioni significative e la scrittura del solo programma costruttore... la parte di visualizzazione resta identica per ogni modello.

