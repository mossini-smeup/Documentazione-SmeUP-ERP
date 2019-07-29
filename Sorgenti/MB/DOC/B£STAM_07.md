## Premessa
AOP Rappresenta un'infrastruttura software di 'output production' intesa a generare documenti a layout dinamico avanzato indirizzati sia verso stampanti fisiche che registrati nel formato file portabile Adobe PDF di tipo attivo.
I documenti incapsulati in files PDF dovranno essere disposti in un filesystem repository non indicizzato. Il nome del file PDF e la sua collocazione fisica saranno inclusi come proprietà direttamente dall'ambiente gestionale su iSeries .
L'interazione del servizio con il  gestionale su iSeries sarà reso possibile attraverso un file XML transazionale strutturato, conforme alle specifiche w3.org nella sua formulazione di base,  per il quale verrà deciso uno specifico schema XSD mandatorio attualmente indicato solo a scopo introduttivo.
La strutturazione dei campi e dei relativi contenuti saranno organizzati in ambito gestionale su iSeries, eventuali feedback provenienti dall'ambiente di emissione, saranno conformi alle regole prestabilite.
Il servizio da qui chiamato 'Advanced Output Production (AOP)' dovrà essere utilizzabile sia in uno stesso dominio di networking, installazioni quindi completamente in rete aziendale lan/intranet, o in ambito dislocato, utilizzando alcuni principi della logica di clouding intesa come decentralizzazione organizzata e trasparente dei dati, dei processi o di entrambi.
Come procedura accessoria iniziale dovrà essere prevista la trasmissione dei documenti generati nel formato Adobe PDF attraverso messaggi mail semplificati senza alcuna procedura di feedback, il processo potrà prevedere l'inserimento dei dati di testata email 'from, to, cc, ccn, subject e body-text (txt o html)' così come generati nel file transazionale originale da procedura gestionale.

## Cos'è il prodotto AOP (Advanced Output Production)
AOP è uno strumento nato per implementare le seguenti funzionalità : 
* emissione di documenti ad alto contenuto grafico
* invio come allegati e-mail dei documenti prodotti
* archiviazione in repositories dei documenti prodotti
* stampa cartacea dei documenti prodotti
AOP non si occupa di : 
* Gestione fax
* Postalizzazione cartacea
* Archiviazione sostitutiva
* Archiviazione relazionale
* Archiviazione outsourcing
* Store&forward Fax
* Trasmissione e ricezione SMS

Tale prodotto è un applicazione server avviabile, su ambiente Windows, sia in modalità interattiva sia come servizio, che svolge le attività suddette ricevendo i file dati tramite una cartella che viene monitorata.
Le attività svolte da AOP sono definite tramite un file dati che viene fornito da Sme UP ERP. Tale file fornisce i dati relativi ad uno o più documenti e le azioni che andranno applicate a tali dati. Il file di interfaccia è un file con una estenzione ben specifica :  S00. Tale file è a tutti gli effetti un file XML con un dtd definito.

## Attivazione
Attaverso la tabella di impostazione B£5.
In tale tabella è presente il campo **Attiva funzioni AOP**
 :  : DEC T(TA) P(B£5) K(*)

## Configurazione
La configurazione del modello AOP risiede nello script SCP_AOP
Per definire la parte variabile del layout si utilizzano le variabili di tipo contesto. ( CO.xxxxx )  definite nel contesto B£H53G.
Sarà compito dello sviluppatore generare le relative variabili.
Se indicato un modello Mail, le variabili di contesto da applicare nella mail, devono essere instanziate con lo stesso nome del modello mail definito tramite il costruttore A17.

## Generazione della stampa
La stampa viene indirizzata verso AOP solo se il programma di stampa è stato implementato con le relative funzioni.
Il nome della configurazione e l'indirizzamento verso AOP è governato dalla GPE.

### Descrizione del formato S00
Il file S00 di interscanbio con AOP ha una struttura ben definita.
Qui di seguito la spiegazione di tale struttura : 
* Versione XML
* EndPoint che processerà l'XML
* Alias (a.k.a. Dominio)
* Contenitore dei dati da elaborare (Production)
** Esecuzioni (Performs)
*** Singola esecuzione (Perform)
**** Azioni (Actions)
***** Singola azione (Action)
**** Lavori (DataJobs)
***** Singolo lavoro (DataJob)
****** Dichiarazione del modello di layout da utilizzare (LayoutModelAlias)
****** Pagine del lavoro (JobPages).
******* Singola pagine del lavoro (JobPage) Il concetto di documento che diventerà PDF è qui!!!
******** Tabella (BodyRecords)
********* Riga di tabella (BodyRecord)
********** Lista campi (RecordFields)
*********** Singolo Campo (RecordField)
************* Nome Campo (RecordFieldName)
************* Valore Campo (RecordFieldContent)
******** Lista Variabili (Variables)
********* Singola Variabile (Variable)
********** Nome Variabile (VariableName)
********** Valore Variabile (VariableContent)

## /copy £AOP
Per generalizzare la costruzione del modello AOP è stata progettata la relativa api "AOP".
Esistono ad oggi due modalità di generazione del modello AOP : 
* Attraverso una funzione che restituisce un xml di tipo "Matrice"
* Attraverso il passaggio diretto delle variabili

Ora vediamo in dettaglio le funzioni della api £AOP che permettono di comporre da programma l'XML.
 :  : PAR L(TAB)
Sequenza|Funzione|Descrizione
001|AOP.INZ|Costrusce la parte iniziale della struttura AOP e instanzia l'elemento nello spool di stato 00
002a|AOP.PGI|Inizializza la pagina dati (intesa come documento da produrre).
002b|AOP.AZI|Aggiunge un'azione di trattamento dei dati contenuti nella pagina appena inizializzata.
002c|AOP.PGF|Chiude la pagina dati .
002|AOP.PAG|Con il limite di poter definire solo le azioni previste nello script SCP_AOP utilizzato e nessun azione aggiuntiva, raccoglie le tre operazioni precedenti. In definitiva costruisce le azioni da intraprendere sul documento prendendole dallo script SCP_AOP. Se passata la funzione i passi dal livello 003 al livello 005 non devono essere eseguiti.
002|AOP.MOD|Permette di effettuare un cambio modulo su cambio pagina dati all'interno di uno stesso S00.
002|AOP.RIG|Richiamato da AOP.MOD solo se viene passata la funzione di una matrice. Questo metodo permette di trasformare un xml prodotto da una funzione che genera xml di matrice in un file S00
003|AOP.OJB|Apri il Job
004|AOP.OBD|Apro il record
004|AOP.OBR|Apro il campo
004|AOP.ABR|Aggiungi campo
004|AOP.CBR|Chiudo il campo
004|AOP.CBD|Chiudo il record
004|AOP.OVA|Apri campo di pagina
004|AOP.AVA|Aggiungi campo di pagina
004|AOP.CVA|Chiudi il campo di pagina
005|AOP.CJB|Chiudi il Job
006|AOP.CLO|Chiudi il documento
007|AOP.INV|Invia il documento al server AOP
007|AOP.RET|Legge i feddback dal server AOP e li collega agli eventi collegati

Se si vuole aggiungere più pagine nel documento AOP bisogna rieseguire i passi dal livello 002 all livello 005.

Nel file SCP_AOP esiste un membro per ogni tipo documento (template) AOP. Il nome del membro è identico al nome del template. Dentro questo membro sono definite le variabili di inizializzazione del file S00 che vengono appunto riportate nel file ogni volta che di un documento di un tipo viene lanciata la generazione : 
* AIve :  versione
* AIep :  nome Endpoint AOP
* AIdo :  Dominio AOP
* AMmo :  Nome modulo
* APnm :  Nome stampante
* ASpe :  Percorso file da generare
* ASnm :  Nome file da generare
* ASpw :  Password modifica del PDF
* AIsa :  System Administrator database
* AIut :  Utente di sistema
* AIpw :  password Alut
* AIpg :  Exit da utilizzare per comporre i comandi FTP di invio dell'xml al server AOP
* AIe3 :  Abilita la registrazione degli eventi per la verifica dell'esito delle azioni AOP

I campi sono definiti nello script SCP_CFG/EDT_AOP

Nella B§H va definito l'indirizzo del server AOP.

### Creazione XML attraverso una funzione che restituisce un xml di tipo "Matrice"
L'XML restituito dalla funzione deve essere in formato matrice.
La gliglia e i record della stessa vengono trasformati in campi di record mentre la cover viene trasformata in campi di pagina.

## Come viene prodotto il file S00
In seguito verrà preso ad esempio la situazione di generazione delle fatture di ciclo attivo come esemplificativo del funzionamento del meccanismo di integrazione..
Nello standard Sme UP viene prodotto il file S00attraverso uil programma V5FA01S che, se sente impostato il modello AOP, produce il suddetto file S00 e lo spedisce al server AOP
## Come viene fornito il file S00 ad AOP
Qualora non sia stata impostata nel relativo script SCP_AOP la modalità di simulazione, il file S00, una volta prodotto, viene passato al server AOP sempre tramite /copy AOP. Il metodo di trasferimento è l'FTP, il server FTP deve essere attivo e correttamente configurato sulla macchina che ospita AOP.
## La risposta di AOP
Una volta che AOP ha elaborato un file S00, restituisce una risposta in una cartella adibita a contenerle che verranno poi acquisite, sempre tramite al /copy AOP, da Sme.UP e serviranno a popolare un database che permette di monitorare lo storico delle operazioni effettuate tramite AOP.
Tale risposta è il file S00 originale corredato delle informazioni, passate in determinati nodi del XML, relative agli esiti delle operazioni e, eventualmente, dei codici di errore per identificare cosa è andato male. Tali informazioni sono consultabili tramite la scheda B£STAM.

## Descrizione dei campi del documento
La descrizione dei campi definiti nel file S00 va inserita nei relativi script delle voci :  nel file DOC_VOC, vanno previsti gli script A_NOME-DELLO-SCRIPT-IN-SCP_AOP.
Al momento è stato definita una nomenclatura di questo tipo :  SME.XXX.YYY dove XXX e YYY sono liberi. Non v'è al momento distinzione fra campi e variabili.

## Procedimento di lavoro
Come si crea di un template per la generazione di un tipo di documento
**Costruire XML S00**
Innanzitutto identificato la massa di dati che dovranno essere emessi nel documento :  variabili di testata e di piede, record dei campi da sviluppare.
Con tali dati va poi costituito il file S00 tramite la /copy £AOP.
Una volta ottenuto il file S00 si può passare alla crezione del template del documento grafico
**Creazione template**
Tramite i ìl designer di AOP va creato un template (from scratch o per copia di un'esistente) cui verrà agganciato il file S00 come database per fornire la struttura dati.di prova.
Una volta agganciato il file S00 va gestito la'spetto grafico del template.
Quindi va salvato il template con il nome che verrà poi riportato nello script SCP_AOP/NOMETEMPLATE in Sme.UP come attributo AMmo.
E' stato stabilito che il nome del template coincida, ove possibile, coincida con il nome del programma di stampa che genera il file S00.
**Avvio monitor AOP**
Il monitor AOP tiene controllata la cartella di input dove il programma si aspetta di ricevere i file S00.

## Esempi di implementazione delle chiamate AOP in un pgm esistente di stampa
Come precedentemente accennato si faccia riferimento al programma di stampa fattura V5FA01S per prendere spunto (altri programmi sono il V5BO01S ed il V5OA01S)

## Architettura della soluzione AOP
![B£STAM_01](http://localhost:3000/immagini/B£STAM_07/BXSTAM_01.png)Vista l'importanza delle stampe generate da Sme.UP, si consiglia l'utilizzo di un server fisico o virtuale dedicato al ruolo AOP avente le seguenti caratteristiche : 
* Sistema Operativo :  Windows Server 2008 o superiori (nel caso che il volume di stampe sia basso può essere utilizzato anche un sistema operativo client Windows XP o Windows 7)
* Ram :  2 Gb o più
* .Net framework 4.0 redistributable
* Ruolo FTP Server
* Ruolo Print and Document Services
* SQL Express 2008R2 con strumenti di amministrazione, installato come Default Instance con Mixed Authentication.
* N° di Server AOP :  uno per ogni sede del cliente, solo nel caso di un numero basso di stampe sul remoto, si può testare l'utilizzo di un solo server che vede le stampanti remote.

## L'editor AOP
La manutenzione dei modelli di layout passa attraverso l'utilizzo dell'editor a support del server.
Per cominciare si deve avviare il programma di amministrazione e disegno di AOP 'Medusa.Xtrategy.Production.Server.Admin.exe'.
![B£STAM_02](http://localhost:3000/immagini/B£STAM_07/BXSTAM_02.png)Quindi è necessario selezionare (o creare e poi selezionare) un alias, all'interno del quale gestire un modello esistente (o creare e gestirne un nuovo)
![B£STAM_17](http://localhost:3000/immagini/B£STAM_07/BXSTAM_17.png)Agganciare un esempio di file S00 associato al modello
![B£STAM_18](http://localhost:3000/immagini/B£STAM_07/BXSTAM_18.png)Caricare la struttura dati
![B£STAM_19](http://localhost:3000/immagini/B£STAM_07/BXSTAM_19.png)Aprire l'editor
![B£STAM_21](http://localhost:3000/immagini/B£STAM_07/BXSTAM_21.png)Utilizzare l'editor per l'implementazione grafica

Sono disponibili, attraverso la finestra di amministrazione, gestire alcune altre funzioni : 

Esportare i file verso un altro editor o importare i file da un altro editor
![B£STAM_20](http://localhost:3000/immagini/B£STAM_07/BXSTAM_20.png)Esportare i file per il deploy su EndPoint (XTableLayoutModel)
![B£STAM_22](http://localhost:3000/immagini/B£STAM_07/BXSTAM_22.png)
Nota :  Il file salvato avrà estensione 'XLayoutModel' e in questo contesto può essere modificato manualmente.
Nota :  Se ad esempio è necessario modificare il path relativo dei link alle immagini contenute nel modello, può essere utile intervenire direttamente attraverso una ricerca/sostituzione nel file ricercando il nome dell'immagine alla quale modificare il percorso. Fondamentale però considerare che qualsiasi modifica inpropria al file può determinare malfunzionamenti, prestare la massima attenzione alle modifiche mantenendo logica e struttura, eseguire sempre un backup preventivo.

## Installazione AOP
Il software per la generazione dei PDF Medusa AOP allo stato attuale deve essere installato manualmente.
Il presente documento illustra i passi necessari e le limitazioni correnti.
Medusa AOP può essere installato su qualunque server i cui servizi non siano in conflitto con l'installazione di MS SQL Server, dedicato o meno.
Questa documentazione è prodotta per l'installazione su di un Windows Server 2008 64 Bit

### PREREQUISITI
Software
* Windows 2008 minimo
* .Net framework 4.0 redistributable
* Ruolo FTP Server
* Ruolo Print and Document Services
* SQL Express 2008R2 con strumenti di amministrazione, installato come Default Instance con Mixed Authentication.

### INSTALLAZIONE
**Utenze, Group memberhip e User Right assignements**
E' necessario creare un'utenza nel dominio e non di dominio al quale appartiene il server AOP, normalmente : 
User :  Medusa
Password :  Medusa2011
Tale utenza deve essere membro dei seguenti gruppi locali al server o di dominio : 
* Print Operators
* Remote Desktop users
Deve anche avere i seguenti diritti locali (Local Security Policies) sul server in questione : 
* Allow logon locally
* Logon as a Service
Se la condivisione dove vengono memorizzati i PDF risiede sullo AS400 deve essere anche creato un utente AS400 con medesimo nome e password ed i diritti completi sulla share IFS ed eventuale percorso.

**File System**
Creare sulla root di uno dei dischi (normalmente C : \) una cartelle AOP.
Assegnare all'utenza Medusa i diritti di Full Control sulla cartella appena creata.
Copiare l'intero contenuto della cartella AOP master sulla cartella AOP del nuovo server.
Copiare i files (non le cartelle) contenuti in C : \AOP\Production\system in : 
* C : \windows\System32
* C : \Windows\SysWOW64 (vale solo per windows 2008)

### INIZIALIZZAZIONE DB
Aprire SQL Server Management studio ed eseguire le query oppure se sql è associato lanciare direttamente questi file : 
* C : \AOP\SQLScripts\CreateDatabase
* C : \AOP\SQLScripts\DatabaseStructure
* C : \AOP\SQLScripts\Update



### CONFIGURAZIONE
* Sito FTP :  Creare un nuovo sito FTP che punti a C : \AOP\Production\FTPBase configurando i permessi di accesso in lettura e scrittura all'utente <DOMINIO AD>\Medusa
* Generare Licenza :  Lanciare il file C : \AOP\Production\AOPLicencer.exe
** Cliccare su Genera e fornire i dati al personale Medusa che ritornerà una KEY che andrà messa nel parametro  AOPAuthCode che troverete al punto 6.3.1
** Il codice di identificativo applicazione deve essere messo nella variabile AOPUId che troverete al punto 6.3.1.
* Configurazione Medusa :  E' necessario modificare manualmente due file di configurazione come illustrato nei due punti seguenti.

Le parti in  blu si riferiscono a nomi e percorsi, quelle in  arancione alla configurazione con autenticazione SQL (non trattata in questo documento)

C : \AOP\Production\Medusa.Xtrategy.Production.Endpoint.exe.config
Inserire il nome del server (nell'esempio QSVM001) nella sezione seguente : 

< connectionStrings >
< !-- Integrated Security=False;User ID=sa;Password=Medusa2011;Pooling=False"-- >
< add name="Medusa.Xtrategy.Production.EndPoint.My.MySettings.XtrategyPSDbConnectionString" Info=True;Integrated Security=True;" providerName="System.Data.SqlClient" / >
< /connectionStrings >

Inserire il nome del server smtp (nell'esempio smtp.smeup.local) nella sezione seguente, se tale server richiede l'autenticazione inserire il nome utente necessario.
< startup >
< supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/ >
< /startup >< applicationSettings >
< Medusa.Xtrategy.Production.EndPoint.My.MySettings >
< setting name="AOPSupportPath" serializeAs="String" >
< value >C : \AOP\Production\Support< /value >
< /setting >
< setting name="AOPInputPath" serializeAs="String" >
< value >C : \AOP\Production\FTPBase\In< /value >
< /setting >
< setting name="AOPOutpuPath" serializeAs="String" >
< value >C : \AOP\Production\FTPBase\Out< /value >
< /setting >
< setting name="SMTPServerAddress" serializeAs="String" >
< value >smtp.smeup.local< /value >
< /setting >
< setting name="SMTPServerPort" serializeAs="String" >
< value >25< /value >
< /setting >
< setting name="SMTPAuthUser" serializeAs="String" >
< value >medusa< /value >
< /setting >
< setting name="SMTPAuthPassword" serializeAs="String" >
< value >Medusa2011< /value >
< /setting >
< setting name="EnableInnerProductionLogging" serializeAs="String" >
< value >True< /value >
< /setting >
< setting name="AOPUId" serializeAs="String" >
< /setting >
< setting name="AOPAuthCode" serializeAs="String" >
< /setting >
< /Medusa.Xtrategy.Production.EndPoint.My.MySettings >
< /applicationSettings >
< value >09acf647-5bce-4594-86cd-d0678f2e021f< /value >
< /setting >
< setting name="AOPAuthCode" serializeAs="String" >
< value >2bab7f9e5434a1e618ec2769e3222c8d< /value >
< /setting >
< /Medusa.Xtrategy.Production.EndPoint.My.MySettings >
< /applicationSettings >

### C : \AOP\Production\Medusa.Xtrategy.Production.server.admin.exe.config
E' necessario inserire il nome del server (nell'esempio QSVM001)
< connectionStrings >
< !--Integrated Security=False;User ID=sa;Password=Medusa2011;Pooling=False"-- >
< add name="Medusa.Xtrategy.Production.Server.Admin.My.MySettings.XtrategyPSDbConnectionString" connectionString="Data Source=qsvm001;Initial Catalog=XtrategyPSDb;Persist Security Info=True;Integrated Security=True;" providerName="System.Data.SqlClient"/ >
< !-- Possibile configurazione alternativa con sicurezza integrata logon. -- >
< !--add name="DatabaseConnection" connectionString="Persist Security Info=True;Integrated Security=True";database=XtrategyPSDb;server=(local);" providerName="System.Data.SqlClient" /-- >
</connectionStrings>
