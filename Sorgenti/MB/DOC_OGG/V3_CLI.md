# CLI -  LISTENERS DI LOOCUP
Questo documento definisce il metodo con cui ci si può definire un listener di Loocup.

## Schema di funzionamento
In attesa che venga realizzato lo schema, descriviamo in dettaglio il comportamento del listener.
Il listener manda un evento al gestore degli eventi (interno a loocup). Il gestore degli eventi riceve un evento del tipo EVT, e se il log è attivo lo salva nel file di log, dopo di che lo gira all'AS400. l'AS, riceve l'evento e in base alle informazioni presenti restituisce

## Limitazioni alla data del 05/03/2007

- L'elenco degli oggetti V3-CLI è recuperato solo dal file DEFAULT. Se vengono definiti listener negli altri script questi non vengono visti, pur essendo attivi.
- Un listener genera un evento che viene mandato su AS400 al servizio indicato nel parametro Service. Il servizio predefinito per la gestione degli eventi è il servizio LOSER_11. Questo servizio è ancora in fase di sviluppo.
- Non è gestita la dimensione massima dei log e la durata


## Famiglie di listener

- JAVA  :  listener implementati in java e possono nativi (cioè presenti nell'installazione standard di Loocup come DirectoryLookupJavaExternalListener) oppure esterni e gestiti come plugin dell'applicazione che sono in grado di passare al MainGuiFrame degli eventi EvtEvent che segnalano l'accadere di un evento gestito dal listener.
- SOCKET  :  applicazioni esterne che si collegano come client ad un server attivo in Loocup (ancora da implementare) su una porta specifica e sono in grado di comunicare a Loocup eventi esterni.
- AS400  :  moduli in grado di essere in ascolto su code AS400 e in grado di veicolare all'interno di Loocup l'avvenuto arrivo di qualcosa su tali code.


 T(Comportamenti generali dei listeners)
- L'inizializzazione  :  il listener deve prevedere una fase di inizializzazione all'interno della quale si può identificare il setup del listener. Se la fase di inizializzazione avviene con successo il listener viene registrato dall'applicazione.
- I ping  :  il listener deve poter comunicare ogni lasso di tempo (eventualmente da stabilire) un evento di tipo F(EVT;XXX;PNG) che permette al server di sapere che il listener è vivo. All'arrivo di tale funzione di ping, come anche all'arrivo di qualunque altro evento dal listener, il manager dei listener aggiorna la data di ultima comunicazione relativa a tale listener. Se l'intervallo di tempo supera il tempo massimo di attesa (di default vale 5 secondi) il listener, qualora ne venga richiesto lo stato tramite il servizio JA_00_16, viene dichiarato inattivo.
- La generazione dell'evento :  il listener deve poter generare e comunicare al server gli eventi che è in grado di raccogliere tramite funzioni F(EVT...
- La distruzione del listener :  il listener deve poter essere distrutto (e quindi deregistrato).



## I listeners della famiglia JAVA
La creazione di listener Java, siano essi interni o esterni, prevede l'estensione della classe Smeup.smeui.uimainmodule.externallistener.java.UIJavaExternalAbstractListener e quindi l'implementazione dei metodi
 :  : PAR
- public boolean initialize(UILoocupSession aLoocupSession, UIJavaExternalListener aServer)  :  si tratta del metodo chiamato in inizializzazione e dal cui esito dipende la registrazione o meno del listener nell'applicazione
- public void doAction(); che viene richiamato ogni x secondi



## I listeners della famiglia JAVA - OLD -
La creazione di listener Java, siano essi interni o esterni, prevede l'implementazione dell'interfaccia Smeup.smeui.uimainmodule.externallistener.java.UIJavaExternalListenerInterface e quindi l'implementazione dei metodi
 :  : PAR
- public boolean initialize(UILoocupSession aLoocupSession, UIJavaExternalListener aServer)  :  si tratta del metodo chiamato in inizializzazione e dal cui esito dipende la registrazione o meno del listener nell'applicazione
- public String sendEvt(MainGuiFrame aFrame, UIFunInputStructure aFunInput)  :  si tratta del metodo che veicolerà all'interno del MainGuiFrame (tramite il suo metodo guiActionRequested) l'evento generato tramite la UIFunInputStructure
- public String ping(MainGuiFrame aFrame)  :  si tratta del metodo che comunica il ping all'applicazione per far sapere che il listener è ancora vivo
- public void destroy()  :  si tratta del metodo che viene richiamato per la distruzione del listener.


## I Listener JAVA INTERNI
- [Listener CARTELLE](Sorgenti/MB/DOC_OGG/V3_CLI_01)
- [Listener code messagi Loocup](Sorgenti/MB/DOC_OGG/V3_CLI_06)
- [Listener casella IMAP](Sorgenti/MB/DOC_OGG/V3_CLI_07)
- [Listener Skype](Sorgenti/MB/DOC_OGG/V3_CLI_08)



## I listener della famiglia SOCKET
TODO

## I listener della famiglia AS400
TODO

## Definizione dei listener
I listener di Loocup sono definiti in maniera simile a come vengono definiti i server :  nei membri di configurazione presenti nel file AS SCP_CLO.
All'interno di tali membri va dichiarata la sezione **C.SEZ Cod="Listener"** che è la sezione di definizione dei listener.
All'interno di tale sezione vanno definiti i singoli listener attraverso delle specifiche **C.LST**.
La sintassi di questo tag è definita nello script EDT_CLO. E' pertanto definito un wizard che guida nella definizione del listener.

## Parametri dei listener
I listener ha i seguenti parametri
 T(Dettaglio dei parametri del listener)
- Cod :   Codice
- Txt :   Descrizione
- Add :  l'indirizzo di rete dove reperire il listener
- Protocol :  il Protocollo implementato (sono supportati JAVA,AS400,HTTP,HTTPS)
- Param :  Parametro in cui definisco le proprietà specifiche del listener. E' formato da coppie VARIABILE=VALORE, separate dal ";".
- LoadOnStartup :  Parti all'avvio
- MaxDelay :  Millisecondi max inattività. Se il listener non genera un evento (attività o ping) per un tempo superiore a quello indicato viene dichiaratto inattivo.
- TestMode :  consente di testare un listener senza averlo creato o disponibile.
- DebugMode :  Attivo in modalità di debug.
- EnableLog :  Attiva log
- MaxLog :  Dimensione max in MB del log
- NumDayLog :  Numero giorni log



## La modalità di avvio in test dei listeners
Ogni listener si può attivare in modalità di test :  per fare questo è sufficiente impostare il parametro **TestMode** a 1 o in alternativa  inserisce nell'attributo **Param** la dichiarazione di avvio del listener in modalità test (TESTXML=1).
Il listener dichiarato viene sostituito da una classe di test Smeup.smeui.uimainmodule.externallistener.UiExternalListenerTester che simulerà ogni 5 secondi l'invio di un evento secondo la seguente modalità : 
Il listener di test ricercherà la cartella LOOCUP_XML\LST\< nome utente>\< codice listener> (ad es. :  LOOCUP_XML\LST\< nome utente>\L2 nell'esempio precedentemente riportato), che dovrà contenere n files il contenuto dei quali verrà utlizzato per generare gli eventi. Di quati n files ne verrà selezionato uno a caso e verrà utilizzato per costruire un evento. Il contenuto dei files ti test dovrà essere il seguente : 
 :  : PAR
- La prima riga riporta la funzione F(EVT che si deve generare
- Il resto del file viene utilizzato come campo Input nella UIFunInputStructure per passare il contenuto dell'evento



### Definizione dei listener della famiglia JAVA
Volendo definire un listener JAVA (facendo l'esempio con il monitor dei file interno a Loocup) definiamo delle specifiche **C.LST** come riportato nei due esempi successivi : 

 :  : C.LST Cod="L1" Txt="ListenerL1" Add="localhost" Protocol="JAVA" LoadOnStartup="1" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=C : \test"

 :  : C.LST Cod="L2" Txt="ListenerL2" Add="localhost" Protocol="JAVA" LoadOnStartup="1" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=C : \test2;TESTXML=1"

L'attributo **-Cod-** è il codice del listener e identifica in maniera univoca il listener che entrerà a far parte degli oggetti V3-CLI
L'attributo **-Protocol-**  identifica la famiglia del listener che si sta definendo
L'attributo **-Add-** indentifica l'indirizzo del listener, per il listener della famiglia JAVA non è sostanzialmente utilizzato quindi si puo' lasciare il valore di default
L'attributo **-LoadOnStartup-** indica l'avvio e la registrazione del listener in avvio di Loocup (1 = sì, 0 = no). Per il momento questo avviene sempre e quindi è come se fosse sempre 1.
L'attributo **-Param-** contiene i parametri del listener separati da '**;**' e, nel caso dei listener della famiglia JAVA si attende obbligatoriamente la dichiarazione della classe java che implementa il listener :  **class=Classe.completa.di.package** ed opzionalmente la dichiarazione della modalità di avvio (che chiariremo in seguito) del listener :  test o effettivo. E' possible passare al listener la definzione del servizio che gestira l'evento attraverso il parametro **Service=< nome servizio >**; è possible passare al listener la definzione del metodo che gestirà l'evento attraverso il parametro **Method=< nome metodo >**; in questo modo la F che il listener genererà per comunicare l'evento sarà di questo tipo :  F(EVT;< nome servizio >; < nome metodo >) LISTENER(codice listener) .Il resto del contenuto dell'attributo Param è legato specificatamente al listener dichiarato.

**NOTA** :  Nell'attributo Param c'è la voce class. Per i listener più comuni sono state definite delle variabili nello script DEFAULT della SMEUP_TST.

### Definizione dei listener della famiglia SOCKET
TODO
### Definizione dei listener della famiglia AS400
TODO

