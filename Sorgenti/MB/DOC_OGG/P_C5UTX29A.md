# OBIETTIVO

 Questo programma elabora i movimenti intra relativi ai servizi riverificando il campo "nazione pagamento". In presenza di differenze viene prodotto un elenco delle stesse e in modalità "esecuzione" vengono generati dei movimenti di rettifica per la correzione di tali differenze.

E' da considerare che tali rettifiche dovranno comunque essere completate nei campi "protocollo" e "progressivo", per i quali vanno indicati il numero di protocollo ed il progressivo attribuiti al documento di origine nella prima trasmissione.
Per quel che riguarda il n° di protocollo questo può essere reperito in automatico se viene compilato tramite la funzione "Controllo dati presentazione".
Per quel che riguarda invece il progressivo, la sua memorizzazione è stata introdotta con l'implementazione di questo programma. Per poterlo aggiornare sullo storico è sufficiente eseguire una ristampa.
La presenza di entrambi i campi è riportata nelle ultime due colonne della stampa di controllo.

Altro aspetto da considerare è che se il documento origine è già stato oggetto di rettifiche, queste dovranno essere riportate manualmente sulla nuova rettifica generata in quanto la nuova rettifica viene generata a partire dai dati d'orgine.

# RICHIESTA PARAMETRI

* Data inizio :  data inizio del periodo da elaborare
* Data fine :  data fine del periodo da elaborare
* Data rettifica :  data che verrà attribuita alle rettifiche che verranno generate
* Modalità :  Stampa/Esecuzione (solo quest'ultima crea anche i record)

# DATI DI OUTPUT

* T  :  tipo movimento (acquisto/cessione)
* Id Origine :  n° movimento d'origine
* NzO :  nazione pagamento attribuita al movimento d'origine
* Id Rettif. :  n° movimento rettifica (se modalità stampa per tutti presenta **)
* NzR :  nazione pagamento attribuita al movimento di rettifica
* Soggetto :  ente intestatario
* P.IVA :  partita iva
* Data Orig. :  data di elaborazione del movimento originale
* Importo :  importo del movimento
* N°Prot. :  n° protocollo del documento
* Dt.Prot. :  data protocollo del documento
* Cod.Ser. :  codice servizio

