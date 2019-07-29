## Generalità
ACOS.UP (congiuntamente a DELT.UP) è un sistema flessibile di calcolo, archiviazione e interrogazione costi atto a riprodurre la struttura rappresentativa desiderata dall'azienda.
ACOS.UP si occupa principalmente delle procedure di calcolo, DELT.UP delle strutture di archiviazione e interrogazione.

Nella nostra realizzazione abbiamo seguito le seguenti linee guida, nello spirito di tutte le applicazioni Sme_Up. : 
 * Impostazione dei dati di base al livello più alto possibile (meccanismo dell'ereditarietà delle proprietà ai livelli inferiori)
 * Indipendenza dall'ambiente gestionale
 * Modularità
 * Possibilità di simulare a video ogni singolo passo
 * Ampia parametrizzazione delle scelte

Le caratteristiche salienti sono le seguenti : 
 * possibilità di gestire differenti tipi costi e differenti metodologie di calcolo (costi fiscali, gestionali, di simulazione, etc.)
 * gestione efficiente della massa di dati ed anche delle particolarità (controllo errori di calcolo, risalita su differenti modelli di calcolo, etc.)
 * integrazione e modularità dell'informazione di costo all'interno del gestionale (valorizzazione giacenze e movimenti di magazzino, valorizzazioni fiscali di magazzino, valorizzazione di scenari budget di acquisto, vendita e produzione, etc.)
 * unificazione e protezione delle informazioni

## Approccio al problema
La maggiore difficoltà nell'affrontare l'installazione del modulo consiste nell'estrema variabilità delle esigenze e degli obiettivi del calcolo costi, che spesso coesistono nella stessa azienda ed evolvono : 
 * fornire indicazioni per la determinazione del prezzo minimo di vendita dei prodotti finiti (prezzo di vendita che consente di coprire tutti i costi a livello di società più un margine percentuale) in fase di preventivazione
 * fornire indicazioni per l'approccio di problematiche di "make or buy" di componenti o lavorazioni
* fornire la valorizzazione fiscale e gestionale dei magazzini
 * fornire indicazioni relative al costo a consuntivo delle commessa e/o dei componenti
 * comporre un modello realistico di costruzione dei costi che includa e rappresenti le variabili significative dell'attività (centri di costo, utilizzo delle risorse, costi dei fattori produttivi, etc.) e consenta di analizzare scenari di variazione
 * fornire una rappresentazione dell'efficienza di utilizzo delle macchine di produzione
 * fornire una rappresentazione dell'efficienza delle prestazioni delle funzioni aziendali
 * ecc...
Tale variabilità si riflette in una molteplicità di procedure aziendali, di responsabilità e di strumenti. Limitandoci agli strumenti, ACOS.UP affronta il problema della variabilità tramite : 
 * flessibilità nella definizione della struttura di costo
 * flessibilità nella definizione dell'impianto di calcolo
### Struttura di costo
La struttura di costo può essere così schematizzata : 

 - _2_definizione del contesto dei costi, (avremo ad esempio costi per articolo, per articolo/magazzino/ubicazione, articolo/cliente, articolo/fase di produzione, etc.) _2_(tabelle D5O e D5S)
 - _2_definizione dell'intervallo di tempo di validità, o periodicità di calcolo (mensile, annuale, etc.) _2_(tabella PER)
 - _2_definizione di una struttura flessibile del dettaglio del costo, (materiali, lavorazioni esterne, lavoro, macchina, attrezzaggio, scarto, parte fissa, variabile, ricariche varie, etc.) _2_(tabella IGI)

![D0BASE_01](http://localhost:3000/immagini/D0BASE/D0BASE_01.png)
### Richiamo programma di gestione
 :  : INI
 :  : CMD CALL PGM(D5CO01G)
 :  : FIN
