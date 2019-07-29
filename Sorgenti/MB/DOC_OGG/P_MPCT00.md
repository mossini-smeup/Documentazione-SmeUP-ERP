## Confronto verticale tra viste
Questa funzione confronta, fissato un periodo (colonna di MPS) i valori di viste diverse, a pari coppie di oggetti, ottenendo sia indici globali degli scostamenti (media, deviazione standard), sia una rappresentazione dettagliata (una riga per ogni elemento di MPS, con i valori originali, le differenze, le differenze percentuali, ecc..).

Tale analisi risulta utile, ad esempio, nell'ambito di un processo di previsioni, in cui, a posteriori, si può confrontare la previsione con l'effettivo risultato, oppure, sempre a posteriori, mettere a confronto due modalità diverse di previsioni.

## Data
Si imposta la data in cui si intende eseguire il confronto.

## Azioni memorizzate
Se si imposta una memorizzazione di parzializzazione MPS, essa agisce come filtro sul Piano/Vista base.

## Piano/Vista
Il Piano/Vista base è obbligatorio :  i confronti vengono eseguiti verso i suoi valori.

Il Piano/Vista di confronto 1 è anch'esso obbligatorio :  si confrontano i suoi valori con quelli del piano base.

Il Piano/Vista di confronto 2 è facoltativo. Se impostato, si confrontano anche i suoi valori con quelli del piano base, ed inoltre si evidenzia il migliore (tra il primo e il secondo) nell'avvicinarsi al base.

## Periodi
Impostando la data, vengono determinati, per ogni piano, il periodo e gli estremi (inizio e fine) a cui essa appartiene.
E' obbligatorio che la data inserita sia compresa in un periodo per ogni piano impostato, mentre non viene controllato che gli estremi dei periodi interessati di ogni piano (che vengono visualizzati) siano gli stessi per tutti i piani.

## Selezione
La partenza è una vista del piano base :  è a partire dai suoi record (coppie di oggetti) che viene eseguito il confronto.
Per i piani 1 e 2 si può scegliere di considerarli anche se assenti, mentre normalmente il confronto viene eseguito solo sui record presenti su tutti i piani.

Inoltre, per tutte le viste piano, si può decidere se escludere i record che hanno, nella cella del periodo selezionato, un valore negativo oppure negativo o nullo. Le condizioni valgono contemporaneamente, es : 
 * se per il piano/vista 1 si sceglie di assumere solo i positivi
 * mentre per il piano/vista 2 si sceglie di assumere solo i valori a zero e positivi
 * se è soddisfatta la prima condizione ma non la seconda, il record viene escluso dal confronto.

## Risultati
Nella sintesi viene riportata la media e la deviazione standard della serie, ottenuta come differenza percentuale tra il valore della vista 1 (oppure 2) e quello della vista base.

Per ogni record (chiave 1 e 2) nel dettaglio vengono riportati i valori della vista 1, della vista base, la loro differenza e la differenza percentuale, sia con segno sia in valore assoluto.
Viene inoltre calcolata l'accuracy, definita come  : **complemento a 100 del valore assoluto della differenza percentuale, limitato inferiormente a zero.
Se i due valori (della vista di confronto e della vista base) sono uguali, l'accuracy è del 100 %. Se l'errore percentuale è maggiore del 100 %, e quindi si avrebbe un valore negativo, l'accuracy è comunque zero. Essa è qunidi un indice insensibile a differenze elevate.

Se è impostato anche il piano/vista 2, si riportano gli stessi valori, ed inoltre si segnala, in grassetto, quale delle due viste si avvicina maggiormente alla base.
Viene quindi riportato il delta, calcolato come differenza tra i valori assoluti delle  due differenze percentuali.
Viene riportato infine un segnale che indica se si avvicina maggiormente alla base la vista 1, oppure la 2, oppure se pareggiano.

Se si è scelto di riportare anche i record assenti, la cella corrispondente viene evidenziata in rosso.
