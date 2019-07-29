## Abstract

Il componente TagCloud permette di renderizzare una nuvola di etichette (tag cloud), una forma di visualizzazione di dati che mostra un gruppo di etichette di grandezza differente, la quale viene utilizzata spesso per rappresentare gli argomenti più trattati all'interno di un sito web. Le voci sono generalmente associate a link che portano alle pagine collegati a quell'argomento. Le tag cloud sono infatti spesso usate come strumenti di navigazione.

In Sme.UP il componente TagCloud recupera i dati da una matrice. Esso opera su due colonne definibili nel setup, la colonna da cui ricavare le label e la colonna di pesi di tipo numerico da cui ricavare la dimensione del tag. La dimensione del tag (denominata strenght) potrà essere un valore da 1 a 5 (su parametro di setup è ammessa anche la classe speciale 0). Per approfondimenti sulle modalità di trasformazione dei pesi in strenght vedere la sezione sugli algoritmi.
