
## Controllo dei requisiti minimi per il funzionamento di un client Looc.Up


Lo scopo del presente documento è presentare le funzionalità e i controlli dedicati alla valutazione della compatibilità di uno specifico sistema con l'esecuzione di un client Looc.Up. L'obiettivo è quello di individuare in modo semplice ed intuitivo l'esistenza di vincoli o problematiche che possano rendere difficoltoso o impossibile il corretto utilizzo di un client Looc.Up su uno specifico PC.

Per facilitare al massimo la valutazione, sono state prodotte delle procedure automatiche per la valutazione di una macchina.

I controlli effettuabili possono essere classificati in due famiglie principali : 


- Controlli di compatibilità sul sistema candidato per l'installazione di Looc.Up
- Controlli sulle prestazioni in avvio di un client Looc.Up


In questo documento tratteremo il primo tipo di controlli.

## Controlli di compatibilità di un sistema con l'installazione di un client Looc.Up

In questa famiglia rientrano tutti i controlli dedicati alla valutazione della compatibilità di uno specifico sistema con l'installazione di un client Looc.Up. Per le sue caratteristiche di funzionamento, Looc.Up può richiedere al sistema candidato per l'installazione l'ottemperanza di requisiti particolari senza dei quali potrebbe essere compromessa la normale funzionalità del prodotto. In mancanza di questi prerequisiti, il client Looc.Up potrebbe non funzionare correttamente o manifestare problemi di funzionamento o di prestazione che potrebbero rendere difficoltosa la normale operatività.

Per questi motivi, prima di procedere con l'installazione di Looc.Up su uno specifico sistema, è importante valutare con attenzione se il sistema stesso soddisfi i requisiti hardware e software minimi richiesti dal client.

La valutazione di compatibilità può avvenire in due fasi.

### Controllo manuale dei requisiti di sistema

La prima fase, più semplice, è quella di effettuare una serie di controlli manuali sul sistema prima di procedere all'installazione del client. Questa fase è utile anche per definire quali debbano essere i requisiti hardware e software minimi nel caso si debba acquistare una nuova macchina o selezionare la macchina più adatta tra quelle in proprio possesso.

Alla pagina : 

 :  : DEC T(J1) P(PATHFILE) [http://www.smeup.com/it/soluzioni/looc-up-download/requisiti-di-sistema-per-l-installazione-di-lo+
](http://www.smeup.com/it/soluzioni/looc-up-download/requisiti-di-sistema-per-l-installazione-di-lo+
)
oc-up)

è possibile trovare una lista dettagliata dei requisiti hardware e software richiesti da Looc.Up. I prerequisiti elencati in questa lista sono sia di tipo obbligatorio (requisiti che devono forzatamente essere soddisfatti) che di tipo consigliato (requisiti non strettamente necessari ma consigliati per un migliore funzionamento del prodotto). Sulla base di questa lista di requisiti sarà possibile effettuare una prima valutazione sulla compatibilità della macchina in proprio possesso.


### Controllo automatico dei requisiti di sistema

Oltre al controllo manuale descritto nel punto precedente, è stata implementata una funzionalità di controllo automatico sui prerequisiti di sistema. Rispetto alla procedura manuale, la procedura di valutazione automatica presenta una serie di vantaggi che possono essere elencati nei seguenti punti : 


- Automatizzazione dei controlli :  oltre al facilitare la procedura, l'automatizzazione dei controlli riduce il rischio che alcuni controlli non vengano effettuati o vengano effettuati in maniera errata.
- Controlli su sistemi multipli :  la procedura automatica facilita la procedura di controllo nel caso in cui Looc.Up debba essere installato su un numero elevato di macchine, magari di tipo eterogeneo.
- Confronto dei risultati :  grazie alla procedura automatica, i controlli possono essere ripetuti ogni volta che serve. Il confronto dei risultati tra macchine diverse o esecuzioni diverse della procedura
automatica può aiutare a capire dove si annidano i problemi e dove sia meglio intervenire per ottimizzare l'installazione Looc.Up.


### Esecuzione manuale del programma di controllo

L'esecuzione manuale del programma di controllo è consigliata la prima volta che si installa Looc.Up su un sistema ed è consigliabile effettuarla appena dopo aver installato il prodotto ma prima della prima esecuzione. Serve per valutare immediatamente eventuali incompatibilità o colli di bottiglia che potrebbero rendere difficoltoso il funzionamento di Looc.Up.

L'esecuzione manuale può essere effettuata nel seguente modo : 


- Se si sta installando Looc.Up in locale, installlare Looc.Up utilizzando il setup ed accedere alla cartella di installazione (normalmente C : /Programmi/Loocup oppure C : /Programmi (x86)/Loocup. Se invece Looc.Up è installato in mopdo centralizzato sul server, accedere alla cartella condivisa sul server.
- Avviare il programma LoocupNetTester_w.exe, presente nella cartella di installazione di Looc.Up a partire dalla versione V3R2.
- Alla partenza della GUI, immettere l'indirizzo del server AS400 di riferimento nell'apposita casella di input.
- Attendere la fine esecuione dei controlli. A termine del programma verrà visualizzata una finestra di riepilogo che mostrerà l'esito dei controlli effettuati e suggerirà eventuali azioni correttive richieste.
- Nella cartella LOOCUP_LOG/NETLOG, sempre presente nella cartella di installazione di Loocup, verrà creato un file di log che potrà essere interrogato all'interno di Looc.Up secondo le modalità illustrate in seguito. Il nome del file di log viene calcolato univocamente ad ogni esecuzione del controllo e viene mostrato all'interno della GUI nell'apposito campo nella parte alta della finestra.
 :  : PAR : END

![LOBASE_092](http://localhost:3000/immagini/LOBASE_038/LOBASE_092.png)
### Esecuzione del programma di controllo ad ogni avvio di Looc.Up

Con questa modalità di esecuzione, il programma di controllo viene lanciato in modalità nascosta ad ogni avvio di Looc.Up. E' una modalità utile soprattutto nel caso di installazione di Looc.Up centralizzata sul server e consente la raccolta periodica di informazioni sullo stato dei singoli client al fine di valutare l'andamento del sistema nel tempo e l'effetto di eventuali variazioni sulle prestazioni globali del sistema.

L'esecuzione del programma di controllo, segue la seguente logica : 


- Il programma di controllo viene eseguito ogni volta che un Looc.Up viene avviato su un PC. E' possibile abilitare o disabilitare questa funzionalità andando a modificare il contenuto del file
**netlog.properties** presente nella cartella <dir installazione loocup>/LOOCUP_LOG. Il file contiene un unica voce **netlog_active** che può essere impostata al valore true o false. Se true il programma di controllo viene avviato ad ogni avvio di Looc.Up, se false no.
- L'esecuzione del programma di controllo è nascosta. Il programma riceve automaticamente da Looc.Up tutte le informazioni necessarie al controllo e non mostra all'utente alcuna richiesta di input e nessun output.
- Il programma di controllo produce un file di log che viene memorizzato all'interno della cartella LOOCUP_LOG/NETLOG. Il file di log contiene il risultato dei controlli effettuati ed ha una denominazione del tipo **<IP macchina>-<utente AS400>-<sistema AS400>.log**. Se nella cartella LOOCUP_LOG/NETLOG esiste già un file con lo stesso nome, il controllo non viene eseguito in modo tale da evitare controlli multipli sulla stessa macchina ad ogni riavvio di Looc.Up. In altre parole, il controllo di avvio su una specifica macchina, per uno specifico utente AS400 e per uno specifico sistema AS400 viene eseguito una volta al primo avvio di quella macchina con quell'utente e quel sistema, poi non viene più rieseguito finchè nella cartella LOOCUP_LOG/NETLOG ci sarà il file di log prodotto dalla prima esecuzione. Per forzare la riesecuzione è sufficiente cancellare il file di log e riportarsi nelle condizioni di prima esecuzione



### Valutazione dei risultati del controllo automatico.

La procedura automatica di controllo produce un log che consente la valutazione della compatibilità di un sistema con l'installazione e l'esecuzione di Looc.Up.

Nel caso in cui il controllo venga avviato in modalità manuale, i risultati oltre che nel file di log vengono anche mostrati all'interno della GUI del programma.
Le informazioni mostrate sono le stesse di quelle inserite nel log ma grazie alla presenza di una GUI è possibile mostrarle in maniera tabellare senza richiedere l'avvio del client Looc.Up. Questa modalità è utile soprattutto quando non è possibile avviare Looc.Up, per evitare un controllo manuale del file di log prodotto.

Una volta avviato Looc.Up, i file di log prodotti all'interno della cartella LOOCUP_LOG/NETLOG potranno invece essere agevolmente analizzati utilizzando l'apposita scheda di secondo le modalità specificate successivamente.

Le informazioni raccolte possono essere classificate in tre categorie : 


- **Ambiente (ENV) : ** consentono l'identificazione dell'ambiente operativo in cui è stato eseguito il test e mostrano una serie di informazioni sull'ambiente stesso
- **Misure (DAT) : ** rappresentano la risposta numerica ottenuta da tests su specifiche funzionalità del sistema importanti per il corretto funzionamento di Looc.Up
- **Verifiche(VER) : ** risultato dei controlli sui requisiti di sistema. Identificano le condizioni mancanti per il corretto funzionamento di Looc.Up.



### Ambiente (VAR)

Come già detto, nella categoria VAR rientrano tutte le informazioni che possono servire per identificare il sistema sotto test e farsi un'idea dello stato dello stesso al momento dell'esecuzione del programma di controllo.

![LOBASE_093](http://localhost:3000/immagini/LOBASE_038/LOBASE_093.png)
I parametri letti per la definizione dell'ambiente sono i seguenti : 


- **DATA** :  giorno di esecuzione del test
- **ORA** :  ora di esecuzione del test
- **IP** :  indirizzo IP della macchina testata
- **SERVER** :  nome del server Windows
- **USERNAME** :  utente windows
- **HOSTNAME** :  nome mnemorico della macchina nella rete windows
- **OS_NAME** :  nome del SO installato
- **OS_VERSIONE** :  versione del SO installato
- **OS_ARCH** :  architettura SO installato (32 o 64 bit)
- **NR_PROC** :  numero di processi attivi sulla macchina al momento del test
- **MEM_TOT** :  memoria totale installata sulla macchina
- **MEM_FRE** :  memoria disponibile al momento del test
- **SYS** :  sistema AS400 testato
- **JAVA_VER** :  versione della Java Virtual Machine installata sulla macchina



### Misure (DAT)

Nella categoria DAT rientrano tutti i risultati delle misure effettuate sul sistema al fine di valutare le prestazioni di specifici sottosistemi importanto per il corretto funzionamento di Looc.Up. Rientrano in questa categoria le misure sulla velocità della rete, le misure sulle prestazioni della macchina e altre informazioni similari. **Questo tipo di misurazioni ha senso soprattutto quando Looc.Up è installato su un server, all'interno di una cartella condivisa, ed eseguito localmente attraverso un link alla cartella condivisa.. I risultati sono invece poco significativi nel caso di installazione locale di Looc.Up.
Per ognuna delle misure effettuate è prevista la possibilità di visualizzare un commento che consenta di interpretare correttamente il risultato ottenuto (ad esempio evidenziare i valori ritenuti anomali)

![LOBASE_094](http://localhost:3000/immagini/LOBASE_038/LOBASE_094.png)
In dettaglio, le misure effettuate sono le seguenti : 


- **PING** :  tempo di risposta (in msec) del server Windows di riferimento
- **LIBS_TIME** :  tempo di caricamento (in msec) delle librerie Java necessarie a Looc.Up
- **FIL_LOA** :  velocità di caricamento (in Mb/sec) files da server Windows. Serve per valutare la velocità della connessione di rete.


### Verifiche (VER)

Nella categoria VER rientrano tutti i risultati delle verifiche effettuate sui prerequisiti richiesti dal sistema per l'installazione di Looc.Up. Ogni controllo va a testare un singolo prerequisito tra quelli richiesti da Looc.Up in modo da evidenziare in maniera chiara la presenza sul sistema di condizioni non adatte al funzionamento del client. Per ognuna delle verifiche fallite viene inoltre mostrato un suggerimento sintetico che descrive l'eventuale azione correttiva o rimanda alla documentazione specifica per il problema rilevato.

![LOBASE_095](http://localhost:3000/immagini/LOBASE_038/LOBASE_095.png)
In dettaglio, le verifiche effettuate sono le seguenti : 


- **JVM_VER** :  compatibilità della JVM installata sul sistema
- **JVM_BITS** :  compatibilità architettura della JVM (numero di bit)
- **OS_VER** :  controllo sulla versione del sistema operativo
- **MEM_VER** :  controllo sulla quantità di memoria disponibile
- **FS_VER** :  controllo autorizzazioni di accesso al file system
- **AS4_AS4** :  controllo raggiungibilità sistema AS400
- **AS4_CEN** :  controllo raggiungibilità servizio CENTRAL su sistema AS400
- **AS4_DTQ** :  controllo raggiungibilità servizio DATAQUEUE su sistema AS400
- **AS4_IFS** :  controllo raggiungibilità servizio FILE su sistema AS400
- **AS4_COM** :  controllo raggiungibilità servizio COMMAND su sistema AS400
- **AS4_SIG** :  controllo raggiungibilità servizio SIGNON su sistema AS400



