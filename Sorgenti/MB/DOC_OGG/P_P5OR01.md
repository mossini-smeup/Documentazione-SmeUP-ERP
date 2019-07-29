# Gestione Ordini di Produzione

## Obiettivo
Descrivere la gestione e le funzioni principali associate agli ordini di produzione.

## Struttura di un Ordine di Produzione
In Sme.up gli ordini di produzione hanno le informazioni principali nella _5_'Testata' che contiene l'articolo e la quantità da produrre e le date di inizio e fine produzione.

A fronte della testata si trovano : 

- _3_impegni materiali  che rappresentano i materiali (componenti e quantità) che devono essere utilizzati per produrre l'articolo di testata
- _3_impegni risorse  che rappresentano il fabbisogno di risorse (centri di lavoro, tempi e sequenza di operazioni) necessario alle lavorazioni


La determinazione degli impegni materiali utilizza la distinta dell'ordine che può essere la distinta base dell'articolo oppure può essere una distinta specifica dell'ordine di produzione creata manualmente oppure per copia dalla distinta base, la distinta specifica viene anch'essa associata alla testata dell'ordine.

La determinazione degli impegni risorse utilizza il ciclo dell'ordine che può essere il ciclo dell'articolo oppure può essere un ciclo specifico dell'ordine di produzione creato manualmente oppure per copia dal ciclo dell'articolo, il ciclo specifico viene anch'esso associato alla testata dell'ordine.

Nella testata sono presenti i dati complessivi dell'ordine (es. l'articolo, la qtà da produrre, le date inizio e fine ordine).

Nella figura seguente si vede un esempio di testata di un ordine di produzione : 

![P5_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_01.png)
Le informazioni tipiche della testata sono : 

- _3_Tipo ordine, possiamo avere diverse tipologie di ordine ciascuna dedicata ad una gestione particolare
- _3_Magazzino, (il plant dove viene eseguito l'ordine di produzione)
- _3_Articolo, l'oggetto della produzione
- _3_Qantità ordinata
- _3_Data Inizio / Fine, le date di inizio e fine dell'ordine, se si imposta la data di fine mentre la data inizio è blank il sistema calcola in automatico la data inizio decrementando la data fine del lead time dell'articolo, se si imposta la data di inzio e quella di fine è blank il sistema calcola la data fine incrementando la data inizio del lead time.

### Dettaglio quantità
Selezionando il campo posto di fianco alla qtà ordinata si apre la finestra che mostra il dettaglio delle qtà dell'ordine : 

![P5_01_02](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_02.png)

### Dettaglio date
Selezionando il campo posto di fianco alle date inizio / fine si apre la finestra che mostra il dettaglio delle date e dei lead time associati all'ordine : 

![P5_01_03](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_03.png)
## Funzioni oggetto dell'ordine
Tutti gli ordini delle funzioni che sono proprie dell'oggetto ordine di produzione e si possono attivare dal formato di dettaglio F10 : 

![P5_01_04](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_04.png)
### Attributi
Presenta, in modo simile alla lista campi, tutte le informazioni associate all'oggetto in questione, ma oltre ai dati del record mostra anche altri attributi associati al record in maniera dinamica (cfr. Doc. Applicativa B£OGAT Oggetto Attributo) : 

![P5_01_09](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_09.png)
### Lista campi
Presenta tutti i campi del record come sono memorizzati sul file : 

![P5_01_05](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_05.png)
di default vengono presentati solo i campi compilati, è possibile vedere anche i campi vuoti.

### Parametri per tipo
Se all'ordine di produzione, attraverso la customizzazione, è  stata attribuita la facoltà di gestire dei parametri aggiuntivi, questa opzione rimanda alla loro gestione (cfr Doc. Applicativa C£PARA Parametri).

### Ordini dipendenti
Ad un ordine di produzione si possono legare N. ordini dipendenti (es. quelli che servono per la produzione dei componenti) che si vogliono considerare come un unico raggruppamento. Questa funzione mostra l'elenco di tali ordini : 

![P5_01_11](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_11.png)
### Funzioni oggetto
Rimanda al formato delle funzioni (F10) dell'articolo presente nella testata ordine.

### Sintesi documenti
Questa opzione premette di accedere ad un cruscotto dove sono compattate una serie delle principali visualizzazioni dell'ordine, molte di queste visualizzazioni sono anche accessibili da altre opzioni richiamabili dalle funzioni di testata o dalle funzioni estese (vedi).

La stessa interrogazione di sintesi ordini può essere lanciata come funzione a se stante direttamente da menù inserendo il numero ordine nel campo di input (cfr. Doc. Operativa P5SI02 - Sintesi ordini produzione).

### Funzioni aggiuntive di ordine produzione
_2_Visualizzazione formato standard
Generalmente il formato di presentazione del dettaglio di un ordine di produzione mostra con priorità le informazioni principali che si utilizzano in quella implementazione, mentre le informazioni secondarie vengono portate nelle finestre successive se non addirittura tolte la dalla visualizzazione. Questa funzione permette di riavere la visualizzazione completa.

_2_Gestione commenti
Agli ordini è possibile associare delle note o commenti (cfr Doc. Applicativa B£NOTE Gestione note), con questa funzione, se in fase di customizzazione all'ordine sono state associate delle note, si accede alla manutenzione : 

![P5_01_15](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_15.png)
![P5_01_16](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_16.png)
###  Modifica in lista ordini di produzione
Può capitare il caso di dover fare delle variazioni di massa su una lista di ordini di produzione, questa funzione serve per svolgere azioni di questo tipo.

Si agisce su una lista di ordini filtrata dal seguente formato di selezione riprende le parzializzazioni degli ordini : 

![P5_01_18](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_18.png)
Sulla lista seguente si possono modificare direttamente per tutti gli ordini presentati :  la qtà in ordine, le date inizio e fine, la commessa e lo stato : 

![P5_01_19](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_19.png)
alla fine delle modifiche premere il tasto F6 per confermarle.

### Fasatura ordini di produzione
Quasta è una funzione di servizio che serve per rifasare per un ordine oppure per tutti gli ordini attivi : 

- _3_impegni materiali, interni, per la produzione ed esterni, per i terzisti
- _3_impegni risorse
- _3_quantità residua (in testata ordine)


Per la rifasatura degli impegni materiali il sistema calcola la qtà residua decrementando la qtà ordinata di tutti i versamenti già effettuati, in base alla qtà residua ed alla distinta del documento calcola gli impegni materiali e li decrementa dei prelievi già eseguiti.

Per la rifasatura degli impegni risorse il sistema, in base alla qtà residua ed al ciclo del documento calcola gli impegni risorse e li decrementa delle dichiarazioni di attività di produzione già eseguite.

Il formato di lancio è il seguente : 

![P5_01_20](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR01/P5_01_20.png)