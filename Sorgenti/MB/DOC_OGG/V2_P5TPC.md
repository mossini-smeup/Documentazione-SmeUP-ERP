# P5TPC     -  TIPO CODA
Definisce come vieno trattato il valore della coda impostato nella risorsa.
La differenza tra i campi alfabetici e quelli numerici è che i secondi trattano la coda come tempo di attraversamento
e quindi l'inizio dell'operazione è prima della coda.
Se la coda è un tempo di carico, si attivano i seguenti comportamenti : 
- viene sempre applicata, anche su operazioni contigue sulla stessa risorsa principale (nel caso di coda effettiva, invece essa viene applicata solo alla prima operazione).
- se presente, sostituisce il tempo di carico effettivo, nella schedulazione a capacità infinita.
L'approssimazione alla giornata opera, nella schedulazione a capacità infinita, nel seguente modo : 
- l'istante di inizio viene approssimato all'inizio giornata, nella schedulazione al più tardi (partendo dalla fine, all'indietro.
- l'istante di fine viene approssimato alla fine giornata, nella schedulazione al più presto (partendo dall'inizio, in avanti.
