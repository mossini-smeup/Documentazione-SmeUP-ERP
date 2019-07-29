## Obiettivo
Attraverso questa funzione è possibile eseguire la registrazione dei ratei relativi alle fatture da ricevere.
Lanciando la funzione in modalità 'Esecuzione' verrà scritta una registrazione all'interno della quale i documenti ancora in attesa di fattura verrano registrati su un conto di rateo 'Fatture da ricevere'. A seconda delle impostazioni di lancio della funzione sarà possibile : 
 * Eseguire una semplice registrazione di giroconto (attraverso il settaggio della tabella C5D sarà poi possibile definire le caratteristiche di questa registrazione).
 * Eseguire una registrazione di giroconto che si autostorni al giorno successivo.
 * Eseguire una registrazione definitiva che aggiorni il conto di contabilizzazione dei documenti in attesa di fattura.
All'interno della registrazione contabile ottenuta sarà poi possibile visualizzare i documenti legati alla registrazione stessa.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5C040_019](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYI0/C5C040_019.png)
All'interno del formato guida è necessario definire l'ente o la lista enti su cui eseguire la funzione. In questo secondo caso lasciando il campo blank verranno presi in considerazione tutti gli enti del tipo selezionato (clienti o fornitori); per definire una specifica lista di enti si veda la documentazione relativa alla gestione liste : 
 :  : DEC T(MB) P(DOC_OPE) K(B£_LIS) I(Gestione liste oggetti) L(1)
Nel campo 'Modalità' è necessario indicare in che modo eseguire la funzione.
Le scelte disponibili sono : 
 * 1 - Stampa :  permette di stampare la lista documenti in attesa di fattura degli enti indicati nel primo campo
 * 2 - Interrogazione :  permette di visualizzare la lista di documenti in attesa di fattura degli enti indicati nel primo campo
 * 3 - Esecuzione :  permette di eseguire la scrittura della registrazione contabile del rateo
 * 4 - Trasferimento PC :  permette di esportare un file contenente la lista di documenti in attesa di fattura degli enti indicati nel primo campo

Definendo i campi 'Data ratei iniziale' e 'Data ratei finale' viene assegnato un range di date all'interno del quale il sistema ricerca i documenti in attesa di fattura. Il significato di queste date è attribuibile tramite le impostazioni. Ad esempio, indicando come data ratei iniziale 01/01/2009 e data ratei finale 31/12/2009 e definendo nelle impostazioni di considerare come data ratei la data documento verranno presi in considerazione solo i documenti che abbiano data bolla fornitore appartenente al 2009.

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Data rateo :  permette di definire il significato della data rateo indicata nel formato guida. Le scelte disponibili sono Data Documento (è la data riportata sulla bolla del fornitore) oppure Data Origine (è la data della BEM, ovvero dell'entrata merce).
 * Cambio :  permette di definire il cambio da utilizzare nella registrazione di giroconto. Le scelte disponibili sono Attuale o Storico.
 * Stampa/Visualizzazione :  definisce le proprietà della stampa/visualizzazione.
 ** Dettaglio :  permette di visualizzare il dettaglio dei documenti in attesa di fattura.
 ** Schema dettaglio :  permette di definire uno schema di visualizzazione specifico per le righe di dettaglio dei documenti in attesa di fattura.
 ** Simulazione esecuzione :  impostando questo campo il sistema tenterà di simulare la registrazione :  di conseguenza escluderà le righe con errore e quindi non selezionabili e produrrà una stampa nel caso in cui esista qualche errore che impedirebbe l'esecuzione della registrazione.
 * Esecuzione giroconto :  definisce i parametri della registrazione del rateo.
 ** Esercizio :  definisce l'esercizio di appartenenza della registrazione.
 ** Data registrazione :  definise la data della registrazione.
 ** Causale giroconto :  imposta il tipo registrazione utilizzato per il giroconto. E' necessario verificare che il tipo registrazione qui indicato abbia all'interno della tabella C5D il campo 'Controllo fatture' valorizzato con R (Registrazione di rateo).
 ** Conto avere :  indica il conto di rilevazione delle fatture da ricevere, ovvero la contropartita del conto di costo indicato sui documenti in attesa di fattura.
 ** Conti merce :  permette di definire in che modalità eseguire la registrazione. Le scelte disponibili sono : 
 *** Giroconto semplice :  esegue la registrazione di giroconto utilizzando i parametri impostati sopra.
 *** Giroconto con storno al giorno successivo :  esegue la registrazione di giroconto e lo storno della stessa al giorno successivo.
 *** Giroconto con aggiornamento conto avere fonte :  esegue la registrazione e aggiorna il conto riportato sulle righe dei documenti in attesa di fattura scrivendo il conto indicato nel campo 'Conto avere'. Attenzione :  cancellando la registrazione di giroconto così eseguita il campo 'Conto di contabilizzazione' sulla fonte NON viene nuovamente aggiornato. Pertanto sulla fonte resterà il conto 'Conto avere' anche se la registrazione di giroconto è stata cancellata.
 * Trasferimento PC :  permette di definire i parametri per la generazione del file.
 ** Colonne :  attraverso questo campo è possibile definire quali record esportare nel caso in cui venga scelta la modalità Trasferimento. In particolare è possibile : 
 *** Esportare il dettaglio delle righe delle fonti scegliendo Dettaglio.
 *** Esportare solo il totale di ogni documento in attesa di fattura scegliendo Totale raggruppamento.

### Tasti funzionali
 * F06 :  Conferma. Permette di confermare ed eseguire la funzione.
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati.
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

## Formato lista
Eseguendo la funzione in modalità Interrogazione è possibile visualizzare la lista fonti in attesa di fattura : 

![C5C040_020](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYI0/C5C040_020.png)
All'interno della lista sono riportate le fonti in attesa di fattura raggruppate per ente. A seconda dei parametri definiti nelle impostazoni è possibile visualizzare o meno il dettaglio di ogni fonte.
Le informazioni riportate per ogni fonte sono : 
 * Valuta
 * Codice e descrizione fonte
 * Numero e data documento dell'ente
 * Data documento interno
 * Numero di righe incluse nella fonte
 * Quantità prevista ed effettiva
 * Imponibile previsto ed effettivo
 * Presenza di errori nel documento
Le informazioni riportate per ogni riga di dettaglio, invece, sono : 
 * Tipo e numero documento interno
 * Numero riga
 * Codice e descrizione articolo
 * Quantità prevista ed effettiva
 * Imponibile previsto ed effettivo

### Opzioni
Sulle righe di dettaglio delle fonti sono disponibili le seguenti opzioni (visualizzabili, quindi, solo nel caso in cui si scelga all'interno delle impostazioni di visualizzare il dettaglio fonte) : 

- 05 :  Dettaglio. Permette di visualizzare il dettaglio delle informazioni disponibili per la fonte : 

![C5C040_018](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYI0/C5C040_018.png)