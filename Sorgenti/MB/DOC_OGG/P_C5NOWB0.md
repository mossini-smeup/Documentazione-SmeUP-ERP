## Obiettivo

Attraverso questa funzione è possibile analizzare e gestire le riclassifiche di bilancio assegnando ai diversi conti contabili la linea di riclassifica corretta.

## Formato guida

Il formato guida si presenta nel seguente modo : 

![C5E010_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOWB0/C5E010_001.png)
All'interno del formato guida è necessario specificare i seguenti campi : 

 - Codice azienda
 - Funzione. Per l'analisi delle riclassifiche di bilancio questo campo viene automaticamente impostato a W.
 - Metodo. Per l'analisi delle riclassifiche di bilancio questo campo viene automaticamente impostato a B.
 - Modalità. In questo campo è necessario indicare il tipo di output desiderato. Le modalità disponibili per l'esecuzione di questa funzione sono : 
 -- 1 - Stampa :  permette di stampare il bilancio riclassificato.
 -- 2 - Interrogazione :  permette di visualizzare e gestire la riclassifica specificata in basso.
- Riclassifica. E' necessario impostare il codice della riclassifica da analizzare.
- Data competenza. Il campo è facoltativo, se viene compilato verranno visualizzati solo i conti contabili validi alla data indicata ovvero i conti contabili con data fine validità vuota o successiva alla data qui impostata.


### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
![C5E010_002](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOWB0/C5E010_002.png)
 - Dettaglio :  permette di definire se visualizzare solo i conti assegnati a una linea della riclassifica in analisi, solo i non assegnati o tutti.
 - Ordinamento :  permette di visualizzare il dettaglio dei conti ordinato per riclassifica oppure per codice conto.
 - Conti :  permette di visualizzare o meno il dettaglio dei conti contabili. Le scelte disponibili sono : 
 -- Default - No. Non visualizza il dettaglio dei conti contabili.
 -- 2 - Sì. Visualizza il dettaglio dei conti contabili.
 -- 3 - Solo utilizzati. Visualizza solo il dettaglio di conti utilizzati.
 -- 4 - Solo non utilizzati. Visualizza solo il dettaglio di conti non utilizzati.
 - Linee livelli inferiori :  permette di visualizzare immediatamente sotto la linea di riclassifica le linee di livello inferiore che hanno all'interno del campo 'Linea di destinazione' la linea in esame.
 - Data saldo :  è possibile visualizzare anche il valore del saldo dei conti contabili impostando in questo campo la data a cui valorizzare il saldo.
 - Linea riclassifica iniziale/finale :  attraverso questi campi è possibile definire un range di linee all'interno del quale visualizzare il bilancio riclassificato.
 - Filtro riclassifiche :  permette di visualizzare solo linee calcolate, solo linee con destinazione oppure solo linee fittizie.
 - Note :  permette di visualizzare o meno le note presenti sui conti contabili o sulle linee.
 - Data ultima movimentazione :  permette di visualizzare o meno l'ultima data in cui il conto è stato movimentato.


 :  : I.INC.MBR Fil(DOC_OPE) Mem(C5C010_01)

### Parzializzazioni

Digitando il tasto F13 o selezionando il relativo bottone è possibile accedere alle Parzializzazioni che consentono di filtrare i conti contabili visualizzati.


### Tasti funzionali

 * F06 :  Conferma. Permette di confermare ed eseguire la stampa
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della stampa; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch e congelare la stampa.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

### Memorizzazioni

Le memorizzazioni consentono di salvare le parametrizzazioni definite all'interno della videata. Per maggiori dettagli sulla loro creazione e gestione si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)


## Formato lista

All'interno del formato lista sarà visualizzato il bilancio riclassificato nel caso in cui si sia scelto l'ordinamento 'Per riclassifica' mentre nel caso in cui si scelga l'ordinamento 'Per conto' verrà visualizzato l'elenco dei conti contabili e per ognuno di essi sarà riportata la linea di riclassifica a cui è associato.
Scegliendo di ordinare i conti per riclassifica con dettaglio per conto apparirà la seguente visualizzazione : 

![C5E010_003](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOWB0/C5E010_003.png)
Nella parte superiore dell'elenco sono riportati i conti contabili non assegnati ad alcuna linea mentre nei record successivi è riportato il bilancio ordinato secondo la riclassifica in analisi.
Per ogni linea di riclassifica sono riportate le seguenti informazioni : 

 - Livello di riclassifica
 - Codice della linea/conto
 - Descrizione della linea/conto
 - D :  segno dare o avere della linea se definito all'interno della tabella C5N (con sottosettore specifico per la riclassifica).
 - Linea se inverso :  se impostato all'interno della tabella C5N.
 - Linea di destinazione :  se impostato all'interno della tabella C5N.
 - S :  segno di destinazione della linea se definito all'interno della tabella C5N
 - L :  indica se la linea è una linea calcolata o meno (definito nella tabella C5N)
 - C :  indica se sulla linea è stata impostata la costruzione dei livelli superiori


Nel caso in cui venga impostata una Data saldo all'interno delle impostazioni per ogni conto a saldo non nullo è visualizzato anche il valore del saldo alla data specificata.


### Opzioni

Per ognuna delle linee visualizzate sono disponibili le seguenti opzioni : 


 - 01 - Inserisci elemento :  permette di inserire una nuova linea all'interno della tabella C5N.
 - 02 - Modifica :  permette di modificare la linea all'interno della tabella C5N.
 - 03 - Copia elemento :  permette di inserire una nuova linea all'interno della tabella C5N copiandola dalla linea su cui è stata digitata l'opzione.
- '+' - Selezione per aggiornamento :  permette di aggiungere alla linea i conti selezionati (si vedano le istruzioni più in basso).
- '-' - Deselezione :  permette di rimuovere i conti selezionati dalla linea (si vedano le istruzioni più in basso).


Per ognuno dei conti visualizzati sono disponibili le seguenti opzioni : 


 - 01 - Inserisci elemento :  permette di inserire un nuovo conto all'interno della tabella C5B.
 - 02 - Modifica elemento :  permette di modificare l'elemento della C5B che codifica il conto contabile.
 - 03 - Copia elemento :  permette di inserire un nuovo conto all'interno della tabella C5B copiandolo dal conto su cui è stata digitata l'opzione.
- '+' - Selezione per aggiornamento :  permette di aggiungere il conto a una linea (si vedano le istruzioni più in basso).
- '-' - Deselezione :  permette di rimuovere il conto da una linea (si vedano le istruzioni più in basso).
- AC - Assegna per codice :  permette di visualizzare l'elenco delle linee ordinato per codice linea e assegnare il conto contabile a una delle linee visualizzate.
- AD - Assegna per descrizione :  permette di visualizzare l'elenco delle linee ordinato per descrizione linea e assegnare il conto contabile a una delle linee visualizzate.
- AP - Assegna per parametri :  permette di visualizzare i parametri delle linee e visualizzare le lineee con un determinato valore di un certo parametro. Da qui è poi possibile assegnare il conto contabile a una delle linee visualizzate.

### Tasti funzionali

 * F01 :  Permette di ricercare una stringa all'interno della videata
 * F05 :  Esegue l'aggiornamento della videata
 * F06 :  Permette di confermare l'assegnazione/rimozione di conti a linee.
 * F09 :  Permette di posizionarsi sulla prima pagina del formato lista
 * F10 :  Permette di posizionarsi sull'ultima pagina del formato lista
 * F13 :  Parzializzazioni. Permette di definire dei filtri per la visualizzazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

## Come assegnare uno o più conti a una riclassifica

Per effettuare l'assegnazione di conti a una linea di riclassifica si consiglia di seguire la seguente procedura : 

- All'interno delle impostazioni scegliere di visualizzare solo i conti non ancora assegnati impostando il campo 'Dettaglio'=3 e 'Conti'=2. In questo modo nella parte superiore saranno visualizzati i conti ancora da assegnare alle linee e nella parte inferiore saranno visualizzate le linee di riclassifica.

![C5E010_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOWB0/C5E010_004.png)
- Selezionare con un '+' i conti da assegnare a una stessa linea e la linea a cui assegnare i conti : 

![C5E010_005](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOWB0/C5E010_005.png)
- Confermare la selezione con F6


## Come rimuovere  uno o più conti da una riclassifica

Per rimuovere i conti contabili da una riclassifica è sufficiente digitare un '-' a sinistra del/i conto/i e confermare con F6.




