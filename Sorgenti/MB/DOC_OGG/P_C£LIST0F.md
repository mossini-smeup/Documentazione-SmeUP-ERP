# ANAGRAFICO LISTINI - SERVIZIO UPDATE
## OBIETTIVO
 Attraverso questa exit, richiamata dal servizio LOSUP_13, si ottiene  la possibilità di gestire tramite matrice di  aggiornamento l'anagrafico dei listini.
## LIMITI
 Esistono però delle limitazioni rispetto alla gestione dell'anagrafico  listini che vengono qui descritte : 

 * La gestione si attiva solo se riceve la struttura del listino. Questo è assunto dal parametro Ogg(LSxxxyyyaa) dove xxx=Listino yyy=Sezione aa=area del listino
 * Lo schema di visualizzazione ricevuto deve essere congruente con la struttura ricevuta.    Questo viene garantito    utilizzando le liste (B£IQ2_LS).
 * I flussi sull'oggetto non sono gestiti.
 * L'exit, sulla sezione, non deve contenere aperture video.    L'errore ricevuto dall'exit non viene legato alla    colonna ma viene emesso un'errore generico.
 * L'aggiornamento è gestito con la modalità differita
 * Non è possibile gestire le note strutturate.

