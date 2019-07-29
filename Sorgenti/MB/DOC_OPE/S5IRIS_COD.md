E' possibile ottenere una rapprestazione dell'andamento nel tempo delle code su di ogni risorsa specifica.

Essa può essere eseguita : 
* per una risorsa specifica
* per tutte le risorse specifiche di una risorsa generale
* per tutte le risorse

Si può lanciare dalla scheda della schedulazione, cliccando su una risorsa

![FIG_073](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_COD/FIG_073.png)
o dal dettaglio cliccando su di una  cella

![FIG_070](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_COD/FIG_070.png)
o in una zona libera

![FIG_069](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_COD/FIG_069.png)

Nell' esempio seguente viene riportato l'andamento delle code su di una risorsa specifica.
Ogni cella rappresenta il tempo in cui una fase sta in coda, che inizia all'istante del vincolo al più presto (quando la fase può iniziare), e finisce all'istante del suo inizio effettivo.
Ad esempio, all'inizio di agosto si prevede che saranno in coda gli ordini 420862, 420863 e 420864.
La coda sulla prima operazione di ogni ordine non viene riportata, in quanto il vincolo al più presto non esiste, e non avendo l'informazione di quando l'ordine può iniziare, si dovrebbe assumere la data di inizio schedulazione, con l'effetto di sovrastimare in modo arbitrario le code.

![FIG_072](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_COD/FIG_072.png)