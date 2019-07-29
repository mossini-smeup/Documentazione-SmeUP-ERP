## Contenuto

La seguente guida prevede le verifiche preliminari, i prerequisiti, e l'implementazione lato iSeries.

Per i prerequisiti degli altri  attori in gioco (KDC, PC ) consultare il documento : 
- [SSO - Prerequisiti](Sorgenti/MB/DOC/LOSSON_50A)


## Prerequisiti lato iSeries
Riportiamo per comodità i prerequisiti : 


- Versione di sistema operativo i5/os uguale o superiore a V5R2M0
- **Ultimo cumulativo PTF per la versione di i5/os installata.**
- I seguenti prodotti programma installati su iSeries : 
-- 5722SS1 Option 12 OS/400 - Host Servers
-- 5722SS1 Option 30 OS/400 - QShell Interpreter
-- 5722AC3 Crypto Access Provider 128-bit for AS/400
-- 5722CE3 Client Encryption 128-bit (optional for Client side encryption)
-- 5722DG1 IBM HTTP Server for iSeries (optional for additional scenarios)
-- 5722XE1 iSeries Access for Windows
- Autorizzazioni *SECOFR per l'utente che configura il servizio (deve avere solo i diritti di *IOSYSCFG e *ALLOBJ)
- Valore di sistema QRMTSIGN impostato a *VERIFY
- iSeries configurato per utilizzare gli stessi DNS Server utilizzati da AD (sconsigliato utilizzare la tabella host).
- Corretta impostazione dei valori di sistema QTIME e QTIMZON
- Configurazione del server NTP (servizio tcp/ip SNTP) in modo che l'adattamento ora sia automatico (meglio configurarlo con il server dns interno AD)
- Authentication Method di i5/OS Netserver impostato a Password/Network autenthication. Ogni utente iSeries deve avere la HOME definita, vedere anche i prerequisiti SmeUp.


**NOTA** :  nel manuale IBM "Redbook Windows-based Single Signon and the EIM .pdf" , si consiglia la consultazione dell'appendice D :  contiene utili tabelle in fase di preanalisi e di configurazione.


## Prerequisiti lato SmeUp : 

- Prima di creare la HOME per ogni utente  fare riferimento alla nota tecnica 000493 - Percorsi IFS e   Single Sign On.


## Come conoscere gli utenti del dominio Active Directory e dell'iSeries.

Al fine di effettuare i legami utenti iSeries-utenti dominio Active Directory, è necessario conoscere gli utenti del dominio Active Directory e dell'iSeries.

Per conoscere gli utenti di del dominio Active Directory, è necessario collegarsi al Domain Controller, con un desktop remoto di console, avviare la console, poi selezionare Utenti e computer di Active Directory , selezionare il dominio e poi xxxx_Users, dove xxxx è il nome del dominio.
Questo elenco si può anche esportare in un file di testo.

Per conoscere gli utenti dell'iSeries WRKUSRPRF USRPRF(*ALL), se si ha SmeUp up fun, OJ, *USRPRF


## PARTE iSeries : 

Nelle pagine seguenti sono illustrati nell'ordine : 

 * I comandi da richiamare per verificare i prerequisiti
 * La configurazione della tabella host
 * La configurazione del realm
 * La procedura per configurare l'EIM
 * I riferimenti ai manuali IBM

### Controllo prerequisiti

Visualizzazione dei programmi installati (go licpgm opzione 10) : 

![LOBASE_122](http://localhost:3000/immagini/LOSSON_50B/LOBASE_122.png)
Visualizzazione dei programmi installati - continua

![LOBASE_123](http://localhost:3000/immagini/LOSSON_50B/LOBASE_123.png)
Verifica del valore di sistema QRMTSIGN  :  Wrksysval QRMTSIGN

![LOBASE_124](http://localhost:3000/immagini/LOSSON_50B/LOBASE_124.png)
Verifica del valore di sistema QTIMZON :  Wrksysval QTIMZON

![LOBASE_125](http://localhost:3000/immagini/LOSSON_50B/LOBASE_125.png)
Verifica del valore di sistema QTIME :   Wrksysval QTIME

![LOBASE_126](http://localhost:3000/immagini/LOSSON_50B/LOBASE_126.png)
Verifica tabella host :  Cfgtcp opzione 10.

![LOBASE_127](http://localhost:3000/immagini/LOSSON_50B/LOBASE_127.png)
Cfgtcp opzione 12 : 

![LOBASE_128](http://localhost:3000/immagini/LOSSON_50B/LOBASE_128.png)
## Implementazione

### operazioni preliminari
Collegarsi in Operation Navigator con uno user con diritti ***SECOFR** (o con un utente con i diritti sopra elencati)

![LOBASE_129](http://localhost:3000/immagini/LOSSON_50B/LOBASE_129.png)
Controllare ed eventualmente completare la tabella host iSeries
![LOBASE_130](http://localhost:3000/immagini/LOSSON_50B/LOBASE_130.png)
Immettere una password per il Tivoli : 

![LOBASE_131](http://localhost:3000/immagini/LOSSON_50B/LOBASE_131.png)
### Configurazione Dominio accesso REALM e  i5/OS NetServer

**NOTA** :  Nonostante si utilizzi un utente con dirittti *SECOFR, è capitato che l'Operation Navigator non consenta l'accesso al EIM. Provare allora a disintallare e reinstallare l'Operation Navigator.
![LOBASE_132](http://localhost:3000/immagini/LOSSON_50B/LOBASE_132.png)
![LOBASE_133](http://localhost:3000/immagini/LOSSON_50B/LOBASE_133.png)![LOBASE_134](http://localhost:3000/immagini/LOSSON_50B/LOBASE_134.png)![LOBASE_135](http://localhost:3000/immagini/LOSSON_50B/LOBASE_135.png)
![LOBASE_136](http://localhost:3000/immagini/LOSSON_50B/LOBASE_136.png)![LOBASE_137](http://localhost:3000/immagini/LOSSON_50B/LOBASE_137.png)
![LOBASE_156](http://localhost:3000/immagini/LOSSON_50B/LOBASE_156.png)
 * inserire la password che si vuole utilizzare e confermarla
 * cliccare su next

![LOBASE_157](http://localhost:3000/immagini/LOSSON_50B/LOBASE_157.png)
* E' possibile accettare il percorso predefinito o eventualmente selezionarne uno alternativo premendo Browse
* Cliccare su next

![LOBASE_158](http://localhost:3000/immagini/LOSSON_50B/LOBASE_158.png)
 * Verificare che tutte le informazioni siano coerenti con quanto inserito
 * Cliccare su finish

Collegarsi  al Domani controller Microsoft
 * Copiare il file .bat creato sopra sul server microsoft
 * Lanciare il file appena  copiato
 * Verranno creati tutti gli utenti necessari per far si da fare accesso all'IFS utilizzando il SSO

Come da figura qui sotto riportata

![LOBASE_159](http://localhost:3000/immagini/LOSSON_50B/LOBASE_159.png)
Passare a iNavigator

![LOBASE_160](http://localhost:3000/immagini/LOSSON_50B/LOBASE_160.png)
Sempre da iNavigator : 
 * Selezionare Network Servers  Tcp/ip
 * Cliccare con il tasto DX su i5/OS NetServer
 * Selezionare proprietà

![LOBASE_161](http://localhost:3000/immagini/LOSSON_50B/LOBASE_161.png)
 * Selezionare la scheda security
 * Verificare che l'authentication method sia impostato a Passwords/Network authentication

A questo punto IFS è funzionante anche dopo il cambio di password da windows.

### Creazione utenti del DC
 Per automatizzare la creazione degli utenti di dominio necessari al dialogo iSeries - DC, utilizzare la seguante procedura : 
![LOBASE_138](http://localhost:3000/immagini/LOSSON_50B/LOBASE_138.png) * E' possibile accettare il percorso predefinito o eventualmente selezionarne uno alternativo premendo Browse
 * Cliccare su next

![LOBASE_139](http://localhost:3000/immagini/LOSSON_50B/LOBASE_139.png) * Verificare che tutte le informazioni siano coerenti con quanto inserito
 * Cliccare su finish

Collegarsi  al Domani controller Microsoft
 * Copiare il file .bat creato sopra sul server microsoft
 * Lanciare il file appena  copiato
 * Verranno creati tutti gli utenti necessari per far si da fare accesso all'IFS utilizzando il SSO

Come da figura qui sotto riportata

![LOBASE_140](http://localhost:3000/immagini/LOSSON_50B/LOBASE_140.png)
### Configurare enterprise identity mapping

![LOBASE_141](http://localhost:3000/immagini/LOSSON_50B/LOBASE_141.png)![LOBASE_142](http://localhost:3000/immagini/LOSSON_50B/LOBASE_142.png)![LOBASE_143](http://localhost:3000/immagini/LOSSON_50B/LOBASE_143.png)![LOBASE_144](http://localhost:3000/immagini/LOSSON_50B/LOBASE_144.png)
**NOTA** : Nella definizione del NAS va impostato sì, in modifica va selezionato il valore NO


![LOBASE_145](http://localhost:3000/immagini/LOSSON_50B/LOBASE_145.png)![LOBASE_146](http://localhost:3000/immagini/LOSSON_50B/LOBASE_146.png)![LOBASE_147](http://localhost:3000/immagini/LOSSON_50B/LOBASE_147.png)
Immettere la password di autenticazione

![LOBASE_148](http://localhost:3000/immagini/LOSSON_50B/LOBASE_148.png)![LOBASE_149](http://localhost:3000/immagini/LOSSON_50B/LOBASE_149.png)
Creare gli identificativi necessari sul nuovo dominio EIM ed associare i registri di dominio/user  per l'autenticazione su iSeries

![LOBASE_150](http://localhost:3000/immagini/LOSSON_50B/LOBASE_150.png)![LOBASE_151](http://localhost:3000/immagini/LOSSON_50B/LOBASE_151.png)![LOBASE_152](http://localhost:3000/immagini/LOSSON_50B/LOBASE_152.png)

### IMPOSTAZIONE TCP SU NAS

Va fatto sulla NAS (network autentication security)
Quindi Operation navigator, Sicurezza, servizio di autenticazione di rete, proprietà : 
Spuntare **utilizza TCP**
![LOBASE_162](http://localhost:3000/immagini/LOSSON_50B/LOBASE_162.png)


## configurazione emulazione e test
Configurare la sessione di emulazione video per autenticarsi come Kerberos nelle proprietà del collegamento

![LOBASE_153](http://localhost:3000/immagini/LOSSON_50B/LOBASE_153.png)
Questa opzione non è valida per i citrix

Testate l'accesso in emulazione

![LOBASE_154](http://localhost:3000/immagini/LOSSON_50B/LOBASE_154.png)![LOBASE_155](http://localhost:3000/immagini/LOSSON_50B/LOBASE_155.png)
## I MANUALI IBM
Maggiori dettagli riguardo la configurazione dell'EIM si trovano nel documento
"Redbook Windows-based Single Signon and the EIM .pdf", disponibile al seguente link : 
[http://www.redbooks.ibm.com/redbooks/pdfs/sg246975.pdf](http://www.redbooks.ibm.com/redbooks/pdfs/sg246975.pdf)
Molto interessante l'appendice D :  contiene due tabelle utili in pre-analisi e configurazione.


## LA GESTIONE DELLE PASSWORD SU iSeries
Una volta che l'accesso in SSO è attivo è funzionante, l'eventuale scadenza della password su iSeries è ininfluente.
Non è ininfluente se verrà eseguito il login con utente e password. In questo caso sarà necessario inserire una nuova password.
Il cambio di password non influirà sull'autenticazione in SSO.

## COSA SUCCEDE SE UN'UTENTE E' DISABILITATO
Se un utente è disabilitato nessun tipo di accesso è consentito.


## CONFIGURAZIONE DEL SSO A LIVELLO DI OPERATION NAVIGATOR

E' possibile specificare che per un iSeries l'accesso avviene in SSO per tutti i servizi.
Attivando questa modalità di connessione si ottiene che, ad esempio, quando si richiama da Loocup la visualizzazione degli spool di stampa,  non è più necessario inserire la password.

Per attivare l'accesso in SSO per tutti i servizio, aprire l'Operation Navigator, collegarsi all'iSeries e, cliccare con il tasto destro sull'icona dell'iSeries e poi selezionare Proprietà.
Nella finestra che si apre, selezionare il pannello Connessione, poi tra le opzioni di connessione scegliere Utilizza nome principal kerberos, senza richiesta.

Dopo questa operazione verificare che le informazioni di accesso ID utente del Client Access (Comunicazioni, configura, Proprietà) sia il valore Utilizza il valore predefinito System i Navigator

## RIMOZIONE CONFIGURAZIONE

NOTA :  Questa procedura rimuove le configurazioni comuni. Se dopo averla eseguita non fosse possibile riconfigurare l'EIM è necessario contattare l'assistenza IBM, solo loro sono grado di ripristinare la configurazione.

Per la rimozione della configurazione compiere i seguenti passi : 

### Step 1 :  Remove EIM.
Do the following : 
 - Delete the Identifiers : 
 --  In IBM iSeries Navigator, select your system and log in.
 -- Expand Network.
 --  Expand Enterprise Identity Mapping.
 --  Expand Domain Management.
 --  Select your domain and authenticate the LDAP administrator.
 --  Expand your domain.
 --  Select Identifiers.
 --  In the right window pane, right-click on each identifier and select **Delete....**
 - Delete the User Registries : 
 --  Select User Registries under your domain.
 --  In the right window pane, right-click on each registry and select **Delete....**
 - Delete the Domain : 
 -- Select Domain Management.
 -- In the right window pane, right-click on your domain and select **Delete....**
 -- Click Yes on the warning message.

### Step 2 :  Remove NAS.
Do the following : 
 - In iSeries Navigator, under your system, expand Security.
 - Expand Network Authentication Service.
 - Select Realms.
 - In the right window pane, right-click on the realm and select Delete.
 - Click OK on the Confirm Realm Deletion window.

### Step 3 :  Remove Kerberos.
Do the following : 
 - Access PASE : 
 -- Sign on your System i.
 -- Type the command **call qp2term**.
 -- Type the command **export PATH=$PATH : /usr/krb5/sbin**.

 - Delete the Kerberos server : 
 -- Type the command **unconfig.krb5**.
 -- Type **Y** for the warning message.
 -- Note the successful message.
 -- Press **F3** to exit.
 -- Leave the session active.

### Step 4 :  Delete the NAS Keytab file.
Do the following : 
**Note : ** Deleting the NAS configuration does not delete the keytab file. A new configuration will append to the same file. This can sometimes cause errors.
 - In the emulation session, type the command **qsh**.
 - Type the command **keytab list**.
 - You should see all the principal names scroll by. Roll back up to the top and note the Key table path.
 - Return to iSeries Navigator and the Integrated File System.
 - Expand each directory in the path **/QIBM/UserData/OS400/NetworkAuthentication/keytab.**
 - Right-click on krb5.keytab and select Delete....
 - Click Yes on the message.

Clients that were connecting through Kerberos authentication might need to
clear any cached information to connect to this new configuration.
References : 
None.

