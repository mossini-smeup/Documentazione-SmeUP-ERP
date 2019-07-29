# CSE - Errori nel calcolo costi std
 :  : DEC T(ST) K(CSE)
## OBIETTIVO
Facilitare la gestione e la caratterizzazione degli errori di costo da parte dell'utente.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Il codice è libero ma deve avere corrispondenza con quanto definito nel programma di gestione degli errori
 :  : FLD T$TIER **Tipo errore / Gravità errore**
Liberamente definibili dall'utente, se presenti vengono riportati nell'archivio di memorizzazione errori, per facilitare la ricerca e le selezioni.
_9_Esempio
Potremo associare un TIPO a tutti gli errori che riguardano l'ufficio acquisti, ecc.
 :  : FLD T$PCER **Programma di controllo**
Se indicato ed esiste, può essere direttamente richiamato dal programma di visualizzazione errori.
_9_Esempio
Se l'errore indica la mancanza del tempo di lavoro su un ciclo, potremo scrivere un semplice programma che, in funzione di codice e fase, permette di aggiornare direttamente il tempo nel DATABSE aziendale.
L'applicazione non contiene programmi specifici di correzione.
Essi andranno scritti dall'utente in funzione del tipo di errore. Con l'applicazione è semplicemente fornito un prototipo da cui partire.
