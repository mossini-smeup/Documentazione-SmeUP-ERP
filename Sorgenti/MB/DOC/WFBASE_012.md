# Introduzione

Durante l'esecuzione di un ordine di workflow è possibile generare ordini derivati (non necessariamente dello stesso processo dell'ordine origine - detto master).
L'esecuzione di questi ordini può essere un requisito per impegni successivi dell'ordine master :  in questo modo si favoriscono la costruzione modulare e il riutilizzo dei processi già definiti.

# Note tecniche

Per creare sottoworkflow vincolanti su un processo master è necessario : 
 * Conseguenza esterna su processo master :  crea il sottoprocesso;
 * Conseguenza esterna su processo derivato, al suo termine :  avanza lo stato del processo e allinea processo master;
 * Requisito esterno su una transizione del processo master, per renderla attivabile solo se i sottoprocessi sono terminati.

Come esempio si guardino il workflow ESE_008 e derivati.

## Attenzione

Si consideri il caso in cui DIVERSI impegni di un ordine master (es. T01 e T02) generino sotto-ordini che devono essere chiusi per poter svolgere una successiva transizione (es. T03) dell'ordine master.
Non è possibile indicare come "transizione di arrivo" T03 per i sotto-ordini creati in questo modo :  se un sotto-ordine (es. quello generato da T01) viene chiuso prima che sia creato l'altro sotto-ordine (ad. esempio perchè T02 è pronta ma non è ancora stata eseguita) il programma di aggiornamento rende eseguibile T03 perchè : 

- vede un solo sotto-ordine (quello di T01) con T03 di arrivo.
- tale sotto-ordine è chiuso.

La soluzione, in questo caso, consiste nell'introdurre due transizioni di arrivo automatiche T04 e T05, che scatteranno separatamente alla chiusura rispettivamente dei sotto-ordini di T01 e T02, e che scriveranno in due luoghi distinti entrambi requisiti per T03.
