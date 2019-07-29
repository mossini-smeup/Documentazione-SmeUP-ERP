## Obiettivo

Attraverso questo programma è possibile generare il file per la trasmissione dei dati relativi a operazioni con enti appartenenti a paesi black list.

Verranno elaborati tutti i movimenti presenti nell'archivio per il periodo in elaborazione ad eccezione dei movimenti per i quali è stato forzata l'esclusione tramite il campo "validità".

Risulta importante considerare che tramite questa elaborazione i dati verranno rielaborati ed eventualmente anche scartati a seguito dei controlli effettuati in questa sede.
Per questo è opportuno che venga sempre prima eseguita una o più elaborazione provvisoria e che solo a seguito dell'analisi delle stampe prodotte dell'elaborazione venga poi eseguita l'elaborazione definitiva.

In particolare è da notare che il risultato dell'analisi di ogni singolo movimento verrà memorizzato sull'archivio dei dati Black List e potrà poi essere visualizzato sia nella gestione del dettaglio che tramite la stampa dell'archivio.

Prima di procedere è necessario controllare i dati anagrafici aziendali : 
* Ragione sociale
* Partita Iva
* Codice Fiscale
ed i parametri legati all'azienda
* Codice Attività (ATECO 2007)
* Indirizzo Mail
* Eventuali dati intermediario

Si sottolineano alcune particolarità : 
* Verrà compilato il QUADRO BL fissando il campo BL002002 (operazioni con paesi fiscalità
  privilegiata)='1' (Si)
* Vengono inclusi anche i movimenti di San Marino di tipo reverse charge
* Le note credito clienti vengono messe nella sezione passiva delle note di variazione
* Le note credito fornitori vengono messe nella sezione attiva delle note di variazione

# Richiesta Parametri

* Tipologia di invio : 
** 0 - Invio ordinario - Normale Trasmissione dei Dati prima della scadenza
** 1 - Invio sostitutivo - Trasmissione che sostituisce una precedente comunicazione inviata
** 2 - Annullamento - Trasmissione che annulla una precedente comunicazione inviata, senza che vengano inviati nuovi dati sostitutivi

* Periodo :  periodo di riferimento dell'invio

* Definitiva :  indica che la trasmissione va considerata come definitiva. A fronte di questo aspetto i dati presi in considerazione non saranno più modificabili o cancellabili. I dati inclusi nella trasmissione assumeranno nel campo "Stato Trasmissione" il valore "2 - In definitiva"

* Escludi operazioni < 500 ¤ :  in questo punto possono essere escludi i movimenti con importo
  inferiore a 500 Euro, per totale soggetto inferiore a 500 Euro o nessuna esclusione

* Identificativi IVA :  se impostato a '1' (Si) verrà trasmesso per ogni soggetto   l'identificativo iva (partia iva o codice fiscale nel BL002001).
  Se non impostato non verrà trasmesso l'identificativo iva.

* Trasferimento :  mettendo una carattere qualsiasi si accede alla finestra di impostazione nome e della cartella IFS (preceduta e e seguita dal carattere "/") in cui verrà collegato il file da trasmettere all'agenzia.

* Dati Soggetto Tenuto alla Comunicazione
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** Codice Carica :  codice carica del soggetto
** Data Inizio Procedura :  è necessaria nell' ipotesi in cui, ad esempio, a presentare la comunicazione sia l'erede od il curatore fallimentare.
* Dati Soggetto Tenuto alla Comunicazione
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** N° Iscrizione al CAF :  n° iscrizione al caf del soggetto
** Data dell'impegno :  è la data in cui chi si occupa della trasmissione se ne è assunto l'impegno.

* Protocollo Telematico (solo se annullamento o reinvio sostitutivo) :  protocollo della trasmissione, da sostituire/annullare
* Protocollo Documento (solo se annullamento o reinvio sostitutivo) :  protocollo documento della trasmissione, da sostituire/annullare

* Stampa Modelli :  produce la stampa cartacea dei modelli della comunicazione

# Stampe di Log
* Log :  in questa stampa vengono riportati i modo preciso i dati effettivamente trasmessi.
Per trovare le anomalie è necessario cercare nello spool la stringa *ER.

Per confermare l'esecuzione del programma digitare F6 da tastiera o il relativo pulsante a video.
