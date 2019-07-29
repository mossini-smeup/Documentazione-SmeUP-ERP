### Frontiera
E' un campo obbligatorio. Si imposta l'ultimo periodo che, nella serie di input, viene considerato "nel passato". La previsione inizia ad essere calcolata dal periodo successivo.

### Numero periodi di previsione
E' un campo obbligatorio. Indica il numero di periodi, a partire da quello successivo alla frontiera, per cui si calcola la previsione. La somma dei periodi di previsione e della frontiera non può superare 120, per non sfondare i periodi del piano. Questo controllo implica che sia la frontiera sia la previsione siano, singolarmente, minori di questo valore.

### Numero periodi di storia
E' un campo obbligatorio. Indica il numero di periodi, a partire dalla frontiera all'indietro, che vengono utilizzati per la determinazione dei parametri di calcolo del metodo. Non può quindi essere maggiore della frontiera, altrimenti provocherebbe uno sfondamento nel passato.
