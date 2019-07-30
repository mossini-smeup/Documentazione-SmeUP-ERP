# Documentazione tecnica B£FIND

Il Cerca è uno strumento che consente la costruzione di ricerche.

Un **Contesto** raggruppa una o più _Categorie**.
Ad ogni **Categoria** corrisponde una query di ricerca.


Quando un Contesto è composto da più Categorie è possibile fare in modo che l'utente veda le singole Categorie oppure che veda soltanto il Contesto (nel cui caso vengono eseguite in sequenza tutte le query delle Categorie associate mostrando insieme tutti i risultati ottenuti).


Per ogni **Contesto**  (tag FND.RIC) : 

- è necessario indicare le categorie, cioè le query da eseguire per il contesto, sotto forma di elenco separato da ;
- è possibile indicare il livello utente (classe di autorizzazione USRLVL) in base alla quale si è autorizzati al contesto di ricerca
- è possibile indicare un elenco di oggetti, separati da virgola, a cui la ricerca si riferisce
- è possibile indicare quale categoria utilizzare per la ricerca per codice (!)
- è possibile indicare quale categoria utilizzare per la ricerca per descrizione (?)
- è possibile indicare se si desidera che le categorie del contesto siano visibili ed eseguibili singolarmente nell'albero dei contesti disponibili
- è possibile indicare che i risultati della ricerca devono essere sottoposti a calcolo del rating
- è possibile indicare che la ricerca supporta l'applicazione di uno schema
- è possibile indicare che la ricerca supporta l'applicazione di un filtro



Per ogni **Categoria**  (tag FND.CAT) : 

- è necessario impostare l'SQL della query da eseguire per la ricerca
- è necessario indicare il campo (o la concatenazione di campi) sui quali viene eseguita la ricerca
- è possibile indicare una where implicita che viene aggiunta nel caso il servizio riceva nella funzione l'oggetto 1
- è possibile indicare i campi dell'order by della query eseguita
- è possibile indicare il livello utente (classe di autorizzazione USRLVL) in base alla quale si è autorizzati al contesto di ricerca
- è possibile indicare un elenco di oggetti, separati da virgola, a cui la ricerca si riferisce
- è possibile indicare che una query sta eseguendo la ricerca sulle note
- è possibile indicare che una query sta eseguendo la ricerca sui parametri
- è possibile indicare che i risultati della ricerca devono essere sottoposti a calcolo del rating
- è possibile indicare che la ricerca supporta l'applicazione di uno schema
- è possibile indicare che la ricerca supporta l'applicazione di un filtro
- è possibile indicare una funzione in sovrascrittura rispetto alla funzione eseguita al doppio click sul codice oggetto dei risultati


## Costruzione della query di ricerca
La query di ricerca viene costruita combinando le seguenti proprietà del tag FND.CAT

**Sql** :  contiene la select dei campi estratti, la cui struttura deve avere la seguente struttura : 

- oggetto (tipo + parametro)
- codice dell'oggetto
- descrizione dell'oggetto (nel caso sia lasciato '' effettua la £DEC)
- contenuto (di solito uguale alla concatenazione di campi su cui viene eseguita la ricerca)

seguita dalla where che deve terminare con &CO.FND (che verrà sostituito con il like di ciò che sto cercando)
Es. :  Sql="SELECT 'CN' CONCAT E§TRAG, E§CRAG, E§RAGS, E§RAGS CONCAT E§RAGA FROM BRENTI0F  WHERE &CO.FND"

**SRic** :  contiene la concatenazione dei campi su cui verrà fatta la scansione di ricerca della stringa
Es. :  SRic="E§RAGS CONCAT E§RAGA"

**SOrd** :  contiene campi di ordinamento della query
 Es. :  SOrd="E§RAGS, E§RAGA"



## Ricezione di un oggetto (come oggetto 1 della chiamata al B£SER_26)
Se ricevuto l'oggetto 1, tale oggetto viene utlizzato per filtrare solamente i contesti e le categorie compatibili con tale oggetto.
Al tempo stesso il codice (£UIBK1) viene utilizzato per la composizione dell'eventuale where implicita (proprietà FOgg del tag FND.CAT).
Ad esempio, se viene ricevuto come oggetto 1(OG;CN;CLI) e FOgg="AND E§TRAG = '&CO.K1 '" la where implicita risultante sarà _AND E§TRAG = 'CLI '_ .

## Dove vengono fisicamente eseguite le ricerche?
Alcune ricerche (come quelle sulla documentazione, sulle news, e, più in generale, quelle contenute negli script, o comunque in membri) vengono eseguite sul file B£FIND0F, che viene riempito a richiesta o in modo schedulato a partire dai membri dei file sorgenti (nel tab Azioni del Set&Play è accessibile il menù per la ricostruzione del file).
Le altre sono invece delle query effettuate direttamente sui file di database di riferimento degli oggetti (ad esempio TABEL per le tabelle, BRENTI0F per gli enti e BRARTI0F per gli articoli.

## Come posso schedulare l'aggiornamento del file B£FIND0F?
Per aggiornare il file B£FIND0F impostare come schedulazione SMEUP per l'ambiente desiderato il richiamo CALL B£UT26H PARM('ALL.UPD') .
La schedulazione deve essere effettuata tramite la scheda B£WSME_JS come schedulazione SMEUP, in modo che sia possibile lanciare il programma con l'ambiente corretto. Per questo si rimanda a : 
 :  : DEC T(MB) P(DOC_NWS) K(NWS001549)
- [Lancio&-x2f;Esecuzione Programma batch](Sorgenti/MB/DOC/A£BASE_SM)

## Devo necessariamente impostare delle query per ogni oggetto?
No. Nel caso per un oggetto non siano presenti delle query il cerca aggiunge automaticamente due categorie COD e DES che permettono la ricerca per codice e descrizione tramite £G60.

