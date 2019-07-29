# GA1 - Personalizz. richieste acq.
## OBIETTIVO
Permette di configurare l'applicazione GARDA ( F0 ) Gestione Richieste di Acquisto.
## CONTENUTO DEI CAMPI
 :  : FLD T$TVDS __Vds da tab. CLS 1=Si__
Modalità di definizione utilizzata nel modulo gestione delle Fatture.
 :  : FLD T$GA1A __Ricl.ass.per rich.__
Numero di riclassifica per l'assegnazione automatica della classificazione della richiesta, quando l'oggetto è un articolo.
 :  : FLD T$GA1T __Tipo oggetto.__
Indicano il Tipo oggetto a cui punta il campo Centri di costo/Rif. della tabella GAU
 :  : FLD T$GA1P __Parametro oggetto.__
Indica il Parametro oggetto a cui punta il campo Centri di costo/Rif. della tabella GAU. Se il tipo oggetto è bianco, assumerà nella tabella GAU 'CC' (centri di costo).
 :  : FLD T$GA1F __Pgm di controllo esterno.__
Se impostato e se non è presente nella tabella del tipo richieste (GAR), nella manutenzione della richiesta viene eseguito questo progamma per implementare controlli specifici.
 :  : FLD T$GA1G __Tipo destinatario.__
Indicano il Tipo oggetto a cui punta il campo destinatario.
 :  : FLD T$GA1H __Parametro destinatario.__
Indicano il Parametro oggetto a cui punta il campo destinatario.
 :  : FLD T$GA1I __Pgm Azioni speciali.__
Indicano un nome di un pgm in cui è possibile eseguire delle opzioni personalizzate, dalla lista richieste (GARDA0L). Il pgm della lista va eseguito con il carattere £ nell'azione (vedi documentazione tecnica per ulteriori informazioni).
 :  : FLD T$GA1C __Conferma ordine__
Se questo campo è impostato a 'S', verrà richiesta la conferma sulle singole righe dell'ordine generato; se vale 'L', verrà presentata la lista delle righe generate, con la possibilità di modifica. Se questo campo vale blank, non verrà richiesta nessuna conferma sulle righe generate.
 :  : FLD T$GA1Z __Parzializz.in validaz.libera__
Se impostato, vengono eliminate tutte le impostazioni prefissate in parzializzazione
 :  : FLD T$GA1W __Inserimento immediato__
Se impostato, nell'inserimento di una nuova richiesta non si passa dalla conferma (F06). Se invece lasciato in bianco, con F06 si passa direttamente al formato di scelta del tipo richiesta, mentre con l'immissione si ripresenta il formato con i campi di numero richiesta e numero riga modificabili e si passa alla finestra di scelta del tipo richiesta con un'ulteriore immissione.
