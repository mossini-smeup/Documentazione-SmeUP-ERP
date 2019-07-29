# Gestione dei moduli server per Looc.Up (serventi)

## Cos'è un modulo server.

Un modulo server per Looc.Up (detto anche servente) è una entità in grado di fornire servizi al client Looc.Up, in alternativa al fornitore di servizi di default.
Quando un Looc.Up viene avviato, si connette al sistema AS400 che da quel punto in avanti diventa il fornitore di servizi di default per quella istanza di Looc.Up. Ogni volta che viene richiesta una funzione, il client Looc.Up gira questa funziona come richiesta al sistema AS400 e legge la risposta XML contenente l'eventuale risposta al servizio richiesto.
E' però possibile fare in modo che alcune funzioni non vengano inoltrate al sistema AS400 ma vengano richieste a dei moduli server specifici, conosciuti da Looc.Up. Questi moduli server sono definiti nel file di configurazione del client ed avviati dal Looc.Up client al suo avvio.

**Per fare in modo che una funzione venga richiesta ad uno dei moduli server aggiuntivi al posto che all'AS400 è necessario specificare il campo SERVER all'interno della funzione.

Quindi, se si invoca la funzione generica : 

F(PGM;FUN : MET) 1(T1;P1;K1)

questa viene richiesta come servizio al sistema AS400.
Ma se la funzione precedente diventa : 

F(PGM;FUN : MET) 1(T1;P1;K1) **SERVER(SERVER1)**

la stessa funzione non viene più richiesta all'AS400 ma al modulo servente esterno identificato da Looc.Up con il codice SERVER1.
In questo documento vedremo come si definiscono i moduli server di Looc.Up e come vengono registrati in una istanza di Looc.Up.

## Identificazione dei server per Looc.Up

I moduli server aggiuntivi per Looc.Up sono identificati all'interno del gestionale Sme.Up come oggetti di tipo **V3-CSE**.
La lista dei moduli attivi è specificata nel file di configurazione SCP_CLO del client Looc.Up, secondo le modalità che verranno illustrate nel proseguo di questo documento.


# Schema di riferimento

![LOCBAS_028](http://localhost:3000/immagini/LOCBAS_CSE/LOCBAS_028.png)
Questa figura mostra come LoocUp, oltre ad essere connesso con il server master AS400, consente di definire una serie di pacchetto di server alternativi (chiamati **SERVER DI LOOCUP** o **SERVENTI**), incaricati di compiere specifiche funzionalità, anche sostitutive a quelle fornite dal master. Questo permette di costruire un sistema molto articolato e di agganciare anche più applicativi sul lato server purchè si rispettino i protocolli di comunicazione. Nel caso in esame, il client Looc.Up ha attivato alla sua partenza 3 serventi, identificati rispettivamente dai codici A, B e C. Da notare che i serventi A e B sono attivi sulla stessa macchina su cui gira Looc.Up mentre il servente C è attivo in una locazione remota. Questa cosa è possibile perchè i serventi vengono attestati su uno specifico indirizzo IP che può anche essere remoto rispetto alla macchina che richiede l'utilizzo del servente stesso.

Le gestione dei serventi esterni avviene tramite il servizio java JA_00_17 che ha il compito di inizializzarli, attivarli e con cui possono essere eseguite interrogazioni. La dichiarazione dei server esterni è codificata, come per i listener, nello script SCP_CLO, nel file dei configuratori SCP_CFG e l'attivazione avviene all'avvio di LoocUp. Il sistema provvede a creare tanti threads, ossia processi che condividono parallelamente l'accesso al processore, quanti sono i servers definiti nello script.


# Definizione dei server per Looc.Up e loro attivazione

La lista dei serventi aggiuntivi che un client Looc.Up deve attivare all sua partenza è definita nel file di inizializzazione SCP_CLO all'interno dell'apposita sezione "Server"
Ad esempio, la notazione : 

 :  : I.XML
C.SEZ Cod="Server"
C.SER Cod="00" Txt="LOOC.UP" Add="127.0.0.1" Protocol="JAVA"
C.SER Cod="01" Txt="FXWord" Add="127.0.0.1" Param="path=/xml/feed.asp" Protocol="HTTP"
C.SER Cod="02" Txt="Documentazione FXWord" Add="documenti.fxword.it" Protocol="HTTP" Param="path=/xml/feed.asp"
C.SER Cod="03" Txt="ICM Server" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.plugins.contentmanager.UICMServerExternalServer"
 :  : I.XML.END

configura 4 serventi, identificati dai codici 00, 01, 02 e 03. La struttura della definizione verrà illustrata più avanti in questo documento.

Se analizziamo la notazione, vedremo che ogni nodo server definisce un servente specifico. Il singolo servente è identificato da un codice univoco (parametro Cod) e da un indirizzo che consente di allocare anche serventi posti su macchine diverse da quella su cui gira Looc.Up (ad esempio, il servente 02 della notazione precedente, che è attestato su un IP remoto e raggiunto tranne un protocollo HTTP).
Da notare la presenza di un particolare servente con codice 00 :  è il client Looc.Up stesso, che di fatto risulta registrato come servente di se stesso e quindi capace di fornire a sua volta dei servizi interni. In pratica, tutti i servizi che possono essere risolti direttamente dal client Looc.Up senza inviare richieste a serventi esterni rientrano in questa categoria e per questo motivo Looc.Up client può essere inteso a sua volta come un fornitore di servizi.

## Protocollo di comunicazione tra Looc.Up e i serventi esterni

I server di Looc.Up esterni possono essere visti come delle interfacce tra Looc.Up e moduli esterni di varia natura. L'interfaccia fa in modo che un modulo esterno, scritto da terze parti e su cui solitamente non si ha controllo, possa fornire dei servizi a Looc.Up con un formato delle richieste di tipo funizzato (quindi basato su richieste di tipo F() e con risposta XML in uno dei formati definiti da Looc.Up).

Visto che moduli esterni possono essere molto eterogenei, sono state definite modalità diverse modalità di comunicazione Looc.Up e i suoi serventi esterni, in modo da poter garantire l'interfacciamento nella maggior parte dei casi.

I protocolli di comunicazione previsti sono i seguenti : 

 T(Protocolli disponibili)
- HTTP :  comunicazione con il server esterno attraverso il protocollo HTTP o HTTPS. Si presume pertanto che il server esterno disponga di una interfaccia HTTP.
- JAVA :  comunicazione con il server esterno attraverso la definizione di un interfaccia scritta in linguaggio Java. Looc.Up fornisce un intefaccia preimpostata che guida la creazione di queste interfaccie e specifica le funzionalità da implementare per il corretto funzionamento della comunicazione.
- SOCKET :  comunicazione con il server esterno attraverso una connessione su porte socket. Il protocollo è specifico per ogni singola implementazione.
- AS400 :  consente di specificare un secondo AS400 come servente alternativo all'AS400 principale.


## Server esterni predefiniti

Looc.Up viene fornito con alcune interfaccie predefinite verso moduli server esterni noti; ad esempio, viene fornito una interfaccia per un server IMAP di posta elettronica oppure per l'interfaccia a un secondo AS400 alternativo a quello primario di collegamento.


## Documentazione dei servizi esterni

Per rendere uniforme la documentazione dei servizi, si e' scelto di portare in documentazione attiva anche i servizi implementati da server esterni con le seguenti regole per la nomenclatura : 
JA_xx_yy
xx = codice del server
yy = progressivo servizio

I servizi locali avranno  nome JA_00_yy.
I servizi di FXWord avranno nome JA_01_yy.

## Server esterni aggiuntivi
Looc.Up viene può essere esteso con server esterni, installabili ed attivabili signolarmente.
Un esempio di questi server esterni aggiuntivi è quello che permette di consumare web service SOAP.
Una realizzazione di tale tipologia di client è quella che si interfaccia al web service AT dell'Autorità Tributaria e Doganiera del Ministero delle Finanze del Portogallo
- [Web service AT](Sorgenti/MB/DOC/LOBASE_20)
