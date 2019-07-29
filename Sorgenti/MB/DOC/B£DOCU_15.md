 :  : HEA PRIV(001)

# Documentazione on-line

## Introduzione
L'attuale sistema di gestione dei manuali di Sme.UP è stato esteso per permettere ai clienti di scaricarli dalla rete internet.

## Generazione e pubblicazione dei manuali
La generazione di un documento/book crea un file in formato PDF. Questo file può essere inviato in FTP su una oppure due destinazioni.

Le destinazioni FTP sono facoltative e possono essere specificate entrambe contemporaneamente.

La generazione/pubblicazione dei manuali può essere eseguita in vari modi differenti.
Alla generazione/pubblicazione di un documento corrisponde una specifica richiesta (identificata da una F). Questa richiesta può essere eseguita sul client dell'utente o essere eseguita da un server Loocup.
Questa richiesta può essere inserita anche in una sequenza di generazione (flusso).

Abbiamo quindi le seguenti possibilità di generare/pubblicare documenti : 
* Manuale di un singolo documento
* Automatica di un singolo documento
* Manuale di tutti i book delle applicazioni
* Automatica di tutti i book delle applicazioni

Posto che la generazione automatica di un singolo documento è poco significativa, illustreremo le altre funzionalità.

_1_Pubblicazione manuale di un singolo documento
La pubblicazione dei documenti può avvenire contestualmente alla generazione oppure in una fase successiva. Se la pubblicazione è contestuale è possibile indicare due destinazioni. La prima sull'AS400A, la seconda sul server al Mix (demo.smeup.com).
N.B. :  la pubblicazione differita avviene solo in modalità manuale usando un client FTP.

![B£DOCU_22](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_22.png)Nell'immagine che segue vediamo la scheda della documentazione e possiamo individuare i passi compiuti per definire il book e per invocare la stampa / pubblicazione.
Nel dettaglio vediamo che dopo aver selezionato la scheda della applicazioni, selezioniamo un'applicazione (in questo caso B£),.
Possiamo selezionare quattro tipi di manuali tra applicativo, operativo, documentazione tecnica e note di sviluppo.
Effettuata la scelta, per generare il PDF è necessario selezionare la linguetta Set'n Play ed infine  Comandi Latex.
Il pulsante che genera la documentazione e la pubblica al mix, sul server demo.smeup.com è  l'ultimo in basso.

![B£DOCU_23](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_23.png)
_1_Generazione manuale e pubblicazione documenti da iSeries
Dalla scheda della documentazione (My Loocup, documentazione), selezionare la linguetta Generazione documenti, poi nell'albero di sinistra, sotto la voce Latex, sono disponibili le varie collane di documenti da generare. Se ad esempio si seleziona Tutte le applicazioni, e poi Flusso batch di tutti i documenti, verrà associata la funzione di creazione al pulsante posto in basso.

![B£DOCU_24](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_24.png)
_1_Generazione automatica e pubblicazione documenti da iSeries
Come descritto dalla seguente immagine, l'AS400 richiede a Loocup server la generazione dei file PDF.
Al termine del processo Loocup server invia i file ottenuti a un server SMEA (MIX).
E' possibile schedulare tale attività direttamente su iSeries.

![B£DOCU_25](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_25.png)
La generazione automatica presuppone un'architettura in cui Loocup è installato su un server, è attivo e l'AS400 è a conoscenza di questo server Loocup.

_3_NOTA :  La generazione automatica scandisce la lista delle applicazione, poi verifica l'esistenza dei  vari tipi di membri di documentazione (operativa, applicativa, tecnica, di sviluppo) e procede alla generazione/pubblicazione. Non vi è nessun controllo sulla validità del contenuto.  La scelta del metodo è a totale discrezione del responsabile dei manuali, anche se di default l'opzione usata è la prima illustrata.

## Consultazione dei manuali
Per consultare la documentazione il cliente deve "loggarsi" all' "Area Riservata" di www.smeup.com, accedere alla sezione "Documentazione" del sito (link nel menu principale in alto a destra) sottosezione "Manuali" e cliccare sul link a fondo pagina ("LINK PER ACCEDERE ALLA LISTA").
A questo punto l'utente può consultare e scaricare i manuali a cui è autorizzato ad accedere.
Il controllo dei documenti accessibili al cliente è effettuato dal server as400 in Smea, a cui il sito smeup.com accede con l'utente specifico WU2_SME, come mostrato dall'immagine che segue.

![B£DOCU_26](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_26.png)
## Autorizzazione ai documenti
In fase di registrazione del cliente al sito di Sme.UP il server web richiede al sistema AS400 (attraverso un web service) un codice SMEUP (codice di 15 caratteri max) che sarà memorizzato assieme agli altri dati dell'utente (quelli immessi al momento della registrazione :  nome, mail, P.IVA ecc).
Quando in seguito il cliente si loggherà al sito per visionare i manuali online il server invierà il suo codice SMEUP all' as400 per ottenere l' elenco dei manuali disponibili.

![B£DOCU_27](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_27.png)
_1_NOTA :  Lo screenshot "Area riservata" (raffigurante la sezione Web.UP 2.0) usato nello schema è indicativo dell' accesso all' area riservata in generale, in quanto al momento del rilascio la documentazione online sarà raggiungibile dalla sezione "Documentazione" del sito.


### Gestione autorizzazioni ai documenti in AS/400
In AS/400 le autorizzazioni sono contenute nel membro C_USR del file DOC_BOK di SMEDEV, dove : 
 * esiste un legame tra il dominio e-mail ed un tipo / codice soggetto :  es. _2_..BOK.DOM Dom="smea.it" Tso="CLI" Sog="001"
 * esiste un legame tra il tipo / codice soggetto e applicazioni, aree, tipi manuale a cui è autorizzato :  es. _2_..BOK.SOG Tso="CLI" Sog="003" AutApp="**" AutAre="**" AutMan="VIS;OPE;APP;TEC"
 * esiste un legame tra un indirizzo e-mail ed un tipo / codice soggetto :  es. _2_..BOK.USR Mai="abcdflu@alice.it" Tso="CLI" Sog="003"

## Procedura di accesso all'area riservata
Il flusso di registrazione/accesso è quello che segue : 

![B£DOCU_28](http://localhost:3000/immagini/B£DOCU_15/BXDOCU_28.png)
## Note tecniche
I documenti sono generati tramite il componente di Loocup FRM. Il componente riceve i dati da elaborare dal servizio B£SER_22, poi richiama il motore Latex utilizzando il setup ricevuto.
Il motore latex genera un pdf che può essere salvato oppure inviato in FTP ad una delle destinazioni.

Vediamo in dettaglio la funzione che genera i documenti in Latex : 
F(FRM;B£SER_22;LAT.PRE) 1(MB;DOC_XXX;YYYY) P(...)

Il campo P ammette i seguenti parametri : 
* Parametro Show : 
** Yes :  apre la finestra di gestione setup con il setup corrente
** No :  non apre la finestra di gestione Setup
* Parametro  Edit : 
** Yes :  l'utente può modificare il setup (se presentato nel gestore)
** No :  l'utente non può modificare il setup
* Parametro Sav : 
** Yes o non definito :  salva nella cartella \\SMEA.IT\DFS_ROOT\SMEUP\SMEDOC\DOC_xxx
** No :  non salva una copia del file generato
* Tmp :  salva nella cartella di installazione di LoocUp, cartella LOOCUP_TMP\DOC_xxx.
* Parametro Snd : 
** Yes :  invia il documento generato in FTP sul server AS400A.SMEA.IT.
** No o non definito :  Non viene inviato
* Parametro Snd2 : 
** Yes :  invia il documento generato in FTP sul server DEMO.SMEUP.COM. NOTA :  l'encoding utilizzato per l'invio dei comandi è UTF-8, pertanto solo server che implementano questa funzionalità sapranno gestire correttamente i nomi dei file se contengono caratteri non ASCII.
** No o non definito :  non viene inviato
* Parametro Mod : 
** BAT :  specifica la modalità di generazione BATCH. Questa modalità forza i seguenti valori :  Show = No, Edit = NO, Opn = No, Sav = Yes.
** Altro o non definito :  vengono utilizzati i parametri passati nel P

_1_N.B.
Affinchè il file generato venga inviato via FTP è necessario che sia specificata una cartella di destinazione.  Per evitare di sovrascrivere book già generati o per effettuare dei test è consigliato indicare Tmp come valore del parametro Sav.

La gestione dei file contengono caratteri non ascii (ad es. il simbolo £) richiedono che il server sia in grado di ricevere comandi in UTF-8. Questa modalità è gestita sulla seconda destinazione FTP. Sulla prima destinazione no in quanto l'AS400 non gestisce i comandi in UTF-8.

## Caching dei dati

- Da Internet Explorer viene lanciata funzione richiesta manuali (con la conseguente apertura della pagina).
- La richiesta viene intercettata dal Programma Java che sottomette la Fun all'iSeries attraverso delle connessioni di tipo Looc.Up (come es. il job  LO_E140607  sottosistema QBATCHUI).
- iSeries :  esegue la Fun nel Job sopra indicato, mette in cache i dati (sempre nel Job) e li restituisce come XML al programma Java.
A questo punto qualcuno modifica le autorizzazioni ai manuali su iSeries attraverso Looc.Up e salva.
- Dalla stessa sessione di Internet Explorer o da una nuova, viene fatta la stessa richiesta fatta al punto 1 e i dati restituiti non vengono filtrati secondo le nuove autorizzazioni.

Il motivo è che la richiesta fatta dal Browser ed intercettata dal programma Java sottomette la Fun nello stesso Job iSeries di prima, che ha i dati in cache e quindi ripresenta gli stessi risultati.

Per evitare questo meccanismo ci sono 2 modi : 
* Forzo la Fun a non utilizzare la cache;
* Individuo od elimino il Job in questione sull'iSeries in modo che la richiesta fatta ne crei uno nuovo;
