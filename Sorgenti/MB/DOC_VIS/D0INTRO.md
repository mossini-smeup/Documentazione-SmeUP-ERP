# Visione Costi Avanzati

## Copertura applicativa
Nella figura seguente vengono evidenzate, all'interno della mappa applicativa, le aree supportate da Acos.Up
![D5BASE_002](http://localhost:3000/immagini/MBDOC_VIS-D0INTRO/D5BASE_002.png)
## Funzionalità
L'applicazione supporta la gestione di costi, principalmente il calcolo dei costi di un articolo, ma utilizzando il modulo costi multicontesto è possibile anche la determinazione del costo di altri oggetti Sme.UP quali : 
* riga di documento del ciclo esterno
* ordini di produzione
* lotto qualità
* commessa

Per lo stesso oggetto possono coesistere diversi "tipi costo" differenziati ad esempio per la modalità del calcolo (es. costo ultimo, costo puntuale, costo medio ponderato, ...) il costo è "datato" dove il periodo di riferiemnto può essere una data puntuale oppure un periodo (mese, anno).
I costi possono essere : 
* **calcolati**, con calcolo di massa oppure per singolo oggetto, e memorizzati nell'apposito file
* "**dinamici**" con determinazione al volo leggendo direttamente le informazioni all'origine

sono possibili "risalite" ad un altro tipo costo qualora non sia stato tovato il costo desiderato.

Ad esempio possiamo avere un costo di acquisto materiali dinamico che legge il costo dall'ultima fattura di acquisto, in mancanza legge l'ultimo ordine di acquisto ed in mancanza di questo legge il listino valido alla data del fornitore preferenziale.
