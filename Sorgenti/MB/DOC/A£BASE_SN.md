# LANCIO DELL'ELABORAZIONE

Come accennato nella documentazione operativa i pgm di elaborazione di una stampa sono programmi eseguiti in batch, per tale motivo sul loro lancio e la loro esecuzione si rimanda al relativo documento.

- [Lancio&-x2f;Esecuzione Programma batch](Sorgenti/MB/DOC/A£BASE_SM)

# UTILITY PER LA PRODUZIONE DELL'OUTPUT

Per la produzione dell'output Smeup mette a disposizione una serie di utility che ne semplificano l'elaborazione. Queste sono quelle riportate di seguito : 

## LA £G18

Questa /COPY permette di produrre l'output secondo vari formati (Video 5250, Printer, PDF) scrivendo i dati dell'output in un formato generico, svincolato dalla forma di output, senza doversi inoltre preoccupare della definizione degli stessi (Printer File, Script ecc.) in quanto essa contiene già una serie di modelli standard.

- [Gestione Visualizzatore](Sorgenti/MB/DOC_OGG/P_TSTG18)

Quando poi le funzioni della suddetta /COPY risultino troppo vincolanti sono cmq disponibili le funzioni generiche, elencate di seguito, utilizzate della /COPY stessa, che possono essere a questo punto configurate in modo più specifico.

## UTILITY PER LA PRODUZIONE DI FILE PDF

### £G53

Fra le varie funzioni questa /COPY permette di produrre un file PDF a partire dalla scrittura di un file di testo prodotto secondo delle regole di codifica interna.

- [Mail, PDF, FTP, etc.](Sorgenti/MB/DOC_OGG/P_TSTG53)

### £H53

Tramite questa /COPY è possibile semplificare la scrittura dei file PDF che vengono prodotti tramite la £G53. In sostanza, viene scissa la definizione della struttura del PDF (Righe Intestazioni, Riquadri ecc.) che viene delegata a degli script, dalla valorizzazione dei che dati che riempiono la struttura stessa. Il programma deve perciò occuparsi solo di quest'ultima parte.

- [Funzione di generazione PDF](Sorgenti/MB/DOC_OGG/P_TSTH53)

## UTILITY PER LA PRODUZIONE DI FILE DI SPOOL

### UTILIZZO DEI PRINTER FILE INTERNI

Sono a disposizione una serie di PRINTER file standard definibili internamente ai programma.

 :  : DEC T(OJ) P(*FILE) K(PRT132)
 :  : DEC T(OJ) P(*FILE) K(PRT132A)
 :  : DEC T(OJ) P(*FILE) K(PRT198)
 :  : DEC T(OJ) P(*FILE) K(PRT198_01)
 :  : DEC T(OJ) P(*FILE) K(PRT198S)
 :  : DEC T(OJ) P(*FILE) K(PRT1982)
 :  : DEC T(OJ) P(*FILE) K(PRT80)
 :  : DEC T(OJ) P(*FILE) K(PRT80C)

In relazione ai printer sono disponibili una serie /COPY che riportare all'interno   del printer una serie di variabili di intestazione standard (sistema informativo, data    utente, ora di elaborazione ecc.)

 :  : DEC T(MB) P(QILEGEN) K(£TES080)
 :  : DEC T(MB) P(QILEGEN) K(£TES132)
 :  : DEC T(MB) P(QILEGEN) K(£TES132_1)
 :  : DEC T(MB) P(QILEGEN) K(£TES132_2)
 :  : DEC T(MB) P(QILEGEN) K(£TES198)
 :  : DEC T(MB) P(QILEGEN) K(£TES198_1)
 :  : DEC T(MB) P(QILEGEN) K(£TES198_2)
Di seguito un esempio di programma che utilizza i printer file standard.

 :  : DEC T(MB) P(QSRCGEN) K(G30_B)

Un aspetto da tenere in conto in merito all'utilizzo delle costati. Queste non vanno mai indicate direttamente nel printer come costanti, devono essere sempre utilizzate tramite variabili referenziate in schiere tipizzate per la traduzione. Si veda il relativo documento.

### UTILIZZO DEI PRINTER FILE ESTERNI

- [Identificare i lavori](Sorgenti/MB/DOC/A£BASE_01O)

### UTILIZZO DELLE TECNICHE DI OVL

Tramite le funzioni di OVL è possibile associare allo spool prodotto da una particolare elaborazione un'immagine grafica. Si rimanda alla relativa documentazione.

- [Utilizzo API IBM QSYSINC](Sorgenti/MB/DOC/A£BASE_01F)

# Configurazione cosa di stampa per stampanti Zebra
Esempio di comando per la creazione dell'OUTQ : 
CRTOUTQ OUTQ(SMESYS/ZEBRA) RMTSYS(*INTNETADR) RMTPRTQ(LPT1) AUTOSTRWTR(1) CNNTYPE(*IP) DESTTYPE(*OTHER) TRANSFORM(*YES) MFRTYPMDL(*WSCST) WSCST(QSYS/QWPDEFAULT) INTNETADR('192.168.1.xxx') TEXT('Coda di stampa Zebra')

# Configurazione Info Print Server

L'info Print server è un software per la creazione di file PDF partendo da uno spool.

Come primo passo è necessario creare una stampante PDF (CRTDEVPRT) con le seguenti caratteristiche : 

>Descrizione unità  . . . . . . . .  :   DEVD              PDFPRT
Opz. . . . . . . . . . . . . . . .  :   OPTION            *BASIC
Categoria dell'unità . . . . . . .  :                     *PRT

Classe unità . . . . . . . . . . .  :   DEVCLS            *LAN
Tipo unità . . . . . . . . . . . .  :   TYPE              *IPDS
Modello unità  . . . . . . . . . .  :   MODEL             0
Collegamento LAN . . . . . . . . .  :   LANATTACH         *IP
Stampa con funzioni avanzate . . .  :   AFP               *YES
Numero porta . . . . . . . . . . .  :   PORT              67
In linea a IPL . . . . . . . . . .  :   ONLINE            *YES
Font . . . . . . . . . . . . . . .  :   FONT
  Identificativo . . . . . . . . .  :                       011
  Dimensione punto . . . . . . . .  :                       *NONE
Alimentazione moduli . . . . . . .  :   FORMFEED          *CONT
Cassetto per separatori  . . . . .  :   SEPDRAWER         *FILE

Programma separatore . . . . . . .  :   SEPPGM            *NONE
Messaggio errore di stampante  . .  :   PRTERRMSG         *INQ
Coda messaggi  . . . . . . . . . .  :   MSGQ              *CTLD
Coda messaggi attuale  . . . . . .  :                     QSYSOPR
  Libreria . . . . . . . . . . . .  :                       QSYS
Tempificatore di attivazione . . .  :   ACTTMR            170
Configurazione immagine  . . . . .  :   IMGCFG            *NONE
Num. max richieste in sospeso  . .  :   MAXPNDRQS         6
Stampa durante conversione . . .  :     PRTCVT            *YES
Tempific. richiesta di stampa  . .  :   PRTRQSTMR         *NOMAX
Definizione moduli . . . . . . . .  :   FORMDF            F1C10110
  Libreria . . . . . . . . . . . .  :                       *LIBL

Identificativo carattere . . . . .  :   CHRID             *SYSVAL
Ubicazione remota  . . . . . . . .  :   RMTLOCNAME
  Nome o indirizzo . . . . . . . .  :                       127.0.0.1
Oggetto definito dall'utente . . .  :   USRDFNOBJ         PDF
  Libreria . . . . . . . . . . . .  :                       *QGPL
  Tipo oggetto . . . . . . . . . .  :                       *PSFCFG
Progr. trasf. dati . . . . . . . .  :   USRDTATFM         *NONE
Pr.un.di contr.def. ut.  . . . . .  :   USRDRVPGM         *NONE
Nome ubicazione dipendente . .  :       DEPLOCNAME        *NONE
Assegnato a : 
Nome lavoro  . . . . . . . . . . .  :                     PDFPRT
  Utente . . . . . . . . . . . . .  :                       QSPLJOB
  Numero . . . . . . . . . . . . .  :                       143887
Pubblicate . . . . . . . . . . . .  :                     *NO
Informazioni di pubblicazione  . .  :   PUBLISHINF
  Supporto fronte/retro  . . . . .  :                       *UNKNOWN
  Colore supporto  . . . . . . . .  :                       *UNKNOWN
  Pagine nere per minuto . . . . .  :                       *UNKNOWN
  Pagine colore per minuto . . . .  :                       *UNKNOWN
  Ubicazione . . . . . . . . . . .  :                       *BLANK

  Flussi di dati supportati  . . .  :                       *UNKNOWN
Testo  . . . . . . . . . . . . . .  :   TEXT              *BLANK


E' necessario poi compilare il programma B£PDFMAP (file source SMESRC) in QGPL (obbligatoria la compilazione, non copiare l'oggetto).

Successivamente bisogna creare l'oggetto  di tipo PSFCFG : 
CRTPSFCFG PSFCFG(QGPL/PDF) PDFGEN(*STMF) PDFDIR('/GMMPDF') PDFMAPPGM(QGPL/B£PDFMAP)

A questo punto è necessario avviare il device precedentemente creato : 
WRKCFGSTS CFGTYPE(*DEV) CFGD(PDFPRT)
In questo momento PDFPRT dovrebbe apparire VARIED OFF, usare l'opzione 1 per attivarla

Effettuare una stampa di prova. Potrebbe essere necessario rispondere al messaggio di caricamento moduli prima di poter stampare correttamente.

Per stampare è sufficiente indirizzare lo spool sulla coda di output PDFPRT. Nell'attributo USRDFNDTA dello spool è possibile indicare il percorso e il nome del file pdf da creare.


