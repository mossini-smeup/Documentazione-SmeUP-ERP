# Obiettivo

Tramite questa funzione verrà prodotto il file da trasmettere all'agenzia delle entrate.

Verranno elaborati tutti i movimenti presenti nell'archivio per il periodo in elaborazione ad eccezione dei movimenti per i quali è stato forzata l'esclusione tramite il campo "validità".

Risulta importante considerare che tramite questa elaborazione i dati verranno rielaborati ed eventualmente anche scartati a seguito dei controlli effettuati in questa sede.
Per questo è opportuno che venga sempre prima eseguita una o più elaborazione provvisoria e che solo a seguito dell'analisi delle stampe prodotte dell'elaborazione venga poi eseguita l'elaborazione definitiva.

In particolare è da notare che il risultato dell'analisi di ogni singolo movimento verrà memorizzato sull'archivio dei dati dello spesometro e potrà poi essere visualizzato sia nella gestione del dettaglio che tramite la stampa dell'archivio.

Prima di procedere è necessario controllare i dati anagrafici aziendali : 
* Ragione sociale
* Partita Iva
* Codice Fiscale
ed i parametri legati all'azienda
* Codice Attività (ATECO 2007)
* Indirizzo Mail
* Eventuali dati intermerdiario

Particolare attenzione, all'impostazione Dati Aggregati.
Il default è la trasmissione dei dati in maniera analitica e quindi verranno trasmessi i
dati di ogni singola fattura e compilati i seguenti i seguenti quadri : 
* QUADRO FE :  Fatture emesse
* QUADRO FR :  Fatture ricevute
* QUADRO NE :  Note di variazione emesse
* QUADRO NR :  Note di variazione ricevute
* QUADRO DF :  Operazioni senza fattura
* QUADRO FN :  Operazioni attive con soggetti non residenti
* QUADRO SE :  Acquisto di servizi non residenti
Se si sceglie la forma aggregata verranno trasferiti i totali per soggetto (a parità di partita
iva e/o codice fiscale), e verranno compilati i seguenti quadri : 
* QUADRO FA :  Operazioni documentate da fattura attive e passive
* QUADRO SA :  Operazioni senza fattura esposte in forma aggregata
* QUADRO BL :  Operazioni con soggetti non residenti

Nella stampe prodotte vanno in particolare analizzati : 
* Segnalazioni sulla singola registrazione (se trasmissione in forma analitica) o
sul totale per soggetto (se trasmissione in forma aggregata).
In particolare le segnalazioni saranno rivolte ad operazioni con segno coerente rispetto alle
specifiche tecniche dello spesometro.

Si sottolineano alcune particolarità : 
* QUADRO FA :  le note di credito clienti vengono messe nella sezione passiva delle note di variazione
             le note di credito fornitorei vengono messe nella seziona attiva delle note di
             variazione
* QUADRO BL :  le note di credito vengono decuratate algebricamente dal totale fatture, non essendoci
             la sezione dedicata
* QUADRO FN :  vengono escluse le note di credito, non essendoci una sezione dedicata
* QUADRO SE :  vengono escluse le note di credito, non essendoci una seziona dedicata

# Richiesta Parametri

* Tipologia di invio : 
** 0 - Invio ordinario - Normale Trasmissione dei Dati prima della scadenza
** 1 - Invio sostitutivo - Trasmissione che sostituisce una precedente comunicazione inviata
** 2 - Annullamento - Trasmissione che annulla una precedente comunicazione inviata, senza che vengano inviati nuovi dati sostitutivi

* Anno :  anno di riferimento dell'invio

* Definitiva :  indica che la trasmissione va considerata come definitiva. A fronte di questo aspetto i dati presi in considerazione non saranno più modificabili o cancellabili. I dati inclusi nella trasmissione assumeranno nel campo "Stato Trasmissione" il valore "2 - In definitiva"

* Dati Aggregati :  a seconda che sia valorizzato o i dati verranno prodotti nella forma aggregata o dettagliata.

* Dati Black-list :  è possibile apporre di filtri sui dati black-list

* Identificativo Iva Quadro BL :  solo se valorizzato ed è presente nell'archivio, viene trasmessa la partita iva italiana di un soggetto trasmesso nel quadro BL

* Trasferimento :  mettendo una carattere qualsiasi si accede alla finestra di impostazione nome e della cartella IFS (preceduta e e seguita dal caratttere "/") in cui verrà collagato il file da trasmettere all'agenzia.

* N° di Righe :  il file prodotto per la trasmissione può avere, secondo normativa, un numero massimo di righe pari a 40.000 record ed una dimensione massima di 5mb. Qualora tali limiti fossero superati risulta necessario inviare più file. Il limite delle righe è gestito automaticamente dal programma, per cui nel caso queste vengano superate, verranno prodotti automaticamente più file da trasmettere. Per quel che riguarda il limite di 5mb, questo dovrà essere tenuto sottocontrollo una volta prodotto il file o i file. Nel caso in cui questo limite venga superato, si potrà aggiustare la cosa, diminuendo il n° di righe massime proposto. Es. mettendo che un file di 40.000 righe abbia una dimensione superiore, tramite il campo n° righe sarà possibile diminuire i n° massimo di righe :  mettendo 35.000, verranno prodotti due file uno di 30.000 righe ed uno di 5.000. Operando in questo modo si dovrebbe poter arrivare al risultato voluto.

* Dati Soggetto Tenuto alla Comunicazione
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** Codice Carica :  codice carica del soggetto
** Data Inizio Procedura :  è necessaria nellipotesi in cui, ad esempio, a presentare la comunicazione sia l'erede od il curatore fallimentare.
* Dati Soggetto Intermediario
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** N° Iscrizione al CAF :  n° iscrizione al caf del soggetto
** Data dell'impegno :  è la data in cui chi si occupa della trasmissione se ne è assunto l'impegno.

* Protocollo Telematico (solo se annullamento o reinvio sostitutivo) :  protocollo della trasmissione, da sostituire/annullare
* Protocollo Documento (solo se annullamento o reinvio sostitutivo) :  protocollo documento della trasmissione, da sostituire/annullare

* Stampa Modelli :  produce la stampa cartacea dei modelli della comunicazione NOTA BENE :  il modello NE è suddiviso su due differenti pagine, una per i primi 9 dettagli ed una sola per il decimo. Per gestire questa situazione vengono prodotti due differenti file, uno con tutte le prime pagine del modello ed uno con tutte le ultime pagine del modello. Per riordinarle basta riordinare le pagine prodotte dai file in base al numero di modello.

# Stampe di Log

* Segnalazioni :  vengono elencati i movimenti che sono stati esclusi dalla trasmissione ed il motivo dell'esclusione. Tale indicazione viene memorizzata sull'archivio ed è visualizzabile sia dalla gesteione dell'archivio che nella stampa dell'archivo, sotto al dicitura "stato trasmissione".

* Dettaglio :  vengon elencati nel dettagli tutti i movimenti elaborati con due particolari evidenze : 
** se il movimento è stato trasmesso o meno
** in che modo differenti movimenti riferiti alla stessa fattura (essendo presenti più aliquote, o per effetto della presenza di note di variazione) si sono abbinati fra loro. Tale informazione viene evidenziata nella stampa, cercando il carattere "=".

* Segnalazione movimenti o totale sui soggetti qualora gli importi non siano corretti rispetto  alle specifiche tecniche .

* Log :  in questa stampa vengono riportati i modo preciso i dati effettivamente trasmessi. Rispetto alla stampa di dettaglio, non sono qui presenti le informazioni che vengono di fatto omesse dalla trasmissione effettiva (es. dettaglio dei movimenti, codice cliente/fornitore, ecc.).

