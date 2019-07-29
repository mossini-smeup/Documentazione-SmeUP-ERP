# Generalità
Per la gestione di una packing esistono diverse modalità che dipendono dai parametri di chiamata del programma o dalle opzioni scelte : 
 * _2_Costruzione packing list progressiva dal bar-code degli articoli (_1_Opzione = PC), con questa modalità si prevede di creare i dati del collo, successivamente attribuire al collo i vari articoli inserendo codice e quantità, al riempimento del collo se ne crea uno nuovo e si riprende il ciclo fino alla conclusione
 * _2_Preparazione manuale packing list (_1_Opzione = PM), prevede la creazione di un collo e subito dopo la presentazione della lista articoli da imballare, per ogni articolo si inserisce la qtà imballata fino al riempimento del collo, poi si passa alla creazione del successivo e si riprende il ciclo.
 * _2_Gestione packing list (_1_Opzione = PK), permette la visualizzazione completa della packing list
 * _2_Gestione packing list libera, questa è la gestione completa in cui le opzioni del formato guida sono libere e permettono di fare tutto quanto visto in precedenza oltre a cose sue specifiche.

# Costruzione Packing List Progressiva
Si presenta il formato iniziale seguente con preimpostata l'opzione PC : 

![SP_03_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_02.png)
Inserire il numero di richiesta di movimentazione e premere INVIO, si presenta il formato seguente : 

![SP_03_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_03.png)
Se alla packing list abbiamo già associato dei colli in questo formato potremmo richiamarne uno per continuare il riempimento, se invece non abbiamo ancora creato nessun collo oppure volgiamo crearne uno nuovo utilizziamo il tasto F24, il sistema richiede di inserire la tipologia del collo, chiamato anche unità di movimentazione (presente nella tabella GMD), una volta selezionato il tipo collo si presenta il formato successivo dove inserire gli articoli / quantità : 

![SP_03_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_04.png)
Gli articoli, ovviamente, sono quelli che sono stati prelevati nella richiesta di movimentazione, la quantità è la quantità prelevata (in un collo si può mettere la qtà parziale di una articolo, ma la qtà totale di un articolo in tutti i colli non può essere superiore alla qtà totale prelevata).

È prevista la ricerca contestuale con il carattere speciale "/" che presenta gli articoli appartenenti alla richiesta di movimentazione.

Dopo aver selezionato l'articolo inserire la quantità e premere INVIO, si può inserire un nuovo articolo / qtà e così via fino al riempimento del collo.
Quando questo è pieno premere il tasto F24 per chiudere l'attività su questo collo e partire con uno nuovo.

## Packing List
Con il tasto F15 si può vedere la packing list al punto di completamento in cui è arrivata : 

![SP_03_05](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_05.png)
Nella packing list vediamo la lista dei colli presenti, con peso netto e peso lordo (calcolati) e sotto a ciascun collo l'elenco degli contenuti, per ogni articolo è indicata la qtà presente nel collo, la qtà totale da imballare, la qtà totale imballata.

Nella packing list sono previste : 
 * Modifica collo
 * Cancellazione collo
 * Modifica articolo
 * Cancellazione articolo

### Modifica collo
Se selezionata si apre il formato di dettaglio del collo dove possono essere modificati i suoi dati caratteristici : 

![SP_03_06](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_06.png)
### Cancellazione collo
Svuota il collo e rende l'articolo libero per altri imballi.

### Modifica articolo
Permette di modificare la qtà imballata dell'articolo nel collo in questione : 

![SP_03_07](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_07.png)
La diminuzione della qtà, libera l'articolo per poterlo aggiungere ad altri imballi, l'aumento della qtà sottrae l'articolo ad altri possibili imballi.

### Cancellazione articolo
Svuota il collo e rende l'articolo libero per altri imballi.

## Preparazione Manuale
Con il tasto F14 si attiva la preparazione manuale :  si presenta la lista dei colli attualmente presenti : 

![SP_03_08](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_08.png)
### Creazione nuovi colli
Con il tasto F24 si possono creare nuovi colli, viene chiesto il tipo unità di movimentazione poi si passa direttamente alla lista degli articoli ancora da imballare dove si possono inserire direttamente, per ciascun articolo, le qtà imballate nel collo : 

![SP_03_10](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_10.png)
### Dettaglio collo
Presenta la lista degli articoli, sia quelli già presenti all'interno del collo che quelli ancora da imballare, si può modificare la qtà di articoli gia presenti o inserire nuove qtà per articoli che vengono messi nel collo : 

![SP_03_09](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_09.png)
### Copia
L'opzione 3 crea un nuovo collo copiandone le caratteristiche da quello scelto.

# Preparazione manuale Packing List
Si presenta il formato iniziale seguente con preimpostata l'opzione PM : 

![SP_03_11](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_11.png)
Inserire il numero di richiesta di movimentazione e premere INVIO, si presenta il formato seguente : 

![SP_03_12](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_12.png)
Tasto F24 per creare il primo collo, poi tutto come visto al paragrafo "_2_Preparazione manuale" del capitolo precedente.

# Gestione Packing List
Si presenta il formato iniziale seguente con preimpostata l'opzione PK : 

![SP_03_14](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_14.png)
Inserire il numero di richiesta di movimentazione e premere INVIO, si presenta il formato della packing list il cui utilizzo è già stato spiegato nel paragrafo "_2_Packing List" del capitolo precedente : 

![SP_03_13](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_13.png)
# Gestione Packing List Libera
Si presenta il formato iniziale seguente, dove le opzioni sono libere : 

![SP_03_15](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_15.png)
A seconda dell'opzione scelta abbiamo una delle gestioni viste in precedenza, da notare l'opzione FU (funzioni di servizio) da utilizzare nel caso una caduta di sistema abbia interrotto a metà l'attività su una packing list. In questo caso no si riesce a riprendere il lavoro su quelle richiesta di movimentazione fino a quando non si attiva l'opzione FU : 

![SP_03_16](http://localhost:3000/immagini/MBDOC_OGG-P_GMPK01/SP_03_16.png)
Selezionando poi come tipo di elaborazione "Ripresa Work File".
