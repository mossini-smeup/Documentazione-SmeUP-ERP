# L'archivio
In Sme.up l'archivio dedicato a questo scopo è il C£MODI0F, che presenta i seguenti campi significativi : 
 * Scenario
 * Contesto
 * Soggetto
 * Tipo verbo
 * Verbo soggetto
 * Oggetto
 * Verbo oggetto
 * Attributo

Lo Scenario è l'insieme universo in cui definire le relazioni significative tra oggetti. E' un oggetto fisso di SmeUp (tipo V2MDI00) di cui sono attualmente disponibili cinque opzioni : 
 :  : PAR L(TAB)
Scenario|Descrizione
APP|Applicazioni
ENV|Ambienti
LIB|Librerie (Sospeso)
PRO|Programmi
DOC|Documenti
SCP|Script
W/U|Where Used


Non viene posto alcun vincolo sulla definizione di nuovi scenari, ma poiché l'identificativo dello scenario è il primo elemento della chiave primaria è bene che essi siano assolutamente indipendenti tra di loro nel concetto o nell'utilizzo pratico, per evitare di allineare relazioni condivise nei programmi di alimentazione del file (per esempio, se creassimo lo scenario "Oggetti", questi non sarebbe indipendente dallo scenario "Applicazioni", in quanto, essendo le applicazioni degli oggetti, le relazioni mappate sullo scenario applicazioni dovrebbero essere replicate su quello degli oggetti). La definizione degli scenari, che è il primo passo da fare nella costruzione di un modello dinamico, è un'operazione delicata e tutt'altro che banale.

Il "Tipo Contesto" e "Contesto" è un oggetto applicativo "OG" che serve ulteriormente a precisare l'ambito della relazione; anche in questo caso non esistono regole ma è chiaro che l'oggetto contesto dovrà essere connesso in maniera logica allo scenario. Nel caso dello scenario "Applicazioni" viene ad esempio naturale pensare che la singola applicazione possa fungere da contesto.

Le colonne Soggetto, Verbo soggetto, Oggetto, Verbo oggetto e i rispettivi tipi e descrizioni contengono gli elementi della proposizione. Sia soggetto che oggetto sono oggetti applicativi che possono coincidere con il contesto o essere oggetti in esso contenuti. Il verbo oggetto è il verbo della relazione inversa se esiste o è significativa. Entrambi i tipi verbo sono oggetti fissi di SmeUp cioè oggetti di tipo V2MDI01 che prevede le seguenti famiglie di verbi : 
 * ATT         Attributi di un oggetto
 * DBA         Utilizzo nel database
 * APP         Appartenenza ad un gruppo
 * ERR         Indicazione di errore
 * TEC         Tecnica (Programmi/Campi/Ecc)

Un'ulteriore precisazione della relazione è fornita da Tipo Attributo, Attributo. Si possono cioè pensare delle relazioni impostabili con un attributo valorizzato.
Esistono allo stato attuale tre formati diversi di attributo : 
 * ATT         Attributi   xx="yy"
 * XML         Formato xml <a> <b xx="yy"/></a>
 * REC         Record      Ogg.RE (10+15) + dati

# La struttura dei programmi
Attualmente la visualizzazione dei modelli dinamici è disponibile solo su Looc.up, attivando il modulo C£MODI dell'applicazione C£. Il servizio C£SER_03 creato a tale scopo è fornito di una serie di metodi di visualizzazione e di organizzazione dei dati dei modelli, che leggono direttamente dal C£MODI0F. Con la funzione SER inoltre si può lanciare il programma di aggiornamento del modello C£MODI0G, che riceve in ingresso 3 parametri indispensabili :  scenario, tipo contesto e contesto. Il lancio dell'aggiornamento del modello dinamico è anche disponibile su Sme.up. Per gli scenari Ambienti e Applicazioni viene lanciato il programma (servizio) XX_MDI01, che carica il file facendo perno sui metodi messi a disposizione dalla /copy £MDI.
In figura la struttura dei programmi in gioco : 

![C£MODI_018](http://localhost:3000/immagini/C£MODI_C/CXMODI_018.png)
Questi programmi di caricamento richiedono una preventiva analisi delle relazioni significative che costituiranno il modello. Per inserire nuovi modelli basta creare il programma che alimenta il file attraverso la £MDI e agganciarlo al programma di smistamento C£MDI0G, senza preoccuparsi della visualizzazione. I metodi di visualizzazione e organizzazione dei dati restano infatti sempre e comunque applicabili ad ogni modello perché leggono le informazioni direttamente dal file.

## Creazione step by step
La creazione di un modello dinamico richiede come prerequisito un'analisi accurata dell'ambiente, delle relazioni e degli oggetti che si ritengono significativi per l'indagine.
Sme.up lascia piena libertà nella configurazione di scenari e contesti, che tuttavia può portare a creare modelli confusi, difficili da aggiornare e indagare. Occorre pertanto seguire alcune regole nella fase di progetto : 
 * Individuare gli scenari di azione tenendo conto che devono essere assolutamente indipendenti... anche se a livello logico scenari diversi potrebbero avere oggetti in comune occorre pensare a livello pratico gli scenari come insiemi ad intersezione nulla, a meno che non si decida di gestire aggiornamenti incrociati;
 * Aggiungere gli scenari nuovi all'oggetto fisso V2MDI00;
 * All'interno degli scenari classificare i contesti, gli oggetti che si ritengono significativi ragionando in termini di inclusione dal generale al particolare (il contesto dovrà essere contenuto nello scenario, soggetto e oggetto dovranno appartenere al contesto);
 * Definire le relazioni significative e associarle ad un verbo opportuno e individuare la categoria del verbo nell'oggetto fisso tipo verbo V2MDI01;
 * Creare un programma specifico per l'aggiornamento del contesto che utilizzi la £MDI a tale scopo; agganciarlo al C£MDI0G con una funzione specifica per scenario nel main del programma;
 * Non occorre creare programmi o servizi di visualizzazione; nel caso si vogliano nuove funzionalità di indagine aggiornare il C£SER_03 tenendo conto che tali migliorie saranno disponibili per qualsiasi modello.
