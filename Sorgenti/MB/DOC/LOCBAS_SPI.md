# Installazione e configurazione di Sme.UP Provider


## Getting Started

Installare e configurare Sme.UP Provider è un'operazione in generale semplice; tutte le complicazioni sono legate alle differenti esigenze di utilizzo e configurazione e vanno affrontate se necessario.

La figura sottostante riassume i concetti primcipalei : 
Sme.UP Provider è un fornitore di servizi che espone questi servizio con protocollo HTTP.
Sme.UP Provider è collegato al server smeup tramite una normale connessione, con un utente dedicato.
I parametri di avvio possono essere passati da riga di comando o messi nel file wrapper.conf (nel caso di avvio come servizio windows)
Le altre configurazioni sono reperite dall'SCP_CLO come avviene per Looc.UP.

Di seguito un video che illustra l'installazione
[https://www.youtube.com/embed/CPd8zGRCiy4](https://www.youtube.com/embed/CPd8zGRCiy4)


![LOCBAS_049](http://localhost:3000/immagini/LOCBAS_SPI/LOCBAS_049.png)
I passi minimi per cominciare sono i seguenti : 

* Installare Sme.UP Provider
* Creare/Scegliere un utente AS400 Dedicato
* Creare il membro SCP_CLO/<Nome dell'utente scelto> nella libreria delle personalizzazioni del cliente (chiedere al responsabile applicativo), copiando SMEDEV/SCP_CLO/SMEUPPR_ES
* Avviare Sme.UP Provider
* Eseguire i test di primo avvio (vedi paragrafo "Passi per la prima esecuzione" per verificare che tutto sia stato fatto correttamente)


## Requisiti minimi di sistema

 * Server Windows __con sistema operativo supportato da Microsoft__, adeguatamente dimensionato in funzione del carico.
** Non sono supportati WIndows XP, Windows Server 2003 e tutti i precedenti
 * Adeguata infrastruttura di rete per poter rendere accessibile su internet/intranet la porta HTTP/HTTPS
 * Un utente Windows dedicato
 * Un utente AS400 dedicato


### Dimensionamento della macchina

**Abbiamo effettuato test di carico arrivando a 400 connessioni simultanee con una macchina così dimensionata : 
SO -  W2008 server R2 32bit
HW - Intel Xeon E5504 2GHZ 4 processori 3GB RAM
Possiamo dunque considerare questa configurazione come requisito minimo per il funzionamanto in un ambiente di produzione.


## Requisiti SmeUp

### Utente AS400

### Ambienti collegati
SmeUp Provider offre vari servizi.
I principali sono : 
 * esecuzione di funzioni batch
 * interfaccia con il mondo esterno
 * fornitore di risorse remote
 * fornitore di dati a WebUp
 * server di aggiornamento delle installazioni di LoocUp

In base al servizio richiesto è possibile avere ambienti applicativi differenti.
Un ambiente di produzione è necessario solo nel caso di interfaccia con il mondo esterno (PLC, bilance ecc).
Nel caso di funzioni batch si consiglia di sutilizzare specifici utenti es SMEUP_BCH, invece che quello dello Smeup Provider.
Le funzionalità rimanenti, richiedono la connessione solo per avere la configurazione di funzionamento, ma non richiedono ambienti di produzione.

Per verificare quali ambienti siano collegati all'utente impostato, effettuare le seguenti operazioni.
Avviare Smeup Provider utilizzando SmeupGo.
Nella maschera di login specificare AS400 utente e password. Lasciare il campo Ambiente vuoto".
Dopo la connessione, se compare una maschera con la scelta ambiente, significa che esiste più di un ambiente.
Se invece la connessione avviene immediatamente significa che esiste un solo ambiente applicativo.
In questo caso, nella configurazione NON va utilizzato il codice alfabetico dell'ambiente, ma o si utilizza il codice numerico, es 0010, oppure si lascia bianco.

## Requisiti Windows
Il provider per accedere ai file, si appoggia al sistema operativo che lo ospita, pertanto se deve accedere a file che sono in rete, vanno considerate le autorizzazioni dell'utente Windows.
Per verificare se il provider può accedere a una risorsa, collegarsi al server con l'utente windows che utilizza il provider e verificare se i file sono raggiungibili.
NOTA :  abbiamo verificato che quando il provider funziona come servizio su Windows 2008, non riesce ad accedere a file su cartelle di rete. In questo tipo di installazione è necessario avviarlo con gli script.

## Requisiti di rete

Sulla macchina in cui è installato il provider deve essere raggiungibile la porta HTTP/HTTPS
La porta è un parametro opzionale di avvio del Provider ( parametro --http:porta oppure --https:porta). Per i dettagli vedi il paragrafo sull'installazione.

Si consiglia di utilizzare il protocollo HTTPS in quanto, a  differenza del protocollo HTTP, i dati vengono criptati.

Sono poi possibili 3 configurazioni a sicurezza crescente : 

 * Viene pubblicata una porta del server windows
 * Come sopra ma il server viene messo in DMZ
 * Si crea una macchina che fa da proxy verso il server windows esponendo verso internet una porta, poi rigirata verso la porta su cui ascolta il provider.


## Possibili installazioni


### Installazione come applicazione interattiva
 * installare con amministratore della macchina o in generale porre attenzione ai requisiti
 * copiare i file **LOOCUP_SCP\startserver.cmd** e **LOOCUP_SCP\stopserver.cmd** in una cartella a scelta
 * modificare i due file con i parametri, come spiegato all'interno dei file stessi
 * schedulare la partenza/spegnimento nelle operazioni pianificate di windows agli orari che si ritengono più opportuni. In ogni caso ricordarsi di : 
 ** avviare il provider dopo l'AS400
 ** spegnere il provider  prima dell'AS400.

**Nota** - i parametri di avvio : 
Looc.UP Provider viene avviato dal file **startserver.cmd** attraverso l'eseguibile Smeupgo.exe
I parametri sono
 * **AS400**  :   Server AS400 Smeup
 * **UTENTE**  :   Utente di avvio (vedere il paragrafo configurazione)
 * **PASSWORD**  :   La password
 * **INGRESSO UTENTE**  :  Ambiente di esecuzione
 * **--server : CODA : PORTA_SERVER**   :  Definisce la coda di comunicazione con l'as400 **(6 CARATTERI ALFABETICI)  e la porta di comunicazione dei client Looc.UP
 * **--http(s):PORTA_HTTP(S)** : Definisce l'attivazione della modalità http(s) (obbligatoria) e la porta di accesso all'http(s) (opzionale, se non specificata assume 9090)


Altri parametri sono
 * **--loglevel : xxxxx** :  dove xxxxx può valere
 ** **DEBUG** :  massimo dettaglio nei log, utile in una fase iniziale o a fronte di segnalazioni di errori
 ** **INFO** :  modalità di funzionamento normale.
 ** **WARN** :  vengono loggate solo le condizioni di avviso
 ** **ERR** :  vengono loggate solo le condizioni di errore
 ** **OFF** :  nessun log. Impostazione sconsigliata :  vengono mantenuti solo i file di log degli ultimi 8 giorni. Tutti quelli più vecchi vengono automaticamente eliminati all'avvio del provider.
 * **pingperiod : nnnn** :  dove  nnnn è un valore numerico per specificare il periodo di ping in secondi. Il default per il provider è 3. Parametro disponibile dalla V5R1M161106.

### Installazione come servizio Windows

**NOTA :  si consiglia di installare su sistemi operativi Windows 2012 o superiore.**
In Windows 2003 SmeupProvider o non si avvia come servizio o non è in grado di accedere a file su altri server.
In Windows 2008 sono emersi problemi nell'accesso a file in rete.

Installare Sme.UP Provider con un **un utente amministratore locale, ma non LOCAL SYSTEM, che di fatto non è un utente.

L'utente di windows deve essere amministratore per poter consentire al provider di riavviarsi in autonomia in caso di caduta di uno dei suoi componenti.


Per configurare il servizio
**Per versioni di Provider precedenti alla Roma REV.1 (rilasciata in data 06/07/2017)**
 * andare nella cartella di installazione e nella sottocartella **serviceNT\conf**
 * se non si è già in possesso di un proprio file **wrapper.conf** precedentement configurato, creare una copia del file wrapper_default.conf chiamandola wrapper.conf
 * aprire il file **wrapper.conf** con un editor di testo
 * modificare le parti tra parentesi quadre. I parametri sono gli stessi dell'avvio : 
 ** **wrapper.app.parameter.2= AS400**  :   Server AS400 Smeup
 ** **wrapper.app.parameter.3= UTENTE**  :   Utente di avvio
 ** **wrapper.app.parameter.4= PASSWORD**  :   La password
 ** **wrapper.app.parameter.5= INGRESSO UTENTE**  :  Ambiente di esecuzione
 ** **wrapper.java.additional.1=-DSmeup.smeui.uiserverside.name=** :  Definisce la coda di comunicazione con l'as400 **(6 CARATTERI ALFABETICI)** La coda serve all'AS400 per richiedere l'esecuzione di funzioni al provider. Chiedere ad un installatore SmeUp se questa funzionalità serve oppure no, se non serve è comunque obbligatorio indicare un nome. Utilizzare ad esempio SMEPRO (verificare che nella libreria SMEUPUIDQ prima dell primo avvio del provider non esistano oggetti ECTSSMEPRO e ESTCSMEPRO)
 ** **wrapper.app.parameter.8=--http(s):[PORTA]** : Definisce l'attivazione della modalità http(s) e la porta di accesso all'http(s) (opzionale, se non specificata assume 9090)
 ** **wrapper.app.parameter.9=--loglevel : [LIVELLO]** :  Definisce il livello di log. Valori possibili per LIVELLO :  DEBUG,INFO(default), WARN, ERR, OFF.
 ** **wrapper.app.parameter.10=--enc : [XX]** :  definisce l'encoding del provider. Identifica il codice dell'encoding da usare. es U8

Parametri dispopnibili solo per la V5R1M161106 ROMA REV.1
 * **wrapper.app.parameter.11=--intserver** : modalità interattiva del provider
 * **wrapper.app.parameter.12=--sbs** : sottosistema_lavori_default_QBATCHUI
 * **wrapper.app.parameter.13=--nodblog** :  disabilitazione loggatura su database
 * **wrapper.app.parameter.14=--cleandb : nnnnF** : pulitura database log

**Operazioni da compiere**
 * lanciare **ServiceTest.bat**. Se è tutto configurato bene si aprirà la finestra di Sme.UP Provider. **Fare gli opportuni test**. Chiudere la finestra dos.
 * lanciare **ServiceInstall.bat**.
 * Aprire il **gestore dei servizi windows** (Strumenti di amministrazione, Servizi) e verificare che **SmeupProvider** sia presente.
 * Modificare le proprietà del servizio impostando l'utente di avvio. Deve essere **come minimo un utente amministratore locale, ma non LOCAL SYSTEM, che di fatto non è un utente!. Se il provider deve accedere al''IFS o ad altri server, utilizzare un opportuno utente di windows. Attenzione che provider installato come servizio NON è in grado di eseguire il comando JA_00_15;NET.AUT. Se questo comando è indispensabile, installare in modalità interattiva e far funzionare in console.
 * lanciare **ServiceStart.bat**.  **Fare gli opportuni test**.

### La pagina di debug
La pagina di debug consente di fare varie verifiche e di far eseguire funzioni al provider.
E' organizzata per sezioni :  in alto le operazioni principali (test della connessione e dei path), informazioni di base del provider e della sessione http.
Più in basso si trovano varie sezioni con cui testare
- la connessione a un IBMi
- testare la raggiungibilità di un server IBMi
- eseguire funzioni nella sessione del provider
- eseguire funzioni in sessioni secondarie
- leggere i file di log
- altri test

### Test consigliati
- aprire un browser e digitare http(s)://localhost:porta, il protocollo e la porta sono definiti nel wrapper :  se il provider è attivo compare una pagina con riportate le informazioni di base del provider. Verificare che risponda il provider configurato.
- se la pagina di debug si è attivata, utilizzare il pulsante "Lettura info di dettaglio (interroga server IBMi) - test paths". Verrà interrogato il provider via http(s), via coda server (necessario LOSER_51) e verrè testata la raggiungibilità e dei percorsi specificati in PROVIDER_PATHS. In fondo alla pagina, verranno riportate le informazioni di dettaglio ottenute.
- se localhost risponde, fare il test da un'altra macchina


**A partire dai Provider versione Roma REV.1 (rilasciata in data 06/07/2017) o successive**
Il file wrapper.conf è stato riorganizzato per rendere più agevole gestire la configurazione.
**N.B.** :  I vecchi file wrapper.conf **CONTINUANO A FUNZIONARE CORRETTAMENTE**

La gestione delle variabili di configurazione è stata divisa in due parti : 
* la parte di dichiarazione delle variabili
* la parte di utilizzo delle variabili

All'inizio del file è presente l'elenco delle variabili gestite
**Parametri di avvio OBBLIGATORI**
 * set.SMEUP_PROVIDER_CODE= [CODICE PROVIDER]
 * set.SMEUP_SYSTEM= [INDIRIZZO SISTEMA SMEUP]
 * set.SMEUP_USER= [UTENTE COLLEGAMENTO SISTEMA SMEUP]
 * set.SMEUP_PASSWORD= [PASSWORD UTENTE COLLEGAMENTO SISTEMA SMEUP]
 * set.SMEUP_ENV= [CODICE AMBIENTE SISTEMA SMEUP]
 * set.SMEUP_PROVIDER_SERVER_PORT= [PORTA TCP INTERFACCIA LOOCUP - univoca per ogni istanza Provider es. 9990]
 * set.SMEUP_PROVIDER_HTTP_PROTOCOL= [PROTOCOLLO INTERFACCIA HTTP - http, https]
 * set.SMEUP_PROVIDER_HTTP_PORT= [PORTA TCP INTERFACCIA HTTP - univoca per ogni istanza Provider es. 9090]


###  Parametri facoltativi il loro utilizzo richiede che venga decommentato il relativo parametro nella sezione wrapper.app.parameter
modifica il livello di log del provider  default è INFO, DEBUG= massimo dettaglio usare solo in fase di test
set.SMEUP_PROVIDER_LOGLEVEL= [LIVELLO LOG - INFO, ERROR, WARNING, DEBUG]


### sottosistema in cui funziona il provider migliora la gestione di eventuali disconnessioni
set.SMEUP_PROVIDER_SUBSYSTEM= [NOME SOTTOSISTEMA LAVORI PROVIDER ]
 * gestione log su DB :  valori possibili nnn(d/h/m/s)
 * dove nnn è un numero seguito da uno tra queste lettere : 
 * d = day (giorni)
 * h = hour (ore)
 * m = minuti
 * s = secondi
 * es. 8h significa che vengono mantenuti i log delle ultime 8 ore
 * NOTA per attivarlo commentare il parametro wrapper.app.parameter.13=--nodblog
set.CLEANDB_TIME= [TEMPO RIPULITURA LOG DB]



In questa sezione si trovano definite (con il comando **set.**) tutte le variabili previste dalla configurazione. Vanno valorizzate quelle che interessano (obbligatorio o opzionali che siano). Come nella versione precedente sono sicuramente indispensabili

 * set.SMEUP_PROVIDER_CODE= [CODICE PROVIDER]
 * set.SMEUP_SYSTEM= [INDIRIZZO SISTEMA SMEUP]
 * set.SMEUP_USER= [UTENTE COLLEGAMENTO SISTEMA SMEUP]
 * set.SMEUP_PASSWORD= [PASSWORD UTENTE COLLEGAMENTO SISTEMA SMEUP]
 * set.SMEUP_ENV= [CODICE AMBIENTE SISTEMA SMEUP]
 * set.SMEUP_PROVIDER_SERVER_PORT= [PORTA TCP INTERFACCIA LOOCUP - univoca per ogni istanza Provider es. 9990]
 * set.SMEUP_PROVIDER_HTTP_PROTOCOL= [PROTOCOLLO INTERFACCIA HTTP - http, https]
 * set.SMEUP_PROVIDER_HTTP_PORT= [PORTA TCP INTERFACCIA HTTP - univoca per ogni istanza Provider es. 9090]


quanto trovate fra parentesi quadre [] serve come indicazione del valore da inserire e, ove vi siano, l'elenco dei valori supportati. Es: **http, https** indica di scegliere fra questi due valori.

E' poi presente la sezione di utilizzo delle variabili

 :  : PAR F(03)
 - Application parameters.  Add parameters as needed starting from 1
wrapper.app.parameter.1=Smeup.smeui.uimainmodule.MainApplication
wrapper.app.parameter.2=%SMEUP_SYSTEM%
wrapper.app.parameter.3=%SMEUP_USER%
wrapper.app.parameter.4=%SMEUP_PASSWORD%
wrapper.app.parameter.5=%SMEUP_ENV%
wrapper.app.parameter.6=--server : %SMEUP_PROVIDER_CODE% : %SMEUP_PROVIDER_SERVER_PORT%
wrapper.app.parameter.7=--service : %SMEUP_PROVIDER_CODE%
wrapper.app.parameter.8=--%SMEUP_PROVIDER_HTTP_PROTOCOL% : %SMEUP_PROVIDER_HTTP_PORT%
 - wrapper.app.parameter.9=--loglevel : %SMEUP_PROVIDER_LOGLEVEL%
 - wrapper.app.parameter.10=--dbg
 - wrapper.app.parameter.10=--enc : U8
 - wrapper.app.parameter.11=--intserver
 - wrapper.app.parameter.12=--sbs : %SMEUP_PROVIDER_SUBSYSTEM%
wrapper.app.parameter.13=--nodblog
 - wrapper.app.parameter.14=--cleandb : %CLEANDB_TIME%



Nella configurazione di base non c'è nulla da toccare. Per ogni parametro verrà usato il valore impostato nella variabile cui fa riferimento.
I parametri obbligatori sono già attivati, quelli opzionali sono commentati tramite il carattere **-** ad inizio riga.
Qualora si voglia attivare uno dei parametrii opzionali va gestito il valore della variabile nella sezione di definizione, sostituendo alla spiegazione fra parentesi quadre il valore desiderato.
Es : 
la specifica
set.SMEUP_PROVIDER_LOGLEVEL= [LIVELLO LOG - INFO, ERROR, WARNING, DEBUG]
diventerà
set.SMEUP_PROVIDER_LOGLEVEL= DEBUG

Va quindi tolto il commento al relativo parametro perchè venga passato al Provider


NOTA

![LOCBAS_050](http://localhost:3000/immagini/LOCBAS_SPI/LOCBAS_050.png)

Se si volesse schedulare un avvio e spegnimento automatico, aggiungere due voci nelle operazioni pianificate : 
 * per l'avvio il comando da utilizzare è il seguente :  **sc start SmeupProvider**
 * per lo spegnimento il comando da utilizzare è il seguente :  **sc stop SmeupProvider**

**NOTA** : Tutti i file che contengono **Smens** nel nome servono all'installazione di questo prodotto e non all'installazione di SmeupProvider.


## Passi per la prima esecuzione
1) Avviare il provider in modalità interattiva. **Deve apparire la scheda iniziale dell'utente di collegamento. Se non succede è errata la configurazione di sme.up per quell'utente.

2) Collegarsi via browser in locale (dall'interno del desktop remoto) all'indirizzo http(s)://localhost:<porta>/debug. La porta default è 9090. Usare https o http a seconda dei come è stato avviato. **Deve apparire una pagina che dice "Smeup provider debug".** Se non succede la porta non è aperta o il programma non è partito. Consultare i log.

3) Collegarsi via bowser remoto.
 3.1) **Deve apparire una pagina che dice "Smeup provider debug".** Se non succede la porta non è aperta o la configurazione di rete non è corretta.
 3.2) Controllare che le informazioni del server e le informazioni di sessione siano corrette. Verificare ad esempio che iSeries, utente e ambiente applicativo siano quelle usate nella connessione.

Superati questi passi Sme.UP Provider è correttamente installato. Spegnerlo, schedulare l'avvio o avviarlo come servizio, scollegarsi dal server e riprovare gli stessi passi.

## Configurazione SW
La configurazione va differenziata tra provider e client.

### Script di configurazione del Provider

La configurazione di Sme.UP Provider avviene attraverso il membro di SCP_CLO dell'utente dedicato, copiato dall'esempio  :  : DEC T(MB) P(SCP_CLO) K(SMEUPPR_ES)

E' possibile impostare le seguenti variabili. Le variabili sono opzionali e dipendono dall'utilizzo : 

**PROVIDER_PATHS**  Questa variabile indica i percorsi in cui il Provider può leggere e scrivere. Ad esempio [*TMP];[*APPDATA]\Loocup;\\SERVER01\azienda01\clienti;. Porre attenzione all'utilizzo di variabili perchè queste vengono risolte nell'ambiente del provider e non in quello dell'utente. Si consiglia pertanto di esplicitare i percorsi quando ambienti diversi richiedono percorsi diversi.

**PROVIDER_UPDATE_FOLDER** Cartella dove vanno installate le varie versioni di Loocup. Ogni installazione deve avere il nome della cartella uguale a quello indicato nel file version.info.

**PROVIDER_CUSTOMER_FOLDER** Questa variabile specifica la cartella dove posizionare le immagini del customer :  l'app prima di effettuare l'autenticazione al provider, richiede un'immagine. Il provider, la cerca pirma in questa carella e in alternativa in nella cartella definita dalla variabile IMG.STD

**PROVIDER_AUTHORIZATION**  Se viene impostato il valore **NOAUTH**, l'autenticazione viene disabilitata e vengono accettate tutte le richieste. NOTA :  da usare solamente quando il provider non è pubblico.

**PROVIDER_DENIED_USER_LIST** - si usa per impedire il login a uno o più utenti.
Per motivi di sicurezza, ai seguenti utenti il login dal provider è sempre impedito indipendentemente dal valore della variabile : 
"QDIRSRV", "QIBMHELP", "QLWISVR", "QMSF", "QNTP", "QPGMR", "QPM400", "QSECADM", "QSECOFR",
"QSPLJOB", "QSRV", "QSYS", "QSYSOPER", "QSYSOPR", "QTCP", "QTMHHTTP", "QUSER", "QYPSJSVR"

**PROVIDER_CHECKSUM_ENABLED** valori Yes/No, default No. Abilita il controllo dei parametri inviati aggiungendo il checksum. Il checksum impedisce che una richiesta venga alterata (esempio modificare la fun con lo stesso codice di connessione)

**PROVIDER_MAX_DELAY**  valori numerici o OFF. Default OFF. Si usa per attivare un controllo temporale sulla richiesta. Tutte le richieste che giungono al provider con un ritardo superiore a quanto indicato nel parametro vengono scartate. Questo impedisce il riutilizzo di una fun fuori dai limiti temporali specificati.

**PROVIDER_HASH_KEY**  Chiave usata dal server per calcolare il checksum dei parametri. E' un valore alfanumerico libero, di almento 32 caratteri.

**PROVIDER_CERT_NAME** Il nome del certificato (se https - vedere paragrafo "Gestione Certificati"). Il certificato providertest distribuito da Sme.UP è SOLO AI FINI DI TEST

**PROVIDER_KEYSTORE_PWD** la password del keystore  (se https - vedere paragrafo "Gestione Certificati"). Il certificato providertest distribuito da Sme.UP è SOLO AI FINI DI TEST

**PROVIDER_KEYMANAGER_PWD**  la password del key manager  (se https - vedere paragrafo "Gestione Certificati"). Il certificato providertest distribuito da Sme.UP è SOLO AI FINI DI TEST

***SFunction** -  E' la funzione di avvio dell'utente server. Si consiglia di valorizzarla con  F(EXD;*SCO;) 2(MB;SCP_SCH;LO_SRV_BC) P(LOMODE(LOSER))


### La gestione dei certificati

Con il provider viene distribuito il certificato providertest.
Si trova nella cartella di installazione di Looc.UP sottocartella LOOCUP_SET\SPR\SSL

Questo certificato NON è valido :  se ad esempio si prova ad accedere con un browser sarà necessario acquisirlo manualmente.
E' possibile farsi rilasciare un certificato valido, da apposite società (ad es. www.trustitalia.it).

Affinchè il certificato rilasciato (o autoprodotto) possa essere utilizzato dal provider è necessario registrarlo nel Keystore della macchina su cui gira il provider.

Per registrare il certificato visionare la documentazione al link seguente : 
NOTA :  Se JAVA non risulta presente, non è necessario installarla :  i comandi per gestire i certificati sono nella cartella di installazione di **Loocup\jre\bin**
 :  : DEC T(J1) P(URL) [https://knowledge.verisign.com/support/code-signing-support/index?page=content&id=AR185&actp=LIST+
](https://knowledge.verisign.com/support/code-signing-support/index?page=content&id=AR185&actp=LIST+
)
&viewlocale=en_US) D(Documentazione di versign) I(Documentazione di versign) L(1)

Il nuovo certificato andrà posizionato sempre nella cartella  LOOCUP_SET\SPR\SSL.
Specificare nelle variabili

### La configurazione del provider come fornitore di file (oggetti J8 e J9)
Se il provider funge anche da fornitore di file ( documenti, pdf, immagini ecc), e' necessario configurare la variabile **PROVIDER_PATHS**.
Questa variabile indica i percorsi in cui il Provider può andare a leggere e scrivere.
Va posta molta attenzione alle variabili che definiscono i percorsi dei file. Le variabili usate dal server devono fare riferimento a percorsi locali o di rete.
NB :  va evitato l'utilizzo di variabili per la definizione dei vari percorsi, ma devono essere utilizzati percorsi assoluti.

### Configurazione dei client Looc.UP per l'utilizzo dei file remoti
Modificare gli SCP_CLO per i client Looc.UP valorizzando le variabili
 * **J8_SERVER** con **smeup;<protocollo><indirizzo provider> : porta;** dove protocollo vale http o https.
 * **J8_ACCEPT_SELFSIGNED**  utilizzando il protocollo HTTPS sarà necessario utilizzare un certificato. Per poter utilizzare, **SOLO AI FINI DI TEST**, quello distribuito con l'installazione di Looc.UP è necessario abilitare l'utilizzo di certificati non validi tramite questa variabile con valore "1".

NOTA :  **J8_PROTOCOL**  è obsoleta :  il protocollo dalla versione ROMA in poi. va specificato nella variabile J8_SERVER. definisce il protocollo da utilizzare per dialogare con il server. valori ammessi HTTP/HTTPS. Default è HTTPS. Definire questa variabile solo quando si utilizza l'HTTP.

## Smeup provider come aggiornatore dei Loocup client
Sme.UP Provider assolve anche il compito di server di gestione degli aggiornamenti tramite Sme.UP Updater.
Questo è composto da un client (vedi
- [Sme.UP GO e Updater lato client](Sorgenti/MB/DOC/LOSMEG)
) e da un server.

La funzionalità di server è assolta da Smeup Provider.

## Funzionamento
Il client  dialog con lo smeup provider e viene informato sulla presenza di un aggiornamento o di un cambio di release.
Se presente un aggiornamento o un cabmio di release il provider lo fornisce al client e questolo installa.

Il client può anche richiedere una versione diversa, in questo caso viene fornita l'intera installazione.

Quando un client richiede una versione completa, Smeup Provider, andrà a creare nella cartella PROVIDER_UPDATE_FOLDER, tre file : 
 * Versione_data.zip :  l'achivio con l'installazione completa
 * Versione_data.zip.created :  un file che informa il provider che l'archivio è stato creato
 * Versione_data.zip.md5 :  il file che contiene il checksum dell'archivio

Quando un client richiede una versione completa  aggiornamento, Smeup Provider, andrà a creare nella cartella PROVIDER_UPDATE_FOLDER, tre file : 
 * Versione_data_ora.zip :  l'achivio con l'upgrade
 * Versione_data_ora.zip.created :  un file che informa il provider che l'archivio è stato creato
 * Versione_data_ora.zip.md5 :  il file che contiene il checksum dell'archivio

NOTA :  la creazione dell'archivio avviene
 * se non esiste
 * se la data del file update.info è più recente di quella dell'archivio
Se si desidera pertanto forzare la ri-creazione dell'archivio è necessario cancellare manualmente tutti e tre i file che hanno la stessa radice.

### Prerequisiti Provider
 * Smeup Provider versione pari o successiva alla V4R1M150315, con relativo upgrade.
 * Spazio disco sufficiente per l'installazione di Loocup e per la creazione del relativo archivio.


### Configurazione e gestione delle versioni
Le varie versioni di Loocup client da tenere aggiornate vanno posizionate nella cartella identificata dalla variabile PROVIDER_UPDATE_FOLDER.
Ogni versione va installata in una cartella il cui nome coincide con il codice della versione stessa.
Ipotizzando che PROVIDER_UPDATE_FOLDER valga d : \update_folder e che si voglia mantenere aggiornate le versioni Le vele e la Tower Bridge, si  dovrà installare rispettivamente in d : \update_folder\V4R1M150515 e in d : \update_folder\V4R1M140701.

Quando si deve installare una versione di loocup va compiuta un'installazione completa (versione base + aggiornamento) nella cartella relativa. Ogni nuovo aggiornamento andrà fatto operando su questa cartella.

Quando si desidera forzare un cambio di versione, creare nella cartella  PROVIDER_UPDATE_FOLDER il file di testo force_version.info e andare a scrivere nella prima riga il codice di versione che deve essere utilizzata dai client, es. **V4R1M150315**.
La presenza di questo file forzerà tutti i client a passare alla nuova versione. E' stata comunque prevista la possibilità di avere client che non cambino versione. Per i dettagli consultare la documentazione
- [Sme.UP GO e Updater lato client](Sorgenti/MB/DOC/LOSMEG)

### Verifica della configurazione
Nella scheda di controllo del provider, raggiungibile dalla scheda del modulo LORRES è stato aggiunto il gruppo   Provider Updater e la voce "Le versioni" lista il contenuto della cartella.
Qui si trovano delle cartelle, una per ogni versione.
Se sono presenti i file descritti nel capitolo Funzionamento, significa che almeno un client si è connesso.
Se sono presenti le cartelle ma mancano i file, verificare il valore della variabile PROVIDER_UPDATE_FOLDER per l'utente con cui il provider sta funzionando.
Verificare successivamente le installazioni/configurazione dei client.


### Il file update.info
Con l'installazione di Loocup viene distribuito il file update.info.
Dalla release V4R1M150315, questo file, contiene, oltre alle informazioni sulla data di rilascio, anche delle istruzioni, utilizzate sia dal provider che dall'updater lato client.

Questo file può essere utilizzato per automatizzare la distribuzione di file o l'esecuzione di operazioni particolari sul client.

Il provider lo utilizza per sapere cosa fornire al client e il client compie le operazioni indicate.

Vediamo la struttura e la sintassi.
La prima riga contiene la data di rilascio/upgrade, nella forma AAAAMMGG_HHMMSS.
La seconda riga contiene la natura :  può essere RELEASE o UPDATE.
Le righe successive hanno significato solo se nella seconda c'è scritto UPDATE. queste righe avranno la forma
comando nome file.

Comando può essere
 * C :  Copia un file o una cartella (sovrascrive senza chiedere conferma)
 * D :  Delete, elimina un file o una cartella (senza chiedere conferma)
 * E :  Esegue il programma aspettando che termini
 * X :  Esegue il programma senza aspettare che termini.

mentre nome file è un nome / path relativo all'installazione di loocup, ad esempio

C Loocup.jar, significa copia loocup.jar dall'archivio alla cartella di installazione.
mentre
C LOOCUP_SCP\mybat.bat
significa copia mybat.bat dall'archivio nella cartella di installazione LOOCUP_SCP

Possiamo ad esempio distribuire dei bat e farli eseguire. sarà sufficiente andarli a copiare nella cartella di origine, ad esempio in PROVIDER_UPDATE_FOLDER\versione\LOOCUP_SCP\, e poi aggiungere al file update.info
C LOOCUP_SCP\mybat.bat
X LOOCUP_SCP\mybat.bat.

Per far recepire questa modifica a tutti i client, dovrò anche modificare la prima riga, inserendo una data successiva a quella indicata.


##  Funzioni di Debug e Controllo
Con Sme.UP V4R1 Dev 1/07/2014, utilizzando Looc.UP è possibile controllare lo stato e la configurazione di **Sme.UP Provider** attraverso la scheda del modulo LORRES
 :  : DEC T(TA) P(B£AMO) K(LORRES)
**Attenzione!** La scheda usa le variabili definite nel paragrafo **Configurazione dei client Looc.UP per l'utilizzo dei file remoti

 * In Looc.UP premere CTRL-F9 oppure Start->Funzioni di controllo->Scheda di debug
 * Scegliere il tab "**Sme.UP Provider**"

La scheda consente di
 *  verificare se loocup client è connesso al provider
 * interrogare il provider su
 ** lo stato (es. dati di connessione)
 ** le variabili
 ** le sessioni attive, comprese quelle remote
 ** accedere ai file di log
 ** eseguire interrogazioni di basso livello (viene mostrato l'XML) saltando meccanismi di sicurezza.
NOTA Queste interrogazioni sono cablate e a solo scopo di test.


Di seguito si può vedere un esempio di un client che dialoga con il provider in modo corretto
![LOCBAS_047](http://localhost:3000/immagini/LOCBAS_SPI/LOCBAS_047.png)
Nell'immagine seguente possiamo vedere la risposta del provider
![LOCBAS_048](http://localhost:3000/immagini/LOCBAS_SPI/LOCBAS_048.png)

### Cosa fare se non si ha una DEV aggiornata?
Vanno aggiornati i seguenti script di scheda : 
 * LOCEXD_DBG
 * LO_SRV_BC
 * LO_SPR

Dalla V3R2 in poi e' necessario aggiornare anche il membro MB SCP_MNU LORRES.

Si ricorda inoltre di copiare il membro MB SCP_CLO SMEUPPR_ES come esempio di configurazione del Provider.

# Script di configurazione di esempio

 :  : I.INC.MBR Lib(SMEDEV) Fil(SCP_CLO) Mem(SMEUPPR_ES)

# Problemi comuni
In questa sezione analizzeremo malfunzionamenti e possibili soluzioni.

Il provider deve essere acceso e funzionante :  attenzione che la presenza dell'interfaccia grafica di Looc.UP compare solo se avviato o da SmeupGo oppure se nella schedulazione viene specificato di farlo funzionare solo se l'utente è connesso.

Se installato come servizio verificare che il servizio sia avviato.
Verificare in ogni caso  che siano presenti i processi
SmeBase
Smetray
Smeuiclt

Si consiglia di scaricare il tool di Microsoft Process Explorer, che facilita l'individuazione e la gestione dei processi in gioco.
E' possibile scaricarlo da
[https://technet.microsoft.com/en-us/sysinternals/bb896653](https://technet.microsoft.com/en-us/sysinternals/bb896653)
s Explorer) L(1)


## Non riesco a visualizzare il contenuto di una cartella remota
 * dal client provare a interrogare il provider con la scheda di debug
 * se nella scheda di debug manca la sottoscheda provider, aprire un browser e scrivere
http(s)://indirizzo_del_provider:porta_del_provider/debug

Se non si ha risposta
- verificare protocollo (http/https), l'indirizzo e la porta del provider.
- se questi dati sono corretti pingare la macchina con il provider
- se la macchina è raggiungibile, andare sulla macchina dove funziona il provider, aprire un browser e digitare
http(s)://localhost:porta_del_provider/debug

se non si ha risposta verificare i parametri di avvio del provider e i file di log.

Se il provider risponde a localhost, verificare che il firewall non blocchi la porta su cui comunica il provider (se non specificato nei parametri di avvio è la 9090)

Se il provider è raggiungibile dal client, verificare che nel SCP_CLO del provider : 
 * sia definita la variabile J8_SERVER con valore blank :  J8_SERVER=""
 * sia definita la variabile PROVIDER_PATHS
 ** i percorsi in essa definiti siano raggiungibili dal provider
 * il provider raggiunga l'AS400 a cui il client vuole collegarsi
 * Looc.UP client utilizzi un nome di AS400 che il provider sia in grado di risolvere :  ad esempio utilizzare un alias nella tabella host locale.

## Non riesco a collegarmi con l'app
Verificare che protocollo, indirizzo e porta del provider.
Se sono corretti, provare ad aprire un browser e digitare
http(s)://indirizzo_del_provider:porta_del_provider/debug
se non si ha risposta verificare la raggiungibilità dell'indirizzo.
Se l'autenticazione fallisce verificare che il provider riesca a raggiungere l'AS400 a cui l'app vuole collegarsi.

## Non riesco ad accedere all'IFS
Esistono 3 soluzioni : 
 * rendere l'accesso pubblico :  contattare un sistemista per i dettagli.
 * utilizzare un utente di dominio windows con la stessa password dell'omonimo utente AS400. NOTA se nel dominio windows le password sono case sensitive e su AS400 no, va impostata una password sull'utente Windows in minuscolo.
 * avviare un provider in una console e autenticarsi sull'ìIFS con il JA_00_05;NET.AUT. NOTA l'avvio come operazione pianificata è assimilabile al funzionamento come servizio.


## Non riesco ad accedere a cartelle di rete quando funziona come servizio
Sintomo :  dal desktop del server riesco ad accedere alle cartelle, ma quando installo come servizio no.
Soluzione :  avviare il provider con i cmd startserver e stopserver (modalità interattiva).
Questi file si trovano all'interno della cartella di installazione, sottocartella LOOCUP_SCP.
Si consiglia di spostare questi file in una cartella apposita, per evitare che aggiornamenti del provider li sovrascrivano

## Non riesco a montare dischi di rete con il JA_00_05;NET.AUT
Causa :  il provider è installato come servizio
Soluzione :  avviare il provider con i cmd startserver e stopserver (modalità interattiva) in **console**.
**Nota :  non è possibile mappare cartelle di rete neppure nel caso in cui il provider venga avviato dalle operazioni pianificate.

Questi file si trovano all'interno della cartella di installazione, sottocartella LOOCUP_SCP.
Si consiglia di spostare questi file in una cartella apposita, per evitare che aggiornamenti del provider li sovrascrivano.


## Non riesco ad eseguire esportazioni con Excel
Causa :  Si sta utilizzando Windows 2003
Soluzione :  Avviare SmeupProvider con i batch o cambiare sistema operativo

Causa Si sta utilizzando W2008 R2 e mancano le cartelle
- C : \Windows\System32\config\systemprofile\Desktop
- C : \Windows\sysWOW64\config\systemprofile\Desktop
Queste vanno create manualmente.
maggiori dettagli nella NTI 1160.

Se dopo aver creato queste cartelle l'esportazione risulta comunque non possibile, avviare loocup utilizzando i batch.

## Il servizio non si avvia

causa :  Si sta utilizzando Windows 2003
soluzione :  Avviare SmeupProvider con i batch o cambiare sistema operativo.

causa :  L'utente è disabilitato
soluzione :  abilitare l'utente

causa :  L'utente è local system (non riesce ad accedere a %appdata%)
soluzione :  utilizzare un utente di dominio

## Il provider non si riavvia
Il provider è fornito di due meccanismi di riavvio automatico, uno legato a
