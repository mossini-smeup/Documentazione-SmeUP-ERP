# Conversione dei programmi da RPG a ILE
## Prerequisiti
Il file source deve avere lunghezza 112 al posto dei consueti 92, pena il troncamento dei commenti a destra. Pertanto, quando si crea un file source tramite CRTSRCPF, conviene impostare la lunghezza record a 112.

## Come convertire i programmi
Per convertire un programma da RPG a ILE è stato creato il programma B£UT24, richiamabile anche automaticamente mettendo IS nelle opzioni del PDM (si ricorda che i comandi di Sme.up sono presenti nel file opzioni QAUOOPT della SMEDEV, impostabili premendo F18 dal PDM e mettendo SMEDEV come libreria del File opzioni).
Lo stesso programma permette anche di creare un programma adatto per LOOC-UP.

# Cambiamenti del linguaggio
## Introduzione
Questo documento ha lo scopo di presentare le possibilità offerte dall'ILE che pensiamo di recepire nello standard. NON si tratta di un'introduzione generale all'ILE, per la quale si rimanda ai manuali IBM, che. peraltro sono disponibili in formato PDF sul server, nella cartella : 
 :  : DEC T(J1) P(PATHDIR) K([SME.SMEPCO]\Documentazione varia AS400) D(Documentazione varia AS400) O(GD)
 :  : DEC T(J1) P(PATHFILE) K([SME.SMEPCO]\Documentazione varia AS400\Manuali AS400 in formato PDF) D(Manuali AS400 in  formato PDF) O(GD)

## Specifiche
Le specifiche di tipo **I** (DS) e di tipo **E** non esistono più e sono state sostituite dalle specifiche di tipo **D**, utilizzabili anche per definire delle variabili.
Per indicare una schiera : 
>.                             lunghezza      schiera a 8 elementi
.                                    \      /
.    DINT              S             80    DIM(8) CTDATA PERRCD(1)
.                      \_ variabile                 |           |
.                                           indica una schiera  |
.                                           definita a tempo di |
.                                           compilazione        |
.                                                               |
.                                               indica il n° di
.                                               elementi per riga
.                                               della schiera
.                                               è opzionale il
.                                               default è 1
.
.    DINT              S             10    DIM(8) CTDATA PERRCD(8)
.                                                               |
.                                                     Tutti gli 8
.                                                   elementi sono
.                                                  scritti su una
.                                                      sola riga
.
.
.Per indicare una DS : 
.     DDSDATA           DS            80
.                       \_ Data structure
..
.
.Per indicare una costante : 
.     DCOST             C                   'ABCDEFGH'
.                       \_ costante            \_ valore della costante
.
.Per indicare una variabile : 
.     DVAR              S             30    INZ('ABCDE')
.                                            \_ la inizializzo con
.                                               un valore
.     DVAR2             S                   LIKE(VAR1)
.                                            \_ equivale a un DEFN *LIKE
.


Per ulteriori approfondimenti leggere i capitoli inerenti l'argomento.

## Espressioni
Le espressioni sono dei gruppi di comandi / operatori che possono essere scritte nel fattore 2 esteso (rendendo il codice più flessibile e leggibile) su più righe, senza la necessità di utilizzare caratteri di continuazione.
>     C                   IF        $A=3 AND ($AZIO='R' OR $AZIO='r')
     C                             AND *IN45=*ON


Possono essere utilizzate solo se l'operazione supporta il fattore 2 esteso.

## Funzioni interne (BIF)
Le funzioni interne sono comandi (quali SUBST, SCAN, EQUAL, ...) che iniziano con il carattere %, possono essere utilizzati all'interno delle espressioni e che spesso rendono inutile l'utilizzo di variabili di appoggio, oltre che il codice molto più leggibile.
>.     C                   IF        %SUBST(£FUNFU : 4)='N'


## Operandi particolari
Oltre ai vari +, -, / (diviso), * (moltiplica), <, >, <> (diverso), >=, <=, AND, OR, NOT, alcuni particolari sono : 
>. ** -> elevamento a potenza
.     C                   EVAL      CUBO=2**3

avrà come risultato 8 nella variabile CUBO.
+ -> se utilizzato fra stringhe esegue un concatenamento.
>.     C                   EVAL      TESTO='Pippo, ' + 'Paperino'

avrà come risultato la stringa 'Pippo, Paperino' in TESTO.

## Parole chiave
Le parole chiave del linguaggio sono rimaste sostanzialmente le stesse, eccetto per alcune varianti : 
 * SETOF -> SETOFF
 * SELEC -> SELECT
 * LOKUP -> LOOKUP
 * UPDAT -> UPDATE
 * REDPE -> READPE
 * DEFN  -> DEFINE
 * DELET -> DELETE
 * EXCPT -> EXCEPT
 * OCUR  -> OCCUR

Le opzioni che prima si mettevano in posizione 53 ('P' per pulizia campo, 'H' per arrotondamento, 'N' per lettura senza allocazione) devono adesso essere specificate fra parentesi dopo l'operazione.
Es. :  MOVEL(P), DIV(H), CHAIN(N).

Alle operazioni di confronto ne sono state aggiunte altre che permettono di sfruttare il fattore 2 esteso, esplicitando su una stessa riga più confronti logici e raggruppandoli tramite parentesi : 
 * WHEN
 * IF
 * DOW
 * DOU

Esempio
>.     C                   IF        $A=3 AND ($AZIO='R' OR $AZIO='r')


E' stata aggiunta l'istruzione FOR, che permette di eseguire dei cicli decidendo il passo di incremento.
> .    C                   EVAL      FATT=1
 .    C                   FOR       X = 1 TO N
 .    C                   EVAL      FATT = FATT * X
 .    C                   ENDFOR

Esegue il calcolo di n fattoriale.
La sintassi è : 
 * FOR  Indice = valore_iniziale BY incremento TO|DOWNTO limite_finale
 * incremento :  passo di incremento
 * TO :  incremento viene sommato a valore_iniziale
 * DOWNTO :  incremento viene sottratto a valore_iniziale

Esempio per trovare in una stringa STR l'ultima posizione di 'H'.
>.     C                   FOR       X = %LEN(STR) DOWNTO 1
.     C                   IF        %SUBST(STR,X,1)='H'
.     C                   LEAVE
.     C                   ENDIF
.     C                   ENDFOR


## Lettura record
Nelle SETLL CHAIN e READ non è più obbligatorio l'indicatore, quindi lo si può dimenticare, con risultati evidentemente imprevedibili.
Il motivo della non obbligatorietà è dato dalla presenza delle funzioni %EQUAL %FOUND e %EOF (vedere sezione sulle funzioni). E' consigliato l'uso di queste funzioni per evitare dimenticanze dell'indicatore, oltre alla maggior chiarezza.

## Funzioni di sottostringa nei test
E' possibile che i test si eseguano su funzioni, compattando il codice, rendendolo più leggibile ed eliminando l'uso di variabili di appoggio.
Ad esempio, nel caso in cui una routine venga eseguita se il quarto carattere della funzione vale 'N', la sintassi da usare è : 
>.     C              IF        %SUBST(£FUNFU : 4)='N'
.     C              EXSR      NOTEDS
.     C              ENDIF


## Variabili
Finalmente la CLEAR ha il campo che pulisce nel risultato (e non più nel fattore 2), è vivamente consigliato di utilizzarla, dichiarandone anche la dimensione.
La lunghezza massima di un campo è stata portata da 256 a 32767 e il numero massimo di decimali a 9.

## Schiere
Per dichiarare una schiera : 
>.                              lunghezza      schiera a 8 elementi
.                                     \      /
.     DINT              S             80    DIM(8) CTDATA PERRCD(1)
.                       \_ variabile                |            |
.                                            indica una schiera  |
.                                            definita a tempo di |
.                                            compilazione        |
.                                                                |
.                                                indica il n° di
.                                                elementi per riga
.                                                della schiera
.                                                è opzionale il
.                                                default è 1
.
.     DINT              S             10    DIM(8) CTDATA PERRCD(8)
.                                                                |
.                                                      Tutti gli 8
.                                                    elementi sono
.                                                   scritti su una
.                                                       sola riga.


L'indice di una schiera viene specificato tra parentesi.

Es. :  TXT(5)
Quando il contenuto di una schiera è un indice, non serve più usare una variabile di lavoro. Nell'esempio, la schiera OPZ contiene le informazioni collegate ad una scelta del £G08 :  mettendole in una DS che le sottostringa, è sufficente la seguente istruzione : 
>.     C                   EVAL      DSRI08=OPZ(£08B(1))

Il numero massimo di elementi di una schiera è stato portato a 32767

E' possibile sovrapporre più schiere per semplificare l'ordinamento di schiere collegate tra loro.
Nell'esempio che segue, alla schiera XLAVORO sono sovrapposte le 3 schiere XOGG, XQTA e XSCO (definite implicitamente).
>.    D             DS
.    D XLAVORO           28    DIM(999)
.    D  XOGG             15    OVERLAY(XLAVORO : 01)
.    D  XQTA              9  0 OVERLAY(XLAVORO : 16) INZ
.    D  XSCO              4  2 OVERLAY(XLAVORO : 25) INZ


Eseguendo
>.     C                   SORTA     XLAVORO

tutte le schiere sono ordinate rispetto al contenuto di XOGG.

## Data Structures -DS-
E' stata ridefinita la struttura della definizione dei sottocampi delle DS, in modo da facilitare notevolmente il programmatore.
Si può definire un sottocampo specificandone unicamente la lunghezza e non più l'inizio e la fine : 
>. (A) D DSTOT           DS           300
.     D  CAMPO1                 1     10
.     D  CAMPO2                11     15
. (B) D DSTOT           DS           300
.     D  CAMPO1                       10
.     D  CAMPO2                        5


Le definizioni (A) e (B) sono equivalenti, ma (B) è notevolmente più semplice.
Naturalmente, per definire una posizione precisa della DS, è necessario impostare comunque l'inizio e la fine (come nella definizione del tasto funzionale del formato video)
>.     D DSFMT1          DS
.     D  £KEY1                369    369

Se un campo è di definizione esterna, è possibile inserirlo come sottocampo di DS, indicandone unicamente il nome.
Ciò è utilissimo nell'uso dell'£MDV : 
>.     D/COPY QILEGEN,£MDVDS
.     D  W$FUNZ
.     D  W$METO
.     D  W$AZIE
.     D  W$TREG


Non è possibile definire come sottocampo di DS un campo definito internamente in un'altra posizione :  in compilazione viene segnalato che un campo è stato definito più volte.
>. (A)  D CAMPO1          S             10
.      D DSTOT           DS           300
. (B)  D  CAMPO1                       10


L'errore è segnalato a causa di una doppia definizione :  (A) e (B). Nel caso in cui un elemento di una DS sia una schiera, dato che le specifiche D sostituiscono le E e le IDS, basterà definire il campo come schiera all'interno della DS : 
>.     D DSTOT           DS
.     D  CMP01                        10
.     D  SCK01                        10    DIM(20)

Con questa codifica verranno definite le variabili : 
 * CMP01, campo alfanumerico dl 10
 * SCK01, schiera di 20 elementi alfanumerici lunghi 10
 * DSTOT, struttura dati che costituisce l'insieme dei due.

Per quanto riguarda la lunghezza di una DS, si possono verificare due casi : 
 - nel caso essa non sia specificata, verrà determinata come somma dei suoi sottocampi;
 - nel caso essa venga specificata, in compilazione verrà controllato che la somma dei suoi sottocampi non superi la lunghezza della DS.
In ogni caso la lunghezza massima è di 32767

_Esempi di definizioni_
>.     DDSDATA           DS            80    OCCURS(8)
.                       \_ Data structure     \_ eventuale numero
.                                                di ricorrenze
.                          posizione iniziale e finale
.                               /     \
.     D  CAMPO1                 1     10
.           \_ sottocampo della DS
.     D  CAMPO2                       30
.                                      \_ indico solo la lunghezza
.     D  CAMPO3                             LIKE(COST)
.                                             \_ uso una precedente
.                                                definizione
.     D  CAMPO4                       15    DIM(8)
.                                             \_ automaticamente
.                                                dichiaro una schiera
.     D  CAMPO5                       15    OVERLAY(CAMPO2)
.                                             \_ suddivido CAMPO2 in
.                                              _  2 campi da 15
.                                             /
.     D  CAMPO6                       15    OVERLAY(CAMPO2 : 16)
.                      equivalente alla specifica precedente
.                                                          \
.     D  CAMPO6                       15    OVERLAY(CAMPO2 : *NEXT)
.
.Per indicare una DS esterna
.     DBRARTI         E DS                  EXTNAME(BRARTI0F)
.                                           PREFIX(A_)
.                                           \_ aggiunge ai campi del
.                                              file il prefisso A_.
.                                              Ex.T§TDOC -> A_T§TDOC
.                                           PREFIX(A$,2)
.                                           \_ sostituisce i primi 2
.                                              caratteri dei campi
.                                              con A$
.                                              Ex.T§TDOC -> A$TDOC
.                                           RENAME(BRARTIR : BRARTI0)
.                                           \_ rinomina il record
.                                           USROPN
.                                           \_ apertura condizionata


## Errori nuovi
E' necessario prestare maggiore cura nella definizione dei campi numerici, poichè se in un'operazione aritmetica di EVAL il risultato è troppo grande, viene emesso un errore (CPF) di overflow.

È stato portato a 00 il livello di gravità di alcuni errori sui file : 
 * file definito, ma non usato;
 * file definito in modo più ampio di quanto effettivamente usato (ad esempio dichiarato in aggiornamento, ma solo letto).

In compilazione viene controllato che la somma dei sottocampi di una DS non superi la lunghezza della DS stessa.

## Varie
Non è necessaria una variabile per l'apertura condizionale di un file :  esiste la funzione %OPEN, che si può usare nelle condizioni : 
>.     C                   IF        %OPEN(nomefile)
.     C                   IF        NOT %OPEN(nomefile)


Ora il numero relativo di record viene sempre aggiornato anche nelle letture per blocchi di record (per esempio con un file in input primario) e l'operazione FREE non è più supportata.
Dal momento che sono state spostate le posizioni delle parole chiave per le ricerche "alla posizione...", sono richieste le seguenti modifiche : 
 * Nome routine (fattore 1) -> da 18 a 12
 * Codice operazione -> da 28 a 26
 * Fattore 2 -> da 33 a 36
 * Risultato -> da 43 a 50

# Parametri di compilazione
## ACTGRP
Il ACTGRP parola chiave consente di specificare il gruppo di attivazione del programma è associato a quando è chiamato.

Se ACTGRP (*CALLER) è specificata, allora il programma viene attivato nella attivazione del chiamante gruppo.

Se ACTGRP (*NEW) è specificata, allora il programma viene attivato in un nuovo gruppo di attivazione ogni volta che il pgm viene richiamato. Il gruppo viene creato/cancellato ogni volta che il pgm viene richiamato/terminato, che il pgm sia che il pgm si chiuda in LR che il pgm si chiuda in RT (perciò è come se il pgm si chiudesse sempre in LR).

Se ACTGRP (Nome) è specificata, allora il programma viene attivato nella attivazione gruppo di attivazione specificato. Il gruppo di attivazione viene creto nel momento in cui il pgm viene richiamato per la prima volta e rimane attivo fintanto che il lavoro termina o che viene eseguito il comando RCLACTGRP in un momento in cui l'ACTGRP non risulta attivo.
Perciò che il pgm che lo ha creato si chiuda in LR o in RT non ha effetto sull'ACTGRP mentre ha effetto sul richiamo del pgm stesso :  anche se l'actgrp esiste già se il pgm si chiude in RT il pgm non verrà riaperto, mentre lo sarà se il pgm si chiude in LR.

# Standard Sme.up
## Mantenere una programmazione comune
Per il momento è stato deciso di non utilizzare le subroutine con parametri (richiamate tramite CALLB).

## Tipizzazione schiere
Quando nei programmi si definiscono delle schiere a tempo di compilazione (CTDATA, per capirsi) bisogna anche definirne la tipologia :  mettere il tipo schiera preceduto dal carattere di underscore nel campo "Comments" della riga di definizione della schiera stessa.
Se una schiera contiene parti da tradurre non deve essere definita mediante la tecnica di separazione di tipo ALT(). In questo caso si consiglia di utilizzare la definizione della schiera base come DS e delle sottoschiere mediante OVERLAY. (Si veda come esempio il sorgente B£IVD0)
Eventuali costanti testuali individuate dal compilatore all'interno delle specifiche C ne bloccano la compilazione.
>N.B. :  i tipi schiera sono oggetti V2 A£TSK. Basandosi su questa definizione, in fase di compilazione (con CO) viene creata automaticamente la routine £INIZTR.

### Esclusione automatismi
In caso il programma debba essere escluso completamente dagli automatismi delle traduzione, è possibile utilizzare l'opzione di compilazione (COP*) ***NOLI** .
Utilizzando questa opzione : 
 * Non vengono estratte le costanti
 * Non viene controllata l'eventuale presenza di costanti nelle specifiche C
 * Non viene aggiunta la routine di traduzione £INIZTR
 * Non viene controllata la tipizzazione delle schiere
Se invece il programma necessita di una gestione manuale delle traduzioni, è possibile utilizzare l'opzione di compilazione (COP*) ***NOA£B** .
Utilizzando questa opzione : 
 * Vengono estratte le costanti
 * Viene controllata la tipizzazione delle schiere
 * Viene controllata l'eventuale presenza di costanti nelle specifiche C
 * Non viene aggiunta la routine di traduzione £INIZTR

## Utilizzo degli actgrp specifici
Di default i pgm smeup dovrebbero essere compilati con DFTACTGRP(*NO) e ACTGRP(*CALLER). Qualora però si vogliano cambiare tali definizioni, oltre a dover implementare le relative istruzioni di compilazione (es. COP* DFTACTGRP(*NO) ACTGRP(*NEW)) vanno utilizzate delle /COPY alternative rispetto alla £INIZH.
- £INIZHAN ACTGRP(*NEW)
- £INIZHNN ACTGRP(Nome)

## Utilizzo delle annotazioni
Sono state attivate le seguenti annotazioni : 
 :  : PAR
@StartTrace
@StopTrace
@StartLog
@StopLog

### Trace
Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione della traccia. L'utilizzo della traccia deve essere fatto quando si vuole inserire un monitor delle performance.
L'attivazione della traccia avviene durante la compilazione, attraverso apposito parametro oppure attraverso l'opzione *TRACE da impostare nei parametri di compilazione (COP*), in
questa maniera la traccia è aggiunta solo quando è necessario monitorizzare le performance.

Il parametro della annotazione **@StartTrace** è il momento **M(<NomeMomento>)**
Il nome momento viene convertito in una variabile che contiene il tempo di inizio della traccia, per questo motivo non inserire spazi o cartteri speciali nel nome.

I parametri della annotazione **@StopTrace** sono il momento **M(<NomeMomento>)** e il testo **T(<Testo>)**.
Il nome momento deve essere lo stesso utilizzato nello @StartTrace, da cui deriva il tempo trascorso tra l'inizio e la chiusura della traccia.
Il testo non deve contenere apici singoli e si possono aggiungere fariabili attraverso la seguente nomenlcatura
**&A(<Variabile di Testo>)**
**&N(<Variabile Numeica>)**

Il risultato è memorizzato nel file JALOGT con tipo record Q06 e origine TRC.

### Log (sviluppo)
Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione dei log. L'utilizzo del log deve essere fatto quando si vuole monitorizzare in modalità dettagliata l'esecuzione del servizio.
L'attivazione del log avviene attraverso la tabella PGM con l'apposito flag.

Il parametro della annotazione **@StartLog** è il momento **M(<NomeMomento>)**
Il nome momento viene convertito in una variabile che contiene il tempo di inizio della traccia, per questo motivo non inserire spazi o cartteri speciali nel nome.

I parametri della annotazione **@StopLog** sono i seguenti : 
*  **M(**<NomeMomento>**)**
*  **LIBE(**<Testo>**)**
*  **ORIG(**<Origine>**)**
*  **WEFU(**<funzione>**)**
*  **WEME(**<Metodo>**)**
*  **TPO1(**<1 oggetto>**)**
*  **CDO1(**<1 istanza>**)**
*  **TPO1(**<2 oggetto>**)**
*  **CDO1(**<2 istanza>**)**
*  **TPO1(**<3 oggetto>**)**
*  **CDO1(**<3 istanza>**)**
*  **TPO1(**<4 oggetto>**)**
*  **CDO1(**<4 istanza>**)**
*  **TPO1(**<5 oggetto>**)**
*  **CDO1(**<5 istanza>**)**
Il nome momento deve essere lo stesso utilizzato nello @StartLog, da cui deriva il tempo trascorso tra l'inizio e la chiusura della traccia.
Se non definita un'origine verrà assunto '???'.
Il testo non deve contenere apici singoli e si possono aggiungere fariabili attraverso la seguente nomenlcatura
**&A(<Variabile di Testo>)**
**&N(<Variabile Numeica>)**
