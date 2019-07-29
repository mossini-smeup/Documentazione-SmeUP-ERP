### Mantiene negativi
Il calcolo può produrre valori di previsione negativi. Se impostato questo valore, essi, nella parte di previsione effettiva (oltre la frontiera) verranno mantenuti, se invece viene lasciato vuoto, verranno portati a zero. Nella parte storica (previsioni dall'inizio della storia alla frontiera) i negativi vengono sempre mantenuti, essendo valori utilizzati nel calcolo dello scostamento tra realtà e previsione, e quindi un loro azzeramento implicherebbe una riduzione arbitraria dello scostamento stesso.

### N. Decimali di arrotondamento
Se impostato un valore da 0 a 3, si esegue l'arrotondamento per il numero corrispondente di decimali. A differenza dell'azzeramento dei negativi, l'arrotondamento viene eseguito su tutta la previsione, sia effettiva sia storica.
