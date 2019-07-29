
# DICHIARAZIONE ATTIVITA'

Le attività sono gli eventi significativi nella vita di un ordine di workflow; la scrittura di un attività coincide con l'avanzamento dell'ordine stesso.

La caratteristica principale di un'attività è la sua azione (V2/WF_02)
Assume i seguenti valori principali : 


 * 0 - Attivazione
 * 1 - Presa in carico
 * 2 - Esecuzione
 * 3 - Assegnazione
 * 4 - Distribuzione
 * 9 - Disattivazione requisiti esterni


Una attività può essere generata, e quindi il workflow avanzato, in 3 modi - in ordine crescente di complessità e completezza : 


 * Modo diretto, richiamando la routine £WFC in 'CLEAR', aggiornando eventualmente i campi opportuni e richiamando la routine £WFC in 'WRI'.
 * (se non è una attivazione) tramite la routine £WFA, con funzione 'ATT' e metodo corrispondente all'azione (DIC, PRC...). A differenza della modalità precedente, in questo caso viene eseguito il programma di avanzamento opportuno (specifico da xxx.FUN oppure standard WFATT_01), dopo averne testato l'eseguibilità.
 * Avanzamento completo di workflow, richiamabile tramite la funzione A(WFESE_01;IMP;PRE) 1(F2;;impegno). In questo caso, oltre a testare l'eseguibilità, viene testato l'eventuale "congelamento" del processo, determinata la natura dell'azione da eseguire (diretta o tramite scheda) e, dopo l'avanzamento, lanciato il flusso di esecuzione wf per proporre automaticamente eventuali impegni successivi.


Si noti che il modo "normale" di avanzare un workflow (esecuzione utente da worklist) è il terzo; i primi 2 sono ad uso interno o a disposizione degli sviluppatori.

Alcune attività si definiscono automatiche (è riservato il flag 1 del file) se non sono frutto di una operazione esplicita dell'utente.
Esse sono : 


 * l'attività di attivazione (che viene scritta quando l'impegno passa al primo tra lo stato assegnabile o pronto)
 * l'attività  di esecuzione se è : 
 ** un impegno automatico
 ** un impegno master con tutti gli impegni slave obbligatori eseguiti
 ** un impegno ancora aperto alla conclusione del wf.


La scrittura di queste attività viene eseguita nel programma WFWFA0_AL.

L'attività di assegnazione, che fissa l'utente esecutore dell'impegno, può essere eseguita in due modi : 


 * non impostando un pgm specifico di assegnazione nello script, lanciando un pgm che sceglie l'utente e lo scrive sull'impegno, ed eseguendo la £WFA in ATT/ASS.
 * impostando un pgm specifico di assegnazione nello script :  in esso si sceglie l'utente, lo si scrive sull'impegno, e si lancia la £WFC in CLEAR e WRITE. In questo secondo modo è possibile scrivere altre informazioni nell'attività (eventualmente impostate a video). Va ricordato che la £WFC, in CLEAR, riporta nell'attività la classe e l'esecutore presenti in quel momento sull'impegno.


L'attività di distribuzione può essere eseguita anch'essa in due modi : 


 * non impostando un pgm specifico di distribuzionne  nello script, lanciando la £WFA in ATT/DIS
 * impostando un pgm specifico di distribuzione nello script :  in esso si lancia la £WFC in CLEAR e WRITE. In questo secondo modo è possibile scrivere altre informazioni nell'attività (eventualmente impostate a video).


La parte che rende pronti gli impegni slave viene comunque eseguita nell'allineamento dell'ordine, successivamente alla scrittura dell'attività (nel pgm WFWFA0_AS, che imposta la slave pronta se la master è distribuita). Questo passaggio di stato viene intercettato dal pgm WFWFA0_AL, che è quello che scrive l'attività di attivazione.
