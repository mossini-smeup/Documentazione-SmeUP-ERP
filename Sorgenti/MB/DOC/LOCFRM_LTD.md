Il tool esterno preferenziale è IRFANVIEW, che, oltre a disporre di una buona gamma di opzioni di memorizzazione e ritaglio, consente di salvare l'immagine nei formati preferiti.

Se si richiedessero migliori esigenze di ritaglio dell'immagine, si può utilizzare un altro tool, reperibile allo stesso indirizzo indicato sopra 'Screen Hunter', tuttavia questo programma consente solo il salvataggio in formato jpeg, occorre quindi convertire in formato png in un passo successivo.

# Componente grafico DEV
Il componente DEV permette di importare e salvare immagini che sono temporaneamente salvate in memoria (ad esempio uno screenshot ottenuto premendo il pulsante "stamp"), o acquisite attraverso periferiche esterne (ad esempio una webcam).

![LOCFRM_023](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_023.png)
Per il componente standard è sufficiente scrivere la seguente sintassi : 
 :  : PAR T(Sintassi) F(04)
  :   : G.SUB.DEV Tit="copia/incolla"

Mentre per il componente con periferica la sintassi è la seguente : 
 :  : PAR T(Sintassi) F(04)
  :   : G.SUB.DEV Tit="webcam"
  :   : G.SET.DEV DevType="Cam"


La bottoniera del componente permette di importare l'immagine in memoria, salvare l'immagine, configurare i dati per la gestione dell'immagine. Una volta importata, l'immagine potrà essere ritagliata, ridimensionata ed elaborata creando etichette, rettangoli, offuscamenti...
Per ridimensionare l'immagine è sufficiente fare click con il mouse sull'immagine e selezionare la voce ridimensiona dal popup menù.

![LOCFRM_024](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_024.png)
Per aggiungere etichette, rettangoli... è sufficiente selezionare un'area dell'immagine tenendo premuto il pulsante del mouse.

![LOCFRM_025](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_025.png)
Al rilascio selezionare l'operazione desiderata ("disegna etichetta" o "disegna rettangolo").

![LOCFRM_026](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_026.png)
Tenendo premuto il tasto CTRL e cliccando sulla voce del popup menù desiderata è possibile modificare le impostazioni di default (quali il colore dell'oggetto disegnato, il colore di riempimento, il testo, la forma della freccia ...).

![LOCFRM_027](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_027.png)
Nel caso di dati sensibili da nascondere, è possibile offuscare tali dati disegnando un rettangolo con colore di sfondo impostato come "maschera dati".

![LOCFRM_028](http://localhost:3000/immagini/LOCFRM_LTD/LOCFRM_028.png)
Per annullare ogni operazione appena eseguita è sufficiente selezionare la voce "torna indietro" dal popup menù.

# IrfanView (versione 4.20)
IrfanView è un programma gratuito per Microsoft Windows con cui è possibile visualizzare, modificare e convertire immagini e riprodurre file audio e video. Creato per essere un visualizzatore/lettore veloce, facile da usare e in grado di maneggiare molti formati di file diversi, dalla versione 4.10 ha implementato alcuni semplici strumenti di modifica.

L'installazione del software è **opzionale**, ma risulta uno strumento molto utile, soprattutto per la generazione e gestione di screenshot finalizzati alla documentazione.

## Installazione IrfanView
E' possibile installare IfranView seguendo il percorso : 
http://www.irfanview.com/download_sites.htm
Successivamente è possibile ottenere la versione italiana del programma scaricando ed installando l'installer all'indirizzo
http://www.irfanview.com/languages.htm
A questo punto, avviando il programma, sarà possibile selezionare la lingua desiderata andando sulla voce di menù options -> change language...

## Generazione degli screenshot
Avviare IrfanView e premere il tasto "C" per impostare le proprietà di cattura dello schermo come mostrato in figura ImgRef(IRF1) (oppure selezionare la voce di menù  Opzioni -> Cattura schermo).

![IRFVIEW_01](http://localhost:3000/immagini/LOCFRM_LTD/IRFVIEW_01.png)
Impostare i seguenti parametri : 

- area da catturare :  finestra in primo piano
- salva l'immagine catturata come file
- cartella di destinazione :  Percorso_Cartella\Nome_Cartella, dove Percorso_Cartella e Nome_Cartella sono il percorso e la cartella temporanea dove andranno salvate tutte le immagini (ad esempio è possibile usare una cartella temporanea sul proprio Desktop)
- salva come :  PNG - portable network graphics

Premere _2_"Avvia".

Scegliere la finestra da salvare e premere CTRL+F11 per generare lo screenshot direttamente nella cartella di lavoro specificata al passo precedente.

## Modifica degli screenshot
Aprire l'immagine da modificare con IfranView e aprire il pannello strumenti di disegno selezionando la voce di menù modifica -> pannello strumenti di disegno.
Se necessario selezionare la porzione di immagine che deve essere ritagliata, nel seguente modo : 

- selezionare dal pannello il puntatore (figura ImgRef(IRF2) n.1)
- selezionare il riquadro da ritagliare
- fare click con il tasto destro del mouse
- premere CTRL+Y per ritagliare la selezione (o selezionare la voce di menù modifica -> ritaglia la selezione)

A questo punto è possibile ridimensionare la pagina selezionando la voce di menù immagine -> aggiungi cornice

Infine si può elaborare l'immagine aggiungendo testo, frecce (figura ImgRef(IRF2) n.2) o altri oggetti grafici (es. ellissi, rettangoli ...) (figura ImgRef(IRF2) n.3)

_2_Nota :  è buona norma eliminare i dati sensibili dell'immagine (come ad esempio nome utente o informazioni riservate) coprendoli con rettangoli colorati

![IRFVIEW_02](http://localhost:3000/immagini/LOCFRM_LTD/IRFVIEW_02.png)
E' possibile unire più immagini nel seguente modo (figura ImgRef(IRF3)) : 

- selezionare la voce di menù immagine -> crea un'immagine panoramica...
- premere sul pulsante "aggiungi immagini"
- infine premere sul pulsante "crea immagine"

![IRFVIEW_03](http://localhost:3000/immagini/LOCFRM_LTD/IRFVIEW_03.png)
Per spostare un'immagine o una porzione di immagine è sufficiente : 

- selezionare l'immagine con lo strumento puntatore
- copiare l'immagine negli appunti premendo CTRL+C
- selezionare l'area di destinazione con lo strumento puntatore
- incollare l'immagine premendo CTRL+V
_2_Nota :  poichè l'immagine verrà incollata nell'area di destinazione con le dimensioni riadattate, per mantenere le proporzioni è buona norma utilizzare la stessa area di selezione usata per copiare l'immagine spostandola semplicemente nella posizione di destinazione desiderata premendo il tasto destro del mouse (figura ImgRef(IRF4)).

![IRFVIEW_04](http://localhost:3000/immagini/LOCFRM_LTD/IRFVIEW_04.png)ImgRef(IRF4)

# Dove si salvano le immagini e come si denominano
Le immagini devono essere salvate in formato png, che, oltre ad essere leggero rispetto ad altri, mantiene nitide le immagini nei ridimensionamenti.

Per convenzione le immagini devono essere salvate nella cartella in cui la parte finale del percorso è _2_\TAB£A\aa\mmmmmm\, dove aa è l'applicazione e mmmmmm è il modulo a cui appartiene il primo documento che richiama l'immagine stessa :  esempio se devo salvare un'immagine richiamata in un documento che spiega la gestione dell'anagrafico articoli il percorso sarà _2_\TAB£A\BR\BRARTI.

La parte iniziale del percorso deve essere quella risolta dalla variabile _3_|SME.IMG|, codificata nel file di impostazione di Loocup e precisamente in _2_SCP_CLO\Default, (a meno di percorsi personalizzati per l'utente o l'azienda).
All'interno della cartella le immagini possono assumere una numerazione progressiva :  es. ARTI_01.png, ARTI_02.png, ARTI_03.png, ARTI_04.png, .....

# Schemi
Per gli schemi, invece, si riserva un formalismo particolare :  ognuno deve essere prodotto attraverso un file visio, i sorgenti visio devono essere inseriti nella cartella SRC_VISIO, messa nella stessa locazione degli schemi.

# Convenzioni di inclusione delle immagini
Nella inclusione delle immagini si deve tener conto di come saranno visualizzate nei book in formato pdf che saranno creati, l'obiettivo è di non saturare la pagina ma al contempo di mantenere una certa leggibilità.

Come regola generale : 
 * le immagini delle schermate intere  dovranno essere impostate per uscire con una larghezza pari al 60% della larghezza pagina :  R (60) e centrate :  A(C) (es. :  IMG P(...\TAB£A\C£\C£PARA\C£_05_02.png) R(60) A(C))
 * le immagini di schemi e grafici dovranno essere impostate per uscire con una larghezza pari al 60% della larghezza pagina :  R (60)
 * le immagini di parti di schermate intere  dovranno essere impostate per uscire con una larghezza minore - fare attenzione ad immagini molto piccole (es. bottoni) perchè al di sotto di un minimo il sistema non opera più nessuna riduzione
