# Applicazione suggerimenti
Quando si applica un suggerimento questo viene portato a livello 8 se la qtà di applicazione e maggiore uguale della richiesta (applicazione con variazioni) oppure si dichiara saldato il suggerimento. Se si esegue una applicazione cumulata la qtà di rilascio va nella prima riga e le altre si sladano a zero (vanno tutte a livello 8). C'è la possibilità di annullare un suggerimento (se attivo va a livello 9).
Un suggerimento è poi riattivabile : 
 * se il livello è 9
 * se il livello è 8 e la qtà rilasciata è diversa da zero e minore della qtà suggerimento (vuol dire saldo forzato, se la qtà rilascita fosse zero si tratterebbe di una riga secondaria si un'applicazione cumulata e quindi non riattivabile)

**Nota bene**, nell'applicazione vengono sempre saldati gli impengi collegati indipendentemente che l'ordine sia stato applicato parzialmente
