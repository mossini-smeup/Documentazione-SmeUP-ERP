# Definizione
La gestione delle estensioni permette di aggiungere alle informazioni normalmente contenute negli archivi anagrafici anche altri dati di natura anagrafica ma che non sempre sono presenti o di cui esiste la necessità di gestione, inoltre la funzione permette di gestire, per lo stesso ente, anche numerose informazioni della stessa natura (es. lista dei contatti telefonici all'interno di un cliente). La struttura permette sia di gestire elementi predefiniti a standard che elementi a supporto di gestioni specifiche dell'implementazione (estensioni utente). La configurazione di tali elementi viene definita nella tabella BRI ed è disponibile dal file modello delle tabelle.

# Elementi standard
Alcuni elementi sono predefiniti a standard, di seguito ne viene riportato l'elenco. La configurazione di tali elementi viene definita nella tabella BRI ed è disponibile dal file modello delle tabelle.
 * _2_£01 Indirizzi di spedizione. Permette di estendere gli indirizzi di spedizione (è direttamente collegato ai campi dell'anagrafica E§TSPE/E§CSPE). Rappresenta i soggetti a cui spedire la merce.
 * _2_£02 Indirizzi di contabilizzazione. Permette di estendere gli indirizzi di contabilizzazione (è direttamente collegato ai campi dell'anagrafica E§TCON/E§CCON). Rappresentano i soggetti a cui fatturare (es. l'azienda intestataria della bolla fa parte di un gruppo aziendale, ed il pagamento viene effettuato dalla holding del gruppo).
 * _2_£03 Indirizzi di conferma. Permette di estendere gli indirizzi di conferma (è direttamente collegato ai campi dell'anagrafica E§TCIN/E§CINC). E' legato agli ordini, un soggetto fa l'ordine, ma un altro lo deve confermare (un esempio è il sopracitato caso del gruppo aziendale).
 * _2_£04 Indirizzi di tratt. prezzo. Permette di estendere gli indirizzi di tratt.prezzo (è direttamente collegato ai campi dell'anagrafica E§TPRZ/E§CPRZ).
 * _2_£05 Indirizzi di corrispondenza. Permette di estendere gli indirizzi di corrispondenza (è direttamente collegato ai campi dell'anagrafica E§TCRR/E§CCRR).
 * _2_£06 Indirizzi di vettore. Permette di estendere gli indirizzi di vettore (è direttamente collegato ai campi dell'anagrafica E§TVET/E§CVET). Rappresentano i soggetti che possono eseguire il trasporto.
 * _2_£07 Modelli ammessi. Ha lo scopo di definire i vari modelli disponibili o non disponibili per un tipo documento su un ente.
 * _2_£08 Param. fatturazione. Ha lo scopo di indicare il calendario fatturazione e n° copie della fattura.
 * _2_£09 Partite IVA. Per chi non attiva la gestione dei data-effective direttamente sull'anagrafico, permette di definire le modifiche per partita IVA sulla data.
 * _2_£10 Home page internet. Definisce le pagine internet collegate all'ente.
 * _2_£11 Documenti/Allegati specifici. Elenco dei documenti accompagnatori (TAV5C).
 * _2_£12 Percorsi validi. Elenco dei percorsi validi (TAV5W).
 * _2_£13 Lettere di esenzione.
 * _2_£14 Dati specifici per modello. Elenco per TAV5A per i quali è possibile inserire dati specifici del modello (es. codice pagamento spese assoggettamento ecc.).
 * _2_£15 Vettori e Agenti Aggiuntivi.
 * _2_£16 Indirizzi E-MAIL. Definisce gli indirizzi mail collegati all'ente.
 * _2_£17 Contropartite contabili. Definisce le contropartite usuali di un fornitore (se non è previsto il controllo bolle fatture passivo).
 * _2_£18 Numero R.I.D.. Definisce il numero di R.I.D. se previsto.
 * _2_£19 Indirizzo Alternativo Riba. Definisce l'indirizzo da indicare nella trasmissione delle riba attive. Un caso di esempio è quello in cui un soggetto fa riferimento per la gestione delle riba ad un società esterna ("Centrale di pagamento").
 * _2_£20 Calendario alternativo. Definisce una fonte di calendario alternativa rispetto a quella prevista dal tipo contatto.
 * _2_£21 Coordinate bancarie. Permette di estendere le coordinate bancarie utilizzabili sull'ente.
 * _2_£22 Piano campionamento forzato.
 * _2_£23 Livello camp. forzato.
 * _2_£24 C.F.It.per non resid. mod. 770. Codice fiscale interno per non residenti utilizzato in 770.
 * _2_£25 MSN messenger.
 * _2_£26 S.I.P..
 * _2_£27 Indirizzo IP.
 * _2_£28 Skype.
 * _2_£29 Matricola Enasarco. Per un soggetto che è un'agente permette di indicarne il n° matricola Enasarco.
 * _2_£31 Tipo Ente Cessione. Definisce il soggetto a cui vengono ceduti i crediti intestati all'ente. I bonifici bancari verranno intestati perciò a questo ente.
 * _2_£32 Codice Agente (per fornitore).
 * _2_£34 Parametri spedizione/consegna.
 * _2_£35 Sede Amministrativa.
 * _2_£40 Dati Persona Fisica. Definisce i dati specifici della persona fisica.
 * _2_£41 Dati Percipiente. Definisce i dati specifici del percipiente.

### Tabella Estensioni contatti
- [BRI - Tipi estensioni contatti](Sorgenti/MB/DOC_OGG/TA_BRI)

