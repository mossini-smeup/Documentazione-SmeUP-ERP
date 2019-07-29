 :  : HEA PRIV(001)

## Troubleshooting
In questo documento raccogliamo i case history, i percorsi seguiti nelle installazioni difficili e le soluzioni

## Installazione in SSO in Bompani

Riassumo sinteticamente tutte le fasi/problematiche incontrate.
Se avete da aggiungere, aggiungete pure.
 - Prima verifica (circa 2 settimane fà) :   Necessario completare la configurazione in quanto mancavano dei passaggi necessari a livello Iseries di configurazione EIM che non erano presenti
 - Necessaria modifica delle chiavi di registro che non erano state modificate
 - Completata la configurazione verificato che Real indicava la risoluzione del nome sistema con 2 nomi diversi (as400fox e asintegra)
 - Analizzato il problema abbiamo trovato che sul DSN di Dominio (SRCMODC1) vi erano 2 nomi corrispondenti allo stesso IP (Dell'as400)
 - Fatto presente al cliente che ne aveva però necessità in quanto doveva utilizzare un'applicazione integra che vuole per forza quel nome Iseries
 - Spiegato che potevamo fare un alias di nome DSN e che la cosa funzionava lo stesso (CONFIGURATO E FUNZIONA)
 - Su Win7 non funzionava, abbiamo richiesto ed avuto a disposizione un WIN XP
 - Testato con XP e funzionava
 - Richieste da chiamata IBM delle PTF di Iseries, le ho scaricate da sito IBM ed installate su sistema BOMPANI
 - Riavviato il sistema dal cliente con le PTF SSO su XP funzionava così come le applicazioni del cliente
 - Durante la settimana successiva per probabili modifiche sulle info di dominio dell'Iseries e successivo riavvio dello stesso da parte del cliente ha smesso di funzionare la parte di ACG WEB EDITION come applicazione di WEbsphere dell'Iseries
 - Al mio rientro ho individuato il problema (sempre nelle info di dominio) e fatto ripartire il portale delle ACG WEB EDITION per la loro parte amministrativa
 - Nella data di ieri individuato, visto che non funzionava + nemmeno nella parte di XP, la mancanza (pre probabili test) della parte di REAL e di Dominio EIM.
 - Appena riconfigurata ha subito ricominciato a funzionare SSO (parte emulazione 5250) solo per win XP
 - Ho effettuato la verifica con file bat krp per Loocup e la vereifica non  passa (il log indica che il KDC non supporta encryption 14)
 - Sui forum abbiamo individuato che un utente aveva risolto la cosa passando la forest di dominio a livello W2008 (avendo dei W2003 e dei W2008 e il livello foresta a W2003)
 - Abbiamo verificato con il cliente ed a breve (forse a brevissimo add. lunedì) dovrebbe migrare l'intera foresta a W2008 e potremo ritestare il krb e verificare se la cosa puòà darci una mano anche su WIN7 (questo perchè non siamo sicuri che la cosa risolva visto che in Query con la foresta a W2003 la cosa funzioni lo stesso con Win7 senza la foresta a livello W2008).

###  Presenza nel dominio Windows viene introdotto anche un solo Domain Controller Windows 2008 R2
  Se nel dominio Windows viene introdotto anche un solo Domain Controller Windows 2008 R2, occorre togliere dagli attributi del primo "utente Kerberos creato dal batch EIM" il flag "Use Kerberos DES encryption types for this account" (o il corrispondente in italiano). Vedi figura sotto : 

![LOBASE_181](http://localhost:3000/immagini/LOSSON_50I/LOBASE_181.png)
  Se viene utilizzato Loocup, è necessario su ogni client installare la patch che trovate in allegato per il supporto Java alla criptatura AES256. Basta copiare i file nella cartella %Program Files%\Java\Jre\Lib\Security e riavviare.

### Operation Navigator che non consente di modificare l'EIM
Durante l'installazione in Bompani, è emerso un errore utilizzando l'operation navigator :  dopo ulteriore tentativi di configurazione l'Operation Navigator non ha più permesso di configurare l'EIM, nonostante sia stato cambiando sistema operativo (7 e XP), utilizzato un'altro utente (di classe SECOFR) e  cancellati tutti i file EIM.

Un analogo problema si verificava in Smea. E' stato risolto disinstallando e reinstallando l'Operation Navigator.

## Eliminazione configurazione KERBEROS
### Step 1 :  Remove EIM. Do the following : 
1. Delete the Identifiers : 
a In IBM iSeries Navigator, select your system and log in.
b Expand Network.
c Expand Enterprise Identity Mapping.
d Expand Domain Management.
e Select your domain and authenticate the LDAP administrator.
f Expand your domain.
g Select Identifiers.
h In the right window pane, right-click on each identifier and
select Delete....
2. Delete the User Registries : 
a Select User Registries under your domain.
b In the right window pane, right-click on each registry and select
Delete....
3. Delete the Domain : 
a Select Domain Management.
b In the right window pane, right-click on your domain and select
Delete....
c Click Yes on the warning message.

### Step 2 :  Remove NAS. Do the following : 
1. In iSeries Navigator, under your system, expand Security.
2. Expand Network Authentication Service.
3. Select Realms.
4. In the right window pane, right-click on the realm and select Delete.
5. Click OK on the Confirm Realm Deletion window.

### Step 3 :  Remove Kerberos. Do the following : 
1. Access PASE : 
a Sign on your System i.
b Type the command call qp2term.
c Type the command export PATH=$PATH : /usr/krb5/sbin.
2. Delete the Kerberos server : 
a Type the command unconfig.krb5.
b Type Y for the warning message.
c Note the successful message.
d Press F3 to exit.
e Leave the session active.

### Step 4 :  Delete the NAS Keytab file. Do the following : 
Note :  Deleting the NAS configuration does not delete the keytab file. A new configuration will append to the same file. This can sometimes cause errors.
1. In the emulation session, type the command qsh.
2. Type the command keytab list.
3. You should see all the principal names scroll by. Roll back up to
the top and note the Key table path.
4. Return to iSeries Navigator and the Integrated File System.
5. Expand each directory in the path
/QIBM/UserData/OS400/NetworkAuthentication/keytab.
6. Right-click on krb5.keytab and select Delete....
7. Click Yes on the message.
Clients that were connecting through Kerberos authentication might need to clear any cached information to connect to this new configuration.
References : None.


## Problema :  Accesso possibile solo elevando i permessi di esecuzione - soluzione IBM

Programs Run From Command Prompt
=================================
Programs run from a command prompt where UAC prompts for permission to elevate the authority of the user will run in a new temporary command prompt window. When the program completes, this temporary command prompt disappears and you will not be able to view any output from the program. To work around this problem, open a command prompt that already has elevated  authority.
Start --> All Programs --> Accessories --> right-click Command
Prompt --> Run as administrator

Run the program from the elevated Command Prompt.

Install considerations : 
Once the PTF is applied to the IBM i system, you can install the service pack from the network share named ROOT on your IBM i.
Accessing this share uses the LAN Manager component of Windows and NetServer support on the IBM i.
Much like Vista, Windows 7 has a default negotiation method for such connections that may  ail when accessing the IBM i. One way to resolve this problem is to change a policy setting on the PC.
Changing the policy setting requires administrator authority and can be performed as follows : 
 -  Bring up the control panel
 - Select "System and Security" --> "Administrative Tools"
 - Double click "Local Security Policy" in right pane.
 - From the "Local Security Policy" window expand "Local Policies"
 - Select Security Options
 - In the right pane, scroll down to the setting called  "Network security :  LAN Manager authentication level" and double-click it.
 - Change it to?"Send LM & NTLM - use NTLMv2 session security if negotiated"
 -  Select OK, and exit.
 You should now be able to access the network share.

On Windows 7, when installing or updating IBM i Access for Windows from a network share, you must first map a network drive from a Command Prompt that has elevated authority (ie was created with "Run as administrator"). For example : 

Start --> All Programs --> Accessories --> right-click Command
Prompt --> Run as administrator

net use x :  \\IBM_server\ROOT (where x is the name of the drive you want to map and IBM_server is the name of your IBM isystem)

Then to run the IBM i Access for Windows installer, using that same Command Prompt do : 

x : 
cd \QIBM\ProdData\Access\Windows
cwblaunch.exe

The installation or update will proceed normally.

As an alternative to installing from a network drive which requires elevated administrative authority, you can copy all the files required for the installation to the local hard drive and run the installation locally.
tratto da
 :  : DEC T(J1) P(URL) [http://www-912.ibm.com/n_dir/NAS4APAR.NSF/c897711a8f5f5aab862564c00079d112/4c7d4d170d3efac4862576+
](http://www-912.ibm.com/n_dir/NAS4APAR.NSF/c897711a8f5f5aab862564c00079d112/4c7d4d170d3efac4862576+
)
48003c70e7?OpenDocument) L( ) R( )

## Problema :  Accesso possibile solo elevando i permessi di esecuzione - soluzione Microsoft

Un utente autenticato su un pc con XP, riesce a collegarsi in SSO, mentre non riesce se si autentica su una macchina con W7.
Riesce ad collegarsi in SSO solo se esegue il programma con i privilegi di amministratore o se nel collegamento viene specificato "esegui in modalità Windows XP"

Per la risoluzione fare riferimento al link seguente : 
 :  : DEC T(J1) P(PATHDIR) K(HTTP : //ANSWERS.MICROSOFT.COM/EN-US/WINDOWS/FORUM/WINDOWS_7-SECURITY/KRBEXCEPTION-INTEGRITY-CHECK-ON-DECRYPTED-FIELD/E43F10EB-BBC8-44C3-B3D6-BD60EF3B0C9B) I(documentazione forum windows) L( ) R( )

## Mailing list su Kerberos
 :  : DEC T(J1) P(PATHDIR) K(HTTP : //MAILMAN.MIT.EDU/PIPERMAIL/KERBEROS/) D(Archivio mailing list) L( ) R( )


## Workaround for Windows 7 restarts related to "lsass.exe, failed with status code 255." message!
Since I upgraded my computers to Windows 7 I got sometime a message that a "A critical system process" failed and the machine will restart within 1 minute. I experienced the problem both on my desktop and laptop computer. After a while I discovered that locking then immediately unlocking the computer reproduces the crash about 70-80% of the time. Searching the net I found that several peoples had the same problem but no one got a real solution yet that worked for me.
 :  : DEC T(J1) P(URL) [http://social.technet.microsoft.com/Forums/en/w7itprogeneral/thread/c71c56cf-f07c-458b-bcbf-76383+
](http://social.technet.microsoft.com/Forums/en/w7itprogeneral/thread/c71c56cf-f07c-458b-bcbf-76383+
)
bc4e64b)
 :  : DEC T(J1) P(URL) [http://social.technet.microsoft.com/Forums/en-US/w7itprogeneral/thread/f5f44b82-b0cc-4813-8199-62+
](http://social.technet.microsoft.com/Forums/en-US/w7itprogeneral/thread/f5f44b82-b0cc-4813-8199-62+
)
964f386500)

After suffering from this problem too much time I've decided to find the real cause of this problem. All the other workarounds suggested on forums discussing this issue are not working or just partial solutions. As far as I can understand the core of the issue is some re-authentication with the domain controller that occurs when the computer is unlocked. At this point some modules that are called by lsass.exe are failing and make the service crash and you know what happens.

Analyzing the crash dumps using windows debugger I've found out that the failure related to kerberos.dll. So then I started to search settings related to Kerberos authentications and found 2 possible entries that can affect the Kerberos authentication process : 

1. Registry entry HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\DefaultEncryptionType
2. Policy setting located at "Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options\Network security :  Configure encryption types allowed for Kerberos", which after all sets the following registry key : 
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\SupportedEncryptionTypes

Searching the net about this parameter reveals more information and details explanations.

What solved the problem for me is setting the following registry key and values to make Windows 7 behave like Windows Server2003 regarding to Kerberos Encryption Type (KERB_ETYPE_RC4_HMAC_NT)

Key :    HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters
Type :    REG_DWORD
Name :    DefaultEncryptionType
Data :     23 (decimal) or 0×17 (hexadecimal)

Now it's also possible to disable the problematic encryption type with a GPO applied the Windows 7 machines or to find a way (which I didn't search for yet) to change the DefaultEncryptionType using GPO.

Hope this will help other peoples and will I update if there will be real solution or I find a better workaround.


## Estensione della cifratura
In alcuni casi le librerie standard della JVM non supportano il livello di sicurezza richiesto dal protocollo KERBEROS.
Si può provare a scaricare una versione di queste librerie e sostiuire quelle standard.
Effettuare su google, la ricerca di JCE policy, oppure di
Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6
nel caso la JVM installata sia una versione 6.x
oppure di
Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7
nel caso la JVM installata sia una versione 7.x

Le librerie da sostituire si trovano nella cartella di installazione della JVM, sottocartella \lib\security.

Se si desidera mantenere il backup di quelle originarie, modificare l'estensione, ad esempio da  **.jar** in **.jar_ori**.



## Authentication - significato dei parametri della chiave Parameters

Tratto da
[http://flylib.com/books/en/1.271.1.69/1/](http://flylib.com/books/en/1.271.1.69/1/)

The following sections contain customizations that help you troubleshoot and optimize authentication. The section "Configuring Kerberos" describes how to configure Kerberos for troubleshooting. The section "Disabling Global Catalog Requirement" describes how to remove the requirement of having a Global Catalog server at remote sites. Finally, the section "Enabling Verbose Winlogon Messages" describes how you can get more information from Winlogon for troubleshooting.
Configuring Kerberos

Kerberos is an authentication mechanism that is used to verify user or host identity. Kerberos is the preferred authentication method for services in Windows Server 2003. If you are running Windows Server 2003, you can modify Kerberos parameters to help troubleshoot Kerberos authentication issues or to test the Kerberos protocol. After you finish troubleshooting or testing the Kerberos protocol, remove any registry entries that you added. Otherwise, your computer's performance might be affected.

Table 6-1 describes the values you can configure in the key HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters and that are REG_DWORD values.
Table 6-1 Control\ Lsa\Kerberos\Parameters


|  Nam="6-1 Control\ Lsa\Kerberos\Parameters" |
| 
| .COL  Txt="Name" LunAut="1" A="L" |
| ---|----|
| 
| .COL  Txt="Value" LunAut="1" A="L" |
| 
| .COL  Txt="Description" LunAut="1" A="L" |
| SkewTime | 5 (minutes) | This value is the maximum time difference that is permitted between the client computer and the server that accepts Kerberos authentication. In Windows Server 2003 checked build version, the default SkewTime value is two hours. A checked build version-also known as a debug version-of the Windows operating system is used in production and testing environments. This kind of build helps trace the cause of problems in system software by turning on many debugging checks in the operating system code and in the system drivers. These debugging checks help the checked build identify internal inconsistencies as soon as they occur. A checked build has many compiler optimizations turned off and is larger and runs more slowly than an end-user version of Windows does. An end-user version of Windows is also known as a free build version or a retail-build version. In a free build version, debugging information is removed, and Windows is built with full compiler optimizations. A free build version is also faster and uses less memory than a checked build version does. |
| LogLevel | 0 | This value indicates whether events are logged in the system event log. If this value is set to any non-zero value, all Kerberos-related events are logged in the system event log. |
| MaxPacketSize| 1465 (bytes) | This value is the maximum User Datagram Protocol (UDP) packet size. If the packet size exceeds this value, TCP is used. |
| StartupTime|120 (seconds) | This value is the time that Windows waits for the Key Distribution Center (KDC) to start before Windows gives up. |
| KdcWaitTime| 10 (seconds)|This value is the time Windows waits for a response from a KDC. |
| KdcBackoffTime|10 (seconds)|This value is the time between successive calls to the KDC if the previous call failed. |
| KdcSendRetries|3|This value is the number of times that a client will try to contact a KDC. |
| DefaultEncryptionType|23 (decimal) or 0x17 (hexadecimal)|This value indicates the default encryption type for pre-authentication. |
| FarKdcTimeout|10 (minutes)|This is the time-out value that is used to invalidate a domain controller from a different site in the domain controller cache. |
| NearKdcTimeout|30 (minutes)|This is the time-out value that is used to invalidate a domain controller in the same site in the domain controller cache. |
| StronglyEncrypt-Datagram|FALSE|This value contains a flag that indicates whether to use 128-bit encryption, as opposed to weaker encryption, for datagram packets. |
| MaxReferralCount|6|This value is the number of KDC referrals that a client pursues before the client gives up. |
| KerbDebugLevel|1 (for Windows Server 2003 checked build version), 0 (for Windows Server free build version)|This value indicates whether debug logging is on (1) or off (0). |
| MaxTokenSize|12000 (Decimal)|This value is the maximum value of the Kerberos token. Microsoft recommends that you set this value to less than 65535. |
| SpnCacheTimeout|15 (minutes)|This value is the lifetime of the Service Principal Names (SPN) cache entries. On domain controllers, the SPN cache is disabled. |
| S4UCacheTimeout|15 (minutes)|This value is the lifetime of the S4U negative cache entries that are used to restrict the number of S4U proxy requests from a particular computer. |
| S4UTicketLifetime|15 (minutes)|This value is the lifetime of tickets that are obtained by S4U proxy requests. |
| RetryPdc|0 (false) Possible values :  0 (false) or any non-zero value (true)|This value indicates whether the client will contact the primary domain controller for Authentication Service Requests (AS_REQ) if the client receives a password expiration error. |
| RequestOptions|Any RFC 1510 value|This value indicates whether there are additional options that must be sent as KDC options in Ticket Granting Service requests (TGS_REQ). |
| ClientIpAddress|0 Possible values :  0 (false) or any non-zero value (true). (This setting is 0 because of Dynamic Host Configuration Protocol and network address translation issues.)|This value indicates whether a client IP address will be added in AS_REQ to force the Caddr field to contain IP addresses in all tickets. |
| TgtRenewalTime|600 (seconds)|This value is the time that Kerberos waits before it tries to renew a Ticket Granting Ticket (TGT) before the ticket expires. |
| AllowTgtSessionKey|0 Possible values :  0 (false) or any non-zero value (true)|This value indicates whether session keys are exported with initial or with cross realm TGT authentication. The default value is false for security reasons. |
| 


Table 6-2 describes the values that you can configure in the key HKLM\SYSTEM\CurrentControlSet\Services\Kdc. (Create the subkey Kdc if it doesn't exist.)
Table 6-2 Services\ Kdc


|  Nam="6-2 Services\ Kdc" |
| 
| .COL  Txt="Name" LunAut="1" A="L" |
| ---|----|
| 
| .COL  Txt="Value" LunAut="1" A="L" |
| 
| .COL  Txt="Description" LunAut="1" A="L" |
| KdcUseClientAddresses|0 Possible values :  0 (false) or any non-zero value (true)|This value indicates whether IP addresses will be added in the Ticket Granting Service Reply (TGS_REP). |
| KdcDontCheckAddresses|0 Possible values :  0 (false) or any non-zero value (true)|This value indicates whether IP addresses for the TGS_REQ and the TGT Caddr field will be checked. |
| NewConnectionTimeout|50 (seconds)|This value is the time that an initial TCP endpoint connection will be kept open to receive data before it disconnects. |
| MaxDatagramReplySize|1465 (decimal, bytes)|This value is the maximum UDP packet size in TGS_REP and Authentication Service Reply (AS_REP) messages. If the packet size exceeds this value, the KDC returns a KRB_ERR_RESPONSE_TOO_BIG message that requests that the client switch to TCP. |
| KdcExtraLogLevel|2|Possible values :  1 (decimal) or 0x1 (hexadecimal) :  Audit SPN unknown errors. 2 (decimal) or 0x2 (hexadecimal) :  Log PKINIT errors. (PKINIT is an Internet Engineering Task Force [IETF] Internet draft for "Public Key Cryptography for Initial Authentication in Kerberos.") 4 (decimal) or 0x4 (hexadecimal) :  Log all KDC errors. This value indicates what information the KDC will write to event logs and to audits. |
| KdcDebugLevel|1 (for checked build), 0 (for free build)|This value indicates whether debug logging is on (1) or off (0). If the value is set to 0x10000000 (hexadecimal) or 268435456 (decimal), specific file or line information will be returned in the data field of KERB_ERRORS as PKERB_EXT_ERROR errors during a KDC processing failure. |
| 


Disabling Global Catalog Requirement

Placement of Global Catalog servers in remote sites is usually desired to improve performance of user logon time, searches, and other actions requiring communication with Global Catalog servers, and to reduce wide area network (WAN) traffic. However, to reduce administrative intervention, hardware requirements, and other related overhead, you might not always want to locate a Global Catalog server at a remote site. This is especially relevant in environments that have a large number of sites that could experience substantially increased hardware costs when the size of the sites might not justify that hardware and administration. The problem is that logons require the domain controller authenticating the user to contact a Global Catalog server to determine whether the user is a member of any universal groups. If the remote office does not have a Global Catalog server and a Global Catalog server cannot be contacted (for various reasons), then the user's logon request might fail (based on the rules stated earlier).

Windows Server 2003 offers an alternative to universal group caching. When this is enabled for a site, users who log on while a Global Catalog server is online can continue to do so if the Global Catalog server is inaccessible at the next logon.

To eliminate the need for a Global Catalog server at a site and to avoid potential denial of user logon requests, enable logons when a Global Catalog server is not available. You must configure this setting on the domain controller that performs the user authentication. To do that, add the REG_DWORD value IgnoreGCFailures to HKLM\SYSTEM\CurrentControlSet\Control\Lsa. Set this value to 0x01. After changing this value, you must restart the domain controller.
CAUTION
The universal groups setting causes potential security vulnerabilities. Universal groups should not be used because if a user is a member of a universal group and the group is denied access to a resource, the key turns off enumeration of universal groups. The result is that the universal group SID is not added to the user's token, and the user could have access to the resource.
Enabling Verbose Winlogon Messages

You can configure Windows so that you receive verbose startup, shutdown, logon, and logoff status messages. Verbose status messages might be helpful when you are troubleshooting slow startup, shutdown, logon, or logoff behavior. To enable verbose status messages, create the REG_DWORD value verbosestatus in the key HLKM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System. Set this value to 0x01. Note that Windows doesn't display status messages if the value DisableStatusMessages exists in the key HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System.







