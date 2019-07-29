# I Programmi Servizio di Loocup
Un servizio è un programma AS400 che : 

- riceve in ingresso una serie di input secondo una modalità standard (analogamente ai programmi "funizzati" su AS)
- effettua delle elaborazioni dei dati su AS
- invia alle code di LOOC.up dell'XML che i componenti grafici interpreteranno e visualizzeranno.


## Entry di un servizio
L'entry di un servizio per LOOC.up assomiglia a quella che caratterizza i programmi funizzati.

I campi più importanti utilizzati sono : 

## FUNZIONE DA SVOLGERE :  F()
Una chiamata standard a un servizio parte con F(A;B;C), dove
 A -> £UIBPG
 B -> £UIBFU (OBBLIGATORIO)
 C -> £UIBME


- **£UIBPG** :  _Componente**. Indica al servizio quale è il componente di destinazione che interpreterà l'XML restituito. In questo modo il servizio sa, ad esempio, che l'XML di una lista di oggetti va restituita secondo la sintassi di un albero piuttosto che di una matrice.
- **£UIBFU** :  _Servizio**. Secondo le vecchie modalità in questo campo si indicava un elemento di TAJAT che indicava il servizio da restituire, come ad esempio *DO, *DR... Un servizio JATRE* poteva basarsi su questa informazione per decidere quale funzione eseguire e quali dati restituire. Ora questo campo contiene il nome del programma che restituisce il servizio. La funzione vera e propria viene indicata in £UIBME.
- **£UIBME** :  _Funzione.metodo**. Indica al servizio la funzione da eseguire, opzionalmente seguita da un metodo separato da un punto.


## OGGETTI
Nella chiamata :  1(T1;P1;K1) ... 6(T6;P6;K6), dove

- T1 -> £UIBT1, P1 -> £UIBP1, K1 -> £UIBK1
- ...
- T6 -> £UIBT6, P6 -> £UIBP6, K6 -> £UIBK6

L'interpretazione dei 6 oggetti è, come sempre, a carico del programma.

## ALTRI PARAMETRI
Nella chiamata :  P() dove

- PA -> £UIBPA

£UIBPA è un campo di 256 da gestire liberamente. Può essere utilizzato per passare diversi oggetti, secondo due modalità :  **posizionale** e **a tag**.

Nella chiamata :  INPUT() dove

- PA -> £UIBD1

£UIBD1 è un campo di lunghezza 30000 da gestire liberamente.
Può essere utilizzato per passare diversi oggetti, secondo due modalità :  **posizionale** e **a tag**.

## Documentazione dei servizi
Ogni programma che implementa un servizio può fornire tramite una schiera una tabella di regole per rendere possibili il controllo e l'immissione guidata della chiamata alle sue funzioni.

Questa schiera può essere definita nella documentazione attiva del programma, in DOC_SER, membro nome programma ad es : 
 :  : DEC T(MB) P(DOC_SER) K(JATRE_29C) L(1)
racchiusa tra le specifiche ..I.RUL e ..I.RUL.END oppure restituita dal programma in risposta a una chiamata con funzione '*JASEP2' (vecchia modalità, sconsigliata)

## STRUTTURA
Una tabella delle regole si compone di 4 sezioni : 

- _7_FUNZIONI/METODI : Definisce le funzioni/metodi gestite dal servizio
- _7_PARAMETRI : Definisce i parametri gestiti, inizia con la keyword ..PAR
- _7_COMPONENTI : Definisce i componenti gestiti, inizia con la keyword ..COM
- _7_OGGETTI : Definisce gli oggetti gestiti :  inizia con la keyword ..OGG


## DEFINIZIONE FUNZIONI E METODI
In questa prima sezione vengono elencate le funzioni/metodi supportati dal servizio.
Ad ogni funzione/metodo possono essere associate delle regole per la costruzione e il controllo del servizio, specificate in seguito.
Le regole possono essere associate alle funzioni in maniera ereditaria :  si può specificare regole generali (valide per tutte le funzioni/metodi), per le funzioni (valide per tutti i metodi della funzione), per i metodi.
Nel caso di regole definite su più livelli le più specifiche hanno la priorità (metodo/funzione/ generali).
La prima riga della sezione specifica le regole generali e dichiara la completezza della tabella delle regole mediante una delle due keywords : 

- ***ALL** :  sono definiti in tabella tutte le funzioni e metodi supportati dal servizio
- ***FREE** :  sono definiti solo alcune funzioni/metodo. Le funzioni/metodo definiti vengono controllati secondo le regole indicate, gli altri sono lasciati liberi.

La righe successive associano dei nomi di regole alle funzioni oppure alle funzioni/metodo.
I metodi si differenziano dalle funzioni mediante un punto in prima posizione.

## PARAMETRI
Questa sezione definisce i parametri che vengono passati tramite il campo £UIBPA al programma che implementa il servizio.
Sono possibili due modalità di passaggio parametri al servizio (mutuamente esclusive) : 
 * **Forma posizionale** :  viene presentata una G30 per i parametri, il risultato va a formare una stringa in cui ad ogni parametro corrisponde una posizione. Esempio : 
 ** Codice articolo (15) = A01
 ** Tipo documento  (3)  = OVE
 ** -> P(A01            OVE)
 * **Forma a tag** :        viene presentata una G11 per i parametri, il risultato va a formare una stringa in cui ogni parametro è associato a un tag che lo racchiude, in questo caso la posizione è ininfluente. Esempio : 
 ** Codice articolo (ART) = A01
 ** Tipo documento  (TDO)  = OVE
 ** -> P(ART(A01)  TDO(OVE))

Struttura della sezione : 

- Definizione dei parametri
- Definizione dei valori particolari (come £11V), opzionale, separata dalla sezione precedente da una riga vuota con '+' in prima posizione


Struttura delle righe della definizione dei parametri : 

- Nome della regola
- Definizione di un parametro (stessa struttura delle righe della £30A della £G30)
- Eventuale tag da associare al parametro per la forma a tag

**NB : ** per definire un gruppo di parametri secondo la modalità a TAG è necessario associare al primo parametro di una regola un tag. Tutti gli altri parametri della stessa regola verranno associati al tag Pnn, dove nn è il numero del parametro nel gruppo. Se non viene definito un tag per il primo parametro viene adottata la modalità posizionale.

## COMPONENTI
Questa sezione definisce quali componenti grafici di LOOC.up sono supportati dal servizio. Se a una determinata funzione/metodo di un servizio non sono associati dei componenti viene accettato qualsiasi componente.

Struttura delle righe di questa sezione : 

- Nome della regola
- Fino a 7 componenti grafici supportati.


## OGGETTI
Questa sezione definisce quali oggetti possono/devono essere passati nei 6 campi oggetto. Se per una funzione/metodo non sono date regole di oggetti vengono effettuati solo i normali controlli tramite la £DEC, per il resto il passaggio di oggetti è libero.

Se ad una funzione/metodo viene associata una regola di oggetti (es. OG10), questa si compone di al più una riga per ognuno dei 6 oggetti passabili.
Gli oggetti non specificati non possono essere immessi, quindi scompaiono i campi a video.
Gli oggetti specificati, invece, vengono controllati per : 
_7_Obbligatorietà :  alla riga dell'oggetto viene associato un carattere : 

- **'O'** :  obbligatorio
- **'F'** :  facoltativo
- **' '** :  non va immesso

_7_Tipizzazione : si possono specificare fino a 5 TipoParametro consentiti per l'oggetto. Il valore immesso deve essere compreso tra questi (e la ricerca suggerisce questi valori), a meno cheil primo oggetto non sia '**' (in tal caso vale qualunque tipo/parametro, la ricerca opera in *CNTT).

Struttura delle righe di questa sezione : 

- Nome della regola
- Numero oggetto (1-6)
- Carattere obbligatorietà Tipo
- Carattere obbligatorietà Parametro
- Carattere obbligatorietà Codice
- Fino a 5 TipoParametro


## ALCUNI ESEMPI
**Parametri**
>..PAR                              TpParametro         Lung.DOVAuD         Tag
PA10 Gruppo fonti ADF              MDC5C6F0G           00010 O
PA10 Gruppo fonti DIS              MDM5FO01G           00010 O

due parametri nella forma posizionale :  P(FAT       BIL       )
>PA20 Tp doc                        TAV5D               00003 O             TDO
PA20 Cod mag                       MG                  00003 O             CMA

due parametri nella forma a tag :  P(TDO(AGE) TOG(£AO))
>PA30 Valore                        V 001002            00003 O
PA30 Val1                          Valore 1
PA30 Val2                          Valore 2

Parametro con valori indicati in £11V
**NB** :  le righe della £11V (001002) sono relative solo alla £11V caricata con la regola associata alla funzione/metodo selezionata. Quindi in : 
>PA10 Parametro 1                   V 001002            00005 O
PA20 Parametro 2                   V 001002            00005 O
PA10 Val1                          Valore 1
PA10 Val2                          Valore 2
PA20 Val3                          Valore 3
PA20 Val4                          Valore 4

Parametro 2 sarà valorizzabile con Val3 o Val4.

**Oggetti**
>..OGG      TpPa1       TpPa2       TpPa3       TpPa4       TpPa5
TP10       1           OFF         TAAGE

per l'oggetto 1 valgono sia il tipo TA che TAAGE, perchè il parametro è facoltativo

## Set'Play dei servizi
### Obiettivi
Facilitare la costruzione delle chiamate ai servizi, rendendo disponibile la documentazione attiva ad essi collegata. Aiutare lo sviluppo dei servizi, in due modi : 

- facendo vedere l'output in XML di una chiamata a un servizio senza dover passare per LOOC.up
- effettuando chiamate ai servizi in interattivo per facilitarne il debug


### Come si richiama il programma
Da linea di comando :  **UP SER**

### Costruzione di una chiamata
Si compilano i campi Servizio, Funzione.Metodo, Componente, gli Oggetti, il Parametro ed eventualmente il Modo grafico.
I dati immessi in questi campi sono controllati mediante le regole per la costruzione del servizio eventualmente immesse nella documentazione attiva del servizio.
In Risultato viene riportata la stringa della chiamata da passare a LOOC.up.

È possibile anche effettuare il percorso inverso, ovvero immettere una stringa di chiamata da riportare nei vari campi :  in questo caso si inserisce la stringa e, PRIMA DI PREMERE INVIO, si preme F21.

### Simulazione dei servizi
Una volta inserita una chiamata, premendo F20 si può passare alla simulazione della stessa.
Viene chiesto l'ambiente in cui eseguire la simulazione, dopo di che si hanno due opzioni : 
**JS** - Esecuzione batch del servizio - con visualizzazione a video dell'XML prodotto
**JD** - Esecuzione interattiva del servizio - per effettuarne il debug.

### HELP
Da Jasep2 si può accedere a varie informazioni : 
**F05**- Nome dei campi £UIBxx in cui vengono passati i dati della chiamata al servizio.
**F17**- Documentazione attiva specifica del servizio.
**F18**- Documentazione attiva relativa alle regole per la costruzione di un servizio.
**F19**- Tabella delle regole per la costruzione del servizio caricata.

## Programma prototipo
Il programma LOSER_ES è il prototipo del servizio. Tale programma costruisce un albero e una matrice di esempio. Nella documentazione attiva ad esso associata è presente la tabella delle regole che rendono espliciti funzione, metodi, parametri, componenti grafici ammessi ecc.
 :  : DEC T(MB) P(JASRC) K(LOSER_ES) I(_7_Apertura del prototipo           >>)

## Considerazioni particolari di programmazione
### Log di controllo
E' attivo se la tabella PGM del programma lo prevede
In tal caso vengono stampate le stringhe aggiunte al buffer e poi inviate su coda

## Richiamo delle routine
### COPY necessarie
 * £INIZH
 * £JAX_D
 * £TABJATDS
 * £PDS
 * £INZSR
 * £RITES
 * £DEC
 * £JAX_C
 * £JAX_O

### Inizializzazione
(All'interno di £INZSR)

 * _2_£JAX_INZP. ENTRY Standard se proveniente da JAJAS1 di LOOC.up. Separata perchè può essere facoltativa (metto io l'entry)
 * _2_£JAX_INZ. Pulisce variabili e se LOG attivo apre file di stampa

### Impostazioni iniziali
(Nella routine iniziale eseguita ad ogni richiamo)

 * _2_£JAX_IMP0.

### Corpo
_7_Lista dei costrutti base predefiniti in COPY £JAX_C0 
 * _2_£JAX_ADD. Aggiunge la variabile £JAXCP in coda al buffer. Se supera limite forza un scrittura con condizione "CONTINUA"
 * _2_£JAX_SND. Invio
 * _2_£JAX_RCV. Ricevo da coda

_7_Lista dei costrutti predefiniti in COPY £JAX_C1 
 * _2_£JAX_ADDO. Aggiunta oggetto
 * _2_£JAX_AGRI. Aggiunta griglia
 ** Riceve una schiera £JAXSWK (Tipo £G30E)
 ** Inizia la griglia
 ** Ripete n colonne
 ** Chiude la griglia
 * _2_£JAX_ACOL. Aggiunta colonna
 * _2_£JAX_ARIG. Aggiunta riga
 * _2_£JAX_AMSG. Aggiunta messaggio

_7_Lista dei costrutti predefiniti in COPY £JAX_C2 
 * _2_£JAX_ATAB_I. Inizializza Caricamento Tabelle
 * _2_£JAX_ATAB. Aggiunta Oggetto a Tabelle
 * _2_£JAX_ATAB_F. Finalizzazzione Tabelle

### Chiusura
- Nella routine precedente al RETURN o LR
 * _2_£JAX_FIN0. Forza l'invio su coda con condizione "FINE"

## Debug di un servizio (SL / RL)
### Introduzione
Nel seguente documento verranno indicate brevemente alcune informazioni su come seguire il debug di un servizio chiamato da Looc.Up.

## Brevemente
Il debug di un **servizio** Sme.Up invocato da Looc.Up è una delle operazioni più frequenti durante lo sviluppo applicativo. E'  possibile avviare una sessione di debug prima individuando il lavoro e il servizio/programma su cui voglio mandare in esecuzione il debug e successivamente eseguendo il comando **SL** per far partire la sessione di debug e infine **RL** per chiuderla.

## Sezioni
### 1 - Getting started - Avvio debug
Per eseguire il debug di un servizio o più in generale di una sessione di lavoro di Loocup tramite il debugger presente sul server solitamente si usa il comando **SL** (avvia debug)  dalla videata di emulazione AS400.
 T(A questo punto è possibile distinguere due casistiche : )
- l'utente connesso ha avviato più sessioni di Loocup o una sessione di Looc.Up e almeno una sessione di emulazione di terminale 5250
- l'utente connesso ha eseguito solo una sessione di Looc.Up e nessuna sessione di emulazione di terminale 5250

Nel primo caso viene mostrato un elenco dei lavori aperti per l'utente connesso.
 T(Normalmente le sessioni di lavoro vengono identificate con 2 tipologie diverse : )
- **LO_EHHMMSS**  per le sessioni connesse alle schede di Looc.Up (E = extended)
- **LO_SHHMMSS**  per le sessioni connesse alle sessioni di emulazione 5250 (S  = Standard)


![LOCBAS_025](http://localhost:3000/immagini/LOBASE_02B/LOCBAS_025.png)
Il codice **HHMMSS** rappresenta la data di creazione del lavoro secondo il formato ore-minuti-secondi.
Le sessioni di lavoro del tipo **LO_EHHMMSS** sono rintracciabili grazie al codice presente nella **barra del titolo** della finestra Windows che contiene la sessione di Looc.Up.

![LOCBAS_023](http://localhost:3000/immagini/LOBASE_02B/LOCBAS_023.png)
Per identificare invece una sessione di emulazione (**LO_SHHMMSS**) è sufficiente tenere traccia del momento in cui viene avviata la finestra di emulazione e associarlo al codice HHMMSS.

Una volta individuato il lavoro è possibile avviare il debug con l'opzione **SJ** (Avvio diagnosi + avvio debug). Sia che io abbia aperte più sessioni (caso 2) sia che  abbia aperta una sola sessione(caso2) il sistema dopo aver invocato il comando SJ mi chiede di indicare quale **programma/servizio** voglio analizzare con il debug. Nel nostro caso è sufficiente individuare il **nome del servizio** (per esempio inseriamo il nome del servizio **A5SER_01**). Da questo momento possiamo interagire con le funzioni del debugger.

![LOCBAS_022](http://localhost:3000/immagini/LOBASE_02B/LOCBAS_022.png)
### 2 - Executing Debugger - Operazioni con il debugger
Una volta inserito il nome del servizio a cui collegare il debug, la prima operazione da fare e decidere quali **breakpoint** inserire tramite il comando **F6**. Una volta inseriti i possibili punti in cui voglio analizzare il programma **attivo il debug** con il comando **F12**.
A questo punto posso far **partire la mia richiesta** dall'interfaccia di Loocup identificando il tab che contiene la mia chiamata al servizio.

Una volta che è stato invocato il servizio la finesta di Loocup rimane in attesa di una risposta da parte del server. A questo punto ci si sposta alla finestra del terminale e da qui possiamo interagire con il debug e passare alle **successive istruzioni** che seguono al mio primo punto di breakpoint grazie al comando **F10**. E' possibile poi passare ad un **punto successivo del programma** spostandosi con le **frecce** e selezionando un  nuovo punto di analisi tramite la sequenza di comandi **F6-F12**.

Pian piano che ci muoviamo dentro il programma possiamo : 
 * **analizzare le varie variabili** :   posizionandosi con il **cursore** sulla variabile da analizzare ed eseguendo il comando **F11**;
 * porre **condizioni** su determinate sezioni del programma tramite il comando **F13**;
 * indicare un **altro sorgente**, tramite il comando **F14**, a cui posso porre dei punti di breakpoint.

### 3 - Ending Debugger - Termina sessione di debug
Per uscire dalle operazioni di debug si usa il comando **F3**. Una volta usciti è comunque possibile ritornare al sorgente in debug tramite il comando **DSPMODSRC**.
Per **concludere definitivamente** il debug dopo essere usciti dall'analisi del sorgente con il comando F3 è necessario usare il comando di chiusura **RL**.

### 4 - Procedura alternativa
 Assumiamo come utente di utilizzo**UISMEUP**
 Il lavoro SMEUPUISTD serve l'emulatore, mentre SMEUPUIEXT tutto il resto.
_2_IMPORTANTE NOTA DI DEBUG
_2_Quindi, per debuggare pgm dell'emulatore lavorare come di seguito su SMEUPUISTD, mentre per debuggare funzioni specifiche Looc.up fare la stessa procedura ma utilizzare SMEUPUIEXT

_5_Ricercare il lavoro
Ricercare il**numero**del lavoro di AS/400 attraverso il comando WRKUSRJOB dell'utente UISMEUP con lavori SMEUPUIxxx. Determinare il numero utilizzano l'opzione 5. Determinare il numero del lavoro in esecuzione su AS/400 attraverso il comando WRKUSRJOB.

 :  : INI  Ricerca Lavoro SMEUPUISTD
 :  : CMD ?WRKUSRJOB USER(UISMEUP) JOBTYPE(*BATCH)
 :  : FIN

### Esempio della ricerca
>. Opz  Lavoro      Utente      Tipo     -----Stato------  Funzione
.      SMEUPUIEXT  UISMEUP     BATCH    ACTIVE            PGM-JAJAS1
.  5   SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.      SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.      SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.     ..............................................................
.     .                    Gestione lavoro
.     .                                        Sistema :    S4431CFA
.     . Lavoro :  SMEUPUISTD  Utente :  UISMEUP     Numero :    852654
.     ..............................................................


_5_Attivare il monitoraggio
Una volta determinato il lavoro,(Es.852654) attivare il monitoraggio attraverso il comando STRSRVJOB.
 :  : INI  Attivo il monitoraggio
 :  : CMD ?STRSRVJOB JOB(852654/UICM/SMEUPUISTD)
 :  : FIN
###
_5_Attivare il debug
Attivare il debug sul programma desiderato, (Es.BRAR01G)
 :  : INI  Attivo l'analizzatore
 :  : CMD ?STRDBG PGM(BRAR01G) UPDPROD(*YES) OPMSRC(*NO)
 :  : FIN
 : T03
_5_Chidere il monitoraggio
Attraverso i comandi tipici del debug eseguire l'analisi del lavoro. Una volta terminata l'analisi chiudere il debug con i comandi ENDDBG e ENDSRVJOB.
 :  : INI  Chiudo il monitoraggio
 :  : CMD ENDDBG
 :  : CMD ENDSRVJOB
 :  : FIN
###
_5_Visualizzare il log del lavoro.
Ricercare il**numero**del lavoro di AS/400 attraverso il comando WRKUSRJOB dell'utente UISMEUP con lavori SMEUPUIxxx. Determinare il numero utilizzano l'opzione 5 e poi la 10 e poi F10.
Determinare il numero del lavoro in esecuzione su AS/400 attreaverso il comando WRKUSRJOB.
 :  : INI  Ricerca Lavoro SMEUPUISTD
 :  : CMD ?WRKUSRJOB USER(UISMEUP) JOBTYPE(*BATCH)
 :  : FIN
###
## Esempio della ricerca
>. Opz  Lavoro      Utente      Tipo     -----Stato------  Funzione
.      SMEUPUIEXT  UISMEUP     BATCH    ACTIVE            PGM-JAJAS1
.  5   SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.      SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.      SMEUPUISTD  UISMEUP     BATCH    ACTIVE            PGM-JAJAS0
.     ..............................................................
.     .                    Gestione lavoro
.     .                                        Sistema :    S4431CFA
.     . Lavoro :  SMEUPUISTD  Utente :  UISMEUP     Numero :    852654
.     .
.     . 1. Visualizzazione attributi di stato del lavoro
.     . 2. Visualizzazione attributi di definizione del lavoro
.     . 3. Visualizzazione attributi di esecuzione del lavoro
.     . 4. Gestione dei file di spool
.     .
.     . 10. Visualizzazione registrazione lavoro
.     ...............................................................

.     ..............................................................
.     .        Visualizzazione registrazione del lavoro
.     .                                        Sistema :    S4431CFA
.     . Lavoro :  SMEUPUISTD  Utente :  UISMEUP     Numero :    852654
.     .
.     . >> CALL PGM(JAJAS0) PARM(' ')
.     .    E' stato creato il file fisico B£WUIA0F nella libreria
.     .    Il membro B£WUIA0F è stato aggiunto al file B£WUIA0F in
.     .    Nessun record copiato dal file B£WUIA0F in SMEUP_OBJ.
.     .
.     ..............................................................


## Procedure per il trattamento xml nei servizi
Per facilitare lo svolgimento di elaborazioni sulle stringhe XML sono state create delle procedure specifiche per ogni tipo di informazione che vogliamo ottenere.
Per poter testare tutte le procedure è stato creato un TST apposito.

 :  : INI Chiamata simulazione azioni su XML
 :  : CMD CALL TSTJAXPC1
 :  : FIN

## Utilizzo della £G00 nei servizi
 :  : INI Chiamata funzioni su servizi
 :  : CMD CALL TSTG00
 :  : FIN

## La £J03
Per ottenere in modo semplice moltepliici informazioni  in merito ad un servizio di loocup può essere utilizzata la copy J03.
Le principali funzioni di questa copy sono la funzione **DAT** che si occupa di lanciare il servizio ed ottenere tutte le principali informazioni relative ad esso e la funzione **FMT** che permette di ottenere una formattazione di un £UIBDS in un stringa semplice e viceversa

 :  : INI Chiamata funzioni su servizi
 :  : CMD CALL TSTJ03
 :  : FIN

## La £UIA
 :  : INI Chiamata pgm di test
 :  : CMD CALL TSTUIA
 :  : FIN

## La £UID
 :  : INI Chiamata pgm di test
 :  : CMD CALL TSTUID
 :  : FIN

## Ritornare messaggi da servizio
Un servizio può ritornare un messaggio da esplodere a video in questo modo : 
>C                   EVAL      £JaxMTxt=TXT(02) => Testo
C                   EVAL      £JaxMLiv='50'    => Livello Gravità
C                   EVAL      £JaxMTyp='C'     => C = Richiesta di conferma / I = Informativo
C                   EXSR      £JAX_BMES


Se il messaggio ha livello 99 (o superiore a 90, quale sia tra le due è da verificare) l'xml del componente non viene visualizzato

## Esempi di servizi
 :  : INI . Sorgente prototipo con le sole /COPY necessarie
 :  : CMD CALL B£VED0 PARM('LOSER_ES' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente prototipo con esempi di risposte ai principali componenti
 :  : CMD CALL B£VED0 PARM('LOSER_00' '' '' '' '0')
 :  : FIN

## Deviatore per servizi
 :  : INI . Sorgente prototipo
 :  : CMD CALL B£VED0 PARM('LOSER_ES_F' '' '' '' '0')
 :  : FIN

## Utilizzare un funizzato per rispondere ad una funzione grafica
L'xml della risposta può essere ritornato in queste due modalità : 
 - i primi dieci caratteri della £FUNW2 devono contenere 'XML.INT' e i caratteri della £FUNW2 a partire dall'undicesimo devono contenere l'xml di risposta. In questo caso chiaramente l'xml deve essere di estensione limitata
 - i primi dieci caratteri della £FUNW2 devono contenere 'XML.MED' e i caratteri della £FUNW2 a partire dall'undicesimo devono la chiave della G00 nella quale l'XML dovrà essere memorizzato.

## Test e Documentazione di un servizio
### Documentazione di un servizio
-> Giro relativo alla documentazione di un servizio
   -> Verificare che funzioni tutto correttamente (tramite UP SER)
   -> Introdurre anche la gestione della campo libero

## Test di un servizio
-> Verificare se è già documentato ed in caso contrario scriverne la documentazione
-> La documentazione si trova in DOC_SER con il membro uguale al nome del servizio.
   Come punto di partenza si può utilizzare il membro XXSER.
-> UP SER
-> Funzione Libera
   -> Aggiungi a Preferiti => Gestione preferiti
   -> Vedi XML
-> Tasti funzione per visualizza ultimo xml letto/scritto fatto dalle icone di loocup
-> Cltr + Esecuzione funzione che apre prima la finestra della funzione invece di lanciarla

## Esempio scrittura setup di matrice
>     C                   EVAL      £J15ST='EDT_SCH/G.SET.MAT'
     C                   EVAL      £J15CO=''
     C                   EXSR      £JAX_ISET
      *
     C                   EVAL      £JAXCP=
     C                              'ShowTotal="Yes" ShowGroup="Yes" '
     C                             +'Showfilter="Yes" Showheader="Yes" '
     C                             +'Showcmdbar="Auto" Showid="Yes" '
     C                             +'Detailhint="Yes" '
     C                             +'Enablesort="Yes" Hlrecord="Yes" '
     C                             +'Expanded="Yes" Autofit="Yes" '
     C                             +'Aligntotal="Yes" '
     C                             +'DftTotal="COUNT(XXCODI)" '
     C                   EXSR      £JAX_ASET
      *


## Scrivere il popup dalle sezione da servizio
>     C                   EXSR      £JAX_APOP_I
      *
     C                   EVAL      £JAXCP='<Oggetto Tipo="J1" Parametro="KEY" '
     C                             +'Codice="*NEXT" '
     C                             +'Testo="'+%TRIM(TXT(2))+'" '
     C                   EVAL      £JAXCP=%TRIM(£JAXCP)
     C                             +' Exec="F('+%TRIM(£UIBPG)+';'
     C                             +%TRIM(£UIBFU)+';'+%TRIM(§LISFU)+'.PNX) '
     C                             +' 1('+XUIBT1+';'+XUIBP1+';'+XUIBK1+') '
     C                             +'" />'
     C                   EXSR      £JAX_ADD
      *
     C                   EVAL      £JAXCP='<Oggetto '
     C                             +'Gruppo="3" '
     C                             +'ShowText="Yes" '
     C                             +'Tipo="J1" Parametro="KEY" '
     C                             +'Codice="*F10" '
     C                             +'Testo="F10='+%TRIM(TXT(3))+'" '
     C                             +'Mode="EXT.PAG" '
     C                             +'_Type="TRE;TRA;MAT Pag(Yes)"'
     C                   EVAL      £JAXCP=%TRIM(£JAXCP)
     C                             +' Exec="F('+%TRIM(£UIBPG)+';'
     C                             +%TRIM(£UIBFU)+';'+%TRIM(§LISFU)+'.PEN) '
     C                             +' 1('+XUIBT1+';'+XUIBP1+';'+XUIBK1+') '
     C                             +'" />'
     C                             +'" />'
     C                   EXSR      £JAX_ADD
      *
     C                   EVAL      £JAXCP='<Oggetto '
     C                             +'Gruppo="3" '
     C                             +'ShowText="Yes" '
     C                             +'Tipo="J1" Parametro="KEY" '
     C                             +'Codice="*F13" '
     C                             +'Testo="F13='+%TRIM(TXT(10))+'" '
     C                             +'Mode="EXT.NOT" '
     C                   EVAL      £JAXCP=%TRIM(£JAXCP)+' '
     C                             +'Exec="'
     C                             +'F(EXD;*SCO;) '
     C                             +'2(MB;SCP_SCH;B£SER_88) '
     C                             +'1(OG'+';;'+%TRIMR(XUIBP1)+')'
     C                             +'" />'
     C                   EXSR      £JAX_ADD
      *
     C                   EXSR      £JAX_APOP_F


## Risolvere una funzione A con un servizio
Un servizio può essere richiamato anche per svolgere una funzione di tipo A. Per fare questo sarà sufficiente oltre a specificare il tipo funzione A, indicare come componente il componente EMU.
Es.

A(EMU;Nomeservizio;Funzione.Metodo)

I parametri passati saranno gli stessi che possono essere ricevuti con una chiamata di tipo F.

### NOTA BENE
Se un servizio viene chiamato da un altro servizio per svolgere funzioni di tipo emulativo, e a sua questo servizio essere nuovamente chiamato con un F è importante che in tale servizio  vengano aggiunte nella routine iniziale le seguenti istruzioni : 
>C                   IF        £UIBSC<>'' AND £JAXSC=' '
C                   EXSR      £JAX_INZC
C                   ENDIF

Questo perchè il programma potrebbe essere aperto la prima volta in modalità non-servizio ed aprirsi perciò senza aver caricato il codice della cosa necessario per risolvere una chiamata F.

## Proposta revisione servizi
### Obiettivi
Uniformare le chiamate ai servizi e lo script di definizione/documentazione (DOC_SER).
Rendere la sintassi più veloce, intuitiva e flessibile.

## Prototipi
Per la definizione delle funzioni e metodi (FEM) e degli oggetti (OGG) vengono utlizzati i prototipi.

 :  : PAR F(04)
Matrice dei lock attivi.
 :  : PRO Fun="F(EXB;B£SER_01;LIS.LCK) 1(RE;K-;--)".

Albero dei significati data la classe e la funzione.
 :  : PRO Fun="F(TRE;B£SER_01;AUA.SIG) 1(TA;B£P;--) 2(**;;--)".

Matrice dei record presenti data la classe,la funzione e l'utente.
 :  : PRO Fun="F(EXB;B£SER_01;AUA.ESI) 1(TA;B£P;--) 2(**;;-) 3(UP;;-)".

Costruisce una matrice delle liste presenti per l'oggetto.
 :  : PRO Fun="F(EXB;B£SER_40;LIS.LIS) 1(LI;--;-)".

Costruisce una matrice degli elementi contenuti nella lista.
 :  : PRO Fun="F(EXB;B£SER_40;LIS.ELE) 1(LI;--;--)".


La sintassi è molto efficace, ma presenta delle limitazioni : 
 * intestazione oggetti non modificabile;
 * difficoltà di estensione;
 * duplicata intestazione FEM fra prototipo (..PRO) e sezione (..SEZ);
 * se il campo chiave non partecipa alla configurazione del parametro, non riesco a referenziarlo;
 * i campi oggetto possono referenziarsi fra di loro
             F(TRE;B£SER_01;ATR.TRE) 1(--;-;--) 2(OA;[T1][P1];--)

 * utilizzo di £UIBTx/£UIBPx/£UIBKx che non esprime un oggetto
             F(EXB;JASER_02;OGG.LIS) 1(TA*CNTT;OG[T1];Q1[T1][P1])

Potremmo gestire degli attributi speciali in modo da trattare i campi oggetto nella configurazione.
Potremmo definire due sezioni differenti **Oggetti/Parametri**.
Per semplicifarne la scrittura, potremmo gestire i modelli più comuni di chiamata tramite include della £G90, sul genere del JATRE_06C.

I casi precedenti si risolverebbero così : 
 F(TRE;B£SER_01;ATR.TRE) 1(--;-;--) 2(OA;[T1][P1];--)
..SEZ
ATR            Attributi
.ATR.TRE        Albero dei valori
..RIG
ATR.TRE


|  R="99" |
| 
| .COL Txt="Nome" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" A="L" |
| 
| .COL Txt="Oggetto" A="L" |
| 
| .COL Txt="H" A="L" |
| 
| .COL Txt="O" A="L" |
| 
| .COL Txt="N" A="L" |
| 
| .COL Txt="M" A="L" |
| 
| .COL Txt="Lun" A="L" |
| 
| .COL Txt="D" A="L" |
| 
| .COL Txt="Impostazione" A="L" |
| 
| .COL Txt="Assunto" LunAut="1" |
|  - T1|Tipo|TA*CNTT||O|||||| |
|  - P1|Parametro|OG[T1]|||||||| |
|  - K1|Codice|T1][P1]||O|||||| |
|  - T2|Tipo|TA*CNTT|H|||||||OA |
|  - P2|Parametro|[P1]|H||||||| |
|  - K2|Codice|[OA][P1]||O|||||| |
| 


F(EXB;JASER_02;OGG.LIS) 1(TA*CNTT;OG[T1];Q1[T1][P1])
..SEZ
OGG            Oggetti
.OGG.LIS      Lista
..RIG
OGG.LIS


|  R="99" |
| 
| .COL Txt="Nome" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" A="L" |
| 
| .COL Txt="Oggetto" A="L" |
| 
| .COL Txt="H" A="L" |
| 
| .COL Txt="O" A="L" |
| 
| .COL Txt="N" A="L" |
| 
| .COL Txt="M" A="L" |
| 
| .COL Txt="Lun" A="L" |
| 
| .COL Txt="D" A="L" |
| 
| .COL Txt="Impostazione" A="L" |
| 
| .COL Txt="Assunto" LunAut="1" |
|  - T1|Tipo|TA*CNTT||O|||||| |
|  - P1|Parametro|OG[T1]||O|||||| |
|  - K1|Query|Q1[T1][P1]||O|||||| |
| 


E' sicuramente più complesso rispetto al prototipo, ma più flessibile.
La complessità potrebbe essere nascosta con gli include dei modelli.
Si potrebbe prevedere una doppia gestione, se la funzione non riceve 1() 2() 3() ne chiede la configurazione.

## Componenti
E' corretto che i servizi trattino il componente come parametro?.
Se ritorno un xml di tipo matrice, è naturale che possa trattarlo come EXA,EXB,EXC; perchè specificarlo?
Il componente dovrebbe essere sostituito dal tipo xml, ma come tratto G.SUB.DYN?

## Parametro
Teoricamente un servizio può avere una struttura del parametro differente per Componente/Fem/£UIBTx.
Il JATRE_18C può ricevere parametri e non ha una FEM.
Servizi in cui i £UIBKx sono parametri -> modificare il programma.
Il parametro può fare riferimento ai campi chiave.

## Utilizzo in scheda
Per le schede che ricevono parametri, potremmo introdurre nello script la sintassi : 
>.. S.PAR.INI
.. S.PAR.DOM Cod="Txt" Txt="Testo da scandire" Ogg="**" Lun="50"
.. S.PAR.DOM Cod="Txt2" Txt="Testo da scandire2" Ogg="**" Lun="50"
.. S.PAR.END


o questa sintassi
>.. S.VAR.VAL Sch.Var="x" Req="1" Txt="Testo da scandire" Ogg="**" Lun="50"


dove Req="1"indica che all'apertura della scheda devo valorizzare la variabile

Per il servizio JATRE_18C la £J03 dovrebbe leggere questa sezione.
in questa direzione è stata modificata la £G90 per scandire una sola sezione di un membro.

Possibilità di gestire i parametri di chiamata al servizio da script, G.SET.MAT FunPar="p1() p2()".
Eventuale memorizzazione in B£MEDE al pari dei setup grafici
L'xml della sezione potrebbe essere
><Sez Name="S1" Type="">
. <Sub Tit="Prototipi di chiamata">
.  <MAT>
.    <UserSetups>
.      <Setup _Type="MAT" _Id="V3ASE/Pro" Name="NAME00" FunPar="DIN(1)" ColsWidth="PROTXT=294"/>
.      <Setup _Type="MAT" _Id="V3ASE/Pro" Name="NAME01" FunPar="DIN(0)" ColsWidth="PROTXT=292"/>
.    </UserSetups>
.    <Dati Funzione="F(EXB;B£SER_40;LIS.LIS) 1(LI;CNCLI)"/>
.  </MAT>
. </Sub>
</Sez>


## Configurazione
Introduciamo un nuovo tipo record S- (Servizio) e deleghiamo a £IR1?.
Aprire il G30 con variabili precaricate.
Codice query di ricerca nella definizione del campo.
Se un campo ha come tipo oggetto "V." non viene chiamto il LOSER_01; se specifico "V " inveci sì. E' un altro tipo di configurazione che non gestisce i V.?
Il LOSER_01 dovrebbe conoscere i campi 1() 2() 3() etc.. nella configurazione del parametro, in modo da poter gestire il JATRE_18C.

## Sviluppi
Parte della documentazione andrebbe legata alla FEM, in modo da gestire l'albero funzione/metodo anche in documentazione.
I dati dell'analisi performance potrebbero essere utilizzati per testare i servizi, servendoso quindi di chiamate reali e non solo simulate.
Durante l'elaborazione del documento utilizzare £G90+£G91 per la sostituzione variabili.
Superare i limiti della struttura posizionale £UIBDS, il JAJAS1 dovrebbe ricevere l'intera stringa F(xx;xx;xx) 1(xx;xx;xx) P().
Rimozione limite 15 caratteri in £UIBKx.
I programmi di aggiornamento XXSUP_ non utilizzano gli oggetti.

## Anomalie
Evidenziare in questa sezione i servizi che non rispettano quanto definito.

### B£SER_03
 :  : DEC T(V3) P(ASE) K(B£SER_03)

Il metodo MAT.PER utilizza £UIBK2 e £UIBK3 come filtri sulle date.
Il metodo MAT.ESE è uguale a MAT.PER, viene però incluso solo il tipo peridodo "A".
Sostuire con configurazione del parametro per MAT.PER al fine di rimuovere il metodo MAT.ESE.
 :  : SEZ
MAT            Matrice
.PER       Periodi
 :  : RIG
MAT.PER


|  R="99" |
| 
| .COL Txt="Nome" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="0" A="L" |
| 
| .COL Txt="Oggetto" Lun="0" A="L" |
| 
| .COL Txt="H" Lun="0" A="L" |
| 
| .COL Txt="O" Lun="0" A="L" |
| 
| .COL Txt="N" Lun="0" A="L" |
| 
| .COL Txt="M" Lun="0" A="L" |
| 
| .COL Txt="Lun" Lun="0" A="L" |
| 
| .COL Txt="D" Lun="0" A="L" |
| 
| .COL Txt="Impostazione" Lun="0" A="L" |
| 
| .COL Txt="Assunto" Lun="0" LunAut="1" |
|  - Nome|Descrizione|Oggetto|H|O|N|M|Lun|D|Impostazioni|Assunto |
|  - IniDate|Data iniziale|D8*YYMD| | | | | | | | |
|  - EndDate|Data finale|D8*YYMD| | | | | | | | |
|  - TPer|Tipo periodo|TA*CNPE| | | | | | | | |
| 


Il metodo CON.PES è uguale a CON.TES, viene esploso l'albero dei mesi.
Da gestire una configurazione del parametro per CON.TES al fine di rimuovere il metodo CON.PES.
..SEZ
CON            Contabilità
.TES       Periodi
..RIG
CON.TES


|  R="99" |
| 
| .COL Txt="Nome" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="0" A="L" |
| 
| .COL Txt="Oggetto" Lun="0" A="L" |
| 
| .COL Txt="H" Lun="0" A="L" |
| 
| .COL Txt="O" Lun="0" A="L" |
| 
| .COL Txt="N" Lun="0" A="L" |
| 
| .COL Txt="M" Lun="0" A="L" |
| 
| .COL Txt="Lun" Lun="0" A="L" |
| 
| .COL Txt="D" Lun="0" A="L" |
| 
| .COL Txt="Impostazione" Lun="0" A="L" |
| 
| .COL Txt="Assunto" Lun="0" LunAut="1" |
|  - Nome|Descrizione|Oggetto|H|O|N|M|Lun|D|Impostazioni|Assunto |
|  - TEsp|Tipo Esplosione|.VTEsp| | | | | | | | |
| 

