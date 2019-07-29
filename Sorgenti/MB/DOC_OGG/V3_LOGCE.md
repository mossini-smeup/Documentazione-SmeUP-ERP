# LOGCE - STILI GRAFICI
Gli stili grafici sono codici che facilitano l'assegnazione delle proprietà grafiche di una cella (colore, sfondo, stile, ecc...) senza dover ricorrere a SETUP estesi.


## MODO DI UTILIZZO
Le celle grafiche possono essere utilizzate degli XML delle matrici e delle stampe.
Per attivare su una cella il carattere grafico, si deve impostare la cella precedente nel seuente modo : 
. nella colonna "H" si inserisce il carattere "G"
. nel campo dell'oggetto si inserisce un codice di cella grafica
Questa cella risulerà nascosta (il carattere "G" corrisponde ad "H").
Lo stile verrà applicato, in base alla codifica della cella grafica, unicamente alla cella successiva, oppure a tutte le celle fino ad incontrare una nuova cella "G" vuota (senza oggetto).


## DEFINIZIONE STILI
Gli stili possono essere definiti implicitamente oppure esplicitamente.
Il modo implicito è la composizione di una stringa di cinque caratteri numerici, ciascuno dei quali identifica una caratteristica
1) Colore
2) Stile
3) Colore dello sfondo
4) Font
5) Continuazione (se "1" lo stile si applica a tutte le celle successive, fino al termine)

E' inoltre possibile definire stili in modo esplicto, inserendoli nello scrpit J3_SET_STD di SCP_SCH.
In esso si inseriscono il nome dello stile e, in modo esplicto, le sue carratteristiche (colore, sfondo, ecc..) ad eccezione della continuazione.

Esistono infine alcuni stili "base"  con il primo carattere *, definiti direttamente dal client.

Esistono inotre stili utilizzati dall'emulatore, descritti in V2/ATTVI, e rimappati (con le stesse caratteristiche) nello script degli stili espliciti.
NON esiste nessuna risalita :  l'emulatore usa gli stili di V2/ATTVI, la scheda utlizza l'insieme degli stili espliciti ed impliciti.
















