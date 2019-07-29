# Precauzioni nella definizione del gruppo distinta
Nel caso di definizione del gruppo distitnta se esso non è al livello minimo = 0, occorre agganciare un codice allo stesso livello in distitnta e non intestare ad un codice a livello superiore, per non alterare il livello minimo dei componenti.

 In questo modo, gli impegni di risorse sono agganciati al documento di testata (ordine produzione / documento V5) e si può usare la routine di controllo chiavi generalizzata £GMK (anche per le parzializzazioni). - è la stessa che si usa per la gestione del documento nel dettaglio del GMRRIM.
Nel caso di impegni risorse, __dopo__, c'è la gestione della fase (fatta con routines specifiche).

![BRDIST_09](http://localhost:3000/immagini/BRDIST_N1/BRDIST_09.png)