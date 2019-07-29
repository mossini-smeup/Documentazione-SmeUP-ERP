La finalità dei promemoria è quella di poter avere una notifica che viene emessa tramite un messaggio a popup in Loocup.
Tipicamente i promemoria sono legati ad un impegno di workflow, ma è possibile creare anche promemoria indipendenti dagli impegni.

In estrema sintesi, quindi : 
 * Un promemoria è un record di database intestato a oggetto (utente)/data/ora.
 * I promemoria aperti vengono scanditi periodicamente e, quando data/ora vengono raggiunte o superate, vengono emessi sul Looc.up dell'utente interessato, che può posporli o chiuderli.

# Prerequisiti

È necessario avere installato almeno la versione V3R2M121109 di Loocup.

# Funzionamento

## Scrittura dei promemoria

I promemoria sono record del file WFPROM0F intestati a un oggetto destinatario tramite i campi F3TPMA e F3CDMA; attualmente tale oggetto deve essere un utente applicativo (oggetto UP).
Un promemoria destinato ad un gruppo o ad una lista di utenti viene quindi esploso scrivendo una serie di record (uno per ciascun utente), in modo da poter gestire separatamente per ciascun utente lo stato del record così come la posposizione del promemoria.
I promemoria possono essere scritti : 
 * Automaticamente, ad esempio come conseguenza esterna di qualche impegno di workflow (e.g. all'attivazione dell'impegno viene impostato un promemoria alla sua scadenza).
 * In modo manuale (come in un calendario/scadenzario) realizzando una scheda di interfaccia utente.

## Emissione dei promemoria

In sintesi : 
 * Per ogni ambiente di Sme.up in cui sono attivi i promemoria è attivo un job che scandisce periodicamente i promemoria attivi;
 * Per ogni promemoria attivo per cui è stata raggiunta o superata la data/ora di emissione viene scritto un XML di messaggio in una apposita coda dati;
 * Sui Looc.up degli utenti è attivo un listener che legge la coda dati ed emette in locale i promemoria trovati per l'utente.

# Impostazione dell'ambiente per l'emissione dei promemoria

Servono : 
 * Un job per ogni ambiente in cui sono attivi i promemoria;
 * Una coda dati;
 * Un listener attivo sui Looc.up degli utenti.

## Job di scansione dei promemoria

L'emissione dei promemoria avviene tramite la schedulazione di un JOB che lanci il programma WFPROM00 ogni mattina.

Tale programma va schedulato : 
 * Una volta con parametro 'CLEAR' per eseguire la pulitura della coda (pulisce i promemoria scritti per tutti gli ambienti) - Es. CALL PGM(WFPROM00) PARM('CLEAR').
 * N volte, una per ambiente, con parametro 'START' per far partire il controllo dei promemoria e la loro scrittura sulla coda - Es. CALL PGM(WFPROM00) PARM('START').
NB :  La schedulazione deve essere effettuata tramite l'opportuna scheda di schedulazione SMEUP, in modo che sia possibile lanciare il programma con l'ambiente corretto.
Per questo si rimanda a : 
 :  : DEC T(MB) P(DOC_NWS) K(NWS001549)
- [Lancio&-x2f;Esecuzione Programma batch](Sorgenti/MB/DOC/A£BASE_SM)

Il programma si chiude una volta superato l'orario impostato nella tabella di configurazione WF1.
Il programma esegue un ciclo di controllo sul file WFPROM0F restando in attesa per un tempo indicato in minuti nella tabella WF1.
Sempre nella stessa tabella viene indicato il tempo dopo il quale reinviare un messaggio se su di esso l'utente non ha eseguito nessuna azione di risposta (non ha cioè posposto il promemoria, nè lo ha ripianificato, nè lo ha chiuso.)

## Coda dati

Il programma di scansione dei promemoria scrive l'XML dei messaggi da emettere in una singola coda dati con chiavi UTENTE e AMBIENTE.
Il nome della coda da creare è anch'esso impostato nella tabella WF1; la coda viene creata automaticamente (se già presente viene pulita) in SMEUPUIDQ all'avvio del programma WFPROM00.

## Listener sulla coda dati dei promemoria

La lettura della coda avviene tramite un apposito listener di loocup attivabile tramite SCP_CLO aggiungendo le righe : 

 :  : C.LST Cod="£01" Txt="Listener coda con chiave" Add="localhost" Protocol="JAVA" Wiz="LST_DIR" Param="class=Smeup.smeui.uimainmodule.externallistener.java.keyedqueues.UIKeyedQueueListenerManager;QNAM=WFPROM;QLIB=SMEUPUIDQ;WTO=60" LoadOnStartup="1" MaxDelay="60000" SendEvt="1" TypeLog="C1S0" MaxLog="1" NumDayLog="1"

I parametri da specificare sono la coda dati da leggere, la libreria in cui si trova e l'intervallo di attesa tra un tentativo di lettura e il successivo.
I parametri presenti nelle righe sopra riportate indicano di leggere la coda dati WFPROM nella libreria SMEUPUIDQ ogni 60 secondi (ogni lettura recupera un solo messaggio e poi si mette in attesa per il timeout specificato prima di leggere il messaggio successivo).

# Modalità di calcolo della data/ora di emissione del promemoria

La data ora di emissione del promemoria può essere calcolata in due modi (V2 WF_23)
 * 1 - Orario assoluto  :  la data ora di emissione viene indicata direttamente nel record del promemoria.
 * 2 - Tempo prima della data riferim.  :  la data ora di emissione viene ricalcolata in base alla  data di riferimento (sul record vengono indicati giorni, ore e minuti di anticipo rispetto alla  data di riferimento ai quali emettere la notifica).

In caso la modalità di calcolo della data ora sia "2 - Tempo prima della data riferim.", la data di riferimento è indicata nella tabella WFP (Tipo promemoria) tramite i valori del V2/WF_24  : 
 * 0 - Libero;
 * 1 - Data attivazione impegno;
 * 2 - Data rich.esec.impegno;
 * 3 - Data rich.esec.ordine.

Nella tabella WFP viene anche indicata la modalità di calcolo della data/ora utilizzata per inizializzare il record di WFPROM0F tramite la /copy £WFF. La £WFF consente comunque la forzatura di una modalità di calcolo differente.

E' anche possibile creare dei promemoria non collegati ad un impegno di workflow utilizzando un tipo promemoria la cui data di riferimento abbia valore "0 - Libero" (a modello è presente l'elemento £02).

L'oggetto F3 promemoria ha come codice un contatore definito nell'elemento OG.F3 della tabella CRNWF.
