## STRSQL
Per eseguire una query SQL su A/400, richiamare da linea comandi : 
>STRSQL


### Istruzione SELECT
L'istruzione SELECT consente la selezione dei campi che si desidera visualizzare di uno o più file.

**Sintassi : **
>SELECT *|nomecampo, nomecampo,... FROM file

Dopo l'operatore SELECT vengono indicati i campi da visualizzare, mentre dopo l'operatore FROM i file da cui recuperare i dati.

Per la selezione di tutti i campi di un file si utilizza la parola chiave *****. Es. : 
>SELECT * FROM BRENTI0F

Esegue la selezione di tutti i campi del file dell'anagrafica enti.


In alternativa, è possibile specificare il nome dei campi da visualizzare separati da virgola. Es. : 
>SELECT E§TRAG, E§CRAG FROM BRENTI0F

Esegue la selezione dei campi tipo e codice del file dell'anagrafica enti.

### Limitare il numero di record restituiti
>FETCH FIRST _ n _ ROW ONLY

_ n _ indica il numero di record da restituire
>SELECT  *   FROM BRENTI0F
WHERE E§TRAG = 'COL'
ORDER BY E§RAGS
 FETCH FIRST 10 ROW ONLY

Seleziona i primi 10 collaboratori in ordine di ragione sociale dall'anagrafica enti.

### Count() e Distinct
Vediamo l'utilizzo della funzione COUNT per contare il numero di record selezionati : 
>SELECT cdnaz, COUNT(cdnaz) FROM Clienti GROUP BY Cdnaz

In questo caso vengono ritornati il codice nazione e il numero di clienti della stessa nazione.

La parola chiave DISTINCT esclude i risultati duplicati della SELECT-
Se volessimo sapere quante nazioni **diverse** abbiamo nel file clienti : 
>SELECT COUNT(DISTINCT(Cdnaz)) FROM Clienti


Un altro metodo è : 
>SELECT COUNT(*) FROM (SELECT DISTINCT(Cdnaz, Cdpag) FROM Clienti) as PIPPO

Attenzione :  questa istruzione funziona solo dalla versione V4R4 in avanti.

### Alias su nomi di campi (Operatore AS per intestazioni di campo)
Quando si esegue una select a video, le intestazioni delle colonne sono le descrizioni COLHDG dei campi del file.
Nel caso non sia presente COLHDG, viene usato il nome del campo. E' possibile visualizzare un'intestazione a piacere, utilizzando la parola chiave AS : 
SELECT Codcli AS "Codice Cliente" FROM Clienti ....

Per cose più complesse è possibile ricorrere al Query Manager STRQM, con il quale è possibile separare la parte SQL da quella di output.

### JOIN di file
Un'operazione di JOIN consente la selezione di record in due tabelle collegate.

Si distinguono 3 tipi di JOIN : 

### INNER JOIN
L'INNER JOIN consente la selezione dei soli record che hanno una corrispondenza in entrambi i file specificati.

Es. :  Se voglio fare una join su record dello stesso file si possono utilizzare gli alias : 
>SELECT * FROM C5TREG0F AS T1, C5TREG0F AS T2 WHERE T1.T5PROG=T2.T5PROG


L'istruzione sopra specificata è equivalente a : 
>SELECT * FROM C5TREG0F AS T1
INNER JOIN C5TREG0F AS T2
ON T1.T5PROG=T2.T5PROG


La parola chiave INNER può anche essere omessa : 
>SELECT * FROM C5TREG0F AS T1
JOIN C5TREG0F AS T2
ON T1.T5PROG=T2.T5PROG


### LEFT JOIN
Il LEFT JOIN consente la selezione di tutti i record del primo file e di quelli corrispondenti nel secondo.

È anche possibile utilizzare il LEFT JOIN per farsi restituire i record non corrispondenti con una condizione nella WHERE in cui il campo su cui si esegue il join sia NULL.
Es. : 
>SELECT ATTROBJECTS.OBJATTRDESCRIPTION,OBJTYPE, DOCUMENTS.*
FROM ATTROBJECTS
LEFT JOIN DOCUMENTS
ON ATTROBJECTS.OBJCODE=DOCUMENTS.OBJCODE
WHERE DOCUMENTS.OBJCODE IS NULL


### RIGHT JOIN
Il RIGHT JOIN consente la selezione di tutti i record del secondo file e di quelli corrispondenti nel primo.

### Alias su file (Operatore AS)
NELLE JOIN FRA FILE CON GLI STESSI CAMPI VA SEMPRE MESSO 'AS' SU TUTTI
I FILE ALTRIMENTI SI HANNO COMPORTAMENTI ANOMALI ANCHE NON SEGNALATI.
(Es. :  una Where EXISTS fatta su un file ridenominato e l'altro no ha sempre risultati positivi).

### Operatore GROUP BY e funzioni di aggregazione
L'operatore GROUP BY consente l'aggregazione di record raggruppati in base all'elenco dei campi specificati.

>SELECT E§TRAG, E§CRAG, E§RAGS FROM BRENTI0F
GROUP BY E§TRAG, E§CRAG, E§RAGS

Seleziona i record dell'anagrafica enti raggruppandoli per tipo, codice, ragione sociale.

L'utilizzo del GROUP BY è associato a quello di **funzioni di aggregazione** (ad esempio **COUNT()** per il conteggio, **AVG()** per eseguire la media su un campo, **SUM()** per sommare i valori di un campo, **MAX()** e **MIN()** per farsi restituire rispettivamente il valore massimo e minimo, ecc...)

Se da un file statistico, ad esempio le righe di vendita, si volessero ottenere i subtotali per nazione e quindi il totale generale come con Query/400 : 
>SELECT NAZI, COUNT(*), SUM(FATT) FROM STATIS0F
 GROUP BY NAZI
 UNION ALL
 SELECT '999 TOTALE', COUNT(*), SUM(FATT)
 FROM STATIS0F GROUP BY '999 TOTALE'
 ORDER BY 1


Si supponga di avere una tabella con lo storico delle vendite degli ultimi n anni, in cui ogni record rappresenta una riga di bolla/fattura con cliente, articolo, quantità, data consegna, ecc... e si desidera  calcolare la media (anno x anno) delle righe consegnate per ogni giorno : 
>SELECT ANNO, AVG(COUNTGIO) AS MEDIAANNO
FROM (Select substring(char(DATACONS),1, 4) as ANNO, DATACONS, COUNT(*) as COUNTGIO
from STORICO group by substring(char(DATACONS),1, 4), DATACONS) as storico group by ANNO order by ANNO


Correlato all'operatore GROUP BY, vi è l'operatore **HAVING**, che consente di **filtrare i record di un raggruppamento.
Es. :  per selezionare un conteggio degli enti per tipo escludendo i tipi per i quali è presente un solo record,  utilizzare il parametro HAVING : 
>SELECT E§TRAG,  Count(*)  FROM BRENTI0F
GROUP BY E§TRAG
HAVING count(*)>1


### Operatore WHERE
L'operatore WHERE consente di filtrare i record selezionati (SELECT), inseriti (INSERT), aggiornati (UPDATE) ed eliminati (DELETE) in base alle condizioni specificate dopo di esso.
Le condizioni di selezione sono delle espressioni booleane.
 :  : PAR F(01)
Nel caso le condizioni riguardino campi di tipo stringa, è importante ricordare che i valori sono _case sensitive._

 :  : PAR
Per ovviare a questo problema fare riferimento alle funzioni descritte nel paragrafo relativo alle _Operazioni sulle stringhe._


**Sintassi : **
>SELECT * FROM nometabella1 WHERE nomecolonna1='Valore1' AND nomecolonna2='Valore2'

Es. : 
>SELECT * FROM BRENTI0F WHERE E§TRAG = 'COL'


Gli operatori matematici disponibili sono i seguenti : 

- = :  uguale;
- < :  minore;
- > :  maggiore;
- <> :  diverso (maggiore o minore);
- <= :  minore o uguale;
- >= :  maggiore o uguale.


È possibile utilizzare più criteri assieme attraverso gli operatori logici : 

- AND :  le due condizioni implicate devono essere entrambe vere perché la riga venga considerata;
- OR :  almeno una delle due condizioni deve essere vera perché la riga venga considerata;
- NOT :  restituisce la riga solo se la condizione implicata non è vera;


### Operatore LIKE

**Sintassi : **
>SELECT campi
FROM nomefile
WHERE campo LIKE ricerca


Es. : 
>SELECT *
FROM BRENTI0F
WHERE E§RAGS LIKE '%ANNA%' ;


L'operatore LIKE utilizza due tipi di **caratteri jolly** per verificare le uguaglianze parziali. I due caratteri sono il simbolo percento '%' e l'underscore '_'. Il primo carattere jolly sostituisce un insieme di caratteri, il secondo si limita a sostituirne uno solo .

    - inizia per a  --> CAMPO LIKE 'A%'
    - finisce per a --> CAMPO LIKE '%A'
    - contiene a    --> CAMPO LIKE '%A%'

>SELECT RAGSOC
FROM CLIENTI
WHERE RAGSOC LIKE 'COOPERATIVA%'

Estrae tutti i clienti con Ragione Sociale che inizia con COOPERATIVA

>SELECT RAGSOC
FROM CLIENTI
WHERE RAGSOC LIKE 'P_PPO'

Estrae tutti i clienti con Ragione Sociale PIPPO,POPPO,PAPPO ecc.

>SELECT RAGSOC
FROM CLIENTI
WHERE STRIP(RAGSOC, TRAILING) LIKE '%SPA'

**Utilizzando l'operatore LIKE, l'SQL considera i campi per l'intera loro lunghezza (se voglio tutte le SPA mie clienti devo togliere con la funzione STRIP() i blank finali).
L'operatore = , al contrario, non considera i blank finali.

Definendo come escape il carattere punto esclamativo posso effettuare una ricerca che  seleziona tutti i clienti con il carattere Underscore nella Ragione Sociale. Es : 
>SELECT *
FROM BRENTI0F
WHERE E§RAGS LIKE '%!_%' Escape '!'


### Operatore BETWEEN
Per specificare un range di valori si puo' ricorrere all'operatore BETWEEN. Es. : 
>SELECT RAGSOC
FROM CLIENTI
WHERE FATTU2001 BETWEEN 1000000 AND 5000000

Per selezionare tutti i clienti con il fatturato tra 1.000.000 e 5.000.000


### Operatore IN / NOT IN
Il predicato SQL IN puo' essere usato per indicare una lista di valori consentiti in una condizione oppure per sfruttare delle subquery SQL : 
>SELECT *
FROM Clienti
WHERE Pagam IN ('100', '101', '300', '301')

oppure
>SELECT *
FROM Clienti
WHERE Pagam IN (Select cod from Pagamenti where tipo='RB')

Per estrarre solo i clienti con alcuni codici pagamento o con un pagamento di tipo Ricevuta Bancaria.

### Operatore EXISTS / NOT EXISTS

EXISTS usa una subquery come condizione :  la condizione è Vera se la subquery ritorna almeno una riga, ed è Falsa se la subquery non ritorna nessuna riga.

**Sintassi : **
>SELECT columns
FROM tables
WHERE EXISTS ( subquery )

Nell'esempio seguente, per ogni dipendente presente nella tabella Employees vengono individuati nella tabella Orders tutti gli ordini che contengono "Washington" nel campo ShippingRegion.
>SELECT * FROM Orders WHERE ShipRegion = 'WA'
AND EXISTS (SELECT EmployeeID FROM Employees AS Emp WHERE Emp.EmployeeID = Orders.EmployeeID)


L'operatore EXISTS può essere utilizzato anche in un'istruzione di UPDATE, DELETE o INSERT.

### Instruzione INSERT
L'istruzione INSERT permette di inserire dei record in un file : 

**Sintassi : **
>INSERT INTO File (NomeCampo1, NomeCampo2, NomeCampo3) VALUES ('Valore1', 'Valore1', 'Valore3')


È anche possibile inserire dei record in un file selezionandoli da un altro : 

**Sintassi : **
>INSERT INTO LibreriaDestinazione/FileDestinazione
SELECT * FROM LibreriaOrigine/FileOrigine WHERE Condizione


### Istruzione UPDATE
Per aggiornare i record di un file : 
**Sintassi : **
>UPDATE NomeFile SET NomeCampo1=ValoreCampo1, NomeCampo2=ValoreCampo2 (WHERE Condizione)


Esempio di aggiornamento di una tabella con un campo preso da un'altra tabella
**Sintassi : **
>UPDATE LIB1/FILE1 A
SET A.CAMPO1=(SELECT CAMPO1 FROM LIB1/FILE2
WHERE CAMPO2=A.CAMPO2 AND CAMPO3=A.CAMPO3 AND CAMPO4=A.CAMPO4)


### Istruzione DELETE
L'operatore DELETE consente di cancellare fisicamente i record di un file : 

**Sintassi : **
>DELETE FROM NomeFile (WHERE Condizione)


### Gestione file multimembro
Se si vuole usare un file multimembro nell'SQL prendendo in considerazione un particolare membro, è necessario seguire la seguente procedura : 
 * fare una prima istruzione SQL che crea un ALIAS del membro : 
>CREATE ALIAS nomealias FOR nomefile (nomemembro)

 * eseguire tutte le operazioni SQL che si vogliono fare sul membro usando come nome del file l'alias
 * eseguire come ultima operazione la cancellazione dell'alias : 
>DROP ALIAS nomealias

Quest'ultima operazione è importante in quanto l'alias è di fatto un file.

### Esportazione dei risultati di una query in un file
CPYF tramite sql :  fare F13 dalla linea comandi SQL --> opzione 1 (Change session attributes), alla voce "SELECT output" mettere 3 (=File) invece che 1 (=Display), dare invio e scrivere il file e la libreria di destinazione, nonchè l'opzione di copia. A questo punto, facendo una select su un file, tutti i record selezionati verranno scritti sul file selezionato nell'F13 e non esplosi a video.

**ATTENZIONE :  DOPO L'OPERAZIONE BISOGNA RICORDARSI DI RIPRISTINARE L'F13 CON "SELECT output" A 1**

### Creazione di viste logiche
Con SQL è anche possibile creare delle viste logiche (LF) su un File Fisico (PF) : 
>CREATE INDEX liblogico/filelogico
ON libfisico/filefisico (chiave1, chiave2, ecc..)


### Operazioni sulle stringhe
### Funzione SUBSTR
Per estrapolare delle sottostringhe : 
>SELECT SUBSTR(RAGSOC, 1, 25)
FROM CLIENTI

 :  : PAR
Per leggere solo i primi 25 caratteri della Ragione Sociale


**Update di un campo con la sottostringa di un'altro campo : **
>update file set  a=substr(b, x, y)


 :  : PAR
dove x sta per la pos.iniziale e y il n° di caratteri da prendere

**Modificare una sottostringa di un campo**

Se volessimo modificare una sottostringa di un campo, non potremmo usare un update set substr(...), ma una sintassi di questo tipo : 
>update FILE set CAMPO='xxxxx' concat substr(CAMPO, 6) where substr(CAMPO, 1, 5)= 'yyyyy'


### Funzione CONCAT
Per concatenare 2 campi stringa bisogna ricorrere al CONCAT : 
>SELECT COUNT(DISTINCT(CONCAT(Cdnaz,Cdpag))) FROM Clienti

equivalente a
>SELECT COUNT(DISTINCT Cdnaz CONCAT Cdpag) FROM Clienti

Se avessimo un campo numerico potremmo usare DIGITS(campo) all'interno del CONCAT.

**Update di un campo concatenando due campi**
>update file set  a=b concat c


### Trasformazione MAIUSCOLE/minuscole
Per effettuare la traformazione dei valori di un campo in caratteri solo maiuscoli, si utilizza la funzione **UPPER()** oppure **UCASE().**
Per effettuare la traformazione in caratteri solo minuscoli, utilizzare **LOWER()** o **LCASE().**
Es. : 
>SELECT * FROM BRENTI0F
WHERE lower(E§RAGS) LIKE 'a%'
ORDER BY E§RAGS

Esegue la selezione di tutti gli enti la cui ragione sociale cominci per 'a', indipendentemente se maiuscola o minuscola. Si noti che la funzione lower() agisce solo sulla condizione, non modifica la visualizzazione dei valori dei campi selezionati. Si evidenza anche che, qualora la condizione fosse stata _LIKE 'A%'_, non sarebbe stato restituito alcun risultato, in quanto la condizione della where è _case sensitive._

### Rimozione degli spazi (TRIM / LTRIM / RTRIM)
La funzione **TRIM()** rimuove gli eventuali spazi (blank)_ iniziali e finali**di una stringa.
La funzione **LTRIM()** rimuove invece i soli spazi iniziali, mentre **RTRIM()** i soli spazi finali.

### Campi stringa contenenti un valore con l'apice
Può creare qualche problema la selezione di campi con il valore contenente il carattere apice, ad esempio, se sulla nostra tabella clienti dovessimo selezionare quelli con Cognome D'Amato : 
>SELECT * FROM CLIENTI
 WHERE COGNOME = 'D''AMATO'

Per evitare che l'apostrofo interno al valore venga rilevato dal database come la chiusura della stringa, è necessario utilizzare 2 apici.

### Operazioni sui numerici
### Conversione di numeri in stringhe
Per confrontare variabili alfanumeriche e numeriche ci sono diverse modalità : 
>alfa = char(numerica)
alfa = DIGITS(numerica)


### Arrotondamenti con SQL
La funzione TRUNC(nomecampo, _n _) o TRUNCATE(nomecampo, _n _) arrotonda sempre per difetto, mentre la funzione ROUND(nomecampo, _n _) arrotonda con la regola dello 0,5 (al giusto).
>SELECT  TRUNCATE(873.726, 2),
        TRUNCATE(873.726, 1),
        TRUNCATE(873.726, 0),
        TRUNCATE(873.726, -1),
        TRUNCATE(873.726, -2),
        TRUNCATE(873.726, -3)
FROM TABLEX

Questo esempio restituisce : 
0873.720 0873.700 0873.000 0870.000 0800.000 0000.000
>SELECT  ROUND(873.726, 2),
        ROUND(873.726, 1),
        ROUND(873.726, 0),
        ROUND(873.726, -1),
        ROUND(873.726, -2),
        ROUND(873.726, -3),
        ROUND(873.726, -4)
FROM TABLEX

Questo esempio restituisce : 
0873.730 0873.700 0874.000 0870.000 0900.000 1000.000 0000.000

### Divisione e problemi con gli Integer
Se in un'istruzione SQL eseguiamo una divisione fra due numeri interi, il risultato viene presentato come intero e quindi senza virgole. Per risolvere il problema si può usare DEC() oppure : 
>SELECT DEC(a)/dec(b) AS C from Tabel
SELECT 1.0*A/B AS C from TABEL


### Operazioni sulle date
Se ho un campo di tipo data in un file posso fare anche delle operazioni di questo tipo : 
>select (CURRENT DATE - Datacreaz) Giorni, CURRENT DATE , Datacreaz from Miofile

In questo caso, però, il risultato del campo Giorni è nel formato YYYYMMDD, quindi un risultato 210 significa 2 mesi e 10 giorni .... un po' scomodo.

Un metodo migliore per calcolare il numero di giorni è il seguente : 
>SELECT (days(CURRENT DATE) - days(Datacreaz)) Giorni, CURRENT DATE , Datacreaz FROM Miofile


Estrarre il numero della settimana con SQL
>select week(date('31.12.2002')) from file --> 53
select week_iso(date('31.12.2002')) from file --> 01


### Funzione RRN()
E' possibile anche ottenere il numero relativo di record con un'istruzione SQL : 
>SELECT RRN(nomefile)
FROM nomefile
WHERE campo = 'valore'

Supponiamo di avere un file di movimenti contabili e di voler rigenerare il campo numero movimento seguendo una nuova numerazione :  prendendo il file movimenti ACG MOAZ200F e il campo NUMOV, vogliamo fare in modo che tutti i movimenti presenti nel file vengano rinumerati dal numero 1.000.000 in avanti : 
>UPDATE moaz200f SET numov=1000000+RRN(moaz200f)


### Campi condizionati :  CASE, WHEN, ELSE, END
Supponiamo di voler estrarre da un file di righe ordini cliente con la data ancora nel formato AAMMGG, la stessa data nel formato AAAAMMGG : 
Nome del file OCRIG00F
Campi :  NRRER=Numero ordine , DTCCR=Data consegna AAMMGG
>SELECT NRRER, CASE WHEN DTCCR=0 THEN 0
WHEN SUBSTR(DIGITS(DTCCR), 1, 2) = '00' THEN 20000000+DTCCR
ELSE 19000000+DTCCR
END
AS DATADAOTTO
FROM OCRIG00F

In questo caso viene considerata anche la possibilità che la data sia zero.

**ORDINAMENTO PER DUE CAMPI ALTERNATI**

Es. :  Ordino in modo alternativo per R§DTCR, se maggiore 20070101 o data inserimento
    se la R§DTCR è <=20070101
>    SELECT r§tdoc, r§ndoc ,
    case when R§dtcr>20070101 then r§DTCR else R§DTin
    end as data3 FROM v5rdoc0f ORDER BY DATA3


## File di sistema
SELECT * FROM SYSCOLUMNS = da le definizione di tutti i campi di tutti i file del sistema
SELECT * FROM SYSTABLES  = da le definizione di tutte le tabelle di sistema

## Utilizzo di un cursore per la lettura di dati in SQLRPGLE
Il recupero dei dati tramite SQL in SQLRPGLE avviene attraverso l'utilizzo di un cursore.
Le operazioni necessarie per la lettura di record con un cursore sono le seguenti : 
 * **DECLARE** :  dichiarazione di un cursore
 * **PREPARE** :  preparazione di una istruzione SQL eseguibile a partire da una variabile stringa
 * **OPEN** :  apertura del cursore
 * **FETCH** :  spostamento tra i record risultanti
 * **CLOSE** :  chiusura del cursore

Le istruzioni SQL embedded in un membro di tipo SQLRPGLE sono comprese tra un'istruzione di apertura C/EXEC SQL e una di chiusura C/END-EXEC e sono caratterizzate da un tipo riga C+.
>      C/EXEC SQL
      C+ ...
      C/END-EXEC


**N.B.** :   Le istruzioni SQL non possono andare oltre la posizione 80 nel codice del programma.

All'interno delle istruzioni SQL embedded è possibile fare riferimento a variabili host definite in RPGLE. Nell'esempio sotto riportato, nell'istruzione SQL si fa riferimento alla variabile RPG SelectStm, facendo precedere il nome della variabile da ' : '. E' importante ricordare che non è possibile utilizzare nei nomi delle variabili host caratteri speciali (come £), in quanto viene generato un errore del precompilatore SQL. Inoltre, nomi di variabili che iniziano con SQ , SQL e DNS sono da considerarsi riservati all'uso del DBMS.
>      D SelectStm       S            200    INZ
       *
      C                   EVAL      SelectStm='SELECT A§ARTI FROM BRARTI0F'
       *
      C/EXEC SQL
      C+ PREPARE S1 from  : SelectStm
      C/END-EXEC


Si distinguono due tipi di cursore : 
 * **SERIAL CURSOR** (supporta soltanto lo spostamento in avanti di un record alla volta);
 * **SCROLLABLE CURSOR** (consente lo spostamento avanti e indietro all'interno dei record risultanti dall'apertura del cursore).

### Serial cursor
Questo tipo di cursore supporta soltanto lo spostamento in avanti di un record alla volta.

### Declare
Il cursore è definito come : 
>      C/EXEC SQL
      C+ DECLARE C1 cursor for S1
      C/END-EXEC

Dove C1 è il nome del cursore e S1 è l'istruzione SQL resa eseguibile tramite l'istruzione PREPARE.

### Prepare
Prepara un'istruzione SQL eseguibile a partire da una variabile stringa : 
>      C/EXEC SQL
      C+ PREPARE S1 from  : SelectStm
      C/END-EXEC

Dove S1 è l'istruzione SQL resa eseguibile e SelectStm è la variabile host stringa che contiene l'istruzione SELECT SQL da eseguire.

### Open
>      C/Exec SQL
      C+                  OPEN C1
      C/End-Exec

Dove C1 è il nome del cursore da aprire.
Quando il cursore viene aperto, è posizionato prima della prima riga nella tabella dei risultati.

### Fetch
Questo tipo di cursore supporta soltanto lo spostamento in avanti di un record alla volta, tramite l'istruzione FETCH.
Una volta raggiunta la fine dei dati (SQLCOD=100) è necessario chiudere e riaprire il cursore per accedere nuovamente ai dati.
>      C/Exec SQL
      C+                  FETCH              C1
      C+                    INTO  : HostVariable
      C/End-Exec

Se sono specificate variabili host (tramite un elenco di singole variabili separate da virgola oppure tramite una DS) con la clausola INTO, SQL esegue lo spostamento dei valori della riga corrente nelle variabili host del programma.
In RPG, un array è una DS a ricorrenze multiple (OCCURS). Un array può essere referenziato in una istruzione FETCH soltanto quando si esegue la fetch multipla (di più righe), o in un'istruzione INSERT quando si esegue una insert a blocchi.

### Close
>      C/EXEC SQL
      C+ CLOSE C1
      C/END-EXEC

Dove C1 è il nome del cursore da chiudere.

### Scrollable cursor
Questo tipo di cursore consente lo spostamento avanti e indietro all'interno dei record risultanti dall'apertura del cursore.

### Declare
Il cursore è definito con l'utilizzo della parola chiave SCROLL : 
>      C/EXEC SQL
      C+ DECLARE C1 SCROLL cursor for S1
      C/END-EXEC

Dove C1 è il nome del cursore e S1 è l'istruzione SQL resa eseguibile tramite l'istruzione PREPARE.

### Prepare
Prepara un'istruzione SQL eseguibile a partire da una variabile stringa : 
>      C/EXEC SQL
      C+ PREPARE S1 from  : SelectStm
      C/END-EXEC

Dove S1 è l'istruzione SQL resa eseguibile e SelectStm è la variabile host stringa che contiene l'istruzione SELECT SQL da eseguire.

### Open
>      C/Exec SQL
      C+                  OPEN C1
      C/End-Exec

Dove C1 è il nome del cursore da aprire.
Quando il cursore viene aperto, è posizionato prima della prima riga nella tabella dei risultati.

### Fetch
Questo tipo di cursore consente lo spostamento avanti e indietro all'interno dei record risultanti dall'apertura del cursore in base all'opzione specificata per l'istruzione FETCH.
Una volta raggiunta la fine o l'inizio dei dati (SQLCOD=100)* non è necessario chiudere e riaprire il cursore per accedere nuovamente ai dati.
Se sono specificate variabili host (tramite un elenco di singole variabili separate da virgola oppure tramite una DS) con la clausola INTO, SQL esegue lo spostamento dei valori della riga corrente nelle variabili host del programma.
In RPG, un array è una DS a ricorrenze multiple (OCCURS). Un array può essere referenziato in una istruzione FETCH soltanto quando si esegue la fetch multipla (di più righe) o in un'istruzione INSERT quando si esegue una insert a blocchi.

*** NOTA : ** _ SQLCOD, SQLERM e SQLSTATE** sono variabili RPG dichiarate automaticamente dal compilatore e accessibili nelle specifiche RPG.
Es. : 
>     C                   IF        SQLCOD=100
     C                   LEAVE
     C                   ENDIF


_1_Opzioni per l'istruzione Fetch
 * **NEXT** :   Posiziona il cursore sulla riga successiva (è l'opzione predefinita se nessuna opzione è specificata)
>      C/Exec SQL
      C+                  FETCH    NEXT
      C+                    FROM   C1
      C+                    INTO  : HostVariable
      C/End-Exec

 * **PRIOR** :  Posiziona il cursore sulla riga precedente
>      C/Exec SQL
      C+                  FETCH    PRIOR
      C+                    FROM   C1
      C+                    INTO  : HostVariable
      C/End-Exec

 * **FIRST** :  Posiziona il cursore sulla prima riga
>      C/Exec SQL
      C+                  FETCH    FIRST
      C+                    FROM   C1
      C+                    INTO  : HostVariable
      C/End-Exec

 * **LAST** :   Posiziona il cursore sull'ultima riga
>      C/Exec SQL
      C+                  FETCH    LAST
      C+                    FROM   C1
      C+                    INTO  : HostVariable
      C/End-Exec

 * **BEFORE** :  Posiziona il cursore prima della prima riga
>      C/Exec SQL
      C+                  FETCH     BEFORE
      C+                    FROM   C1
      C/End-Exec

>N.B. :  Non è possibile specificare variabili host con la clausola INTO per l'opzione BEFORE.
 * **AFTER** :  Posiziona il cursore dopo l'ultima riga
>      C/Exec SQL
      C+                  FETCH     AFTER
      C+                    FROM   C1
      C/End-Exec

>N.B. :  Non è possibile specificare variabili host con la clausola INTO per l'opzione AFTER.
 * **CURRENT** :  Esegue la rilettura della riga corrente
>      C/Exec SQL
      C+                  FETCH    CURRENT
      C+                    FROM   C1
      C+                    INTO  : HostVariable
      C/End-Exec

 * **RELATIVE** :  Esegue il posizionamento (in base al numero specificato in una variabile host di tipo integer) in relazione al record corrente del cursore.
 Ad esempio, se il valore della variabile host RecNum è -1, il cursore si posiziona sulla riga precedente rispetto alla riga corrente del cursore. Se RecNum è +3, il cursore si posiziona in avanti di 3 righe tra i risultati rispetto alla riga corrente.
Specificare RecNum uguale a 0 è equivalente all'utilizzo dell'opzione CURRENT.
>      C/Exec SQL
      C+                  FETCH    RELATIVE  : RecNum
      C+                    FROM C1
      C+                    INTO  : HostVariable
      C/End-Exec


### Close
>      C/EXEC SQL
      C+ CLOSE C1
      C/END-EXEC

Dove C1 è il nome del cursore da chiudere.

## Accorgimenti relativi alle performance
### File fisici e logici
E' **preferibile utilizzare nelle istruzioni SQL riferimenti ai file fisici**, piuttosto che ai file logici.
Infatti, con i file fisici l'ottimizzazione delle query viene affidata a partire dalla V5R2 al SQE (SQL Query Engine), che è più performante e che farà automaticamente uso dell'indice e (quindi del logico) più adatto.
In caso contrario verrà invece utilizzato il vecchio CQE (Classic Query Engine), le cui prestazioni sono nettamente inferiori.
