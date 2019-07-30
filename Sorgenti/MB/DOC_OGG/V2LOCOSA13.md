 :  : HEA RESP(BMA) STAT(10)

# DESCRIZIONE GENERALE
Il LOA13 esegue un'istruzione sql di select emettendo i record risultanti in matrice.
L'istruzione eseguita può : 

- Essere ricevuta nell' INPUT del servizio
- Essere ricavata in base agli oggetti ricevuti dal servizio
- Leggere l'istruzione in una £G00 la cui chiave è passata nel K3 del servizio

La modalità principale è la ricezione di un sql nell' INPUT.


## Cosa avviene se vengono passati degli oggetti?


### Caso 1 :  Viene passato un Q3 nell'oggetto 1 e non vi è un sql nell' INPUT
es. F(EXB;LOA13_SE;ESE.SQL) 1(Q3;IDBRARTI0F;E/*JOB)
Il servizio costruisce un sql a partire dall'oggetto ricevuto, quindi assume un select * sul file di riferimento dell'oggetto e costruisce la where in base a quanto presente nel Q3 indicato.


### Caso 2 :  Viene passato un Q3 nell'oggetto 1 e vi è un sql nell' INPUT
es. F(EXB;LOA13_SE;ESE.SQL) 1(Q3;IDBRARTI0F;E/*JOB) INPUT(SELECT * FROM BRARTI0F WHERE A§TIAR='[K1]')
Il servizio utilizza l'sql ricevuto nell' INPUT , accodando alla where eventualmente presente nell'istruzione ulteriori campi indicati nel Q3.
In questo caso l' sql passato nell'input sia essere un select * che specificare dei campi, in quanto il Q3 si limita a "completare" la where.


### Caso 3 :  Viene passato un Q2 nell'oggetto 4 e non vi è un sql nell' INPUT
es. F(EXB;LOA13_SE;ESE.SQL) 1(Q3;IDV5STAT0F;E/*JOB) 4(Q2;IDV5STAT0F;T/DFT)
Il servizio costruisce la select in base ai campi presenti nel Q2 e costruisce la where in base a quanto presente nel Q3 eventualmente indicato. I setup di matrice presenti nel Q2 vengono utilizzati.


### Caso 4 :  Viene passato un Q2 nell'oggetto 4 e vi è un sql di tipo "SELECT * FROM"  nell' INPUT
es. F(EXB;LOA13_SE;ESE.SQL) 1(Q3;IDV5STAT0F;E/*JOB) 4(Q2;IDV5STAT0F;T/DFT) P( NRW(500)) INPUT(SELECT * FROM V5STAT0F WHERE D6TDOC='[TIPDOC]' AND D6TRIG='[TIPRIG]' AND D6CDCL='[CLIENT]'  ORDER BY D6DT03 DESC)
Il servizio costruisce la select in base ai campi presenti nel Q2 e accoda alla where eventualmente presente nell'istruzione ulteriori campi indicati nell'eventuale Q3.
I setup di matrice presenti nel Q2 vengono utilizzati.

Esempio di SQL eseguito : 
SELECT D6TIPC, D6TPOG, D6PEPR, D6TDOC, D6NDOC, D6NBOL, D6DBOL, D6NFAT, D6DFAT, D6COMM, D6CDOG, D6DESC, D6COD1, D6COD2, D6COD3, D6COD4, D6COD5, D6COD6, D6COD7, D6COD8, D6COD9, D6COD0, D6DTAG, D6ORAG, RRN(V5STAT0F)  FROM V5STAT0F WHERE D6TDOC='FAT' AND D6TRIG='ART' AND D6CDCL='000001'  AND   D6AZIE='01' ORDER BY D6DT03 DESC


### Caso 5 :  Viene passato un Q2 nell'oggetto 4 e vi è un sql con un elenco di campi specificati  nell' INPUT
es. F(EXB;LOA13_SE;ESE.SQL) 1(Q3;IDV5STAT0F;E/*JOB) 4(Q2;IDV5STAT0F;T/DFT) P( NRW(500)) INPUT(SELECT D6TIPC, D6TDOC, D6NDOC FROM V5STAT0F WHERE D6TDOC='FAT' ORDER BY D6DT03 DESC)
Il servizio ignora completamente il Q2, sia relativamente all'elenco dei campi che ai setup di matrice associati e usa l'sql ricevuto nell'input accodando alla where eventualmente presente nell'istruzione ulteriori campi indicati nell'eventuale Q3.

Esempio di SQL eseguito : 
SELECT D6TIPC, D6TDOC, D6NDOC , RRN(V5STAT0F) AS $_RRN FROM V5STAT0F WHERE D6TDOC='FAT'  AND   D6AZIE='01' ORDER BY D6DT03 DESC


_2_I Q2 DI TIPO T/ SUPPORTATI SONO DEFINITI IN SCP_NAV COME INDICATO NELLA PTF LO00901A.

## Modalità di chiamata
L'**istruzione select SQL** da eseguire viene passata al servizio nell' **INPUT()** .

In alternativa è possibile salvare l'istruzione select SQL da eseguire nella £G00 : 
>C                   EVAL      £G00FU='OUT'
C                   EVAL      £G00TS=[nome G00]
C                   EVAL      £G00RE=[istruzione SQL]         .
C                   EXSR      £G00

e passare il nome utilizzato per scrivere la £G00 nel K3 della chiamata del servizio.

**N.B. :  L'istruzione SQL passata nel parametro INPUT() prevale su quella eventualmente impostata nella £G00


| **Parametro** | **Descrizione** | **Valori ammessi** | **Significato** |
| ---|----|----|----|
| **CHD()** | Intestazioni colonne | ' '=Utilizza le etichette dei campi come intestazioni di colonna (DEFAULT)   '1'=Utilizza i nomi dei campi come intestazioni di colonna| |
| **TPZ()** | Tipizzazione campi | ' '=Esegue la tipizzazione dei campi (DEFAULT)  '2'=Non esegue la tipizzazione dei campi| |
| **NRW()** | Nr. righe paginazione iniziale | Numero intero | Numero in base al quale viene paginata la visualizzazione dei risultati la prima volta (se 0 o non impostato pagina per 1000  record). Dalla seconda paginazione il numero di record visualizzati viene di volta in volta raddoppiato. |
| **HML()** | Formato Intest.matrice | ' '=Le intestazioni della matrice vengono suddivise su 2 righe (DEFAULT)  '1'=Le intestazioni della matrice vengono presentate su una sola riga| |
| **SNM()** | Contesto setup | Alfanumerico fino a 50 caratteri | Aggiunge una chiave al contesto di salvataggio dei setup della matrice |
| **NOR()** | Non aggiungere RRN | ' '=NO  '1'='SI' | Disabilita l'aggiunta del RRN (Relative Record Number) all'instruzione SQL |
| **LVL()** | Livello chiamata £SQLD. | Una lettera ad indicare la replica del B£SQLD01 da richiamare. La replica 'Z' è riservata all'utilizzo da comando UP SQL| |
| 


**E' necessario specificare livello di chiamata quando abbiamo più sezioni che richiamano il servizio LOA13_SE, in modo da aprire cursori SQL differenti ed evitare interferenze tra una matrice e l'altra in caso di paginazione.

### Esempi di chiamata del servizio LOA13_SE
**Interrogazione sul BRARTI0F con tipizzazione campi attiva e descrizioni dei campi come intestazioni di colonna
F(EXB;LOA13_SE;ESE.SQL) 1(;;) 2(;;) P(TPZ(1)) INPUT(SELECT * FROM BRARTI0F)

**Interrogazione sul BRARTI0F senza tipizzazione campi e nomi di sistema dei campi come intestazioni di colonna
F(EXB;LOA13_SE;ESE.SQL) 1(;;) 2(;;) P(CHD(1)) INPUT(SELECT * FROM BRARTI0F)

**Interrogazione sul BRARTI0F con tipizzazione campi attiva e nomi di sistema dei campi come intestazioni di colonna
F(EXB;LOA13_SE;ESE.SQL) 1(;;) 2(;;) P(CHD(1) TPZ(1)) INPUT(SELECT * FROM BRARTI0F)

**Interrogazione sul BRARTI0F con tipizzazione campi attiva e paginazione ogni 5000 record (se non impostato 1000)
F(EXB;LOA13_SE;ESE.SQL) 1(;;) 2(;;) P(TPZ(1) NRW(5000)) INPUT(SELECT * FROM BRARTI0F)


### Esempio di chiamata della scheda LOA13 come sottoscheda
F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCH;LOA13) INPUT(SQL(SELECT * FROM BRARTI0F WHERE A§TIAR='ART')  NRW(100))

**Input** :  contiene l'istruzione SQL con la SELECT da eseguire all'interno di un attributo SQL() e tutti i parametri sopra elencati per il servizio ciascuno all'interno del proprio attributo.


### Possibilità di forzare descrizione, oggetto e altre caratteristiche di un campo nella matrice
Utilizzando la clausola AS del linguaggio SQL è possibile indicare una descrizione alternativa per una colonna, ponendo tale descrizione tra "".
All'interno della descrizione (utilizzando come separatore il carattere '**;**' ) è possibile forzare altre caratteristiche della colonna.
_Di conseguenza non è possibile utilizzare il carattere ; (punto e virgola) all'interno di una clausola AS.

 T(**Caratteristiche gestite nell'ALIAS**)
- Intestazione della colonna
- Oggetto SMEUP
- Codice colonna della matrice
- 'R' per indicare alla matrice di non visualizzare se uguale al precedente
- Lunghezza del campo (per i numerici indicare i decimali separati da '**,**' ad esempio 10,2 )
- I/O del campo


In questo esempio alla colonna A§ARTI viene forzata come descrizione 'Codice', come oggetto '**', come codice della colonna 'C001' e come lunghezza 10 caratteri.

F(EXB;LOA13_SE;ESE.SQL) P(LVL(A)) INPUT(SELECT A§ARTI AS "Codice;**;C001;;10" FROM BRARTI0F)

**Nell'alias è possibile fare riferimento ad un altro campo per l'oggettizazione dinamica sostituendo le [ ] del riferimento al campo con le ( ).

F(EXB;LOA13_SE;ESE.SQL) INPUT(SELECT A§TIAR, A§ARTI AS "Codice;AR(A§TIAR)", A§DEAR as "Descrizione", A§PESO FROM BRARTI0F)

### Paginazione progressiva
La paginazione della matrice dell' UP SQL non avviene più in base ad un numero fisso di record, ma raddoppia ogni volta il numero di record caricati.
Il pulsante di paginazione indica inoltre nella propria descrizione il numero di paginazioni effettuate rispetto al numero di paginazioni totali così come il numero di record caricati rispetto ai record totali.
Ad esempio  :  "Segue (1 / 4 - 1000 / 12025)" dove 1 / 4 indica che si è paginato una volta rispetto ad un totale di 4 paginazioni e 1000 / 12025 indica che sono stati caricate mille righe su un totale di 12025 .

# AUTORIZZAZIONI (richiamo come comando UP SQL)

## Autorizzazioni di esecuzione del comando UP SQL : 

E' stata aggiunta una nuova classe di autorizzazione sul comando UP.
Si consiglia l'impostazione delle autorizzazioni in particolare relativamente alla funzione UP SQL , in modo da limitare solo alle persone autorizzate l'esecuzione di istruzioni SQL sui file. Qualora non venga creato l'elemento UP di B£P e non vengano impostate le autorizzazioni , le funzioni UP rimarranno autorizzate.
L'impostazione predefinita (PTF B£81211) prevede l'inserimento della classe UP in B£P , autorizzazioni SI su funzione '**' e autorizzazione NO su funzione 'SQL'.


## Autorizzazioni su istruzioni eseguite tramite comando UP SQL : 
E' stata aggiunta una nuova classe di autorizzazione (UPSQL) sulle istruzioni SQL eseguite tramite comando UP SQL.
 T(Le opzioni disponibili sono : )
- 01  :  autorizzazione all'inserimento di record (istruzione INSERT o SELECT INTO)
- 02  :  autorizzazione alla modifica di record (istruzione UPDATE)
- 04  :  autorizzazione alla cancellazione di record (istruzione DELETE)
- 05  :  autorizzazione all'interrogazione (istruzione SELECT)
- DDL :  autorizzazione alla modifica di oggetti di database (istruzioni CREATE, ALTER, DROP e GRANT)


In relazione a queste modifiche è stata implementata l'apposita PTF B£00723A, che crea automaticamente l'elemento UPSQL di B£P e imposta le autorizzazioni predefinite (solo interrogazione).

Le istruzioni di manipolazione dei dati e degli oggetti vengono comunque eseguite con le autorizzazioni di sistema dell'utente (e non del proprietario del programma) sugli oggetti relativi.

## Servizio di aggiornamento generico LOSUP_13
- [SER Sevizio di aggiornamento generico](Sorgenti/MB/DOC_SER/LOSUP_13)
