La schedulazione calcola una serie di indici globali, che possono essere visualizzati dalla scheda ed opzionalmente memorizzati in un record dell'archivio D5COSO se impostato nel campo specifico della tabella dello scenario (S5B).
La chiave di memorizzazione è : 
* Contesto = "TAS5B"
* Tema = "£I1"
* Codice = Scenario (di output, se impostato, altrimenti quello di input)
* Codice 1 = Tipo impegno risorse
* Codice 2 = Ambito
* Data = Data di esecuzione

![FIG_059](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_IND/FIG_059.png)
Gli indici sono i seguenti : 

 - _2_N.ro totale ordini. E' il numero totale di ordini processati dalla schedulazione.
 - _2_N.ro ordini in anticipo. E' il numero di ordini per cui la data consegna schedulata è inferiore alla data consegna richiesta.
 - _2_N.ro ordini puntuali. E' il numero di ordini per cui la data consegna schedulata è uguale alla data consegna richiesta.
 - _2_N.ro ordini in ritardo. E' il numero di ordini per cui la data consegna schedulata è maggior della data consegna richiesta.
 - _2_% ordini in anticipo. E' il rapporto tra gli indici 02 e 01.
 - _2_% ordini puntuali. E' il rapporto tra gli indici 03 e 01.
 - _2_% ordini in ritardo. E' il rapporto tra gli indici 04 e 01.
 - _2_Lateness media. Per ogni ordine di calcola la differenza tra la data fine richiesta e la data fine schedulata :  un anticipo è rappresentato da un numero negativo. La media di queste differenze costituisce la lateness. Il limite di questo indice è che un anticipo è trattato come recupero di un ritardo, il che non è sempre realistico.
 - _2_Lateness deviazione standard. E' dato dalla deviazione stanard della popolazione da cui si calcola l'indice 08.
 - _2_Tardiness media. E' somma di tutti i ritardi (differenza, se positiva, tra la data fine richiesta e la data fine schedulata), divisa per il numero totale degli ordini.
 - _2_Tardiness deviazione standard. E' dato dalla deviazione standard della popolazione da cui si calcola l'indice 11.
 - _2_Tardiness media condizionale. E' somma di tutti i ritardi (differenza, se positiva, tra la data fine richiesta e la data fine schedulata), divisa per il numero degli ordini in ritardo.
 - _2_Tardiness media condizionale deviazione standard. E' dato dalla deviazione stanard della popolazione da cui si calcola l'indice 12.
 - _2_Tardiness massima. E' il valore massimo della differenza, se positiva, tra la data fine'richiesta e la data fine schedulata. Se non c'è nessun ordine in ritardo essa vale 0.
 - _2_Earliness media. E' somma di tutti gli anticipi (differenza, se negativa, tra la data fine richiesta e la data fine schedulata), divisa per il numero totale degli ordini. Dato che questo numero è intrinsecamente negativo, ne viene considerato il valore assoulto.
 - _2_Earliness deviazione standard. E' dato dalla deviazione standard della popolazione da cui si calcola l'indice 15.
 - _2_Earliness media condizionale. E' somma di tutti gli anticipi (differenza, se negativa, tra la data fine richiesta e la data fine schedulata), divisa per il numero degli ordini in anticipo. Dato che questo numero è intrinsecamente negativo, ne viene considerato il valore assoulto.
 - _2_Earliness media condizionale deviazione standard. E' dato dalla deviazione stanard della popolazione da cui si calcola l'indice 17.
 - _2_Earliness massima. E' il valore massimo della differenza, se negativa, tra la data fine richiesta e la data fine schedulata. Dato che questo numero è intrinsecamente negativo, ne viene considerato il valore assoluito. Se non c'è nessun ordine in anticipo essa vale 0.
 - _2_Makespan. Rappresenta l'orizzonte di schedulazione :  è dato dalla differenza, in giorni solari, tra la più alta data fine schedulata e la data di inizio schedulazione.
 - _2_Ore di carico a capacità finita. Sono le ore per cui sono caricate le risorse a capacità finita.
 - _2_Ore di holes a capacità finita. Sono le ore in cui le risorse a capacità finita rimangono inutilizzate.
 - _2_Ore di occupazione a capacità finita. E' la somma degli indici 21 e 22.
 - _2_% saturazione. E' la percentuale di utilizzo delle risorse a capacità finita :  è dato dal rapporto tra l'indice 21 e l'indice 23.
 - _2_Ore di carico a capacità infinita. Sono le ore per cui sono caricate le risorse a capacità infinita.
 - _2_Ore di carico totali. E' la somma degli indici 21 e 25.

