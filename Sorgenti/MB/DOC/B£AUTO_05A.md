# In breve
In Sme.up abbiamo grande attenzione al concetto di autorizzazione. In Looc.up ereditiamo le autorizzazioni di Sme.up ma il concetto di autorizzazione diventa più importante proprio in funzione del fatto che l'accesso alle funzioni è molto facilitato. In questo documento descriviamo gli aspetti delle autorizzazioni in Looc.UP.
Looc.UP utilizza le autorizzazioni di Sme.up quindi si rinvia alla opportuna documentazione per la comprensione dei concetti relativi.
Tutte le classi di autorizzazione di Looc.UP sono del tipo LO.xxx dove di solito xxx è il componente grafico (quindi BAS per base, GNT per Gantt ecc).

# Definizioni specifiche

- **Classe di autorizzazione** :  elemento della tabella B£P. In Looc.UP utilizzeremo classi simili alla classe "STATI" che cioè permettono di associare una matrice di 100 condizioni divise in 10 categorie con 10 livelli di importanza
- **Oggetto di autorizzazione** :  è un oggetto dipendente dalla classe di autorizzazione. Ad esempio la classe LO.SER definisce come oggetto di autorizzazione il servizio (quindi V3 ASE)
- **Categoria** :  sigla da 0 a 9 associata ad una classe di autorizzazione
- **Livello di importanza** :  numero da 0 a 9 che definisce quanto è riservata la funzione all'interno della categoria
- **Codice di protezione** :  numero di due cifre dove la prima descrive la categoria e il secondo il livello di importanza


## Introduzione :  classi di autorizzazione specifiche per Looc.UP
_1_Link alle classi di autorizzazione specifiche per Looc.UP
 :  : DEC T(TA) P(B£P) K(LO.EXD)
 :  : DEC T(TA) P(B£P) K(LO.BAS)
 :  : DEC T(TA) P(B£P) K(LO.SER)
 :  : DEC T(TA) P(B£P) K(LO.POP)

_1_Autorizzazioni menù Looc.UP
- [Doc.tecnica LOA12](Sorgenti/MB/DOC_OGG/V2LOCOSA12)

_1_Funzioni definite a livello client
Consideriamo definiti i seguenti oggetti : 
 :  : DEC T(TA) P(B£P) K(LO.BAS)
 :  : DEC T(OG) P(V2) K(LOBAS)
Tutte le funzioni definite direttamente nel client grafico (ad esempio le funzioni MENU BAR) appartengono ad una categoria definita mediante l'oggetto V2LOBAS e all'interno di tale categoria hanno un livello di importanza. Quindi ogni azione appartiene ad un "oggetto di autorizzazione" ed ha associato un "codice di protezione".
Al momento del collegamento viene fornito il livello di autorizzazione per l'utente per ogni categoria e il client controlla l'abilitazione alle funzioni.

Le autorizzazioni sono comunicate al collegamento quindi eventuali modifiche saranno recepite solo al collegamento successivo.

_2_NB! I significati delle 10 righe di autorizzazioni sono definite dinamicamente puntando dalla TAB£SAZ agli oggetti fissi V2LOBAS del tipo FFF.n, dove FFF è il nome della funzione e n il numero di riga. Questo : 

- permette di associare significati diversi alle 10 righe a seconda dell'oggetto (barra dei menù, pulsante...)
- permette di cablare mediante oggetti fissi questi significati, gestiti non da Sme.up ma dal client grafico.


_1_Esempio
La funzione "Servizi/Funzione libera" del MENU BAR è di "oggetto di autorizzazione" MNU.BAR di "categoria" 2 e di "importanza" 7 (quindi "codice di protezione" 27).
Nella classe di autorizzazione LO.BAS, per la "oggetto di autorizzazione"  MNU.BAR per la "categoria" 2 l'utente USR001 ha associato 4 quindi la funzione è non autorizzata.

_1_Come vedo l'associazione delle funzioni alle categorie
Per quanto riguarda le autorizzazioni sulla barra dei menù della finestra ogni voce riporta, in parte al nome che ne descrive la funzione, il numero che indica la coppia categoria-livello della funzione e quindi l'indicatore di autorizzazione che è stato passato dall'AS400.  Il valore 1 passato dall'AS indica l'autorizzazione concessa alla funzione, il valore 0 indice la negazione.
Nel menu delle finestre, sotto _7_"Servizi"** **-->** _7_"Funzioni di controllo"** ci sono le voci _7_"XML barra menu" e _7_"Setup autorizzazioni" che permettono rispettivamente di visualizzare lo XML che il client costruisce per definire la barra dei menu delle finestre e l'elemento XML di setup così come è giunto dall'AS in fase di inizializzazione.
_2_TODO le autorizzazioni sui bottoni(OM)


# Autorizzazione sui servizi
Chiamiamo servizio xxx il programma xxx definito come oggetto V3 ASE xxx e documentato in DOC_SER/xxx.
Nella documentazione sono classificati funzioni e metodi e ad ognuno è associato un codice di protezione. Se funzione e metodo non sono autorizzati, il client riceve un messaggio di non abilitazione. Il comportamento è come se il programma non esistesse quindi non vengono forniti i dati XML.

## Esempio
_1_Nota tecnica di sviluppo
Il programma JAJAT0D che richiama tutti i servizi gestisce la verifica dell'autorizzazione. Il programma JAJAT0D cataloga i servizi e la prima volta che viene richiamato un servizio ricerca (per ora nella documentazione) funzioni e metodi soggetti ad autorizzazione. Se almeno uno è protetto verifica l'abilitazione. Dalla seconda volta riutilizza i dati in memoria al fine di ottimizzare le prestazioni.

# Autorizzazione sulle schede
E' possibile richiedere un livello di autorizzazione minimo su
 :  : PAR F(01) L(NUM)
- l'intera scheda
- una sezione
- una subsezione
- una parte dello script

La **classe** di autorizzazione utilizzata è la **LO.EXD**.

## Autorizzazione sull'intera scheda
Per impostare un livello di autorizzazione sull'intera scheda è possibile utilizzare l'istruzione S.EXD.AUT. Questo permette di ridefinire l'autorizzazione impostata con UP AUT.
A questa istruzione è possibile associare 2 attributi : 

- Lev :  in cui si specifica il livello di autorizzazione richiesto (se non specificato viene assunto **05**)
- Src :  in cui si specifica la "sorgente" delle autorizzazioni , cioè il **£AUAAZ** (se non specificato viene assunto lo script della scheda)

L'istruzione di setup di autorizzazione di una scheda può essere definita a livello di scheda o di sottoscheda. Questo permette di definire (all'interno dello stesso script) un livello e una funzione per la scheda "main" e altrettanti per tutte le sottoschede lì definite.
Nella costruzione dell'XML di una sottoscheda (ossia nella cui nella chiamata è presente l'oggetto 4), viene prima cercata l'istruzione S.EXD.AUT nelle istruzioni della sottoscheda, se è presente viene utilizzata quella, altrimenti viene utilizzata l'istruzione S.EXD.AUT inserita nelle istruzioni della scheda principale, se non è presente nemmeno quella vengono usati i valori di default.
Quindi se in una scheda non viene utilizzata l'istruzione S.EXD.AUT, viene utilizzato il nome dello script come funzione di autorizzazione e 05 come livello minimo richiesto.
Se una scheda risulta essere non autorizzata, al suo posto viene aperta la scheda contenuta nello script NOAUT. Di default questa scheda contiene solo la scritta "NON AUTORIZZATO".
## Come individuare funzione e livello di autorizzazione richiesti per una scheda
Visualizzando l'XML di una scheda (o di una sottoscheda), si possono leggere, nel tag AUT, la funzione e il livello minimo richiesti per l'autorizzazione della scheda stessa.
Se ad esempio leggo l'XML della sottoscheda "dati commerciali" di un ente, noto : 
<Setup>
<Program>
<EXD>
_1_<AUT Lev="05" Cls="LO.EXD" Src="CN_COM"/>
</EXD>
</Program>
</Setup>
Da cui capisco che la funzione di autorizzazione da impostare è la CN_COM e il livello minimo richiesto è lo 05.

## Esempi autorizzazioni sull'intera scheda

_1_Esempio 1
![LOEXD_1](http://localhost:3000/immagini/B£AUTO_05A/LOEXD_1.png)In questo esempio la script di scheda è chiamato PIPPO, all'interno di questo è definita una sottoscheda PAPERINO. Non è definita l'istruzione S.EXD.AUT nè nella scheda principale e nemmeno nella sottoscheda. In questo caso sia nella valutazione della scheda principale che della sottoscheda viene utilizzato PIPPO come funzione (£AUAAZ) e 05 come livello richiesto (£AUAC4CP).

_1_Esempio 2
![LOEXD_2](http://localhost:3000/immagini/B£AUTO_05A/LOEXD_2.png)In questo esempio è definita l'istruzione S.EXD.AUT solo nella scheda principale (dello script PIPPO). L'istruzione ridefinisce sia il livello che la funzione. In questo caso sia nella valutazione della scheda principale che della sottoscheda viene utilizzato PLUTO come funzione (£AUAAZ) e 08 come livello richiesto (£AUAC4CP).

_1_Esempio 3
![LOEXD_3](http://localhost:3000/immagini/B£AUTO_05A/LOEXD_3.png)In questo esempio è definita l'istruzione S.EXD.AUT sia nella scheda principale (dello script PIPPO) che nella sottoscheda PAPERINO. L'istruzione nello script principale ridefinisce sia il livello che la funzione, mentre l'istruzione inserita nella sottoscheda ridefinisce solo il livello. In questo caso nella valutazione della scheda principale viene utilizzato PLUTO come funzione (£AUAAZ) e 08 come livello richiesto (£AUAC4CP), mentre nella valutazione della sottoscheda viene utilizzato PIPPO come funzione (£AUAAZ) e 02 come livello richiesto (£AUAC4CP).

_1_Esempio 4
![LOEXD_4](http://localhost:3000/immagini/B£AUTO_05A/LOEXD_4.png)In questo esempio è definita l'istruzione S.EXD.AUT solo nella sottoscheda PAPERINO. Tale istruzione ridefinisce sia il livello che la funzione. In questo caso nella valutazione della scheda principale viene utilizzato PIPPO come funzione (£AUAAZ) e 05 come livello richiesto (£AUAC4CP), mentre nella valutazione della sottoscheda viene utilizzato MINNIE come funzione (£AUAAZ) e 02 come livello richiesto (£AUAC4CP).

### Esempio "applicativo" :  autorizzazione sulla scheda cliente
Se voglio autorizzare solo uno specifico gruppo di utenti (ad esempio ADM) alla scheda del cliente (senza voler modificare la relativa scheda), posso impostare il record di autorizzazione
 :  : PAR
_£AUARA : _ LO.EXD
_£AUAUT : _  **ADM
_£AUAAZ : _ CN

con un valore maggiore o uguale a 05 (ma non superiore a 09, dato che si tratta comunque di una classe di autorizzazione gestita come la classe stati).
Poi per revocare l'autorizzazione a tutti gli altri utenti, posso impostare il record di autorizzazione
 :  : PAR
_£AUARA : _ LO.EXD
_£AUAUT : _  **
_£AUAAZ : _ CN

con un valore inferiore o uguale a 04.
### Secondo esempio "applicativo" :  autorizzazione sulla sottoscheda commerciale della scheda dell'articolo
Analogamente a prima, devo andare ad agire sullo script AR_COM, impostando
 :  : PAR
_£AUARA : _ LO.EXD
_£AUAUT : _  **ADM
_£AUAAZ : _ AR_COM

al livello 05, mentre il record
 :  : PAR
_£AUARA : _ LO.EXD
_£AUAUT : _  **
_£AUAAZ : _ AR_COM

deve essere portato a 04.

_2_NOTA sulla posizione dell'istruzione S.EXD.AUT
L'istruzione S.EXD.AUT è un'istruzione di setup di scheda (o sottoscheda), quindi deve essere posizionata prima della definizione delle varie istruzioni di definizione delle sezioni.
Quindi questa istruzione deve venire prima della prima istruzione G.SEZ dello stesso "livello" a cui si riferisce la S.eXD.AUT.Cioè se voglio impostare le autorizzazioni sulla scheda "main", allora S.EXD.AUT deve essere messa prima di qualunque istruzione G.SEZ; se invece voglio impostare le autorizzazioni su una specifica sotttoscheda, la S.EXD.AUT deve essere messa prima delle G.SEZ di quella sottoscheda.

Ad esempio in questo script : 

| 
| .COL Txt="Riga" A="L" |
| ---|----|
| 
| .COL Txt="Istruzione" LunAut="1" A="L" |
|  - 1 | G.SEZ Pos(A) |
|  - 2 | G.SUB.TRE Tit="Articoli" |
|  - 3 | D.FUN.STD F(TRE;*LIS;) 1(OG;;AR) |
|  - 4 | G.SEZ Pos (B) |
|  - 5 | G.SUB.SCH Tit="Sottoscheda cliente" |
|  - 6 | D.SCH Nam(CLI) |
|  - 7 | I.SCH Nam(CLI) |
|  - 8 | G.SEZ Pos(A) |
|  - 9 | G.SUB.MAT Tit="OAV" |
|  - 10 | D.FUN.STD F(EXB;*OAV;) 1(CN;CLI;000001) |
|  - 11 | G.SEZ Pos(B) |
|  - 12 | G.SUB.IMG Tit="Fotografia" |
|  - 13 | D.IMG.OGG T(CN) P(CLI) K(000001).IMG |
|  - 14 | I.SCH.END |
| 

L'istruzione S.EXD.AUT relativa a tutta la scheda va messa come prima istruzione, mentre l'istruzione S.EXD.AUT relativa alla sottoscheda CLI va messa tra l'istruzione 7 e 8 (cioè tra "I.SCH Nam(CLI)" e la successiva "G.SEZ Pos(A)").
## Autorizzazione sulla singola sezione.
E' possibile impostare un livello di autorizzazione minimo anche sulla singola sezione. Per fare questo bisogna impostare nell'istruzione G.SEZ l'attributo _Aut_, passandogli il livello minimo richiesto per quella sezione.
Il nome della funzione di autorizzazione è di default (come nel caso dell'autorizzazione sull'intera scheda) il nome del membro in cui è contenuto lo script della scheda in questione. Tale funzione può, anche in questo caso, essere ridefinita mediante l'utilizzo dell'istruzione S.EXD.AUT (con le risalite viste precedentemente). Ovviamente in questo caso l'eventuale livello specificato nell'istruzione S.EXD.AUT viene ignorato, in quanto il livello richiesto è specificato direttamente nell'istruzione G.SEZ.
In caso una sezione risulti essere non autorizzata, nella costruzione della scheda viene ignorata, come se quella sezione non fosse presente nello script.

## Autorizzazione sulla singola subsezione
E' possibile impostare un livello di autorizzazione minimo anche sulla singola subsezione. Per fare questo bisogna impostare nell'istruzione G.SUB.xxx l'attributo _Aut_, passandogli il livello minimo richiesto per quella subsezione.
Il nome della funzione di autorizzazione è di default (come nei casi precedenti) il nome del membro in cui è contenuto lo script della scheda in questione. Tale funzione può, anche in questo caso, essere ridefinita mediante l'utilizzo dell'istruzione S.EXD.AUT (con le risalite viste precedentemente). Ovviamente anche in questo caso l'eventuale livello specificato nell'istruzione S.EXD.AUT viene ignorato, in quanto il livello richiesto è specificato direttamente nell'istruzione G.SUB.xxx.
In caso una subsezione risulti essere non autorizzata, nella costruzione della scheda viene ignorata, come se quella subsezione non fosse presente nello script.

## Autorizzazione su una parte di script
E' possibile autorizzare una parte di script "a piacere". E' possibile infatti utilizzare l'istruzione I.IF.AUT, a cui viene passato nell'attributo _Aut_ il livello di protezione. Se l'utente non risulta autorizzato, tutta la parte di script compresa tra l'I.IF.AUT in questione e l'I.IF.END relativo, viene ignorata. Analogamente ai casi precedenti, la funzione di autorizzazione utilizzata è lo script di scheda a meno di ridenominazioni fatte utilizzando l'istruzione S.EXD.AUT.

## Capire le autorizzazioni nelle schede
All'interno delle schede di esempio "Cosa si può fare con le schede" esiste una scheda di esempio specifica per le autorizzazioni "ESE1_AUT" la quale a sua volta richiama (tra le altre) : 
- una sezione per le autorizzazioni di tipo IF
- una sezione per le autorizzazioni su sezioni e subsezioni
- una sezione per le autorizzazioni sull'intera scheda
- una sezione che presenta (e consente di modificare) le autorizzazioni rilevanti per Looc.UP


# Autorizzazione alle funzioni di un oggetto
- (SV) Da definire (sviluppo RPG)

# Autorizzazione nell'emulazione
L'emulazione utilizza tutte e sole le autorizzazioni definite normalmente in Sme.up

# Autorizzazioni sulle colonne delle matrici
Il servizio carica la classe di autorizzazione LO.EXB.
Ad ogni campo della matrice è associato un numero identificativo del livello di protezione.
Al momento della costruzione della "GRIGLIA" il servizio si occupa di trasformare in "non visibili" (H) le colonne per cui non si ha autorizzazione

# In sintesi
Per poter accedere a una scheda contenente la chiamata a un servizio che mostri dati riservati l'utente dovrà superare autorizzazioni a livello di : 

- Chiave di menù (poter selezionare la scheda)
- Scheda (poter visualizzare la sezione contenente la chiamata)
- Servizio (poter eseguire la funzione richiesta)
- Oggetto (? poter accedere ai dati riservati)


# Sviluppi previsti
Contiamo di continuare a migliorare gli aspetti di autorizzazione e in particolare dovremo risolvere i seguenti aspetti : 

- Semplificare la manutenzione della tabella autorizzazioni (modifica in matrice)
- Documentare meglio il significato delle categorie di autorizzazione (10 gruppi delle classi di tipo "STATI")
- Permettere di porre, facoltativamente, i livelli di protezione all'esterno di programmi, servizi e schede. In modo simile alle traduzioni penseremo ad una funzione che fornisce il livello di protezione impostato dall'utente e che sovrascrive quello presente in programmi, schede e documentazione dei servizi.

