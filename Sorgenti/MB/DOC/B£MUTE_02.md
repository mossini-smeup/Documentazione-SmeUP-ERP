# Gestione memorizzazioni avanzate
La scheda permette di gestire le memorizzazioni avanzate (B£MEDE).

Queste memorizzazioni sono organizzate per : 
* __Utente__, può essere un profilo utente (elemento della tab. B£U) oppure un gruppo utente (elemento della tab. B£*GU) oppure "**", le ricerche vengono opportunamente indirizzate dal campo "Tipo utente"
* __Struttura / Contesto__, la struttura stabilisce come interpretare i dati inseriti nel corpo della memorizzazione (tracciato, campi, contenuto), poiché la struttura è eterogenea, compilando opportunamente il tipo si possono attivare ricerche specifiche, se la struttura è una configurazione è necessario specificare anche la sezione che rappresenta la sezione del configuratore (SCP_CFG) da utilizzare. Il contesto serve per differenziare memorizzazioni che interessano oggetti o funzioni "simili" (es. nei surf degli enti si possono avere le stesse strutture valide sia per ricercare clienti che per ricercare fornitori, le memorizzazioni vengono separate grazie al contesto CLI o FOR)

Compilando solo i campi relativi all'utente vengono presentate tutte le memorizzzaizoni dell'utente, mentre se si compilano i campi di struttura/contesto si presentano tutte le memorizzazioni per gli utenti presenti con la stessa struttura/contesto.
Se si compilano tutti i campi utente, quelli di struttura ed il nome il programma presenta direttamente la configurazione richiesta.
Gli altri campi sono per ricercare per informazioni contenute nel dettaglio della configurazione oppure nella descrizione e/o nelle note.

