# Struttura della scheda di ricerca

La scheda di ricerca è composta da due sottoschede principali : 
* **Ricerca** :  la prima sottoscheda in cui viene riportata la funzione di ricerca scelta e dalla quale potrà essere selezionata l'istanza dell'oggetto ricercato (nell'immagine evidenziata nel riquadro arancio)
* **Altre Ricerche** :  la seconda sottoscheda in cui è possibile sfruttare tutte le forme di ricerca previste per la classe oggetto (nell'immagine evidenziata dal riquadro verde)

![B£EQRY_10](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_10.png)
# Utilizzo della scheda di ricerca

Solitamente la prima sottoscheda è a sua volta divisa di due ulteriori sezioni : 
* **Parametri di selezione** :  la sezione orizzontale in alto attraverso la quale, il risultato della ricerca può essere ristretto ai particolari criteri di ricerca previsti dalla funzione specifica (nell'immagine evidenziata nel riquadro azzurro).
* **Risultato della sezione** :  la sezione in basso, attraverso la quale, può essere selezionata l'istanza in interessata (nell'immagine evidenziata nel riquadro giallo)

![B£EQRY_13](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_13.png)
Le scelte della richiesta parametri possono essere confermate o tramite la pressione del tasto invio o tramite click sul bottoncino riportato all'estrema destra della richiesta parametri.

La singola istanza, una volta posizionatisi sulla riga corrispondente può essere selezionata, alternativamente nei seguenti modi : 
* Premendo il tasto funzione F06
* Premendo il tasto funzione Invio
* Posizionandosi sulla cella sull'estremai sinistra e facendo click con il mouse (o premendo la barra spaziatrice che vi corrisponde)

![B£EQRY_14](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_14.png)
# Funzionalità Comuni della Gestione della selezione

Ogni forma di ricerca presente ha le sue specificità di selezione, ma all'interno di ognuna sono ricorrenti anche altre funzionalità : 
* **Filtri Aggiuntivi** :  se l'oggetto appartiene ad un archivio, sarà attivo il tasto F13, attraverso cui, il risultato della ricerca potrà essere filtrato mediante qualsiasi campo dell'archivio di appartenenza dell'oggetto

![B£EQRY_15](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_15.png)![B£EQRY_16](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_16.png)
Quando il tasto F13 è stato utilizzato tale utilizzo viene evidenziato sia tramite l'indicazione riportata ad inizio pagina "Filtro Attivo" che tramite la scritta attribuita al tasto F13 che da "Gestione Filtro", si modifica in "Filtro Attivo".
![B£EQRY_17](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_17.png)
* **Schema colonne** :  solitamente nei parametri di selezione è presente un campo "Schema", tramite tale campo è possibile visualizzare differenti modelli di informazioni già predisposti. A tali modelli possono poi essere applicate le funzionalità di setup presenti in ogni matrice ed attraverso cui la presentazione può essere ulteriormente personalizzata. Va inoltre considerato che salvo per la forma di ricerca sia stato previsto uno schema predefinito è possibile modificare lo schema di default attraverso l'apposita funzione che verrà descritta a seguire.

![B£EQRY_18](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_18.png)![B£EQRY_19](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_19.png)
* **Ordinamento** :  a volte può essere inoltre presente un campo "Ordinamento", se presente, tramite questo campo può essere modificato l'ordine di caricamento del risultato. NOTA BENE :  è importante notare che l'eventuale modifica dell'ordinamento tramite la gestione dei setup, non influisce sul reale ordinamento di caricamento dei dati. L'effetto dell'ordinamento tramite setup viene applicato solo ai dati caricati, il cui caricamento avviene attraverso quando previsto dalla funzione di ricerca.

* **Nr righe** :  tramite questo campo è possibile condizionare il numero di righe che verrà presentato sulla prima pagina. Se per la selezione i risultati sono maggiori, sarà possibile paginare per visualizzare gli ulteriori risultati. NOTA BENE :  ad ogni paginazione verrà caricato un numero di righe doppio rispetto a quello caricato sino a quel momento (es. partendo da una prima di pagina di 100, la seconda sarà di 200, la terza di 400, la quarta di 800, ecc.)

# Indicazioni particolari all'interno della scheda di ricerca.

Nelle schermata di ricerca sono presenti alcune indicazioni particolari, il cui scopo è dare delle informazioni relative alle modalità di avvio della scheda di ricerca, quando questa viene avviata da un campo di imputazione. Nello specifico : 
* Nelle l'elenco delle ricerche i caratteri indicati fra parentesi "!"," : ", "?" identificano le forme di ricerca che corrispondono all'avvio della scheda di ricerca quando questa avviene tramite uno di tali caratteri speciali.
![B£EQRY_20](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_20.png)
* Nella sezione per la gestione della selezione, nella parte relativa alla richiesta parametri, potranno invece essere indicati fra parentesi nelle intestazioni i caratteri : 
** **"!"** :  per indicare che quel particolare campo verrà riempito con i caratteri che seguono il "!" nel campo di imputazione da cui è stata fatta partire la ricerca (es. "!111", i caratteri 111 saranno quelli che finiranno in tale campo di selezione
** **" : "** :  per indicare che quel particolare campo verrà riempito con i caratteri che seguono il " : " nel campo di imputazione da cui è stata fatta partire la ricerca (es. " : BRE", i caratteri BRE saranno quelli che finiranno in tale campo di selezione
** **"?"** :  per indicare che quel particolare campo verrà riempito con i caratteri che seguono il "!" nel campo di imputazione da cui è stata fatta partire la ricerca (es. "!111", i caratteri 111 saranno quelli che finiranno in tale campo di selezione
** **"+"** :  in presenza dell'indicazione con il + significa che tale campo verrà riempito a seguito di ricerca lanciata tramite il carattere "+". Se viene lanciata la query di default (quindi senza indicare specificatamente la query) verranno considerati come parametri tutti i campi a seguito del "+" considerando come carattere di suddivisione il ".". Se al contrario viene lanciata una query specifica (es. +LOCA, la fine del codice della query e l'inizio dei parametri dovrà essere a sua volta suddiviso tramite un "."

![B£EQRY_21](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_21.png)
Va inoltre notato che nell'elenco delle ricerche sono presenti due importanti informazioni che permettono di identificare il codice di una ricerca :  attraverso queste due indicazioni è possibile determinare il codice della ricerca che si può utilizzare nell'avvio della ricerca tramite il carattere "+".

A fianco di ogni ricerca è indicato un codice, a questo va aggiunto l'eventuale prefisso indicato nel gruppo. Se questo prefisso è presente il codice della ricerca sarà dato da "prefisso/codice", viceversa sarà sufficente il codice. Per le ricerche evidenziate nell'immagine a seguire la ricerca potrà essere rispettivamente lanciata nei seguenti modi : 
* "+F/C"
* "+BASE"

![B£EQRY_22](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_22.png)
# Altre ricerche

In questa sottoscheda abbiamo oltre che alla sezione di ricerca, una sezione di sinistra in cui sono elencate tutte le forme di ricerca previste per la classe oggetto. Cliccando su una delle voci di tale albero verrà lanciata sulla destra la corrispondente funzione di ricerca da cui potrà essere selezionata l'istanza dell'oggetto ricercato.

![B£EQRY_12](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_12.png)
# Scelta default

Nell'albero dell'elenco delle ricerche è possibile attraverso la voce riportata in fondo "Scelta Default", lanciare la funzione attraverso la quale è possibile fissare alcuni default : 
* Lo schema :  se indicato, sarà lo schema che verrà utilizzato su tutte le ricerche ad eccezione di quelle ricerche che prevedono un loro schema specifico di default
* La ricerca :  quella qui indicata è la ricerca che viene avviata con la sola indicazione del carattere "+". Se a seguire di questo carattere non viene indicato il codice specifico di una forma di ricerca i caratteri a seguire son considerati come parametri della ricerca di default. Tramite tale indicazione inoltre si sovrascrive l'eventuale scelta effettuata nelle ricerche speciali previste dalla struttura emulazione (++).
* nr righe :  il valore indicato corrisponderà al numero di righe caricato sulla prima pagina di ogni forma di ricerca

![B£EQRY_24](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_24.png)
![B£EQRY_25](http://localhost:3000/immagini/MBDOC_SCH-B£EQRY_SEA/BXEQRY_25.png)


