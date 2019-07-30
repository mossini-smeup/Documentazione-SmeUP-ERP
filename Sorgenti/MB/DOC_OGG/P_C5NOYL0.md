## Obiettivo
Attraverso questa funzione è possibile interrogare la lista documenti in attesa di fattura.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5C040_016](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYL0/C5C040_016.png)
All'interno del formato guida è necessario definire l'ente o la lista enti su cui eseguire l'interrogazione in funzione del fatto che l'interrogazione venga lanciata per un singolo ente o per una lista enti. Nel secondo caso, lasciando il campo blank verranno presi in considerazione tutti gli enti del tipo selezionato (clienti o fornitori); per definire una specifica lista di enti si veda la documentazione relativa alla gestione liste : 
- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)
Nel campo 'Modalità' è necessario indicare il tipo di output desiderato.
Le modalità disponibili per l'esecuzione di questa funzione sono : 
 * 1 - Stampa :  permette di stampare la lista documenti in attesa di fattura.
 * 2 - Interrogazione :  permette di visualizzare la lista di documenti in attesa di fattura.
 * 4 - Trasferimento PC :  permette di esportare un file su PC contenente la lista di documenti in attesa di fattura.

All'interno del campo 'Valuta' è possibile indicare una specifica valuta :  in questo modo il sistema prenderà in considerazione i soli documenti che abbiano la valuta indicata.

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Dettaglio :  permette di visualizzare il dettaglio dei documenti in attesa di fattura.
 * Schema dettaglio :  permette di definire uno schema di visualizzazione specifico per le righe di dettaglio dei documenti in attesa di fattura.
 * Escludi righe con errore/Non selezionabili :  attraverso questo campo è possibile fare in modo che il sistema non prenda in considerazione le righe contenenti errori e quindi non selezionabili.
 * Colonne trasferimento PC :  attraverso questo campo è possibile definire quali record esportare nel caso in cui venga scelta la modalità Trasferimento. In particolare è possibile : 
 ** Esportare il dettaglio delle righe delle fonti scegliendo Dettaglio.
 ** Esportare solo il totale di ogni documento in attesa di fattura scegliendo Totale raggruppamento.
 ** Esportare solo un record di totale per ogni ente selezionando Totale ente.
 * Ordinamento :  permette di definire l'ordinamento dei record, le possibilità sono : 
 ** Fonte/data/Codice raggruppamento :  permette di ordinare per data e numero documento.
 ** Data/Numero documento originario :  permette di ordinare per data e numero bolla.
 ** Fonte/Codice/Data Raggruppamento :  permette di ordinare per numero e data documento.

### Tasti funzionali
 * F06 :  Conferma. Permette di confermare ed eseguire la funzione
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

## Formato lista
A seconda delle impostazioni definite nella tabella C56 è possibile visualizzare o meno una schermata di filtro prima di accedere alla lista fonti in attesa di fattura.
Nel caso in cui all'interno delle impostazioni si sia scelto di visualizzare il dettaglio delle fonti il formato lista si presenterà in questo modo : 

![C5C040_017](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYL0/C5C040_017.png)
Se, invece, si sceglie di non visualizzare il dettaglio nel formato lista verranno visualizzate solo le testate delle fonti in attesa di fattura.
All'interno del formato lista per le testate sono riportate le seguenti informazioni : 
 * Codice e descrizione fonte
 * Numero e Data Bolla
 * Data fonte
 * Numero totale di righe presenti nella fonte
 * Quantità totale prevista ed effettiva
 * Imponibile totale previsto ed effettivo
 * Eventuale presenza di errori all'interno del documento che impedirebbero la selezione della fonte all'interno di una fattura (campi E e W)
Per le righe sono invece riportate le seguenti informazioni : 
 * Tipo riga
 * Numero documento e numero riga
 * Codice e descrizione articolo
 * Quantità totale prevista ed effettiva
 * Imponibile totale previsto ed effettivo
 * Eventuale presenza di errori all'interno del documento che impedirebbero la selezione della fonte all'interno di una fattura (campi E e W)

### Opzioni
Sulle righe di dettaglio delle fonti sono disponibili le seguenti opzioni (visualizzabili, quindi, solo nel caso in cui si scelga all'interno delle impostazioni di visualizzare il dettaglio fonte) : 

- 05 :  Dettaglio. Permette di visualizzare il dettaglio delle informazioni disponibili per la fonte : 

![C5C040_018](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOYL0/C5C040_018.png)
- VO :  Origine - Visualizza. Permette di visualizzare la riga del documento origine.
- VT :  Origine(T) - Visualizza. Permette di visualizzare la testata del documento origine
- MO :  Origine - Modifica. Permette di modificare la riga del documento origine.
- MT :  Origine (T) - Modifica. Permette di modificare la testata del documento origine.
