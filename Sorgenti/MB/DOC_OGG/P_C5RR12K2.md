## Obiettivo
All'interno di questa videata è possibile visualizzare/gestire l'elenco delle scadenze incluse in una distinta

## Formato lista
il fornmato lista si presenta suddiviso in due parti : 
* Selezionati :  riporta l'elenco delle scadenze incluse nella lista
* Non selezionati :  riporta l'elenco delle scadenze non incluse nella lista ma che potrebbero esserlo. Ad esempio, se siamo in gestione di una pratica di bonifico a fornitori verranno presentate come selezionabili solo le rate aperte che riporano come tipologia di pagamento bonifico.

Per ogni rata sono riportati : 
 * Data scadenza
 * Importo in pagamento
 * Importo residuo
 * Numero e data fattura
 * A :  indica se sulla scadenza sono presenti abbuoni negativi (N), abbuoni positivi (P) o sconti (S)
 * T.P. :  indica la tipologia di pagamento della rata
 * L :  inidica la cumulabilità della rata (se libera il campo è vuoto, se è non cumulabile è compilato con 1 mentre se il cumulo è obbligatorio è compilata con 2)
 * B :  il campo è compilato con una W rossa se i dati bancari sono mancanti o non corretti, con una A azzurra se sulla scadenza sono riportare informazioni bancarie diverse da quelle riportate sull'anagrafica del soggetto (in questo caso è solo una segnalazione, non è un errore bloccante), con una N se la nazione della banca non è SEPA, con una I rossa se il codice Iban è assente, con una S se il codice Swift è mancante.
 * C :  riporta una segnalazione riferita al conto corrente. In particolare sarà compilato con W se il conto è assente o non valido o con una A se è dverso da quello riportato in anagrafica.
 * Cir :  nel caso in cui la banca del soggetto apaprtenga allo stesso circuito bancario di una delle banche aziendali viene esposto il codice della banca aziendale (questo potrebbe agevolare in termini di costi di presentazione)
 * Az :  indica il codice dell'azienda a cui appartiene la scadenza
 * Div :  indica la divisione a cui appartiene la scadenza.

In funzione di come sono compilate le parzializzazioni è possibile visualizzare le rate ordinate per cliente/scadenza oppure per scadenza/cliente oppure per importo/scadenza oppure per scadenza/importo.
Agendo sulle impostazioni è poi possibile visualizzare informazioni aggiuntive e totali riferiti alle scadenze selezionate e selezionabili

### Opzioni
Le opzioni possono essere a livello di raggruppamento (quindi su tutte le rate di uno stesso soggetto o di una stessa data scadenza, ecc) o a livello di scadenza e variano in funzione del fatto che si stia agendo sulle scadenze selezionate o su quelle non selezionate.
 * Opzioni di gruppo scadenze selezionate : 
 ** DG Deseleziona Gruppo :  permette di portare il gruppo scadenze tra quelle Non selezionate
 ** CG Cumula Gruppo :  permette di cumulare le scadenze incluse nel gruppo
 ** LG Decumula Gruppo :  permette di annullare il cumulo sulle scadenze del gruppo
 ** NO Modifica note ente :  nel caso in cui abbia un raggruppamento per soggetto permette di modificare le note presenti sull'anagrafica del soggetto
 ** SE Scadenzario Ente :  nel caso in cui abbia un raggruppamento per soggetto permette di visualizzare lo scadenzario residuo del soggetto.
 * Opzioni singole scadenze selezionate : 
 ** 05 Visualizzazione rata :  permette di visualizzare il dettaglio della rata
 ** 02 Modifica rata :  permette di visualizzare e modificare i dati di dettaglio della rata
 ** SR Sblocca rata :  permette di sbloccare una rata bloccata in pagamento
 ** D Deseleziona :  permette di riportare la rata tra quelle Non selezionate
 ** C Cumula :  permette di cumulare le rate che rispettano i criteri di cumulo impostati nel F17
 ** CP Cumulo parziale :  permette di cumulare le singole scadenze su cui è indicata l'opzione
 ** L Decumula :  permette di annullare il cumulo su una singola scadenza
 ** AC Annulla Anticipo :  nel caspo in cui si tratti di una anticipo permette di annularlo
 ** NO Modifica note rata :  permette di modificare le note della scadenza
 ** SE Scadenzario Ente :  permette di visualizzare lo scadenzario residuo del soggetto.
 * Opzioni di gruppo scadenze non selezionate : 
 ** SG Seleziona gruppo :  permette di portare il gruppo scadenze tra quelle Selezionate
 ** SE Scadenzario Ente :  nel caso in cui abbia un raggruppamento per soggetto permette di visualizzare lo scadenzario residuo del soggetto.
 * Opzioni singole scadenze non selezionate : 
** 05 Visualizzazione rata :  permette di visualizzare il dettaglio della rata
 ** 02 Modifica rata :  permette di visualizzare e modificare i dati di dettaglio della rata
 ** SR Sblocca rata :  permette di sbloccare una rata bloccata in pagamento
 ** S Seleziona :  permette di riportare la rata tra quelle Selezionate
  ** AC Annulla Anticipo :  nel caspo in cui si tratti di una anticipo permette di annularlo
 ** NO Modifica note rata :  permette di modificare le note della scadenza
 ** SE Scadenzario Ente :  permette di visualizzare lo scadenzario residuo del soggetto
 ** SC Lettera cumulo per ente : 
 ** SP Lettera cumulo per pratica : 

### Tasti funzionali
 * F01 Cerca :  permette di ricercare una stringa all'interno del formato lista
 * F02 Navigazione :  seguito dal tasto F01 permette di accedere alla documentazione della funzione
 * F03 Abbandona :  permette di uscire dalla videata
 * F04 Stampa lista :  permette di stampare la lista di scadenze
 * F05 Aggiorna :  aggiorna la videata
 * F06 Conferma
 * F09 Posizionamento a inizio :  il cursore si posiziona all'inizio della videata
 * F10 Posizionamento a fine :  il cursore si posiziona alla fine della videata
 * F12 Torna indietro :  permette di annullare l'ultima azione lanciata
 * F13 Parzializzazioni :  permette di accedere al filtro delle scadenze
 * F17 Impostazioni :  permette di accedere alle impostazioni
 * F18 Pos. Tot. Sel :  permette di posizionare il cursore sul totale delle scadenze selezionate
 * F19 Selezione globale :  permette di selezionare tutte le scadenze presenti nella sezione 'Non selezionati'
 * F20 Deselezione globale :  permette di deselezionare tutte le scadenze persenti nella sezione 'Selezionati'
 * F21 Crea anticipo :  permette di creare un anticipo
 * F23 Help :  permette di visualizzare una rapida guida delle colonne della videata

### F17 Impostazioni


## Formato dettaglio
I
