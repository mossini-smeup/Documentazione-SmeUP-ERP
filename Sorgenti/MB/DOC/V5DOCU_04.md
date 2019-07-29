# Obiettivo
Fornire una base di lancio per programmi da eseguire UNA E UNA SOLA VOLTA alla fine di un insieme di operazioni manuali (transazione) su un documento V5.

Questi flussi sono necessari perchè : 
 * I flussi I-DO vengono lanciati prima dell'inserimento delle righe.
 * I flussi M-DO vengono lanciati dopo l'inserimento delle righe ma solo se ho effettuato ulteriori modifiche alla testata.

# Quando vengono lanciati
Alla fine di un insieme di operazioni su un DO o DR se ho fatto partire un aggiornamento su uno dei record del DO e di una delle sue righe. Ad esempio : 
 * Alla fine dell'inserimento (inserisco testata, lavoro sulle righe, torno in testata -> all'uscita, con o senza ulteriore modifica di testata, lancio il flusso).
 * Alla fine della modifica di una riga se entro direttamente sulla riga senza passare dalla testata (ad esempio azione di G18 su  un DR).
 * Alla fine di modifiche fatte entrando con l'opzione 'RI' sul guida delle testate.

## Note varie di funzionamento
 * Se entro in modifica su un DO, F07 per passare a righe ed esco senza effettuare modifiche :  il flusso viene comunque lanciato, perchè sull'F07 viene aggiornata la testata; se invece entro con 'RI' dal formato guida della gestione testata ed esco senza modificare le righe il flusso non viene lanciato, perchè nessun record è stato toccato.
 * Il flusso viene lanciato alla fine (quindi DOPO gli eventuali altri flussi di testata e riga).
 * È disponibile il campo £FUNFT della £FUND1 per sapere come nasce il flusso di transazione : 
 ** '0' dall'inserimento di nuovo documento (compreso il caso inserimento, righe, modifica).
 ** '1' da una modifica di testata (compresa l'opzione 'RI' per modificare le righe).
 ** '2' da una modifica diretta di riga (ad esempio chiamata diretta da deviatore su DR).

# Implementazione
Questi flussi vengono attivati da un'opportuna B£H (T-DO***) :  la presenza dell'elemento adeguato per il DO in esame attiva la gestione dei flussi di transazione.
Tale gestione si appoggia a un programma "mongolfiera" (V5DO00T) che valuta lo stato della transazione e decide quando e come (da riga o da testata) lanciare il flusso.

NB :  per personalizzazioni di inserimento/modifica righe in lista è necessario riportare sui programmi personalizzati la chiamata al lancio del flusso di transazione (vedi ad esempio modifiche sui programmi V5DO19A/V5DO20A).
