Utilizzare una API in programma RPG ILE equivale ad eseguire una normale istruzione CALL come con un qualunque programma esterno. Ciò che rende l'utilizzo delle API un
po' più complesso è la comprensione dei parametri di input e output richiesti. Il tutto è reso a volte ancora più complesso dal fatto che molte API necessitano di determinati parametri e restituiscono risultati di lunghezza variabile, per cui è necessario ricorrere all'utilizzo di puntatori.
va bene
La documentazione di tutte le API disponibili può essere letta accedendo al link : 
 :  : DEC T(J1) P(PATHFILE) K( http://publib.boulder.ibm.com/infocenter/iseries/v5r3/topic/apis/apifinder.htm) O(K)

__Prestare attenzione alla versione del sistema operativo (in questo caso ci riferiamo alla versione 5.3).

Per accedere alla documentazione relativa ad altre versioni del sistema operativo si consiglia di consultare il sito "base" della documentazione IBM relativa all'Iseries.

[ http://publib.boulder.ibm.com/iseries/]( http://publib.boulder.ibm.com/iseries/)

Utili esempi sull'utilizzo di API possono essere trovati anche in questi siti : 
[ http://www.think400.dk]( http://www.think400.dk)
[ http://www.code400.com/]( http://www.code400.com/)

## Esempio di utilizzo di una API
Syntax Check SQL Statement (QSQCHKS) API.
Nel file QAPIGEN si può vedere il membro QSQCHKS
 :  : DEC T(MB) P(QAPIGEN) K(QSQCHKS) O(K)

Dal sito IBM sopra citato si legge che i parametri di questa API sono i seguenti : 
>1 Source records containing SQL statement         Input   Char(*)
2 Record length                                   Input   Binary(4)
3 Number of records provided                      Input   Binary(4)
4 Language                                        Input   Char(10)
5 Options                                         Input   Char(*)
6 Statement information                           Output  Char(*)
7 Length of statement information                 Input   Binary(4)
8 Number of records processed                     Output  Binary(4)
9 Error code I/O                                  I/O     Char(*)


Questo esempio comprende parametri di input e di output a lunghezza variabile.
Il tipo di dato Char(*) significa puntatore ad una varibile di tipo CHAR (con un poco di conoscenza del il linguaggio C, tutto risulterà molto famigliare).
Per utilizzare questa Api in un programma QRPGLE è consigliabile definire un prototipo di chiamata, che consenta di utilizzare la stessa sotto forma di procedura.
Il nostro programma RPG comprenderà quindi le seguenti specifiche D (queste definizioni sono presenti nella /COPY QAPIGEN,QSQCHKS.
>  *-- Syntax Check SQL Statement -----------------------------------------.
 D SQLSYNTAX       Pr                  ExtPgm( 'QSQCHKS' )                .
 D  SQLSTR                    32767a   Const  Options( *VarSize )         .
 D  SQLSTRL                      10i 0 Const                              .
 D  SQLSTRRN                     10i 0 Const                              .
 D  SQLLANG                      10a   Const                              .
 D  SQLOPT                    32767a   Const  Options( *VarSize )         .
 D  SQLINF                    32767a          Options( *VarSize )         .
 D  SQLINFL                      10i 0 Const                              .
 D  SQLREC                       10i 0                                    .
 D  SQLERROR                  32767a          Options( *VarSize )         .
  *---------------------------------------------------------------------- .


Nel prototipo sono stati dichiarati i parametri : 
 * CHAR(*)  è stato definito come Const  Options(*VarSize)
 * Binary(4) è stato dichiarato come 10I 0

La dichiarazione come Const è riservata ai soli paramatri di input.
Il prototipo può anche ridefinire il nome dell'API (come avviene in questo caso, dove l'API verrà utilizzata richiamando la procedura SQLSYNTAX). In ogni caso, la procedura può essere chiamata come il none dell'API stessa.

Per utilizzare l'API in un programma RPGLE occorre definire anche le DS che rappresentano la struttura dei parametri di input e output.
La definizione di queste DS (non per tutte le API) può essere cercata nel file sorgente QSYSINC/QRPGLESRC, la cui libreria viene fornita con il sistema operativo, ma non è normalmente installata. Essa può essere installata attraverso la normale procedura per i programmi su licenza (prodotto  5722SS1 opz. 13 OS/400 - Include apertura del sistema).

Se una delle definizioni presenti in questa libreria è stata utilizzata in un programma di Sme.up, se ne potrà trovare una copia in SMESTD/QAPIGEN (con lo stesso nome membro).
E' importante osservare come non sia sempre possibile utilizzare queste definizioni includendole nel nostro programma con la direttiva /COPY, in quanto molto spesso contengono solo la parte "fissa" della DS, lasciando al programmatore l'onere di definirne la parte variabile.
L'API di cui stiamo parlando non fa eccezione a questa regola (vedere QSYSINC/QRPGLESRC,QSQCHKS).

Per definire le DS necessarie alla nostra API è necessario specificare la struttura dei parametri per le DS previste. Si rimanda al membro QSQCHKS in QAPIGEN per il dettaglio delle DS necessarie
per l'utilizzo di questa API.
Per illustrare la struttura di Ds "variabile" frequentemente utilizzata dalla API, ecco nel dettaglio una di queste DS.
>D  SQLOPT                    32767a   Const  Options( *VarSize )          .
                                                                          .
Type Definition for the SQLOPT                                            .
                                                                          .
DQSQTIONS         DS                                                      .
D*                                             Qsq Options                .
D QSQNBROK                1      4B 0                                     .
D*                                             Number Of Keys             .
D*QSQTIONS00              5      5                                        .
D*                             Varying length                             .
                                                                          .
 *----------------------------------------------------------------------- .
D*Type Definition for parte variabile di SQLOPT                           .
 *----------------------------------------------------------------------- .
DQSQVO            DS                                                      .
D*                                             Qsq Vlen Option            .
D QSQK                    1      4B 0                                     .
D*                                             Key                        .
D QSQLVO                  5      8B 0                                     .
D*                                             Length Vlen Option         .


Nell'esempio riportato il parametro SQLOPT è strutturato nel modo seguente : 
 * Numero di opzioni (N) passate
 * Ripetizione di N volte della struttura QSQVO

Per quanto riguarda la DS relativa agli errori si può utilizzare la /COPY APIERROR
 :  : DEC T(MB) P(QAPIGEN) K(APIERROR) O(K)

La /COPY QAPIGEN,QSQCHKS include a sua volta questa /COPY

Dopo il richiamo dell'API, se la variabile AeBytAvl contiene un valore <> di 0, il richiamo dell'API non è avvenuto correttamente.
>N.B. :  Il campo AeBytAvl è definito nella DS degli errori (APIERROR)

Il richiamo avrà pertanto una struttura di questo tipo : 
>C                   CallP     SQLSYNTAX                                   .
C                             ($SQLSTR                                    .
C                              :  %Len($SQLSTR)                            .
C                              :  1                                         .
C                              :  $SQLSTRL                                  .
C                              :  QSQTIONS                                  .
C                              :  QSQSI00                                   .
C                              :  %LEN(QSQSI00)                             .
C                              :  $SQLSTRRN                                 .
C                              :  ApiError)                                 .
C                                                                         .
C                   IF        AeBytAvl=0                                  .
C                   IF        QSQMI00=*BLANKS                             .
C                   ELSE                                                  .
C                   ENDIF                                                 .
C                   ELSE                                                  .
C                   ENDIF                                                 .


E' necessario prestare particolare attenzione nel caso si utilizzino variabili di tipo VARING  (come nell'esempio la variabile $SQLSTR) come parametro di input, con indicazione della lunghezza del parametro passato :  non si dovrà utilizzare la funzione %SIZE, come si farebbe con variabili non varing, ma la funzione %LEN (la funzione %SIZE applicata alla variabile $SQLSTR restituirebbe sempre il valore 32769 (32767 + 2 bytes).
