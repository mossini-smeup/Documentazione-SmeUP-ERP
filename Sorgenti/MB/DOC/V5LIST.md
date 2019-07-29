## Generalità
La gestione listini permette di associare dei valori numerici ad un gruppo di oggetti (da 1 a 3). Il caso classico è il prezzo di un  articolo per un cliente.

Le informazioni principali sono : 
## Area
L'area definisce il campo di applicazione del listino; normalmente nelle applicazioni Sme.up si utilizza l'area blank, ma in casi particolari si possono utilizzare aree specifiche; protemmo avere ad esempio area SI per listini di simulazione.
L'area è rappresentata da un sottosettore della tabella C£L dei listini.

## Listino
Viene inserito nella tabella C£L, identifica il gruppo di informazioni associate, ad esempio possiamo parlare di listino acquisti, listino vendite Italia, listino vendite CEE, listino vendite extraCEE, ecc.
Un listino riporta una o più sezioni dove sono descritti con maggiore dettaglio gli argomenti gestiti.
Un listino è anche appartenente ad una categoria.
Sul listino si stabilisce anche il grado di autorizzazione necessario per la sua gestione (interrogazione, modifica).
Ogni Fornitore / Cliente deve avere un listino associato, se manca viene chiesto in fase di creazione del documento.

## Categoria
Classifica il tipo di listino, ad esempio la categoria dei listini di acquisto e quella dei listini di vendita, è definita nella tabella C£*_CL.
A livello di tipologia documento (V5D) o tipologia ente (BRE) si può definire una categoria che sarà utilizzata come condizione di validità nel listino. Ai clienti, ad esempio, potrò assegnare solo listini di vendita ecc..

## Sezione
Gestita negli opportuni sottosettori della tabella C£V, permette di definire all'interno di un listino una ulteriore scomposizione in cui si compone il listino.

Le sezioni individuano quelle parti del listino che si riferiscono ad un insieme di informazioni congruenti. Ad esempio possiamo avere il listino vendite che è costituito dalle sezioni dei prezzi, dalle sezioni delle provvigioni, dalle sezioni sconti e/o maggiorazioni, della sezione del costo di assistenza, dalla sezione attrezzature, dalla sezione trasporti, ecc..

La sezione del listino definisce le seguenti caratteristiche particolari : 
 * Griglia di controllo degli oggetti a cui è intestata la sezione del listino (es. fornitore articolo)
 * Se gestita la valuta
 * Se gestito il lotto (se è usato come limite inferiore o superiore)
 * Se gestita la data di validità (se è usata come limite inferiore, superiore o entrambe)
 * Descrizione dei campi valore utilizzati nella sezione. (_3_Nota, le descrizioni dei campi valore sono codificate nei sottosettori della tabella C£H il sottosettore è specificato nella sezione).
