## REGOLE PER L'INSERIMENTO DELLE MACRO IN UN PROGRAMMA RPG    3
# PRECOMPILATORE RPG
## Obiettivo
Scopo di tale funzione è di realizzare richiami compatti alle routines standard, eliminando le MOVE precedenti e successive al richiamo, oppure di eseguire sequenze ripetitive e parametrizzabili, ma troppo brevi per giustificare l'utilizzo di una routine apposita, per la pesantezza del passaggio dei parametri.
## Vantaggi
1.   Diminuire il numero di specifiche RPG da scrivere
2.   Aumentare la leggibilità. I comandi da richiamare possono essere impostati in una forma del tipo : 
OVRDBF (TABEL,TABEL01L)
3.   Diminuire le possibilità di errori banali
4.   Ottenere gli stessi vantaggi di modificabilità esterna di parti di programma comune. (decidere di gestire il carattere * nelle parzializzazioni ABC* uguale da ABC ad ABC999999)
## Esempio
Si supponga di dover eseguire un programma che dopo aver controllato i limiti impostati a video sui valori VALINI e VALFIN, esegue una apertura del membro MEM1 del file FIL1 con nome NOM1.
Per ogni record letto, si eseguono le decodifiche della tabella TA1 e del centro di costo.
Avremo : 
C              CRTFMT     BEGSR
M* IMPLIM (VALINI,VALFIN)      Impostazione limiti
M* CORLIM (VALINI,VALFIN,61)   Controllo se inf > sup e indic
C                         ENDSR
C*
C              APEFIL     BEGSR
M* OVRDBF (NOM1,FIL1,MEM1,OPEN)
C                         ENDSR
C*
C              LETREC     BEGSR
C                         READ NOM1
M* £LETSM ('TA1',F$ELTA,DESTAB,51)
M* £IFCDC (F$CDC,DESCDC,52)
C                         ENDSR
## FORMATO DI RICHIESTA PARAMETRI
Il formato richiede membro, file e libreria di origine nel quale sono scritte le macro e la destinazione corrispondente per l'espansione e la creazione dell'RPG.

Sono eseguiti i seguenti controlli : 
-    L'origine deve esistere
-    La destinazione deve essere diversa dall'origine
-    Se si chiede la sostituzione, il membro deve esistere, altrimenti non deve esistere
-    Il file di destinazione non deve essere "SRC" oppure
"QRPGSRC" per evitare rischi di distruzione accidentale di propri programmi.
-    Deve esistere il file contenente le MACRO
## REGOLE PER LA PREPARAZIONE DELLE MACRO
La creazione di una macro avviene mediante la definizione di un membro TXT con alcune specificità.
In particolare avremo due nuovi TIPI SPECIFICA, P ed M
### Specifiche P di definizione dei parametri
Descrivono le caratteristiche dei parametri attraverso una codifica posizionale fissa e in particolare : 
P O assunto   Descrizione                        TKnnnCondizione
P F &1        Descrizione parametro 2            T  5 CLS
P F 60        Ecc.                               VK 1 S N
-    Tipo specifica
identifica la definizione dei parametri
-    Obbligatorietà (1)
O = Il parametro è obbligatorio
F = Facoltativo
-    Valore assunto (10)
Questo valore viene sostituito al parametro se questo non viene passato. Il valore assunto può riferirsi ad altro parametro se inizia con &.
Potremo ad esempio specificare che se il parametro 3 non viene passato si assume uguale al parametro 1 ecc.
-    Descrizione parametro
Utilizzato come documentazione e nella segnalazione degli errori del procompilatore
-    Tipo di controllo
Indica al programma interattivo di costruzione macro se eseguire dei controlli. I caratteri minuscoli indicano che viene eseguito un controllo (esempio ricerca) ma non è obbligatorio mentre il maiuscolo indica l'obbligatorietà.
Abbiamo in particolare : 
T/t  Elemento della tabella specificata nella condizione
S/s  Settore di tabella
V    I primi due caratteri del parametro devono essere fra quelli specificati nella condizione
M    Messaggio del file specificato nella condizione
I    Indicatore
-    Costante
Se presente il carattere K, il parametro viene considerato come una costante e pertanto vengono posti gli apici iniziale e finale.
-    Condizione
Utilizzato per condizionare il tipo di controllo da eseguire sul parametro.
### Specifiche di tipo M
M* xxx/xxx/xxx (PARAM.1, param.2, param.3 + param.4)
-    xxx/xxx/xxx = individuazione della macro mediante libreria/file/membro.
Libreria/file sono facoltativi. Se non specificati si assumono *LIBL e file QMACGEN
-    Membro
E' il nome della macro da esplodere con inizio a posizione 9
-    Parametri.
Se i parametri sono scritti in maiuscolo significa che sono obbligatori, viceversa sono facoltativi)
### Specifiche di tipo C
C        &1       IFEQ *BLANK                        -&3
C                 MOVEL*BLANK'    &2                 &1
C                 ELSE                               &1
C                 MOVEL*ALL'9'    &2                 &1
C                 END                                &1
C        &1       CAT  &2 : 1       &3
Trasferite nel programma finale contengono : 
-    &1,&2 e &3 indicano dove devono essere posti i parametri passati dalla MACRO. A partire da 10 i parametri vengono identificati dalla lettere dell'alfabeto. Avremo quindi che &A identifica il parametro 10 e &D il parametro 13. ## Convenzioni per la definizione delle macro
Bisogna aver cura nella definizione della macro :  vanno prima inseriti i parametri obbligatori, e poi quelli facoltativi, ordinati in modo decrescente rispetto al loro uso presumibile.
Così facendo, il parametro che viene usato più raramente è posto all'estrema destra, in modo tale che non c'è bisogno di inserire virgole intermedie.
## REGOLE PER L'INSERIMENTO DELLE MACRO IN UN PROGRAMMA RPG
Si consiglia di importare la prima specifica M della MACRO stessa.
Si inserisce una specifica di tipo M seguita dal nome della macro e dalle variabili fra parentesi e separate da virgole.
### Tipo parametro
. Variabile (il nome del campo nel programma RPG)
. Costante (racchiusa fra apici)
. Se il parametro contiene il carattere ',' o il carattere '/' o delle parentesi tonde, nella chiamata della macro dovrà essere compreso tra i simboli minore '<' e maggiore '>'.
Es.
M* Nome_macro ( <PAR1,IND> ,  PAR 2 , PAR 3 )
NB : Sia i parametri che le costanti possono avere una lunghezza massima di 8 caratteri, compresi gli apici per le costanti.
### Numerazione parametri
Se il parametro è mancante, si deve inserire comunque la virgola che lo precede, ad esempio yyy1,,,yyy4.
### Continuazione riga
Una funzione macro può continuare su più righe. Per indicare che la riga continua si può inserire un carattere + e continuare con una nuova riga di tipo M*

## TECNICA DI ESPANSIONE DELLE MACRO
La sostituzione dei parametri viene eseguita con le seguenti regole : 
-    ogni volta che si trova una &n, si puliscono questi due caratteri, e si inserisce il parametro n della macro
-    se uno dei parametri utilizzati non è stato passato, si ignorano le istruzioni che lo contengono
-    E' possibile forzare l'esclusione di una specifica in funzione della presenza di un parametro o della mancanza.
.    Il parametro "&n" nelle posizioni di commento RPG vale come condizionamento. Se esso manca la specifica viene esclusa.
.    Se il primo carattere di commento è "-" allora la specifica viene esclusa dalla presenza del parametro "&n". Ciò può ad esempio essere utile per definire alternativamente  due messaggi in funzione della presenza o mancanza di un parametro.
-    se il parametro è una costante, (tra apici o iniziante con una cifra) si ignorano le istruzioni in cui compare come campo del risultato.
Controlli del precompilatore : 
-    esistenza macro
-    costanti definite correttamente :  alfanumeriche tra apici, numeriche con solo numeri
-    controllo parametri :  gli obbligatori devono essere presenti; non possono essere presenti parametri non previsti
## STANDARD ASSUNTI
### Denominazioni
-    Le macro collegate ad una COPY hanno lo stesso nome della COPY
-    Le Macro collegate a comandi hanno il nome del comando
### File e Librerie
-    Le macro standard si trovano in QMACGEN di SMESTD
-    I programmi esplosi prima della compilazione si trovano in un file SRCMAC della stessa libreria.
## NOTE VARIE AD USO INTERNO
### // DA FARE
Il precompilatore dovrà controllare che il sorgente di partenza contenga solo numeri di riga interi, e dovrà rinumerarlo a partire dalla prima istruzione in cui trova un numero di riga con decimali. Nel sorgente d'arrivo le istruzioni esplose dalla macro verranno numerate con passo 0.01. In tal modo non si dovrebbero avere problemi con l'esecuzione del debug anche se il sorgente non è stato salvato con l'opzione di riordinamento membro.
### // NOTE PROVVISORIE
Il tempo di costruzione sembra dai primi test non rilevante. In ogni caso ci preoccuperemo in seguito di eventuali miglioramenti di prestazioni.
Nella fase di definizione delle macro, sarà opportuno procedere ad una normalizzazione delle routine standard coinvolte :  definire se i campi di input vengono ripuliti alla fine e se quelli di output vengono puliti all'inizio, e decidere se far eseguire ciò alle routine o alle macro.
nella macro avranno i nomi &9,&A,&B..&I
Per il momento si è deciso di fissare il numero massimo dei parametri a
Nella libreria SMESTD, c'è il file source QMACGEN contenente alcune prove di macro.
### // IMPLEMENTAZIONI FUTURE
.    Espansione di calcoli aritmetici
.    Inserimento delle specifiche standard di un sorgente
## Appendice del 7.9.92 (Guido)
Mi pare che la definizione di macro locali possa portare problemi nel debug, non essendo ben chiari i numeri di riga che assumeranno nel sorgente finale.
E' da tener presente che una macro locale, essendo definita al momento, è più probabile che conterrà errori rispetto ad una macro esterna, e quindi avrà bisogno del debug per scoprirli.
Preparare un comando unico che esegue la precompilazione e, se è andata a buon fine, la compilazione. Se la precompilazione contiene errori,produrre una stampa delle anomalie e mandare un messaggio all'utente.
Questo comando dovrebbe contenere i parametri del CRTRPGPGM, almeno i più importanti (release current o previous, ignore decimal error,..).
