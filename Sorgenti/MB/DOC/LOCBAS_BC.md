

# Introduzione al sistema di Business Continuity

## Struttura hardware di base non ridondata

La struttura hardware di base di una installazione Loocup di tipo client-server è quella visibile nella
seguente figura : 


![BC_001](http://localhost:3000/immagini/LOCBAS_BC/BC_001.png)

Gli elementi di base di questa struttura sono : 


- AS400 :  è il server di riferimento il modulo che fornisce i servizi per il corretto funzionamento del client Loocup.
- Loocup client :  è il client grafico, il principale fruitore dei servizi XML offerti dal server AS400. Il client Loocup comunica con il server AS/400 attraverso code di comunicazione attestate su server. La comunicazione è di tipo a richiesta, dove il client grafico genera richieste e il server fornisce le informazioni gestionali necessarie al completamento delle richieste
- Loocup server :  è una elemento di controllo della rete. Comunica sia con il server AS/400 attraverso apposite code, sia con tutti i client della rete attraverso un meccanismo di registrazione via socket. I compiti di un server Loocup sono molteplici : 
-- Registrazione dei client attivi sulla rete. Tutti i client di tipo registrato (identificati in fase di setup) si registrano sul server Loocup ogni volta che si avviano. In questo modo il server sa sempre quali sono i client attivi ed è in grado di fornire all'AS400 informazioni riguardo lo stato di uno specifico client. La registrazione di un client sul server di Loocup avviene con un meccanismo di comunicazione via sockets.
-- Fare da centro di raccolta unificato dei segnali e degli eventi provenienti da fonti esterne al sistema. Attraverso un meccanismo a plugins, il server Loocup è in grado di raccogliere eventi dal mondo esterno e notificarli al server AS/400 attraverso un evento su coda di comunicazione.
--Fornire il supporto per la comunicazione da server AS/400 verso i clients attivi. Il sistema AS/400 server può inviare al client Loocup una richiesta di azione destinata a uno qualsiasi dei client Loocup registrati. Il server Loocup è in grado di ricevere la richiesta e indirizzarla correttamente al client di destinazione.


A differenza di un normale client Loocup, la struttura di rete di tipo client server consente una serie di funzionalità aggiuntive : 

- Il server di Loocup funziona da centro di aggregazione per la comunicazione con moduli esterni al sistema gestionale. Attraverso l'utilizzi di plugin specifici, il server di Loocup può raccogliere informazioni provenienti da sistemi di fabbrica, dispositivi software hardware esterni o sistemi di comunicazione con sistema remoti.
- A differenza di un normale client, il server Loocup può anche ricevere da AS400 delle richieste di esecuzione di servizio. Attraverso l'utilizzo del server e di una speciale coda dedicata, il sistema gestionale su AS400 può richiedere servizi  al server Loocup. Il server Loocup può gestire questi servizi in prima persona oppure indirizzare le richieste a moduli esterni interfacciati attraverso l'uso dei plugins.
- Il Loocup server è in grado di registrare e controllare in ogni momento la lista dei client Loocup connessi. Questa funzionalità non si esaurisce al controllo dello stato dei client remoti ma consente anche l'invio di eventi a una postazione remota o l'invio di una richiesta di esecuzione di funzione. Quindi attraverso il server Loocup, il gestionale può inviare messaggi a un client remoto oppure richiedere che su di esso venga eseguita una particolare funzione gestionale (ad esempio, la visualizzazione di una scheda specifica oppure l'esecuzione di una procedura 5250)
- Analogamente al punto 3, una struttura di tipo client server consente una serie di operazioni reciproche tra client diversi. Ad esempio, è possibile che un client Loocup chiede che una specifica funzione sia eseguita su un client diverso oppure, più
semplicemente, un client può richiedere l'invio di un messaggio che ha come destinatario un altro client registrato sul server e attivo su una macchina fisica diversa.


## Effetti dei malfunzionamenti sul sistema

Prima di ipotizzare una soluzione per la business continuity, è necessario valutare l'effetto dei malfunzionamenti sul funzionamento dell'intero sistema in modo da valutarne le possibili conseguenze.

### Malfunzionamento di un client Loocup

Il malfunzionamento di un client Loocup non ha ripercussioni dirette sul corretto funzionamento del sistema se non quella di perdere una postazione di lavoro e quindi trovarsi nella impossibilità di ricevere input o inviare un output a quella postazione.  Se il client Loocup che si blocca è di tipo non registrato non è richiesto nessun intervento da parte del sistema di gestione. Se invece il client bloccato è uno di quelli registrati come attivi dal server Loocup, è necessario fare in modo che il sistema si accorga del blocco del client e segnali correttamente la sua mancanza. Questo per evitare che il server Loocup continui a considerare attiva postazione che nella realtà è invece fuori servizio e quindi non presidiata.

### Malfunzionamento del server Loocup

Il malfunzionamento del server Loocup porta al blocco di tutte le funzioni di gestione dei client registrati. Il blocco del server Loocup non comporta il blocco dei singoli client attivi sulla rete, perché questi client possono funzionare anche senza la presenza del server. Infatti i client Loocup richiedono servizi direttamente all'AS/400 senza passare dal server Loocup. Il blocco del server Loocup ha però gravi conseguenze sulla gestione delle interconnessioni tra le varie parti del sistema.
In particolare : 


- Viene persa ogni informazione relativa ai client Loocup attivi sulla rete. Non è più possibile sapere se uno specifico client è attivo o meno.
- Al server AS400 viene a mancare la possibilità di richiedere funzioni al server Loocup o a uno qualsiasi dei client Loocup attivi.
- Non vengono più raccolti gli eventi provenienti da moduli esterni interfacciati attraverso plugins. Specularmente, non è più possibile inviare richieste di servizio a moduli esterni che diventano pertanto completamente isolati rispetto al sistema



### Malfunzionamento del server AS/400

Il malfunzionamento del server AS/400 rappresenta probabilmente la situazione più critica per il corretto funzionamento del sistema. Il blocco del sistema AS/400 comporta il completo blocco :  tutti i client attivi e il server Loocup perdono il principale fornitore di servizi e si trovano pertanto nella condizione di non poter funzionare.


## La business continuity

###  Scopi

Lo scopo della funzionalità di business continuity è quello di garantire che il sistema informativo sia in un certo grado capace di rilevare e gestire nel modo opportuno problematiche che possano portare al blocco del sistema stesso. L'obiettivo di base è quello di ridurre al minimo possibile le situazioni di blocco del servizio e consentire agli operatori di continuare a lavorare anche a seguito di problematiche hardware o software che altrimenti potrebbero impedire il normale funzionamento del sistema. Il concetto di business continuity non si estende a tutte le funzioni del sistema ma solo a un sottoinsieme di funzioni individuate come fondamentali per il corretto funzionamento del sistema di gestione; in caso di problemi, il sistema deve essere in grado di mantenere disponibili queste funzioni fondamentali e garantire una copertura funzionale minima anche in situazioni di emergenza. E' invece accettato il fatto che le funzioni considerate secondarie possano non essere disponibili in alcune situazioni critiche.

### La struttura hardware ridondata

Nella seguente figura è mostrato uno schema di massima che rappresenta la struttura hardware/software necessaria alle funzionalità di business continuity.  La struttura prevede la duplicazione completa nel sistema e la creazione di una linea (client-server-AS400) di backup che sia alternativa a quella principale.
Una struttura di questo tipo prevede due modalità distinte di funzionamento, identificate da due distinti stati del sistema : 


- Funzionamento su linea primaria :  è il normale funzionamento del sistema, dove i singoli client, registrati sul server, dialogano e richiedono funzioni al sistema AS400 primario. E' la condizione di utilizzo prevalente e prevede la disponibilità di tutte le funzionalità e di tutti i servizi previsti in fase di progettazione.
- Funzionamento su linea di backup :  è da intendere come la modalità di funzionamento di emergenza, da attivare qualora non sia possibile operare attraverso l'utilizzo della linea principale. La modalità di backup prevede un set limitato di servizi, identificati tra quelli ritenuti come fondamentali per il mantenimento dell'operatività del sistema. L'attivazione della linea di backup e lo switching delle attività su questa linea deve avvenire a seguito di problemi sulla linea principale e può essere automatico (è il sistema stesso che rileva problemi e commuta in automatico sulla linea di backup) o manuale (l'amministratore del sistema forza l'attivazione della linea di backup per poter liberare la linea principale e consentire la manutenzione su di essa). Il ritorno alla linea principale verrà invece gestito in maniera manuale da un amministratore di sistema.


Le due modalità di funzionamento sono completamente distinte sia nella parte hardware che nella parte puramente software e mutuamente esclusive. Ad un certo istante può essere attiva solo una delle due modalità disponibili e tutti gli operatori devono operare nella modalità attiva in quel momento; in linea di massima, in un sistema ben configurato ed ottimizzato l'utilizzo prevalente sarà quello attestato sulla linea primaria mentre l'utilizzo della linea di backup (che è comunque una linea a funzionalità ridotta rispetto a quelle primaria) sarà meno frequente e legato solo ad occasionali problemi o a necessità di manutenzione della linea primaria. Il sistema non prevede alcuna forma di controllo su problematiche che coinvolgono contemporaneamente la linea principale e la linea di backup :  in caso di problemi sulla linea primaria, la reazione del sistema consiste sempre e solo nella attivazione della linea di backup. Se nemmeno quella può essere attivata il problema si deve considerare bloccante e non gestibile dal sistema di business continuity.

### Architettura hardware e software del sistema di business continuity

La struttura hardware necessaria per la definizione di un sistema di business continuity prevede l'utilizzo di due diversi sistemi denominati server primario e server di backup. Tipicamente si tratta di due macchine distinte, posizionate preferibilmente su sistemi di rete diversi e con linee di alimentazione elettrica distinte. Queste condizioni garantiscono che un eventuale problema di rete o di fornitura elettrica non possa mai coinvolgere contemporaneamente le due macchine, condizione questa che vanificherebbe ogni sforzo di gestione della business continuity.
Analogamente ai server di Loocup, esiste anche una duplicazione a livello di sistema gestionale su AS400. Il sistema gestionale primario gira sul sistema AS400 di produzione, attivo nelle condizioni di utilizzo normali. Al sistema di produzione può essere affiancato un sistema AS400 di backup :  questo sistema può essere una copia esatta del sistema di produzione oppure può essere un sistema che implementa solo un sottoinsieme delle funzionalità gestionali normalmente fornite dal sistema primario. L'importante è che i due sistemi AS400, il primario e il sistema di backup, siano continuamente allineati per quel che riguarda i dati gestionali. L'aggiornamento deve avvenire nei due sensi :  quando è attiva la linea primaria, tutti i dati gestionali inseriti nel sistema AS400 principale devono essere replicati (in tempo reale o a intervalli prestabiliti) sul sistema AS400 di backup. Viceversa, quando è attivo il sistema di backup, tutti i dati inseriti nel sistema AS400 di backup dovranno essere riversati sul sistema AS400 principale prima che questo ritorni ad essere il sistema gestionale di riferimento.

La figura seguente mostra in linea di massima la struttura hardware e software di un sistema di business continuity.

![BC_002](http://localhost:3000/immagini/LOCBAS_BC/BC_002.png)

Gli elementi che compongono il sistema software-hardware di gestione della business continuity sono tre : 


- Linea primaria :  è la linea attiva nelle normali condizioni di funzionamento. Il sistema AS400 di riferimento è quello primario e tutti i client Loocup in attività sono registrati e comunicano con il server Loocup principale. In queste condizioni, il controllo dei client è centralizzato sul server primario.
- Linea di backup :  è la corrispondente della linea primaria attestata sul sistema di backup. E' il sistema che si attiva in caso di malfunzionamento o fuori servizio delle linea principale, al fine di minimizzare i tempi di fuori servizio del sistema gestionale. A seconda dei casi, la linea di backup può essere una copia fedele e pari funzionale della linea primaria oppure una linea che garantisce le sole funzionalità ritenute vitali per il corretto funzionamento del sistema gestionale. E' importante notare che in nessun momento è possibile il funzionamento contemporaneo della linea principale e della linea di backup. Il funzionamento delle due linee deve essere per forza mutuamente esclusivo :  o funziona la linea principale o funziona quella di backup, in modo da evitare che lo stesso evento gestionale possa essere registrato due volte attraverso due strade di comunicazione diverse.
- Linea di controllo :  rappresenta il sistema di controllo che governa l'intelligenza della business continuity. La funzione della linea di controllo è quella di controllare lo stato del sistema principale e di gestire le azioni necessarie per il controllo del sistema di backup. La linea di controllo è composta da tre elementi fondamentali : 
-- BCBackupController :  è il sistema di controllo principale. Questo elemento è in grado di dialogare sia con il Loocup Server principale che con il Loocup Server di backup e di conseguenza con tutti i client di sistema, siano essi della linea principale che della linea di backup. Questo elemento è in grado di rilevare malfunzionamenti sulla linea principale e scatenare di conseguenza tutte le azioni necessarie all'attivazione della linea di backup. Il BCBackupController è attivo sul server di backup e per la sua natura di controllore non può mai essere fermato (a meno di non voler disattivare le funzionalità di business continuity).
-- BCBackupNodePrimary :  è un client fittizio usato dal BCBackupController per comunicare con il server Loocup primario. Nella lista dei client attivi sul server primario, questo client fittizio compare con il nome di BACKUP_NODE.
-- BCBackupNodeBackup :  è un client fittizio usato dal BCBackupController per comunicare con il server Loocup di backup. Nella lista dei client attivi sul server di backup, questo client fittizio compare con il nome di BACKUP_NODE.
-- BCProcessController :  è un piccolo modulo esterno che fornisce un primo livello di controllo sulla business continuity. Lo scopo di questo modulo è quello di fornire un controllo sullo stato di alcuni processi del sistema e intervenire nel caso si verifichi uno stop indesiderato del processo controllato. In particolare, il BCProcessController controlla il server primario di Loocup e il BCBackupController e interviene ogni volta che uno di questi due processi si chiude in maniera imprevista. Il controllo consiste nel semplice riavvio del processo che si è inaspettatamente fermato.


Il corretto funzionamento del sistema di business continuity prevede due prerequisiti fondamentali : 


- Comunicazione tra i componenti :  è necessario che tutti gli elementi del sistema siano in grado di comunicare tra di loro e scambiarsi sia informazioni sullo stato del sistema, sia richieste di esecuzione di comandi operativi.
- Rilevazione automatica e controllo delle situazioni di errore :  perché la business continuity funzioni correttamente è necessario che il sistema sia in grado di rilevare, con un certo grado di accuratezza, le situazioni di malfunzionamento della linea primaria. L'accuratezza del meccanismo di business continuity dipende in larga parte dalla capacità di autodiagnosi del sistema e dalla sua capacità nell'individuare e valutare i possibili problemi. E' inoltre molto importante distinguere i problemi in funzione della loro gravità e delle loro ripercussioni sul funzionamento globale del sistema :  l'obiettivo è quello di evitare che problemi locali o di scarso impatto sul sistema nel suo insieme provochino delle commutazioni indesiderate nella modalità di backup.
- Uniformità di comportamento :  la commutazione del sistema dalla linea primaria alla linea di backup deve avvenire in perfetta sincronia su tutti gli elementi della rete.



### Modalità di funzionamento su linea primaria

Nella modalità di funzionamento normale, il sistema attivo è quello riferibile alla linea primaria. In questa modalità le condizioni di funzionamento possono essere riassunte nei seguenti punti : 


- Il sistema AS400 attivo è quello primario e tutte le funzionalità gestionali sono disponibili ed operative.
- Il sistema AS400 di backup viene continuamente allineato nei contenuti allo stato del sistema AS400 primario. L'allineamento tra le due macchine non riguarda tutti i dati gestionali nel loro insieme ma solo un sottoinsieme di informazioni considerate vitali per il mantenimento in funzione del sistema informativo.
- Il Loocup Server attivo è quello primario. Sul questo server sono attivi i moduli aggiuntivi (plugin) delegati alla comunicazione con il sistema di fabbrica (tipicamente, la comunicazione con il modulo PLC). Il server Loocup è correttamente collegato all'AS400 primario e può sia ricevere comandi da esso sia inviare notifiche di eventi. Ha inoltre una funzione di controllo sul sistema AS400 primario visto che ad intervalli regolari controlla che il sistema sia disponibile ed attivo.
- Il loocup server di backup è disabilitato.
- Sulla macchina di backup è attivo il processo BCBackupController che attraverso il client fittizio BCBackupNodePrimary controlla in continuazione lo stato del server Loocup primario attestato sul server primario di Loocup.
- Sulle n postazioni di lavoro sono attivi i Loocup client primari. Ognuno di questi client è collegato sia all'AS400 (che funziona da fornitore di servizi gestionali), sia al server di Loocup primario (che funziona da gestore dei client attivi e della comunicazione tra gli stessi).
- Ognuno dei client Loocup è anche connesso al controllore della business continuity, oggetto che gira permanentemente sul server di backup e che è in grado di controllare i client e di prendere il controllo della situazione nel caso che il server primario vada fuori servizio.


La figura seguente riassume lo stato del sistema nelle condizioni di funzionamento normale.

![BC_003](http://localhost:3000/immagini/LOCBAS_BC/BC_003.png)

## Gestione dei malfunzionamenti del sistema

In caso di problemi sulla linea primaria, viene attivata la modalità di funzionamento su linea di backup. L'attivazione può avvenire in modi distinti a seconda del tipo di problema che si verifica.
In particolare, possono essere due le cause principali di attivazione della linea di backup.

### Malfunzionamento del sistema AS400 primario

La condizione di malfunzionamento del sistema AS400 primario rappresenta la situazione più critica tra quelle possibili perché viene a mancare il principale fornitore di servizi gestionali. Il malfunzionamento del sistema AS400 può essere dovuto a vari motivi : 


- Blocco del sistema dovuto a guasti o a problemi di accessibilità (ad esempio, mancanza del collegamento di rete).
- Blocco dei servizi. Il sistema AS400 funziona ed è attivo ma non è in grado di fornire i servizi gestionali richiesti.


In entrambe le situazioni, il sistema gestionale non è più in grado di fornire servizi necessari al corretto funzionamento del sistema informativo e quindi è necessario ripristinare una situazione di completa o parziale funzionalità attraverso l'attivazione del sistema di business continuity.
La sequenza di eventi che si verifica in questo caso può essere riassunta nei seguenti punti : 

- Il sistema AS400 principale non è più in grado di fornire servizi (per guasto o per problemi di comunicazione).
- Il server Loocup primario, che controlla in continuazione la connessione con l'AS400 primario, si accorge della mancanza di collegamento.
- Il server Loocup primario esegue una serie di test per tentare di capire la natura del problema sull'AS400 primario. Questi test sono necessari per filtrare eventuali malfunzionamenti temporanei ed evitare che il sistema di business continuity si attivi anche nel caso di malfunzionamenti temporanei del sistema gestionale primario.
- Se il malfunzionamento permane anche dopo i controlli, il server primario di Loocup notifica al BCBackupController di aver perso la connessione con l'AS400 primario. Il BCBackupController esegue a sua volta dei controlli sullo stato di funzionamento del sistema AS400, per controllare che il problema non sia limitato al solo server primario di Loocup. Se il sistema AS400 dovesse risultare funzionante ed attivo il BCBackupController invia al server primario di Loocup un comando di reset nel tentativo di risolvere il suo problema di comunicazione con AS400.
- Se anche il BCBackupController rileva che il sistema AS400 primario è fuori servizio, viene attivata la procedura di avvio del sistema di backup. I passo di questa procedura sono i seguenti : 
-- Il BCBackupController invia al server primario di Loocup un comando di spegnimento.
-- Il BCBackupController invia a tutti i client di Loocup attivi un comando di commutazione su linea di backup. Ognuno dei client Loocup reagisce al comando disconnettendosi dal server Loocup primario e riavviandosi in modalità backup, che prevede la connessione al server Loocup secondario.
-- Il BCBackupController avvia il server Loocup di backup, che si connette al sistema AS400 di backup. Nel frattempo, tutti i client Loocup che si avviano in modalità di backup si registrano sul server di backup e si connettono a loro volta al sistema AS400 di backup.


Lo stato del sistema dopo l'intervento della business continuity è il seguente : 

![BC_004](http://localhost:3000/immagini/LOCBAS_BC/BC_004.png)
Sulla linea primaria non rimane più nulla di attivo. Tutto il controllo passa sulla linea secondaria e tutto il sistema gira sulla macchina di backup. Il sistema primario non è attivo ed è quindi possibile intervenire per la soluzione del problema che ha portato al blocco del sistema AS400 principale. Il supporto gestionale viene fornito dal sistema AS400 di backup che registrerà dati ed eventi fino a quando il sistema primario non ritornerà a funzionare. Il Loocup Server di backup prende il posto del Loocup server primario anche nella gestione della comunicazione con i sistemi esterni :  se nelle condizioni normali è il server primario che si occupa di raccogliere eventi esterni (ad esempio, eventi provenienti dal PLC) tranne l'uso dei plugin, nel sistema di backup è il server di backup che prende il controllo anche di queste funzionalità.

### Malfunzionamento del server Loocup

Un'altra forma di malfunzionamento del sistema si verifica quando è il server Loocup a manifestare malfunzionamenti o situazioni di fuori servizio.
Il server Loocup ha lo scopo principale di centralizzare in un unico punto la raccolta di eventi e di informazioni provenienti da ambiti esterni al sistema gestionale. Rappresenta inoltre un centro di controllo dei client di Loocup attivi sulla rete e consente l'invio a client remoti di eventi e richieste di comando.
Per il corretto funzionamento del sistema globale è quindi importante garantire il funzionamento del server Loocup per evitare l'isolamento del sistema gestionale dal resto dei sistemi informativi o tecnici dell'azienda.

Come già detto per il sistema AS400, il malfunzionamento del server Loocup può essere la conseguenza di un guasto della macchina ospitante, di un problema software del sistema di gestione del server o un problema di comunicazione o di accesso di rete esterno alla macchina stessa.

In una qualunque di queste situazioni è importante che il sistema di business continuity sia in grado di gestire il problema e ricondurre in maniera automatica il sistema globale in uno stato di funzionalità minima garantita.

Vediamo in dettaglio la sequenza di eventi che si verifica in caso di problemi sul server Loocup primario : 


- Il server di Loocup primario non è più attivo o non è più raggiungibile dalla rete.
- Il processo BCBackupController, attivo sulla macchina di backup e costantemente attivo nel controllare lo stato del server primario, si accorge che il server primario non è più disponibile. Viene attivata una procedura di controllo che esegue una serie di tentativi di riconnessione al server primario, allo scopo di evitare l'intervento del sistema di business continuity in caso di problemi temporanei.
- Se il problema sul server primario persiste, il modulo BCBackupController attiva la procedura di attivazione della linea di backup, che consiste nei seguenti passi : 

-- Il modulo BCBackupController controlla se il sistema AS400 primario è attivo o meno. Questo controllo è necessario per evitare di commutare tutta la linea sull'AS400 di backup anche nei casi in cui è solo il server di Loocup ad avere problemi. Tendenzialmente, il sistema di business continuity manterrà ove possibile la comunicazione con il sistema AS400 primario e commuterà su AS400 di backup (che per sua natura può avere funzionalità ridotte) solo nel caso in cui anche il sistema AS400 primario dovesse risultare fuori uso.
-- Il modulo BCBackupController manda a tutti i client Loocup attivi sulla linea primaria un comando di commutazione su linea di backup. Unitamente al comando, viene notificato anche l'indirizzo del sistema AS400 da utilizzare in modo da poter consentire al client in modalità di backup di continuare a dialogare con il server primario, se ancora funzionante.
-- Il modulo BCBackupController avvia il server Loocup di backup, notificando anche ad esso quale sistema AS400 utilizzare.


In caso di malfunzionamento del server primario di Loocup sono quindi possibili due situazioni diverse di intervento, a seconda dello stato del sistema AS400 primario.

La figura seguente mostra lo stato finale del sistema di business continuity in reazione al solo malfunzionamento del server primario di Loocup.


![BC_005](http://localhost:3000/immagini/LOCBAS_BC/BC_005.png)

Il sistema di business continuity è intervenuto per gestire il malfunzionamento del server primario di Loocup attivando il server Loocup di backup e commutando tutti i client attivi su di esso. Viene però mantenuta, sia a livello di server che di client, la connessione con il sistema AS400 primario che, non avendo manifestato malfunzionamenti, rimane il sistema gestionale di riferimento. In questa modalità ibrida, il sistema pur trovandosi in una modalità di emergenza mantiene comunque attive tutte le funzionalità gestionali.

La seconda situazione operativa è quella che vede il contemporaneo malfunzionamento sia del server primario di Loocup che del sistema AS400 primario. In questo caso, la situazione finale dopo l'intervento del sistema di business continuity è lo stesso a quello del caso di malfunzionamento del solo AS400 :  tutto il sistema commuta su linea di backup e sulla linea primaria non rimane più nulla di attivo. Il sistema gestionale attivo è quello di backup e quindi per tutta la durata dell'emergenza sono garantite le sole funzionalità di base offerte dal sistema gestionale di backup.

# Comandi disponibili per BC

![BC_006](http://localhost:3000/immagini/LOCBAS_BC/BC_006.png)
# Variabili di setup per BC

Per configurare il sistema di BC è necessario specificare nel file di setup SCP_CLO tutte le informazioni necessarie alla configurazione.

Le variabili da settare sono le seguenti : 


**..****C.VAR**  _Cod**="*BCServerIP" Txt="IP server primario" Value="172.16.2.213" TVal="" PVal=""
**..****C.VAR**  _Cod**="*BCServerPort" Txt="Porta server primario" Value="9990" TVal="" PVal=""
**..****C.VAR**  _Cod**="*BCClientCode" Txt="Nome client" Value="TSTCLI" TVal="" PVal=""

**..****C.VAR**   Cod="*BCServerPath" Txt="Path server primario" Value="X : \programmi\Loocup_test" TVal="" PVal=""
**..****C.VAR**   Cod="*BCServerName" Txt="Nome server primario" Value="SRVTST" TVal="" PVal=""
**..****C.VAR**   Cod="*BCAS400IP" Txt="IP AS/400 Primario" Value="172.16.2.11" TVal="" PVal=""
**..****C.VAR** Cod="*BCBackupServerIP" Txt="IP server backup" Value="10.67.7.63" TVal="" PVal=""
**..****C.VAR**Cod="*BCBackupServerPort" Txt="Porta server backup" Value="9999" TVal="" PVal=""
**..****C.VAR**Cod="*BCBackupServerPath" Txt="Path server backup" Value="\\10.67.7.63\LoocupServer" TVal="" PVal=""
**..****C.VAR** Cod="*BCBackupServerName" Txt="Nome server backup" Value="SERVER" TVal="" PVal=""
**..****C.VAR** Cod="*BCBackupAS400IP" Txt="IP AS/400 Backup" Value="10.67.7.55" TVal="" PVal=""


Il primo blocco di variabili sono le stesse di quelle utilizzate per attivare un Looc.Up come client.

Il secondo blocco di variabili sono invece specifiche per il sistema di BC e devono essere tutte definite perchè il sistema funzioni.





