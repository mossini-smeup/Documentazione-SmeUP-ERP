# Servizio LOSER_23
## Introduzione al servizio
Il servizio LOSER_23 è un servizio (in fase di sviluppo) che permette di eseguire un flusso di
azioni partendo da uno script SCP_FLU.
L'idea da cui è nata l'esigenza di uno script è perchè tramite questo strumento è più facile comprendere i passi di un flusso a prescindere dall'implementazione specifica che il flusso può assumere.
Il servizio LOSER_23 - che potrebbe in un secondo momento divenire una /COPY- a differenza di una chiamata del flusso cablata in un programma rende possibili le seguenti funzioni : 
 * Rendere più semplice e chiara la lettura del flusso di azioni
 * Creare un flusso impostando i passi indipendentemente dalla loro posizione ma usando un ID che ne permetta di definire la sequenza
 * Impostare delle variabili  che possano essere sostituite runtime dai programmi che lanciano il flusso. Questo permette di lanciare lo stesso flusso n volte valorizzando man mano le variabili di utilizzare
 * Utilizzare delle variabili globali di LoocUp (Features ancora da validare 12-03-08)
 * Infine permette di essere maggiormente flessibili per eventuali implementazioni successive separando la logica di esecuzione dall'insieme di dati man mano elaborati

## Esempi di utilizzo
In MyLoocup-Esempi-Capire LoocUp-Funzioni con Interazione-Flusso di azioni
sono state predisposti alcune schede di esempio dove è possibile vedere l'esecuzione di semplici chiamate.

