 :  : PRO Cod(A01) Txt(Esercizi) STAT(00) RESP(SCIMAM)

 :  : ATT Cod(001) Txt(Creazione di una scheda)  STAT(10) RESP(SCIMAM)
//--***************************************************************
//--  CREAZIONE DI UNO SCRIPT DI SCHEDA        *
//--***************************************************************

01. La SCHEDA in SmeUP
//-- ********************** CAPITOLO 1 **********************

Con la parola SCHEDA in SmeUP ci si riferisce ad una specie di contenitore che ci permette di visualizzare i componenti grafici all'interno di LoocUp o WebUP, riuscendo a definirne la posizione ed il contenuto.
La scheda viene costruita scrivendo uno script (chiamato script di scheda) che viene poi interpretato da un programma che lo trasforma in XML per essere dato in pasto al  componente EXD in grado di visualizzare a video in maniera corretta il contenuto.

Per una documentazione più approfondita si rimanda alla funzione A dell'esercizio corrente.
 :  : DEC T(J1) P(FUN) D(A. Documentazione SCHEDA) K(F(EXD;*SCO;) 1(MB;DOC;LOCEXD_B) 2(MB;SCP_SCH;OGDOCU) P(TPM(SIN) POP(1) PRF(1)))

Per visualizzare il componente scheda, arrivabile anche tramite la pressione tasto F1 per avere informazioni, è visionabile tramite la funzione B dell'esercizio corrente
 :  : DEC T(J1) P(FUN) D(B. Il componente SCHEDA) K(F(EXD;*SCO;) 1(V2;JAGRA;EXD))

02. Aprire un oggetto di tipo scheda
//-- ********************** CAPITOLO 2 **********************

NB :  !!!  PER ESEGUIRE QUESTO ESERCIZIO ESSERE SICURI DI ESSERSI COLLEGATI AL SERVER DI SVILUPPO + W (OVVERO LO SVIU) !!!

Il metodo più veloce per aprire un oggetto di tipo scheda è quello di ricercare un membro (MB) all'interno di uno specifico file (SCP_SCH) ed indicarne il nome se lo si conosce, altrimenti utilizzare il comando "!" per visualizzarli tutti e scegliere quello voluto.
Vedremo ora come arrivare allo script di una scheda ricercandolo sia in WebUP che in LoocUP ed utilizzeremo per esempio una scheda dello showcase del semaforo.

Si noti inoltre che TUTTI  gli script di scheda si trovano all'interno del file SCP_SCH.

02.A. Aprire uno script di scheda in LoocUP
    1- Cliccare sulla lente di ingrandimento vicina allo spotlight (o tramite la pressione di F4)
    2- Inserire nel box di ricerca
                   - il tipo "MB" (ovvero di ricercare un tipo membro)
                   - il parametro "SCP_SCH" (ovvero il file in cui ricercare il membro)
                   - il codice "WETEST_SEM" (ovvero lo script di scheda del semaforo dello showcase)

Il risultato finale dovrebbe essere come quello nella funzione B dell'esercizio corrente
 :  : DEC T(J1) P(FUN) D(C. Scheda Semaforo) K(F(EXD;*SCO;) 1(MB;SCP_SCH;WETEST_SEM))

02.B. Aprire uno script di scheda in WebUP
Metodo utilizzabile anche in LoocUP ma che reputo più corretto utilizzare in WebUp
    1- Cliccare sullo spotlight in alto (se non visualizzato cliccare sulla lente di ingrandimento oppure ALT+SHIFT+F9)
    2- Scrivere nell'input "O MB SCP_SCH WETEST_SEM" (!!! Attenzione agli spazi !!!)

Il risultato finale dovrebbe essere come quello nella funzione B dell'esercizio corrente

03. Copiare uno script di scheda
//-- ********************** CAPITOLO 3 **********************

Una consuetudine spesso utilizzata da compiere quando si intende creare una nuova scheda è quella di copiarne una già esistente nel proprio ambiente di lavoro, dopodichè applicare le proprie modifiche solo a quella nella propria libreria. Vediamo quindi i passi di come si può copiare una scheda esistente nella propria zona di lavoro.

Dopo aver completato il passo 2 (ed essere quindi sulla scheda del semaforo) : 
    1- Nel menu laterale di sinistra scegliere GESTIONE -> COPIA
    2- Nel campo "libreria" indicare la propria libreria personale (che solitamente è composta da "W_<nomeutente>", nel mio caso è W_SCIMAM dove SCIMAM è il mio nome utente)
    3- Nel campo "membro" inserire il nome che si vuole dare allo script di scheda che andrà a salvarsi nella nostra libreria (in questo caso inseriamo "SCH_PROVA")
    4- Il campo "tipo sorgente" indica al server AS la tipologia del membro che andremo a creare. Inseriamo quindi la dicitura "OTH" che indica una tipologia generica
    5- Nel campo "testo" inseriamo una didascalia di massimo 50 caratteri per indicare cosa conterrà il sorgente, in questo caso inseriamo "Scheda di prova"
    6- Confermiamo la copia del file




04. Visualizzare una scheda
//-- ********************** CAPITOLO 4 **********************

Per visualizzare il risultato dello script di una scheda basta digitare nello spotlight
"SCH <nomeDellaScheda>"

Nel nostro caso "SCH SCH_PROVA"


05. Editare uno script di scheda
//-- ********************** CAPITOLO 5 **********************

Prima di inziare a modificare uno script, è bene sapere che all'interno di una scheda si ha la definizione di : 
 1- Un layout grafico
 2- I dati da presentare a video

Il layout grafico viene definito da delle "sezioni" e delle "subsezioni" che non fanno nient'altro che suddividere lo schermo in "fette" orizzontali (tramite i numeri) o "fette" verticali (tramite le lettere). Vengono così generate delle finestre all'interno della nostra scheda.
Ogni sezione deve contenere una o più subsezioni; in ogni subsezione un componente visualizza un insieme di dati, fornito come XML da un programma RPG.
La subsezione invece si addossa il compito di presentare i dati, che possono essere visualizzati tramite un componente grafico (albero, matrice, ecc...) oppure tramite un componente specifico della scheda (label di testo, semafori...)

NB :  Essendo la scheda stessa un componente grafico, una subsezione di scheda può contenere a sua volta una scheda.

05.A. Creazione di una sezione
    1- Ogni comando in uno script di scheda inizia con " :  : "
    2- Per creare una sezione basta inserire il comando :  G.SEZ
    3- Dopodichè è necessario inserire la posizione con Pos(<lettere o numeri>)
    4- E' possibile inserire inoltre la dimensione con Dim(<dimensione in pixel o in percentuale>)

05.A.1. Esercizio 1 - Creazione 2 sezioni verticali
    1- Inserire la prima sezione con G.SEZ
    2- Inserire posizione Pos(A)
    3- Inserire dimensione Dim(50%)
    4- inserire la seconda sezione con G.SEZ
    5- Inserire posizione Pos(B)
    6- Inserire dimensione Dim(50%)

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali.ad ogni istruzione per funzionare)
(Risultato nella sezione Funzioni dell'esercizio)
 G.SEZ Pos(A) Dim(50%)
 G.SEZ Pos(B) Dim(50%)

NB :  Avendo solamente diviso la scheda principale in sezioni e non avendoci inserito nessun componente, non sarà possibile vedere nulla, se non delle "righe divisorie".
 :  : DEC T(J1) P(FUN) D(ES_05.A.1 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_A_001))

05.A.2. Esercizio 2 - Creazione 2 sezioni orizzontali
    1- Inserire la prima sezione con G.SEZ
    2- Inserire posizione Pos(1)
    3- Inserire dimensione Dim(20%)
    4- inserire la seconda sezione con G.SEZ
    5- Inserire posizione Pos(2)
    6- Non inserendo nulla la seconda scheda prende la dimensione massima disponibile

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
(Risultato nella sezione Funzioni dell'esercizio)
  G.SEZ Pos(1) Dim(20%)
  G.SEZ Pos(2)

NB :  Avendo solamente diviso la scheda principale in sezioni e non avendoci inserito nessun componente, non sarà possibile vedere nulla, se non delle "righe divisorie".
 :  : DEC T(J1) P(FUN) D(ES_05.A.2 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_A_002))

05.A.3. Esercizio 3 - Creazione sezioni avanzate
L'idea è quella di avere più sezioni con un layout ben preciso.
Questo layout prevede una sezione che riempia verticalmente metà schermo. Dopodichè altre quattro sezioni che vengano visualizzate in questo ordine :  una nella prima riga, due nella seconda riga e l'ultima nella terza riga.

    1- Inserire la prima sezione con G.SEZ
    2- Inserire posizione Pos(A)
    3- Inserire dimensione Dim(50%)
    4- inserire la seconda sezione con G.SEZ
    5- Inserire posizione Pos(B1)
    6- inserire la terza sezione con G.SEZ
    7- Inserire posizione Pos(B2A)
    8- Inserire la dimensione con Dim(50%)
    9- Inseire la quarta sezione con G.SEZ
  10- Inserire la posizione con Pos(B2B)
  11- Inserire la quinta sezione con G.SEZ
  12- Inserire la posizione con Pos(B3)

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
(Risultato nella sezione Funzioni dell'esercizio)
  G.SEZ Pos(A) Dim(50%)
  G.SEZ Pos(B1)
    G.SEZ Pos(B2A) Dim(50%)
    G.SEZ Pos(B2B)
  G.SEZ Pos(B3)

NB :  Avendo solamente diviso la scheda principale in sezioni e non avendoci inserito nessun componente, non sarà possibile vedere nulla, se non delle "righe divisorie".
 :  : DEC T(J1) P(FUN) D(ES_05.A.3 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_A_003))

05.B. Creazione di una subsezione
Dopo aver creato una sezione, per creare una subsezione bisogna inserire il comando :  "G.SUB.<tipocomponente>" dove il tipo di componente è (al momento della scrittura di questo articolo) uno fra quelli proposti in calce.
Una subsezione per funzionare ha bisogno (tranne per la FLD) di un campo D.OGG che ne identifica i dati da visualizzare.

Accordion (ACC)
Bottoni (BTN)
BoxList (BOX)
Calendario (CAL)
Grafico (GRA)
Emulatore (EMU)
Field (FLD)
Cruscotto (GAU)
Gantt (GNT)
HTML (HTM)
Immagine (IMG9
Lista immagini (IML)
Pannello di Input (INP)
Pannello di output (OUT)
Label (LAB)
Matrice (MAT)
Matrice di aggiormamento (EXU)
ActiveX (OCX)
Pdf viewer (PDF)
Editor (CDE)
TreeMap (TMP)
Preview (PRW)
Scheda oggetto (SCH)
Semaforo (SEM)
Spotlight (SPL)
Albero con tab (TRA)
Albero (TRE)
Testo (TXT)
Messaggio (MSG)
Device (DEV)
Con conferma (UMC)
Con richiesta configurazione (UCF)
Con richeiesta di Query (UQR)
Con richiesta Parametri (UPA)
Mind map (MIN)
Tag Cloud (TCL)
SpreadSheet (SHE)
Camera (CAM)
JSON (JSO)
Editor di script (XED)
Paypal (PAY)
Organigramma (OGN)
Horizontal Tree (HTR)
Activity Timeline (ATM)
Knob (KNO)
Line (LIN)
Path (PAT)

05.B.1. Esercizio 1 - Creazione di subsezioni di tipo label
    1- Dopo aver effettuato uno fra gli esercizi del punto 05.A
    2- Inserire il componente Field all'interno delle sezioni create precedentemente con G.SUB.FLD
    3- Obbligatorio dare un titolo ad ogni subsezione con il comando Tit="<titolo>", nel caso non lo si voglia dare inserire "*NONE"

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
(Risultato nella sezione Funzioni dell'esercizio)
  G.SEZ Pos(A) Dim(50%)
      G.SUB.FLD Tit="Field A"
  G.SEZ Pos(B1)
      G.SUB.FLD Tit="Field B1"
      G.SEZ Pos(B2A) Dim(50%)
          G.SUB.FLD Tit="Field B2A"
      G.SEZ Pos(B2B)
          G.SUB.FLD Tit="Field B2B"
  .SEZ Pos(B3)
      G.SUB.FLD Tit="Field B3"

 :  : DEC T(J1) P(FUN) D(ES_05.B.1 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_B_001))

05.B.2. Esercizio 2 - Creazione di subsezione di tipo bottone
    1- Dopo aver effettuato uno fra gli esercizi del punto 05.A
    2- Inserire il componente Bottone all'interno di due sezioni verticali che dividono lo schermo con G.SUB.BTN
    3- Obbligatorio dare un titolo ad ogni subsezione con il comando Tit="<titolo>", nel caso non lo si voglia dare inserire "*NONE"
    4- Inserire ora altre tre sezioni in ogni sezione del punto 2. Le tre sezioni devono essere disposte parallelamente.
    5- Anche in questo caso inserire un componente bottone per ogni sezione creata.
    4- Inserire un campo D.OGG per indicare i dati da inserire nel botone e nel parametro inserire D(<label bottone>)

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
(Risultato nella sezione Funzioni dell'esercizio)
  G.SEZ Pos(A1) Dim(50%)
    G.SUB.BTN Tit="Bottone A1"
      D.OGG D(Bottone 1)
  G.SEZ Pos(A2)
    G.SEZ Pos(A2A) Dim(50%)
      G.SUB.BTN Tit="Bottone A2A"
        D.OGG D(Bottone 3)
      G.SEZ Pos(A2B) Dim(50%)
        G.SUB.BTN Tit="Bottone A2B"
          D.OGG D(Bottone 4)
       : G.SEZ Pos(A2C) Dim(50%)
        G.SUB.BTN Tit="Bottone A2C"
           : D.OGG D(Bottone 5)
  G.SEZ Pos(B1)
    G.SUB.BTN Tit="Bottone B1"
      D.OGG D(Bottone 2)
  G.SEZ Pos(B2)
    G.SEZ Pos(B2A)
      G.SUB.BTN Tit="Bottone B2A"
        D.OGG D(Bottone 6)
    G.SEZ Pos(B2B)
      G.SUB.BTN Tit="Bottone B2B"
        D.OGG D(Bottone 7)
    G.SEZ Pos(B2C)
      G.SUB.BTN Tit="Bottone B2C"
        D.OGG D(Bottone 8)

 :  : DEC T(J1) P(FUN) D(ES_05.B.2 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_B_002))

05.C. Riempire i componenti con dati fittizzi
Per comprendere al meglio l'utilizzo dell'inserimento di dati fittizzi nei componenti si rimanda al capitolo sui prototipi : 
"Come generare dati prototipo"

05.D. Utilizzo di due componenti con relativi settaggi
Dopo aver creato una sezione, e la subsezione è giunto il momento di creare una subsezione che possa essere settata a piacimento.
Questo viene fatto mediante l'aggiunta di G.SET.<nome componente>
Le opzioni di set ovviamente cambiano da componente a componente, infatti per esempio per il grafico non vi è nessun parametro obbligatorio, mentre per i box il parametro obbligatorio è il Layout.
Vediamo come inserire questi due componenti.

05.D.1. Esercizio 1 - Creazione di subsezione con aggiunta set
    1- Dopo aver letto il capitolo sui prototipi vediamo ora come aggiungere il settaggio dei componenti
    2- Inserire il componente "grafico" all'interno di una sezione con G.SUB.CHA
    3- Dare come titolo "Grafico a torta"
    4- Inserire un G.SET.CHA per identificare che si tratta di un grafico a torta con Typ="PIE"
    5- Inserire questa istruzione per caricare i dati nel nostro grafico.
        D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_001)
    6- Creare ora un'altra sezione sottostante a quella già inserita
    7- Inserire un componente di tipo BOX con titolo "Box"
    8- Indicare tramite il settaggio il parametro obbligatorio che è il Layout e diamogli come valore per esempio "A£_000_01"
    9- Indicare inoltre nel settaggio anche il valore "BackgroundColName" che identifica il colore che deve assumere il box che viene letto da una colonna nascosta dell'XML.
        In questo caso il valore di queso parametro diventa il nome della colonna nascosta in cui sono contenuti i valori dei colori scritti come "rgb(<RRR>,<GGG>,<BBB>)"
    10- Utilizzare questa istruzione per riempire i dati del nostro BOX
        D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_BOX) 2(;;BOX_011)


Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
  G.SEZ Pos(1)
    G.SUB.CHA Tit="Grafico a torta"
      G.SET.CHA Typ="PIE"
      D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_001)
  G.SEZ Pos(2)
      G.SUB.BOX Tit="Box"
         G.SET.BOX Layout="A£_000_01" BackgroundColName="BOX_BACKGROUND"
         D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_BOX) 2(;;BOX_011)

NB :  Non tutti i componenti grafici sono compatbili con LoocUP, alcuni sono solo visualizzabili in WebUP (come ad esempio i box)
 :  : DEC T(J1) P(FUN) D(ES_05.D.1 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_D_001))


05.D.2. Esercizio 2 - Utilizzo di altri componenti con settaggi
    1- Dopo aver letto il capitolo sui prototipi vediamo ora come aggiungere il settaggio dei componenti
    2- Inserire il componente "FLD" all'interno di una sezione con G.SUB.FLD
    3- Dare come titolo "*NONE"
    4- Inserire un G.SET.FLD per identificare che richiede come parametro obbligatorio il tipo. Diciamoc che vogliamo creare un calendario Typ="Cal"
    5- Creare ora un'altra sezione affiancata a quella già inserita
    7- Inserire un altro  componente di tipo FLD
    8- Indicare che ora vogliamo un componente di tipo Typ=""
    8- Indicare tramite il settaggio il parametro obbligatorio che è il Layout e diamogli come valore per esempio "A£_000_01"
    9- Indicare inoltre nel settaggio anche il valore "BackgroundColName" che identifica il colore che deve assumere il box che viene letto da una colonna nascosta dell'XML.
        In questo caso il valore di queso parametro diventa il nome della colonna nascosta in cui sono contenuti i valori dei colori scritti come "rgb(<RRR>,<GGG>,<BBB>)"
    10- Utilizzare questa istruzione per riempire i dati del nostro BOX
        D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_BOX) 2(;;BOX_011)

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
  G.SEZ Pos(1)
    G.SUB.CHA Tit="Grafico a torta"
      G.SET.CHA Typ="PIE"
      D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_001)
  G.SEZ Pos(2)
      G.SUB.BOX Tit="Box"
         G.SET.BOX Layout="A£_000_01" BackgroundColName="BOX_BACKGROUND"
         D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_BOX) 2(;;BOX_011)

NB :  Non tutti i componenti grafici sono compatbili con LoocUP, alcuni sono solo visualizzabili in WebUP.
 :  : DEC T(J1) P(FUN) D(ES_05.D.2 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_D_002))

05.E. Creazione di una subsezione con stili di scheda
Dopo aver visto l'utilizzo degli SCP_SET per utilizzarli come metodo per prototipizzare i dati, nei membri SCP_SET è possibile inoltre inserire altri ulteriori settaggi come per esemio l'utilizzo degli stili.
All'interno di una scheda è inoltre possibile scrivere degli stili da attribuire ad un componente ( :  : G.STY) e quindi attribuirli ad esso richiamandoli nell'SCP_SET inserendoli in una colonna nascosta avente codice Cod="STYLE". Vediamo come utilizzarla

05.E.1. Esercizio 1 - Creazione di due stili per due componenti

  1- Iniziamo con il creare due sezioni che dividano verticalmente in parti uguali lo schermo
  2- Inseriamo in ogni sezione un componente di tipo BOX
  3- In cima al documento prima della definizione delle sezioni inserire il comando per inserire uno stile di scheda con  :  : G.STY
  4- Nella definizione dello stile gli daremo un nome, il colore del font, il colore di background, la grandezza del font e l'allineamento.
      Nam="stile_1" FontColor="R100G100B100" BackColor="R20G100B200" FontSize="20" Align="right"
  5- Creiamo un secondo stile con valori diversi da quelli sopracitati, ad esempio
      Nam="stile_2" FontColor="R255G255B200" BackColor="R100G20B100" FontSize="32" Align="center"
  6- Creiamo ora un membro SCP_SET in cui inseriremo
  7- Come al solito passiamo la funzione per riempire il nostro box
      D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_BOX) 2(;;BOX_011)

Esempio : 
(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)



NB :  Non tutti i componenti grafici sono compatbili con LoocUP, alcuni sono solo visualizzabili in WebUP.
 :  : DEC T(J1) P(FUN) D(ES_05.E.1 - Risultato) K(F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCHESE;SCH_STR) 4(;;ES_E_001))

05.F. Creazione di subsezioni con dinamismi
E' possibile associare ad un componente un dinamismo che faccia far qualcosa da qualche parte.
I possibili dinamismi sono per esempio : 
    - al click;
    - al doppio click;
    - al cambio valore;
    - allo scorrimento;
    - all'aggiornamento;
    - ecc...

05.F.1. Esercizio 1 - Creazione di un dinamismo
  1- Dopo aver creato due sezioni con Pos(1) e Pos(2)
  2- Inserire un componente FLD di tipo CMB (combo)
  3- Per indicare dove andare al dinamismo diamo un "Id" alla seconda sezione valorizzandolo con "din"
  4- Indichiamo ora dopo il primo FLD il G.DIN e diciamo che al click "When="Click"" di saltare alla sezione 2 con "Where="din""
  5-









 :  : ATT Cod(002) Txt(Liste in SmeUP)  STAT(10) RESP(SCIMAM)
//-- ********************** CAPITOLO 1 **********************

01. Cosa è una lista?
In SmeUP una lista è un'insieme di oggetti che più genericamente possiamo identificare attraverso la matematica insiemistica.
Quindi la lista prende il concetto di sottoinsieme di un insieme (in questo caso di oggetti), che può essere l'insieme vuoto, l'insieme stesso o parte di esso.

Altra documentazione visionabile in "Funzioni dell'esercizio"
 :  : DEC T(J1) P(FUN) D(Documentazione Liste) K(F(EXD;*SCO;) 1(MB;DOC_OGG;OG_LI) 2(MB;SCP_SCH;OGDOCU))



02. Creazione di una lista
//-- ********************** CAPITOLO 2 **********************

Ci sono sostanzialmente tre modi per inserire una lista.
02.A. Creazione da ricerca
La prima avviene mediante la ricerca.
   1- Clicchiamo quindi sulla lente di ingrandimento (o F4)
   2- inseriamo LI -> !   così facendo potremo scegliere la classe oggetto su cui creare una lista.
   3- Una volta scelto la classe (ad esempio CNCOL) cliccare sul parametro e cliccare con il tasto destro del mouse
   4- Selezionare AGGIUNTA
   5- Verrà aperta una scheda in cui ci verrà chiesto come chiamare la lista "Descrizione" ed altri parametri per specializzare la lista. Inseriamo per esempio "Lista calcetto".
   6- Il "Tipo lista" identificherà le varie tipologie di liste, e per ora accontentiamoci di popolarla manualmente e quindi "00"
   7- Premiamo il tasto conferma in alto a sinistra.
   8- Ora sarà creata la lista chiamata "Lista calcetto"

Successivamente vedremo come popolarla

02.B. Creazione da selezione
Il secondo metodo è quello di crearla dopo aver scelto gli oggetti da inserirci

02.C. Creazione da una lista esistente
Il terzo metodo prevede di crearne una nuova da una già creata
  1-  Ricerchiamo con F4 LI -> CNCOL -> !
  2- Così facendo ci verrà restituita la lista delle liste create, scegliamone una e confermiamo
  3- Dal menu laterale cliccare GESTIONE -> AGGIUNTA
  4- Così facendo ci ritroveremo nella situazione del punto 5 qui sopra

Successivamente vedremo come popolarla

03. Operazioni sulle liste
//-- ********************** CAPITOLO 3 **********************

03.A. Aggiungere dati ad una lista
  1- Scegliamo di creare una lista di collaboratori che vogliono partecipare ad una partita di calcetto.
  2- Essendo formata da persone, ovvero da collaboratori rechiamoci sulla classe collaboratori (un metodo potrebbe essere quello tramite la ricerca F4)
  3- Ricerchiamo OG -> CN -> COL
  4- Sul menu di sinistra ricerchiamo la voce SPECIFICHE OGGETTO -> ANALISI -> ELEMENTI
  5- Dalla matrice dei collaboratori scegliere (e selezionare) quali si vogliono aggiungere alla lista appena creata, dopodichè cliccare con il tasto destro sull'intestazione della colonna e scegliere "AGGIUNGI A LISTA"
  6- Comparirà una schermata con :  sulla sinistra gli oggeti selezionati, mentre sulla destra la successione delle liste già create. Per inserire gli oggetti nella lista voluta, cliccare sulla freccia "->" accanto al nome della lista.

03.B. Ricerca delle liste
   1- Il metodo più semplice è quello tramite ricerca
   2- Basta infatti selezionare la ricerca (lente ingrandimento o F4)
   3- ricercare LI -> <classe oggetto> -> !

03.B. Visualizzare i dati inseriti in una lista
Anche qui ci sono diversi metodi

03.B.1. Accedendo alla lista
   1- Una volta all'interno della lista delle liste
   2- Cliccare sulla lista desiderata per aprirla
   3- Nel tab "Dati di dettaglio" sarà possibile vedere tutti gli oggetti inseriti

03.B.2. Accedendo alle info della lista
   1- Una volta che mi trovo nella lista delle liste create
   2- Scelgo il tab "Controllo liste"
   3- Sulla destra comparirà un'ulteriore pannello in cui è possibile scegliere il tab "Elementi"

03.C. Modificare dati in una lista
   1- Una volta che ci si trova all'interno della propria lista
   2- Cliccare sulla lista desiderata per aprirla
   3- Nel menu laterale scegliere GESTIONE -> MODIFICA
   4- Compare la scheda di modifica della lista in cui è possibile cambiare nome, tipo, visibilità, ecc
   5- Cliccando sul tab DATI DI DETTAGLIO è possibile aggiungere o rimuovere anche oggetti alla lista
