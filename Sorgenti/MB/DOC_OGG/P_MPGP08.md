## Navigazione tra viste piano
Con questa funzione, data una coppia di elementi di una vista piano, è possibile navigare attraverso tutte le viste relazionate con essa e selezionarne una per visualizzare tutte le entità 2 corrispondenti all'entità 1 e viceversa della vista piano di partenza.

## Schermo Guida
![MP_001_23A](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP08/MP_001_23A.png) * Il campo "Codice piano" definisce il piano su cui agire. Esso è obbligatorio ed è riferito alla rispettiva tabella su cui è possibile la ricerca.
 * Il campo "Vista piano" definisce il piano su cui agire. Esso è obbligatorio ed è riferito alla rispettiva tabella su cui è possibile la ricerca.
 * I campi di input successivi contengono le entità definite dalla vista piano e sono collegati ai rispettivi archivi di riferimento sui quali è possibile la ricerca.

## Ricerche particolari
![MP_001_23B](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP08/MP_001_23B.png)Sui campi di input delle entità dipendenti dalla vista piano è possibile, mediante la barra inclinata "/ '', attivare la ricerca mirata al contenuto dell'archivio dei piani :  il sistema presenta una videata con la lista degli elementi relativi all'entità su cui è stata messa la barra.
Dalla lista, mediante il comando funzione F14, è possibile vedere informazioni di dettaglio (quantità per periodo) e da qui, sempre con il comando funzione F14, si può ritornare alla lista precedente.
Con F18 si può accedere ad una videata in cui raggruppare più periodi, ottenendo una lista di quantità sommarizzate per gruppo di periodi.
Sia dalla lista di dettaglio che da quella di sintesi, attraverso le opzioni, è possibile : 
 * selezionare l'entità (portandola sullo schermo guida);
 * passare alla lista della seconda entità;
 * andare in ricerca delle viste piano con informazioni presenti in archivio;
 * andare in ricerca dei piani con informazioni presenti in archivio.

## Schermo viste collegate
Dopo aver compilato i campi relativi a piano, vista piano ed entità relative, il sistema presenta nella videata di lista tutte le viste collegate : 

![MP_001_23](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP08/MP_001_23.png)
Nella lista sono presentate le seguenti informazioni : 
 * viste piano collegate (con cui si intendono tutte le viste piano aventi almeno una delle entità caratteristiche della vista piano in input);
 * codice della vista piano collegata;
 * prima entità della vista piano in input;
 * seconda entità della vista piano in input;
 * collegati (entità diverse da quelle della vista piano in input, ma appartenenti alle altre viste piano collegate).

Sono possibili le seguenti attività : 
* sostituire la vista di riferimento (quella compilata nel formato guida) con una di quelle listate (la sostituzione si ottiene inserendo una "X" in corrispondenza di uno dei campi di input posti a
sinistra della colonna intestata "Codice")

>N.B. :  sono intercambiabili solo le viste piano con la stessa coppia di entità presenti nello stesso ordine (codice 1 / codice 2).
 * accedere alle informazioni contenute in una delle viste collegate e relative a una delle entità in input (l'accesso si ottiene inserendo una "X" in corrispondenza di uno dei campi di input posti nelle colonne intestate con i nomi delle entità o con "Collegati")
Nell'esempio, immettendo una "X" in corrispondenza del campo collaboratore della vista piano >P-D si ottiene la seguente videata : 

![MP_001_24](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP08/MP_001_24.png)
Sulla testata il sistema riporta i dati della vista piano di cui si è richiesta la visualizzazione (piano, vista, entità di cui si vogliono vedere i dati collegati).
Con il comando funzione F14 si può passare al dettaglio : 

![MP_001_25](http://localhost:3000/immagini/MBDOC_OGG-P_MPGP08/MP_001_25.png)