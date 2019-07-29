# AUTORIZZAZIONI APPLICATIVE - SERVIZIO UPDATE
## OBIETTIVO
 Attraverso questa exit, richiamata dal servizio LOSUP_13, si ottiene la possibilità di  gestire tramite matrice di  aggiornamento le autorizzazioni applicative.
## LIMITI
 Esistono però delle limitazioni rispetto alla gestione delle autorizzaioni applicatice che  vengono qui descritte : 

 * La gestione si attiva solo se riceve la classe. Questa è assunta dal parametro CUpd(xxx).
 * Lo schema di visualizzazione ricevuto deve essere congruente con il tipo classe ricevuta.    Questo viene garantito utilizzando le liste (B£IQ2_IDAU).
 * L'aggiornamento è gestito con la modalità differita
 * Non è possibile gestire i vari livelli dal record selezionato

