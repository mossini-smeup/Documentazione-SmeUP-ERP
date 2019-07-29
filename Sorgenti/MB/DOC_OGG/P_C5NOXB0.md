## Obiettivo
Attraverso questa funzione è possibile analizzare la situazione attuale dei rapporti bancari e la previsione della stessa a una certa data. In particolare, è possibile indicare una Data situazione e una Data previsione e visualizzare all'interno di una stampa i valori dei saldi effettivi e simulati a queste due date.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D030_027](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXB0/C5D030_027.png)
All'interno del formato guida è necessario selezionare l'azienda d'interesse; per questa funzione è disponibilie la sola modalità stampa che restituisce un file all'interno dello spool.
I campi 'Pertinenza' e 'Condizione' devono essere compilati in funzione della tipologia di registrazioni che si vogliono considerare per il calcolo della situazione dei rapporti. In particolare nel campo Pertinenza è necessario indicare se considerare solo registrazioni gestionali, solo contabili o entrambe mentre nel campo Condizione è possibile indicare se considerare solo registrazioni attive, solo simulate o entrambe.
Nei campi 'Data situazione' e 'Data proiezione' è possibile indicare a che data visualizzare rispettivamente il saldo effettivo e previsionale dei rapporti bancari selezionati.
Nel campo 'Tipi rapporto' è necessario indicare per quali tipologie di rapporti visualizzare i saldi.

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Ordinamento :  permette di definire l'ordinamento di visualizzazione dei record; le scelte disponibili sono per tipo rapporto/banca oppure per banca/tipo rapporto.
 * Impostazioni generali : permette di definire le impostazioni della stampa e visualizzare o meno a inizio stampa la pagina delle impostazioni.

### Tasti funzionali
* F06 Conferma. Conferma l'esecuzione della funzione
* F11 Parametri esecuzione. Permette di definire i parametri di lancio della stampa
* F17 Impostazioni. Permette di accedere alla schermata delle impostazioni.

## Output
La stampa prodotta attraverso questa funzione avrà il seguente aspetto : 

![C5D030_028](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXB0/C5D030_028.png)
Nella parte superiore della stampa sono riportati i parametri di lancio; in particolare, è possibile visualizzare la Data situazione e la Data previsione.
All'interno dei record per ogni rapporto bancario sono riportati i seguenti campi : 
 * Saldo effettivo in avere o in dare alla data situazione
 * Saldo simulato in avere o in dare alla data situazione
 * Saldo totale in avere o in dare alla data situazione che deriva dalla somma dei primi due valori
 * Valore dei movimenti previsti in avere nell'arco di tempo che va dalla data situazione alla data previsione
 * Valore dei movimenti previsti in dare nell'arco di tempo che va dalla data situazione alla data previsione
 * Valore del saldo totale alla data previsione
