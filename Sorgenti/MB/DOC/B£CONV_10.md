## STRUTTURA

La gestione del lancio delle conversioni poggia sulla struttura del gruppo di azioni.
Tale struttura si basa su due tabelle la **B£J** e la **B£H**  :  la B£J definisce l'elenco   dei vari pgm che devono essere eseguiti in una conversione, mentre la B£H definisce   il sottoinsieme degli elementi della B£J di cui è costituita una particolare conversione.
Nella codifica di tali elementi vengono seguite delle particolari convenzioni : 
 * 1. L'elemento della B£H viene denominato "CON_"+nome ambiente partenza es.      per ACG CON_A7. Nella B£H nel "Sottosettore azioni" viene sempre indicato il      sottosettore della B£J CV, mentre come "Limite Azioni 01" viene messo il      codice dell'ambiente+"*" (in questo modo vengono presi in considerazione      i soli elementi della B£JCV che iniziano con il nome dell'ambiente).
 * 2. Tutti i pgm delle conversioni vengono codificati come sopradetto negli elementi del sottosettore CV della tabella B£J, e che per poter essere utilizzati all'interno della conversione di un certo ambiente ne devono riportare il codice nei primi due caratteri. A tali due caratteri vengono fatti seguire
 * 3 caratteri numerici, la cui definizione non è casuale :  tramite essi viene infatti definito l'ordine con il quale le azioni verranno eseguite nella conversione. Solitamente la numerazione progressiva avviene per 10 unità in modo che l'introduzione di un nuovo passo intermedio non porti alla ricodifica dell'intera successione.
 :  : DEC T(ST) P() K(B£H) I(_9_ B£H - Azioni >>)
 :  : DEC T(ST) P() K(B£JCV) I(_9_ B£JCV - Gruppo Azioni Conversioni >>)

Le strutture standard sono memorizzate nel modello e sono da esso reperibili.

## ESECUZIONE
Il lancio delle conversioni avviene attraverso il pgm B£CONV. La conversione può essere lanciata essenzialmente in due modalità :  interattiva e batch

 * >Lancio interattivo :   Va eseguita una chiamata secca del B£CONV. Vanno impostati come funzione CON e metodo AGG. Nei campi "Destinazione" ed "Origine" vanno indicati i codici degli ambienti di arrivo e di partenza. Vanno inoltre indicati, essendo campi obbligatori, un'applicazione ed un file che di fatto non hanno utilizzo in quest'ambito. Nel campo gruppo azioni va invece indicato il codice della B£H che si vuole utilizzare (se i campi precedenti sono riempiti e il campo viene sbiancato viene assunto automaticamente CON_+ambiente destinazione).

Impostando inoltre 2 per l'esecuzione del flusso e premendo F08 si avrà accesso all'elenco dei passi del flusso di conversione. Da qui per effettuare l'esecuzione è necessario selezionare tramite una X le azioni che si vogliono eseguire (solo queste verranno eseguite) e premere F06 e F11 per lanciarne il lavoro.

 * >Lancio batch :   Il pgm può anche essere lanciato in modo cieco ad esempio tramite un pgm schedulato chiamando il B£CONV con due parametri :  nel primo va indicato il gruppo azioni (es. CON_A7) che si vuole eseguire (in questo caso verranno eseguite tutte le azioni del flusso che non hanno impostato il campo attivazione a "N"); il secondo parametro va invece lasciato blank.

Quindi la chiamata può essere di questo tipo CALL PGM(B£CONV) PARM('CON_A7' '')

NOTA BENE :  mentre nel lancio interattivo vengono lanciate solo le azioni con la "X", nel flusso batch vengono lanciate tutte le azioni attive (quindi visibili) per il flusso.

 :  : INI  _9_Lancio interattivo  >>
 :  : CMD CALL B£CONV
 :  : FIN
