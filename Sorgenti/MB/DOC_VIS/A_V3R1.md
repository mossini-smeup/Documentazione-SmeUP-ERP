# Novità della nuova versione
Come di consueto, si è effettuato il consolidamento di tutte le implementazioni rilasciate dopo il 17/10/2007, data di disponibilità del precedente V2R3, inoltre sono state introdotti miglioramenti applicativi, miglioramenti architetturali e di utility di base.

# Miglioramenti applicativi
 * **Previsioni statistiche con il metodo Holt Winters"**, l'introduzione di questo pacchetto ha comportato : 
 ** la completa revisione del programma di calcolo delle funzioni matematiche B£MATE
 ** la rivisitazione dell'applicazione MPS (MP - Plan.UP) con il rifacimento ed ampliamento delle schede Looc.UP
 ** l'aggiunta di nuove funzioni di elaborazione viste piano ed un nuovo programma per la gestione delle sostituzioni di articoli (articolo in esaurimento ed articolo subentrante).
 * **Contabilità**
 ** __Scadenzario__, forma di presentazione per partita (tramite F17); evidenza totali scaduto / a scadere; metodo di interrogazione "S" dei soli soggetti che presentano uno scaduto
 ** __Lettere solleciti / estratto conto__, aggiunta la produzione in formato PDF
 ** __Tesoreria__, gestione Calcolo/Contabilizzazione Piano d'Ammortamento dei Finanziamenti; in conformità con la normalizzazione delle condizioni introdotta dalla PSD (Direttiva Europea per i Servizi di Pagamento) è stata introdotta la gestione di un rapporto di default "**"; interrogazione dei movimenti stimati per rapporto, i movimenti stimati sono determinati dalle scadenze ancora da presentare che, tramite le informazioni anagrafiche o l'utilizzo delle proposte, possono essere riconducibili ad un certo rapporto. tali movimenti posso poi essere inclusi nell'interrogazione aziendale delle proiezioni saldi.
 ** __Ratei / risconti__, è possibile attivare, da tabella C5D, la gestione per data competenza solo a livello gestionale e non fiscale. Inoltre già dalla tabella C5D è possibile attivare ora il calcolo per data invece che per mese.
 ** __Pratiche__, possibilità di includere (solo come visualizzazione) le scadenze bloccate; pratiche multivaluta su c/c in euro; nelle proposte, nell'importo disponibile, possibilità di includere anche il fido
 ** __IVA__, nella contabilizzazione da Sme.UP del ciclo attivo è stato aggiunto come default la contabilizzazione per conto/assoggettamento.
 ** __Contabilità generale__, possibilità, dalle interrogazioni di contabilità, tramite l'opzione 80 di poter consolidare manualmente un singolo movimento di registrazione; aggiunta, in base alla struttura definitiva dalla riclassifica BAS, del completamento automatico dell'ultimo livello del piano dei conti.
 * **Pianificazione materiali MRP**,
 ** nuove schede Looc.UP, per gruppo e per periodo per l'analisi globale dei risultati MRP
 ** rilascio multiplo dei suggerimenti da scheda Looc.UP
 ** possibilità di realizzare un HMRP (Home made MRP), attraverso una exit con cui diversificare i raggruppamenti e le datazioni dei suggerimenti
 ** possibilità di eliminare gli impegni pianificati per gli articoli gestiti a punto di riordino
 * **Gestione Produzione**, introduzione della nuova modalità di produzione MFP (Materials Flow Production) che gestisce l'avanzamento della produzione attraverso lo spostamento fisico dei contenitori, sono possibili : 
 ** rilavorazioni
 ** parallelismi
 ** disponibilità distribuita nel tempo
 * **Gestione Ciclo Esterno**,
 ** __nuova gestione KIT__, con questa gestione si può :  collegare righe "padre" a righe "figlie" all'interno dello stesso documento; costruire le righe figlie a partire da una "distinta kit"; scegliere se il costo della riga "padre" è ricavato sommando i costi delle righe "figlie"; spedire automaticamente le righe "figlie" collegate ad una riga "padre"; scegliere se le righe padre e/o figlie sono rilevanti per la disponibilità.
 ** gestione facoltativa del lock dell'intero documento (testata e righe)
 ** modifica alle interfacce testata e righe documento (£ido e £idr)
 ** modifiche struttura exit
 ** modifica a Visualizzatori Gruppo £VS
 ** modifiche alla contabilizzazione fatture
 ** __ri-estazione provvigioni__, cioè possibilità di estrarre di nuovo le provvigioni dai documenti anche dopo che erano state estratte una prima volta
 * **Gestione Post_Acquisto**, standardizzato il giro completo di emissione fatture (note di debito e note di credito) VERSO fornitori :  creazione / stampa / contabilizzazione
 * **Workflow**, razionalizzate le dinamiche di creazione di nuovi workflow e gestione dei flussi di esecuzione; miglioramenti su Azioni di contesto
 * **Gestione dati di base** : 
 ** modificata l'interfaccia contatti £IFCON
 ** modificati i programmi di gestione distinta base : 
 *** possibilità di gestire il formato di dettaglio a 132 colonne
 *** nella copia di un legame di distinta aggiunta anche la copia dei commenti
 *** possibilità di impostare, nella exit di controllo pre salvataggio, che NON venga eseguita la scrittura della distinta
 * **Gestione materiali**, possibilità di utilizzare il collo nelle chiavi variabili della GMF
 * **Gestione indici**, nuova exit in scrittura Igrept/Igstor
 * **Gestione classi**, migliorata la gestione parametri
 * **Gestione manutenzione**, rivisitata tutta l'applicazione MM - Mant.UP. In particolare : 
 ** __gestione macchine/impianto__ :  aggiunti campi data/num/cod/flag per parametri impliciti; oggettizzato Database con adeguamento agli standard Sme.UP
 ** __gestione interventi__ :  lancio dei flussi automatici; aggiunti campi data/num/cod/flag per parametri impliciti; oggettizzato database; unificato programma di gestione sia per interventi pianificati che non pianificati; gestione data/ora inizio e data/ora fine
 ** __gestione materiali di manutenzione__, possibilità di chiamare pgm di ripresa materiali ad-Hoc (impostato in tab MMO)
 ** __schedulatore interventi__, eliminata gestione multimembro del file degli interventi estratti e sostituita con il codice di raggruppamento
 * **Gestione modifiche tecniche**, rivisitata tutta l'applicazione MT - Prom.UP. In particolare : 
 ** introduzione di azioni di applicazione della modifica tecnica alle distinte basi e agli esponenti di modifica
 ** possibilità di attivare la gestione del processo di modifica tecnica attraverso il workflow
 ** normalizzazione archivi (flag, numeri, date, alfanumerici liberi) e ridenominazione campi per disambiguarli rispetto ad altri archivi
 * **Posta elettronica certificata (PEC)**,  è possibile utilizzare la /copy G53 per l'invio di mail di posta certificata (PEC), tramite normali account di posta certificata.
 * **Single Sign On (SSO)**,  con il rilascio della V3R1 di LoocUp è stata introdotta la possibilità di autenticarsi all'iSeries  utilizzando Single Sign On (SSO) basato su kerberos. Obiettivi principali
 ** rendere la sicurezza trasparente all'utente finale; per cui l'utente deve rendersi conto di lavorare in un sistema sicuro, ma non deve assolutamente vivere la sicurezza come un onere aggiuntivo;
 ** rendere semplice la gestione della sicurezza da parte degli amministratori;                   
 ** (nell'ottica del multipiattaforma) rendere trasparente allo sviluppatore la gestione dell'autenticazione tra server. Es. server iSeries che con programma RPG recupera dati da Server DB Oracle
 * __Applicazione in Sme.UP__ :  nel nostro caso il sistema è l'iSeries dove risiede Sme.UP e il client è Looc.UP oppure Client Access. Il sistema di autenticazione responsabile della sicurezza e del rilascio delle credenziali sarà il server di dominio Windows 2008 (presso il quale ci siamo autenticati dal nostro PC). In questo modo, per dirla in breve, quando client Access o Looc.Up chiederanno accesso all'iSeries, quest'ultimo verificherà che le questi applicativi client siano muniti di credenziali rilasciate dal server di domino responsabile della sicurezza. Il protocollo kerberos sarà il linguaggio comune attraverso il quale i diversi sistemi potranno comunicarsi e verificare l'attendibilità delle credenziali. Nota. Kerberos è un protocollo che permette l'autenticazione crittografata tra client (es. Looc.Up o Client Access) e server (es. iSeries) o tra server e server (es. iSeries e Windows 2008).

# Evoluzioni applicative presenti nelle ultime "dev" della V2R3
Tra le ultime evoluzioni applicative presenti nella V2R3 e conglobate nella V3R1 possiamo citare : 
 * **Statistiche V5**, estensione e completamento modulo V5STAT con attivazione anche per il ciclo passivo. Il modulo permette di : 
 ** garantire la congruenza fra i dati contabili e i dati di fatturato, le statistiche di vendita/acquisto sono quindi anche il dettaglio di una registrazione contabile
 ** semplificare l'analisi di vendite e acquisti attraverso alcuni report preparati standard
 ** utilizzare in modo esteso le nuove funzionalità grafiche di Looc.UP : 
 *** Filtri
 *** SQL
 *** Costruttori standard per analisi
 * **Filtro generalizzato Q3**, filtro che utilizza le funzioni SQL che, oltre alle normali parzializzazioni da - a, permette di filtrare attraverso liste di inclusione e/o liste di esclusione e/o con selezioni dirette SQL (uguale, maggiore di, lista valori, scansione, ecc...)
 * **Oggetto lista**, nuove funzioni dell'oggetto lista e alla sua /COPY di interfaccia £G40 : 
 ** rivisto il motore di caricamento delle liste che ora, dove possibile, sfrutta le /COPY dell'UP SQL.
 ** introdotto il concetto di programma fonte :  possono essere implementati dei programmi che date, in input, le risposte ad alcune domande, permettono di caricare gli elementi della lista in un modo specifico
 ** nuove modalità di determinazione della lista (oltre alle precedenti elenco di codici e filtri per attributi) : 
 *** programmi di fonte
 *** filtri Q3 (Riconoscibili fra le istanze dal suffisso E/)
 *** carrelli utente intestati all'oggetto (Riconoscibili fra le istanze dal suffisso C/)
 ** introdotta la classe d'autorizzazione specifica LI
 ** introdotta la lista "*" come elemento fisso che permette di ottenere l'elenco di tutte le istanze della classe oggetto
 * **Applicazione suggerimenti di acquisto da contratto** :  derivazione ordine da contratto, con accodamento a ordine derivato da contratto o con creazione nuovo ordine; la riga creata deriva sempre le informazioni dalla riga contratto di riferimento
 * **Migliorie a gestione lotti qualità da scollegamento documenti V5** :  possibilità di inibire la cancellazione del lotto quando la riga del documento viene scollegata; attivazione del flusso di Post-Cancellazione Lotto della Qualità in caso di scollegamento di una riga documento
 * **Integrazione con sistemi documentali**, è stato sviluppato un modulo generalizzato di interfaccia con sistemi documentali, al momento sono attive interfacce verso ArchiBox e CompEd.

# Miglioramenti architetturali e tecnici
 * Razionalizzazione dell'uso dei Gruppi di Attivazione
 * Revisione gestione errori
 * Aumentata la flessibilità della "localizzazione" (lingua, separatori decimali ecc.)

## Revisione di archivi con l'introduzione di nuovi campi e/o nuovi logici
 * File A5MOVI0F - Movimenti cespiti
 * File BRARES0F - Dati Articolo/Ente
 * File BRDINT0F - Dichiarazioni d'Intento
 * File C5TREG0F - Testate Contabili
 * File C5RREG0F - Righe Contabili
 * File C5RATE0F - Rate Contabili
 * File C5SOLL0F - Solleciti
 * File C5ICEE0F - Movimenti Intrastat
 * File GMTRIM0F - Testate Richieste di movimentazione
 * File GMRRIM0F - Righe Richieste di movimentazione
 * File GMCOLL0F - Colli
 * File GMDAIN0F - Rettifiche di Inventario
 * File P5TEOP0F - Ordini di produzione
 * File V5TDOC0F - Testate Documenti
 * File V5RDOC0F - Righe Documenti

## Miglioramenti a utility varie
 * Aggiunta la possibilità di installare contemporaneamente di più versioni di SmeNS e SmeDG
 * Aggiunta la possibilità di inviare mail precedentemente salvate come .eml
 * Portato a 80 il massimo di flag inseribili in un archivio
 * Aggiunta la possibilità di "storicizzare" i numeri di un oggetto
 * Migliorata la gestione SETUP e Memorizzazione dati video
 * Migliorata la gestione date in matrici di aggiornamento
 * Migliorata la gestione variabili in scheda
