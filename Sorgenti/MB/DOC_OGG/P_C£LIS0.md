# Gestione Listini

### Generalità
In Sme.up i listini sono basati su una struttura di dati che ne permette un utilizzo estremamente libero quando risulta necessario associare ad un gruppo di dati dei valori, dei codici e/o dei numeri.
L'applicazione più comune è l'associazione a  articolo / ente di un prezzo unitario e fino a 4 possibili sconti, il tutto con una data ed una quantità di fornitura di validità.
Per comodità di spiegazione nella documentazione faremo riferimento ad un listino di acquisto, dove in genere esiste un prezzo per un determinato articolo fornito da un particolare fornitore (la principale differenza possibile con i listini di vendita è che in genere nella vendita esiste un prezzo stabilito per articolo con delle eccezioni per particolari clienti, questa particolarità è compresa nella possibilità di descrivere un listino sia per codici cliente specificati che per codici cliente generici "**").

### Definizioni
 :  : T04 Area
L'area definisce il campo di applicazione del listino, normalmente nelle applicazioni Sme.up si utilizza l'area blank, ma in casi particolari si possono utilizzare aree specifiche, avremo ad esempio area SI per listini di simulazione. L'area è rappresentata da un sottosettore della tabella C£L dei listini.

 :  : T04 Listino
Viene inserito nella tabella C£L, identifica il gruppo di informazioni associate, ad esempio possiamo parlare di listino acquisti, listino vendite Italia, listino vendite CEE, listino vendite extraCEE, ecc...
Un listino riporta una o più sezioni dove sono descritti con maggiore dettaglio gli argomenti gestiti.
Un listino è anche appartenente ad una categoria.
Sul listino si stabilisce anche il grado di autorizzazione necessario per la sua gestione (interrogazione, modifica).
Ogni Fornitore / Cliente deve avere un listino associato, altrimenti il listino viene chiesto in fase di creazione dell'ordine.

 :  : T04 Categoria
Classifica il tipo di listino, ad esempio la categoria dei listini di acquisto e quella dei listini di vendita, è definita nella tabella C£*_CL.
A livello  di tipologia documento (V5D) o tipologia ente (BRE) si può definire una categoria che sarà utilizzata come condizione di validità nel listino. Ai clienti, ad esempio, potrò assegnare solo listini di vendita ecc..

 :  : T04 Sezione
Gestita negli opportuni sottosettori della tabella C£V, permette di definire all'interno di un listino una ulteriore scomposizione in cui si compone il  listino.

Le sezioni individuano quelle parti del listino che si riferiscono ad un insieme di informazioni congruenti. Ad esempio possiamo avere il listino  vendite che è costituito dalle sezioni dei prezzi, dalle sezioni delle provvigioni, dalle sezioni sconti e/o maggiorazioni, della sezione del costo di assistenza,dalla sezione attrezzature, dalla sezione trasporti, ecc..
La sezione del listino definisce li seguenti caratteristiche particolari : 

- Griglia di controllo degli oggetti a cui è intestata la sezione del listino (es. fornitore / articolo)
- Se gestita la valuta
- Se gestito il lotto (se è usato come limite inferiore o superiore)
- Se gestita la data di validità (se è usata come limite inferiore o superiore)

Descrizione dei campi valore utilizzati nella sezione. Nota, le descrizioni dei campi valore sono codificate nei sottosettori della tabella C£H (il sottosettore è specificato nella sezione).


## Formato guida gestione listino
Per accedere alla gestione di un listino si parte dal formato seguente : 

![C£LIST_01](http://localhost:3000/immagini/MBDOC_OGG-P_C£LIS0/CXLIST_01.png)
devono essere inseriti opportunamente il codice listino e la sezione, in base alla sezione inserita si configurano i successivi campi di input della videata.
Le opzioni sono quelle standard con in aggiunta : 

- VA - variazione, apre il formato di variazione di massa dei listini che sarà spiegato in seguito;
- ML - Modifica in lista, fissato uno dei campi chiave (es. articolo) presenta la lista con tutti i valori relativi, è possibile mantenere direttamente tutti i campi modificabili presentati.

Se invece non si sceglie una delle opzioni particolari la gestione è quella standard.
Quando non si compila nessuna opzione viene presentata la solita lista, nella gestione listini, seuno dei possibili campi chiave è compilato la lista si presenta ordinata secondo il campo chiaveed il valore inserito serve come posizionamento della lista.

![C£LIST_03](http://localhost:3000/immagini/MBDOC_OGG-P_C£LIS0/CXLIST_03.png)
Entrando nel formato di gestione al dettaglio si presentano tutti i campi gestibili : 

![C£LIST_04](http://localhost:3000/immagini/MBDOC_OGG-P_C£LIS0/CXLIST_04.png)