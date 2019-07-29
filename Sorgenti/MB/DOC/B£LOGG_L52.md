# Obiettivo
Loggare il funzionamento della G53 per i Mail inviati e per i Pdf generati secondo un formato strutturato.

# Surf
## Visualizzazione dati di trace
Visualizza l'elenco di tutti i log esistenti.
Nel campo "Modello" è possibile selezionare la visualizzazione dei soli Mail inviati o dei soli Pdf generati. In entrambi i casi vengono elencate tutte le informazioni specifiche, lasciando invece il campo vuoto vengono selezionati tutti i tipi di log, pertanto vengono visualizzate solo le informazioni generiche.
Per parzializzare la visualizzazione è possibile selezionare una data massima (fino a) ed ordinare i log in modalità ascendente o discendente.

 * Opzioni possibili nella visualizzazione MAIL
 ** Cliccando sulla prima colonna Log (con la lente di ingrandimento) vengono visualizzati tutti i dati del singolo log nella parte inferiore della scheda.
 ** Cliccando sulle colonne Oggetto, Testo, Mittente, Destinatario, CC e BCC vengono visualizzati tutti i dati del singolo argomento.

 * Opzioni possibili nella visualizzazione PDF
 ** Cliccando sulla prima colonna Log (sulla lente di ingrandimento) vengono visualizzati tutti i dati del singolo log, nella parte inferiore della scheda.

### Nota su funzioni e metodo
Le funzioni e i metodi mostrati sono quelli "interni", non è detto che corrispondano a quelli dell'effettivo richiamo della G53.
Ad esempio a fronte di una singola chiamata alla £G53 con funzione PDF - G&M_AS4 (crea PDF ed invia mail) vengono effettuate due chiamate alla parte java e quindi due log distinti :  uno accessibile da modello MAIL e uno da modello PDF.

## Visualizzazione dati di log
Informazioni visualizzate in modo strutturato : 
 * ORIGINE (Smens o Smedg)
 * STATO del processo (INIT, PROCESS, CLOSE)
 * LIVELLO (INF, ERR, ...)
 * ISTANTE (Data e ora)
 * DATI (log)
 * ID CHIAMATA G53 (ID passato dalla parte RPG della G53)
 * VERSIONE (versione smens o smedg)

Per visualizzare il contenuto completo del file selezionare "File di Log", viene visualizzato il contenuto completo del log in formato non strutturato.


# Actions
## Eliminazione completa trace utente
Dopo aver confermato di voler eseguire questa funzione vengono eliminati tutti i log dell'utente sia nel file JALOGT0F che nella cartella di trace.

## Attivazione/disattivazione trace
Tramite questa azione è possibile attivare o disattivare la raccolta dati di trace da parte della £G53.
E' possibile attivare/disattivare separatamente il "log di sistema" (ossia quello scritto dalla parte Java su file IFS) e il "log di ambiente" (ossia quello scritto dalla parte RPG su file di database - JALOGT0F).

# Nota su pulizia file di trace
L'attivazione delle funzioni di trace è molto utile per l'individuazione di casi problematici, ma scrive un elevato numero di dati.
Per questo si consiglia (in caso di attivazione permanente del trace) di schedulare operazioni di pulizia periodiche.
Per fare questo è stato previsto un programma di pulizia (B£LOG3). Questo programma riceve in ENTRY due parametri : 
 * utente
 * data minima
Una volta lanciato pulisce tutti i dati di trace (quindi sia record su JALOGT0F che file nella cartella trace) dell'utente passato e con data minore della data passata.
E' possibile passare la keyword *ALL ad entrambi i parametri per indicare di cancellare i dati di tutti gli utenti e/o di tutte le date.
E' possibile anche indicare una data dinamica, in questo modo è possibile schedulare una chiamata del tipo :  CALL PGM(B£LOG3) PARM('*ALL' '_&_OGI60-') che cancella i dati di log di tutti gli utenti di oltre 60 giorni fa.

