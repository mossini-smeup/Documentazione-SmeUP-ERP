# Obiettivo

La finalità dei promemoria è quella di emettere un messaggio a popup in loocup.
Tipicamente i promemoria sono legati ad un impegno di workflow, ma è possibile creare anche promemoria indipendenti dagli impegni.

In estrema sintesi, quindi : 
 * Un promemoria è un record di database intestato a oggetto (utente)/data/ora.
 * I promemoria aperti vengono scanditi periodicamente e, quando data/ora vengono raggiunte o superate, vengono emessi sul Looc.up dell'utente interessato, che può posporli o chiuderli.

# Prerequisiti

È necessario avere installato almeno la versione V3R2M121109 di Loocup.
È necessario che sia presente la libreria SMEUPUIDQ in cui creare la coda dati per l'emissione dei promemoria.

# Descrizione del funzionamento

## Scrittura dei promemoria

I promemoria sono record del file **WFPROM0F** intestati a un oggetto destinatario tramite i campi F3TIPO, F3PARA e F3CODI; attualmente tale oggetto deve essere un utente applicativo (oggetto UP).
Un promemoria destinato ad un gruppo o ad una lista di utenti viene quindi esploso scrivendo una serie di record (uno per ciascun utente), in modo da poter gestire separatamente per ciascun utente lo stato del record così come la posposizione del promemoria.
I promemoria possono essere scritti : 
 * Automaticamente, ad esempio come **conseguenza esterna** di qualche impegno di workflow (e.g. all'attivazione dell'impegno viene impostato un promemoria alla sua scadenza).
 * In modo manuale (come in un calendario/scadenzario) realizzando una scheda di interfaccia utente.

## Emissione dei promemoria

In sintesi : 
 * Per ogni ambiente di Sme.up in cui sono attivi i promemoria è attivo un job che scandisce periodicamente i promemoria attivi;
 * Per ogni promemoria attivo per cui è stata raggiunta o superata la data/ora di emissione viene aggiunta una notifica del tipo notifica impostato in tabella WFP sul tipo promemoria.
 * In Looc.UP , Web.UP o Mobile viene visualizzato un messaggio popup che segnala la presenza del promemoria. Cliccando sul messaggio viene aperta una scheda che visualizza tutti i promemoria dello stesso tipo e ne permette la gestione. (La funzione richiamabile è personalizzabile configurando opportunamente la funzione di presentazione nello script del tipo notifica).


E' possibile modificare testo della mail impostandolo sul tipo mail (SE.SUB.A17), nelle note del promemoria o tramite la exit WFPROM00_* il cui suffisso è tabellato in WF1.


# Impostazione dell'ambiente per l'emissione dei promemoria

Servono : 
 * Un job per ogni ambiente in cui sono attivi i promemoria;
 * La configurazione degli elementi di tabella WFP con opportuni tipi notifica (SE.SUB.A60).

## Tabelle da impostare
- [Impostazioni generali workflow](Sorgenti/MB/DOC_OGG/TA_WF1)
- [Tipo Promemoria](Sorgenti/MB/DOC_OGG/TA_WFP)
L'oggetto **F3** promemoria ha come codice un contatore definito nell'elemento **OG.F3** della tabella **CRNWF**.

## Schedulazione del Job di scansione dei promemoria

L'emissione dei promemoria avviene tramite la schedulazione di un JOB che lanci il programma WFPROM00 ogni mattina.

Tale programma va schedulato : 
 * N volte, una per ambiente, con parametro 'START' per far partire il controllo dei promemoria.
- Es. CALL PGM(WFPROM00) PARM('START').
NB :  La schedulazione deve essere effettuata tramite l'opportuna scheda di schedulazione SMEUP, in modo che sia possibile lanciare il programma con l'ambiente corretto.
Per questo si rimanda a : 
 :  : DEC T(MB) P(DOC_NWS) K(NWS001549)
- [Lancio&-x2f;Esecuzione Programma batch](Sorgenti/MB/DOC/A£BASE_SM)

Il programma si chiude una volta superato l'orario impostato nella tabella di configurazione **WF1**.
Il programma esegue un ciclo di controllo sul file WFPROM0F restando in attesa per un tempo indicato in minuti nella tabella **WF1**.

**N.B. : **Trattandosi di un lavoro sempre attivo, prestare attenzione a schedularlo su una coda dedicata oppure su una coda *NOMAX


# Modalità di calcolo della data/ora di emissione del promemoria

La data ora di emissione del promemoria può essere calcolata in due modi (V2 WF_23)
 * 1 - Orario assoluto  :  la data ora di emissione viene indicata direttamente nel record del promemoria.
 * 2 - Tempo prima della data riferim.  :  la data ora di emissione viene ricalcolata in base alla  data di riferimento (sul record vengono indicati giorni, ore e minuti di anticipo rispetto alla  data di riferimento ai quali emettere il messaggio).

In caso la modalità di calcolo della data ora sia "2 - Tempo prima della data riferim.", la data di riferimento è indicata nella tabella **WFP** (Tipo promemoria) tramite i valori del V2/WF_24  : 
 * 0 - Libero;
 * 1 - Data attivazione impegno;
 * 2 - Data rich.esec.impegno;
 * 3 - Data rich.esec.ordine.

Nella tabella **WFP** viene anche indicata la modalità di calcolo della data/ora utilizzata per inizializzare il record di WFPROM0F tramite la /copy £WFF. La £WFF consente comunque la forzatura di una modalità di calcolo differente.

E' anche possibile creare dei promemoria non collegati ad un impegno di workflow utilizzando un tipo promemoria la cui data di riferimento abbia valore "0 - Libero" (a modello è presente l'elemento £02).


