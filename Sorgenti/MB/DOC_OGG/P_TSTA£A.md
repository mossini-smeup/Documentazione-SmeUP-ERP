# OBIETTIVO
Gestire le operazioni sul file A£TROR0F.
Tutte le operazioni avvengono individuando un record specifico mediante la terna (frase, contesto, ambito), dove il contesto è l'insieme di 6 campi che definiscono l'oggetto in cui la frase viene utilizzata.

# FUNZIONI E METODI

## DEL - Cancellazione
La funzione DEL cancella un record di A£TROR0F.

## WRI - Scrittura
La funzione WRI scrive un nuovo record di A£TROR0F.
Va passato, insieme alla terna che individua la frase, l'intero formato A£TROR da scrivere.
Vengono calcolati automaticamente : 
 * L'applicazione di appartenenza del contesto.
 * L'utente/data/ora di creazione dell'oggetto che contiene la frase. Questo si declina in diversi modi a seconda della tipologia di oggetto : 
 ** TAxxx :  Dati di aggiornamento (se presenti) o di inserimento dell'elemento di tabella stesso            (£RITES sull'elemento di tabella)
 ** ST, RET- :  Dati di aggiornamento (se presenti) o di inserimento della definizione della               tabella (da TABDS00F)
 ** OGSP :  Dati di aggiornamento (se presenti) o di inserimento dell'elemento di tabella INTxx           (xx = codice contesto) con codice uguale al Dettagio1
 ** OJxxxx :  Dati dell'ultima creazione dell'oggetto (OAV I/006, I/003, I/004 sull'oggetto OJxxxx)
 ** REF- :  Dati dell'ultima creazione del file (OAV I/006, I/003, I/004 sull'oggetto OJ*FILE)
 ** MBxxxx :  Dati dell'ultima compilazione del membro (ee attiva). Vengono usati i dati             dell'ultima creazione dello USRSPC corrispondento (OAV J/U06, I/018, I/019             sull'oggetto MBxxxx)

## UPD - Aggiornamento
La funzione UPD aggiorna un record esistente di A£TROR0F.
Va passato, insieme alla terna che individua la frase, il nuovo formato A£TROR che sostituisce il precedente.
Viene ricalcolato automaticamente : 
 * L'applicazione di appartenenza nel contesto.
 * Utente/data/ora di aggiornamento.
Vengono ripresi dal record già salvato : 
 * Utente/data/ora di inserimento.
 * Utente/data/ora di creazione dell'oggetto (all'atto della prima estrazione della frase).
 * Note 1/2.

