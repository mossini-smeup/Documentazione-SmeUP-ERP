## Obiettivo
Analizzare e confermare i dati enasarco di un certo periodo a partire da quello che risulta sull'archivio del piano contributi.

## Parametri di lancio
* Anno :  è l'anno di riferimento
* Trimestre :  è il trimestre di riferimento che verrà analizzato
* Modalità :  determina la modalità di esecuzione. Le possibili scelte sono fra : 
** " "  :  permette di interrogare i dati del periodo indicato
** "D"  :  definitiva. Non si distingue dalla modalità di controllo se non che per il fatto che alla presentazione dei dati, viene aggiunto anche un tasto funzione di conferma, che fa si che i dati vengano certificati. NOTA BENE :  tale conferma ha come solo effetto il fatto di far avanzare la data della tabella B£4 "*CP", consolidamento provvigioni. Questa, blocca la modifica e la cancellazione dei dati dei piani dei periodi precedenti o uguali a tale data e nel caso il cui la contabilità sia l'applicazione master, blocca anche le registrazioni contabili pertinenti.
** "A"  :  annulla definitiva. Funziona come la modalità definitiva se non che con l'annullamento invece che portare avanti la data *CP, questa viene riportata indietro.
* Ultima data consolidata :  è solo un'informazione di output in viene riportato il valore attuale della data *CP.
* Anche non contabilizzati :  questa voce è presente solo l'applicazione master è il v5 e permette di decidere se comprendere o meno anche i dati enasarco, calcolati, ma non ancora finiti in contabilità.

## Dettaglio informazioni
* Dettaglio segnalazioni :  evidenzia la presenza di qualche incongruenza. Al click verrà aperta una finestra che le documenterà.
* Enasarco da contabilizzare :  evidenzia il fatto che l'enasarco non è ancora stato contabilizzato. Rispetto a questo possono presentarsi tre differenti condizioni : 
** La prima è quella per cui la fattura fornitore non è ancora stata registrata
** La seconda è quella per cui la fattura fornitore è stata registrata in provvisorio (in questo caso verrà proposto il riferimento della registrazione, ma comunque in questo caso l'enasarco risulta non contabilizzato. NOTA BENE :  se è necessario chiudere il periodo, quest'enasarco andrà contabilizzato attraverso la procedura apposita di contabilizzazione dei contributi; tale contabilizzazione avrà l'effetto di far se che al momento di rendere definitiva la fattura, su di essa sia rilevato il fatto che l'enasarco è stato già contabilizzato e che quindi vengano utilizzati specifici conti pertinenti.
** La terza è quella per cui non sono presenti provvigioni, ma è da versare esclusivamente l'enasarco calcolato per effetto del controllo dei minimali.
* Agente :  agente intestatario della riga
* Mese :  mese di liquidazione della provvigione
* Codice fiscale :  dell'agente intestatario
* Matricola Enasarco
* % :  eventuale % corrispondente all'agente nel caso in cui questo faccia parte di una società
* Importo provvigioni
* Imponibile enasarco
* Dovuto azienda :  enasarco a carico dell'azienda
* Dovuto agente :  enasarco a carico dell'agente
* Anticipo azienda :  enasarco che per effetto del controllo del minimale dovrà essere anticipato (o recuperato) dall'azienda
* Totale azienda :  enasarco totale che dovrà versare l'azienda, dato dalla somma del dovuto e dell'anticipo
* Totale enasarco :  sommatoria del totale azienda e del dovuto agente
* Registrazione :  registrazione contabile della fattura del fornitore
* Data registrazione :  data in cui è stata registrata la fattura del fornitore
* Condizione registrazione :  indica lo stato della registrazione (nel caso in cui non sia attiva)
* Valuta :  valuta della fattura
* Segnalazioni :  testo indicativo del tipo delle eventuali segnalazioni presenti

## Funzioni Disponibili
* Modifica piano :  solo per utenti gestori, permette di andare a rettificare manualmente il piano provvigioni
* Interroga piano :  permette di andare ad interrogare nel dettaglio la riga del piano provvigioni
* Cancella piano :  solo per utenti gestori, permette di andare a cancellare manualmente il piano provvigioni
* Dettaglio provvigioni :  permette di andare ad interrogare il dettaglio delle provvigioni che hanno generato il piano
* Scheda registrazione fattura fornitore :  permette di andare ad interrogare la registrazione della fattura del fornitore
* Dettaglio ritenute :  permette di andare ad interrogare il dettaglio delle ritenute collegate alla registrazione della fattura del fornitore
* Scheda del documento :  permette di andare ad interrogare il documento di proforma corrispondente
* Elenco righe documento collegate :  permette di andare ad interrogare le righe del documento di proforma corrispondente

