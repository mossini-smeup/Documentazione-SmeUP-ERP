Un processo è un insieme di compiti, eseguiti sia da persone, sia in modo automatico, collegate tra loro da precedenze.
La rappresentazione delle dinamiche di esecuzione di un processo avviene mediante il modello delle reti di Petri, descritte nel seguito.
La definizione di una rete di Petri viene effettuata in uno script collegato al processo.

# Componenti elementari
I componenti elementari che descrivono un processo sono i seguenti : 
 * Transizione :  rappresenta un compito da eseguire, graficamente è descritta con un rettangolo.
 * Luogo :  rappresenta una posizione a cui può essere giunto un processo, graficamente descritto con un cerchio.
 * Arco (orientato) collega una transizione ad un luogo, o viceversa; graficamente viene descritto da una freccia.
 * Token :  rappresenta lo stato di attivazione di un luogo; graficamente è un pallino nero all'interno del luogo. NB :  in un dato istante possono essere presenti più token su luoghi diversi in una rete di Petri.

Un processo deve iniziare e terminare con dei luoghi.

Vediamo di seguito un semplice esempio di processo, costituito dai luoghi L01, L02, L03 e dalle transizioni T01, T02. Il luogo L01 contiene un token.
![WF-FIG0003](http://localhost:3000/immagini/WFBASE_015/WF-FIG0003.png)# Esecuzione di un processo
Un processo viene eseguito eseguendo alcune o tutte le transizioni che lo compongono (svolgimento dei compiti previsti).

L'esecuzione di una transizione si compone di due elementi : 
 * I requisiti per cui essa può avvenire. In prima istanza una transizione può scattare quando tutti i luoghi in ingresso sono attivi (presenza di token).
 * Le conseguenze prodotte quando essa avviene :  vengono eliminati tutti i token dei luoghi precedenti, ed aggiunti a tutti i luoghi a cui essa punta.

All'inizio del processo tutti i luoghi di partenza contengono un token. Nell'esempio illustrato in queste condizioni la transizione T01 è eseguibile, perchè il suo luogo in ingresso (L01) contiene un token.

L'esecuzione della transizione T01 toglie il token dal luogo L01 e ne mette uno nel luogo L02 :  a questo punto T01 non può più essere eseguita e diventa attiva T02 : 
![WF-FIG0004](http://localhost:3000/immagini/WFBASE_015/WF-FIG0004.png)L'esecuzione di T02 sposta il token da L02 a L03 : 
![WF-FIG0005](http://localhost:3000/immagini/WFBASE_015/WF-FIG0005.png)Dal momento che il luogo L03 è finale (non porta in nessuna transizione) il processo è terminato.

L'esempio appena illustrato rappresenta quindi un semplice processo composto da due compiti in sequenza.

# Esempi

## Mutua esclusione
![WF-FIG0006](http://localhost:3000/immagini/WFBASE_015/WF-FIG0006.png)Sia T01 che T02 possono essere eseguite, perchè il luogo in ingresso ad entrambe (L01) contiene un token.
L'esecuzione di una delle due transizioni (ad es. T01) toglie il token dal luogo L01 (disattivando così l'altra transizione, ad es. T02) e lo mette nel luogo L02.
Dal momento che il luogo L03 è finale (non porta in nessuna transizione) il processo è terminato : 

## Parallelismo
![WF-FIG0007](http://localhost:3000/immagini/WFBASE_015/WF-FIG0007.png)Sia T01 che T02 possono essere eseguite, perchè l luoghi in ingresso ad entrambe (L01/L02) contiengono un token.
L'esecuzione di T01 e di T02 sposta i token, rispettivamente, da L01 a L03 e da L02 a L04; la transizione successiva, T03, può quindi essere eseguita solo dopo l'esecuzione sia di T01 che di T02, perchè deve esserci un token sia in L02 che in L04.

## Diramazioni complesse
![WF-FIG0008](http://localhost:3000/immagini/WFBASE_015/WF-FIG0008.png)All'esecuzione della transizione T01 il processo può chiedere all'utente di scegliere in quale luogo, L02 o L03, mettere il token :  nel primo caso viene attivata la transizione T02, la cui esecuzione riattiverà la T01 (eseguendo quindi un loop), mentre nel secondo la T03.

Si noti che configurazioni alternative della transizione T01 potrebbero implicare : 
 * tutti i luoghi (L02, L03) vengono riempiti automaticamente dall'esecuzione della transizione T01 :  in questo modo T02 e T03 si attivano contemporaneamente.
 * i luoghi (uno o più) in cui deve essere posto il token vengono calcolati automaticamente dal motore di workflow, eventualmente sulla base di ragionamenti complessi.

Queste diverse configurazioni non sono rappresentate graficamente (sono impostazioni di script) ma danno luogo a comportamenti diversi dei processi.


# In pratica

 * Si definisce un processo, compilando in uno script la rete di Petri che lo definisce.
 * Si possono così istanziare degli ordini di workflow sulla base del modello definito
 ** un ordine è costituito da più impegni, ognuno modellato da una transizione nella rete di Petri del processo
 ** si attivano gli impegni per cui è attiva (eseguibile) la relativa transizione nella rete di Petri
 ** l'esecuzione di un impegno è l'esecuzione della relativa transizione, per cui viene aggiornata la rete di Petri relativa all'ordine e viene effettuato così l'avanzamento (si attivano gli impegni successivi)


# Accenno alle estensioni

## Requisiti esterni

L'esecuzione di un impegno  può essere condizionata da fattori esterni alla rete di Petri (es. attributi di oggetti di Sme.up, quando sono modificabili fuori dal workflow).

## Conseguenze esterne

L'esecuzione di un impegno, oltre ad agire sulla rete di Petri spostando i token (e facendo così avanzare l'ordine), può avere come conseguenza l'esecuzione di un flusso di programmi funizzati (definiti nello script), che possono modificare ad esempio oggetti di Sme.up.
