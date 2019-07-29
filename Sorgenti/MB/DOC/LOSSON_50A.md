 :  : HEA STAT(10) USAG(FORFED) DTAG(20141024) ORAG(155900) RELS(V4R1) APPL(LO) AMBT(TE)

## Scopo del documento
In questo documento sono elencate tutti i prerequisiti necessari affinchè si possa attivare l'autentizazione SSO con Kerberos tra CA e iSeries e tra LoocUp e iSeries.

Verranno inoltre descritte le verifiche preliminari di tutti gli attori in gioco :  KDC (normalmente l'AD), il iSeries,  i client, lo SmeUp e LoocUp.


## Prerequisiti lato Iseries

 * **DEVE ESSERE ATTIVO IL CONTRATTO DI MANUTENZIONE SW IBM**
 * Versione di sistema operativo i5/os uguale o superiore a V5R3M0
 * **Ultimo cumulativo PTF per la versione di i5/os installata.**
 * I seguenti prodotti programma installati su Iseries : 
 ** 5722SS1 Option 12 OS/400 - Host Servers
 ** 5722SS1 Option 30 OS/400 - QShell Interpreter
 ** 5722AC3 Crypto Access Provider 128-bit for AS/400
 ** 5722CE3 Client Encryption 128-bit (optional for Client side encryption)
 ** 5722DG1 IBM HTTP Server for iSeries (optional for additional scenarios)
 ** 5722XE1 iSeries Access for Windows
 * Autorizzazioni *SECOFR per l'utente che configura il servizio (deve avere solo i diritti di *IOSYSCFG e *ALLOBJ)
 * Valore di sistema QRMTSIGN impostato a *VERIFY- iSeries configurato per utilizzare gli stessi DNS Server utilizzati da AD (sconsigliato utilizzare la tabella host).
 * Corretta impostazione dei valori di sistema QTIME e QTIMZON
 * Configurazione del server NTP (servizio tcp/ip SNTP) in modo che l'adattamento ora sia automatico (meglio configurarlo con il server dns interno AD)
 * Authentication Method di i5/OS Netserver impostato a Password/Network autenthication. Ogni utente AS400 deve avere la HOME definita, vedere anche i prerequisiti SmeUp.

**NOTA** :  nel manuale IBM "Redbook Windows-based Single Signon and the EIM .pdf", si consiglia la consultazione dell'appendice D :  contiene utili tabelle in fase di preanalisi e di configurazione.

## Prerequisiti lato SmeUp

- Prima di creare la HOME per ogni utente  fare riferimento alla nota tecnica 000493 - Percorsi IFS e   Single Sign On.


## Prerequisiti lato Server Windows

 - SO Domain controller Windows Server 2003 o superiore con Microsoft Active directory
 - Il livello funzionale del domino e della foresta Active Directory minimo deve essere Windows Server 2003.
 - Support tools installati per abilitazione Ktpass (Su 2008 sono gia implementati ci servono solo su w2k3).
 - Aggiornamento struttura Active Directory (nel caso di windows 2003 deve essere struttura AD 2003).
 - Configurazione di reverse loocup DNS funzionante e testata (verificare il corretto funzionamento del DNS).
 - Presenza nel dominio AD degli account necessari alla comunicazione kerberos  tra iSeries e AD.

## Prerequisiti lato client Pc

 - Tutti i client devono essere correttamente uniti al dominio Active Directory in questione.
 - Tutti i client interessati alla funzionalità devono utilizzare Windows 2000 Professional o superiori. Non sono ammesse licenze Home o Home Premium in quanto non unibili all'Active Directory.
 - La tabella host del client NON deve contenere riferimenti alla risorsa cui si vuole accedere (Kerberos utilizza anche il DNS diretto e inverso per la verifica del ticket di autenticazione).
 - In caso di sistema Windows7 o XP il supporto a kerberos deve essere abilitato. Vanno modificate delle chiavi di registro (da distribuire via policy). Vedi documento LOBASE_50D (link riportato di seguito)
 - In caso di sistema operativo Windows7 e Active Directory 2008, vanno modificati i tipi di criptatura consentiti per kerberos. Far riferimento al documento : 
- [SSO - Configurazione dominio Windows](Sorgenti/MB/DOC/LOSSON_50D)

- In caso di sistema operativo Windows 8, 8.1 se l'utente è amministratore locale, loocup deve essere avviato innalzando i diritti ad amministratore. Questa operazione può essere compiuta ogni volta che si avvia Loocup (tasto dx "esegui come amministratore") oppure si può creare un link al GO in cui, nelle proprietà, nel pannello "Compatibilità", si spunta "Esegui questo programma come amministratore".

## Prerequisiti Loocup

 - Aver installato una versione V3R1 o successiva.
 - Deve essere installata una JVM 7.0 (1.7.0_67) a 32 bit.
 - Deve essere applicata la JCE (Java Criptographic Extension).

Se si utilizza la V4R1, la JVM è distribuita insieme a Loocup. La JCE va scaricata dal sito www.smeup.com, download, Loocup Download, JVM e tool consigliati per Looc.Up, Java Cryptography Extension, o utilizzando il link diretto : 
[http://erp.smeup.com/loocup_downloads/UnlimitedJCEPolicyJDK7.zip](http://erp.smeup.com/loocup_downloads/UnlimitedJCEPolicyJDK7.zip)
JCE per java 1.7.0) L(1)



## Prerequisiti Operation Navigator

 - Per l'accesso al iSeries tutti i client devono aver installato Client Access 5.3 o superiore nel caso di Windows 2000 o XP e Client Access 5.8 o superiori per Vista e Windows 7.  L'accesso all'iSeries in SSO tramite un'emulazione telnet 5250 è non è possibile tramite software di terze parti in quanto ad oggi non supportano il protocollo Kerberos.
 - Per la configurazione e l'amministrazione dell'EIM :  aver installato le opportune funzioni dell'Iseries Operation Navigator.

