# Introduzione
La schedulazione di una fase consiste nell'aggiornare il contenuto della memoria del dettaglio ricevuto nella variabile £A05.
Il programma che esegue questa funzione è il S5SMES_13

# Descrizione azioni eseguite
Si fissa l'inizio dell'operazione come l'istante maggiore tra la disponibilità della risorsa e il vincolo più restrittivo sull'impegno.
A partire da esso si determina la fine dell'operazione.
Se essa è a capacità finita e non iniziata, al tempo di esecuzione aggiunge l'attrezzaggio (eventualmente ricalcolato con una exit specifica, in base alla differenza con quanto eseguito in precedenza sulla stessa risorsa).

Se è a capacità infinita, l'operazione viene schedulata col calendario della risorsa principale, nel seguente modo
 * si avanza della coda se il tempo di carico è zero oppure se la coda ha il significato di tempo di attraversamento, impostato nel tipo coda in tabella gruppo risorsa (BRM) a cui appartiene la risorsa
 * altrimenti
 ** se iniziata si avanza con il tempo di carico
 ** se non iniziata si avanza della coda per determinare l'inizio dell'operazione, e successivamente si avanza del tempo di carico per determinare la fine dell'operazione.

Si aggiornano poi la sintesi dell'ordine, l'istante di fine occupazione della risorsa specifica, e si crea una hole se l'inizio dell'operazione è maggiore della fine dell'occupazione precedente.

Si eliminano qundi le alternative della stessa fase, e si rende pronta l'operazione successiva, variandone lo stato e determinando l'istante al più presto (tenendo conto, se prevista, della sovrapposizione).

Se essa è su una risorsa a capacità finita si esamina la possiblilità di accostamento, se impostato in tabella scenario. Se l'accostamento è possibile, si schedula questa seconda operazione e si ripete il ciclo.
Ricordo che l'accostamento standard prevede di eseguire, se possibile, la fase successiva a quella schedulata, sulla stessa risorsa specifica e subito dopo la precedente.

Se essa è invece su una risorsa a capacità infinita viene subito schedulata, e si ripete il ciclo fino a quando si incontra un'operazione su una risorsa a capacità finita o si giunge all'ultima operazione dell'ordine.

In quest'ultimo caso, se previsto, si passa all'esame degli appuntamenti statici (i legami con gli ordini di livello superiore).

