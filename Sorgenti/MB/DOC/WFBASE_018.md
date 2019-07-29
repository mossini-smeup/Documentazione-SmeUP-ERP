# Costruzione di un workflow

Un processo di workflow di codice PROCESSO è costituito da : 
 * Un elemento PROCESSO in tabella WFA, che definisce le proprietà generali del processo.
 * Uno membro PROCESSO dello script SCP_WFA, che definisce flussi, responsabilità e contenuto applicativo del processo.
 * (Opzionale) Un membro PROCESSO del file DOC_WFA, in cui si può mettere la documentazione operativa di processo.

Dalla scheda del modulo WFBASE, sottoscheda Base/Lista workflow, è possibile scegliere le due opzioni di creazione facilitata "Nuovo processo" e "Copia processo".
Si inserisce un codice per il processo (che non deve già esistere) e una descrizione per il processo, nel caso di copia anche il processo di partenza.
Confermando la creazione viene : 
 * Creato/copiato un corrispondente elemento di tabella WFA (dal processo di partenza o da un modello **).
 * Creato/copiato e inizializzato un corrispondente script in SCP_WFA.
 * Creato/copiato e inizializzato un membro nel file DOC_WFA.

A questo punto la creazione di un processo prevede i seguenti passi logici : 
 * Definizione delle proprietà generali del processo, verificando l'elemento di tabella WFA.
 * Definizione del flusso (costruzione della rete di Petri, transizioni e luoghi) tramite Workflow Designer.
 * Definizione delle responsabilità e del contenuto applicativo, arricchendo la transizioni (da Workflow Designer o direttamente da script).
 * (Opzionale) Documentazione del processo e dei suoi passi in DOC_WFA.


## Definizione delle proprietà del processo (tabella WFA)

Nella tabella WFA si definiscono le proprietà generali del processo, come ad esempio : 
 * Tipo di oggetti su cui è definito ed eventuale ridefinizione della gestione su tali oggetti (il workflow sostituisce la gestione).
 * Punto e modalità di creazione degli ordini relativi.

Per il dettaglio delle opzioni consultare l'help della tabella WFA, anche relativamente alla documentazione dei singoli campi : 
 :  : DEC T(ST) P() K(WFA)

## Modellazione della rete di Petri (script in SCP_WFA)

Nello script vengono descritti i singoli passi che compongono il processo, ovvero : 
 * Quali sono.
 * In che ordine vanno svolti.
 * Quali persone li possono svolgere.
 * Che operazioni comportano, che informazioni portano all'esecutore.

Lo script è un insieme di blocchi di istruzioni, ognuno rappresentante una transizione della rete di Petri, con questa struttura : 


 * TRA.
 ** DIC(PRC/...).FUN.
 ** FROM.
 *** LUO.
 ** TO.
 *** LUO.
 ** CST.EXT Tip...
 ** EXT.


### Definire le transizioni e i flussi
Quali operazioni vanno eseguite nel corso di un workflow.
Quali precedenze e relazioni di causalità esistono tra le transizioni, eventuali scelte automatiche o utente.
Queste informazioni vengono costruite graficamente tramite il componente Workflow Designer e scrivono le istruzioni TRA, FROM, TO e LUO.

### Definire le responsabilità
Quali utenti o gruppi di utenti possono eseguire una determinata transizione.
Quali utenti o gruppi di utenti sono eventualmente responsabili dell'assegnazione di una transizione a un utente.
Sempre dal Workflow Designer si seleziona con il tasto destro una transizione e si entra in modifica della sua parte di script (attributi dell'istruzione TRA).
Vedi capitolo specifico "Definizione delle responsabilità".

### Aggiungere il contenuto applicativo

Tre dimensioni rilevanti : 


 * Azioni accessorie (azioni esterne) :  Chiavi di menù e informazioni utili all'esecuzione di un'attività da presentare contestualmente.
Dal Workflow Designer in modifica di script della transizione :  istruzioni EXT e relative sottoistruzioni.
 * Integrazione con Sme.up all'avanzamento (azioni di dichiarazione) :  Creazione / modifica controllata di oggetti Sme.up, controlli particolari da parte del motore di workflow ecc ecc...
Dal Workflow Designer in modifica di script della transizione :  sostituire le chiamate implicite alle funzioni standard di avanzamento con particolari programmi (azioni) di integrazione (DIC.FUN).
 * Automazione (conseguenze esterne) :  Esecuzione in maniera automatica da parte del motore di workflow di determinate attività in certi punti del processo.
Dal Workflow Designer in modifica di script della transizione :  istruzioni CSG.EXT, conseguenze esterne da eseguire durante gli avanzamenti del processo, e relative sottoistruzioni.


## Documentazione del processo

### Documentazione applicativa/operativa del processo e delle transizioni
Tutte le informazioni rilevanti alle varie attività raccolte in fase di analisi possono essere salvate in modo da essere presentate al momento opportuno a chi dovrà eseguire tali attività.
Questo si riflette nello scrivere un membro dal nome uguale al processo nel file DOC_WFA, in questo modo : 
 * sotto il tag TAG Id="WFA" si compilano le istruzioni relative al processo, presentate poi nella scheda dell'ordine di workflow.
 * sotto i tag  TAG Id="(codice transizione)" si scrivono le istruzioni delle transizioni, che vengono presentate nelle schede dei relativi impegni come guida per l'utente che deve eseguire un determinato compito.

### Documentazione tecnica

Un posto dove documentare dal punto di vista tecnico il processo (particolarità, programmi personali e personalizzati attinenti, tabelle e autorizzazioni correlate, ...) è in fondo allo script del processo stesso, sotto forma di documentazione attiva iniziante con il tag DOC.

# Tipi di programmi che interagiscono con il workflow

## Programmi di flusso

Servono a indirizzare il motore di workflow nella scelta dei flussi da percorrere; sono denominati con la convenzione WFFLU_nn (entry specifica).
Si dividono in : 
 * Programmi di requisiti esterni.
 * Programmi di requisiti sui luoghi
 * Programmi di conseguenze sui luoghi.

## Programmi di calcolo variabili
Consentono al motore di workflow di utilizzare variabili complesse a piacere per le proprie decisioni; sono denominati WFVAR_nn e vengono eseguiti come servizi ciechi (entry funizzata estesa £UIBDS).

## Azioni

Programmi funizzati WFAZxx_nn, xx è l'applicazione di competenza, nn è un progressivo.
Se personali si suggerisce di denominarli XWFyyy.
Possono servire a : 

- Indirizzare, in maniera automatica o meno, il flusso di workflow.
- Integrare il workflow con Sme.up.
- Automatizzare determinate attività.


Si dividono in : 
 * Programmi di dichiarazione :  ricevono in input l'impegno (F2), sulla base del risultato dell'elaborazione si occupano di chiamare la £WFC per istanziare un'attività (F4).
* Conseguenze esterne :  Vengono eseguiti come risultato dell'esecuzione di un'attività. Ricevono in input l'attività appena eseguita (F4)

Una serie di programmi standard sono già presenti in WFSRC; la documentazione delle loro funzionalità e chiamate è in testa al sorgente.
