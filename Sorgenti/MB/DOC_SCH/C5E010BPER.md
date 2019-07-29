## Obiettivo
Analizzare il bilancio aziendale a una certa data.

![C5E010_011](http://localhost:3000/immagini/MBDOC_SCH-C5E010BPER/C5E010_011.png)
## Parametri di lancio
 * Esercizio :  è l'esercizio da analizzare. Se lasciato vuoto viene analizzato l'esercizio corrente
 * Data Iniziale :  è la data a partire dalla quale vengono analizzati i movimenti. Se lasciata vuota viene considerato il primo giorno dell'esercizio in analisi.
 * Data Finale :   è la data fino a cui vengono analizzati i movimenti. Se lasciata vuota viene considerato 31/12/9999, quindi nel caso in cui siano presenti registrazioni sovrapposte vengono incluse.
 * Conto Iniziale/Finale :  è possibile impostare un filtro per codice del conto contabile. Se i campi vengono lasciati vuoti il sistema mostrerà tutti i conti.
 * Pertinenza :  in questo campo è possibile indicare se si vogliono analizzare solo i movimenti civilistici, solo i gestionali o entrambe. Se lasciato vuoto vengono considerati i soli movimenti civilistici.
 * Condizione :  in questo campo è possibile indicare se si vogliono analizzare solo i movimenti attivi, simulati, sospesi o tutti i movimenti inseriti. Se lasciato vuoto vengono considerati i soli movimenti attivi.
 * Riclassifica :  è la riclassifica secondo cui analizzare il bilancio. Se lasciata vuota viene analizzata la riclassifica base.
 * Arrotondamento Decimali :  impostando questo campo verranno presentati valori arrotondati al numero intero e non verranno mostrati i decimali.
 * Divisione :  nel caso in cui sia attiva la gestione della divisione contabile sarà possibile filtrare per divisione
 * Conti a zero :  permette di includere anche i conti con saldo a zero e non movimentati nel periodo
 * Intercompany :  permette di visualizzare solo i movimenti intercompany o di escluderli
 * Saldi conti valutari :  nel caso in cui siano presenti conti monovalutari è possibile esporre anche il saldo nella valuta del conto


### Dettaglio informazioni
L'analisi di periodo riporta per ogni conto e per ogni livello di riclassifica : 
 * Saldo Inizio :  è il saldo alla data iniziale impostata nei parametri
 * Dare :  è il saldo dei movimenti in dare registrati tra le data iniziale e finale impostate nei parametri
 * Avere :  è il saldo dei movimenti in avere registrati tra le data iniziale e finale impostate nei parametri
 * Saldo Periodo :  è il saldo dei movimenti registrati tra le data iniziale e finale impostate nei parametri
 * Saldo Finale :  è il saldo progressivo alla data finale impostata nei parametri

## Funzioni Disponibili
 * Dettaglio :  Cliccando con il tasto destro all'interno di una cella sarà possibile analizzare il dettaglio delle registrazioni che compongono quel valore
 * Scheda conto :  Facendo doppio click sul codice di un conto contabile sarà possibile accedere alla scheda del conto stesso

