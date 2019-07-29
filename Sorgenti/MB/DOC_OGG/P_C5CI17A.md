
# Obiettivo

Tramite questa funzione verrà prodotto il file da trasmettere all'Agenzia Delle Entrate.

Prima di procedere è necessario controllare : 
DATI AZIENDALI
* Ragione sociale
* Partita Iva
* Codice Fiscale
* Impresa non Residente per Stabile Organizzazione (estensione £54)
* Soggetto Rappresentato (estensione £42)
* Comune
* Indirizzo
* CAP
* Provincia
* Nazione
DICHIARANTE
* Codificare il soggetto dichiarante
* Codice Fiscale soggetto dichiarante

# Richiesta Parametri

* Tipologia di invio : 
**   - INVIO ORDINARIO - Normale Trasmissione dei Dati prima della scadenza. Verranno elaborati tutti i movimenti presenti nell'archivio per il periodo in elaborazione, ad eccezione dei movimenti per cui è già stata registrata la ricevuta dell'Agenzia Delle Entrate tramite l'azione X, ed i movimenti per i quali è stata forzata l'esclusione tramite il campo "validità".
** A - ANNULLAMENTO - Trasmissione che annulla una comunicazione o singoli documenti, precedentemente inviati di cui è stata registrata la ricevuta di accettazione tramite l'azione X. Per annullare una precedente comunicazione inviata bisogna compilare il campo "ID File per Annullamento Intera Comunicazione". In questo caso verrà creato un file XML di annullamento e verrà cancellata la rispettiva ricevuta di accettazione registrata tramite l'azione X. Per annullare un singolo movimento entrare nella gestione di dettaglio (tramite azione M o scheda di interrogazione), settare il campo "Ann/Rett" ad A, ed effettuare  la trasmissione di annullamento. In questo caso verrà creato un XML per ogni documento cancellando dai record interessati la ricevuta di accettazione registrata tramite l'azione X.
** R - RETTIFICA    - Trasmissione che rettifica singoli documenti precedentemente inviati di cui è stata registrata la ricevuta di accettazione tramite l'azione X. Per rettificare un singolo movimento entrare nella gestione di dettaglio (tramite azione M o scheda di interrogazione), settare il campo "Ann/Rett" a R, ed effettuare la trasmissione di rettifica. In questo caso verrà creato un XML per ogni documento.
**ATTENZIONE :  in caso di annullamenti/rettifiche l'ID file da indicare è quello riportato come 'ID Sistema Ricevente' nella comunicazione di avvenuto ricevimento inviata dall'Agenzia delle Entrate

* Tipo Elaborazione : 
**   - Acquisti e Vendite  - Verrà creato il file degli acquisti ed il file delle vendite
** A - Acquisti            - Verrà creato solo il file degli acquisti
** V - Vendite             - Verrà creato solo il file delle vendite

* Id File per Annullamento Intera Comunicazione :  in caso di annullamento di una intera comunicazione, compilare questo campo con l'identificativo file trasmesso dall'Agenzia Delle Entrate e registrato nelle ricevute di accettazione tramite l'azione X.

* Data Iniziale :  Data iniziale dei movimenti da trasmettere

* Data Finale   :  Data finale   dei movimenti da trasmettere

* Trasferimento :  mettendo un carattere qualsiasi nel campo, sarà possibile   accedere alla maschera in cui poter indicare il percorso ove verranno depositati i file della   comunicazione da inviare all'Agenzia Delle Entrate.   Il nome dei file verrà composto nel seguente modo : 
  ** IT + CodiceFiscale +_DF_+ Progressivo.XML. Il progressivo viene calcolato dal numeratore   in tabella CRN sottosettore C5 elemento J7.C5MCIV. Nel secondo semestre 2017 questo progressivo   partirà da 100.

* Numero Enti :  numero massimo di enti all'interno del file xml (assume 1000 da istruzioni tecniche)

* Numero Fatture Per Ente :  numero massimo delle fatture per ogni ente all'interno del file xml (assume 1000 da istruzioni tecniche)

* Byte massimi Per Ciascun File :  numero massimo di Byte per ciascun file. Se viene superato questo limite verranno creati più file.

* Trasmetti Cod.Fiscale Persona Fisica anche se P.IVA presente :  se settato questo parametro a fronte di persone fisiche aventi sia partita iva che codice fiscale, vengono trasmesse entrambe le informazioni

* Dichiarante :  Questa sezione va valorizzata solo se il soggetto obbligato alla comunicazione dei dati fattura non coincide con il soggetto passivo IVA al quale i dati si riferiscono. NON deve essere valorizzato se per il soggetto trasmittente è vera una delle seguenti affermazioni : 
** coincide  con il soggetto IVA al quale i dati si riferiscono;
** è legato da vincolo di incarico con il soggetto IVA al quale i dati si riferiscono;
** è un intermediario.

* Dati Dichiarante : 
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** Codice Carica :  codice carica del soggetto

# LOG EXCEL
Nella stessa cartella indicata nel trasferimento verrà creato il rispettivo csv con i dati trasmessi. Questo Excel riporta tutti i campi possibili da trasmettere ed ha la funzionalità di avere un log di quello che si stà trasferendo per identificare eventuali anomalie tramite filtri o funzioni.
  Il nome dei file verrà composto nel seguente modo : 
  ** IT + CodiceFiscale +_DF_+Progressivo+_A.CSV per gli acquisti
  ** IT + CodiceFiscale +_DF_+Progressivo+_V.CSV per le vendite

# LOG ESECUZIONE
Vegono prodotti file di spool suddivisi tra acquisti/vendite che permettono di verificare i parametri di lancio ed i file XML generati
