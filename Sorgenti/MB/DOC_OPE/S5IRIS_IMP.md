La schedulazione consiste nell'eseguire un motore BCD di cui viene richiesto il codice (elemento della tabella B§G), all'atto del lancio.
Un motore BCD viene eseguito lanciando il programma B£BCD01 (se si imposta nella voce di menù anche l'elemento della tabella B§G esso non viene richiesto e si presenta subito il formato di richiesta impostazioni).

Le impostazioni generali della schedulazione sono : 

* informazioni generali contenute nell'elemento B§G che si esegue (nome dello script, programma di innesco, ecc..)
Per la schedulazione, il programma di innesco (che contiene 'fisicamente' le aree di memoria in cui si esegue il processo)  è S5SMIN, mentre il settore di tabella in cui si descrivono i dati di input è S5X.
* informazioni passate all'atto del lancio della schedulazione (data e ora di lancio, scenari di input e di output, filtri di ambito e tipo impegno, ecc...). Queste informazioni sono descritte nel settore di tabella (di sola definizione tracciato) inserito nell'elemento di B§G che si è selezionato.
* informazioni contenute nello script di parametri, definito sempre nell'elemento B§G.
Esso contiene una stringa di 200 bytes, i cui vari sottocampi costituiscono le impostazioni generali del processo di schedulazione, definite 'una tantum' da chi ha la responsabilità dell'installazione.
* informazioni che condizionano le presentazioni dei Gantt. Si impostano tramite la voce di popup 'impostazioni', cliccando in una zona vuota del Gantt (al di fuori di una cella).
* informazioni da riportare su ogni riga del Gantt, nella sua parte matriciale, memorizzate all'interno del componente Gantt.

La richiesta dell'elemento di BCD è il seguente

![FIG_056](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_IMP/FIG_056.png)
Successivamente si presenta la richiesta dei parametri di lancio.

![FIG_057](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_IMP/FIG_057.png)
 In questo formato si impostano i campi : 
* Scenario di input (obbligatorio)
* Data schedulazione (obbligatoria) - è l'oggi della schedulazione, da cui si parte per caricare le risorse :  si  può impostare una data anche in forma implicita (&xxx)
* Ora schedulazione (facoltativa) - se impostata è l'ora di partenza (nel giorno definito dalla data di schedulazione), se assente si assume zero. Per ogni risorsa, l'ora di partenza è la maggiore tra quella impostata a video e l'ora di inizio lavoro sul calendario della risorsa
* Stato minimo ordine di produzione (facoltativo) - filtro per ridurre gli impegni da schedulare
* Tipo impegno (obbligatorio) - definisce quali impegni (produzione, ciclo esterno, ecc..) saranno trattati
* Ambito (facoltativo) - se impostato costituisce un filtro, se non impostato saranno trattati tutti gli ambiti
* Scenario di output (facoltativo) - se impostato, i risultati verranno memorizzati in questo scenario, che verrà precedentemente pulito di tutti gli impegni del tipo selezionato, se lasciato in banco i risultati aggiorneranno gli impegni presenti nello scenario di input.
