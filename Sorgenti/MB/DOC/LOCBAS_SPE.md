# Scritp di esempio come fornitore di risorse remote
Di seguito viene riportato uno script con le impostazioni per l'utilizzo del provider come fornitore di risorse remote.

sostituire xxC. con  :  : C.

xxC.SEZ Cod="Variable"
Funzione di avvio del provider :  è la scheda di controllo
xxC.VAR Cod="*SFunction" Value="F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCH;LO_SRV_BC) P(LOMODE(LOSER))"


Indirizzo di loocup service provider :  va specificato il valore "" per evitare che il provider chieda sè stesso i file.
xxC.VAR Cod="J8_SERVER" Txt="Service Provider" Value=""

Path accessibili da remoto :  qui vanno raccolti tutti i path a cui gli utenti dovranno accedere, indipendentemente dall'azienda del singolo utente.
xxC.VAR Cod="PROVIDER_PATHS" Txt="Path accettati dal server remoto" Value="\\srv001.smeup.com\Comuni Gruppo\;\\srv001.smeup.com\azienda1\;\\srv001.smeup.com\azienda2\;\\srv001.smeup.com\azienda3\;[*APPDATA];[*TMP];\\srv002\QUECOM\Commerciale\Clienti;[IMG.STD]"
Questa configurazione consente agli utenti l'accesso alle seguenti cartelle : 
 * \\srv001.smeup.com\Comuni Gruppo\
* \\srv001.smeup.com\azienda1\
 * \\srv001.smeup.com\azienda2\
 * \\srv001.smeup.com\azienda3\
 * [*APPDATA]
 * [*TMP]
 * \\srv002\QUECOM\Commerciale\Clienti
 * [IMG.STD]

Gli utenti poi, accederanno solamente a determinate cartelle in funzione delle variabili definite nel loro SCP_CLO.

xxC.VAR Cod="PROVIDER_MAX_DELAY" Txt="ritardo in ms sulla richiesta" TVal="NR" Value="120000"

xxC.VAR Cod="PROVIDER_CHECKSUM_ENABLED" Txt="abilitazione controllo checksum" Value="NO"
xxC.VAR Cod="PROVIDER_HASH_KEY" Txt="chiave di has" Value="dftypG1Hm3H8xs9CwGeIs3lO5Agi7xc2P3u4"

----------------------------------------------------------------------------------------
da eliminare
----------------------------------------------------------------------------------------
# Installazione e configurazione di Sme.UP Provider

Con l'**upgrade del 25/11/2014** sono state introdotte importanti novità : 
 * Si è passati all'utilizzo di Java Versione 1.7
 * si può gestire la comunicazione in HTTPS
 * è stata incrementata la sicurezza. E' possibile attivare : 
 ** il controllo temporale sulla richiesta :  solo a richieste ricevute entro un arco temporale viene data risposta
 ** un meccanismo per impedire l'alterazione della richiesta

Sia l'HTTPS che gli altri due meccanismi di controllo sono configurabili tramite gli script SCP_CLO.

## Prerequisiti
 * Indirizzo IP statico
 * Firewall
 * Server Windows adeguatamente dimensionato in funzione del carico.
 * Adeguata infrastruttura di rete per poter rendere accessibile su internet/intranet la porta HTTP/HTTPS
 * Un utente di dominio Windows dedicato
 * Un utente AS400 dedicato

## Possibili installazioni
Smeup provider può essere installato sia con interfaccia grafica, utile nel caso in cui svolga funzioni anche di server batch (es. per l'esecuzione di flussi), in questo caso le schede consentono di monitorare queste attività. Può essere anche installato come un servizio di Windows.


## Installazione con interfaccia grafica
 * scaricare dal sito la versione di Loocup **Sme.Up Provider**
 * installare con amministratore della macchina o in generale porre attenzione ai requisiti
 * copiare i file LOOCUP_SCP\startserver.cmd e LOOCUP_SCP\stopserver.cmd in una cartella a scelta
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
 * **--server : CODA : PORTA_SERVER**   :  Definisce la coda di comunicazione con l'as400 e la porta di comunicazione dei client loocup
 * **--http(s):PORTA_HTTP(S)** : Definisce l'attivazione della modalità http(s) (obbligatoria) e la porta di accesso all'http(s) (opzionale, se non specificata assume 9090)


Altri parametri sono
 * **--loglevel : xxxxx** :  dove xxxxx può valere
 ** **DEBUG** :  massimo dettaglio nei log, utile in una fase iniziale o a fronte di segnalazioni di errori
 ** **INFO** :  modalità di funzionamento normale.
 ** **WARN** :  vengono loggate solo le condizioni di avviso
 ** **ERR** :  vengono loggate solo le condizioni di errore
 ** **OFF** :  nessun log. Impostazione sconsigliata :  vengono mantenuti solo i file di log degli ultimi 8 giorni. Tutti quelli più vecchi vengono automaticamente eliminati all'avvio del provider.

NOTA :  Loocup è composto da tre moduli e i log del modulo emulatore e di quello grafico (scheda) non sono influenzati dal parametro loglevel :  questi due componenti mantengono sempre la stessa modalità di loggatura.

## Installazione come servizio
 * scaricare dal sito la versione di Loocup **Sme.Up Provider**
 * installare con amministratore della macchina o in generale porre attenzione ai requisiti
 * scaricare serverplugin dai plugin
 * scompattare il contenuto dell'archivio dentro la cartella di installazione di Loocup, facendo sovrascrivere i file presenti. Al termine dell'operazione, verificare che nella cartella di installazione di loocup siano presenti i file
 ** warapper.exe
 ** ServiceInstall.bat
 ** ServiceUninstall.bat
 ** ServiceStart.bat
 ** ServiceStop.bat
 ** ServiceRestart.bat
 * la cartella serviceNT

Per configurare il provider, andare nella cartella serviceNT, conf e aprire il file wrapper.conf con un editor di testo e modificare le parti tra parentesi quadre.

dopo la riga **wrapper.app.parameter.7=--service** aggiungere **wrapper.app.parameter.8=--http(s)(:porta)**

dopo aver modificato questo file, installare il provider come servizio facendo doppio click su ServiceInstall.bat.

Aprire il gestore dei servizio (Pannello di controllo, Strumenti di amministrazione, servizi) e verificare che SmeupProvider sia presente.

Per l'avvio e lo spegnimento del provider, aggiungere due voci nelle operazioni pianificate : 
 * per l'avvio il comando da utilizzare è il seguente :  **sc start SmeupProvider**
 * per lo spegnimento il comando da utilizzare è il seguente :  **sc stop SmeupProvider**

**NOTA** : Tutti i file che contengono **Smens** nel nome servono all'installazione di questo prodotto e non all'installazione di SmeupProvider.


## Passi per la prima esecuzione
1) Avviare smeup provider. **Deve apparire partire con la scheda iniziale dell'utente di collegamento. Se non succede è errata la configurazione di sme.up per quell'utente.

2) Collegarsi via browser in locale (dall'interno del desktop remoto) all'indirizzo http(s)://localhost:<porta>/debug. La porta default è 9090. Usare https o http a seconda dei come è stato avviato. **Deve apparire una pagina che dice "Smeup provider debug".** Se non succede la porta non è aperta o il programma non è partito. Consultare i log.

3) Collegarsi via bowser remoto. **Deve apparire una pagina che dice "Smeup provider debug".** Se non succede la porta non è aperta o la configurazione di rete non è corretta.

4) Collegarsi via bowser remoto. Controllare che le informazioni del server e le informazioni di sessione siano corrette. Queste dipendono dalla configurazione di Sme.UP.


Superati questi passi Sme.UP Provider è correttamente installato. Spegnerlo, schedulare l'avvio, scollagarsi e, una volta avviatosi riprovare gli stessi passi.

## Configurazione SW
La configurazione va differenziata tra provider e client.

### La configurazione del Provider
Modifiche a SCP_CLO per **Sme.UP Provider**  : 
Si consiglia di creare un utente AS400 che verrà utilizzato come **utente master** per **Sme.UP Provider
In questo caso, si consiglia di copiare il membro SMEDEV\SCP_CLO\SMEUPPR_ES nella propria PER, **dandogli il nome dell'utente master**.
Personalizzare il membro come descritto nel membro stesso.
Se non si dispone di una DEV aggiornata, creare il membro con il nome dell'utente master e definire le variabili

**J8_SECRET** - OBSOLETA Definisce la chiave di dialogo tra Loocup client e provider - E' UNA SEQUENZA CARATTERI CASUALI  (dovrà essere identica a quella create per gli SCP_CLO dei client!)

**J8_PATHS** - OBSOLETA Percorsi dove lo SmeUp Provider può accedere, separati da punto e virgola


Il provider non ha un database degli utenti a cui può fornire servizi, ma lo chiede all'AS400. Per evitare che utenti di sistema vengano disabilitati involontariamente o a causa di azioni malevoli il login viene impedito per gli utenti
"QDIRSRV", "QIBMHELP", "QLWISVR", "QMSF", "QNTP","QPGMR", "QPM400", "QSECADM", "QSECOFR",
"QSPLJOB", "QSRV", "QSYS", "QSYSOPER", "QSYSOPR", "QTCP", "QTMHHTTP", "QUSER", "QYPSJSVR"
eventuali altri utenti vanno specificati con la variabile seguente : 
**PROVIDER_DENIED_USER_LIST** - elenco utenti con login inibito, separati da punto e virgola.


**PROVIDER_MAX_DELAY**  valori numerici o OFF. Default OFF. Se viene specificato un valore numerico, viene aggiunto ai parametri il timestamp della richiesta. Questa deve giungere al server entro un'intervallo massimo specificato da questa variabile (in millisecondi).

**PROVIDER_CHECKSUM_ENABLED** valori Yes/No, default No. Abilita il controllo dei parametri inviati aggiungendo il checksum.

**PROVIDER_HASH_KEY**  Chiave usata dal server per calcolare il checksum dei parametri. E' necessaria solo se abilitato il checksum. NON DEVE ESSERE DEFINITA PER I CLIENT :  il provider la comunica dopo l'autenticazione.

**PROVIDER_AUTHORIZATION** (SVI AL 15/12/2014) Se viene impostato il valore **NOAUTH**, l'autenticazione viene disabilitata e vengono accettate tutte le richieste. NOTA :  da usare solamente quando il provider non è pubblico.

**La gestione dei certificati**

Con il provider viene distribuito il certificato  providertest.
Si trova nella cartella di installazione di loocup sottocartella LOOCUP_SET\SPR\SSL

Questo certificato NON è valido :  se ad esempio si prova ad accedere con un browser sarà necessario acquisirlo manualmente.
E' possibile farsi rilasciare un certificato valido, da apposite società (ad es. www.trustitalia.it).

Affinchè il certificato rilasciato (o autoprodotto) possa essere utilizzato dal provider è necessario reistrarlo nel Keystore della macchina su cui gira providertest.

Per registrare il certificato visionare la documentazione al link seguente : 
NOTA :  Se JAVA non risulta presente, non è necessario installarla :  i comandi per gestire i certificati sono nella cartella di installazione di **Loocup\jre\bin**
 :  : DEC T(J1) P(URL) [https://knowledge.verisign.com/support/code-signing-support/index?page=content&id=AR185&actp=LIST+
](https://knowledge.verisign.com/support/code-signing-support/index?page=content&id=AR185&actp=LIST+
)
&viewlocale=en_US) D(Documentazione di versign) I(Documentazione di versign) L(1)




Il nuovo certificato andrà posizionato sempre nella cartella  LOOCUP_SET\SPR\SSL.
Specificare nelle variabili
**PROVIDER_CERT_NAME** Il nome del certificato

**PROVIDER_KEYSTORE_PWD** la password del keystore

**PROVIDER_KEYMANAGER_PWD**  la password del key manager

***SFunction** -  E' la funzione di avvio dell'utente server. Si consiglia di valorizzarla con  F(EXD;*SCO;) 2(MB;SCP_SCH;LO_SRV_BC) P(LOMODE(LOSER))


### La configurazione del provider come fornitore di file
Se il provider funge anche da fornitore di file ( documenti, pdf, immagini ecc), e' necessario configurare la variabile PROVIDER_PATHS (ex J8_PATHS).
Questa variabile indica i percorsi in cui il Provider può andare a leggere e scrivere.
Va posta molta attenzione alle variabili che definiscono i percorsi dei file. Le variabili usate dal server devono fare riferimento a percorsi locali o di rete.
NB :  va evitato l'utilizzo di variabili per la definizione dei vari percorsi, ma devono essere utilizzati percorsi assoluti.


### Configurazione dei client Looc.UP
SCP_CLO per i client Looc.UP : 
 * Definire la variabile J8_SERVER con smeup;SERVER_WINDOWS : porta;
 * OBSOLETA Definire la variabile J8_SECRET formata da una sequenza di caratteri casuali
 * J8_PROTOCOL (OPZIONALE) definisce il protocollo da utilizzare per dialogare con il server. valori ammessi HTTP/HTTPS. Default è HTTPS. Definire questa variabile solo quando si utilizza l'HTTP.

Utilizzando il protocollo HTTPS sarà necessario utilizzare un certificato. Per poter utilizzare quello distribuito con l'installazione di Loocup è necessario abilitare l'utilizzo di certificati non validi tramite la variabile J8_SELFSIGNED con valore "1".

### Configurazione dell'APP
L'app deve conoscere quale è il provider a cui collegarsi e le credenziali dell'AS400.
Per specificare il provider bisogna andare in **impostazioni**, selezionare la SmeApp e inserire l'indirizzo del provider specificando, protocollo,  eventualmente la porta e abilitare l'utilizo con l'apposito selettore.
Qaundo si apre la SmeApp veranno richieste le credenziali di accesso all'AS400, in modo analogo a Loocup. Nel caso in cui si specifichi solamente l'utente e la password, la connessione avverrà all'AS400 a cui il provider è connesso e l'ambiente sarà quello utilizzato dal provider. In questo caso, se l'utente non avrà tra i propri ambienti quello del provider verrà restituito un'errore.
NOTA BENE :  l'autenticazione eseguita tramite la SmeApp segue le stesse regole di LoocUp o del Client Access :  se in Loocup l'uente si disabilita dopo aver fornito per tre volte di seguito credenziali errate, accade lo stesso con la SmeApp.
Se pertanto si disabilita l'utente accedendo con la SmeApp, l'utente non potrà collegarsi in nessun modo all'AS400.

Per sapere come realizzare schede utilizzabili dall'APP, consultare la documentazione del modulo MOBASE.

NOTA :  Se sul provider si abilita il controllo checksum non serve definire la variabile J8_HASH_KEY per l'utente :  questo parametro viene fornito dal provider alla SmeApp una volta che l'autenticazione è avvenuta.


### Configurare l'accesso alle risorse remote
Se il client dovrà usare dei file chiedendoli al Provider, tutti i percorsi dovranno far riferimento al protocollo smeup.
Sarò pertanto necessario anteporre la variabile J8_SERVER ai percorsi.
Andrà verificato che il Provider sia in grado di raggiungere i percorsi così specificati :  se ad esempio dal pc dell'utente si raggiunge la macchina WINDOW_SERVER_01, questa macchina dovrà essere raggiungibile anche dal Provider.
L'utilità di passare dal Provider sta nel rendere raggiungibili sempre e ovunque i documenti, indipendentemente da dove si trovi il client (intranet piuttosto che in internet).


## La configurazione dell'HW


### Dimensionamento Server Windows
Se le utenze sono poche (meno di 10) o si desidera effettuare qualche test, è sufficiente un PC recente con Windows XP.

In ambiente di produzione si consiglia di optare per macchine virtuali con installata una versione server di Windows (da 2003 in poi).

Abbiamo effettuato test di carico arrivando a 400 connessioni simultanee con una macchina così dimensionata : 

SO -  W2008 server R2 32bit
HW - Intel Xeon E5504 2GHZ 4 processori 3GB RAM

### Configurazione della rete
Sulla macchina in cui è installato il provider deve essere raggiungibile la porta HTTP/HTTPS
La porta è un parametro di avvio del Provider ( parametro --http:porta oppure --https:porta). Per i dettagli vedi il capitolo sull'installazione.

Si consiglia di utilizzare il protocollo HTTPS in quanto, a  differenza del protocollo HTTP, i dati vengono criptati.

Sono poi possibili 3 configurazioni a sicurezza crescente : 

 * Viene pubblicata una porta del server windows
 * Come sopra ma il server viene messo in DMZ
 * Si crea una macchina linux che fa da proxy verso il server windows. Il server Linux va messo in DMZ e fa da ponte tra la porta raggiungibile da internet e la porta su cui ascolta il provider.


##  Funzioni di Debug e Controllo
Con Sme.UP V4R1 Dev 1/07/2014, utilizzando Looc.UP è possibile controllare lo stato e la configurazione di **Sme.UP Provider**.
L'accesso è sempre dalla scheda di debug.
Per il client andare nella sottoscheda "Smeup Provider - risorse remote"
Per il provider selezionare la sottoscheda "Server", poi  "Smeup Provider".

 * In Looc.UP premere CTRL-F9 oppure Start->Funzioni di controllo->Scheda di debug
 * Scegliere il tab "**Sme.UP Provider**"

Nel cruscotto si vede lo stato delle variabili in gioco.
Se la comunicazione con il provider avviene in HTTPS, l'unica variabile che deve essere definita è la J8_SERVER.
Se la comunicazione avviene in HTTP , allor è necessario definire la cariabile J8_PROTOCOL = HTTP.
Le altre variabili, come pure il plugin SP vengono definite automaticamente.

Nella scheda, sotto il cruscotto, sono stati predisposti varie modalità di interrogazione del provider, dalla più complessa alla più semplice :  posso interrogare i log, accedendovi come risorse remote, oppure avere solo l'elenco dei file in formato XML o testare lo scaricamento.
Le funzioni di debug di basso livello saltano tutti i controlli su cifratura dei parametri o limiti temporali, ma offrono solo funzionalità cablate :  non è ad esempio possibile richiamare una funzione qualsiasi come se fosse una di test.

Di seguito si può vedere un'esempio di un client che dialoga con il provider in modo corretto
![LOCBAS_047](http://localhost:3000/immagini/LOCBAS_SPE/LOCBAS_047.png)
Nell'immagine seguente possiamo vedere la risposta del provider
![LOCBAS_048](http://localhost:3000/immagini/LOCBAS_SPE/LOCBAS_048.png)
### Cosa fare se non si ha una DEV aggiornata?
Vanno aggiornati i seguenti script di scheda : 
 * LOCEXD_DBG
 * LO_SRV_BC
 * LO_SPR

Dalla V3R2 in poi e' necessario aggiornare anche il membro MB SCP_MNU LORRES.

Si ricorda inoltre di copiare il membro MB SCP_CLO SMEUPPR_ES come esempio di configurazione del Provider.
