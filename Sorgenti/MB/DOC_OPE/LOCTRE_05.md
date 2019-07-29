I tasti funzionali associati al componente sono : 

 *  F9 :  espande interamente l'albero
 *  F10 :  collassa interamente l'albero
 *  F17 :  apre la gestione dei setup.

Mentre i comandi rapidi sono : 

-  CTRL + S :  permette di passare dalla visualizzazione a 'Stella' a quella a 'Albero' e viceversa. Il comando si attiva solo dopo aver selezionato l'opzione 'Visualizza come' nel menù di PopUp della sezione.
-  CTRL + T :  (in fase di sviluppo) digitando il comando (o premendo il relativo pulsante) è possibile digitare una parola nel campo 'Trova' :  in questo modo il sistema ricerca ed evidenzia la prima occorrenza  della parola indicata. Digitando nuovamente il comando il sistema restituirà la seconda occorrenza della parola e così via.  Il comando si attiva solo dopo aver selezionato l'opzione 'Visualizza come' nel menù di popup della sezione.

![LOCTRE_033](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_033.png)
-  CTRL + F (o ALT+F9) :  abilita la linea di comando per l'esecuzione di funzioni sull'albero selezionato (affinchè il comando funzioni è necessario selezionare un nodo). E' possibile eseguire differenti tipologie di comando :  la ricerca semplice, il filtro, la selezione multipla, l'esecuzione di funzioni (come ad esempio l'aggiunta dei nodi selezionati ad un carrello).

Qui di seguito saranno elencati i vari comandi : 

1) Per eseguire una ricerca semplice è necessario compilare il campo 'Comando' con _ F : ParolaCercata (o scrivendo per esteso il comando 'FIND : '). In questo modo la parola indicata verrà cercata all'interno dei nodi e delle foglie dell'albero, i quali verranno  evidenziati nel caso la parola stessa venisse individuata : 

![LOCTRE_030](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_030.png)
2) Per filtrare le voci dell'albero è, invece, necessario compilare il campo 'Comando' che si apre ai piedi della subsezione con _K : ParolaCercata_ (o scrivendo per esteso il comando 'KEY : '). In questo modo la parola indicata verrà ricercata all'interno dei nodi e delle foglie dell'albero e verrà eseguito un vero e proprio filtro, lasciando visualizzati solo i nodi le cui foglie contengono la parola indicata : 

![LOCTRE_032](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_032.png)
3) Per selezionare una serie di nodi, è necessario compilare il campo 'Comando' con _ S : ParolaCercata  (o scrivendo per esteso il comando 'SELECT : '). In questo modo la parola indicata viene ricercata all'interno dei nodi e delle foglie dell'albero e vengono selezionati i nodi in cui essa viene individuata (lo strumento è utile nel caso si voglia ad esempio aggiungere una serie di nodi ad un carrello). E' possibile inoltre selezionare ad uno ad uno i nodi desiderati premendo CTRL+click del mouse sul nodo desiderato : 

![LOCTRE_031](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_031.png)
Per eseguire l'aggiunta ad un carrello dei nodi selezionati vi sono varie modalità : 
* Premento ALT+C (o andando sulla voce di menù popup :  carrelli->appunti ) i nodi selezionati vengono aggiunti al carrello appunti (carrello *LAST). Il carrello contiene un solo oggetto per ogni
tipologia.
* Premendo ALT+W (o andando sulla voce di menù popup :  carrelli->di lavoro) i nodi selezionati vengono aggiunti al carrello di lavoro (carrello *WORK). Il carrello può contenere N oggetti per ogni
tipologia.
* Premendo ALT+O (o andando sulla voce di menù popup :  carrelli->standard componenti graf.) i nodi selezionati vengono aggiunti al carrello OGGETTO (funzionalità utile per raggruppare gli oggetti per tipo). Se i nodi selezionati sono di tipologie differenti, vengono creati N carrelli suddivisi per tipo di oggetto.

Per aggiungere i nodi selezionati al carrello generico *DRAG è necessario compilare il campo 'Comando' con_ E : _  (o scrivendo per esteso il comando 'EXECUTE : CARRELLO'). La stessa funzionalità può essere ottenuta facendo ALT+doppio click su uno dei nodi selezionati dell'albero, con il menù di popup, o con il drag del mouse (funzionalità disponibile solo se l'albero ha l'attributo DRAG='MULTI').
Questa funzionalità è utile per raggruppare in un unico carrello tutti gli oggetti, anche se eterogenei.

![LOCTRE_039](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_039.png)
Il risultato ottenuto può essere visto andando sulla voce di menù popup :  Carrell >> Carrelli utente

![LOCTRE_040](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_040.png)
Per maggiori informazioni sulle funzionalità del carrello consultare la documentazione relativa : 
- [Carrello](Sorgenti/MB/DOC/B£CARR)

4) Per modificare le impostazioni di visualizzazione dell'albero è necessario compilare il campo 'Comando' con_ SETUP : _. E' possibile mostrare e nascondere il codice e testo del nodo, mostrare e nascondere icone, riordinare i nodi dell'albero in ordine crescente o decrescente.
Nota :  i comandi eseguiti non sono permanenti, ma sono relativi alla sola vista corrente. Alla riapertura del componente, o all'aggiornamento dello stesso, si ritornerà alle impostazioni caricate da setup.

Di seguito vengono presentati un elenco con alcuni comandi di setup possibili : 
* SETUP : -TEXTTYPE CODE    (per mostrare solo il codice del nodo)
* SETUP : -TEXTTYPE TEXT     (per mostrare solo il testo del nodo)
* SETUP : -TEXTTYPE BOTH    (per mostrare sia il codice sia il testo del nodo)
* SETUP : -ICONE NO              (per nascondere le iconeassociate al nodo, vengono mostrate le icone generiche. Se il nodo non ha il tipo/parametro/codice non viene mostrata alcuna icona.)
* SETUP : -ICONE YES             (per mostrare le icone associate al nodo)
* SETUP : -ICONE SPECIFIC     (per mostrare solo le icone specificate nell'attributo I="" del nodo. Se l'attributo non è specificato non viene mostrata alcuna icona.)
* SETUP : -SORT ASC              (per riordinare l'albero in ordine crescente)
* SETUP : -SORT DES              (per riordinare l'albero in ordine decrescente)
* SETUP : -SORT NONE           (per togliere gli ordinamenti dell'albero)

E' possibile modificare più impostazioni contemporaneamente come segue : 
SETUP : -TEXTTYPE BOTH -SORT DES -ICONE SPECIFIC

![LOCTRE_038](http://localhost:3000/immagini/MBDOC_OPE-LOCTRE_05/LOCTRE_038.png)alcuna icona poichè non specificata nell'attributo I="" dei nodi.)

Per velocizzare alcune operazioni è possibile eseguire alcuni alias da linea di comando : 

| 
| .COL Txt="Comando" A="R" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| - +1 | espande l'albero di un livello |
| - -1  | collassa l'albero di un livello |
| - +A | espande l'albero totalmente |
| - -A  | collassa l'albero totalmente |
| - +S | riordina l'albero in ordine alfabetico crescente |
| - -S  | riordina l'albero in ordine alfabetico decrescente |
| 

