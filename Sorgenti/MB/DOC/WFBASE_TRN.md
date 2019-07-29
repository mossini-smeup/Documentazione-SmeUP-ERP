 :  : PRO Cod(COS) Txt(Costruzione workflow) STAT(00) RESP(GR)
 :  : ATT Cod(001) Txt(Attivare il modulo) STAT(00) RESP(GR)
01. Seguire il documento "Installazione :  oggetti richiesti" che illustra quali oggetti creare/riprendere da modello per attivare il modulo WFBASE.
 :  : ATT Cod(002) Txt(Attivare un processo d'esempio) STAT(00) RESP(GR)
01. Riprendere da modello un elemento ESE* di tabella WFA.
02. Attivare il processo togliendo la spunta "Spegni inserimento" dal dettaglio dell'elemento di tabella.
 :  : ATT Cod(003) Txt(Creare un nuovo processo) STAT(00) RESP(GR) DATA(20121116) ORA(180018)
01. Andare nella scheda del modulo WFBASE.
02. Sottoscheda Lista workflow.
03. Nuovo processo :  inserire un codice e una descrizione per il processo.
04. Revisionare e confermare l'elemento di tabella WFA creato.
05. Agire sulla rete di Petri : 
05a. Aggiungere una seconda transizione;
05b. Collegarla tramite luogo alla prima;
05c. Ridenominare la transizione;
05d. Assegnare una classe di esecutori di tipo '**' (tutti gli utenti).
06. Scrivere due capitoli di documentazione operativa, uno per il processo e uno per la seconda transizione.
 :  : ATT Cod(004) Txt(Approfondire un tema di costruzione mediante gli script di esempio) STAT(10) RESP(GR) DATA(20121119) ORA(165538)


 :  : PRO Cod(ESE) Txt(Esecuzione workflow) STAT(10) RESP(GR) DATA(20121116) ORA(180754)
 :  : ATT Cod(001) Txt(Creazione di un ordine di workflow generico) STAT(10) RESP(GR) DATA(20121116) ORA(180827)
ESEMPIO :  Workflow di esempio ESE_001.
01. Andare nella scheda workflow, sottoscheda "Nuovo ordine".
02. Selezionare un processo tra quelli attivi.
03. Cliccare il pulsante "Nuovo ordine ...".
 :  : ATT Cod(002) Txt(Creazione di un ordine di workflow di oggetto) STAT(10) RESP(GR) DATA(20121116) ORA(180958)
ESEMPIO :  Workflow di esempio ESE_003.
01. Selezionare un punto di Sme.up con un articolo (es.premere F4 e selezionare un articolo).
02. Tasto destro sull'oggetto per fare comparire il pop.up.
03. Selezionare, sotto Workflow, il nome del processo di cui fare partire un ordine (es. "Azioni sugli impegni").
 :  : ATT Cod(003) Txt(Esecuzione di un impegno) STAT(10) RESP(GR)
01. Visualizzare la propria worklist.
02. Selezionare un impegno da eseguire.
03. Prendere in carico/avanzare l'impegno.
 :  : PRO Cod(INT) Txt(Interrogazione) STAT(10) RESP(GR) DATA(20121116) ORA(181255)
 :  : ATT Cod(001) Txt(Visualizzazione delle attività su un ordine di workflow) STAT(10) RESP(GR) DATA(20121116) ORA(181316)
01. Individuare un ordine di workflow.
02. Entrare nella scheda dell'ordine.
03. Visualizzare le attività eseguite su quell'ordine di workflow.
 :  : ATT Cod(002) Txt(Esecuzione di un impegno) STAT(10) RESP(GR) DATA(20121116) ORA(181411)
