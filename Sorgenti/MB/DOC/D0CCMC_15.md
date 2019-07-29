# Costo Rimanenze Articolo

Il Costo Rimanenze Articolo è un costo che determina il valore di magazzino di una giacenza.

E' diviso in due parti
* >Costo
* >Quantità

## Costo
Il costo è determinato dalla lettura del tipo costo indicato nei parameti di lancio come "Tipo costo Materiali"  : 
Come costo si considerano tutte le sue voci. Comprese ricariche. Diventa un costo unitario.

## Quantità
Le quantità possono essere determinate con due diversi metodi : 
>Magazzino fisico
La quantità è la giacenza dell'articolo, in tutti i magazzini, alla data di calcolo del costo
La giacenza alla data è determinata dai rogrammi standard £GMC.
>Magazzino fiscale__n
La quantità è la giacenza finale dell'articolo, in tutti i magazzini fiscali, nell'esercizio(Anno) relativo alla dala di calcolo del costo
La giacenza alla data è determinata dalla lettura diretta del file dei magazzini fiscali GMSIAN

La rimanenza è data da tutte le voci di costo miltiplicate per la quantità
E' un costo totale.
