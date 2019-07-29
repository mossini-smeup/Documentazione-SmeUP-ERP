# ANAGRAFICO MATRICOLE - SERVIZIO UPDATE
## OBIETTIVO
 Attraverso questa exit, richiamata dal servizio LOSUP_13, si ottiene la possibilità di  gestire tramite matrice di  aggiornamento l'anagrafico delle matricole.
## LIMITI
 Esistono però delle limitazioni rispetto alla gestione dell'anagrafico  matricole che vengono qui descritte : 

 * La gestione si attiva solo se riceve il tipo matricola,    assunto dal parametro CUpd(xxx), e la stessa possiede    la categoria assunta.
 * La matricola verrà inserita utilizzando sempre la categoria assunta, questa non è modificabile.
 * Vengono visualizzati i soli documenti e enti descritti nella categoria.
 * La data del documento non è modificabile ma viene derivata dal documento stesso.
 * Lo schema di visualizzazione ricevuto deve essere congruente con il tipo matricola ricevuto.    Questo viene garantito    utilizzando le liste (B£IQ2_IDBR).
 * I flussi sull'oggetto non sono gestiti.
 * Il passo di costruzione codice non è gestito.
 * L'aggiornamento è gestito con la modalità differita
 * Non è possibile gestire le note strutturate.

