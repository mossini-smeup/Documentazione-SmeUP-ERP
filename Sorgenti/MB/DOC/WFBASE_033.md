Il modello semplificato dell'avanzamento di un impegno è il seguente : 
![WF-FIG0002](http://localhost:3000/immagini/WFBASE_033/WF-FIG0002.png)
I nodi rappresentano gli stati in cui ciascun impegno di workflow si può trovare, mentre gli archi sono le azioni di workflow necessarie per avanzare di stato.
Ogni azione di workflow genera un'attività (quindi lascia un log su tempo e utente di esecuzione).

Gli stati sono : 
 * Non pronto :  non sono soddisfatti i suoi requisiti (ad esempio non tutti i luoghi in ingresso contengono il token).
 * Assegnabile :  l'impegno è eseguibile ma non è ancora determinato univocamente l'utente esecutore.
 * Pronto :  l'impegno è eseguibile, l'utente esecutore è ben definito.
 * Preso in carico :  l'utente esecutore ha preso in carico l'impegno, ovvero ha cominciato il lavoro.
Lo stato "Non pronto" ed "eseguito" coincidono, perchè un impegno può essere eseguito più volte.

Le azioni di workflow sono : 
 * Attivazione :  è un'azione automatica, rende eseguibile un impegno.
 * Disattivazione :  è un'azione automatica che viene eseguita quando i requisiti non sono più soddisfatti prima che un impegno attivo sia stato svolto.
 * Presa in carico :  inizia l'esecuzione di un impegno (i token vengono tolti dai luoghi di ingresso). Ha una tripla valenza, ovvero l'utente che la esegue : 
 ** Dichiara di voler eseguire un impegno, quando questo è eseguibile da più utenti (l'impegno diventa esclusivamente suo).
 ** Dichiara di avere iniziato il lavoro sull'impegno (chi guarda lo stato dell'ordine vede che l'impegno è già in fase di svolgimento).
 ** Infine, consuma il token in ingresso, inibendo l'attivazione di eventuali impegni alimentati  dallo stesso luogo (impegni alternativi).
 * Assegnazione :  è l'azione con cui un utente decide chi svolgerà un impegno tra gli utenti abilitati a farlo.
 * Dichiarazione :  è l'azione di esecuzione vera e propria di un impegno -> alla fine della dichiarazione viene messo il token nei luoghi in uscita alla transizione.

Configurando opportunamente le transizioni nello script è possibile ottenere comportamenti diversi per gli impegni nell'ambito di questo modello.
Ad esempio : 
 *  se per un impegno viene configurato un singolo esecutore a livello di script l'attivazione porta in stato di pronto.
 * se per un impegno viene disabilitato il push non è attiva l'azione di assegnazione.
 * e così via.


