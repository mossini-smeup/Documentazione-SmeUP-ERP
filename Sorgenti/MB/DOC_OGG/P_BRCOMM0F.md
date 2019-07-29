# ANAGRAFICO COMMESSE - SERVIZIO UPDATE
## OBIETTIVO
 Attraverso questa exit, richiamata dal servizio LOSUP_13, si ottiene la possibilità di  gestire tramite matrice di  aggiornamento l'anagrafico delle commesse.
## LIMITI
 Esistono però delle limitazioni rispetto alla gestione dell'anagrfico commesse  che vengono qui descritte : 

 * La gestione si attiva solo se riceve il tipo commessa. Questo è assunto dal parametro Ogg(CMxxx).
 * Lo schema di visualizzazione ricevuto deve essere congruente con il tipo commessa ricevuto.    Questo viene garantito    utilizzando le liste (B£IQ2_CM).
 * I flussi sull'oggetto non sono gestiti.
 * Il passo di costruzione codice non è gestito.
 * L'exit, sul tipo commessa, non deve contenere aperture video.    L'errore ricevuto dall'exit non viene legato alla    colonna ma viene emesso un'errore generico.
 * L'aggiornamento è gestito con la modalità differita
 * Se viene richiesto l'inserimento, ed è presente un numeratore, questo viene    incrementato immediatamente se però    non viene convermato il numero non viene recuperato.
 * Non è possibile gestire le note strutturate.

