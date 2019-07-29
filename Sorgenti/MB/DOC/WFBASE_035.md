# Personalizzazione liste WF

A seconda dell'ambito applicativo di un processo di workflow le informazioni che possono servire all'utente per lavorare sui suoi oggetti (ordini, impegni, attività) possono variare di molto.
Si pensi ad esempio a un processo riguardante ordini di vendita, per il quale potrebbe fare comodo vedere in worklist informazioni sul cliente e sull'agente, confrontato con un processo di sviluppo di nuovi prodotti, per il quale magari basta il tipo articolo oltre al codice dello stesso.

Questa eterogeneità di esigenze informative non può essere soddisfatta unicamente dai programmi standard di presentazione di ordini, impegni e attività.
Per questo esistono 2 strade per potenziare le informazioni a disposizione degli utenti del workflow in interrogazione delle liste di ordini, impegni e attività : 
 * I programmi di caricamento di queste liste possono agganciare una exit, il cui nome sarà WFWRK_01U, per aggiungere colonne e informazioni specifiche a seconda dei workflow trattati in azienda. Questa exit è condivisa da tutti i servizi di caricamento standard (ordini, impegni, attività) per tutti i processi, quindi porterà a visualizzare sulla stessa colonna informazioni che variano in natura con il tipo di processo. Si faccia riferimento all'esempio fornito in WFSRC.
 * E' sempre possibile scrivere dei servizi di caricamento specifici per processo, che forniscono un'entrata alternativa e più mirata agli impegni o ordini di un determinato processo. Questi servizi possono integrare o, al limite, sostituire le liste standard.

