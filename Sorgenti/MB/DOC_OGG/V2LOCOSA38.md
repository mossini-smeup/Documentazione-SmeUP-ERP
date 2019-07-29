## Obiettivo
Il modulo A38 è un'interfaccia che permette di chiamare webservice esterni, pertanto è un costruttore che permette di integrare dati in ingresso, oppure di inviarne.
Ha lo scopo di mettere a disposizione una configurazione, e la relativa interfaccia per l'utilizzo, che permette di definire e dichiarare connettori verso servizi (in prima istanza HTTP-based, ma non solo) esposti da esterni esterni.
Il caso principale è il consumo di web service SOAP o REST.
La richiesta di una chiamata ad un webservice tramite il provider avviene con l'API specifica K11.

Il costruttore A38 è costituto da 4 entità : 
* una scheda :  LOA38
* una servizio base :  LOA38_SE
* script SCP_SET specifici Sme.UP o utente :  LOA38_xx
* programmi specifici Sme.UP o utente che richiamano i webservice tramite l'API K11

## Funzionamento
Lo Sme.UP Provider alla sua attivazione, tramite il servizio LOA38_SE, interpreta gli script di di interfaccia ai web service.

Negli script vengono definite le istanze della classe SESUB.A38 nel formato xx.yyy.zzz : 
* xx è il gruppo, corrisponde al nome dello script LOA38_xx
* yyy è la sezione definita all'interno dello script
* zzz è la subsezione definita all'interno dello script

All'interno dello script vengono pertanto indicate le chiamate web service pubblicate e le variabili di input e di output.

## La configurazione
La configurazione si basa sugli script con prefisso LOA38_ contenuti nel file SCP_SET.
ereditando la struttura dagli script dei LOA, la struttura riproposta è quella di Sezione e Subsezione.

## La sezione
Nella sezione, viene definito chi è l'interlocutore esterno, quindi il plugin che verrà attivato.
Es :  Operazioni tramite Socialmailer per l'infrastruttura di web marketing, operazioni tramite Gulliver per l'infrastuttura offline, etc.
Nella sezione è presente la specifica **A38.CLSSEZ** attraverso il quale viene definito il "driver" da attivare. Il driver non è altro che una classe java che implementa le operazioni definite nelle varie subsezioni attestate in questa sezione.
Es :   :  : A38.CLSSEZ Class="Smeup.smeww.webservices.client.socialmailer.SocialMailerConnectorAdapter" Pgm=""

## La subsezione
Nella subsezione ci sono diversi tipi di istruzioni.
Nella istruzione che la definisce è presente il timeout di attesa del completamento dell'istruzione. Al raggiungimento del timeout la richiesta viene considerata persa.
Es :   :  : SUB Cod="B00" Txt="Richiesta Messaggi" Timeout="300"
C'è poi l'istruzione che definisce il nome dell'operazione
Es :   :  : A38.SUBMET Value="MSGLIS" Txt="Nome che identifica la funzione"
Poi una serie di definizioni dei parametri necessari all'operazione che si sta definendo
Es :   :  : A38.SUBVAR Name="Token" Value="" Txt="Token di autenticazione" DftVal=""
Con questa istruzione si definisce il nome del parametro, il valore (qualora questo valore si voglia passarlo "cablato" o ereditato da una variabile), la sua descrizione ed il valore di default (qualora lo si voglia impostare)
Infine esiste, tramite l'istruzione A38.MSGOGG, la possibilità di gestire i parametri di risposta. Quindi oggettizzare le colonne della matrice che costituirà la risposta piuttosto che gestire degli alias per ovviare ai limite del campo Col della colonna.
Es :   :  : A38.MSGOGG Name="newsletter_messenger" Ogg="V2SI/NO"  Alias="NWLMSGR"

## Definizione nello script SCP_SET
Nel dettaglio questi sono i tag previsti nello script ed i relativi attributi principali : 


| 
| .COL Cod="COL001" Txt="Tag" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="Descrizione" LunAut="1" |
| A38.SUPPRV|l'attributo Active='1' indica l'attivazione, se non impostato lo script viene ignorato, invece nell'attributo DtaQ è possibile impostare un provider specifico per lo script, quando non è indicato la risalita del provider da utilizzare avviene tramite l'API K16 (è comunque necessario che sia impostato l'attributo Active='1') |
| SEZ       |nell'attributo Cod viene indicata la sezione |
| A38.CLSSEZ|l'attributo Class indica la classe lato provider e Pgm il programma richiamato da SND.MSG |
| A38.CNFSEZ|l'attributo Name indica il nome di una variabile di sezione e Value il relativo valore |
| SUB       |nell'attributo Cod viene indicata la subsezione |
| A38.SUBMET|l'attributo Value indica il nome attribuito alla funzione |
| A38.SUBVAR|l'attributo Name indica la variabile da passare al webservice. |
| A38.MSGOGG|l'attributo Name indica la variabile ricevuta dal webservice, è possibile definire anche un oggetto in Ogg e un nome per la ridenominazione della variabile in Alias. |
| 

E' infine possibile tramite il tag A38.VAR definire delle variabili di contesto G91 (&CO.xxx..).

Per la peculiarità dell'integrazione dei webservice normalmente l'interfaccia è un servizio specifico (vedi REMAMA_01). E' comunque possibile utilizzare il webservice in modalità diretta con una risposta in matrice tramite il LOA38_SE con la funzione metodo SIM.K11, oppure richiamando un programma di exit LOA38_xx tramite il LOA38_SE con la funzione metodo SND.MSG, che deve interfacciarsi al webservice direttamente tramite la K11.

# Autorizzazioni

E' possibile autorizzare tramite la classe d'autorizzazione A38, applicare un'autorizzazione all'esecuzione di una subsezione. L'autorizzazione può essere definita a 3 livelli : 
* Per l'intero script, indicando nella funzione il codice del gruppo (istanza dell'oggetto SEGRU.A38)
* Per una sezione, indicando nella funzione il codice della sezione (istanza dell'oggetto SESEZ.A38)
* Per singola subsezione, indicando nella funzione il codice della subsezione (istanza dell'oggetto SESUB.A38)

E' importante notare, che il controllo dei tre livelli si ferma alla prima verifica per cui il valore dell'autorizzazione per l'utente risulta essere "NO". Questo significa che quando viene disautorizzato un livello più alto, non verranno prese in considerazione le eccezioni di livello inferiore (es. se disautorizzo una sezione, ma setto come autorizzata una subsezione appartenente a quella sezione, quest'ultima autorizzazione non verrà controllata, vincerà il fatto che l'utente NON è autorizzato alla sezione).

 :  : DEC T(TA) P(B£P) K(A38)
 :  : DEC T(OG) P() K(SEGRU.A38)
 :  : DEC T(OG) P() K(SESEZ.A38)
 :  : DEC T(OG) P() K(SESUB.A38)

# Connettori disponibili

Con il client Looc.UP vengono distribuiti dei connettori predefiniti, disponibili per l'uso senza la necessità di installare software integrativo.

# WS :  Connettore per invocazione di Web Service su Smeup Provider remoto

Consente l'accesso a funzioni Smeu.Up esposte come web service su uno Smeup Provider remoto

Esiste in due versioni : 

## Connettore LOA38_WS di tipo stateless

Esegue accessi al web service remoto di tipo stateless.
Ogni richiesta è pertanto gestita in 3 fasi distinte, eseguite in sequenza : 


- Connessione al webservice remoto e autenticazione sul server di riferimento con le credenziali fornite (utente, password, ambiente)
- Esecuzione della FUN passata e lettura XML di risposta
- Disconnessione


Esempio di script (vedi LOA38_WS su server sviluppo) : 

 :  : SEZ Cod="S00" Txt="Accesso a Smeup Provider remoto tramite Web Service"
 :  : A38.CLSSEZ Class="**Smeup.smeui.loa38.smeupprovider.SLWSLOA38Connector**" Pgm=""
 :  : A38.CNFSEZ Name="HTTPS" Value="0"
 :  : A38.CNFSEZ Name="SERVICE" Value="127.0.0.1"
 :  : A38.CNFSEZ Name="PORT" Value="9090"
 :  : SUB Cod="B00" Txt="Invocazione WS" Timeout="100000"
 :  : A38.SUBMET Value="SLWSINVOKE" Txt="Nome che identifica la funzione"
 :  : A38.SUBVAR Name="SYSTEM" Value="" Txt="Server di destinazione della FUN" DftVal=""
 :  : A38.SUBVAR Name="USR" Value="" Txt="Utente" DftVal=""
 :  : A38.SUBVAR Name="PWD" Value="" Txt="Password" DftVal=""
 :  : A38.SUBVAR Name="ENV" Value="" Txt="Ambiente" DftVal=""
 :  : A38.SUBVAR Name="FUN" Value="" Txt="FUN richiesta (deve tornare matrice XML)" DftVal=""


## Connettore LOA38_WS con gestione del pool di connessioni

Consente l'accesso utilizzando un pool di connessioni predefinite e create in fase di inizializzazione del connettore
La gestione è pertanto del seguente tipo : 


- All'avvio del connettore WS vengono create N connessioni con lo Smeup Provider remoto che fornisce il web service
- Quando viene richiesta una FUN, viene allocata una delle connessioni attive e viene usata per l'invocazione su web service della FUN richiesta. Alla risposta la connessione viene tornata al pool.
- Se nessuna connessione è disponibile, la richiesta di esecuzione viene messa in coda.


Le connessioni che appartengono al pool sono tutte dello stesso tipo e pertanto condividono le stesse credenziali,
definire nella configurazione a livello di sezione. Il richiamo della singola funzione deve quindi specificare la sola
FUN da eseguire.

Esempio di script (vedi SCP_SET/LOA38_WS su server sviluppo)

 :  : SEZ Cod="S01" Txt="Esempio connettore WS pooled"
 :  : A38.CLSSEZ Class="**Smeup.smeui.loa38.smeupprovider.WSLOA38Connector**" Pgm=""
 :  : A38.CNFSEZ Name="SIZE" Value="3"
 :  : A38.CNFSEZ Name="HTTPS" Value="0"
 :  : A38.CNFSEZ Name="SERVICE" Value="127.0.0.1"
 :  : A38.CNFSEZ Name="PORT" Value="9090"
 :  : A38.CNFSEZ Name="SYSTEM" Value="srvlab01.smeup.com"
 :  : A38.CNFSEZ Name="USR" Value="FORDAR"
 :  : A38.CNFSEZ Name="PWD" Value="dario0316"
 :  : A38.CNFSEZ Name="ENV" Value="0010"
 :  : A38.CNFSEZ Name="TIMEOUT" Value="300"
 :  : SUB Cod="B00" Txt="Invocazione WS" Timeout="100000"
 :  : A38.SUBMET Value="WSINVOKE" Txt="Nome che identifica la funzione"
 :  : A38.SUBVAR Name="FUN" Value="" DftVal="" Txt="FUN richiesta (deve tornare matrice XML)"

si noti il parametro **SIZE** che identifica il numero di connessioni create nel pool in fase di inizializzazione e il parametro
**TIMEOUT** che definisce il tempo di attesa (in secondi) di una risposta da parte del web service remoto prima che la
richiesta sia considerata fallita e la connessione ritornata al pool.



# 39 :  Connettore per invocazione di servizi A39 su Smeup Provider remoto

Consente l'accesso a funzioni A39 esposte da uno Smeup Provider remoto

Esiste in due versioni : 

## Connettore LOA38_39 di tipo stateless

Esegue richieste A39 allo Smeup Provider remoto senza mantenere a connessione attiva
Ogni richiesta è pertanto gestita in 3 fasi distinte, eseguite in sequenza : 


- Connessione allo Smeup Provider remoto e autenticazione sul server di riferimento con le credenziali fornite (utente, password, ambiente)
- Esecuzione della funzione A39 richiesta e lettura XML di risposta
- Disconnessione


Esempio di script (vedi SCP_SET/LOA38_39 su server sviluppo) : 

-- Accesso A39 remoto di tipo stateless (connessione-call-disconnessione)

 :  : SEZ Cod="A39SL" Txt="Accesso a Smeup Provider remoto tramite A39 stateless"
 :  : A38.CLSSEZ Class="**Smeup.smeui.loa38.smeupprovider.SLA39LOA38Connector**" Pgm=""
 :  : A38.CNFSEZ Name="HTTPS" Value="0"
 :  : A38.CNFSEZ Name="SERVICE" Value="127.0.0.1"
 :  : A38.CNFSEZ Name="PORT" Value="9090"
 :  : A38.CNFSEZ Name="SYSTEM" Value="" Txt="Server di destinazione della FUN" DftVal=""
 :  : A38.CNFSEZ Name="USR" Value="" Txt="Utente" DftVal=""
 :  : A38.CNFSEZ Name="PWD" Value="" Txt="Password" DftVal=""
 :  : A38.CNFSEZ Name="ENV" Value="" Txt="Ambiente" DftVal=""
 :  : SUB Cod="DEC" Txt="Lettura DEC di un oggetto" Timeout="3000"
 :  : A38.SUBMET Value="DEC" Txt="Decodifica oggetto"
 :  : A38.SUBVAR Name="FUN" Value="" DftVal="DEC" Txt="DEC su A39_MU"
 :  : A38.SUBVAR Name="TIPO" Value="" Txt="Tipo oggetto"
 :  : A38.SUBVAR Name="PARAMETRO" Value="" Txt="Parametro oggetto"
 :  : A38.SUBVAR Name="CODICE" Value="" Txt="Codice oggetto"

**N.B. : **Si noti che la variabile di sezione FUN deve essere inizializzata con un valore di default uguale al nome della funzione A39 che
si vuole invocare. Nell'esempio si la sezione DEC è pensata per il richiamo della funzione A39 remota con nome "DEC"

**N.B. : **Le variabili successive alla FUN sono le stesse variabili attese dalla funzione A39 remota. In questo esempio la funzione
remota DEC esegue la decodifica di un oggetto quindi si attende le variabili TIPO, PARAMETRO e CODICE. Ovviamente funzioni
remote diverse hanno un set di parametri diversi, quindi la parte di script successiva al campo FUN ha una struttura che dipende
dalla funzione A39 chiamata. Il connettore è in grado di leggere tutte le variabili successive alla FUN e
passarle correttamente alla funzione A39 invocata.

## Connettore LOA38_39 con gestione del pool di connessioni

Consente l'accesso ai servizi A39 offerti da uno Smeup Provider remoto utilizzando un pool di connessioni
predefinite e create in fase di inizializzazione del connettore.
La gestione è pertanto del seguente tipo : 


- All'avvio del connettore WS vengono create N connessioni con lo Smeup Provider remoto che fornisce il web service
- Quando viene richiesta una funzione A39, una delle connessioni disponibili viene allocata ed utilizzata per la
comunicazione con il servizio A39 remoto. Eseguita la richiesta la connessione viene liberata per utilizzi futuri.
- Se nessuna connessione è disponibile, la richiesta di esecuzione viene messa in coda.


Le connessioni che appartengono al pool sono tutte dello stesso tipo e pertanto condividono le stesse credenziali,
definire nella configurazione a livello di sezione. Il richiamo della singola funzione deve quindi specificare la sola
FUN da eseguire.

Esempio di script (vedi SCP_SET/LOA38_39 su server sviluppo) : 

-- Accesso A39 remoto con pool di connessioni

 :  : SEZ Cod="A39" Txt="Esempio connettore A39"
 :  : A38.CLSSEZ Class="**Smeup.smeui.loa38.smeupprovider.A39LOA38Connector**" Pgm=""
 :  : A38.CNFSEZ Name="SIZE" Value="3"
 :  : A38.CNFSEZ Name="HTTPS" Value="0"
 :  : A38.CNFSEZ Name="SERVICE" Value="127.0.0.1"
 :  : A38.CNFSEZ Name="PORT" Value="9090"
 :  : A38.CNFSEZ Name="SYSTEM" Value="srvlab01.smeup.com"
 :  : A38.CNFSEZ Name="USR" Value="USER"
 :  : A38.CNFSEZ Name="PWD" Value="PASSWORD"
 :  : A38.CNFSEZ Name="ENV" Value="0010"
 :  : A38.CNFSEZ Name="TIMEOUT" Value="300"
 :  : SUB Cod="DEC" Txt="Lettura DEC di un oggetto" Timeout="3000"
 :  : A38.SUBMET Value="DEC" Txt="Decodifica oggetto"
 :  : A38.SUBVAR Name="FUN" Value="" DftVal="DEC" Txt="DEC su A39_MU"
 :  : A38.SUBVAR Name="TIPO" Value="" Txt="Tipo oggetto"
 :  : A38.SUBVAR Name="PARAMETRO" Value="" Txt="Parametro oggetto"
 :  : A38.SUBVAR Name="CODICE" Value="" Txt="Codice oggetto"


si noti il parametro **SIZE** che identifica il numero di connessioni create nel pool in fase di inizializzazione e il parametro
**TIMEOUT** che definisce il tempo di attesa (in secondi) di una risposta da parte del web service remoto prima che la
richiesta sia considerata fallita e la connessione ritornata al pool.

**N.B. : **Si noti anche che la variabile di sezione FUN deve essere inizializzata con un valore di default uguale al nome della funzione A39 che
si vuole invocare. Nell'esempio si la sezione DEC è pensata per il richiamo della funzione A39 remota con nome "DEC"

**N.B. : **Le variabili successive alla FUN sono le stesse variabili attese dalla funzione A39 remota. In questo esempio la funzione
remota DEC esegue la decodifica di un oggetto quindi si attende le variabili TIPO, PARAMETRO e CODICE. Ovviamente funzioni
remote diverse hanno un set di parametri diversi, quindi la parte di script successiva al campo FUN ha una struttura che dipende
dalla funzione A39 chiamata. Il connettore è in grado di leggere tutte le variabili successive alla FUN e
passarle correttamente alla funzione A39 invocata.

# UP :  Connettore per l'upload di file su Smeup Provider remoto

Consente di effettuare l'upload di un file su uno Smeup Provider remoto. Il file uploadato può essere salvato sia sul file system
dello SmeupProvider (o di un server da esso accessibile) sia nel IFS del sistema iSeries a cui è connesso il provider.

Esempio di script (vedi SCP_SET/LOA38_UP su server sviluppo) : 

 :  : SEZ Cod="S00" Txt="Upload di un file su Smeup Provider remoto"
 :  : A38.CLSSEZ Class="**Smeup.smeui.loa38.smeupprovider.FileUploadLOA38Connector**" Pgm=""
 :  : A38.CNFSEZ Name="HTTPS" Value="0"
 :  : A38.CNFSEZ Name="SERVICE" Value="127.0.0.1"
 :  : A38.CNFSEZ Name="PORT" Value="9090"
 :  : SUB Cod="B00" Txt="File upload" Timeout="100000"
 :  : A38.SUBMET Value="UPLOAD" Txt="Nome che identifica la funzione"
 :  : A38.SUBVAR Name="SYSTEM" Value="srvlab01.smeup.com"
 :  : A38.SUBVAR Name="USR" Value="USER"
 :  : A38.SUBVAR Name="PWD" Value="PASSWORD"
 :  : A38.SUBVAR Name="ENV" Value="0010"
 :  : A38.SUBVAR Name="FILE" Value="" Txt="Path del file da caricare" DftVal=""
 :  : A38.SUBVAR Name="FS_DEST" Value="" Txt="Destinazione su FS" DftVal=""
 :  : A38.SUBVAR Name="IFS_DEST" Value="" Txt="Destinazione su IFS" DftVal=""
 :  : A38.SUBVAR Name="OVERWRITE" Value="" Txt="Sovrascrivi (0/1) (opt.)" DftVal=""
 :  : A38.SUBVAR Name="CRC32" Value="" Txt="CRC file (opt, per controllo)" DftVal=""
 :  : A38.SUBVAR Name="FILE_SIZE" Value="" Txt="Dimensione file (opt, per controllo)" DftVal=""
 :  : A38.SUBVAR Name="LAST_MODIFIED" Value="" Txt="Last mod. file (opt, per controllo)" DftVal=""
 :  : A38.SUBVAR Name="DES_TYPE" Value="" Txt="Tipo destinazione (opt.)" DftVal=""

Le variabili vanno valorizzate opportunamente a seconda dell'operazione desiderata


- Se si valorizza la variabile FS_DEST, il file uploadato verrà salvato nel file system dello Smeup Provider nella posizione
definita dal valore passato
- Se si valorizza la variabile IFS_DEST, il file uploadato verrà salvato nel file IFS del sistema iSeries connesso allo Smeup Provider nella posizione
definita dal valore passato


Ovviamente solo una delle variabili FS_DEST e IFS_DEST deve essere valorizzata, se entrambe son definite verrà considerata la
sola variabile FS_DEST.

Le variabili con **opt** nella descrizione sono da considerare opzionali.

La funzione di upload di un file risponde con un file XML di conferma spedizione oppure, in caso di errore, con un
messaggio di warning.

Per l'interfaccia ai webservice si rimanda alla documentazione specifica dell'API K11 : 
- [TST Integrazione con webservice](Sorgenti/MB/DOC_OGG/P_TSTK11)
