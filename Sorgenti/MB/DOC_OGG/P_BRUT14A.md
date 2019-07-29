# OBIETTIVO

Monitorare che i nostri acquisti in esenzione IVA e che gli acquisti dei nostri clienti non superino il plafond dichiarato all'Agenzia delle Entrate.

# PARAMETRI

Nella prima videata che il sistema ci propone si dovranno inserire i seguenti parametri : 

* Anno :  l'anno che intendiamo analizzare;
* Sezione :  è la sezione di fatture che vogliamo estrarre, è possibile scegliere tra emesse/ricevute o lasciare il parametro vuoto se vogliamo che il programma ci presenti sia le une che le altre;
* Tipo Elaborazione :  indica come vogliamo visualizzare la funzione, con _stampa_ la aprirà a video provvisoriamente, mentre _stampa e esegui_ andrà a scrivere effettivamente i dati estratti nel database;
* Dati :  in questo campo è consigliabile mantenere la dicitura _Solo dati mancanti_.

# STAMPA DI CONTROLLO

Una volta premuto INVIO il sistema mi proporrà il video della stampa interattiva, a questo punto, selezionando **S** nel campo **Esecuz. interattiva** e premendo INVIO dovremo andare nella linea comandi ed aprire lo spool di stampa appena lanciato.
Una volta aperto lo SPOOL di stampa vedremo che il programma avrà filtrato tutti i clienti per i quali avremo registrato dichiarazioni d'intento per importo e tutti i fornitori ai quali abbiamo spedito le dichiarazioni per importo da noi emesse.

Lo SPOOL si presenta in questa struttura : 


* gli enti, che siano fornitori o clienti, verranno filtrati in base alla partita IVA;
* ad ogni partita IVA è associato un ente, se le registrazioni estratte fanno riferimento ad un fornitore, sotto la partita IVA vedremo la sigla FOR seguita dal codice fornitore. Se l'ente preso in considerazione si tratterà di un cliente vedremo la sigla CLI seguita sempre dal proprio codice d'identificazione;
* sotto i dati sopracitati il programma presenta l'elenco delle dichiarazioni d'intento registrate a sistema che presentano il codice d'esenzione **N.I. art. 8/C** specifico per l'ambito, le prime dichiarazioni riportate sono quelle che hanno come parametro di riferimento il periodo, dopo di queste vengono elencate quelle per importo;
* per ogni dichiarazione d'intento il sistema scrive tutte le registrazioni contabili ad essa associate evidenziando il numero di registrazione, la data e l'importo. Con le dichiarazioni d'intento per importo il programma sottrae tutti gli importi in codice d'esenzione art. 8/C dal plafond dichiarato e riportato nel modulo, fatto questo scrive un totalizzatore che permette di controllare se il cliente o la nostra azienda ha superato il plafond a disposizione.




