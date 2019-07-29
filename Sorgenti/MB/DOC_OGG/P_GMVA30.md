### Creazione sintesi di magazzino da chiusura
La funzione crea la sintesi valorizzata di magazzino partendo, per ogni articolo, dalla giacenza finale dell'ultimo esercizio ed applicando la sommatoria algebrica dei carichi / scarichi derivati dai movimenti memorizzati, periodo per periodo, nell'archivio degli indici storici.

![GMVA30_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMVA30/GMVA30_01.png)
La sintesi valorizzata viene costruita utilizzando le modalità e le caratteristiche associate (nella tabella GM3) allo scenario in input.
Il tipo costo definisce il costo da utilizzare nella valorizzazione della sintesi, l'esercizio è definito nella tabella PER e costituisce il nome della sintesi valorizzata.
Il limite periodo rappresenta il periodo superiore (tratto dall'archivo indici storici) a cui si deve fermare la creazione sintesi magazzino.
Vengono eseguiti dei controlli di congruenza tra l'esercizio, il limite periodo e i periodi memorizzati nell'archivio indici storici.
