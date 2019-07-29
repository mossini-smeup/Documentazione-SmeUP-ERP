# Introduzione al modulo V5STAT

## Premessa (descrizione sintetica del modulo)
Il modulo STAT dell'applicazione V5 è dedicato alle statistiche di fatturazione.
Il modulo è costituito in estrema sintesi da : 
 * un file estratto dagli archivi transazionali :  il V5STAT0F
 * una struttura di schede Looc.UP per la sua analisi.

## Obiettivo del modulo
L'obiettivo del V5STAT è fornire uno strumento adeguato ad ottenere delle statistiche di fatturato attivo e passivo facilmente consultabili per l'azienda.

## Contenuto
I dati inclusi nella statistica includono attualmente 4 tipologie : 
 * L'**Attivo Contabilizzato**, che comprende le fatture e le note di credito del Ciclo Attivo registrate in contabilità. In sostanza costituisce una visione "analitica" della parte contabile relativa ai ricavi.
 * Il **Passivo Contabilizzato**, che riguarda le fatture e le note di debito del Ciclo Passivo registrate contabilmente, permettendo così di analizzare il dettaglio dei costi riportati in contabilità.
 * L'**Attivo Atteso**, che comprende le fatture e le note di credito del Ciclo Attivo non ancora contabilizzate e lo spedito in attesa di fatturazione.
 * Il **Passivo Atteso**, che riguarda tutti i documenti ricevuti da fornitori in attesa di fattura.

Vi sono anche : 
 * Il **Budget**, che comprende la parte relativa ai costi, quantità e valori (importi) previsti da un piano MPS.
 * L'**ordinato Attivo**, che rapprensenta invece l'insieme degli ordini di vendita (ordini clienti).
 * L'**ordinato Passivo**, che rappresenta l'insieme degli ordini di acquisto.

## Terminologia
### Ciclo Attivo/Passivo

- _2_Definizione ciclo attivo
Il ciclo attivo è l'insieme delle operazioni che un'azienda intrattiene verso i suoi Clienti e determina dei guadagni finanziari per quest'ultima. In sostanza, esso comporta le operazioni aziendali che permettono all'azienda di vendere i suoi prodotti e servizi e gestire tutte le fasi della vendita.
Le operazioni che costituiscono il Ciclo Attivo di una azienda comprendono : 
-- Gestione della anagrafica del Cliente con l'indicazione dei dati fondamentali del soggetto, come la ragione sociale, la P.I.,  le modalità di pagamento ecc.
-- Gestione dei documenti per la vendita del bene a partire dall'Ordine di vendita, per arrivare alla consegna del bene/servizio da parte dell'azienda, fino alla fattura attiva e alle note di credito attive.
Tramite tutte queste operazioni le aziende possono determinare anche con anticipo le entrate che si verificheranno.
- _2_Definizione ciclo passivo
Il Ciclo Passivo di una azienda è un insieme di azioni che la stessa intrattiene con i Fornitori e per cui ha delle uscite finanziarie.
Le attività che caratterizzano il Ciclo Passivo Aziendale sono : 
-- Definizione dell'anagrafica dei Fornitori. Ad ogni fornitore viene associato un codice univoco, una ragione sociale, una partita iva, un indirizzo, ecc...
-- Registrazione dei documenti che legano l'azienda al fornitore :  ordine di Acquisto, consegna delle merci/servizi, fattura passiva, eventuali note di credito passive.
Analizzando tale ciclo, possiamo sempre sapere i nostri impegni verso i fornitori, i servizi prestati e le spese che dovremmo sostenere in un determinato tempo.


### Contabilizzato/Atteso

- _2_Definizione contabilizzato
E' l'insieme dei documenti (fattura di acquisto e di vendita) registrati nel modulo della contabilità, ovvero che si trovano nell'applicazione C5.
- _2_Definizione atteso
Per atteso si intende l'insieme dei documenti (fatture e note di credito, bolle, ecc.) non ancora contabilizzati e in attesa di essere registrati in contabilità.

