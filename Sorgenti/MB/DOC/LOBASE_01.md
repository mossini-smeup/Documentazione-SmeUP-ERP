# Schemi Applicativi
## Schema generale
![LOCBAS_041](http://localhost:3000/immagini/LOBASE_01/LOCBAS_041.png)Lo schema illustra l'architettura generale di LoocUp : 

 * LoocUp in qualità di interfaccia grafica si pone come strumento di comunicazione tra l'area utente, evidenziata in basso al di sotto della linea tratteggiata verde, e le macchine in alto. Il dialogo con i server avviene attraverso la chiamata di programmi RPG detti "servizi" incaricati di ascoltare ed elaborare  le richieste. Il protocollo di comunicazione è simile a quello di un Browser; è costituito infatti dalla richiesta di un servizio (invece che di una pagina Web) e dal passaggio di parametri, attraverso stringhe.
 * La risposta del Server, in genere un file XML, contiene dati da visualizzare. Le informazioni grafiche delle pagine risiedono per di più sul client. Si ottiene in
questo modo una comunicazione "all'osso" :  vengono trasmessi solo dati secondo i più recenti standard di comunicazione client-server.
 * Lo strumento principale di comunicazione con l'esterno è l'Interfaccia Video/Tastiera :  LoocUp fornisce strumenti molto potenti di manipolazione dei dati, tools di visualizzazione ed organizzazione, editor e programmi guida come è meglio illustrato nella sezione di Interfaccia Grafica.
 * Esiste anche un altro aggancio al mondo esterno, che è costituito dai Listener attivabili a piacimento. Si tratta di programmi ascoltatori di eventi, in grado cioè di "accorgersi" di azioni che vengono eseguite su periferiche come telefono/fax/scanner o un'altra qualsiasi apparecchiatura richiesta dall'utente o semplici cartelle. L'evento può essere scatenato anche dai server pertanto si può affermare che i Listener sono in grado di percepire sia eventi esterni che interni al sistema.
 * Gli eventi  o le azioni dell'utente su tastiera vengono raccolti e direzionati dal modulo base al modulo di comunicazione che smista le richieste direttamente al server AS400 master, oi ai Server esterni, o al gestore delle funzioni interne qualora la richiesta inoltrata non esiga informazioni remote, ma possa essere interamente soddisfatta sul client. E' il caso quest'ultimo di richieste di riorganizzazione di dati già visualizzati o di semplici calcoli sui medesimi. Le richieste possono però anche essere spedite verso server diversi dal master e raggiungibili tramite Rete. Essi possono svolgere incarichi particolari come contenere  archivii, gestire servizi di posta, o altri servizi di second'ordine. Anche in questo caso, come per i Listener, il cliente può agganciare all'architettura un proprio server predisposto a specifiche funzionalità

## Modulo di comunicazione
![LOCBAS_032](http://localhost:3000/immagini/LOBASE_01/LOCBAS_032.png)Costituito da un pacchetto di classi java, il modulo di comunicazione, all'interno del modulo base, ha il compito di smistare le richieste effettuate da esterni e di pilotarne le risposte. La F() viene passata direttamente al modulo di trattamento delle funzioni che provvede a completare, elaborare la richiesta e riformulare la risposta. Vedi anche "Aspetti generali", "Richiamo di una funzione"

La fase di elaborazione consiste anche di una fase di smistamento della F(). Il formato della richiesta F() infatti contiene le informazioni per capire il destinatario che dovrà elaborarla. Se si tratta di funzioni di manipolazione, di visualizzazione di dati già presenti sul client non occorre risalire fino al server master e la richiesta perciò verrà deviata al "Gestore server interno" ossia al client stesso che contiene un pacchetto di servizi java specifici. Le funzioni di questo tipo si distinguono perchè hanno definito una costante di lancio 'INT' nel formato :  sono del tipo F(INT;...;...).

La richiesta può anche essere deviata quando su server remoti, come ad esempio quando si vuole visualizzare una pagina web oppure si cercano informazioni depositate su server diversi dal Master; In questo caso il modulo che si sobbarca l'onere è il "Gestore server esterni" e la funzione chiamante contiene una voce 'SERVER()' con specificato l'indirizzo del server di destinazione della richiesta.

Se  la richiesta non subisce reindirizzamenti si assume che il server master la debba soddisfare pertanto essa viene depositata sulla coda di ingresso all'AS400 Master, coda creata appositamente per ogni sessione... ogni sessione cioè ha la sua specifica coda di ingresso e di uscita dal Server. L'AS400 ha una serie di servizi incaricati di gestire le richieste e di indirizzarle verso altri servizi o programmi che producono in uscita un file XML. L'architettura come si vede è analoga a quella di un WebApplicationServer... e la comunicazione di informazioni avviene attraverso stringhe e file XML. La maggior parte delle informazioni grafiche stanno sul client, il passaggio di informazioni si limita al passaggio di dati.

Le informazioni in uscita vengono depositate su una coda specifica e il programma di Gestione delle code provvede a reindirizzare la risposta all'utente... se la risposta è un messaggio di errore, un avviso o una richiesta di conferma il "Gestore Messaggi" espone una finestra di dialogo con l'utente e poi reimmette nel flusso la richiesta con le direttive indicate dall'utente per il caso.

Qualora la funzione richieda l'immissione di più dati viene fatta una chiamata all'emulatore 5250 ed esposta una form da compilare dall'utente... una volta dato invio dopo i controlli di formato e di obbligatorietà la richiesta viene reimmessa nel flusso.

Se la risposta non contiene messaggi o non richiede ulteriori informazioni il file xml viene passato al modulo base che provvede a visualizzarlo nell'opportuno modulo grafico.

## Interfaccia Grafica
![LOCBAS_033](http://localhost:3000/immagini/LOBASE_01/LOCBAS_033.png)L'interfaccia grafica in connessione diretta con il modulo base è costituita da un pacchetto di programmi java/delphi e di componenti grafici che forniscono strumenti di dialogo con l'utente, di visualizzazione e organizzazione dei dati.
Si possono individuare all'interno del pacchetto tre macro partizioni : 
 * la prima riguarda il contenitore detto "scheda" e le finestre grafiche dell'emulatore 5250;
 * la seconda riguarda i componenti grafici specifici, tabelle, gantt, grafici ecc... che "riempiono" le sezioni della struttura. E i tools di manutenzione  della scheda.
 * il pacchetto di programmi di gestione dell'emulatore 5250.

- La parte riguardante il contenitore è scritta in delphi e, per poter dialogare con il modulo base scritto in java, necessita di un "gestore di comunicazione Socket" che faccia da allacciamento tra i due linguaggi. La scelta di delphi è giustificata dalla rapidità e versatilità dei suoi componenti grafici. Il modulo Delphi a sua volta si suddivide in due sottomoduli;
 -- Modulo Smetray (gestore di schede) che fornisce il componenente contenitore, annidabile, cioè la scheda. Per la definizione della struttura   LoocUp mette a disposizione un'editor di facilissima comprensione, un tool di controllo sintattico e un wizard;
 -- Modulo Smeviclt (emulatore SDA) che riproduce i display file DSPF definiti su AS400.
 - Looc.up fornisce diversi strumenti grafici di rappresentazione e manipolazione delle informazioni. Sono tutti componenti java e perciò non hanno problemi di allacciamento con il modulo base. E' possibile facilmente introdurre nuovi componenti qualora il cliente ne facesse esplicita richiesta. Di seguito l'elenco dei componenti grafici disponibili : 
 * EXA  Grafico
 * EXB Matrice
 * EXU    Matrice modificabile
 * GNT    diagramma di Gantt
 * GND diagramma di Gantt/distinta
 * G30 questionario
 * HTM Browser
 * INP Input panel
 * MAP Immagine attiva
 * STR Stella
 * TRE albero
 * TRA albero con tab
 * TRG albero con griglia
 * GRP grafo
 * DOC  documento
 * CHT chart

A questa sezione appartengono anche l'editor di creazione e manutenzione della scheda.
Per maggiori dettagli riguardo ai componenti grafici consultare la scheda 'Componenti grafici e logici'.
 * Emulatore   si tratta dei programmi di emulazione di AS400, meglio descritti nel Modulo gestore 5250 e in stretto dialogo con il modulo Smeviclt.

## Gestore Listener
![LOCBAS_034](http://localhost:3000/immagini/LOBASE_01/LOCBAS_034.png)La comunicazione con il mondo esterno non avviene solo tramite interfaccia grafica... LoocUp fornisce oltre all'ambiente grafico altri strumenti di ascolto di eventi e questi sono appunto i "Listener" o "ascoltatori di eventi".

Le gestione di questi oggetti avviene tramite il servizio java JA_00_16 che ha il compito di inizializzarli, attivarli e tramite il quale possono essere eseguite interrogazioni. La dichiarazione dei listener è codificata nello script EDT_CLO nel file dei configuratori SCP_CFG e l'attivazione avviene con l'avvio di LoocUp. Il sistema provvede a creare tanti threads, ossia processi che condividono parallelamente l'accesso al processore, quanti sono i listener definiti nello script... ciascun thread si aggancia ad una cartella o ad una periferica ed esegue periodicamente dei controlli, detti "ping", sullo stato della medesima studiandone gli eventi. Nel caso si verifichi un evento significativo, il listener provvede a segnalarlo al "Gestore degli eventi" che costruisce una generica funzione F() analoga a quella prodotta dall'interfaccia grafica e la immette nel flusso verso il modulo base. La richiesta poi segue il flusso regolare delle funzioni richiesta F().

Esiste una procedura specifica per i test agganciata ad una cartella... l'evento scatenato da una qualsiasi periferica può essere simulato immettendo in tale cartella la sua decodifica.

## Server AS/400
![LOCBAS_035](http://localhost:3000/immagini/LOBASE_01/LOCBAS_035.png)Il Server Master AS400 è il principale responsabile delle richieste effettuate dall'utente. Esso lavora con una serie di servizi "ascoltatori" che, sintonizzati sulle code, si fanno carico delle richieste e le smistano ad altri servizi detti "esecutori" che hanno il compito di soddisfare la richiesta.

Ma procediamo con calma...

All'avvio della sessione, LoocUp si connette con il server AS400 e genera due code una in ingresso ed una in uscita specifiche per la sessione corrente. L'AS400 da parte sua attiva un servizio di risposta il JAJACO che è il  Motore di comunicazione verso la parte client per le  applicazioni client/server Java e che attiva un pacchetto di lavori batch LO_S incaricati di ascoltare l'emulatore e un pacchetto di lavori batch LO_C incaricati di ascoltare servizi.
La natura delle richieste che pervengono al server può essere infatti di due tipi : 

1. richieste dell'emulatore

2. richieste di servizi specifici

Nel primo caso trattandosi di un'emulazione dell'AS400 si verifica l'apertura di una transazione ossia di una sequenza di programmi in catena che eseguono istanze e che si pongono in diretto dialogo con l'utente.

Nel secondo caso il pacchetto di lavori batch LO_C attiva il servizio  JAJAS1 che smista la richiesta secondo tre diverse possibilità : 

a) transazione (è il caso della schedulazione della produzione per esempio) la funzione cioè richiede l'apertura di una sequenza di programmi in catena, come nel caso precedente;

b) La richiesta è un semplice ping, ossia un avviso da parte del client che la sessione è ancora aperta;

c) richiesta di uno specifico servizio; in questo caso il jajas1 si comporta come una Servlet e attiva il servizio indicato nella F(); questi a sua volta può necessitare di più informazioni o girare ad altri programmi l'istanza ed attivare una transazione o soddisfare da sè la richiesta. Ciascun servizio può poi chiudersi liberando la memoria oppure conservando lo stato delle variabili attraverso l'indicatore LR/RT di return. A ciascun servizio può infine essere agganciato un log che fornisce informazioni su prestazioni o su azioni del medesimo.

Dal punto di vista tecnico è prevista la funzionalità UP SER utile per eseguire test di debug sul servizio. Può essere agganciata a livello di coda, modalità 'JS', o a livello di servizio, modalità 'JD' consentendo così di eseguire test a più livelli del ciclo.

# Richiamo di una funzione
![LOCBAS_031](http://localhost:3000/immagini/LOBASE_01/LOCBAS_031.png)Il processo di trattamento di una funzione può essere suddiviso in tre fasi fondamentali : 

- Fase di composizione della 'request'
- Fase di esecuzione della 'request'
- Fase di composizione della 'response'


### Composizione della Request
In questa fase avviene il completamento dei dati mancanti della request o la sostituzione delle macro presenti nella richiesta.
Si suddivide in tre sottofasi : 
 * **Gestione degli alias**
 * **Gompletamento variabili di tipo -**
 * **Gestione Parametri di setup**

### Gestione degli alias
Al fine di facilitare la chiamata di una funzione, in LOOC.up è prevista la gestione di chiamata mediante ALIAS. L'obiettivo è quello di poter definire una sintassi di scrittura più facile da memorizzare e scrivere da parte dell'utente. Per fare un esempio posso permettere all'utente di individuare tutte e sole le azioni di menù che contencono la parola "Provvigioni" chiedendo di digitare :  "Cerca Provvigioni AZI". Se invece voglio far trovare i fornitori che contengono "OFFICINA" nella ragione sociale basterà digitare "Cerca OFFICINA FOR"

### Accesso
Gli ALIAS sono attivi nella "Barra di comando" accessibile da qualsiasi mappa di LOOC.up premendo F21.

### Definizione
Nella parte destra della barra una icona permette di accedere alla visualizzazione e gestione degli ALIAS stessi.
Gli ALIAS sono definiti in un membro si SCP_CLO di nome ALIAS il cui accesso è consentito dalla scheda sopra descritta.
Se non sono trovati nel membro di cui sopra, vengono utilizzati quelli del file presente nella direttory del programma nella sottocartella \LOOCUP_DAT\SHO

### Sintassi della stringa
Le parole che seguono l'ALIAS sono utilizzate come parametri che sostituiscono nell'ordine le variabili definite nella struttura base della funzione.
Il separatore della variabili è il carattere bianco. Se si vuole passare una stringa contenente caratteri bianchi la si deve racchiudere fra apici (")

### Nota
Nella composizione della stringa dell'alias prestare attenzione agli spazi perchè hanno rilevanza nella composizione della stringa.

### Completamento variabili di tipo -
Una funzione definisce in modo univoco tutte le informazioni per ottenere un XML di ritorno. Tali informazioni sono passate al servizio secondo una sintassi convenzionale definita in
SME.up.
E' possibile scrivere la funzione in modo tale che l'utilizzatore possa inserire una qualsiasi informazione in un formato richiesto. Tale obiettivo si ottiene inserendo il carattere - all'interno della funzione. Ciò permette in pratica una micro-configurazione della funzione stessa e si utilizza quando si devono chiedere pochi parametri e non si prevede alcun controllo di congruenza fra le diverse risposte. Diversamente si dovrà utilizzare il "setup di funzione" descritto più avanti.

### Sintassi di un parametro da richiedere
Il carattere - può essere seguito da parametri che ne condizionano tipo e modo della richiesta secondo la sintassi seguente : 
-(O/F;Default;Tipo Oggetto;Descrizione;C/U) che nell'ordine indicano : 
 * O=Obbligatorio. Diversamente viene accettato anche il carattere bianco
 * Default = Luogo di default in cui cercare
 * Tipo oggetto = Eventuale tipo oggetto da richiedere
 * Descrizione = Testo che appare vicino alla richiesta
 * C=Controllare, U=Non Controllare. Default C

**Esempio di funzione** : 
F(EXD;*SCO;) 1(;;) P(Stringa(-) Dove(-(O;BR;TAB£A;Contesto)))
Sostituisce la stringa e chiede un codice di applicazione obbligatorio assumendo BR.

A(LOIP_01;RIC;EMU) P(Str(-(F;;**Stringa;Stringa)) Whe(-(O;CF;TAB£A;Stringhe selezionate)) )
La funzione nel partire presenta due finestre consecutive in cui chiede prima una stringa(di tipo facoltativo) da ricercare e poi l'oggetto di tipo TAB£A in cui cercare assumendo CF come default. Nel presentare la finestra di ricerca mostra inoltre la stringa "Stringhe selezionate".

F(EXD;*SCO;) 1(CN;CLI;-(O))
Chiedo il cliente per cui presentare la scheda

### Estensione sintassi - Da valutare
La sintassi -(H[;Default]) consente di definire paramerti che se non passati non vengono richiesti.
Mediante il suffisso -P viene chiamato l'alias senza parametri.

### Nota
Nel caso di completamento di oggetti la sintassi utilizzabile si limita ai primi due parametri.

### Gestione Parametri di setup
**Obiettivi**

- Configurare il campo P prima della chiamata del servizio
- Identificare il setup da passare nel tag Setup/Program/MODULO dell'XML restiuito dal servizio chiamato.


### Esistente ad ottobre 2007
Versione 2.
Supporta, per compatibilità con il passato il MODA e il MODB della versione 1.
La versione definitiva sostiuirà la versione 1.

### Versione 2
 T(La nuova gestione dell'SP consente di : )
- visualizzare un questionario con una configurazione associata
- specificare quale configurazione caricare
- la configurazione può essere modificata, visualizzata non modificabile oppure non essere visualizzata.


 T(Significato dei parametri del campo SP : )
- TQST :  tipo questionario
- KQST :  codice questionario
Consentono di identificare il questionario. Se il tipo di questionario è U- e se si desidera che la configurazione sia modificabile, va definita la sua struttura utilizzando i parametri SCPSRC e SCPSEC. Il rpimo definisce lo script da cui estrarre le sezioni, il secondo specifica le a la sezione da utilizzare. Nel caso di sezioni vanno indicate separate da ";".
- CFG :  identifica la configurazione. Si può specificare o l'IDOJ oppure le 3 chiavi del MEDE, separate da ";". Opzionalmente si può indicare che si desidera che venga effettuata la risalita aggiungendo un ";1" dopo  l'ultima chiave.
- VM :  modalità di visualizzazione al lancio ella funzione : 
-- W :  viene mostrato un setup con la configurazione indicata o quella di default se non si specifica nulla. La configurazione è modificabile.
-- R :  come sopra ma la configurazione NON è modificabile
-- H :  viene letta la configurazione indicata o quella di default e fornita al servizio nel campo P.
- DOCSER :  consente di indicare, come sorgente delle domande, la documentazione del servizio (file DOC_SER)


### Esempi
Si possono vedere nella scheda degli esempi di Loocup (My Loocup->Esempi), Sezione "Per gruppo", Capire Loocup, Funzioni con Interazione, Configurazione al lancio.
C'è sia un esempio secondo la sintassi della versione 2 che nella sintassi della versione 1.

Di seguito vediamo le F in modo esplicito.
### Configurazione da script creato ad hoc
Lo script va definito, secondo al solita sintassi dei questionari, in un apposito mebro del file SCP_CFG.
F(TRE;*LAP;) SP( TQST(L-) KQST(GRA_G30) CFG(**;**;**) VM(W) )

### Configurazione da script filtrato
In questo caso il questionario viene definito basandosi su un insieme di sezioni di un'altro questionario. Il questionario di base è un membro del file SCP_CFG.
Nell'esempio che segue
F(TRE;*LAP;) SP( TQST(U-) KQST(FRM.REP) CFG(**;**;**;1) VM(W) SCPSRC(EDT_SCH)   SCPSEC(S.FRM.DOC;S.FRM.FMT;S.FRM.COV;S.FRM.IDX,S.FRM.HEA;S.FRM.FOO;S.FRM.MOD;S.FRM.LAY;S.FRM.STY))
apprezziamo le seguenti definizioni : 
Tipo questionario è U-
Codice Questionario FRM.REP
la configurazione caricata è quella di default per tutti gli ambienti e utenti. La risalita è abilitata, cosa superflua in quanto abbiamo richiesto la configurazione più generica di tutte.
Il modo di visualizzazione è in modifica
Il questionario di filtro è EDT_SCH
Le sezioni che compongono il questionario sono :  S.FRM.DOC;S.FRM.FMT;S.FRM.COV;S.FRM.IDX,S.FRM.HEA;S.FRM.FOO;S.FRM.MOD;S.FRM.LAY;S.FRM.STY.

### Versione1
Gestisce tre modalità di gestione del parametro SP() note come MODA, MODB e MODS per la configurazione del campo parametro e il richiamo di un setup da associare ad una funzione.

### Esecuzione della Request
Una volta composta la funzione attraverso la fase precedente si hanno tutti gli elementi necessari per poter passare alla fase di esecuzione. La fase di esecuzione termina con la produzione del contenuto restituito a programma su file xml.
La prima questione che si pone a questo livello è chi sia il destinatario della F()  A()  R() incaricato di eseguirla.

### Richieste di tipo INT
Se specificato INT nelle informazioni di lancio (F(INT;...;...))  significa che la richiesta non necessita di informazioni remote per poter essere risolta... tutte le informazioni necessarie sono già presenti sul client. In questo caso quindi è a disposizione un modulo di servizi java detto 'Modulo Server Interno' che si incarica di risolvere la richiesta sul client. Essi emettono un risultato in XML analogo a quello dei servizi su server remoti.

### Richieste di tipo SERVER
Se tra le voci di richiesta compare una voce SERVER() con specificato un nome di server della rete la richiesta non viene spedita al server master di default ma viene smistata a tale server 'slave' che conterrà i servizi di risposta. Tali server vanno configurati sul setup di default si veda la documentazione relativa.

### Richiesta su server Master
Se la richiesta è una F() e non ricade nelle casistiche precedenti, viene girata direttamente al server master
Se si tratta invece di una A() (richiesta di programma) o di una R() può darsi che venga attivato l'emulatore 5250 e si richieda un'interattività con l'utente che rigenera request e replica quindi il processo da capo.

### Composizione della Response
La fase di composizione della response consiste in sostanza nella composizione dell'xml di contenuto con il setup di trattamento dei dati (contenente le informazioni relative al 'trattamento' dei dati :  modalità di visualizzazione, organizzazione delle informazioni ecc...).
Questo processo in genere è gestito interamente dal servizio che oltre a generare il contenuto provvede anche ad agganciare un tag di setup in coda all'xml.
Attualmente il setup di trattamento può anche essere impostato direttamente sulla funzione F() di lancio tramite configuratore.
Si presentano pertanto due casi : 

- Setup di trattamento non impostato su F() : 
-- il setup generato è completo :  l'xml può essere agganciato al componente
-- il setup generato è incompleto :  contiene cioè ancora richieste F() con SP()... in questo caso l'xml va ancora sottoposto a gestore setup che provvede ad espletare le sezioni incomplete (i dati non cambiano);
- Setup di trattamento impostato su F() :  prevale sul setup generato dal servizio e lo sostituisce integralmente.

A fine di questo processo il risultato consiste in un file xml con setup di trattamento eseguibile.

## Funzioni
In Looc.up chiamiamo funzione la stringa che in vari modi viene associata alla richiesta di azione da parte dell'utente (un clic del mouse, un comando ecc).
Il modulo di comunicazione verifica la stringa, la indirizza opportunamente al server, si pone in attesa della risposta e la fornisce al componente grafico opportuno.

### Chi chiama la funzione
Normalmente la funzione viene richiamata per attivare un nuovo passo di colloquio (vedi gestione dello STACK in LOOC.up). Ad esempio : 
- una chiave di menù
- associata al tasto destro di un oggetto
- associata ad un tasto funzionale.

E' però possibile che una funzione sia richiamata da un componente per sue esigenze. In tal caso sarà cura del componente stesso gestire opportunamente l'informazione fornita. Ad esempio
- emissione di una matrice in una sezione di una scheda
- popup delle funzioni di un oggetto
- esito del controllo di una tabella compilata.

### Tipi di funzione
Abbiamo diversi tipi di funzione. La funzione è caratterizzata dal suo primo carattere e abbiamo : 

### F Richiesta di servizio
E' la funzione più importante. Si chiede ad un programma AS (servizio) di costruire un file XML e di renderlo disponibile ad un componente di Looc.up capace di rappresentarne il contenuto.

Vedi "Funzioni di base", "Lato server", "Programmi di servizio Loocup".
**Struttura**
F(Componente;Servizio;Funzione.metodo) 1(Tipo;Parametro;Codice) 2(...) 3() 4() 5() 6() P(Parametri specifici).
**Esempi**
F(EXD;*SCO;) 1(CN;CLI;000001)

## M Richiamo di una chiave di menù
Trova la funzione associata ad una chiave di menù. La funzione associata può essere : 
- Un programma eseguito dal componente di emulazione
- Una qualsiasi funzione di tipo F
**Struttura**
M(EMU;ESE;AZI) 1(TA;MEAmenù specifico;Codice azione)
**Esempi**
M(EMU;ESE;AZI) 1(TA;MEABR;0101)

### A Esecuzione di un programma con eventuale risposta
Chiama un programma AS (Che nella terminologia SME.up è "Funizzato"). Se la funzione è richiamata da un componente grafico, alla fine del programma, il componente riceve il risultato (£FUND2) e ne gestisce il contenuto.
**Struttura**
A(Programma;Funzione;Metodo) 1(Tipo;Parametro;Codice) P(Parametri specifici)
**Esempi**
A(B£FU01X;CAL;) 1([1 : 1 : 2];[1 : 3 : 10];[2]) P(CDL000031)

### R Esecuzione di un programma con esecuzione della funzione contenuta nella risposta.
Come per la funzione di tipo A ma la risposta contiene sempre una funzione che viene
intercettata dal componente di comunicazione di Looc.up e richiamata.
Ad esempio chiamo un programma RPG che decide dinamicamente quale funzione richiamare.
**Struttura**
R come primo carattere, poi come A
**Esempi**
R(S5SER_01C;SCH;OGG)

### Come determinare le funzioni chiamate in Looc.Up
Per scoprire quale funzione viene chiamata per ottenere una certa schermata di Looc.up si può : 
- Cliccare sulla barra dei menù "Servizi", poi "Funzione Corrente"
- Dalla voce di menù di Looc.up, cliccare con il tasto dx, "Apri Come" / "Funzione Associata"
In entrambi i casi si apre la schermata che dettaglia la funzione scelta :  la stringa che appare sotto "Anteprima funzione composta" è la funzione desiderata.

**NB** :  Nel caso di schede con più sezioni il metodo Servizi/funzione corrente porta alla funzione associata alla chiamata dell'intera scheda.
Se si desidera determinare la funzione chiamata per ottenere una subsezione è necessario : 
- cliccare sul tab della subsezione con il tasto dx, selezionare "Visualizza come..." per aprire una nuova finestra con la chiamata alla singola subsezione
- procedere con Servizi/funzione corrente


### Funzione come oggetto(sv)
La funzione è un oggetto tipico di Looc.up quindi potrà essere posta ad esempio come domanda di un questionario.

# Gestione dei server esterni
## Schema di riferimento
![LOCBAS_036](http://localhost:3000/immagini/LOBASE_01/LOCBAS_036.png)LoocUp oltre ad essere connesso con il server master AS400, consente di definire un pacchetto di server alternativi, incaricati di compiere specifiche funzionalità, anche sostitutive a quelle fornite dal master. Questo permette di costruire un sistema molto articolato e di agganciare anche più applicativi sul lato server purchè si rispettino i protocolli di comunicazione.

Le gestione dei server esterni avviene tramite il servizio java JA_00_17 che ha il compito di inizializzarli, attivarli e con cui possono essere eseguite interrogazioni. La dichiarazione dei server esterni è codificata, come per i listener, nello script EDT_CLO nel file dei configuratori SCP_CFG e l'attivazione avviene all'avvio di LoocUp. Il sistema provvede a creare tanti threads, ossia processi che condividono parallelamente l'accesso al processore, quanti sono i servers definiti nello script... A differenza dei Listener stavolta la richiesta di utilizzo di un server esterno è inoltrata dal modulo base vesro il Gestore dei servers esterni... tale richiesta contiene specificatamente il codice del server destinatario ed è perciò distinta dalle altre normali richieste. Sui server devono essere previsti degli opportuni servizi di ascolto in grado di trattare la richiesta e di generare l'XML di risposta. La funzione segue quindi il regolare flusso di una generica funzione.

Esiste anche in questo caso come per i listener una procedura specifica per i test agganciata ad una cartella... la risposta del server ad una specifica richiesta può essere simulata immettendo in tale cartella la sua decodifica.

## Approfondimenti
In Looc.up e' possibile gestire server esterni all'iSeries che ritornino informazioni compatibili con il protocollo del client grafico, che rispondano quindi a chiamate di tipo F() e che ritornino XML di tipo EXB,TRE e degli altri componenti implementati.
L'utilizzo di server esterni si rende necessario qualora si intenda integrare applicazioni non residenti su iSeries. I server aggiuntivi vengono caricati al momento dell'avvio di Looc.up. Il server e' un oggetto di tipo V3/CSE.

### Sintassi della chiamata
L'indirizzamento di un server avviene a livello di funzione tramite il tag SERVER() .

F(;;) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P() SERVER(xx)
dove xx referenzia il codice server in SCP_CLO/xx

### Definizione dei server
La definizione di un server aggiuntivo viene configurata nel file SCP_CLO/xx con la seguente sintassi XML : 

### Esempio
>.  <Servers>
.       <Server Cod="00" Txt="Local Add="127.0.0.1" Param="" Protocol="JAVA"/>
.       <Server Cod="01" Txt="FXWord" Add="ufidi" Param="path=/xml/feed.asp" Protocol="HTTP"/>
.  </Servers>


Nel precedente esempio viene configurato il server di FXWord tramite protocollo HTTP. Il client grafico viene considerato anch'esso un server di codice 00

### Protocollo di chiamata
Per venire incontro alle molteplici forme di connessione fra sistemi, sono stati sviluppati differenti protocolli di comunicazione, sia locali che remoti.

 T(Protocolli disponibili)
- HTTP
- HTTPS
- JAVA
- SOCKET


### Documentazione dei servizi esterni
Per rendere uniforme la documentazione dei servizi, si e' scelto di portare in documentazione attiva anche i servizi implementati da server esterni con le seguenti regole per la nomenclatura : 
JA_xx_yy
xx = codice del server
yy = progressivo servizio

I servizi locali avranno  nome JA_00_yy.
I servizi di FXWord avranno nome JA_01_yy.

Da questa visione di insieme LoocUp appare come un ponte di comunicazione malleabile ed estendibile in maniera molto libera dall'utente sia all'interno che all'esterno; Costituisce pertanto un potente strumento gestionale adattabile a esigenze diversificate.

# Comunicazione Client Server
In questa parte della documentazione vengono analizzate le varie fasi di comunicazione tra client Looc.Up e server ed affrontate principalmente tre tematiche : 

- le fasi di **connessione al server**
- la fase di scambio di **messaggi XML**
- l'apertura di una **sessione**  di **emulazione 5250**

## Fasi di connessione al server
### Connessione al server
Alla partenza del client Looc.Up per connettersi al server AS400 è necessario indicare : 

- l'indirizzo del server a cui connettersi (172.16.2.34 per esempio)
- l'utente con cui connettersi (mioNomeUtente)
- la password (miaPassword)
- (opzionalmente) il codice dell'ambiente (0010)

Questi parametri possono essere indicati nel momento in cui si chiama l'applicazione Loocup.jar o Loocup.exe (per es Loocup.exe 172.16.2.34 mioNomeUtente miaPassword 0010) o altrimenti riempiendo i campi che si presentano avviando l'eseguibile di Loocup senza indicare altri parametri. (E' ovvio che è possibile coniugare problematiche di comodità con quelle connesse alla sicurezza indicando solo alcuni di questi parametri, per esempio l'indirizzo del server e il nome utente tralasciando la password e il codice dell'ambiente ad una fase successiva).
L'applicazione, una volta ottenuti i parametri in uno dei due modi sopra indicati, contatta  il server tramite la libreria Java **JT400** (http://jt400.sourceforge.net/) creando una **connessione socket**. Tale libreria gestisce anche le successive fasi della comunicazione.

_7_NOTA :  per poter usufruire dei servizi AS400 avanzati (es. gestione stampe o lavori) è necessario che la connessione avvenga con il nome dell'AS400 e non l'indirizzo. Se l'AS400 non è riconosciuto dalla rete con un nome va modificata la tabella host del pc

### La libreria JT400
La libreria JT400 è una libreria che fornisce una serie di API che facilitano la connessione e l'esecuzione di comandi AS/400 all'interno di applicazioni scritte in Java. In particolare tale libreria, una volta instaurata una connessione verso il server, fornisce tre tipologie di chiamata  : 

- chiamata ad un programma/procedura AS/400 tramite **PGMCALL**;
- la creazione di una coda dati verso o dal server in cui passare i dati da e verso il server tramite **QUEUE**;
- la gestione di comandi di gestione del sistema tramite **SYSTEM** (comandi di gestione delle stampe, dei lavori....).

### Inizializzazione delle code e scelta dell'ambiente
Il server AS400 una volta ottenuta la richiesta di connessione chiama l'applicazione JAJAC0 che, come risultato della connessione, ritorna un**codice di sessione**.
Il client a questo punto attiva  due code verso il server : 

- ECTS + codice sessione (**E**xtended **C**lient **T**o **S**erver) per la comunicazione dal **Client** al **Server**.
- ESTC + codice sessione (**E**xtended **S**erver **T**o **C**lient ) per la comunicazione dal **Server** al **Client**.

Una volta che sono state create le code di comunicazione il client richiede al server la lista degli ambienti a cui può accedere. Se gli ambienti sono più di uno Looc.Up mostra all'utente la lista permettendogli di scegliere l'ambiente. Una volta che il server conosce l'ambiente da associare all'utente esso carica le librerie associate all'ambiente scelto (il server chiama JAJAC0 con messaggio "DATSES" Funzione "CON" e ambiente scelto).

### Inizializzazione dell'ambiente di partenza Looc.Up
Il client dopo aver scelto l'ambiente sulla coda ECTS incomincia la prima vera comunicazione verso il server. Tramite una funzione FUNIZZATA richiede i dati di setup al server. Il server risponde inviando un XML di setup che contiene : 

- Un elenco di autorizzazioni;
- Le stringhe delle voci del client nella lingua prescelta;
- I nomi degli elementi del menù;
- Le voci di pop-up dei menù contestuali;
- Una lista di path di risorse ( al momento come risorse sono state definite le immagini e le icone);
- Una lista di variabili;
- Una funzione di partenza iniziale.

Per ulteriori informazioni sulle fasi di inizializzazione si veda "Funzioni di base", "Lato client", "Configurazione" : 
- [Configurazione - Aspetti base](Sorgenti/MB/DOC/LOBASE_033)
Una volta che il client ha analizzato il messaggio XML iniziale chiama i vari componenti e schede e dopo aver chiamato la funzione di partenza iniziale è pronto ad essere utilizzato.

## La fase di scambio di messaggi XML
Durante l'utilizzo del client Looc.Up l'utente interroga varie volte il server per richiederne le funzioni. Le chiamate verso il server avvengono tramite delle funzioni funizzate.

documentazione in completamento
-------------------------------------------
  - Sceglie una qualsiasi funzione

### Looc.up
In base alla funzione scrive sulla coda opportuna

### AS/400
Distingue i seguenti casi
 * Emulazione
 ** Sulla coda ICTS ricevo una chiave di menù
 ** Ricavo il programma e lo richiamo
 ** Il programma chiamato fornisce l'output sulla coda invece che sul video
 * Funzione
 ** Sulla coda ECTS ricevo una funzione
 ** Ricavo il programma dalla tabella JAT in base alla funzione
 ** Chiamo il programma e fornisco l'XML

## Richiesta di collegamento da parte del CLIENT
### Utente
 * Chiede l'esecuzione di Looc.up con un clic su icona di Loocup.jar o Loocup.exe  che puo essere sul server oppure sul client
 * Immette identificativo del SERVER (IP AS400) / UTENTE / PASSWORD
### Looc.up (Componente COM di comunicazione)
 * Legge gli ambienti attivi per l'utente (Oggetto IU per l'utente)
 * Se più di un ambiente (e non indicato in collegamento) richiede la scelta ambiente altrimenti assume l'unico ambiente presente
### AS/400
 * Imposta le librerie in base all'ambiente
 * Chiama JAJAS0SB con funzione "CON" e metodo "MAS"
 * Recupera il nome del lavoro in esecuzione (Es.abcdef)
 ** Crea la coda MSTCabcdef
 ** Riceve sulla coda MSTCabcdef il numero di tale lavoro (Es.123456)
 ** Il codice ricevuto diventa >Numero della connessione = 123456
 ** Sottomette il lavoro **LO_Ehhmmss - Gestore delle funzioni grafiche** Il nome è formato dal prefisso LO_E + l'ora + i minuti + i secondi
 *** **>**JOBQ da tabella UI1 (Consigliato BATCH)
 ** crea diverse nuove code dati nella libreria SMEUPUIDQ : 
 *** **>**ECTS123456 - Extended    Client To Server
 *** **>**ESTC123456 - Extended    Server To Client
 *** **>**ICTS123456 - Interfaccia Client To Server (n per ora tre)
 *** **>**ISTC123456 - Interfaccia Server To Client (n per ora tre)
 * Termina JAJAS0SB e JAJAC0 restituendo il nome della connessione

### Stato
 * I programmi JAJAS0 e JAJAS1 sono in attesa sulle code ECTS e ICTS
### Looc.up
 * Chiede sulla coda ECTS l'XML dei menù e la emette

## Loop di esecuzione

## Cambio ambiente
 * Chiama JAJAC0 con messaggio "DATSES" Funzione "CHG" e ambiente scelto. Gli ambienti devono essere definiti in modo comune (ad esempio in tabelle generali)

## Chiusura
### Looc.up
 * Chiama JAJAC0 con messaggio "DATSES" Funzione "DIS"
 ** Chiama JAJAS0SB con funzione "DIS"
 *** Chiede sulla coda ECTS la chiusura di JAJAS1
 *** Chiede sulla coda ICTS la chiusura di JAJAS0
 *** Cancella tutte le code create

## Note per eventuali (improbabili) malfunzionamenti
### Il CLIENT termina in modo anomalo
 * Lavori in BATCH su AS/400
 ** Time-out sulla tabella UI1
 *** impostato       -> Il lavoro AS/400 termina normalmente
 *** non impostato   -> I lavori devono essere eliminati (ev. allo spegnimento macchina)
 * Code
 ** Restano nella libreria
 *** schedulare un lavoro di pulizia della stessa (mediante WRKJOBSCDE)
 :  : INI Vuoi schedulare il lavoro di pulizia?

## Il programma RPG termina in modo anomalo
 * Lavori in BATCH su AS/400
 ** Verificare il messaggio per rimuovere la causa
 ** Eliminare manualmente il lavoro
 ** Cancellare il TASK sul client
 * Code
 ** Si elimineranno al momento della pulizia della libreria

# Analisi Performance
### Scopo del documento
Lo scopo di questo documento è di raccogliere le informazioni relative all'analisi delle performance del sistema AS400 - client Looc.up, ai problemi noti e alle relative soluzioni.

## Comunicazione, Aspetti Base.
Il processo che si occupa di gestire la comunicazione tra AS400 e Looc.up è JAJAS1.

Per ogni Looc.up attivo viene creato su AS400 un processo JAJAS1.
Per ogni sessione di emulatore avviata da Looc.up, viene creato un processo JAJAS0.
Questo significa che dato un client Looc.up attivo posso avere da 1 a n JAJAS0 attivi.

## I log
Vediamo l'aspetto relativo ai log. Sono disponibili tre tipi di log : 
 - I log dei servizi.
 - I log dell'emulatore.
 -I log della scheda.

### I log dei servizi
Sono depositati su AS400 come file di Spool. Ogni chiamata crea un file con il nome del servizio escluso il caso del JAJAS1 dove il file è unico per ogni Looc.up avviato.

### Come attivare il log di un servizio.
E' possibile monitorare ogni servizio attivando il log nella tabella PGM.
Dal 1 feb 2006 se si sottopone a log il servizio JAJAS1, quello di base di Looc.up, vengono monitorati TUTTI i servizi. Il log si trova nello spoolfile JAJAS1.
Attivare il log su questo servizio è utile quando non si capisce qule servizo risulta particolarmente lento.

### Visualizzare i log dei servizi
I log dei servizi sono dentro i file di spool (SP o WRKSPLF). Il file ha il nome del servizio richiamato. All'interno del file si trova l'XML letto e il tempo necessario. Se l'XML supera i 25.000 caratteri viene spezzato in n blocchi e per ognuno viene riportato il tempo di creazione.
Il tempo di creazione è espresso in milionesimi di secondo quindi un tempo di 25.000 corrisponde a 25 millisecondi.

### Come testare un servizio
I servizi sono elencati nella tabella PGM.
Se non si conosce quale servizio compie una determinata azione si può, da LoocUp, una volta eseguita l'azione che interessa andare ad analizzare la funzione corrente (menù di loocup, Servizi, Funzione Corrente) oppure analizzare l'ultimo XML scritto (menù di loocup Servizi, Ultimo XML Scritto) che rappresenta la richiesta inviata da LoocUp all'AS400.
Nella prima riga dell'XML scritto c'è la funzione richiesta ad esempio : 
Funzione richiesta : JS        FUN       EDT       *EDTAGG             MBDOC       LOBASE_015     OJ*LIB      SMEDEV         OJ*FILE     DOC
cioè : 
 * Tipo Messaggio :           JS
 *  Azione :                         FUN
 * Componente :                EDT
 * Servizio :                        *EDTAGG
 * Funzione.metodo :         Blank
 * Oggetto1 - tipo :             MB
 * Oggetto1 - parametro :  DOC
 * Oggetto1 - codice :        LOBASE_015
 * Oggetto2 - tipo :            OJ
 * Oggetto2 - parametro :  *LIB
 * Oggetto2 - codice :        SMEDEV
 * Oggetto3 - tipo :            OJ
 * Oggetto3 - parametro :  *FILE
 * Oggetto3 - codice :        DOC

Va notato che in questo caso il servizio che si deduce (*EDTAGG) non è il servizio richiamato. Per capire quale è il servizio associato bisogna andare nella tabella JAT.
Se invece dell'ultimo XML scritto si accede all'ultimo XML letto si ottiene l'XML che risponde l'AS400 a fronte della richiesta ricevuta. In questo XML la funzione richiesta si trova nel tag Service, attributo Funzione.
Vediamo un frammento della risposta dell'AS400 a fronte della richiesta presentata sopra : 
< Service Titolo1="Documenti / Lettura testo" Titolo2="Analisi Performance" Funzione="F(EDT;*EDTAGG;) 1(MB;DOC;LOBASE_015) 2(OJ;*LIB;SMEDEV) 3(OJ;*FILE;DOC) 4(;;) 5(;;) 6(;;) P()" Servizio="JATRE_29C"/ >

L'attributo funzione è normalmente così composto : 
F(Componente;Servizio;Funzione.Metodo) 1(tipo oggetto1;parametro oggetto1;codice Oggetto1) 2(tipo oggetto2; ....)
Nel caso appena visto il servizio è definito dell'attributo Servizio perchè *EDTAGG non è il servizio.

Note : 
 * per maggiori dettagli sulle funzioni vedi "Aspetti generali", "Funzioni".

 * per maggiori dettagli sulla comunicazione vedi "Aspetti generali", "Schemi applicativi"

### Su AS400
Un singolo servizio è testabile mediante il comando UP SER, F20 e se si desidera avere il log F6.
ATTENZIONE :  se si imposta il log per il servizio specificato, il log viene mantenuto attivo anche per Looc.up, l'F6 scrive nella tabella PGM.

### Da Looc.up
Da qualunque finestra di Looc.up se si seleziona Servizi, Funzioni di Controllo, Test prestazioni e comunicazione si accede alla possibilità di eseguire n chiamate dell'ultima funzione eseguita e verificare i tempi.

### I log dell'emulatore
Da una finestra di emulazione fare click con il tasto dx del mouse sull'icona rossa in alto a dx, selezionare "Analisi della Comunicazione" e poi "Visualizza Dati Performance".

### I log della Scheda
Viene creato un file nella cartella C : \Documents and Settings\ nome utente windows \ Dati applicazioni\loocup\ nome utente AS400\Logging.
In questo momento sono presenti due file, uno che contiene i dati delle performance dell'emulatore, l'altro che contiene la traccia di tutta la comunicazione.
NON VENGONO MAI SVUOTATI

## Problemi noti
 * Lentezza code
 * Code di grosse dimensioni (prossime ai 16MB)
 * Code che non vengono cancellate
 * AS400 che diventa improvvisamente lento
 * Lentezza se Looc.up installato su server
 * Lentezza nell'avvio
 * Lentezza G53
 * Lentezza JVM
 * Eccessivo utilizzo della memoria con lo schedulatore

### Problema lentezza code
Informazioni generali in "Funzioni lato server", "Configurazione dell'AS/400".

### Code di grosse dimensioni (prossime a 16MB)
Se nella libreria SMEUPUIDQ si trovano oggetti di dimensione molto elevata, prossime ai 16MB, significa che o Looc.up o l'AS400 non legge la coda o la legge a una velocità inferiore a chi la scrive.
Una coda di dimensioni normali è di circa 512KB.
Per verificare lo stato della coda si può utilizzare la G72, funzione RTV, metodo P. Se alla voce "Numero di voci" è presente il valore blank, significa che la coda

|  R="0000000099" |
| 
| .COL Txt="**N. voci 1 esec. G72**" A="L" |
| ---|----|
| 
| .COL Txt="**N. voci 2 esec.**" A="L" |
| 
| .COL Txt="**;Looc.Up**" A="L" |
| 
| .COL Txt="**server**" A="L" |
| 
| .COL Txt="**risultato**" LunAut="1" |
| blank|blank|attivo|attivo|OK |
| blank|blank|non attivo|non attivo|coda non cancellata |
| n|n|attivo|attivo|OK |
| n|n|non attivo|non attivo|coda non cancellata |
| n|m(n>m)|attivo|attivo|lettore più veloce - OK |
| n|m(m>n)|attivo|attivo|scrittore più veloce - rischio riempimento coda |
| 


### NOTA 1 :  dimensione code
La dimensione delle code non cala mai :  se il lettore risulta più lento la dimensione della coda viene incrementata. Se il lettore successivamente la svuota, la dimensione rimane comunque quella massima.

### NOTA 2 :  nomenclatura code
Le code seguono la seguente nomenclatura xyyynnnnnn, dove : 
Valori possibili per x : 
 * E :  Extended, sono le code su cui viaggiano i dati e richieste di schede o componenti JAVA
 * M :  coda Master che riceve la richiesta di avvio di una sessione di emulazione dal client
 * I :  coda su cui viaggiano i dati dell'emulazione

Valori possibili per yyy : 
 * CTS :  Client To Server -> richieste/dati dal client che vanno al server
 * STC :  Server To Client -> richieste/dati dal server al client

La parte rimanente del nome è composto da 6 cifre ed è un progressivo che identifica la coda.

### Code non cancellate
La terminazione corretta di Looc.up dovrebbe cancellare le code create. Una terminazione anomala di Looc.up può lasciare delle code. Si possono eliminare manualmente con il comando CLRLIB(SMEUPUIDQ). Non ci deve essere nessun utente connesso pena la disconnessione.
Questo comando andrebbe messo nello script di spegnimento o di accensione dell'AS400.

### AS400 che diventa improvvisamente lento
Si sono verificati dei casi in cui l'AS400 è diventato improvvisamente lento. Un possibile motivo è dovuto alle batterie della cache del raid (cache battery pack ) che si stanno scaricando.
In questa situazione la scrittura sui dischi non passa più per la cache del raid ma è diretta e questo provoca un forte (anche del 50%) rallentamento dell'AS400.
Per verificare questa situazione bisogna controllare che la memoria dei dischi sia in condiziona ATTIVA, oppure si deve accedere ai programmi di manutenzione.

Azioni da eseguire : 
 * controllare lo stato del sistema
 * controllare lo stato dei dischi e della memoria del raid
 * visualizzare registrazioni assistenza
 * verificare il cache battery pack

Controllare lo stato del sistema : 
 * comando WRKSYSSTS
>N.B. :  la memoria ASP è costituita dai dischi.

Controllare lo stato dei dischi : 
 * comando WRKDSKSTS mostra lo stato dei dischi :  non devono avere un'occupazione superiore al 90%
 * F11 mostra lo stato della memoria dei dischi :  deve essere ATTIVA o ACTIVE. Se non è in questa condizione bisogna chiamare l'assistenza urgentemente perchè le prestazione dell'A400 decadono e si rischia il fermo della macchina.

Procedura visualizzazione registrazioni assistenza)
 - connettersi con utente QSECOFR
 - esegui comando STRSST
 - inserisci utente e password programmi manutenzione (chiedere al cliente) (sono richieste dalla versione v4r5m0 in poi)
 - a seconda del rilascio del sistema operativo i seguenti punti potrebbero variare di numero : 
 -- Vai in avvia programma di manutenzione - gestore servizio hardware - gestione delle registrazioni di assistenza
 -- Verifica la richiesta di assistenza e la relativa parte interessata

Verifica cache battery pack : 
 - gestione unità disco
 - visualizzazione configurazione unità disco
 - visualizzazione stato hardware del disco : 
 - controllare che non vi sia la dicitura "prestazioni in decadimento" sui dischi.

### Lentezza se Looc.up installato su server
Quando Looc.up viene installato sul server risulta generalmente più lento rispetto all'installazione in locale.
Questo è dovuto al fatto che il programma vien letto dai dischi del server e deve transitare per la rete.
Una volta avviato Looc.up le informazioni scambiate con il server si riducono e le differenze di performance con loocup installato in locale dovrebbero essere minime.

Se Looc.up dovesse risultare sensibilmente più lento rispetto all'installazione in locale potrebbe essere dovuto a : 
 * Server di rete sovraccarico o non sufficientemente performante
 * Rete lenta
 * Problema del sistema operativo.

### Server di rete sovraccarico o non sufficientemente performante
Quando Looc.up è installato sul server, si è nella situazione in cui Looc.up gira sul client e utilizza il server per depositare parte delle informazioni (file temporanei, preferiti, cache).
In questa situazione sul server non gira nessun processo di Looc.up. Il server è solo un deposito di file è quindi importante che abbia dischi veloci e non troppo pieni, piuttosto che un processore veloce ma dischi lenti.
Per la verifica/soluzione di questo problema contattare un sistemista

### Rete lenta
Per verificare un problema di lentezza di rete bisogna chiedere supporto a tecnici dotati delle appropriate apparecchiature.

### Problema del sistema operativo
E' stato riscontrato un problema che affligge alcuni pc :  Looc.up, sia durante l'avvio, sia durante il normale uso, legge i file del server in piccoli frammenti.
Questo comportamento anomalo porta ad eseguire un numero enorme di accessi al disco con conseguente decadimento delle prestazioni del client.
Per verificare questa situazione anomala si può utilizzare ProcessMonitor che verificano l'accesso alla rete e alla cartella di installazione di Looc.up.
Se nel report che genera ProcessMonitor sono presenti una grande quantità di righe che nella colonna Request hanno il valore READ allora significa che è presente il problema.

ProcessMonitor lo potete trovare su
 :  : DEC T(J1) P(PATHFILE) [http://www.microsoft.com/technet/sysinternals/FileAndDisk/processmonitor.mspx](http://www.microsoft.com/technet/sysinternals/FileAndDisk/processmonitor.mspx)
I(link_pagina_ProcessMonitor) O(GI)

>N.B. :  L'attività di questo tool è piuttosto invasiva e può capitare che Process Monitor, anche se viene chiuso correttamente, impedisca a Loocup di ripartire o blocchi il PC. In questo caso l'unica soluzione è spegnere e riaccendere.

Non si conosce nè la causa nè la soluzione di questo problema.

### Lentezza nell'avvio
COMPLETARE
 * Documentare i parametri
 ** startdbg :  mostra i tempi di tutte le fasi di avvio di loocup. Prerequisito è l'esecuzione di Loocup con la console Java attiva (usare Loocup.exe)
 ** nouif :  non fa caricare i font all'inizio ma solo all'apertura di un mebro di documentazione attiva
 ** nologo :  non fa caricare il logo di Loocup
 ** logco :  logga tutta la comunicazione tra Loocup e l'AS400
 ** dbg :  attiva la modalità di debug. la console di Loocup diviene visibile e vengono mostrate tutte le informazioni sul funzionamento.

### In citrix
Scaricare la versione del 20 marzo 2008

### Molti font installati
E' stato verificato che il caricamento dei font rallenta molto l'avvio di Looc.up.
Questo è dovuto al funzionamento di Java.
Una soluzione alternativa alla riduzione del numero di font è di inserire nella riga di comando di loocup il parametro --nouif. Questo fa sì che i font vengano caricato solo quando l'utente accede alla documentazione.

### Molte installazioni della Java Virtual Machine (JVM)
 * Disinstallare tutte le versioni della jvm presenti tranne l'ultima, solo nel caso in cui l'utente non usi altre applicazioni basate su JAVA. L'installazione standard di JAVA si predispone per scaricare e installare automaticamente le nuove versioni. Purtroppo non disinstalla le precedenti ma crea un'installazione parallela.
Per verificare quali installazioni sono presenti seguite la procedura standard : 
 * In Windows XP :  pannello di controllo -> installazione applicazioni -> cercare Java.
 * In Windows Vista :  pannello di controllo -> Programmi e funzionalità -> cercare Java.

Se sono presenti più installazioni si avranno informazioni del tipo
 * J2SE Runtime Environment 5.0 update 7
 * J2SE Runtime Environment 5.0 update 9
 * Java(TM) SE Runtime Environment 6

Le versioni della JVM sono caratterizzate da 2 numeri, il numero di versione (1.4.2, 5, 6 ...) e il numero di upgrade (1...)
In questo caso ci sono 3 installazioni due 5.0, una è update 7 e l'altra 9 e una terza è alla versione 6 (update 0).
In questo esempio dovremmo quindi disinstrallare le due JVM con versione 5.

Completare
Nomenclatura Versioni di java.
Con il comando java -version, digitato in una finestra del prompt dei comandi  si capisce versione principale e aggiornamento della versione corrente

1.4.2 -
1.5.0 - anche nota come 5
1.6.0 -

### Lentezza G53
Se il tcp su AS400, sezione dominio non è configurato correttamente i tempi di generazione dei pdf sono molto lunghi. Si nota una differenza di un fattore 10 tra una configurazione corretta e una non corretta. Per i dettagli consultare la nota tecnica 78  - Prestazioni G53.
Un altro problema di lentezza si ha quando i file di modello sono troppo grandi. Si consiglia di creare file con dimensione NON superiore a 100Kb.

### Lentezza della JVM
Verificare la versione della JVM installata sul pc :  è consigliabile utilizzare la JVM 6 e successivi upgrade in quanto molto più performanti delle precedenti

### Eccessivo utilizzo della memoria con lo schedulatore
Lo schedulatore con la JVM 1.4.2 provoca un consumo abnorme di memoria. si consiglia il passaggio a JVM successive.

## Analisi sistema AS400
### Dove funziona Looc.up
TODO elencare caratteristiche di AS400 (Batch/interattivo) su cui funziona.

# Analisi Performance Servizi
### Cos'è l'analisi delle performance dei servizi?
L'analisi dei servizi fornita dall'applicativo Looc.Up permette di avere velocemente sotto gli occhi alcuni dati statistici sull'utilizzo e l'efficienza dei servizi forniti da Sme.Up.
Il servizio di Sme.Up che permette di ottenere l'analisi e la rappresentazione tramite matrici e grafici delle performance dei servizi è il **JASER_04**. Tale servizio, tra le varie funzionalità offerte, permette di visualizzare le informazioni sui servizi più/meno utilizzati, quelli più/meno veloci e inoltre per ogni singolo servizio fornisce  il tempo medio di esecuzione, il numero di volte richiamato e il dettaglio del tipo di funzione-metodo chiamati. Per dirla in breve il servizio **JASER_04** tiene traccia di ogni chiamata eseguita da Looc.Up verso Sme.Up per monitorare le performance di ogni servizio.

### Oggetti dell'analisi
Che cosa possiamo monitorare? A quale utente è riferita l'analisi? Qual'è il livello di dettaglio?
Il servizio di analisi delle performance fornisce dati statistici realitivi all' **utente** in quel momento connesso. In particolare offre due livelli di dettaglio : 

- analisi dei **servizi** correlati all'utente
- analisi delle **funzioni/metodi** per ogni servizio


### Come vengono recuperate le informazioni da cui partire per fare l'analisi statistica?
Vedi documento "Log collegamenti Looc.up e Web.up"

## Come funziona l'analisi?
### Possibilità offerte

- Vedere nome servizio/nome metodo, utilizzo, tempo di esecuzione medio
- Vedere elenco per il tipo di funzione chiamata, utente, utilizzo
- Informazioni su servizi più utilizzati, più lenti, meno usati


## FAQ

- All'aumentare del numero degli utenti connessi al sistema, il servizio tiene conto del diverso valore delle preformance?
- E' possibile tracciare un profilo delle applicazioni più utilizzate da tutti gli utenti?
- E' possibile raggruppare le statistiche per mese?


# Log collegamenti Looc.up e Web.up

- [Log collegamenti Looc.up e Web.up](Sorgenti/MB/DOC/JALOGT)

# Log Looc.up lato Client
I log di loocup sono salvati in  file locali, organizzati per sessione
## I log prodotti dal client Loocup
Alla data del 27/11/2007, versione di test di loocup, i file di log sono stati concentrati nella cartella identificata dal percorso
_7_%APPDATA%\Loocup\LOG.

La variabile di windows %APPDATA%, corrisponde alla variabile di Loocup ***APPDATA**.

Se il sistema operativo è Windows XP la variabile viene risolta in : 
C : \Documents and settings\utente_di_windows\Dati Applicazioni\Loocup\
## Durata dei log
I log vengono mantenuti per 7 giorni.
## Nomenclatura
I file hanno  il nome composto secondo due sintassi : 

Sessione_Utente_LOCComponente.estensione
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LOC :  è una costante
- Componente :  è il codice del componente Loggato (J1GRA)
- estensione può essere
-- PR :  indica log di performance (scritti dai componenti EXD e EMU)
-- ERR :  indica log di errore (scritti dai componenti EXD e EMU)
-- CMN :  indica log di comunicazione (solo per il componente EMU)
-- log :  indica log generali o di altri componenti


Sessione_Utente_LOTipoLog.log
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LO :  è una costante
- TipoLog :  è il tipo di log. Attualmente sono definiti i seguenti due tipi
-- PING :  memorizza i messaggi di ping inviati all'AS400 (sono i messaggi necessari a mantenre attivi i lavori su AS400)
-- INFO :  memorizza le informazioni di sato del client


TIPOLOG, può assumere i seguenti valori : 

- CONSOLE :  contiene tutte le informazioni visibili nella console JAVA. Attivato con le opzioni --dbg, --logcom, --server o --startdbg  **NOTA** :  alla data del 22/06/09 solo in sviluppo
- STARTUP :  contiene le informazioni sull'avvio di loocup. Attivato con le opzioni  --dbg e/o --startdbg
- BAS :  logga tutta la comunicazione sulle code ECTS-ESTC. Si attiva con l'opzione --logcom
- QUE :  logga la scrittura sulle code e gli eventi richiesti al main gui frame.
- INFO :  logga le informazioni sulla macchina e le variabili di ambiente. Attivato con le opzioni --dbg,  --logcom
- GUI :  logga gli eventi
- HTM :  logga le informazioni del modulo HTM
- FRM :  logga le informazioni del modulo FRM


oppure

SESSIONE_UTENTE_APPLICAZIONE.TIPOLOG
Dove : 

- SESSIONE :  è il codice della sessione corrente.
- APPLICAZIONE :  vale
-- Smetray :  il componente della scehda
-- Smeuiclt :  il compoinente dell'emulatore
- TIPOLOG vale
-- CMN :  registra la comunicazione Java-APPLICAZIONE
-- PR :  logga le performance
-- ERR :  logga gli errori.


## Log specifici di loocup server
Quando loocup è avviato in modalità server viene creato anche il file BCPROCESSCONTROLLER.LOG che si occupa di registrare le attività del programma BCProcessController, che si occupa di controllare i 3 processi che compongono Loocup e di riavviarlo se uno o più cascano.
### La scheda di analisi dei log
Mediante il comando CTRL+F9 viene aperta la scheda di debug di LoocUp. In questa scheda, la sezione "Log Loocup Client"  è dedicata all'interrogazione e alla gestione dei log prodotti.
### Variante disponibile nella versione di sviluppo di Loocup
Nella versione di sviluppo di Loocup è stato migliorato il servizio JA_00_05, che è in grado di interpretare la struttura del file di log e di creare una matrice

# Looc.Up e i Tasti rapidi (ShortCut)
In Looc.Up, come in altre applicazioni, è presente una funzionalità che permette di eseguire determinate operazioni con la pressione di una combinazioni di tasti della tastiera.

### ShortCut impostabili
In Looc.Up e' possibile definire una combinazione di tasti rapidi associati a diversi elementi : 

- Menù di finestra.
- Menù di sezione.
- Menù di Popup di oggetto.

Per tutti questi elementi la modalità di definizione è la medesima. Se esiste nell'XML di definizione di una voce di Menù l'attributo ShortCut, la combinazione di tasti in esso definita viene associata alla voce.

L'attributo ShortCut deve essere definito nel seguente modo : 

    ShortCut="<Tasto di controllo>+<Tasto di definizione>"
.. dove <Tasto di controllo> può essere solamente CTRL o ALT, mentre <Tasto di definizione> può essere un qualunque altro tasto (escluso quello di controllo ovviamente).

Esempio : 

   ShortCut="CTRL+G"
   ShortCut="ALT+R"

### ShortCut di sistema
In Looc.Up sono presenti anche degli shortcut già impostati, per eseguire rapidamente alcune operazioni standard.
In particolare, oltre ai tasti Funzione che ricopiano le funzionalità dei bottoni della bottoniera principale, esistono nella scheda altre combinazioni di tasti.
Possiamo suddividere queste combinazioni di Tasti rapidi in due categorie.

## ShortCut di Debug  : 
**CTRL+F05** (qualunque sezione di una scheda) :  Mostra al successivo refresh, l'xml di struttura delle sezioni della scheda, nelle sezioni stesse. Per disabilitare questa modalità è sufficiente premere di nuovo la combinazione di tasti.
**CTRL+F06** (qualunque sezione di una scheda) :  Mostra al successivo refresh, l'xml di dati delle sezioni della scheda, nelle sezioni stesse. Per disabilitare questa modalità è sufficiente premere di nuovo la combinazione di tasti.
**CTRL+F07** (solo matrice di aggiornamento) :  Mostra in una apposita sezione l'xml di comunicazione tra il servizio di aggiornamento e la matrice e viceversa. Per disabilitare questa modalità è sufficiente premere di nuovo la combinazione di tasti.
**CTRL+F09** (qualunque sezione di una scheda) :  Carica la scheda del debug in una nuova finestra.
**CTRL+F10** (solo matrice) :  Mostra le colonne nascoste di una matrice. Per disabilitare questa modalità è sufficiente premere di nuovo la combinazione di tasti.

## ShortCut funzionali : 
**ALT+D**(solo matrice) :  Mostra in una finestra esterna un pannello di dettaglio del record selezionato nella matrice.
**ALT+C** (solo sezioni matrice ed albero) :  Esegue la funzione che aggiunge l'oggetto selezionato (cella o nodo dell'albero) al carrello.
**ALT+O** (solo sezioni matrice ed albero) :  Esegue la funzione che aggiunge l'oggetto selezionato generico (cella o nodo dell'albero) al carrello.
