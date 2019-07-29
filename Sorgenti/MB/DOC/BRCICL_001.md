## Gestione dei cicli
Un ciclo descrive una sequenza di operazioni che devono essere eseguite per ottenere un articolo.

L'archivio principale è BRRICI0F che contiene la descrizione delle varie lavorazioni.
La tabella guida è la BRT
 :  : DEC T(ST) K(BRT)
a cui si rimanda per la documentazione di dettaglio.

Ciascuna lavorazione può essere creata con riferimento ad un'altra, si consiglia di creare un tipo ciclo "OPE" (operazioni) in cui descrivere l'"anagrafico" delle operazioni base e poi creare le varie fasi del ciclo di un articolo derivandole dalle operazioni base.

Un ciclo può essere anche identificato da una testata (codificata nell'archivio BRTECI0F), la testata ciclo agisce come metodo di selezione delle sequenze valide, a seconda delle impostazioni potremo avere la testata ciclo come "prefisso" o "suffisso" (cfr "Gestione alternative di ciclo" per una spiegazione più approfondita).
Comunque la testata ciclo non è obbligatoria e la quasi generalità delle implementazioni utilizza solo le fasi senza la testata.
