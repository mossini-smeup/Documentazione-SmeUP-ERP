# Esempio di architettura Looc.Up in una installazione client-server completa

In questo documento verrà mostrato un esempio di architettura Looc.Up con tutti gli elementi che entrano in gioco.

La seguente immagine mostra la struttura della rete client server di esempio che andremo ad analizzare : 

![LOCBAS_026](http://localhost:3000/immagini/LOCBAS_001/LOCBAS_026.png)
Questo documento mostra la struttura di una tipica installazione di Loocup in modalità server. Questa modalità di utilizzo di Loocup si propone di risolvere tutta una serie di problemi legati alla interazione tra procedure AS/400 e processi o entità esterne esterni.

In particolare, attraverso una installazione server di Loocup è possibile : 
 * Raccogliere informazioni provenienti da processi o entità di terze parti operanti su sistemi esterni all'AS/400
 * Inviare informazioni o richiedere azioni a entità remote
 * Richiedere l'esecuzione su sistemi remoti di operazioni di sistema (ad esempio, operazioni di lettura o scrittura del file system, invio mail, interazioni con protocolli di sistema o altro).

L'installazione di Loocup in modalità server è tipicamente una installazione come servizio su una macchina ospitante. Attualmente la macchina ospitante può essere solo un PC con sistema operativo Windows.

# Architettura di base
La seguente figura mostra una tipica installazione di Loocup in modalità server. L'ipotesi di partenza è quella di risolvere le esigenze di comunicazione e integrazione tra un sistema AS/400 su cui è installato il software gestionale (tipicamente Smeup), e un sistema esterno di terze parti che può essere sia un software installato su una macchina diversa dal AS/400, sia un dispositivo hardware verso cui interfacciarsi.

La struttura è incentrata su quattro attori distinti : 
 - Il sistema gestionale attestato su piattaforma AS400. In questo contesto il sistema gestionale di riferimento è Smeup ma potrebbe essere qualsiasi altro software funzionante su questa piattaforma operativa.
 - Loocup installato in modalità server. Tipicamente è un servizio Windows attivo su una macchina di rete sempre attiva e in grado di stabilire un collegamento sia verso l'AS/400 sia verso il sistema esterno
 - Un modulo di interfaccia, la cui funzione è quella di fare da ponte e da adattatore tra il Loocup Server e il sistema esterno da interfacciare. Il modulo di interfaccia può essere di tipo standard o di tipo proprietario a seconda del tipo di modulo esterno a cui interfacciarsi.
 - Il modulo esterno, tipicamente un software o un dispositivo hardware di terze parti che può richiedere o fornire informazioni al gestionale su AS/400. Il modulo esterno può essere locale o remoto.


Un struttura di questo tipo consente varie tipologie di interazioni : 
 * **Integrazione del gestionale AS/400 verso Sistema Esterno** :  il gestionale ha bisogno per il suo funzionamento di informazioni che sono possedute da un Sistema Esterno di terze parti. Attraverso il Loocup Server il gestionale può far pervenire al sistema esterno una richiesta di lettura delle informazioni e ricevere la risposta, tipicamente in formato XML.
 * **Integrazione del Sistema Esterno verso gestionale su AS400** :  è il caso in cui è il sistema esterno che in qualche modo è in grado di notificare all'AS400 informazioni, eventi o cambio di stato.

All'interno del sistema gioca un ruolo fondamentale il  modulo di interfaccia. Lo scopo di questo modulo è quello di interfacciare il Loocup Server verso un sistema esterno e garantire che i due sistemi possano scambiarsi informazioni. In pratica opera una funzione di "traduttore" tra i protocolli di richiesta e comunicazione di Loocup e quelli richiesti dal sistema esterno. Il modulo di interfaccia garantisce che tutti i sistemi esterni, qualunque essi siano, siano sempre visti da Loocup Server come oggetti omogenei e capaci di ricevere richieste e fornire risposte in un formato prefissato e standard.

Tipicamente possono essere distinte due grandi famiglie di Interfacce : 
 - **Interfacce di tipo standard** :  sono quei moduli pensati per l'interfacciamento verso sistemi esterni di tipo standard. Ad esempio, un sistema esterno potrebbe essere un sito internet o un Web Service. In questo caso, il sistema esterno implementa precisi standard codificati a livello internazionale e quindi anche il modulo di interfaccia può essere considerato tale. Ad esempio, un modulo di interfaccia pensato per l'interfacciamento verso un Web Service non funzionerà solo per quel Web Service ma anche per qualsiasi altro servizio costruito secondo quello standard. Per la loro natura i moduli di interfaccia standard sono sviluppati per un uso generale e sono forniti con Loocup Server.
 - **Interfacce di tipo proprietario** :  sono quei moduli pensati per l'interfacciamento verso sistemi esterni di tipo proprietario e non riconducibili verso uno standard generale. In questo caso è necessario sviluppare un modulo di interfaccia specifico per quel contesto e in grado di interfacciarsi solo verso uno specifico software o dispositivo. Per la loro natura, questo tipo di interfacce non può essere fornita con l'installazione standard di Loocup Server ma devono essere sviluppate di volta in volta a seconda del tipo di contesto.

La comunicazione tra AS400 e Loocup Server avviene attraverso code dati. Ogni istanza del Loocup Server che viene avviata su un PC esterno crea due code dati denominate STC + codice server e CTS + codice server. La prima di queste code consente la comunicazione nella direzione AS400 - Loocup Server mentre la seconda la comunicazione inversa. In una rete ci possono essere più Loocup Server attivi, ognuno individuato da uno specifico codice. Il sistema AS400 può scegliere con quale Loocup Server comunicare scegliendo la coda opportuna su cui inviare la richiesta.

La generalità del concetto di interfaccia comporta anche una generalità nel concetto di canale di comunicazione. Infatti mentre la comunicazione tra AS/400 e Loocup Server avviene sempre con un meccanismo di code dati, la comunicazione tra Loocup Server e Interfaccia (vedi elemento A in figura) e la comunicazione tra Interfaccia e Sistema Esterno (elemento B) può avvenire in modalità diverse a seconda del contesto.

In particolare : 

- **Comunicazione tra Loocup Server e modulo di Interfaccia (A)** :  in questo caso la tipologia di comunicazione viene definita dal Server Loocup che mette a disposizione varie modalità con cui comunicare con un modulo di interfaccia. Le modalità oggi previste per la comunicazione tra Loocup Server e modulo di interfaccia oggi sono : 
-- Comunicazione di tipo http
-- Comunicazione su porta Socket
-- Istanza diretta dell'interfaccia come plugin del server

- **Comunicazione tra Interfaccia e Sistema Esterno (B)** :  in questo caso, la tipologia di comunicazione dipende fortemente dal sistema esterno verso cui è necessario interfacciarsi. In molti casi potrebbe anche non esserci una vera comunicazione :  ad esempio, quando il sistema esterno salva le informazioni su un file o su un database e l'interfaccia non fa altro che accedere a queste informazioni senza comunicare direttamente con l'entità esterna.

