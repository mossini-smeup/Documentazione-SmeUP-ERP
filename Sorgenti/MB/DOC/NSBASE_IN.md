# Installazione
Il software Smens e Smedg può essere installato direttamente su AS400 o sui vari PC che lo utilizzano

## Prerequisiti comuni a tutte le installazioni : 

- Assicurarsi di avere installato sull'AS/400 l'ambiente Java : 
-- Lanciare GO LICPGM selezionare l'opzione 10 e controllare di avere installato i programmi (XX varia a seconda del sistema) : 
--- 57XXJC1    *COMPATIBLE  AS/400 Toolbox for Java
--- 57XXJV1    *COMPATIBLE  AS/400 Developer Kit for Java
- Verificare la corretta esistenza dell'ambiente Java sull'AS400 aprendo una shell di comando con STRQSH e digitando il comando java -version , se il sistema è correttamente configurato il sistema dovrebbe rispondere con qualcosa di simile a  versione java "1.5.0" $  (ovviamente 1.5.0 cambierà se la JVM installata è diversa)

Per sistemi di OS in versione 7.1 o successivi, potrebbe cambiare l'organizzazione dei programmi su licenza.
Ciò singnifica che il pacchetto Toolbox for java (JC1) risulta "annegato" nel 5770-SS1 opz.3.
**Ricordiamo che la versione minima di Java Virtual Machine per far funzionare il modulo in questione è la 1.5.

## Installazione su AS400
L'installazione è gestita in modo automatico mediante mediante il comando UP UT3.
L'unico parametro richiesto in fase di installazione è la cartella in cui installare tale
prodotto.
Il software Smens e Smedg non può essere installato in una cartella qualunque dell'IFS.
Dato che l'esecuzione avviene da ben determinati percorsi, è necessario porre la dovuta attenzione
in fase di installazione.

La cartella da cui vengono eseguiti Smens e Smedg si basa sul contenuto del campo T$JA1I (Path
Specifico £G53) della tabella JA1.
Se tale campo è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/Smeup**
Se tale campo non è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/xxxxx/Smeup**
dove xxxxx è il contenuto del campo.
In questo modo è quindi possibile utilizzare diverse versioni di Smens e Smedg per diversi sistemi informativi.

La cartella in cui viene installato tale software deve seguire quindi la struttura indicata.
Ogni tentativo di installare il software (tramite UP UT3) in una cartella con una struttura
diversa causerà un messaggio di conferma per ricordare appunto le problematiche a cui si va
incontro.

Una volta effettuata l'installazione, qualora si desideri accedere alle cartelle sotto SmeExt dalle cartelle di rete di windows per consultare i log eventualmente attivabili (vedere oltre in merito a questo argomento), o per editare il file di configurazione, è consigliabile configurare il NetServer dell'iSeries per condivirere la cartella SmeExt.

## Installazione su macchina Windows : 
La versione per PC del server SmeNS può essere scaricata al seguente indirizzo.
[http://www.smeup.com/it/soluzioni/looc-up-download/utility-software](http://www.smeup.com/it/soluzioni/looc-up-download/utility-software)
D(Download Smens) O(KD)

- Installare lo **Smens** su tutti i Pc e i server con i quali si vuole comunicare. Non è necessario installarlo se si utilizzalo Smens solo sull'As400.
-- L'installazione può avvenire come applicazione utente (interattiva) o come servizio
--- In caso di installazione come servizio non saranno disponibili funzioni interattive di visualizzazione documenti/immagini, resteranno invece disponibili funzioni di esecuzione programmi o di movimentazione FTP.
- Oltre ad essere installato, deve essere in esecuzione sul Pc
-- In caso di installazione utente (interattiva) l'applicazione va avviata tramite lo script startmanager.bat contenuto nella cartella smens
-- In caso di installazione come servizio Windows l'applicazione è attiva quando il servizio è in stato Avviato.
--- Per le indicazioni su come installare l'applicazione come servizio si rimanda al successivo paragrafo


### Configurazione del servizio Windows : 

- Configurazione del servizio nel file _2_wrapper.conf contenuto nella sottocartella "./serviceNT/conf".
- Installare il servizio SmeNS  tramite _2_ServiceInstall.bat.
- Avviare il servizio tramite la gestione servizi di Windows
- Il corretto avvio del servizio potrà essere verificato verificando i file di log di smens ed in "./serviceNT/log".


### Aggiornamento/installazione del servizio Windows in 10 passi

- Scaricare lo zip da http://www.smeup.com/loocup_downloads/utility/smeup.zip
- **In caso di aggiornamento **  Spegnere il servizio smens attualmente attivo sul server tramite il pannello di controllo dei servizi windows
- **In caso di aggiornamento **  Prendere nota dell'utente con cui si avvia il servizio o definirlo in caso di nuova installazione
- **In caso di aggiornamento **  Deregistrare il servizio smens attuale tramite lo script ServiceUninstal.bat
- **In caso di aggiornamento **  Rinominare la cartella Smeup attualmente installata (ad es. come Smeup_old)
- Copiare la cartella Smeup contenuta nella cartella dove si è scompattato lo zip
- Riportare correttamente l'utente (e la relativa password) di cui si è preso nota al punto 3 (che dovrebbero anche essere presenti nel file wrapper.conf nella cartella servicent\conf della vecchia versione) nel file wrapper.conf della nuova versione.
- Registrare il servizio smens tramite lo script ServiceInstall.bat presente nella nuova cartella Smeup
- Controllare nel pannello dei servizi di windows che il servizio si sia installato con l'utente desiderato, eventualmente modificarlo tramite (sul servizio SmensService) Tasto destro --> Proprietà --> TAB Connessione
- Controllare che il servizio si sia avviato nel pannello dei servizi di windows o, eventualmente avviarlo verificando che si sia installato con avvio Automatico



# Configurazione
## Verifiche e configurazione per invio mail
Affinchè l'AS400 sia in grado di inviare mail tramite la G53 è necessario che siano soddisfatti alcuni prerequisiti dal punto di vista del networking e della configurazione dell'applicazione
### Prerequisiti Networking
L'AS400 per inviare le mail utilizzerà un SMTP server che deve essergli indicato nel file Configurazione.cfg presente nella cartella SmeExt/Smeup/Cfg (o SmeExt/xxxxx/Smeup/Cfg in base
all'installazione) relativo al percorso d'installazione alla voce MailServer.
L'AS400 deve essere in grado di raggiungere tale SMTP server sulla porta TCP del servizio SMTP (il default è la porta 25). La cosa può essere testata con il seguente questo comando
>TELNET RMTSYS('smtp.acme.com') PORT(25)
dove a smtp.acme.com va sostituito il nome del server SMTP che si vuole utilizzare e che verrà indicato nel suddetto file di configurazione.
Se l'AS400 riesce a raggiungere l'SMTP Server verrà aperta una finestra che dovrebbe indicare che il collegamento è stato stabilito con successo. se si vuole poi chiudere questa finestra va digitato >quit
Se l'AS400 non riesce a raggiungere l'SMTP Server verrà mostrata un messaggio del tipo >Nessuna risposta dal sistema host remoto ...
Se si utilizza un nome server e non un indirizzo IP, accertarsi che l'AS400 riesca a risolvere il nome. Se non è in grado di farlo è OBBLIGATORIO utilizzare direttamente l'indirizzo IP oppure risolvere la limitazione a livello di configurazione TCP dell'AS400
### Prerequisiti di configurazione
Una volta assolti i prerequisiti relativi al networking vanno affrontati quelli relativi alla configurazione. Per fare ciò bisogna avere alcune informazioni relative al tipo di servizio che il server SMTP mette a disposizione : 

- porta TCP del server SMTP (la porta standard è la 25)
- l'invio mail è sottoposto ad autenticazione?
- se la risposta è sì procurarsi un ID e password validi

Nel caso la porta TCP su cui opera il server SMTP non sia quella standard (la 25), va indicata alla voce MailServer (dove si indica anche l'indirizzo del server SMTP), come suffisso preceduto dal due punti ( : ). Ad esempio, se il server SMTP, ipoteticamente all'indirizzo 192.168.0.100 è configurato sulla porta 1880, andrà indicato nel modo seguente : 
MailServer= 192.168.0.100 : 1880

Nel caso l'invio sia sottoposto ad autenticazione bisogna indicare nel file di configurazione nella voce SMTPAuth=SI
Quindi bisogna indicare utente e password validi per permettere l'invio
SMTPAuthUser= ; Utente SMTP per l'invio se SMTPAuth è abilitato
SMTPAuthPassword= ; Password per utente SMTP per l'invio se SMTPAuth è abilitato

Nel caso l'invio NON sia sottoposto ad autenticazione bisogna indicare nel file di configurazione nella voce SMTPAuth=NO

### Test di invio mail da Sme.UP
L'invio della mail è effettuato tramite la /copy **£G53**.
Tale /copy viene gestita tramite il servizio B£SER_85 e la funzione di test è la seguente : 
 :  : DEC D(Richiamo interfaccia invio mail) I(Tester invio mail) X(F(INP;B£SER_85;MAILTE) SP(Mod(C) Nom(B£SER_85/A) Out(INP))) O(D)

### Test e debugging sessione SMTP
Per gli invii di test è possibile attivare l'emissione in console dei messaggi di debug della transazione STMP abilitando nel file di configurazione la voce SMTPDebug, quindi indicando
SMTPDebug= DEBUG;

Si precisa che questo flag abilita l'emissione in console dei log per qualunque invio mail attraverso la G53. Quindi utilizzarlo solo nelle fasi di testing e poi ricordarsi di disabilitarlo mettendo
SMTPDebug= NO;

### Simulazione manuale sessione SMTP
E' altresì possibile, qualora l'SMTP non sia sottoposto ad autenticazione sull'invio simulare manualmente l'invio di una mail : 

- Avviare telnet sul server SMTP con TELNET RMTSYS('smtp.acme.com') PORT(25)
- EHLO _7_dominio completo mittente <INVIO> ( oppure HELO _7_dominio completo mittente <INVIO> )
- mail from :  _7_NOME COMPLETO DEL MITTENTE CON IL DOMINIO <INVIO>
- rcpt to :  _7_NOME COMPLETO DEL DESTINATARIO CON IL DOMINIO <INVIO>
- data <INVIO>
- _7_TESTO DELL'EMAIL <INVIO>
- . <INVIO>
- quit per chiudere la sessione

Nota1 :  per <INVIO> si intende l'ENTER
Nota2 :  le diciture racchiuse fra parentesi quadre [] stanno ad indicare che tipo di dato inserire.
Nota3 :  la digitazione è "sempre attiva", quindi qualunque tasto premuto entra nella digitazione, vale a dire che eventuali digitazioni per cancellare, spostare il cursore, etc. entrano a far parte dei dai passati al server quasi sempre "sporcando" o invalidando i dati. Quindi se si sbaglia digitare in qualunque momento della simulazione probabilmente bisogna disconnettersi e ripetere completamente tutto.

### Invio di Posta Elettronica Standard
L'invio di mail passa attraverso la configurazione presente nel file Configurazione.cfg.
I parametri del file di configurazione coinvolti nelle impostazioni relative all'invio di mail sono i seguenti : 

- MailServer :  indicare l'indirizzo del server SMTP fornito dal provider dell'account di Posta Elettronica Certificata
- MailDomain= acme.com; Dominio della posta elettronica aziendale (talvotla richiesto dal serve di posta per permettere l'invio
- ESMTPSupport=SI ;
- SMTPAuth=SI ; Abilitazione dell'autenticazione per SMTP (se autenticazione non richiesta mettere NO)
- SMTPAuthUser= xxxxxxxx ; Utente di autenticazione fornito dal provider dell'account nel caso SMTPAuth sia SI
- SMTPAuthPassword=yyyyyyyy ; Password fornita dal provider dell'account nel caso SMTPAuth sia SI



### Invio di Posta Elettronica Certificata (PEC)
Avendo a disposizione un account di Posta Elettronica Certificata è possibile inviare mail certificate.
Si rimanda alla documentazione specifica disponibile in rete per la comprensione dei concetti relativi alla PEC.
L'invio di mail di tale tipo passa attraverso la configurazione presente nel file Configurazione.cfg. Se si desidera gestire l'invio di mail certificate come opzionale si rimanda ai concetti relativi al campo £G53CF della /copy presenti in questo stesso documento.
I parametri del file di configurazione coinvolti nelle impostazioni relative all'invio di PEC sono i seguenti : 

- MailServer :  indicare l'indirizzo del server SMTP fornito dal provider dell'account di Posta Elettronica Certificata
- MailDomain= acme.com; Dominio della posta elettronica aziendale (talvotla richiesto dal serve di posta per permettere l'invio
- ESMTPSupport=SI ;
- SMTPAuth=SI ; Abilitazione dell'autenticazione per SMTP
- SMTPAuthUser= xxxxxxxx ; Utente di autenticazione fornito dal provider dell'account di Posta Elettronica Certificata
- SMTPAuthPassword=yyyyyyyy ; Password fornita dal provider dell'account di Posta Elettronica Certificata
- SecureSMTP= SI; (NUOVO PARAMETRO)

**ATTENZIONE** :  il parametro SecureSMTP è nuovo, quindi non presente in file Configurazione.cfg precedenti al 4 dicembre 2010.

**ATTENZIONE** :  La funzione di invio di PEC è disponibile su AS400 su cui è installata una Java Virtual Machine 5.0 o successive

**ATTENZIONE** :  Nel caso in cui si riscontrino, problemi nell'invio di mail PEC a causa della non completa validità della catena di certificazione dei certificati SSL può risultare necessario aggiungere al file di configurazione con i dati il parametro :  **DisableSSLCert= SI;**

### Invio tramite SecureSMTP (es :  GMAIL)
Avendo a disposizione un account con invio tramite SecureSTMP (GMAIL ne è un esempio) è possibile inviare mail tramite tale tipo di connessione.
L'invio di mail tramite tale account passa attraverso la configurazione presente nel file Configurazione.cfg.
I parametri del file di configurazione coinvolti nelle impostazioni relative all'invio tramite SecureSMTP sono i seguenti : 


- MailDomain= acme.com; Dominio della posta elettronica aziendale (talvotla richiesto dal serve di posta per permettere l'invio
- ESMTPSupport=SI ;Utilizza le specifiche ESMTP :  "SI" o "NO" i valori possibili (il default e SI)
- SMTPAuth=SI ; Abilitazione dell'autenticazione per SMTP ( il default è NO)
- SMTPAuthUser= account@gmail.com ; Utente SMTP per l'invio se SMTPAuth è abilitato
- SMTPAuthPassword=passwordaccount; Password per utente SMTP per l'invio se SMTPAuth è abilitato
- SMTPDebug= NO; Attivo se DEBUG, disattivo altrimenti
- MailDomain=gmail.com ;
- SecureSMTP= SI

**ATTENZIONE** :  il parametro SecureSMTP è nuovo, quindi non presente in file Configurazione.cfg precedenti al 4 dicembre 2010.

**La funzione di invio di mail tramite SecureSMTP (necessario per l'invio tramite GMAIL) è disponibile su AS400 su cui è installata una Java Virtual Machine 5.0 o successive

### Invio tramite Office 365
Avendo a disposizione un account con invio tramite Office 365 è possibile inviare mail tramite tale tipo di connessione.
L'invio di mail tramite tale account passa attraverso la configurazione presente nel file Configurazione.cfg.
I parametri del file di configurazione coinvolti nelle impostazioni relative all'invio tramite Office 365 sono i seguenti : 


- MailServer= smtp.office365.com : 587;questo indirizzo NON funziona senza autenticazione.
- MailDomain= acme.com; Dominio della posta elettronica aziendale (talvotla richiesto dal serve di posta per permettere l'invio
- ESMTPSupport=SI ;Utilizza le specifiche ESMTP :  "SI" o "NO" i valori possibili (il default e SI)
- SMTPAuth=SI ; Abilitazione dell'autenticazione per SMTP ( il default è NO)
- SMTPAuthUser= account@acme.com ; Utente SMTP per l'invio se SMTPAuth è abilitato
- SMTPAuthPassword=passwordaccount; Password per utente SMTP per l'invio se SMTPAuth è abilitato
- SMTPDebug= NO; Attivo se DEBUG, disattivo altrimenti
- MailDomain=acme.com ;
- SecureSMTP= NO;
- TLS=SI;

**ATTENZIONE** :  il parametro SecureSMTP è nuovo, quindi non presente in file Configurazione.cfg precedenti al 4 dicembre 2010.

**La funzione di invio di mail tramite SecureSMTP (necessario per l'invio tramite GMAIL) è disponibile su AS400 su cui è installata una Java Virtual Machine 5.0 o successive

### Utilizzo in SSL di server non certificati
Nell'utilizzo dell'invio e-mail attraverso protocollo SMTPS (basato su SSL) può capitare che il server da utilizzare possieda un certificato non riconosciuto, scaduto o self-made.
In questo caso la Java Virtual Machine chiude la connessione in maniera autonoma e non sindacabile e nei log della G53 si ottiene una segnalazione di questo tipo :  "javax.mail.MessagingException :  Could not connect to SMTP host :  indirizzo-server-SMTPS :  465".
La procedura da mettere in atto, e che verrà di seguito indicata, è volta a far acquisire localmente alla Java Virtual Machine dell'AS400 il certificato specifico del server SMTPS in questione.
La questione è del tutto simile a quanto viene fatto su client di posta classici (Outlook, Thunderbird, etc.) quando si gestisce l'eccezione di certificato per poter utilizzare un server di posta.


- Ottenere il file del certificato dal server in formato di certificato (in seguito indicato con _7_file-cer) e prendere nota dell'alias di certificato (in seguito indicato con _7_alias-certificato), in esso contenuto, relativo al server di cui si vuole acquisire il certificato (chi vi fornisce il file .cer dovrebbe essere a conoscenza di quest'ultima informazione)
-- Per poterlo fare bisogna munirsi di Openssl ed installarlo su un PC.
-- Una volta fatto questo aprire una riga comando e inserire il comando :  openssl s_client -connect my.server.com : port -showcerts 2>null | openssl x509 -out certfile.txt
--- certfile.txt è _7_file-cer
--- my.server.com è _7_alias-cerificato
- Copiare il file file-cer nella cartella d'installazione di smens sull'IFS
- Collegarsi come QSECOFR
- Entrare in una sessione QSHELL :  "strqsh" da riga comando (in questo modo si avrà a disposizione una riga comado in una shell)
- Portarsi nella cartella di security della Java Virtual Machine "cd /QIBM/ProdData/Java400/jdk15/lib/security" (jdk15 indica che la Java Virtual Machine utilizzata è la 1.5, se dovesse essere diversa dovrebbe cambiare di conseguenza la cartella)
- Eseguire il seguente comando per importare il certificato nella Java Virtual Machine
-- keytool -import -alias _7_alias-certificato -file _7_/SmeExt/file-cer -keystore cacerts -storepass changeit

La procedura è completata, ora è possibile inviare attraverso il server SMTPS.

## Log e trace su AS400
E' attivabile un log per SMEDG e per SMENS su AS400 che tiene traccia, oltre che della versione dei software che si stanno utilizzando, di tutte le chimate alla G53 lanciate e di eventuali problemi riscontrati. Il file di log, qualora l'opzione sia abilitata viene creato per ogni differente utente As400 che lancia la generazione e risiede nella cartella Smeup/log relativa al percorso d'installazione. Per attivare questa opzione è necessario creare un file (anche vuoto) di nome logsmedg.yes per attivare il log di SMEDG, ed un file (anche vuoto) di nome logsmens.yes per attivare il log di SMENS nella cartella Smeup/log relativa al percorso d'installazione dell'IFS. A fronte dell'attivazione verranno creati dei file per ogni utente AS400 che richiama la G53 di nome rispettivamente NOMEUTENTE_pdf.log e NOMEUTENTE_smensserver.log  per i log della generazione Pdf e delle altre attività della G53.
E' inoltre attivabile un file di trace nella cartella Smeup/trace relativa al percorso d'installazione che riporta, in formato CSV informazioni sulle operazioni richieste dai programmi RPG. Per attivare questa opzione è necessario creare un file (anche vuoto) di nome tracesmens.yes nella cartella Smeup/trace relativa al percorso d'installazione dell'IFS. Come nel caso del file di log, il file di trace, qualora l'opzione sia abilitata viene creato per ogni differente utente As400 che lancia la generazione e risiede nella cartella Smeup/trace relativa al percorso d'installazione. In questo caso, a fronte dell'attivazione, verrà creato uu file per ogni utente AS400 che richiama la G53 di nome rispettivamente NOMEUTENTE_g53trace.log per le attività della G53.

## Protezione documenti generati
I file PDF generati con SmeDG permettono l'impostazione di una password a protezione della modifica del documento. Il comportamento di default è quello di generare files non protetti in lettura ma bloccati in modifica. E' possibile però gestire delle eccezioni.
Nella generazione di PDF tramite £G53 è infatti possibile impostare la password di modifica attraverso il parametro £G53MP. Tale parametro permette appunto di creare PDF con password di modifica personalizzata.
Se tale parametro è vuoto La /copy verificherà la presenza di un valore nel capo T$JA1H della tabella JA1. Attraverso questo campo è quindi possibile definire una password di modifica per tutti i PDF generati dalla £G53. Se tale campo è vuoto viene mantenuta la password di modifica hard-coded.
Vale sempre la regola che per disabilitare la presenza della password di modifica va usato il valore *NONE.
