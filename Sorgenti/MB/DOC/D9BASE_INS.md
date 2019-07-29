Per l'installazione di Cube.up seguire i punti spiegati di seguito.
Esistono due tipi di comunicazione tra AS400 e host, che si possono affiancare o in base alle esigenze scegliere tra uno e l'altro.
In generale conviene utilizzare lo Smens (Sme.up Network Service) che permette un numero di opzioni maggiore rispetto al Pc Organizer del Client Access, come ad esempio di svincolare le funzioni del Pc da quelle della macchina da cui è partita l'estrazione da As400, e di non essere vincolati al Client Access.
Per contro è sicuramente più immediata da far partire la comunicazione Pc organizer, anche se è utilizzabile solo dove è usato come emulatore il Client Access.

## Prerequisiti
Si consiglia di utilizzare sempre l'ultimo rilascio di Sme.up perchè il modulo D9 si basa su alcuni programmi di nuova concezione. Avere installato una release recente di Os400 (dalla 4.2) e di Client Access (dalla 3.2).
È consigliabile installare le PTF dell'AS400 relative al Netserver, che variano a seconda della release dell'Os400. Per verificare quelle necessarie visitare il sito www.as400.ibm.com/netserver.
Consigliabile anche installare il service pack del Client Access, che varia a seconda della versione che si ha installato
 * Installazione del Databeacon :  installazione e configurazione del Databeacon sul pc dal quale si faranno le estrazioni da Sme.up, con relativa licenza del cliente se presente o con licenza Demo di Softia
 * Installazione del modulo D9 di Sme.up :  portare e integrare tutti i programmi, le tabelle, i menu del modulo D9 nell'ambiente Sme.up già installato dal cliente, vedere sezione specifica.
 * Installazione Smens o utilizzo del PC Organizer :  installazione e configurazione dello Smens sull' AS400 e sui pc dal quale si faranno le estrazioni da Sme.up
 * Configurazione Netserver (solo se si utilizza il Pc Organizer) :  creazione di un'unità di rete dell'As400 che è vista dalla rete sotto Windows. È necessario configurare una parte da AS400 e una parte da Client Access.
 * Provare ad estrarre un cubo partendo da Sme.up. Se non funziona rivedere la procedura.

La procedura completa va fatta la prima volta che si installa Cube_up. Per preparare una nuova postazione Pc per estrarre da Sme_up è sufficiente eseguire i punti 1 e 3 della procedura, ovvero installare sul Pc il Databeacon e lo Smens.

# Databeacon
Normalmente Databeacon viene installato su un server, appoggiato ad un Webserver (IIS, Apache..) e viene quindi visto in rete dai client via Intranet o Internet direttamente dal Browser.
La comunicazione avviene tramite lo Smens, installato su As400 e sul server.

## Installazione
 - Scaricare dal sito www.internetivity.com la versione Demo di Db probe
 - Lanciare il file eseguibile e procedere all'installazione con la procedura standard di Windows.
 - Selezionare no quando chiede di installarlo come web server.
 - A fine installazione autorizzare il programma con i runcode forniti dalla società Internetivity per il cliente specifico o con la procedura Demo di Softia.
 - Leggere il file txt fornito da loro che spiega passo passo come agire.

La versione di Databeacon installata sul propio pc serve a chi deve creare cubi sia normali che da Sme.up. Per vederli visualizzati basta aprire il cubo su un Pc dove è installato il Databeacon, che può essere un computer di rete o un server web giustamente configurato come da manuale databeacon.

Quando si installa il programma si installa anche la documentazione su come utilizzare al meglio il Databeacon, sia come visualizzatore cubi che come creatore di cubi da altre fonti.
Si consiglia, se non è già presente, di installare sul Pc dove si usa Databeacon Acrobat Reader per produrre stampe dai cubi. Infatti la stampa avviene attraverso questo programma.
	
# Installazione del modulo D9 di Sme.up
Per poter far funzionare il modulo D9 di Sme.up è necessario : 
 * un rilascio recente di Sme.up, che contiene tutti i sorgenti, i  programmi, i menu, le /copy D9
 * le tabelle D9 tutte
 * i file D9WK*
 * i programmi di controllo delle tabelle D9
 * determinati programmi B£ di gestione degli OAV, di decodifica oggetti e tabelle, ed alcune nuove utility, il più recenti possibili
 * alcuni nuovi oggetti (creare oggetto "V3" nella *CNTT, Valori Sme_up dinamici, elemento "*UP" nella tabella *CND1 con descrizione "formato data dinamica)

A seconda dei programmi specifici di estrazione controllare che funzionino in ambienti diversi da quelli con l'ultimo rilascio.
Per ulteriori istruzioni leggere il capitolo Cube.up.
	
# Installazione Comunicazione Host
Si possono utilizzare due diverse tecniche di comunicazione con l'host, come precedentemente illustrato. Possono essere affiancate oppure in base alle esigenze decidere quale delle due è la più indicata.

Non si deve installare niente sul Pc. Si consiglia di controllare se la versione del Client Access supporta questa funzione. Per provare se è attiva, si deve digitare da una sessione AS400 il comando STRPCO, e in seguito provare ad eseguire un prgramma con il comando STRPCCMD e poi il tasto F4 per inserire i suoi parametri. Ad esempio si può provare a lanciare notepad.exe di Windows.

Come prerequisito è necessario aver avviato (vedi capitolo specifico) il servizio di As400 Netserver.

Per installare SMENS si deve possedere il Cd-rom di installazione e la relativa procedura (vedi capitolo specifico), che prevede un'installazione su AS400 di una applicazione JAVA e delle librerie di funzionamento. Anche Sui Pc dai quali si vuole comunicare è necessario installarlo. Questo server Java permette di fare chiamate da As400 direttamente ad un PC qualsiasi della rete sul quale sia installato lo SmeNS, semplicemente utilizzando il protocollo Tcp-ip.
Quando installato, bisogna accertarsi che sia attivo sul Pc o sul Server quando esso riceve delle chiamate di esecuzione, come quella per la creazione di un cubo.
	
## Installazione Smens
Procedura da attuare solo se si utilizza come tipo comunicazione Host Sme.up Network Service.

L'installazione si compone di una parte su AS400 e di una parte su tutti gli host (PC o server) che devono fungere da client, ovvero tutti quelli che devono direttamente comunicare con As400, per fare chiamate o per essere chiamati.

Questo servizio permette di far comunicare AS400 con PC in rete, e permette di : 
 * Aprire file ed eseguire programmi sul PC
 * Eseguire FTP da e verso l'AS400
 * Mandare E-mail senza configurare un percorso dell'AS400 a internet per essere un client o un server di posta
	
### Smens su AS400
Entrare con un profilo alto QSECOFR o QPGMR. Si consiglia di riavviare il computer ed entrare da subito nei collegamenti del Client Access e fare il login come Qsecofr o Qpgmr prima di entrare in As400 o in rete.
Da una sessione AS400 : 
>_1_
CRTDIR DIR('/Smeup') DTAAUT(*RX) OBJAUT(*OBJEXIST)

DIR	> /Smeup
DTAAUT 	> *RX
OBJAUT	> *OBJEXIST
CRTOBJAUD	*SYSVAL



>N.B. :  Per il nome DIR è Key sensitive

Per visualizzare tutte le cartelle e quella creata utilizzare il comando

_1_WRKLNK

Per modificare le autorizzazioni dell'oggetto se da problemi entrare con opzione 9 per verificare autorizzazioni ed eventualmente modificarle.

Si può vedere sul PC la cartella creata in modi diversi : 
 * Creare il collegamento alla cartella Smeup con il Netserver se già avviato. Si collega da operations navigator come spiegato nella sezione configurazione Netserver.
 * Dall'unità di rete attivata da client access in risorse di rete, nome dell'As400.
 * Quando vedo la cartella Smeup dell'As400 posso copiargli dentro le cartelle "Smens" e "Lib" con tutti gli oggetti contenuti dal cd-rom di installazione. Attenzione agli attributi dei file sul cd-rom che possono essere di sola lettura. Per trasportarli èsi consiglia di creare uno Zip di tutti i file.
	
### Smens su host
Teoricamente vista la portabilità dell'ambiente Java, Smens può essere installato su vari sistemi operativi (Pc windows 95/98/2000/Nt, linux, ecc..). Per meglio spiegare il processo di installazione verrà fatto riferimento all'ambiente Windows. Per installazioni su altri tipi di host, contattare il support SME.up.

Per permettere la comunicazione da As400 ad un host specifico, è necessario eseguire sull'host i seguenti passi : 
 * Installare la Java virtual machine (JDK sul cd-rom distribuita gratuitamente), che significa spostare in c : \ la cartella JDknn
 * Copiare le directory "Smens" e "Lib" nella cartella Smeup (se non esiste crearla in C : \)
 * Lanciare config.bat ed impostare le informazioni necessarie

Una volta installato è necessario che sia attivo quando deve comunicare con As400.

Attivare Smens ogni qualvolta debba essere utilizzato, lanciando il file startserver.bat e lasciarlo attivo finchè si utilizza. Per interrompere l'applicazione lanciare il file stopserver.bat. Per riavviarlo fermarlo e poi rilanciare lo startserver.bat. Personalizzando lo script si può nascondere l'applicazione in esecuzione.

Per testare il suo funzionamento, utilizzare il pgm TSTG53 che ne gestisce le chiamate, e provare se apre i file, o esegue programmi o se riesce a fare FTP.
L'utility di chiamata G53 utilizza le tabelle B§H (nome host con associato un'indirizzo IP) e la JA1 (nome utente e password di AS400 per fare gli FTP).
	
## Configurazione Netserver di As400
Procedura da attuare solo se si utilizza come tipo comunicazione Host il Pc Organizer.
	
### Configurazione da AS400
Prerequisiti :  entrare con profilo QSECOFR
 * Creare su AS400 profilo utente NSGUEST, password *NONE, classe utente *USER, e autorizzazioni speciali *NONE ===> CRTUSRPRF USRPRF(NSGUEST) PASSWORD() USRCLS(*USER) TEXT('Utente assunto per NETSERVER') SPCAUT(*NONE) AUT(*USE)
 * Iscrivere utente NSGUEST ad indirizzario di sistema : 
 ** WRKDIRE 1=aggiunta
 *** Utente :     NSGUEST
 *** Indirizzo :  S44xxxxx   (nome del sistema As400)
 ** Compilare i campi : 
 *** Descrizione . . . . . .   Net Server Guest
 *** Nome sist./Gruppo . . .   S44xxxxx
 *** Profilo utente  . . . .   NSGUEST
 *** ID utente rete  . . . .   NSGUEST  S44xxxxx
 ***  le altre impostazioni sono di default.	
 * Creare la Cartella condivisa "SMEC_S" nella QDLS
 ** GO FOLDER
 ** gestire le cartelle (Aggiungi 1  SMEC_S)
 *** Cartella . . . . . . . . . . . . . .   SMEC_S         Nome
 *** Descrizione cartella . . . . .    Cartella per estrazione Cubi
 *** Profilo
 *** per documenti  . . . . . . . . ______________   (lasciare bianco)
 *** ID lotto di memoria ausiliaria . . .   1              1-16
 * Entrare con l'opzione 14 sulla SMEC_S e impostare autorizzazione pubblica *ALL

### Configurazione da Client Access
Prerequisiti :  entrare con profilo Administrator sul PC da cui si configura il NETSERVER; è consigliato scollegare e ricollegare l'accesso ad AS400 con il Client/Access usando il profilo QSECOFR
 * Configurare NETSERVER tramite Operations Navigator : 
 ** Selezionare il percorso Rete/Server/ e selezionare la voce NETSERVER (o Server di rete); se non c'è vedere sotto la voce TCP/IP (varia a seconda della release del Client Access)

>N.B. :  Se non è possibile visualizzare il percorso indicato si deve integrare l'attuale installazione del Client Access. Aprire dallla barra d'avvio il menu del Client Access, aprire accessori e selezionare la voce "Installazione selettiva" (Selective setup). Inserire il Cd di Client Access e selezionare "seleziona una fonte alternativa", e indicare il percorso del Cd fino a Install/image; oppure, se non si dispone dell Cd selezionare "utilizza il sistema S44xxxxx". Selezionare "AS400 Operations Navigator" e premere "Detttagli" o fare un doppio clic. Selezionare per sicurezza tutte le voci (basterebbe Network o Rete) e premere "Continua". Arrivare fino in fondo all'installazione e riavviare il computer. Se serve riinstallare il service pack del client access. Ora dovrebbe essere possibile visualizzare il percorso dall'Operations Navigator.

 ** Tasto destro del mouse scegliere proprietà
 *** Nome server : 	Q+nome sistema
 *** Nome dominio o gruppo : 	nome del dominio di rete principale della rete NT
 *** Profilo Utente : 	NSGUEST
 *** Codepage : 	850
 * Creazione condivisione tramite Operations Navigator : 
 ** aprire la voce NETSERVER o SERVER DI RETE
 ** selezionare OGGETTI CONDIVISI e con il tasto destro cliccare nuovo - file
 ** compilare la finestra di dialogo con : 
 *** nome condiviso : 	Smecs
 *** descrizione : 	Cartella Per Cubi
 *** permessi : 	Lettura/Scrittura
 *** Nessun Valore Max
 *** Percorso : 	//Qdls/Smec_S
	
### Avvio da AS400 del Netserver
 - Verificare se dopo la configurazione il Netserver è già partito. Se si saltare la procedura di seguito, se no eseguirla.
 - La prima volta o tutte le volte che non parte il Netserver fare l'avvio manuale per la sessione in corso CALL QZLSSTRS PARM('0' X'00000000')
 - Modificare o creare programma di avvio sistema specificato in valore di sistema QSTRUPPGM, implementando l'avvio automatico del NETSERVER, all'avvio della macchina AS400 : 
per trovare il sorgente fare DSPOBJD di tipo *PGM e nome del Qstruppgm

Verificare le voci con davanti &&&&&&&&&&& nel sorgente che segue e in caso aggiungerle.
Poi ricompilare seguendo le istruzioni del PGM

Programma Qstrup_sm esempio del Pgm SME.up : 
>/******************************************************************************/
/* ATTENZIONE :  compilare con  USRPRF(*OWNER)	*/
/*             quindi modificare l'oggetto	*/
/*  CHGOBJOWN OBJ(QGPL/QSTRUP_SM) OBJTYPE(*PGM) NEWOWN(QSECOFR)*/
/**************************************************************************/
/* 5769SS1 V4R3M0 980729    Emissione RTVCLSRC   14/11/98 14 : 28 : 42*/
/*                                                                  	*/
/* Nome programma . . . . . . . . . . . . .  : 	QSTRUP	PN*/
/* Nome libreria  . . . . . . . . . . . . .  :    	QSYS	PL*/
/* File origine originale . . . . . . . . .  : 	SN*/
/* Nome libreria  . . . . . . . . . . . . .  : 	SL*/
/* Membro origine originale . . . . . . . .  :   : 	SM*/
/* Modifica file origine	*/
/* data/ora . . . . . . . . . . . . . . .  : 	SC*/
/* Opzione di correzione  . . . . . . . . .  : 	*NOPATCH	PO*/
/* Profilo utente . . . . . . . . . . . . .  : 	*USER	UP*/
/* Testo  . .  : 	TX*/
/* Proprietario . . . . . . . . . . . . . .  : 	QSYS	OW*/
/* ID modifica correzione . . . . . . . . .  : 	PC*/
/* ID correzione APAR . . . . . . . . . . .  : 	PA*/
/* Indicatore di modifica utente  . . . . .  : 	*NO	UM*/
/*	ED*/
/***************************************************************************/
PGM
DCL VAR(&STRWTRS) TYPE(*CHAR) LEN(1)
DCL VAR(&CTLSBSD) TYPE(*CHAR) LEN(20)
DCL VAR(&CPYR) TYPE(*CHAR) LEN(90) VALUE('5769-SS1 (C) COPYRIGHT
IBM CORP 1980, 1997. LICENSED MATERIAL - PROGRAM PROPERTY OF IBM')
QSYS/STRSBS SBSD(QSPL)
QSYS/STRSBS SBSD(QSPL)
MONMSG MSGID(CPF0000)
QSYS/STRSBS SBSD(QSERVER)
MONMSG MSGID(CPF0000)
QSYS/RLSJOBQ JOBQ(QGPL/QS36MRT)
MONMSG MSGID(CPF0000)
QSYS/RLSJOBQ JOBQ(QGPL/QS36EVOKE)
MONMSG MSGID(CPF0000)
QSYS/STRCLNUP
MONMSG MSGID(CPF0000)
QSYS/RTVSYSVAL SYSVAL(QCTLSBSD) RTNVAR(&CTLSBSD)§
IF COND((&CTLSBSD *NE 'QCTL      QSYS      ') *AND (&CTLSBSD *NE-'QCTL QGPL ')) THEN(GOTO CMDLBL(DONE))
QSYS/STRSBS SBSD(QINTER)
MONMSG MSGID(CPF0000)
QSYS/STRSBS SBSD(QBATCH)
MONMSG MSGID(CPF0000)
MONMSG MSGID(CPF0000)
QSYS/STRSBS SBSD(QCMN)
MONMSG MSGID(CPF0000)
DONE : 
QSYS/RTVSYSVAL SYSVAL(QSTRPRTWTR) RTNVAR(&STRWTRS)
IF COND(&STRWTRS = '0') THEN(GOTO CMDLBL(NOWTRS))
CALL PGM(QSYS/QWCSWTRS)
MONMSG MSGID(CPF0000)
NOWTRS : 
/* INIZIO TASK AGGIUNTIVI  - TCP/IP HOST SERVER  */
&&&&&     QSYS/STRTCP
MONMSG MSGID(CPF0000)
&&&&&&&     QSYS/STRTCPSVR *ALL
MONMSG MSGID(CPF0000)
&&&&&&&     QSYS/STRHOSTSVR *ALL
MONMSG MSGID(CPF0000)
/* FINE   TASK AGGIUNTIVI  - TCP/IP HOST SERVER  */
/* INIZIO TASK STRSBS QSNADS */
QSYS/STRSBS SBSD(QSNADS)
MONMSG MSGID(CPF0000)
/* FINE   TASK STRSBS QSNADS */
/* AVVIO SERVIZIO NETSERVER */
&&&&&&&&     DLYJOB DLY(300)
&&&&&&&&     CALL QZLSSTRS PARM('0' X'00000000')
RETURN
CHGVAR VAR(&CPYR) VALUE(&CPYR)
ENDPGM

	
### Verifica funzionamento Netserver
 * Selezionare Trova Computer dalla Barra avvio di Windows
 * Cercare il nome del netserver che si è creato (QSxxxxxx)
 * Se si vede e aprendolo vedo la cartella Smecs e posso portare con il drag&drop dei file all'interno, aprirli e cancellarli  significa che il Netserver è avviato e funziona correttamente
 * Se non funziona rivedere la procedura
	
### Aggiornamento PTF per Netserver
Fare riferimenuto al sito internet dell'AS400 per la lista di PTF necessarie per la release dell'AS400 in questione. www.as400.ibm.com/netserver/infoapar.htm
Di seguito viene riportata la procedura per installare le PTF della Release 4.4 di Os400.
Utilizzarla come esempio e non prenderla alla lettera.
In questo caso le PTF sono salvate nella libreria QDLS come SAVF, normalmenute si scaricano via Modem da AS400 direttamenute dall'ÌBM
Verificare la lista delle PTF necessarie, che se eventualmenute presenti non vanno caricate...> caricare quelle che mancano.

Con il comando
_1_DSPPTF *ALL per listarle tutte

oppure, per listarle separate

_1_ DSPPTF 5769999 MFxxxxx

DSPPTF 5769SS1 SFxxxxx

devono essere applicate temporaneamenute, permanentemenute o superate.

Dopo essersi assicurati che il file QGPL/QAPZCOVER non contenga dei membri (se ne contiene eventualmenute rinominarlo come old), restorizzare i seguenti oggetti nella libreria QGPL con : 
RSTOBJ OBJ(*ALL) SAVLÌB(QGPL) DEV(TAPxx)

**************se non funziona... farlo una ad una
>	RSTOBJ OBJ(
	QAPZCOVER
	QSF54003
	........
	QMF23628) SAVLÌB(QGPL) DEV(TAPxx)
**************
Caricare le PTF con il comando : 
LODPTF LÌCPGM       > 5769999
       DEV            *SERVÌCE
	SELECT       > MFxxxxx
	MFyyyyy
	.......
	LODPTF LÌCPGM       > 5769SS1
	DEV            *SERVÌCE
	SELECT       > SFxxxxx
**********se non funzionasse con *SERVÌCE (....) è necessario caricare le PTF una ad una....
	LODPTF LÌCPGM       > 5769999
	DEV            *SAVF
	SELECT       > MFxxxxx
	SAVF           QMFxxxxx
	QGPL
**************
APYPTF LÌCPGM       > 5769999
	RLS            *ONLY
	SELECT       > MFxxxxx
	APY            *TEMP
	DELAYED      > *YES
	ÌPLAPY
	*YES
	*APYPERM
	APYREQ         *NO
	APYPTF LÌCPGM       > 5769SS1
	RLS            *ONLY
	SELECT       > SFxxxxx
	APY            *TEMP
	DELAYED      > *YES
	ÌPLAPY
	*YES
	*APYPERM
	APYREQ         *NO

