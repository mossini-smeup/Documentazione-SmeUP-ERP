# Introduzione
Con questo documento illustreremo gli aspetti tecnici della configurazione e dell'utilizzo di Looc.Up come server

# Cosa è Loocup Server
Looc.Up server è una particolare modalità di funzionamento di Loocup, in cui nella rete viene creata una istanza del client stesso (server) che funziona da controllore di tutte le altre istanze (i client) e come come fornitore di servizi centralizzato.
L'installazione e l'avvio di un Looc.Up in modalità server consente quindi di creare una rete Looc.Up di tipo client-server e permette tutta una serie di funzionalità aggiuntive rispetto ad un sistema basato unicamente su client Looc.Up singoli (installati sulle singole macchine o avviati da una cartella di condivisione).

Una installazione di tipo client-server ha una struttura descritta dalla seguente figura : 


![LOCBAS_029](http://localhost:3000/immagini/LOCBAS_SER/LOCBAS_029.png)

Gli elementi caratteristici di tale struttura sono.

 T(Gli elementi caratteristici di questa struttura sono : )
-  **Il Looc.Up server** :  è l'elemento centrale della struttura client server. E' una istanza di Looc.Up avviata in modalità server e dedicata al controllo della rete.
-  **I Looc.Up clients** :  sono n istanze di Looc.Up avviate in modalità client. Ogni client è collegato al Looc.Up server attraverso una connessione diretta e al relativo sistema AS400.
-  **I serventi Looc.Up** :  sono dei fornitori di servizio alternativi all'AS400. Non rientrano negli argomenti di questo documento ma sono illustrati nella apposita sezione di documentazione.


# Looc.Up server

E' l'elemento di controllo di una rete client-server.

 T(Rispetto ad un client Looc.Up normale, il Looc.Up server ha una serie di funzionalità aggiuntive : )
- Il Looc.Up server può fornire servizi al sistema AS400. Nei client Looc.Up normali è il client stesso che accede ai servizi offerti dal sistema AS400 invocandoli su code di comunicazione. Nel server è possibile anche la cosa opposta, cioè il sistema AS400 può a sua volta richiedere servizi al Looc.Up server. Questo è possibile perchè Looc.Up server attiva una coda di comunicazione specifica sulla quale si registra come fornitore di servizi.
- Il Looc.Up server è in grado di controllare i client Looc.Up ad esso connessi. Quando un Looc.Up viene avviato in modalità client all'interno della rete client-server, si registra sul server e crea un canale di comunicazione specifico attraverso il quel il server può comunicare con il client stesso. Grazie a questo canale di comunicazione, il server può controllare tutti i client collegati e sono pertanto consentite operazioni normalmente non eseguibili all'interno di una rete non client server. Ad esempio, chiedere che un specifica funzione venga eseguita su uno specifico client, spegnere o riavviare remotamente dei client, consentire al singolo client di demandare l'esecuzione di alcune funzioni al server (ad esempio, i processi lunghi che non richiedono controllo).
- Il Looc.Up server è strutturato in modo tale da garantire la stabilità di funzionamento. All'interno del server ci sono dei meccanismo di controllo che verificano la funzionalità del server stesso; nel caso si dovessero rilevare problemi (ad esempio, il crash improvviso di uno dei moduli che costituiscono il server) il sistema di controllo interviene immediatamente e riavvia il server con le stesse credenziali attive prima del crash. Questo meccanismo garantisce che il server sia sempre disponibile, anche a seguito di errori fatali.


In Sme.Up i server Looc.Up sono classificati come oggetti di tipo **V3-LSE**

## Prerequisiti per l'installazione come server

L'installazione su una singola macchina di un Looc.Up in modalità server non ha alcun prerequisito aggiuntivo rispetto ai normali prerequisiti richiesti per un client Looc.Up normale.

## Avvio di Looc.Up in modalità server

 T(Looc.Up può essere avviato in modalità server inserendo nella linea di comando la notazione **--server : NOME_SERVER : PORTA** dove :  )
- **--server : ** è la notazione che indica a Looc.Up di avviarsi nella modalità server
- **NOME_SERVER** è il nome univoco assegnato al server **(max 6 caratteri)**. E' il nome con cui il server è conosciuto dal sistema AS400.
- **PORTA** è la porta socket usata dal server per connettersi con i client. Non è un parametro obbligatorio e di default vale 9999. La specificazione della porta consente di installare più server su una singola macchina, assegnado ad ognuno dei server una porta di comunicazione diversa.


Con questa modalità, un esempio di avvio di Looc.Up in modalità server può essere il seguente : 

_1_Loocup.exe SISTEMA UTENTE PASSWORD AMBIENTE --server : SRVTST : 9991

 T(Dove : )
- SISTEMA :  as400 a cui si connette il server
- UTENTE, PASSWORD, AMBIENTE :  autenticazione utente
- SRVTST :  nome in codice del test
- 9991 :  porta socket di comunicazione con i client


Oltre a questa modalità di avvio è possibile una seconda modalità, più tecnica, che sfrutta le funzionalità offerte dalla Java Virtual Machine.

Riportiamo un esempio di questa seconda modalità, ricordando comunque che è consigliabile avviare il server nel modo descritto in precedenza

java -Xms128m -Xmx512m -Dsun.java2d.noddraw -DSmeup.smeui.uiserverside.name=NOME_SERVER -DSmeup.smeui.uiserverside.port=PORTA -jar Loocup.jar SISTEMA UTENTE PASSWORD AMBIENTE --server


## Identificazione di un Loocup Server e comunicazione con AS400

All'interno di Sme.Up i server Looc.Up sono classificati come oggetti di tipo **V3-LSE** (**L**oocup **SE**rver).

Per ognuna delle istanze di Loocup server attive, vengono create su AS400 delle code di comunicazione specifiche per il server, che consentono al sistema AS400 di interrogare il server stesso.
Queste code sono identificate come : 

- **ESTC+NOMESERVER** :  coda su cui l'AS400 può inviare richieste al Loocup Server. Le richieste devono  essere inviate in formato funizzato.
- **ECTS+NOIMESERVER** :  coda su cui il server Loocup invia la risposta all'AS400. Le risposte sono stringhe di max. 25000 caratteri ed è prevista la possibilità di paginazione (CONT e FINE nei primi 4 caratteri della risposta).

La coda di risposta ECTS + NOMESERVER può essere di tipo normale o di tipo a chiave. Nel secondo caso la risposta viene scritta nella cosa usando come chiave il codice passato nel campo K6 della richiesta. La chiave usata è quindi
lunga 15 caratteri al massimo.

 T(Si ricorda che : )
- Il nome del server NOMESERVER deve essere univoco (per ogni AS400) e **può essere al max si 6 caratteri.
- Le code ci comunicazione AS400-Looc.Up server vengono create dal Looc.Up server al suo avvio e cancellate allo spegnimento.
- L'esistenza delle code può essere interpretata da lato AS400 come disponibilità del server
- La lista dei server attivi su uno specifico As400 può essere ottenuta come lista di oggetti V3-LSE.
 :  : PAR : END


# Looc.Up client

Un Looc.Up client è una particolare esecuzione di Looc.Up abilitata alla connessione sul server.
Nel normale modo di funzionamento, Looc.Up è connesso al sistema As400 che funziona da fornitore di servizi e si comporta come un singolo programma in esecuzione su un determinato PC. Se invece viene avviato in modalità client, Looc.Up oltrea a connettersi con l'AS400 si connette anche sul server Looc.Up di riferimento, creando così una rete di client connessi tra di loro attraverso l'intermediazione del server.

Grazie a questa rete di connessione tra i client, sono possibili alcune funzionalità normalmente non disponibili in un sistema basato su singole esecuzioni di Looc.Up su singole macchine.

 - Il client è connesso al server e può quindi ricevere dal server stesso richieste di funzione, messaggi e comandi di controllo.
 - Attraverso la comune connessione al server, un client può interfacciarsi con qualsiasi altro client presente in rete, purchè connesso al server. Un client può quindi richiedere funzioni o servizi ad altri client o accedere risorse disponibili su altre macchine :  ad esempio, un client può accedere ad una stampante presente su un altro client attraverso l'uso di una funzione, come se la stampante fosse disponibile localmente.
- Il singolo client può demandare l'esecuzione di alcune funzioni al server, ad esempio funzioni non presidiate di lunga esecuzione (batch).

In questo contesto il Looc.Up server ha pieno controllo della rete e conosce in ogni momentoquanti sono e quali sono i client collegati ed attivi sulla rete stessa.

In Sme.Up i server Looc.Up sono classificati come oggetti di tipo **V3-LCL**

## Avvio di Looc.Up in modalità client

Perchè Looc.Up si possa avviare come client all'interno di una rete di tipo client-server è necessario specificare alcune informazioni aggiuntive rispetto al normale avvio di Looc.Up.

In particolare : 

- L'indirizzo del server Looc.Up a cui si dovrà connettere il client
- La porta socket su cui verrà effettuata la connessione
- Il nome con cui il client sarà riconosciuto da AS400 (parametro non obbligatorio, che è consigliato non specificare)

Pertanto, un singolo server verrà identificato da un client Looc.Up attraverso la coppia IP-porta, che deve essere univoca per server. Nel caso vengano installati più server Looc.Up su una singola macchina (quindi stesso IP) sarà quindi necessario fare in modo che ognuno dei server si attivi su una porta diversa, per evitare conflitti.


 T(I parametri di connessione possono essere specificati in due modi distinti : )
- A linea di comando
- Nel file di configurazione SCP_CLO


### Avvio del client Looc.Up con configurazione a linea di comando

 T(Looc.Up può essere avviato in modalità client inserendo nella linea di comando la notazione **--client : IP_SERVER : PORTA : CODCLI** dove :  )
- **--client : ** è la notazione che indica a Looc.Up di avviarsi nella modalità client
- **IP_SERVER** è l'indirizzo IP (o il nome mnemorico) della macchina su cui è attivo il Looc.Up server a cui collegarsi
- **PORTA** è la porta socket con sui collegarsi al server. Se non specificata vale 9999.
- **CODCLI** è il nome (che deve essere univoco) con cui il server identificherà questa istanza del client. **Normalmente si consiglia di non specificarlo.**


Un esempio di avvio con questa modalità è il seguente : 

**Loocup.exe SISTEMA UTENTE PASSWORD AMBIENTE --client : 172.16.2.213 : 9990 : TSTCLI**

che avvia un Looc.Up client identificato dal codice TSTCLI e collegato al Looc.Up server attivo sulla macchina 172.16.2.213 sulla porta 9990.

### Avvio del client Looc.Up con configurazione nel file SCP_CLO

Un modo alternativo di avviare Looc.Up client è quello di inserire a linea di comando la sola notazione **--client** e specificare nel file SCP_CLO di iniazializzazione della connessione gli attributi di connessione all'interno di variabili specifiche.

Quindi la stringa di avvio diventa semplicemente : 

**Loocup.exe SISTEMA UTENTE PASSWORD AMBIENTE --client**

e nella SCP_CLO si inseriranno le variabili : 

**..****C.VAR**  _Cod**="*BCServerIP" Txt="IP server primario" Value="172.16.2.213" TVal="" PVal=""
**..****C.VAR**  _Cod**="*BCServerPort" Txt="Porta server primario" Value="9990" TVal="" PVal=""
**..****C.VAR**  _Cod**="*BCClientCode" Txt="Nome client" Value="TSTCLI" TVal="" PVal=""

che definiscono IP del server, porta e codice da assegnare al client (anche qui è comunque consigliato non specificare il codice).

### Avvio del client Looc.Up come listener

Esiste una terza modalità per attivare un client, decisamente sconsogliata perchè ormai considerata obsoleta, ma che riportiamo a solo titolo di documentazione.
In questa modalità un Looc.Up diventa un client all'interno di una rete client-server solo se viene abilitato uno specifico listener attraverso la notazione : 

**..****C.VAR**  Cod="CL" Txt="Client node" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.client.UILoocupClientListener;server=172.16.2.111;Service=LOSER_11" LoadOnStartup="1" DebugMode="0"

inserita nel SCP_CLO

### Parametri aggiuntivi per la funzionalità di Business Continuity
Per completezza dell'informazioni citiamo anche le seguenti variabili, utilizzate per la funzionalità di business continuity.

**..****C.VAR**   Cod="*BCServerPath" Txt="Path server primario" Value="X : \programmi\Loocup_test" TVal="" PVal=""
**..****C.VAR**   Cod="*BCServerName" Txt="Nome server primario" Value="SRVTST" TVal="" PVal=""
**..****C.VAR**   Cod="*BCAS400IP" Txt="IP AS/400 Primario" Value="172.16.2.11" TVal="" PVal=""

**..****C.VAR** Cod="*BCBackupServerIP" Txt="IP server backup" Value="10.67.7.63" TVal="" PVal=""
**..****C.VAR**Cod="*BCBackupServerPort" Txt="Porta server backup" Value="9999" TVal="" PVal=""
**..****C.VAR**Cod="*BCBackupServerPath" Txt="Path server backup" Value="\\10.67.7.63\LoocupServer" TVal="" PVal=""
**..****C.VAR** Cod="*BCBackupServerName" Txt="Nome server backup" Value="SERVER" TVal="" PVal=""
**..****C.VAR** Cod="*BCBackupAS400IP" Txt="IP AS/400 Backup" Value="10.67.7.55" TVal="" PVal=""


## Identificazione di un client Looc.Up

All'interno di Sme.Up, i client Looc.Up sono identificati come oggetti **V3-LCL** (**L**oocup **CL**ient)

# Note finali su architettura Client-Server

- Un Looc.Up  client può collegarsi ad uno e un solo Loocup server alla volta.
- Un Looc.Up server non può avere due client con lo stesso codice collegati. Se un client tenta di collegarsi al server e trova già una altro client con lo stesso nome collegato, si mette in attesa e aspetta che il primo client si disconnetta. Non appena il collegamento si libera si collega.
- I Looc.Up client possono dalogare con il server e con altri client della rete solo se connessi al server.


