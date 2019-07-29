Il componente **LaTeX/PDF** permette di creare presentazioni di alto livello evitando l'utilizzo di power point, mantenendo la stesse potenzialità ed ottenendo un **PDF** di alta qualità!

# Elementi
La sintassi di ogni elemento inizia con il tag ** :   : P.** (dove P specifica l'appartenenza dell'elemento al gruppo "presentazione").
E' possibile creare e personalizzare una presentazione inserendo i seguenti elementi : 

- copertina
- indice (o sommario)
- sezioni e subsezioni
- frame (pagina)
- subframe (parte della pagina)
-- paragrafi e formattazione del testo
-- liste puntate e numerate
-- immagini
-- tabelle


Durante la creazione sarà sempre possibile servirsi del Wizard per semplificare il lavoro (figura ImgRef(WIZARDPRE)).
![WIZARDPRE](http://localhost:3000/immagini/LOCFRM_LTB/WIZARDPRE.png)ImgRef(WIZARDPRE)

# Risultato
Seguendo la sintassi e lanciando la compilazione della presentazione è possibile ottentere un PDF di qualità, come quello presentato in figura ImgRef(PDFPRE).

![PDFPRE](http://localhost:3000/immagini/LOCFRM_LTB/PDFPRE.png)
# Ubicazione
Presentazioni ed esempi si possono trovare seguendo il percorso di menù : 
My Loocup - Per lo sviluppatore - Esempi

Quindi dalla scheda "Per gruppo" seguire il percorso : 
Capire LOOC.up - Esempi applicativi - Documentazione

Dalla scheda "Documentazione" selezionare : 
Presentazioni LATEX

Ed infine selezionare "Presentazioni"

# Sintassi
Di seguito vengono descritte le specifiche ed i costrutti disponibili per la composizione delle presentazioni in formato PDF.
Gli esempi possono essere consultati da MyLoocup - Esempi - Contenuto origine.

Questo a complemento del wizard presente nell'editor e richiamabile premendo _B_CTRL+W sulle specifiche.

### La copertina
**Specifica  :   : P.COV**
Elemento di struttura. Definisce la copertina della presentazione. E' possibile specificare i seguenti attributi : 
- Tit, permette di specificare il titolo
- Ver, per specificare la versione o il sottotitolo
- Aut, per specificare l'autore
- Sta, per specificare lo stato
- Dat, per specificare la data
- BckCov, per specificare l'immagine di sfondo della sola copertina
- BckAll, per specificare l'immagine di sfondo di tutta la presentazione
- LogCov, per specificare il logo della sola copertina (visualizzato in centro)
- LogAll, per specificare il logo di tutta la presentazione ( visualizzato in basso a destra)

**Esempio**
![PDFCOV](http://localhost:3000/immagini/LOCFRM_LTB/PDFCOV.png) :  : PAR T(Sintassi) F(04)
 :   : P.FRM
 :   : P.COV Tit="Titolo" Sub="Sottotitolo" Aut="Autore" Ver="Versione" Sta="00" Dat="" BckCov="[SME.HOM]\SMEIMG\LOGHI\SFO_000.PNG" BckAll="[SME.HOM]\SMEIMG\LOGHI\SFO_001.PNG"


### Le sezioni
**Specifica  :   : P.T01  :   : P.T02  :   : P.T03**
Elemento di struttura. Le sezioni permettono di definire l'indice della presentazione.
Esistono tre livelli gerarchici di sezioni, di importanza decrescente : 

-  :   : P.T01
-  :   : P.T02
-  :   : P.T03


**Esempio**
![PDFSOM](http://localhost:3000/immagini/LOCFRM_LTB/PDFSOM.png) :  : PAR T(Sintassi) F(04)
 :   : P.T01 Tit="Sezione 1"
 :   : P.T01 Tit="Sezione 2"
 :   : P.T02 Tit="SubSezione 2.uno"
 :   : P.T02 Tit="SubSezione 2.due"
 :   : P.T02 Tit="SubSezione 2.tre"
 :   : P.T01 Tit="Sezione 3"
 :   : P.T01 Tit="Sezione 4"


### Nuova pagina/frame
**Specifica  :   : P.FRM**
Elemento di struttura. Definisce nuove pagine/frame. Ad esso possono essere associati i seguenti attributi : 
- Tit, per specificare il titolo della pagina/frame
- Tra, per specificare il tipo di transizione

In ogni pagina/frame è possibile inserire elementi di testo, elementi grafici o combinazioni di testo e grafica.

### Testo libero
Elemento di testo. Il testo libero può essere inserito nella pagina/frame senza utilizzare alcuna specifica.
**Esempio**
 :  : PAR T(Testo libero)
Esempio di testo libero

 :  : PAR T(Sintassi) F(04)
 :   : P.FRM
Esempio di testo libero


### I paragrafi
**Specifica  :   : P.SUB.TXT**
Elemento di testo. I paragrafi possono essere formattati valorizzando tre diversi attributi : 
- StiTxt, permette di specificare lo stile del testo
- ColTxt, permette di specificare il colore del testo
- DimTxt, permette di specificare la dimensione del testo
- Dim, per specificare la dimensione del paragrafo in proporzione alla pagina
- Pos, per specificare l'allineamento del testo nella pagina
 :  : R01 Esempio
 :  : PAR T(Paragrafo)
_1_Esempio di paragrafo formattato

 :  : PAR T(Sintassi) F(04)
 :   : P.FRM
 :   : P.SUB.TXT StiTxt="01" ColTxt="01" DimTxt="04" Pos="1"

Esempio di paragrafo formattato


### Le liste
**Specifica  :   : P.SUB.ITL**
Elemento di testo. Il linguaggio permette di comporre delle liste, anche annidate.
- I singoli item delle liste devono essere una riga nuova che comincia con uno o più punti e uno spazio (". ") (il numero di punti specifica il livello di profondità della lista, per un livello di profondità massima pari a 3)
- Mod, per specificare la modalità di visualizzazione dell'elenco
- Dim, per specificare la dimensione dell'elenco in proporzione alla pagina
- Pos, per specificare l'allineamento dell'elenco nella pagina

**Esempio**
 :  : PAR T(Lista puntata) L(PUN)
- Riga 1.p
- Riga 2.p
-- Nested 1
-- Nested 2
-- Nested 3
- Riga 3.p

 :  : PAR T(Sintassi) F(04)
 :   : P.FRM
 :   : P.SUB.ITL
. Riga 1.p
. Riga 2.p
.. Nested 1
.. Nested 2
.. Nested 3
. Riga 3.p


### Le tabelle
Elemento grafico. Le tabelle possono essere costruite in due modalità : 
- attraverso la sintassi standard  :   : TAB
- attraverso la chiamata di servizio
**Specifica  :   : P.SUB.SER**
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


Attraverso la chiamata di servizio è possibile specificare i seguenti attributi : 
- Tit, per specificare il titolo della tabella
- Fun, per specificare il percorso ed il nome della tabella
- Cnd, per specificare le colonne (ovvero i campi) e il numero di righe da visualizzare
- Dim, per specificare la dimensione della tabella in proporzione alla pagina
**Esempio**
![PDFTAB](http://localhost:3000/immagini/LOCFRM_LTB/PDFTAB.png) :  : PAR T(Sintassi) F(04)
 :   : P.FRM
 :   : P.SUB.SER Tit="Articoli " Fun="F(EXB;*OAV;) 1(OJ;*FILE;BRARTI0F)" Dim="0.45" Cnd="COD(£OAVIN&£OAVOV) RIG(6)"


### Le immagini
**Specifica  :   : P.SUB.IMG**
Elemento grafico. Le immagini possono essere incluse valorizzando i seguenti attributi : 
- Tit, per specificare il titolo dell'immagine
- Pat, per specificare il percorso ed il nome dell'immagine (è accettato sia un percorso locale, sia un percorso di rete, usando anche le variabili di Loocup)
- Dim, per specificare la dimensione dell'immagine in proporzione alla pagina espressa in percentuale
- Pos, per specificare l'allineamento della figura nella pagina
 :  : PAR T(Sintassi) F(04)
 :   : P.FRM
 :   : P.SUB.IMG Pat ="[nome_variabile]\nome_cartella\nome_file.jpg" Dim="30%"


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
