# Introduzione

L'obiettivo delle nuove navigazioni è quello di rendere la consultazione delle commesse __agevole__ dal punto di vista della raggiungibilità, e __semplice__ dal punto di vista della comprensione.
Dal punto di vista della raggiungibilità, queste schede possono essere richiamate direttamente dal modulo BRCOMM, mentre dal punto di vista della comprensione queste sono semplici e intuitive perchè ripropongo l'ormai nota struttura a tre sezioni.
Ciascuna sezione ha una funzione ben precisa : 
**1.** la prima verticale a sinistra, dedicata al menù :  questa riporta tutte le azioni e navigazioni più importanti relative alle commesse
**2.** la seconda orizzontale, nella parte alta, dedicata ai filtri e alla loro impostazione
**3.** la terza, che occupa tutta la restante parte, destinata a contenere il risultato della ricerca.
La scheda di navigazione si presenta quindi così : 


![BRCOMM_001](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_001.png)
# Il dashboard del modulo

La prima voce di menù ci permette di accedere al cruscotto del modulo, ovvero una scheda puramente statistica che permette di visionare quante commesse  di un certo tipo sono presenti nel sistema.
La visualizzazione di queste informazioni è sensibile al tipo di raggruppamento, che può essere impostato mediante il campo "Forma" presente sull'input panel.
L'esempio di seguito mostra la visualizzazione di default, con il conteggio delle commesse presenti nel sistema, raggruppate per tipo commessa, livello e stato.

![BRCOMM_002](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_002.png)
# Le navigazioni :  il SURF delle commesse

Per le commesse è stata studiata una navigazione ricca e articolata, organizzata in una decina di SURF diversi. Oltre alle due navigazioni di base per codice commessa e descrizione, sono state previste altre consultazioni come quelle per commessa di riferimento, per responsabile, per articolo, per riferimento, etc..
Ciascuna di queste interrogazioni corrisponde a un SURF preciso, come si può vedere dal dettaglio : 

![BRCOMM_003](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_003.png)
Ciascuna navigazione metterà a disposizione degli specifici filtri. Si consideri per esempio il surf per codice (SURF A).
I filtri che possono essere imposati in questo caso sono per lo più legati alle informazioni di base della commessa. Tra i tanti, quelli più particolari sono : 
** Posizinamento codice :  digitando in questo campo un codice commessa, o solo una sua parte,    sarà possibile visualizzare tutte le commesse a partire da o fino a quel valore inserito.
   Il risultato è quindi sensibile al tipo di ordinamento che si è deciso di imposatre nel campo    A/D (ascendente o discendente)
** Cod/descrizione contiene :  usato in abbinamento agli altri campi, questo filtro permette di    estrarre le commesse che hanno o nel codice o nella descrizione quanto viene inserito dentro qui.
Il risultato di un utilizzo congiunto di tutti e due questi filtri è : 

![BRCOMM_004](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_004.png)
Ciascuno di questi filtri è dotato di una documentazione che ne spiega il significato, l'utilità e lo scopo. A questa si può accedere premendo il tasto funzionale F1 dopo aver posizionato il cursore del mouse sul campo di cui si vuole leggere la documentazione.

![BRCOMM_005](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_005.png)
# Il popup delle opzioni :  il menù di una commessa

Dopo aver confermato i filtri nell'apposita sezione, è possibile visualizzare l'elenco delle commesse nella parte centrale della scheda. La matrice che viene caricata, indipendentemente dallo schema scelto e dal tipo di SURF,  presenta sempre una colonna con una piccola icona (evidenziata in figura) : 

![BRCOMM_006](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_006.png)![BRCOMM_007](http://localhost:3000/immagini/MBDOC_OPE-BRCOMM_01/BRCOMM_007.png)
Questa icona permette di accedere direttamente al menù di popup di una commessa, nel quale sono riportate tutte le azioni di gestione e di interrogazione.
