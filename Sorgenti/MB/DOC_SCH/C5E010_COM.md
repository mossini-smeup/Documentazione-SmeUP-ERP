## Obiettivo
Obiettivo di questa scheda è analizzare il saldo di un conto contabile a una ceerta data scomponendolo in ratei e risconti in funzione della competenza delle scritture inserite.
![C5E010_008](http://localhost:3000/immagini/MBDOC_SCH-C5E010_COM/C5E010_008.png)
## Parametri di lancio

 * Lista conti :  permette di eseguire l'estrazione su uno specifico gruppo di conti. Per eseguire l'estrazione di tutti i conti inserire *.
 * Esercizio :  in questo campo è necessario impostare l'esercizio che interessa analizzare. Se non è impostato nessun valore il sistema assume l'esercizio corrente
 * Data situazione :  in questo campo è possibile impostare una data situazione. Se non è impostato nessun valore il sistema assume oggi
 * Natura Conto :  permette di filtrare per natura del conto (costi o ricavi)
 * Pertinenza :  permette di filtrare le registrazioni esposte in funzione della loro pertinenza fiscale o gestionale. Se non compilato vengono esposti i saldi delle scritture fiscali
 * Condizione :  permette di filtrare le registrazioni esposte in funzione della loro condizione attiva o simulata. Se non compilato vengono esposti i saldi delle scritture attive
 * Riclassifica :  permette di visualizzare i conti secondo una delle riclassifiche di bilancio impostate. Se non compilato i conti vengono visualizzati in ordine di codice
 * Risconti futuri da Esercizi precedenti :  permette di visualizzare una colonna in cui è riportato il saldo delle scritture di risconto che si manifesteranno nel futuro e la cui registrazione origine è precedente all'esercizio che sto analizzando. Ad esempio se stiamo analizzando il saldo al 31/03/XX e sul conto 333333 ho effettuato una scrittura in data 31/12/XX-1 con competenza 01/01/XX - 31/12/XX+1 in questa colonna verrà riportato il saldo del costo imputato nell'esercio XX+1

## Dettaglio informazioni

* Conto e descrizione
* Registrazioni Documenti del periodo :  è il saldo delle registrazioni fiscali (anche non effettive se con il filtro sulla condizione vengono incluse) di documenti registrati nel periodo. I movimenti inclusi in questa colonna vengono identificati analizzando la causale contabile (tabella C5V) riportata sulla riga. In particolare, vengono qui incluse tutte le registrazioni con tipo movimento di riga <= 03.
* Registrazioni Generale del periodo :  è il saldo delle registrazioni fiscali (anche non effettive se con il filtro sulla condizione vengono incluse) di contabilità generale, ovvero quelle che non sono associate a documenti, non hanno tipo movimento di rettifica e non sono movimenti automatici per competenza. In sostanza vengono escluse tutte le righe con tipo movimento pari a 01, 02, 03, 32, 33, 34 all'interno della tabella C5V.
* Rettifiche Manuali del Periodo :  è il saldo delle registrazioni fiscali con causale contabile che riporta tipo movimento 32, 33, 34 all'interno della tabella C5V e gli eventuali movimenti gestionali manuali (se questi vengono inclusi con il filtro sulla pertinenza). Vengono esclusi movimenti automatici per competenza.
* Storno a rateo :  è il saldo degli storni automatici con cui sono stati rateizzati i costi/ricavi. Tramite il parametro 'Pertinenza' è possibile includere o escludere i movimenti gestionali.
* Storno a risconti :  è il saldo degli storni automatici con cui sono stati ricontati i costi/ricavi. Tramite il parametro 'Pertinenza' è possibile includere o escludere i movimenti gestionali.
* Ratei da periodi futuri :  è il saldo delle scritture con cui sono stati attribuiti al periodo in analisi costi/ricavi provenienti da registrazioni effettuate in esercizi successivi a quello in analisi.
* Risconti da periodi passati :  è il saldo delle scritture con cui sono stati attribuiti al periodo in analisi costi/ricavi provenienti da registrazioni effettuate in esercizi precedenti a quello in analisi.
* Totale periodo :  è la sommatoria di tutte le colonne precedenti. Deve corrispondere al saldo finale dell'analisi di bilancio.
* Risconti futuri di esercizi precedenti :  evidenzia la quota parte di risconto che deriva totalmente da esercizi precedenti a quello in analisi. E' una colonna opzionale che appare sono se attivata tramite la relativa opzione.

## Opzioni
 * Dettaglio valori :  cliccando con il tasto destro all'interno di una cella e selzionando la voce _Dettaglio_ sarà possibile evidenziare il dettaglio delle scritture che compongono il saldo della cella. Se la voce _Dettaglio_ viene selezionata cliccando con il tasto destro del mouse sul codice del conto contabile verranno visualizzate tutte le scritture che compongono il saldo del conto e per ogni scrittura il valore verrà inserito in una delle colonne elencate nel paragrafo Dettaglio informazioni.



