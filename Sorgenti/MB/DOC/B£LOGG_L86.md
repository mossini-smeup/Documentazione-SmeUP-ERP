# Obiettivo
Loggare la comuncazione.

# Surf
## Dettaglio log
Visualizza l'elenco di tutti i log esistenti.
Nel campo "Data inizio" e "Data fine" è possibile selezionare il periodo, nel campo "Utente" lo USRPRF e "Solo errori" seleziona solo i log con errori.
L'ordinamento è temporale discendente, dal log più recente al più vecchio.
E' un servizio paginato e vengono mostrati 100 record alla volta.
Queste le informaizoni mostrate
* Tipo record :  identifica la tipologia delle informazioni loggate (S-FUN di richeista servizio / C-Program Call o FUN di Comunicazione / D-Dettaglio di altra chiamata / X - Non riconosciuto)
* Lavoro / Utente (di sistema) / Numero sessione
* Ambiente
* Utente applicativo
* Device
* Dettagli dell'informazione loggata (dipende dal tipo record)
** Per FUN :  Servizio / componente / funzione.metodo
** Per le Program Call :  £JACMS / £JACFU / £JACME
* Data / Ora evento (dati di ricezione-inizio della FUN / Program Call)
* Data / Ora ultima operazione (dati di completamento operazione)
* Programma che riceve la FUN / Program Call
* Master :  codice che raggruppa tutti i record di un'unica sessione (sia FUN che Program Call)
* ID Sessione :  Id sessione di JOB
* JOB sottomettente :  ID del JOB che ha effettuato la sottimissione del record a cui fa riferimento il log
* Tipo Azione :  più dettagliato rispetto a "tipo record" : 
** FUN :  esecuzione FUN
** DET :  Dettagli di altra chiamata
** COL :  FUN di collegamento
** JA :  Program Call
** PNG :  ping
* Timestamp :  istante di ricevimento
* Durata in ms
* Durata significativa :  Se flaggato significa che la durata indicata è stata correttamente calcolata
* Versione Log :  versione con cui è salvato il log
* Errore :  il record si riferisce ad una condizione di errore
* Utente QUSER :  l'utente di sistema effettivo è QUSER
* Campo libero :  ulteriori dettagli. Nel caso delle FUN contiene la FUN ricevuta

# Actions
## Eliminazione completa log utente
Dopo aver confermato di voler eseguire questa funzione vengono eliminati tutti i log dell'utente nel file JALOGT0F.

## Attivazione/disattivazione log
Tramite questa azione è possibile attivare o disattivare la raccolta dati di log comunicazione.
Viene visualizzato il campo specifico della tabella JA1.

# Nota sulla pulizia del file di log comunicazione
L'attivazione delle funzioni di log comunicazione è molto utile per l'individuazione di casi problematici, ma scrive un elevato numero di dati.
Per questo si consiglia (soprattutto in caso di attivazione del log per tutte le informazioni disponibili) di schedulare operazioni di pulizia periodiche.
Per fare questo è stato previsto un programma di pulizia (B£LOG4). Questo è un programma generico di pulizia del JALOGT0F, pertanto è necessario specificare che si vogliono cancellare i dati di log relativi alla comunicazione. Nello specifico, il programma di pulizia riceve in ENTRY questi tre parametri : 
 * funzione
   **   'FLU'     :  cancella log flussi
   **   'BAT'     :  cancella log LOA27 (Batch)
   **   'COM'     :  cancella log di comunicazione
   **   'LIN'     :  cancella log modulo A£LING
   **   'LIB'     :  cancella log in base a TREC() E ORIG() ricevuti in parametro
 * metodo (al momento sempre '')
 * utente
 * data minima
 * parametro
 * libreria (se passato '' assume il JALOGT0F in linea)
Una volta lanciato pulisce tutti i dati di log (su JALOGT0F) dell'origine passata (LOC per il log comunicazione), dell'utente passato e con data minore della data passata.
E' possibile passare la keyword *ALL ai parametri utente e data per indicare di cancellare i dati di tutti gli utenti e/o di tutte le date.
E' possibile anche indicare una data dinamica, in questo modo è possibile schedulare una chiamata del tipo :  CALL PGM(B£LOG4A) PARM('COM' '' '*ALL' '_&_OGI60-' '_&_OGI02-' '' '') che cancella i dati di log di tutti gli utenti di oltre 60 giorni fa (e quelli più vecchi di 2 giorni per i dati di dettaglio se T$JA1F='9')
Per eseguire la riorganizzazione del file dopo la cancellazione dei record richiamare il B£LOG4B.

