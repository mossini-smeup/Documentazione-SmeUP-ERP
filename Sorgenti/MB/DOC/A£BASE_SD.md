# Comandi
I comandi Sme.up sono presenti nel file opzioni **QAUOOPT** della SMEDEV, impostabili premendo F18 dal PDM e mettendo SMEDEV come libreria del File opzioni.

## CO - Compilazione
La compilazione di tutti i programmi deve avvenire con l'opzione **CO** da PDM, in modo da ottenere un oggetto che opera in ambiente 5250 e in ambiente grafico.
Per i programmi non contenenti un video (senza una specifica 'F' WORKSTN), il comportamento di questo comando è simile all'opzione 14.

Per i programmi contenenti un video, viene creato un _membro sorgente intermedio_ (a cui sono aggiunte dal precompilatore le specifiche necessarie alle traduzioni e all'emulazione in Looc.up) nel file sorgente **£UI_SRC** nella stessa libreria in cui risiederà l'oggetto. Il membro sorgente intermedio viene effettivamente compilato e sarà necessario per poter eseguire il DEBUG dei programmi con video.

Se il file £UI_SRC non esiste, esso viene creato automaticamente e nello standard è disponibile nelle librerie SMEUP_OBJ e SMEUP_DEV.

Presso il cliente, la compilazione con 'CO' dei programmi personalizzati e specifici, necessaria per il loro funzionamento in ambiente grafico, avrà come effetto che anche nella libreria di personalizzazione risiederà il file sorgente £UI_SRC.

Il comando 'CO' si occupa anche di eseguire le repliche dei file :  i file da replicare e i nomi delle repliche vanno aggiunti e gestiti in SMEDEV/SMESRC/B£PD01.

## Specifiche aggiunte dal precompilatore
Si elencano di seguito i tipi di specifiche aggiunte automaticamente dal precompilatore nel sorgente intermedio : 

| LI>* | Specifiche per le lingue. Se nella B£2$DS (definita nella /copy £TABB£1DS) non c'è ITA ---|
| viene chiamato un programma che traduce le costanti. |
| LO>* | Specifiche per Looc.Up. Fanno sì che il video venga emesso solo se non si sta eseguendo un lavoro di Looc.Up. Il compilatore necessita del video nello stesso file dei sorgenti. |
| 


**Esempio di specifiche LI>***
>.   RD* ROUTINE INIZIALE
.     *--------------------------------------------------------------*                     .
.    C     £INIZI        BEGSR
.LI> * Inizializzazione schiere interne in lingua
.LI>C     ££B£2I        IFNE      *BLANK
.LI>C                   EXSR      £INIZL
.LI>C                   ENDIF
.    *
.                           ...
.    *
.   C                   ENDSR
.LI> *---------------------------------------------------------------*                    .
.LI> * Inizializzazione schiere interne in lingua
.LI> *---------------------------------------------------------------*                    .
.LI>C     £INIZL        BEGSR
.LI>C     £INIZL        BEGSR
.LI> *
.LI>C                   MOVEL(P)  'TXT         '£LINNC                                      .
.LI>C                   MOVEL(P)  'TXT         '£LINTC                                      .
.LI>C                   CLEAR                   £LINSC                                           .
.LI>C                   MOVEL     TXT           £LINSC                                       .
.LI>C                   EXSR      £LIN
.LI>C                   MOVEL     £LINSC        TXT                                          .
.LI> *
.LI>C                   ENDSR
.LI>C/COPY QILEGEN,£LIN
.LI> *--------------------------------------------------------------*


**Esempio di specifiche LO>***
>.    * Emissione formato video
.LO>C                   IF        £INZJT<>'L'
.   C                   EXFMT     FMT1
.LO>C                   ELSE
.LO>C                   EVAL      £UIAKS = '
.LO>C                   MOVEL(P)  'FMT1'        £UIAID                           .
.LO>C                   MOVEL(P)  'R'           £UIATF                              .
.LO>C                   MOVEL     £RASDI        £RASDI00
.LO>C                   MOVEL     W$FUNZ        W$FUNZ00
.LO>C                   MOVEL     W$METO        W$METO00
.LO>C                   MOVEL     W$AZIE        W$AZIE00
.LO>C                   MOVEL     W$TREG        W$TREG00
.LO>C                   MOVEL     W$PROG        W$PROG00
.LO>C                   MOVEL     W$NUES        W$NUES00
.LO>C                   MOVEL(P)  £UFMT1        £UIAD1
.LO>C                   MOVEL(P)  'EXFMT'       £UIAOP                    .
.LO>C                   EXSR      £UIA
.LO>C                   MOVEL(P)  £UIAD1        £UFMT1
.LO>C                   MOVEL     £RASDI00      £RASDI                   .
.LO>C                   MOVEL     W$FUNZ00      W$FUNZ               .
.LO>C                   MOVEL     W$METO00      W$METO             .
.LO>C                   MOVEL     W$AZIE00      W$AZIE                 .
.LO>C                   MOVEL     W$TREG00      W$TREG              .
.LO>C                   MOVEL     W$PROG00      W$PROG             .
.LO>C                   MOVEL     W$NUES00      W$NUES              .
.LO>C                   ENDIF

In presenza di un'istruzione di emissione del video, viene aggiunto un 'IF' che si occupa di testare il nome del lavoro corrente e, se si tratta di un lavoro Looc.up (iniziale "L"), esegue delle istruzioni che corrispondono in grafica all'emissione del video.

## DO
L'opzione DO da PDM esegue la scansione di un sorgente aggiungendo dei tag che identificano il livello di indentazione.
Nell'esempio si può vedere un ciclo Do, contenente una struttura 'IF' e una 'SELECT'.
Il ciclo Do rappresenta il primo livello, identificato dai tag 1 e 1e in apertura e chiusura.
La 'IF' rappresenta il secondo livello di indentazione con tag 2 e 2e in apertura e chiusura.
La 'SELECT' è allo stesso livello di 'IF' e presenta tag 2 , 2x e 2e rispettivamente sulle istruzioni 'SELECT', 'WHEN' ed 'ENDSL'.

>.1    C                   DO        1000          $X                5 0                 .
.     C     KTIAR         READE     BRARTI2L                               50           .
.     C   50              LEAVE                                                         .
.      *                                                                                .
.2    C                   IF        %SUBST(A§DEAR : 1 : 1)<>'D' AND                         .
.     C                             %SUBST(A§DEAR : 1 : 1)<>'T'                             .
.     C                   ITER                                                          .
.2e   C                   ENDIF                                                         .
.      *                                                                                .
.2    C                   SELECT                                                        .
.2x   C                   WHEN      %SUBST(A§DEAR : 1 : 1)='D'                              .
.     C                   EVAL      A§DEAR=%REPLACE('T' : A§DEAR : 1 : 1)                     .
.     C                   UPDATE    BRARTIR                                             .
.2x   C                   WHEN      %SUBST(A§DEAR : 1 : 1)='T'                              .
.     C                   EVAL      A§DEAR=%REPLACE('D' : A§DEAR : 1 : 1)                     .
.     C                   UPDATE    BRARTIR                                             .
.2e   C                   ENDSL                                                         .
.      *
.     C                   CLEAR                   S§STRI                             .
.     C                   EVAL      S§ARTI=A§ARTI                                .
.     C                   EVAL      S§TIAR=A§TIAR                                .
.     C                   EVAL      S§DEAR=A§DEAR                          .
.     C                   EVAL      S§DEA2=A§DEA2                           .
.     C                   EVAL      STR198=S§STRI                            .
.     C                   EXSR      PRTSR                                           .
.1e   C                   ENDDO                                                     .


## AT
L'opzione AT da PDM mostra lo stato delle traduzioni delle schiere contenute nel programma.

## Blocco di un membro della SMEDEV
**Nota**
Questa parte è da considerare deprecata sui sistemi di sviluppo a fronte del passaggio alla gestione tramite branch.

I comandi di blocco vengono utilizzati per segnalare che un sorgente è in modifica da un determinato utente. _Non eseguono automaticamente la copia del sorgente in SMEUP_TST / P_ / W_ , né impediscono che un altro utente possa eseguire delle modifiche.  Ciò dipende dal buon comportamento dello sviluppatore.

### BT - Blocco in SMEUP_TST
Per "bloccare" un membro della SMEDEV, mettere l'opzione **BT** sul membro, nel caso si entri in modifica del sorgente nella SMEUP_TST.

### BP - Blocco in libreria di progetto
Per "bloccare" un membro della SMEDEV, mettere l'opzione **BP** sul membro, nel caso si prenda in modifica il sorgente in una libreria di progetto.

### BL - Blocco in libreria utente (W)
Per "bloccare" un membro della SMEDEV, selezionare l'opzione **BL** sul membro, modificando il sorgente nella nella propria W.

## SB - Sblocco
Per "sbloccare" un membro utilizzare l'opzione **SB** sul membro stesso.

## IS - Conevrsione da RPG A RPGLE
### Prerequisiti
Il file source deve avere lunghezza 112 al posto dei consueti 92, pena il troncamento dei commenti a destra. Pertanto, creando un file source tramite CRTSRCPF, conviene impostare la lunghezza record a 112.

### Come convertire i programmi
Per convertire un programma da RPG a ILE è stato creato il programma B£UT24, richiamabile automaticamente con opzione **IS** dal PDM.
Lo stesso programma permette anche di creare un programma adatto per Looc.up.

# Modello dinamico
- [Obiettivo](Sorgenti/MB/DOC/C£MODI_A)
- [Definizioni](Sorgenti/MB/DOC/C£MODI_B)
- [Costruzione Modello](Sorgenti/MB/DOC/C£MODI_C)
- [Lettura Modello](Sorgenti/MB/DOC/C£MODI_D)
- [Scenari](Sorgenti/MB/DOC/C£MODI_E)

# Debug
Per effettuare il debug di un programma bisogna utilizzare il debug attivabile da linea comando con STRDBG o da opzioni di riga con **SD**.
Non essendo presentata alcuna linea di comando da cui richiamare il programma interessato, per prima cosa bisogna mettere un breakpoint (F6) all'interno del codice e premere F12, per poi digitare ENDDBG da linea comando o da opzioni di riga **ED**.

>N.B. : 
 * Effettuando richiesta di sistema (F4), opzione 3 e digitando DSPMODSRC, viene mostrato il codice del programma in debug, per reimpostare nuovi breakpoint nel caso in cui, per esempio, sia stato premuto un F12 di troppo;
 * eseguendo le operazioni passo-passo (tramite F10) e incontrando una /COPY, il debug perde il puntatore ed è necessario premere molte volte F10, fino a quando il flusso non ritorna alla specifica successiva alla chiamata. Il consiglio è di porre un breakpoint sulla specifica seguente la chiamata alla /COPY e di fare eseguire il codice (F12);
 * per aggiungere programmi alla lista dei programmi da debuggare, premere F14 e usare l'opzione 1, seguita dall'opzione 5 per impostare un breakpoint (dato che il controllo non viene passato al programma chiamato);
 * per **vedere il contenuto di una variabile**, oltre al tasto _F11**, è possibile utilizzare il comando EVAL, anche attraverso le funzioni %SUBST e %INDEX. Per esempio, EVAL %SUBSTR(VAR 1 2) mostra i primi 2 caratteri della variabile VAR;
 * la **ricerca** di testo, attuabile tramite il tasto funzionale F16, una volta arrivati in fondo non riparte dall'inizio del codice sorgente. E' quindi consigliabile posizionarsi sempre all'inizio col comando T;
 * con il comando di _WATCH_ su di una variabile, si viene informati su quando essa cambi (è come impostare un breakpoint condizionato);
 * per cambiare il valore di una variabile, è necessario digitare un _EVAL_ (es. :  EVAL <variabile>='PIPPO').

Per effettuare il debug di un programma già attivo nella lista lavori (cosa che prima si effettuava mettendo *SELECT nell'opzione SRVJOB) occorre digitare STRSRVJOB da linea di comando, indicando gli attributi del lavoro da debuggare e avviare il debug normalmente. Terminato il debug con ENDDBG, digitare ENDSRVJOB.

# Looc.Up lato client
- [Controllo prerequisiti Looc.Up](Sorgenti/MB/DOC/LOBASE_03)

# Analisi di un file di dati (F)
Il comando F, richiamabile dalla riga di comando sia da emulatore 5250 che da Looc.up, permette di visualizzare le caratteristiche di un file di dati.
L'operazione può essere eseguita sia su un file fisico che su un file logico.

Eseguendo il comando : 
>F BRENTI0F

si ottiene la visualizzazione di una schermata in cui viene rappresentata la DDS del file e da cui è possibile, attraverso specifiche opzioni e tasti funzione, interrogare le caratteristiche dei diversi campi (opzioni di riga), vedere i file logici associati (F15), le chiavi (F14), entrare in editazione del sorgente del file (F16) o del sorgente del dizionario (F17), aprire il tool QUERY (F20) di sistema di AS/440 ecc.

![A£BASE_016](http://localhost:3000/immagini/A£BASE_SD/AXBASE_016.png)
## Ricerca stringa (UP SCA)
Il comando UP SCA, richiamabile dalla riga di comando sia da emulatore 5250 che da Looc.up, permette di eseguire la ricerca di una o più stringhe di testo.

![A£BASE_017](http://localhost:3000/immagini/A£BASE_SD/AXBASE_017.png)
La ricerca può avvenire in uno o più (fino a 35) file sorgenti (identificati dalla coppia Libreria / File), filtrando eventualmente il tipo Membro.

Altre opzioni : 

| **Ricerca** | _Stringhe** :  cerca in tutto il membro; _Modifiche** :  cerca nelle modifiche ---|
| V* che indicano le modifiche apportate a un sorgente. |
| **A/O/M** | _A** :  esegue la ricerca delle stringhe in AND sulla medesima riga del sorgente. _O_ :  esegue la ricerca delle stringhe in OR. _M_ :  esegue la ricerca delle stringhe in AND all'interno di tutto il membro. |
| **PosI / PosF** | Esegue la ricerca della stringa in una parte della riga compresa tra la posizione iniziale (PosI) e la posizione finale (PosF) specificate. |
| **Case Sensitive** | Esegue la ricerca delle stringhe distinguendo maiuscole e minuscole. |
| **Tipo Stampa** | Specifica se nella stampa dei risultati riportare solo i nomi dei membri nei quali la stringa è stata trovata o anche il dettaglio delle singole righe contenenti la stringa. |
| **Intes.Salto.P** | Indica se, nella stampa dei risultati, l'intestazione deve essere ripetuta al cambio di pagina. |
| **Scans.Commenti** | Indica se la ricerca della stringa deve considerare anche le righe di commento nei sorgenti. |
| 


I risultati della ricerca vengono salvati in un file di stampa (Prt198 con Dati specificati dall'utente dal programma B£UT09), visualizzabile da 5250 e da Looc.up, accedendo al proprio spool di stampa utente.

![A£BASE_018](http://localhost:3000/immagini/A£BASE_SD/AXBASE_018.png)**Spool di stampa utente**

![A£BASE_019](http://localhost:3000/immagini/A£BASE_SD/AXBASE_019.png)**Visualizzazione stampa dei risultati della ricerca**
