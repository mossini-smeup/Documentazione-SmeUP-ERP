# Struttura
Un Book è composto da uno o più documenti.
Un documento può essere di tipo indice o di tipo contenuto.

# Documenti di tipo indice
I documenti di tipo **indice** servono a raggruppare i documenti di tipo contenuto e sono di tipo **IND**. Un'indice può essere composto da documenti che sono a loro volta indice.
Questo tipo di documento è composto solamente di istruzioni di tipo  :   : DEC.
Ad esempio
** :   : DEC T(MB) P(DOC) K(nome_membro)**

Il massimo livello di annidamento è 3 partendo dai documenti base di un'applicazione.
Per maggiori dettagli sui documenti di tipo indice consultare il documento sulla nomenclatura
- [LATEX - Nomenclatura](Sorgenti/MB/DOC/LOCFRM_LTF)

# Documenti di tipo contenuto
I documenti di tipo **contenuto** contengono il testo e sono di tipo **TXT**.
Rispettano la sintassi della documentazione attiva di  Sme.up.

# Struttura documenti di tipo contenuto
Utilizzando il Wizard è possibile inserire i seguenti elementi ai book : 

- copertina
- indice (o sommario)
- capitoli
- sezioni e subsezioni
-- paragrafi e formattazione del testo
-- liste puntate e numerate
-- immagini
-- tabelle
- documenti - vedi **NOTA**

**NOTA** :  Un documento di tipo contenuto può utilizzare l'istruzione  :   : DEC. Questa possibilità NON va utilizzata perchè il massimo livello di inclusione di un Book è 3.

![WIZARDPRE](http://localhost:3000/immagini/LOCFRM_LTC/WIZARDPRE.png)
# Risultato
Seguendo la sintassi e lanciando la compilazione del book è possibile ottentere un PDF di qualità, come quello presentato in figura.

![PDFBOK](http://localhost:3000/immagini/LOCFRM_LTC/PDFBOK.png)
# Consultazione
Manuali ed esempi si possono trovare seguendo il percorso di menù : 
My Loocup - Per lo sviluppatore - Esempi

Quindi dalla scheda "Per gruppo" seguire il percorso : 
Capire LOOC.up - Esempi applicativi - Documentazione

Dalla scheda "Documentazione" selezionare : 
Presentazioni LATEX

Ed infine selezionare "Manuali"

# Sintassi
Di seguito vengono descritte le specifiche ed i costrutti disponiibili per la composizione dei book in formato PDF.

Questo a complemento del wizard presente nell'editor e richiamabile premendo _B_CTRL+W sulle specifiche.

### La copertina
La copertina viene generata in modo automatico assegnando come titolo la descrizione del membro BOOK di riferimento (o la descrizione del documento nel caso della generazione di un singolo documento), ed altre informazioni quali :  l'utente che ha generato il documento, la data di creazione, la versione di Sme.up, il nome del membro BOOk di riferimento (o il nome del membro DOC).
![PDFCOVBOK](http://localhost:3000/immagini/LOCFRM_LTC/PDFCOVBOK.png)
### Le sezioni
**Specifica  :   : T01  :   : T02  :   : T03**
Elemento di struttura. Le sezioni permettono di definire l'indice del book.
Esistono tre livelli gerarchici di sezioni, di importanza decrescente : 

-  :   : T01
-  :   : T02
-  :   : T03


**Esempio**
![pdfIndice](http://localhost:3000/immagini/LOCFRM_LTC/pdfIndice.png) :  : PAR T(Sintassi) F(04)
 :   : T01 Sezione 1
 :   : T01 Sezione 2
 :   : T02 SubSezione 2.uno
 :   : T03 SubSezione 3.uno
 :   : T02 SubSezione 2.tre
 :   : T01 Sezione 3
 :   : T01 Sezione 4


### Testo libero
Elemento di testo. Il testo libero può essere inserito nella pagina/frame senza utilizzare alcuna specifica.
**Esempio**
 :  : PAR F(03) L(NUM) T(Testo libero)
Esempio di testo libero

 :  : PAR T(Sintassi) F(04)
Esempio di testo libero


### I paragrafi e le liste
**Specifica  :   : PAR**
Elemento di testo. I paragrafi possono essere formattati valorizzando tre diversi attributi : 
- F(), permette di specificare il formato del testo (default, non proporzionale, in evidenza, nota tecnica, ...)
- L(), permette di specificare la tipologia di lista nel paragrafo (numerata, puntata)
- T(), permette di specificare il titolo del paragrafo
Nel paragrafo di tipo lista i singoli item della lista devono essere una riga nuova che comincia uno/più tratti e uno spazio("- "), o con uno/più punti e uno spazio (". ") (il numero di punti specifica il livello di profondità della lista, per un livello di profondità massima pari a 3)
**Esempio**
 :  : PAR T(Lista puntata) L(PUN)
- Riga 1.p
- Riga 2.p
-- Nested 1
--- Nested 2
-- Nested 3
- Riga 3.p

 :  : PAR T(Sintassi) F(04)
 :   : PAR L(PUN)
- Riga 1.p
- Riga 2.p
-- Nested 1
--- Nested 2
-- Nested 3
- Riga 3.p
 :   : PAR.END


### Le tabelle
Elemento grafico. Le tabelle possono essere costruite attraverso la sintassi standard  :   : TAB

**Specifica  :   : TAB**
Attraverso la sintassi standard  :   : TAB è possibile specificare i seguenti attributi : 
- Nome, per specificare il titolo della tabella
- R, per specificare la percentuale di riduzione
Inoltre per ogni singola colonna è possibile specificare altri attributi : 
- Txt, per specificare l'intestazione della colonna
- Lun, per specificare la dimensione in percentuale della colonna rispetto alla pagina. La colonna è multiriga e il testo va a capo automaticamente.
- LunAut, per far gestire in modo automatico la dimensione della colonna. La colonna è multiriga e il testo va a capo automaticamente.
- A, per specificare l'allineamento del testo nella colonna (valori accettati :  "L", "R", "C"). La colonna NON E' multiriga e il testo NON VA a capo.

Gli attributi Lun, LunAut, A sono mutualmente esclusivi, ovvero se sono definiti più attributi contemporaneamente su una colonna solo l'attributo con maggior priorità viene preso in considerazione. L'ordine di priorità rispetta il seguente ordine :  LUN, LUNAUT, A.

 :  : PAR T(Sintassi) F(04)
 :   : TAB Nam="Esempio tabella" R="100"
 :   : TAB.COL Txt="col. A='l'" A="L"
 :   : TAB.COL Txt="col. A='r'" A="R"
 :   : TAB.COL Txt="col. A='c'" A="C"
 :   : TAB.COL Txt="colonna Lun=40" Lun="40"
 :   : TAB.COL Txt="colonna LunAut" LunAut="1"
- cella 11 | cella 12 | cella 13 con lunghezza specificata nell'attributo | cella 14 con lunghezza automatica
- cella 21 | cella 22 | cella 23 con lunghezza specificata nell'attributo | cella 14 con lunghezza automatica
- cella 31 | cella 32 | cella 33 con lunghezza specificata nell'attributo | cella 14 con lunghezza automatica
 :   : TAB.END



|  Nam="Esempio tabella" R="100" |
| 
| .COL Txt="col. A='l'" A="L" |
| ---|----|
| 
| .COL Txt="col. A='r'" A="R" |
| 
| .COL Txt="col. A='c'" A="C" |
| 
| .COL Txt="colonna Lun='40'" Lun="40" |
| 
| .COL Txt="colonna LunAut" LunAut="1" |
| - cella 11 | cella 12 | cella 13 | cella 14 con lunghezza specificata nell'attributo | cella 15 con lunghezza automatica |
| - cella 21 | cella 22 | cella 23 | cella 24 con lunghezza specificata nell'attributo | cella 25 con lunghezza automatica |
| - cella 31 | cella 32 | cella 33 | cella 34 con lunghezza specificata nell'attributo | cella 35 con lunghezza automatica |
| 


### Le immagini
**Specifica  :   : IMG**
Elemento grafico. Le immagini possono essere incluse valorizzando i seguenti attributi : 
- Tit, per specificare il titolo dell'immagine
- Pat, per specificare il percorso ed il nome dell'immagine (è accettato sia un percorso locale, sia un percorso di rete, usando anche le variabili di Loocup)
- Dim, per specificare la dimensione dell'immagine in proporzione alla pagina espressa in percentuale
- Pos, per specificare l'allineamento della figura nella pagina
 :  : R01 Esempio
 :  : IMG P(Percorso ad un immagine) R(40) C(Esempio di immagine per presentazione)
 :  : PAR T(Sintassi) F(04)
 :   : IMG Pat ="[nome_variabile]\nome_cartella\nome_file.jpg" Dim="30%"


### Formattazione testo inline
Per **formattazione inline** si intende la possibilità di cambiare il formato del testo all'interno di frasi, elementi complessi come liste, tabelle, etc.

|  Nam="Esempi di tutti i font trattati" R="100" |
| 
| .COL Txt="Effetto" Lun="60" |
| ---|----|
| 
| .COL Txt="Specifica" |
| _1_  Rosso   Grande    | 1 |
| _2_  Blu     Grande    | 2 |
| _3_  Verde scuro    Grande    | 3 |
| _4_  Rosa  Grande    | 4 |
| _5_  Verde chiaro Reverse    | 5 |
| _7_  Rosso              | 7 |
| >  Blu                | 8 |
| _9_  Verde scuro      | 9 |
| _B_  Rosa   | B |
| _R_  Verde chiaro| R |
| __  Sottolineato       __| u |
| ** Alta intensità    **| h |
| _  Italic             _| i |
| _r_  Rosso sottolineato| r |
| Normale| *blank |
| 


All'interno di un testo si può cambiare il formato del testo ponendo prima del testo oggetto del cambio una delle specifiche sopra indicate racchiuse fra _ e chiudendo la porzione di test
