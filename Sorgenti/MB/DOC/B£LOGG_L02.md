## OBIETTIVO

Permettere di tracciare i tempi e le chiamate che avvengono sull'AS400, sfruttando il comando di sistema TRCJOB. Questo comando permette di tracciare tutto ciò che avviene durante un'elaborazione dell'As400.

## ATTIVAZIONE

L'attivazione al momento è prevista solo per il Job corrente di loocup. Per farlo è necessario utilizzare le funzionalità predisposte nella scheda specifica.

Va inoltre specificato che la raccolta delle informazioni ha una struttura per la quale la sua funzionalità è limitata ad un certo lasso di tempo, questo lasso è definito dall'esecuzione delle funzioni di attivazione e disattivazione del log. Senza aver prima disattivato il log non sarà possibile interrogare i dati raccolti. Nel caso in cui una volta attivato il log, il lavoro venga chiuso senza che sia stata eseguita la disattivazione, anche in questo caso tutti i dati racconti andranno perduti.

## GESTIONE DATI DEL LOG

I dati prodotti dal log vengono memorizzati in un file temporaneo della libreria QTEMP, corrispondente al tracciato del file di sistema QATRCJOB. Questo file pure essendo interrogabile dalla scheda di sistema, non è di immediata lettura, per questo è stata predisposta la possibilità di copiare il file temporaneo nel file JALOGT in cui le informazioni di lettura vengono semplificate e su tali record sono state poi predisposte delle funzioni di interrogazione.

Per il file temporaneo non è necessaria alcuna funzione di pulizia, in quanto ogni volta che viene attivata una traccia o nel momento in cui il lavoro viene chiuso il file viene eliminato. Viceversa se viene utilizzato il file JALOGT, i suoi record (riconoscibili dal tipo record "J") potranno essere eliminati manualmente tramite la funzione specifica predisposta nella scheda.


