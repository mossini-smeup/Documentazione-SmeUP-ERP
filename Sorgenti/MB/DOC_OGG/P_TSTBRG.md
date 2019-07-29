# £BRG GESTIONE OGGETTI / SVILUPPI DI UNA FASE DI CICLO

## OBIETTIVO
 Semplificare la gestione degli sviluppi di una fase, tramite programmi esterni che hanno una  struttura simile e che svolgono tutte le funzioni possibili sul singolo oggetto / sviluppo.

## IMPLEMENTAZIONE
 Per attivare questa gestione si deve innanzitutto impostare in tabella B£H l'elemento 'A-F2<tipo ciclo>'  o il generico 'A-F2'.
 Poi si deve inserire in tabella B£J<s/s da B£H> un elemento per ogni sviluppo che si intende gestire.
 Il caricamento iniziale delle tabelle B£JF2 standard può essere fatto da questo stesso programma  con funzione/metodo BAS/COS.
 Per migliorare le prestazioni, si consiglia di cancellare gli elementi di tabella relativi a sviluppi  che si prevede di non utilizzare.
 Con funzione/metodo IMP/02 si accede alla manutenzione guidata del campo "Parametri aggiuntivi".
 Se si avesse la necessità di gestire oggetti / sviluppi personali, utilizzare il sorgente prototipo  BRBRG_XX per scrivere il programma specifico.

 Per ulteriori informazioni si veda la documentazione all'interno della routine.
