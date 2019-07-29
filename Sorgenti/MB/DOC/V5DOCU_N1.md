# Controlli modello documento in V5
 - Se impostato manualmente lo assume controllando che l'ente lo consenta (Inclusi/Esclusi) : 
 -- se "**I**" e non è in lista dà errore
 -- se "**E**" ed è in lista dà errore
 - Se non impostato e presente lista modelli inclusi prende il primo elemento
 - Se non impostato ed assente lista modelli inclusi prende il modello di default (da V5D)
 - Se non impostato e presente lista modelli esclusi prende il modello di default (da V5D) e controlla che non sia in questa lista
Dopo ogni inserimento non viene assunto l'ultimo modello inserito. Tutti i campi (ente / modello documento) vengono ripuliti
