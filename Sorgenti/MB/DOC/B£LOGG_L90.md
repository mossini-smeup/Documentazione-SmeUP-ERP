## OBIETTIVO

Log di funzionamento di Looc.Up quando eseguito in modalità server.

## ATTIVAZIONE

Il log viene creato automaticamente quando Looc.Up è avviato in modalità server attraverso l'opzione di avvio --server.

## GESTIONE DATI DEL LOG

Il formato del file di log è il seguente : 

**server_<NOME SERVER>_<AS400>.log**

dove **NOME_SERVER** è il nome univoco associato all'istanza del server e serve per identificare lo specifico server sulla rete.

Il file di log contiene informazioni di vario tipo : 


* Log di comunicazione e di stato dei client collegati. Visualizza lo stato del client e registra i messaggi di comunicazione scambiati tra server e client.
* Elenco delle richieste di funzione ricevute sulla coda server (da AS400 attraverso la coda server o da client)
* Elenco delle richieste di tipo batch ricevute sulla coda, da client collegato o da processo Looc.Up esterno.
* Log delle operazioni del modulo BC (Businness Continuity). Registra i problemi del server e le eventuali di operazioni di ripristino dello stato operativo (riavvio,
switching su server di backup o chiusura controllata).


