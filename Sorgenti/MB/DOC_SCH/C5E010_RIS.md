## Obiettivo
Analizzare i risconti ancora aperti alla data situazione richiesta, ovvero tutte le registrazioni di risconto automatiche con data successiva a quella impostata nella data situazione.
![C5E010_009](http://localhost:3000/immagini/MBDOC_SCH-C5E010_RIS/C5E010_009.png)
## Parametri di lancio

 * Esercizio situazione :  in questo campo (obbligatorio) è necessario impostare l'esercizio che interessa analizzare
 * Data situazione :  in questo campo è possibile impostare una data situazione. Se non è impostato nessun valore il sistema assume 31/12/XX dove XX è l'esercizio impostato nel campo precedente
 * Pertinenza :  permette di filtrare le registrazioni esposte in funzione della loro pertinenza fiscale o gestionale. Se non compilato vengono esposti i soli risconti fiscali
 * Condizione :  permette di filtrare le registrazioni esposte in funzione della loro condizione attiva o simulata. Se non compilato vengono esposti i soli risconti attivi
 * Data Limite Risconto :  permette di analizzare i soli risconti antecedenti a questa data. Se non impostato assume 31/12/9999
 * Conto :  permette di filtrare l'analisi per conto di costo/ricavo. Se non impostato vengono esposti i risconti aperti su tutti i conti economici
 * Natura conti :  permette di filtrare l'analisi per natura del conto (costo o ricavo). Se non impostato vengono esposti i risconti aperti su tutti i conti economici. Si sottolinea che l'analisi della natura del conto viene effettuata in funzione di quanto impostato sull'anagrafica del conto stesso (tabella C5B).
 * Tipo contatto :  permette di filtrare l'analisi per tipologia di contatto intestatario del costo/ricavo.
 * Codice contatto :  permette di analizzare i risconti aperti relativi a uno specifico cliente/fornitore
 * Da data documento/ A data documento :  permette di analizzare i risconti derivanti da documenti che hanno data inclusa nel range impostato
 * Numero documento :  permette di visualizzare i risconti aperti associati a uno specifico documento. All'interno del campo è sufficiente indicare una parte del numero documento; il programma, infatti, ricerca tutti i documenti che hanno all'interno del numero la stringa riportata in questo campo. Quindi se il numero fattura è 160000264 mi basterà scrivere 264 nel Numero documento per vedere i risconti associati alla scrittura.
 * Da data registrazione origine/A data registrazione origine :  permette di filtrare per data della registrazione che ha generato il risconto.
 * Righe per pagina :  permette di aumentare il numero di righe mostrato al lancio della funzione (di default vengono presentate le prime 1000 righe).

## Dettaglio informazioni

All'interno della matrice di dettaglio è possibile visualizzare le scritture di risconto ancora aperte. In particolare, vengono prima riportate le scritture che riguardano conti di costo e successivamente quelle che riguardano conti di ricavo.
Per ogni scrittura di risconto vengono riportati : 
 * Esercizio del risconto
 * Numero registrazione di risconto
 * Data registrazione del risconto
 * Conto Contabile :  è il conto di costo o ricavo su cui è stato effettuato il risconto
 * Importo risconto
 * Pertinenza della scrittura :  identifica se si tratta di una scrittura fiscale (campo blank) o gestionale
 * Intestatario della registrazione :  è il cliente/fornitore intestatario della registrazione se presente
 * Esercizio origine :  è l'esercizio a cui appartiene la scrittura che ha generato il risconto automatico
 * Registrazione origine
 * Data registrazione origine
 * Tipo e Descrizione registrazione origine
 * Data e Numero documento della registrazione origine
 * Data inizio e data fine competenza
 * Tipo e descrizione registrazione di risconto
 * Conto utilizzato per il risconto


