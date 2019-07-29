## Definizione e utilizzi

Una lista di oggetti è un elenco di istanze di oggetti che può essere creato definendo le singole istanze da includere nella lista oppure definendo una condizione che deve essere verificata affinchè un'istanza venga inclusa all'interno della lista.
Riferendoci a un esempio specifico si potrebbe creare una lista di clienti indicando i singoli codici da includere nella lista oppure definire la condizione "Nazione=Italia" che consente di includere tutti i clienti italiani.
E' possibile utilizzare una lista di oggetti non solo nelle interrogazioni in lista ma anche all'interno delle parzializzazioni. L'utilizzo delle liste all'interno delle parzializzazioni non è definito per tutti i campi ma solo per quelli che si presentano sottolineati : 

![B£BASE_005](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_005.png)
In particolare, le liste riportate nel campo a sinistra di un oggetto definiscono le istanze da includere nella parzializzazione mentre quelle riportate a destra definiscono le istanze da escludere : 

![B£BASE_006](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_006.png)
## Creazione

Per creare una lista inserire uno dei caratteri di ricerca classici di Smeup ('!' '?') all'interno del campo in cui viene richiesta la lista : 

![B£BASE_007](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_007.png)
In questo modo si apre l'elenco delle liste disponibili. Per creare una nuova lista è necessario compilare la prima linea (che si presenta vuota) digitando l'opzione 1 e indicando codice e descrizione della lista : 

![B£BASE_008](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_008.png)
Dando invio compare lo specchietto per l'inserimento delle istanze da includere nella lista. A questo punto si hanno due modalità disponibili : 

- Inserimento delle singole istanze :  con questa modalità è possibile elencare le singole istanze da includere nella lista : 

![B£BASE_009](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_009.png)

- Definizione di una condizione sugli attributi delle istanze da includere nella lista :  per attivare questa modalità è necessario compilare il campo 'Attributi' con 1 e indicare nella lista il codice dell'attributo su cui si intende applicare la condizione e i limiti della condizione stessa. Se viene compilato solo il limite inferiore il sistema considera solo quelle istanze il cui attributo ha il valore riportato nel limite inferiore. Se vengono compilati entrambe i limiti, il sistema considera quelle istanze il cui attributo ha valore compreso tra limite inferiore e limite superiore.

![B£BASE_010](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_010.png)


Terminata la compilazione delle istanze da includere nella lista è necessario confermare con F6.
A questo punto è sufficiente scegliere la lista creata con una X : 

![B£BASE_011](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_011.png)
## Modifica

Per modificare una lista esistente utilizzare l'opzione D : 

![B£BASE_012](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_012.png)
In questo modo verrà visualizzata la lista creata e da qui sarà possibile modificarla.

## Richiamo

Per utilizzare una lista all'intenro di un'interrogazione è sufficiente indicare il codice della lista nel campo specifico : 

![B£BASE_013](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_013.png)
E' sempre possibile utilizzare i caratteri speciali di ricerca per visualizzare le liste disponibili e scegliere poi la lista desiderata con una X.
Il richiamo delle liste all'intenro delle parzializzazioni avviene compilando il campo da filtrare con _NomeLista mentre per effettuare la ricerca sarà necessario utilizzare il carattere '_' prima dei caratteri speciali : 

![B£BASE_014](http://localhost:3000/immagini/MBDOC_OPE-B£_LIS/BXBASE_014.png)