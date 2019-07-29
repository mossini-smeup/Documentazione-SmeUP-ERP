## Princìpi generali
Costruire una scheda significa creare uno script che descriva quali dati visualizzare e come disporli graficamente.
Questo script viene interpretato dal servizio *SCO (implementato dal programma JATRE_18C) e in base ad esso viene costruito un XML, presentato dal componente EXD (Scheda).
Gli script delle schede sono salvati su AS come membri nel file SCP_SCH.

## Best practice
 :  : PAR F(01) L(PUN)
- Le istruzioni degli script (TUTTI!) sono **case-sensitive**! L'immissione di istruzioni non valide può portare a comportamenti spesso difficili da individuare.
- Si raccomanda di portare la massima attenzione quando vengono editati mediante il PDM (può capitare che il formato di editazione sia impostato a MAIUSCOLO).
- Si consiglia di utilizzare per quanto possibile l'editor di Loocup.
- Si consiglia di mantenere allineati i membri del file SCP_CFG con la relativa versione di SmeUp. Questo consente un controllo sintattico privo di false segnalazioni di errore :  ad esempio la nuova versione del client supporta un tag che non risulta definito.
- Nel caso vengano segnalati errori, si raccomanda SEMPRE di verificare il dettaglio. Se i membri del file SCP_CFG sono aggiornati, pochi errori segnalati si possono trascurare : 
-- risposta che eccede la lunghezza MA, la domanda non tipizzata E il formato della risposta è DOMANDA(RISPOSTA) oppure DOMANDA="RISPOSTA"
-- Oggetto non definito nell'ambiente in cui sto modificando lo script MA definito nell'ambiente effettivo.
-- tag supportato ma membro di definizione non ancora creato o aggiornato


# Creazione
La creazione di una scheda segue due passi : 

- Definizione del layout grafico della scheda (sezioni e subsezioni)
- Indicazione dei dati da presentare

Le istruzioni (o famiglie di istruzioni) da utilizzare negli script per costruire una scheda verranno di seguito evidenziate **in grassetto**; nello script devono essere precedute da un doppio ' : '.

## 1. Definizione del layout grafico
Definiamo scheda un insieme di sezioni (le finestre contenute nella scheda) disposte sul video.
Ogni sezione deve contenere una o più subsezioni rappresentate ciascuna da un "tab", ovvero un'etichetta di testo in alto a sinistra.
In ogni subsezione un componente visualizza un insieme di dati, fornito come XML da un servizio (programma RPG); le subsezioni contenute nella stessa sezione vengono rappresentate alternativamente nella stessa finestra.

![EXD002](http://localhost:3000/immagini/LOCEXD_B/EXD002.png)
### Autodimensionamento e Autoposizionamento delle schede (attributi AutoPos e AutoFit)
L'autodimensionamento fa in modo che le subsezioni si dimensionino in funzione del loro contenuto mentre l'autoposizionamento fa in modo che le subsezioni si aprano in modo tale da non coprire totalmente le sezioni gia' aperte (in questo modo e' possibile avere un'idea dei livelli e delle schede aperte).

### Sezioni
Nella scheda deve essere definita almeno una sezione (**G.SEZ**), se la scheda è costituita da un'unica finestra.
Più sezioni vengono definite per "affettamenti" successivi della finestra della scheda :  ogni sezione è individuata da una stringa alfanumerica, in cui le lettere rappresentano un "affettamento" verticale e i numeri orizzontale.
Per esempio due sezioni affiancate in orrizzontale saranno associate alle stringhe 'A' e 'B'.
![LOCEXD_02](http://localhost:3000/immagini/LOCEXD_B/LOCEXD_02.png)
Se volessi suddividere la sezione 'A' in due sezioni disposte in verticale le definirei come 'A1' e 'A2', e così via.
![LOCEXD_03](http://localhost:3000/immagini/LOCEXD_B/LOCEXD_03.png)
Se non specificato altrimenti le sezioni interne a una sezione vengono equidimensionate.
Se invece si vogliono dimensionare diversamente le sezioni si utilizza il comando **Dim** seguito dalla percentuale della dimensione tra parentesi :  esempio Dim (30%) significa "assegna alla sottosezione il 30% del totale". Se il valore percentuale è preceduto dal segno meno (-) si intende calcolo della dimensione a partire dal fondo (destra o basso) se manca il segno si intende a partire dall'inizio (sinistra - alto).

E' possibile definire il titolo della sezione da xml dati tramite l'attributo Title

### Subsezioni
Data una sezione (una sottofinestra della scheda) è necessario definire quale componente/i vi verrà utilizzato per la visualizzazione dei dati.
Una subsezione può presentare dei dati tramite : 

- Un componente grafico di LOOC.up (albero, matrice,...)
- Un "componente" proprietario della scheda (cruscotto, label di testo, semaforo)

Si noti come, essendo la scheda stessa un componente grafico di LOOC.up, una subsezione di scheda può contenere a sua volta una scheda.

Ad una subsezione possiamo associare : 

- Un setup che condiziona il comportamento del componente (quindi la presentazione) (**G.SET**). Ad esempio, per una subsezione che visualizza un grafico si può specificare se il grafico è a barre oppure a torta.
- Un'indicazione sulle subsezioni che cambiano il contenuto dinamicamente in base a valori scelti in questa subsezione  (**G.DIN**).


## 2. Indicazione dei dati da presentare
Una volta indicato, tramite la definizione della subsezione, quale componente visualizza i dati e come li visualizza, è necessario fornire i dati stessi (istruzioni di tipo **D**).
È possibile : 

- Indicare direttamente un valore da visualizzare (ad esempio un attributo di un oggetto da visualizzare in una label) (**D.OGG**).
- Chiamare un programma esterno (servizio o programma generico) per la costruzione dinamica dei valori (ad esempio per ritornare l'elenco degli ordini di un cliente) (**D.FUN.STD**, oppure **D.PGM**).


## Altre possibilità
### Istruzioni di tipo I (opzionali)
Le istruzioni di tipo **G** e **D** sono indispensabili per costruire una scheda. Ad esse possono essere affiancate le istruzioni di tipo **I**,
di controllo nella costruzione della scheda. Esse permettono di : 

- Includere uno script o addirittura un pezzo di XML nello script corrente (**I.INC**, **I.XML**)
- Gestire la costruzione di parti di scheda al verificarsi di determinate condizioni (**I.IF**)
- Costruire dinamicamente parti di scheda effettuando loop su proprietà di un oggetto (**I.LOP**)
- Definire sottoschede all'interno dello stesso membro della scheda corrente, evitando la proliferazione di membri (**I.SCH**)


### Dinamicità
Mediante l'utilizzo di variabili è possibile rendere dinamico il comportamento della scheda, rendendola sensibile a oggetti e opzioni passati nella chiamata e alle scelte dell'utente nella navigazione della stessa.

## Help di dettaglio
- [Componenti ed eventi](Sorgenti/MB/DOC/EDT_SCH)

## Forme grafiche delle sezioni
Sono i tipi di rappresentazione dei dati utilizzabili nelle subsezioni di una scheda.

Si dividono in due tipi : 

- forme grafiche legate a componenti di LOOC.up :  il componente "Scheda" chiama un componente di Looc.up (eventualmente anche una sottoscheda) per la rappresentazione dei dati di una subsezione.
- forme grafiche rappresentate direttamente dal componente scheda :  è il componente scheda stesso che effettua la visualizzazione dei dati per una subsezione. Queste forme non sono utilizzabili all'esterno della scheda :  pur potendo creare servizi che costruiscono XML per esse, le funzioni relative a tali servizi sono richiamabili solo all'interno di una scheda.


 :  : PAR T(Forme grafiche legate a componenti) L(PUN)
- TRE :  Albero.
- TRA :  TabAlbero.
- HTM :  Pagina Internet.
- MAT :  Matrice (componente EXB).
- CHA :  Grafico (componente EXA).
- SCH :  Sottoscheda (componente EXD).
- DYN :  forma grafica ricavata dinamicamente dal componente specificato nella chiamata a seguire.


 :  : PAR T(Forme grafiche "interne") L(PUN)
- IMG :  Immagine.
- LAB :  Label.
- IML :  Lista di immagini.
- BTN :  Bottoniera.
- SEM :  Semaforo.
- GAU :  Cruscotto.
- PDF :  Documento PDF.



### Documentazione dei componenti interni : 

**Etichetta**
Visualizza un testo con la possibilità di formattarlo
**Opzioni**
**XML**

**Semaforo**
Visualizza un semaforo. La luce accesa rappresenta un valore (Valore) in ingresso confrontato con due valori di soglia (Soglia1, Soglia2) forniti in ingresso.
Date Soglia1<Soglia2 : 

- Valore<Soglia1 :  semaforo rosso
- Soglia1<Valore<Soglia2 :  semaforo giallo
- Soglia2<Valore :  semaforo rosso
**Opzioni**
Nessuna
**XML**
  <Elemento Soglia1="50" Soglia2="100" Valore="80" />

### Forme grafiche raggruppate per tipo di XML processato
 :  : PAR T(Albero) L(PUN)
- IMG :  Immagine (solo un elemento).
- LAB :  Label (solo un elemento).
- TRE :  Albero.
- TRA :  TabAlbero.
- IML :  Lista di immagini.
- BTN :  Bottoniera.


 :  : PAR T(Matrice) L(PUN)
- MAT :  Matrice.
- CHA :  Grafico.


Le altre utilizzano XML proprietario...

## Variabili e dinamicità
### Variabili
Distinguiamo due casi : 

- Variabili statiche :  ricavate dai parametri con cui è chiamata la scheda
- Variabili dinamiche :  valorizzate in base a scelte utente dopo la creazione/visualizzazione della scheda


### Variabili statiche
Le variabili statiche, della forma _1_&VAR, sono valorizzate automaticamente in base agli oggetti passati nella chiamata alla scheda nell'_2_Oggetto 1 e nel Parametro. Sono perciò disponibili al servizio **JATRE_18C** quando questi legge lo script per costruire la struttura della scheda.

### Variabili definite
**Dall'Oggetto 1**
I nomi di queste variabili sono standard e assumono significati precisi in relazione all'Oggetto 1 passato nella chiamata.

- _&_OG.T1, _&_OG.P1, _&_OG.K1, _&_OG.D1 : 
Restituiscono il tipo, parametro, codice e descrizione dell'Oggetto 1
- _&_OA.xxx, _&_OD.xxx, _&_OT.xxx, _&_OP.xxx, _&_OI.xxx : 
Restituiscono il valore (OA) o la descrizione (OD) o il tipo (OT) o il parametro(OP) o l'intestazione (OI) dell'attributo xxx dell'Oggetto 1
- _&_OB.xxx : 
Restituisce il valore dell'attributo xxx dell'Oggetto OG tipo/parametro dell'Oggetto 1
- _&_LO.VA, _&_LO.SI, _&_LO.PA : 
Usate all'interno di un loop ..I.LOP sull'Oggetto 1, restituiscono un valore diverso a seconda del tipo di loop.
Ad esempio, per un loop di tipo £IMM ritornano il tipo accesso (VA), il significato (SI) e il percorso (PA) di un immagine relativa all'Oggetto 1.


**Dal Parametro**

- _&_PA.xxx : 
 Restituiscono il valore di un parametro passato alla scheda nel Parametro. xxx è il nome con cui è stato passato il parametro, a discrezione dell'utente. La variabile &PA.*ALL restituisce la stringa di tutti i parametri.


**Dal Parametro INPUT**

- _&_IN.xxx : 
 Restituiscono il valore di un parametro passato alla scheda nel Parametro INPUT. xxx è il nome con cui è stato passato il parametro, a discrezione dell'utente. La variabile &IN.*ALL restituisce la stringa di tutti i parametri.


**Di Ambiente**

- _&_AM.AZ :  Azienda
- _&_AM.UT :  Utente
- _&_AM.DT :  Data attuale (dell'utente)
- _&_AM.MG :  Magazzino unico (da B£2)


**Altro**

- _&_D8.xxx : 
Restituisce la data corrispondente alla formula indicata dal valore xxx in formato gg/mm/aaaa. Le formule sono quelle disponibili sull'oggetto D8 mettendo una / nel codice.



### Esempi
Variabili su Oggetto1 :  data una chiamata del tipo :  F(EXD;*SCO;) 1(CN;CLI;000001), corrispondente alla scheda dell'oggetto cliente 000001, sono valorizzate le variabili : 

- _&_OG.T1='CN'
- _&_OG.P1='CLI'
- _&_OG.K1='000001'
- _&_OG.D1='Dario Rossi s.p.a.' (ad esempio)
- _&_OA.I/02='000001'
- _&_OD.I/02=''
- _&_OA.I/05='BS' (ad esempio)
- _&_OD.I/05='Brescia'
- _&_OT.I/05='TAV§P'
- _&_OI.I/05='Provincia'
- _&_OB.J/002 ='BRENTIOF' (Ritorna il valore dell'Oav J/002 dell'oggetto OG codice CNCLI che calcola il file dell'oggetto)


Variabili sul Parametro :  data una chiamata del tipo :  F(EXD;*SCO;) 1(CN;CLI;000001) P(UNO(val1) DUE(35) ART(A01)) sono valorizzate le variabili : 

- _&_PA.UNO='val1'
- _&_PA.DUE='35'
- _&_PA.ART='A01'


### Attenzione!
All'interno di una scheda le chiamate alle funzioni standard di LOOC.up passano l'Oggetto1 ricevuto in ingresso nella chiamata alla scheda, se non diversamente specificato. Così all'interno di una scheda chiamata con F(EXD;*SCO;) 1(CN;CLI;000001) sono equivalenti : 

- F (...funzione) 1(_&_OG.T1;_&_OG.P1;_&_OG.K1)
- F (...funzione) 1(CN;CLI;000001)
- F (...funzione)

_Nota : _ Se nella chiamata della funzione sono presenti variabili dinamiche (vedi paragrafo successivo) questo passaggio implicito dell'Oggetto1 non viene applicato, dato che nelle variabili stesse potrebbe essere presente l'Oggetto1.


### Variabili dinamiche
Le variabili dinamiche, racchiuse tra parentesi quadre, sono valorizzate dinamicamente cliccando su elementi della scheda.
Questo avviene **dopo** la creazione della scheda, quindi il loro valore non può condizionarne la costruzione (in senso di struttura e metodi interni alla scheda) ma solo eventuali chiamate a funzioni di LOOC.up ripetute dopo la creazione.
È però possibile passarle a sotto-schede, in modo che all'interno di queste siano viste come variabili statiche.
 per la documentazione delle chiamate a programmi esterni e fornitori di dati interni alla scheda.
Se viene richiesto il valore di una variabile non precedentemente valorizzata, tale variabile sarà assunta come "vuota".
### Attenzione!
Per una corretta interpretazione delle variabili dinamiche, il primo carattere del loro nome non può essere un numero.

### Esempio
Consideriamo una subsezione che contiene l'elenco delle applicazioni di SME.up (elementi della tabella B£A) sotto forma di albero, ottenuta con la chiamata alla funzione F(TRE;*LAP;). Se specifichiamo che questa subsezione induce dinamicità in un'altra sezione cliccando su un elemento dell'albero (ad esempio BR) istanzieremo le variabili : 

- T1='TA'
- P1='B£A'
- K1='BR'
- Tx='BREC_up basic records'
- Fu='F(TRE;*APP;) G(CDI) 1(TA;B£A;BR)'

T1, P1, K1, Tx sono rispettivamente tipo, parametro, codice e descrizione dell'elemento selezionato. Fu è una chiamata a funzione standard di LOOC.up associata al doppio clic sull'elemento :  questa associazione viene fatta nella costruzione dell'albero da parte del servizio (in questo caso *LAP).
Tutti i valori delle variabili sono salvati nell'XML dell'albero in esame.
I nomi delle variabili T1, P1, K1, Tx, Fu sono nomi standard associati in questo caso agli elementi di un albero di LOOC.up; altri componenti, come la matrice, presentaranno un set diverso di variabili con nomi diversi. È possibile, nel loro impiego all'interno di una scheda, ridenorminarle.

### Di albero
T1 / P1 / K1 = Tipo/Parametro/Codice dell'oggetto
Tx = Testo o descrizione
Fu = Funzione eventualmente presente nell'attributo EXEC

Nell'albero c'è anche lòa possibilità di asseganre al singolo livello dell'albero un nome che verrà assegnato ai nodi di quel livello come attributo Nome="". A quel punto il click sul nodo di un albero valorizzerà anche una serie di variabili T1, P1, K1, D1 per ogni padre.
> T(Esempio)
Un albero siffatto : 
.Nodo con Nome="L1"
.        |
.        |
.        ___Nodo con Nome="L2"
.                          |
.                          |
.                          ___Nodo con Nome="L3"


Clickando sul **Nodo con Nome="L3"** verranno valorizzate anche le variabili L1.T1 con il tipo dell'oggetto del nodo in questione, L1.P1 con il parametro dell'oggetto del nodo in questione, L1.K1 con il codice dell'oggetto del nodo in questione, L1.D1 con la descrizione dell'oggetto del nodo in questione, L2.T1 con il tipo dell'oggetto del nodo in questione, etc. fino a L3.D1 con la descrizione dell'oggetto del nodo in questione.
Questo permette, sulla selezione di un nodo dell'albero di avere a disposizione i dati di tutto il percorso che dalla radice dell'albero porta al nodo selezionato.

### Di matrice
Cliccando su un campo della matrice vengono valorizzate : 

K1 = Valore del campo cliccato
ID = Numero della riga della matrice
Cont = ???
Inoltre vengono valorizzate tutte le variabili corrispondenti ai campi della riga selezionata : 
i nomi delle variabili sono quelli assegnati ai campi nella tabella di definizione delle colonne
Es. data una matrice definita dalla £JAXSWK : 
>S5SCAD    Scadenza                     D8*YYMD               12
S5TPPA    Tipo Pagamento               TAC5G                 03
S5COPA    Codice Pagamento             TAPAG                 03
S5NDOR    Numero Documento                                   20
S5DAAV    Dare / Avere                                       01
S5IMPO    Importo                      NR                    15

cliccando su un campo della matrice (ad. esempio un importo) si avrà in K1 e S5IMPO il valore del campo, in S5SCAD il valore della scadenza sulla stessa riga, S5TPPA il tipo pagamento e così via..

### *CLEAR
E' possibile cancellare tutte le variabili dinamiche di un certo scope (di sezione, di scheda...) mediante la funzione *CLEAR.
Tale funzione deve essere implementata come una variabile, deve cioè essere specificata all'interno delle variabili "esplicite".
### Esempio
... Sch.Var="*CLEAR() NumFat(12)"
Vengono cancellati tutti i valori delle variabili e successivamente viene assegnato il valore 12 alla variabile NumFat

## XML di una scheda
### Concetti generali
L'XML letto dal componente "Scheda" è prodotto dal servizio JATRE_18C interpretando uno script di scheda.
In questo XML sono contenute informazioni relative a : 

- Aspetto grafico - organizzazione della scheda (definizione e disposizione delle sezioni, suddivisione in subsezioni).
- Dati da mostrare in ogni subsezione.
- Relazioni di dinamicità tra le subsezioni.
- Impostazioni relative alle rappresentazioni.


Importante :  i dati da visualizzare in ogni subsezione possono essere già visibili in questo XML oppure possono essere ottenuti mediante una chiamata a una funzione di LOOC.up. (sviluppare)


### Sezioni dell'XML

**Popup (opzionale)**
Contiene un insieme di funzioni aggiuntive da associare alla pressione del tasto destro sugli oggetti presenti nella scheda.

**Setup (opzionale)**
Contiene l'eventuale inizializzazione delle variabili dinamiche usate nella scheda e della stampa.

**Sezioni**
Date le sezioni, contiene informazioni sulle loro subsezioni : 

- forma grafica utilizzata (con eventuale setup).
- dati da rappresentare (espliciti oppure chiamata al servizio che li fornisce).
- eventuali legami di dinamicità tra subsezioni.


**Layout**
Contiene informazioni sulla disposizione e la dimensione delle sezioni della scheda.

## Istruzione mediante esempi
Illustriamo i concetti base che stanno dietro la costruzione di una scheda e le sue potenzialità creando passo-passo una scheda di esempio.
Le istruzioni introdotte in questo primo tutorial sono quelle strettamente necessarie alla definizione di una scheda.

Requisiti per la comprensione del documento : 
 * Familiarità con i concetti principali della scheda.
 * Conoscenza delle chiamate alle funzioni di LOOC.up.

### Una scheda per i clienti
Ipotizziamo di voler creare una scheda personalizzata per i clienti.
Tale scheda conterrà una matrice con i dati di base del cliente, un elenco (sempre sotto forma di matrice) degli ordini di vendita ad esso intestati e qualche etichetta di testo che evidenzia alcuni dati importanti ad esso relativi (ad esempio numero di telefono e indirizzo) : 
<img src="file : [SME.IMG]\TAB£A\LO\LOCEXD\ese_010.png">
Per prima cosa va creato un membro CNCLI, associato all'oggetto cliente, da collocare nel file sorgente SCP_SCH della libreria dei sorgenti personalizzati.
Il membro CNCLI conterrà lo script che descrive la scheda; esso potrà essere modificato : 
 * Dal SEU, operando con un Client Access
 * Dall'editor di Looc.up (con la possibilità di costruzione guidata tramite Ctrl+W)

La scheda verrà chiamata cliccando con il tasto destro su un oggetto di tipo CNCLI e scegliendo "scheda oggetto", oppure con la chiamata equivalente (ad esempio per il cliente 000001) :  F(EXD;*SCO;) 1(CN;CLI;000001)

### 1. Impostazione della struttura grafica
**Sezioni**
La prima operazione da compiere è impostare la struttura grafica delle sottofinestre che compongono
la scheda. Nel nostro caso avremo 4 finestre : 
 * Dati di base
 * Ordini attivi
 * Telefono
 * Indirizzo

Dividiamo prima il nostro foglio in due parti verticali, una per i dati di base e una
per le altre informazioni, mediante i comandi : 
 :  : PAR F(04)
..G.SEZ Pos(A) Dim(60%)
..G.SEZ Pos(B)


Tramite le keyword Pos A e B, alfabetiche, indichiamo di effettuare un partizionamento della scheda in orizzontale; con Dim specifichiamo la dimensione in percentuale della sezione sinistra - non avendolo specificato per B viene assunto il rimanente.
Se non avessimo indicato la dimensione nemmeno per A sarebbero state create per default due sezioni dalla stessa dimensione, 50%.
La sezione B va ripartita a sua volta in 3 finestre, quindi : 
 :  : PAR F(04)
..G.SEZ Pos(B1) Dim(70%)
..G.SEZ Pos(B2) Dim(15%)
..G.SEZ Pos(B3)


Il numero dopo la B fa sì che la sezione B venga partizionata in verticale. La keyword Dim indica sempre la dimensione del livello inferiore (in questo caso delle sottofinestre 1, 2 e 3).
Se definisco le sezioni B1 e B2 non è strettamente necessario definire anche la B (viene fatto implicitamente), a meno che non desideri specificarne la dimensione in relazione alle sezioni dello stesso livello (in questo caso A).
Ad esempio, se avessi tre sezioni A, B e C, con B divisa in B1 e B2, dovrei definire B se volessi dire che B occupa in orizzontale il 20% dello spazio della scheda. Questo perchè la Dim su B1 e B2 specifica le dimensioni in verticale, tra B1 e B2.

**Subsezioni**
Il passo successivo è la definizione delle subsezioni :  bisogna dire a LOOC.up quali componenti chiamare per la rappresentazione delle informazioni in ogni sezione.
Con l'istruzione  :   : G.SUB specifichiamo, immediatamente dopo la definizione di ogni sezione, il tipo di informazione da essa rappresentata e un titolo per la finestra.
Quindi : 
 * Matrice per i dati di base :   :   : G.SUB.MAT Tit="Dati di base"
 * Matrice per gli ordini attivi :   :   : G.SUB.TRE Tit="Ordini attivi"
 * Label per il numero di telefono :   :   : G.SUB.LAB Tit="Telefono"
 * Label per l'indirizzo :   :   : G.SUB.LAB Tit="Indirizzo"

La label non è un componente di Looc.up, ma un metodo interno alla scheda. Non viene chiamato alcun componente esterno per la presentazione, è la scheda stessa che lo visualizza.

### 2. Indicazione dei dati
Dopo avere definito il posizionamento delle finestre e che tipo di dati conterranno è necessario specificare quali dati verranno rappresentati.
Questi dati possono essere specificati direttamente oppure si può chiamare un servizio AS per produrre l'XML che li contiene.
Nel nostro caso : 
 - Per i dati di base si chiama un servizio che produce una matrice con gli attributi intrinseci dell'oggetto CNCLI :   :   : D.FUN.STD F(EXB;*OAV;LIM) P(I         I999999999)
 - Per gli ordini attivi si chiama un servizio che restituisce una matrice di ordini attivi :   :   : D.FUN.STD F(EXB;*BAR;) 1(OJ;*PGM;V5TDOC_B) 2(**;;3L) P(C01(OVE) C02(2) C03(CLI) C04(&OG.K1))
 - Per il numero di telefono e l'indirizzo si specifica direttamente che sono OAV dell'oggetto in ingresso, quindi :   :   : D.OGG D(&OA.I/44) e D.OGG D(&OA.I/03)

Alcune osservazioni : 
 * I dati specificati in 1. e 2. sono chiamate a funzioni di Looc.up, quindi sono rispettivamente i servizi *OAV (pgm JATRE_17C) e *BAR (pgm JATRE_31C) a fornire l'XML contenente i dati
 * Nella chiamata alla funzione in 1. è implicito il parametro 1 :  se non specificato l'Oggetto 1, infatti, viene passato lo stesso con cui è stata chiamata la scheda. In questo caso stiamo trattando una scheda di oggetto, quindi l'Oggetto 1 è proprio valorizzato con l'oggetto in esame. Se la scheda fosse stata chiamata sul cliente 000001, ad esempio, la chiamata equivale a : 
 :   : D.FUN.STD F(EXB;*OAV;LIM) 1(CN;CLI;000001) P(I         I999999999)
 * Nella chiamata alla funzione in 2., "&OG.K1" si riferisce al codice dell'Oggetto 1 con cui è stata chiamata la scheda (nel caso precedente :  000001)
 * L'istruzione  :   : D.OGG (sostituibile dalla sua vecchia versione  :   : D.LAB.STD, sconsigliata) in 3. e 4. specifica manualmente due oggetti. Di questi oggetti forniamo solo la descrizione (coincidente con il valore degli OAV I/44 e I/33 dell'Oggetto 1 con cui è stata chiamata la scheda) :  la label visualizza infatti sempre la descrizione di un oggetto, ricavata dal suo tipo e codice oppure fornita direttamente (come in questo caso).

### Lo script finale
 :  : PAR F(04)
..G.SEZ Pos(A) Dim(60%)
..G.SUB.MAT Tit="Dati di base"
..D.FUN.STD F(EXB;*OAV;LIM) P(I         I99999999)

..G.SEZ Pos(B1) Dim(70%)
..G.SUB.MAT Tit="Ordini attivi"
..D.FUN.STD F(EXB;*BAR;) 1(OJ;*PGM;V5TDOC_B) 2(**;;3L) P(C01(OVE) C02(2) C03(CLI) C04(&OG.K1))

..G.SEZ Pos(B2) Dim(15%)
..G.SUB.LAB Tit="Telefono"
..D.OGG D(&OA.I/44)

..G.SEZ Pos(B3)
..G.SUB.LAB Tit="Indirizzo"
..D.OGG D(&OA.I/03)


### Sottoschede e dinamicità
Estendiamo ora la scheda di esempio creata nel primo tutorial, familiarizzando con i concetti di : 
 * Sottoschede
 * Più subsezioni in una sezione
 * Setup di componente
 * Variabili e dinamicità

### Creazione di sottoschede / più subsezioni in una sezione
Dividiamo la scheda in due sottoschede, una contenente i dati di base e una per la visualizzazione di alcuni dati commerciali (ordini di vendita attivi e relative righe).
Per far questo creiamo una scheda con una sola sezione, corrispondente all'intera finestra della scheda, a cui associamo non una ma due subsezioni di tipo scheda (visualizzate in alternativa nella stessa finestra).
![LOCEXD_04](http://localhost:3000/immagini/LOCEXD_B/LOCEXD_04.png)
Si notino i due tab associati alle subsezioni. Per default viene visualizzata la prima subsezione ("Dati di base"), mentre la subsezione "Dati commerciali" non è ancora caricata (questo è evidenziato dal colore azzurro del testo del tab "Dati commerciali").

Lo script della scheda madre è : 
 :  : PAR F(04)
..G.SEZ Pos(A)
..G.SUB.SCH Tit="Dati di base"
..D.SCH Nam(BASE)
..G.SUB.SCH Tit="Dati commerciali"
..D.SCH Nam(COMMERCIALE)


L'istruzione  :   : D.SCH indica di aprire una sottoscheda definita nello stesso membro della scheda corrente;  :   : D.SCH Nam(SUB) è l'equivalente abbreviato di  :   : D.FUN.STD F(EXD;*SCO;) 1(stesso oggetto) 2(stesso membro) 4(;;SUB), dove nell'oggetto 4 della chiamata si specifica la sottoscheda.

Un'altra possibilità era definire le sottoschede in membri diversi, ad esempio la sottoscheda dei dati commerciali nel membro CNCLI_COM.
In questo caso una chiamata avrebbe potuto essere  :   : D.FUN.STD F(EXD;*SCO;) 1(CN;CLI;&OG.K1) 3(;;COM).

### Una sottoscheda
La sottoscheda di nome "BASE" è compresa tra le istruzioni  :   : I.SCH Nam(BASE) e  :   : I.SCH.END.
Nello script CNCLI, quindi, in coda allo script della scheda madre andranno inserite, per la scheda "Dati di base", le seguenti istruzioni : 
 :  : PAR F(04)
..G.SEZ Pos(A) Dim(60%)
..G.SUB.MAT Tit="Dati di base"
..D.FUN.STD F(EXB;*OAV;LIM) P(I         I99999999)
..G.SEZ Pos(B1)
..G.SUB.LAB Tit="Telefono"
..D.OGG D(&OA.I/44)
..G.SEZ Pos(B2)
..G.SUB.LAB Tit="Fax"
..D.OGG D(&OA.I/45)
..G.SEZ Pos(B3)
..G.SUB.LAB Tit="Indirizzo"
..D.OGG D(&OA.I/03)
..G.SEZ Pos(B4)
..G.SUB.LAB Tit="Partita IVA"
..D.OGG D(&OA.I/08)


### Dinamicità tra subsezioni
Analizziamo ora la sottoscheda "Dati commerciali".
![LOCEXD_05](http://localhost:3000/immagini/LOCEXD_B/LOCEXD_05.png)Nella subsezione in alto vengono presentati gli ordini attivi del cliente, cliccando su una riga parte il caricamento della subsezione in basso che presenta il dettaglio delle righe dell'ordine selezionato : 
![LOCEXD_06](http://localhost:3000/immagini/LOCEXD_B/LOCEXD_06.png)Questo comportamento viene ottenuto specificando un legame di dinamicità tra le due subsezioni :  nella definizione della subsezione "Ordini attivi" si specifica che un click nella subsezione indurrà dinamicità nella subsezione "Righe" : 
 :  : PAR F(04)
..G.DIN Where="Righe" Sch.Var="TDOC([T§TDOC]) NDOC([T§NDOC])"

Questo indica che cliccando sulla subsezione "Ordini attivi" si triggera il ricaricamento della subsezione "Righe", passandogli nelle variabili TDOC e NDOC i contenuti delle colonne di nome T§TDOC e T§NDOC (della riga selezionata).
La keyword Sch.Var indica che TDOC e NDOC sono variabili di scheda, visibili anche nelle altre subsezioni della scheda.
I dati nella subsezione "Righe" vengono caricati con : 
 :  : PAR F(04)
..D.FUN.STD F(EXB;*DR;) 1(DO;[TDOC];[NDOC])

Le parentesi quadre indicano di utilizzare il valore delle variabili TDOC e NDOC nella chiamata.

# Setup di componente
Condizioniamo la rappresentazione dei dati nella subsezione "Righe". Tramite l'istruzione : 
 :  : PAR F(04)
..G.SET.MAT Columns="NUMRIG|R§TRIG|CODOGG|DESOGG|QTAORD|QTACON|CONRIC|CONCON" Load="D"

indichiamo al componente matrice chiamato per la visualizzazione della subsezione "Righe" quali colonne mostrare e in che ordine tra quelle restituite dal servizio *DR, oltre a specificare un caricamento differito della subsezione :  la subsezione viene caricata al click sul suo tab oppure al click su una delle subsezioni che la condizionano dinamicamente.

### Lo script completo
 :  : PAR F(04)
..G.SEZ Pos(A)
..G.SUB.SCH Tit="Dati di base"
..D.SCH Nam(BASE)
..G.SUB.SCH Tit="Dati commerciali"
..D.SCH Nam(COMMERCIALE)

..I.SCH Nam(BASE)
..G.SEZ Pos(A) Dim(60%)
..G.SUB.MAT Tit="Dati di base"
..D.FUN.STD F(EXB;*OAV;LIM) P(I         I99999999)

..G.SEZ Pos(B1)
..G.SUB.LAB Tit="Telefono"
..D.OGG D(&OA.I/44)

..G.SEZ Pos(B2)
..G.SUB.LAB Tit="Fax"
..D.OGG D(&OA.I/45)

..G.SEZ Pos(B3)
..G.SUB.LAB Tit="Indirizzo"
..D.OGG D(&OA.I/03)

..G.SEZ Pos(B4)
..G.SUB.LAB Tit="Partita IVA"
..D.OGG D(&OA.I/08)
..I.SCH.END

..I.SCH Nam(COMMERCIALE)
..G.SEZ Pos(1)
..G.SUB.MAT Tit="Ordini attivi"
..G.DIN Where="Righe" Sch.Var="TDOC([T§TDOC]) NDOC([T§NDOC])"
..D.FUN.STD F(EXB;*BAR;) 1(OJ;*PGM;V5TDOC_B) 2(**;;3L) P(C01(OVE) C02(2) C03(CLI) C04(&OG.K1))

..G.SEZ Pos(2)
..G.SUB.MAT Tit="Righe"
..G.SET.MAT Columns="NUMRIG|R§TRIG|CODOGG|DESOGG|QTAORD|QTACON|CONRIC|CONCON" Load="D"
..D.FUN.STD F(EXB;*DR;) 1(DO;[TDOC];[NDOC])
..I.SCH.END


# Approfondimenti
- [Scheda - approfondimenti](Sorgenti/MB/DOC/LOCEXD_B1)
