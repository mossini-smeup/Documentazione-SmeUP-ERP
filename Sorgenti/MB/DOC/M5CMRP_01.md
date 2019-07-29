# Applicazione di massa suggerimenti da scheda

L'applicazione suggerimenti avviene in Looc.up dalla scheda dell'MRP.
Selezionando uno o più suggerimenti (Ctrl+Click sul rettangolo a sinistra di ogni suggerimento nelle liste consigli) e trascinando sui bottoni a destra si chiama l'applicazione di massa dei suggerimenti selezionati.
Esiste un limite di poco più di 1800 suggerimenti applicabili contemporaneamente, dovuto alla struttura di passaggio parametri all'applicazione.

# Personalizzazione dei bottoni disponibili

Per personalizzare la lista dei bottoni disponibili sulla destra (e quindi le possibili azioni applicabili sui suggerimenti) si personalizza la scheda M5CMRP_BA.
Si tratta di un semplice elenco di bottoni, l'unica cosa a cui prestare attenzione è il dinamismo sul Drop :  esso fa scattare l'applicazione sulla variabile [FROM.H£NORI], una lista di suggerimenti separati da ';'.
Il servizio M5SER_10, funzione 'APP.LIS', fornisce l'applicazione dei suggerimenti :  si verifichi l'help in testa al programma per i parametri di chiamata.
