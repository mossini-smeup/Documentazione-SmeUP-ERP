Ogni impegno di un ordine di workflow deve essere eseguito da un utente preciso, a meno che non si tratti di un impegno automatico.
La definizione delle modalità di assegnazione dell'esecutore di un impegno viene effettuata a livello di script di processo, caratterizzando in maniera opportuna la relativa transizione.

# Utente esecutore

È l'utente che deve eseguire / ha eseguito un impegno.

# Classe di esecutori

È l'insieme di utenti che possono potenzialmente eseguire un impegno.
Se la classe di esecutori è costituita da più utenti la definizione di chi eseguirà l'impegno può avvenire in due modi : 
 * Pull, ovvero uno degli utenti prende in carico l'impegno. A questo punto diventa l'utente esecutore dell'impegno, che non è più eseguibile dagli altri utenti.
 * Push, ovvero qualcuno abilitato decide quale utente nella classe di esecutori deve eseguire l'impegno, effettuando così un'operazione di assegnazione.


# Responsabile assegnazione

È l'utente / insieme di utenti abilitati ad assegnare un impegno, ovvero a decidere chi tra gli utenti appartenenti alla classe di esecutori dovrà eseguire l'impegno.
