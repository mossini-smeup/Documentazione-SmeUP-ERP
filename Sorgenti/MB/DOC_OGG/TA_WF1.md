# WF1 - Impostazioni generali workflow
## CONTENUTO DEI CAMPI
 :  : FLD T$WF1A **Min.ctr.invio prom.**
Tempo di attesa in minuti del programma WFPROM00 prima di eseguire il controllo della presenza di promemoria nel file WFPROM0F ed eseguirne l'invio sulla coda.
 :  : FLD T$WF1B **Rispedisci dopo min**
Minuti dopo i quali inviare nuovamente un promemoria per il quale l'utente non ha eseguito nessuna azione di risposta (non ha cioè posposto il promemoria, nè lo ha ripianificato, nè lo ha chiuso.)
 :  : FLD T$WF1C **Nome coda dati prom.**
Nome della coda dati con chiavi UTENTE e AMBIENTE utilizzata per la scrittura dei promemoria.
La coda deve trovarsi nella libreria SMEUPUIDQ.
Avendo in chiave l'ambiente è consigliato l'utilizzo di un'unica coda dati.
 :  : FLD T$WF1D **Ora termine ctr.**
Orario dopo il quale il programma WFPROM00 si chiude, terminando quindi il ciclo di controllo dei promemoria.
 :  : FLD T$WF1F **Log flussi WF (SV)**
Se attivo, in Loocup viene scritto su JALOGT il log di inizio e fine di ciascun passo di flusso eseguito. Non viene recepito da Webup.
