# UDF (User Defined Functions) SMEUP per SQL

Sono state introdotte alcune UDF (User Defined Function) SQL che permettono l'interrogazione di
alcune /copy all'interno di un'istruzione SQL (sia come campo della select che come condizione
nella where).
Le UDF sono utilizzabili sia da interattivo con STRSQL che in un programma SQLRPGLE che con la
nuova funzionalità UP SQL.
Le /copy attualmente implementate sono : 
**£OAV**
**£DEC**
**£FUN** (consente il lancio di un programma funizzato)

Queste funzionalità sono rivolte principalmente all'installatore, allo sviluppatore o al
responsabile EDP.

Tramite l'utilizzo del TST  della /COPY £SQLF, è possibile ottenere la sintassi per l'esecuzione delle UDF implementate.


# Utilizzo di una UDF per chiamare un programma RPG in una istruzione SQL

Esempio (UDF per la chiamata della £OAV) : 

>CREATE FUNCTION library/£OAV  (
 OAVFUN VARCHAR(10) ,
 OAVTIP VARCHAR(2) ,
 OAVPAR VARCHAR(10) ,
 OAVCOD VARCHAR(15) ,
 OAVATT VARCHAR(15) )
 RETURNS CHAR(35)
 LANGUAGE RPGLE
 SPECIFIC library/£OAV
 NOT DETERMINISTIC
 MODIFIES SQL DATA
 RETURNS NULL ON NULL INPUT
 EXTERNAL ACTION
 ALLOW PARALLEL
 EXTERNAL NAME library/B£UDF_02S
 PARAMETER STYLE DB2SQL



**LANGUAGE : **
Linguaggio in cui è implementato il programma esterno chiamato. Se non specificato assume C.
**SPECIFIC : **
Nome univoco per la funzione. (Utile nel caso di voglia creare più funzioni
con lo stesso nome nella stessa libreria che ricevano differenti parametri :  ad esempio una che
riceva in input una strnga e una che riceva un numerico). In caso non venga specificato, viene
assegnato dal sistema. La chiamata della funzione non può avvenire attraverso il nome specifico,
che può invece essere usato per eseguire il drop della funzione.
**DETERMINISTIC : **
 - NOT DETERMINISTIC :  la funzione non è deterministica (ricevuti gli stessi parametri di input può
   dare differenti risultati
 - DETERMINISTIC :  la funzione è deterministica (ricevuti gli stessi parametri di input restituisce
   gli stessi risultati (es. una funzione che esegue un calcolo matematico)
**SQL : **
 - NO SQL :  la funzione non esegue istruzioni SQL.
 - CONTAINS SQL :  la funzione non esegue istruzioni SQL che leggono o modificano dati.
 - READS SQL DATA :  la funzione non esegue istruzioni SQL che modificano dati.
 - MODIFIES SQL DATA :  permette l'esecuzione di qualunque tipo di istruzione SQL all'interno del
   programma esterno chiamato (ora potremmo usare NO SQL, ma in questo modo non dovremmo ricreare
   la funzione anche includendo comandi SQL nel programma RPG)
**NULL INPUT : **
 - RETURNS NULL ON NULL INPUT :  se riceve input nulli, non viene chiamata e restituisce valore NULL
 - CALLED ON NULL INPUT :  se riceve input nulli, viene chiamata e gli input non validi devono essere
   gestiti dal programma chiamato
**EXTERNAL ACTION : **
 - EXTERNAL ACTION :  la funzione esegue azioni esterne. Viene eseguita ad ogni chiamata.
 - NO EXTERNAL ACTION :  la funzione non esegue azioni esterne. Non necessita di essere eseguita
   ad ogni successiva chiamata.
**PARALLEL : **
 - ALLOW PARALLEL :  significa che lo stesso programma chiamato dall'UDF può essere eseguito in
   molteplici therad. Si applica solo qualora DB2 Symmetric Multiprocessing (SMP) sia installato e
   attivato
 - DISALLOW PARALLEL :  disabilita l'esecuzione parallela (questa opzionedeve essere abilitata se
   l'UDF restituisce una tabella invece che un valore scalare.
**EXTERNAL NAME**
Specifica il programma, programma di servizio o la classe java che sarà eseguito alla chiamata
dell'UDF in un'istruzione SQL. Il nome del programma deve essere qualificato, cioè completo di
libreria).
**PARAMETER STYLE : **
 - SQL
 - DB2SQL
 - GENERAL
 - GENERAL WITH NULLS
 - DB2GENERAL
 - Java

Si prenderà ora in considerazione lo stile **DB2SQL** che può essere utilizzato sia per UDF che
restituiscano un valore scalare cbe per UDF che restituiscano una tabella.

## PARAMETRI OBBLIGATORI
IN parameters (max 90),
OUT result,
IN parameter null indicator (repeated),
OUT result null indicator,
OUT sqlstate,
IN function name,
IN specific name,
OUT diagnostic message,

## PARAMETRI OPZIONALI
INOUT scratchpad,
IN call type,
IN dbinfo

## Esempio di implementazione dei parametri obbligatori nell'entry del programma esterno RPGLE
E' importante definire i parametri di input stringa RPG come VARYING, in modo che nel chiamare la
UDF in SQL non sia necessario che il parametro contenga spazi finali fino a raggiungere la
lunghezza dichiarata.
(Se i parametri non corrispondono il DBMS non riesce a trovare la UDF eseguendo la risalita nelle
librerie)

Nell'entry definiamo i parametri di input (5 come da script di creazione dell'UDF esemplificata),
a cui segue un ulteriore parametro che corrisponde all'output (è la variabile da impostare in
uscita e che la UDF restituirà).
A seguire le variabili degli indicatori di input e di output, del SQLSTATE, del nome e del nome
specifico della funzione e del messaggio (parametri impostati e utilizzati dal DBMS  e non inclusi
nella chiamata dell'UDF in una istruzione SQL)

>     d OAFFUN          s             10    VARYING
     d OAFTP1          s             02    VARYING
     d OAFPR1          s             10    VARYING
     d OAFCD1          s             15    VARYING
     d OAFATT          s             15    VARYING
     d OUTPUT          s             35
     d inpInd          s              5i 0
     d outInd          s              5i 0
     d outSQLState     s              5
     d inpFuncName     s            139    varying
     d inpSpecName     s            128    varying
     d outDiagTxt      s             70    varying


     C     *ENTRY        PLIST
     C                   PARM                    OAFFUN
     C                   PARM                    OAFTP1
     C                   PARM                    OAFPR1
     C                   PARM                    OAFCD1
     C                   PARM                    OAFATT
     C                   PARM                    OUTPUT
     c                   parm                    inpInd
     c                   parm                    outInd
     c                   parm                    outSQLState
     c                   parm                    inpFuncName
     c                   parm                    inpSpecName
     c                   parm                    outDiagTxt


## Esempio di chiamata della UDF
>      SELECT FunctionName(parinput1, parinput2, ..., parinputN) FROM File

      SELECT A§ARTI, £OAV('VAL', 'AR', A§TIAR, A§ARTI, 'I/05') AS Attributo,
      FROM BRARTI0F


**Una UDF viene eseguita nello stesso Job del programma chiamante, ma in un differente Thread.**




# Come implementare una UDF personalizzata

- Creare un programma SQLRPGLE B£UDF_xxS che verrà eseguito dall'UDF a partire dal sorgente di esempio B£UDF_XXSE.
- Creare un programma contenente le istruzioni SQL di drop e create dell'UDF a partire dal sorgente di esempio B£UDF_CXE.
- Modificare le istruzioni di PRP e POP in testa al programma B£UDF_xxS sostituendo B£UDF_XXS con il nome del programma da eseguire e B£UDF_CX con il nome del programma contenente le istruzioni SQL di drop e create dell'UDF.
- Compilare il programma contenente le istruzioni SQL di drop e create dell'UDF
- Compilare il programma B£UDF_xxS


**La compilazione del programma B£UDF_xxS comporterà in modo automatico il drop e il create dell'UDF rispettivamente prima e dopo la compilazione nella stessa libreria di destinazione
della compilazione del pgm.

## Salvataggio e ripristino di una UDF
Per il corretto funzionamento delle operazioni di ripristino di un'UDF il programma eseguito nell'UDF deve esistere al momento della creazione dell'UDF. Il ripristino dell'UDF avverrà quindi automaticamente al ripristino dell'oggetto del PGM. Questa condizione è automaticamente soddisfatta dalla creazione dell'UDF tramite le istruzioni di post-compilazione comprese nei programmi B£UDF_xxS


## Integrazione della costruzione della sintassi di chiamata dell'UDF tramite la /copy £SQLF : 

- Aggiungere un oggetto V3 PUF corrispondente alla UDF personalizzata implementata
- Creare un programma  B£UDF_xx contenente la gestione della costruzione della sintassi di chiamata dell'UDF. Tale programma deve comprendere 2 metodi :  un metodo G per la costruzione guidata tramite G30 e un metodo blank per la costruzione senza emissione del file video di guida, utilizzato nei programmi del modulo EQRY.





