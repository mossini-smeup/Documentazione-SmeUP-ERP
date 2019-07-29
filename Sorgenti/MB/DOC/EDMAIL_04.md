_3_GESTIONE RICEZIONE MESSAGGI

Per gestire questa funzione è sufficiente all'interno del proprio flusso EDI lanciare una chiamata
al pgm "EDAP02CL", il quale si occupa di tutta la gestione relativa alla ricezione dei dati sull'AS
producendo come output una copia del file EDFLAT0F in QTEMP, che potrà essere utilizzata in input
dallo specifico pgm di flusso per la scrittura dell'EDRECI0F.
Unici parametri di input di tale pgm sono il codice del flusso EDI in analisi e un'indicatore di
errore, da testare nel caso la ricezione non vada a buon fine.

