# Problema

Mediante workflow è possibile descrivere vaste classi di problemi, dalla semplice sequenza di operazioni al processo molto complicato, con elevate interdipendenze sia a livello di descrizione del processo (reti di Petri) che di oggetti Sme.up coinvolti.

Nel secondo caso è necessario porre dei vincoli sull'eseguibilità degli impegni per evitare potenziali situazioni di inconsistenza dovute all'esecuzione concorrente di impegni correlati.

Questo viene fatto allocando in certi casi l'ordine di workflow durante l'esecuzione di un impegno, per evitare che altri utenti possano in contemporanea agire sullo stesso workflow con risultati imprevedibili sullo stato dell'ordine e degli oggetti coinvolti.

L'allocazione viene testata quando un utente vuole eseguire un impegno : 
 * Entrando in una scheda di impegno se il workflow è allocato la scheda non viene presentata
 * Se il workflow non è allocato la scheda è visibile, il workflow non è ancora allocato
 * All'esecuzione di un'attività (ad. esempio dichiarazione) viene testata ancora l'allocazione : 
 ** se il workflow non è allocato l'impegno corrente lo alloca, viene eseguita l'attività e il workflow viene deallocato
 ** se il workflow è stato allocato nel frattempo l'attività non può essere eseguita fino a quando il workflow non sia stato deallocato

# Cosa c'è

 * È possibile attualmente definire, per un processo, due distinte modalità di gestione dell'allocazione : 
 ** All'ordine corrente :  viene testato e allocato l'ordine di workflow a cui appartiene l'impegno in analisi
 ** All'ordine root :  viene testato e allocato l'ordine root, ovvero partendo dall'ordine a cui appartiene l'impegno si risale per ordine master (F1NMAS), a più livelli, fino a quando non si incontra un ordine senza ordine master.


# Attenzione!

Adesso il motore di workflow automaticamente : 
 * se necessario testa e alloca il workflow prima di eseguire un'azione di workflow (presa in carico, dichiarazione, ...)
 * esegue l'azione, le sue conseguenze, allinea l'ordine...
 * al termine dealloca il workflow.
Questo viene fatto nell'intorno di un'azione. Non è ancora possibile, ad esempio, allocare il workflow alla presa in carico di un impegno e deallocarlo dopo la sua dichiarazione.
Questo potrebbe essere un problema se si vuole garantire la consistenza di dati esterni modificati ad esempio tramite matrice di aggiornamento (fuori dall'azione di workflow).



# Sviluppi futuri

 * Distinguere tra modalità di valutazione blocchi e modalità di scrittura (es. valuto allocazioni degli ordini master, alloca solo sè stesso)

 * Dettagliare per transizione le modalità di valutazione blocchi

 * Allocare certi impegni all'entrata nella scheda, deallocare all'uscita
 ** All'entrata :  nel test di allocazione faccio un test&lock
 ** All'uscita :  rimappare l'F12 per fare eseguire prima la deallocazione
