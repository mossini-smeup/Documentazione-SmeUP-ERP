## Previsioni con Regressione lineare
### Introduzione
Questo passo calcola, a partire da una vista di input**(vista storico)**la previsione futura, con il metodo della regressione lineare.
Si determina la retta che meglio interpola la vista di input, minimizzandone la distanza con i valori della vista, e su di essa si calcolano ii valori della vista di output**(vista previsioni).
### Impostazioni
Il piano deve essere a periodi omogenei (a mesi, settimane, ecc..). Tutti i valori da impostare (periodi di previsione, di storia, ecc..) vanno impostati in questa unità di misura.
### Frontiera
E' un campo obbligatorio. Si imposta l'ultimo periodo che, nella serie di input, viene considerato "nel passato". La previsione inizia ad essere calcolata dal periodo successivo.

### Numero periodi di previsione
E' un campo obbligatorio. Indica il numero di periodi, a partire da quello successivo alla frontiera, per cui si calcola la previsione. La somma dei periodi di previsione e della frontiera non può superare 120, per non sfondare i periodi del piano. Questo controllo implica che sia la frontiera sia la previsione siano, singolarmente, minori di questo valore.

### Numero periodi di storia
E' un campo obbligatorio. Indica il numero di periodi, a partire dalla frontiera all'indietro, che vengono utilizzati per la determinazione dei parametri di calcolo del metodo. Non può quindi essere maggiore della frontiera, altrimenti provocherebbe uno sfondamento nel passato.
### Esempio di impostazione periodi
Con i seguenti valori : 
* Frontiera = 35
* N. Periodi di Storia = 24
* N. Periodi di Previsione = 12
Si ottiene la seguente griglia : 
* Storia :  dal periodo 12 al 35 (estremi compresi)
* Previsione :  dal periodo 36 al periodo 47 (estremi compresi)
### Mantiene negativi
Il calcolo può produrre valori di previsione negativi. Se impostato questo valore, essi, nella parte di previsione effettiva (oltre la frontiera) verranno mantenuti, se invece viene lasciato vuoto, verranno portati a zero. Nella parte storica (previsioni dall'inizio della storia alla frontiera) i negativi vengono sempre mantenuti, essendo valori utilizzati nel calcolo dello scostamento tra realtà e previsione, e quindi un loro azzeramento implicherebbe una riduzione arbitraria dello scostamento stesso.

### N. Decimali di arrotondamento
Se impostato un valore da 0 a 3, si esegue l'arrotondamento per il numero corrispondente di decimali. A differenza dell'azzeramento dei negativi, l'arrotondamento viene eseguito su tutta la previsione, sia effettiva sia storica.
