# Obiettivo dell' applicazione

Il modulo A£LING si occupa delle tematiche relative alla localizzazione di Sme.UP in lingue diverse dall'italiano : 
 * Traduzione di Sme.UP;
 * Traduzione della documentazione di Sme.UP;
 * Gestione dei caratteri speciali, presenti in diverse lingue;
 * Impostazione di ambienti multilingua ed esecuzione di Sme.UP in lingua.

# La traduzione :  concetti generali

La traduzione di Sme.UP avviene attraverso due file, origine e destinazione.
 * Il file origine contiene tutte le frasi in italiano di Sme.UP, estratte dai diversi oggetti che lo compongono (programmi, video, schede...).
 * Il file destinazione contiene, per ogni lingua, tutte le frasi da tradurre/tradotte. È il file che viene utilizzato per preparare/eseguire un ambiente in lingua.

Schematicamente il processo di traduzione è : 
 * Estrazione delle frasi in italiano sul file origine (un processo continuo che mira ad avere il file origine sempre aggiornato con tutte le frasi di Sme.UP);
 * Preparazione del file di destinazione, riportando le frasi da tradurre per ogni lingua;
 * Traduzione del file destinazione, per ogni lingua;
 * Utilizzo del file di destinazione (tradotto) per compilare in lingua gli oggetti che necessitano di ricompilazione (es. video, printer file, message file);
 * Utilizzo del file di destinazione (tradotto) a runtime, per tradurre dinamicamente oggetti che non necessitano di ricompilazione (es. testo in schiera nei programmi).

Le modalità di estrazione verso il file origine vengono impostate una sola volta per installazione, dopo di che il processo può essere automatico (ad esempio schedulato di notte). Anche l'estrazione da file origine a file destinazione può essere schedulata in automatico.

La traduzione delle frasi estratte in una determinata lingua può essere fatta direttamente sul file destinazione, tramite schede di gestione minimale messe a disposizione nel modulo A£LING.

NB :  è solo il file di destinazione che viene utilizzato nell'esecuzione di uno Sme.UP in lingua, il file origine esaurisce il suo compito una volta estratte le frasi da tradurre!

## Il contesto :  come tradurre in maniere differenti lo stesso termine

Un termine in italiano può dovere essere tradotto in maniere differenti, perchè può significare cose diverse in diversi contesti.
L'esempio classico è il termine "stato", traducibile in inglese con "country" (nazione) oppure "status" (stato di un oggetto).
Perchè ciò sia possibile, sia nel file origine che in quello di destinazione le frasi sono associate a un contesto, ovvero il posto dove vengono utilizzate (oggetto di Sme.UP). Quindi, per restare nell'esempio, "stato" viene estratto n volte per ogni suo utilizzo (programma1, programma2, ...), sia nel file origine che in quello destinazione, in modo da poter avere diverse traduzioni.
In linea di massima ogni frase/termine utilizzato in ogni punto di Sme.UP ha i suoi record specifici nei file origine/destinazione, in modo da potere essere gestito in maniera autonoma. Ci sono delle limitazioni, per le quali si rimanda alla documentazione specifica.

## L'ambito :  come distinguere tra le traduzioni standard e quelle personalizzate

Un secondo tema importante, ai fini della traduzione di Sme.UP, è come distinguere tra traduzioni standard (fornite da Sme.UP) e personalizzate (effettuate dal cliente).
Questo per due motivi : 
 * Individuare a chi compete la traduzione (Sme.UP vs cliente);
 * Determinare una priorità in presenza di traduzioni contrastanti.

Viene così introdotto il concetto di ambito, con diverse analogie con quello di libreria di programmi standard/personali : 
 * Ambito 00 :  Standard (assimilabile a programmi in SMEDEV+SMESRC);
 * Ambiti >=10 :  Personali (assimilabile a programmi in SME_PER).

L'ambito caratterizza le frasi sia nel file origine che in quello di destinazione. Come per le librerie : 
 * L'ambito standard viene mantenuto da Sme.UP, e si aggiorna in fase di rilascio;
 * L'ambito standard viene posto "più in basso" rispetto a quelli personali, quindi in presenza di traduzioni diverse tra standard e personali "vincono" quelle personali.

Si configurano tre casistiche : 
 * Frasi di ambito standard :  estratte da oggetti standard, traduzione a carico di Sme.UP e aggiornate al rilascio.
 * Frasi di ambito personale :  estratte da oggetti personali/personalizzati, traduzione a carico del cliente e non toccate al rilascio.
 * Frasi di ambito standard, a traduzione personalizzata :  estratte da oggetti standard (quindi con traduzione standard) copiate solo nel file delle traduzioni su ambito >=10 per personalizzarne la traduzione per una o più lingue. Questo consente di personalizzare la traduzione senza dovere necessariamente personalizzare l'oggetto. Al rilascio gli oggetti standard possono essere cambiati, mentre le traduzioni personalizzate non vengono toccate :  eventuali "buchi" (frasi introdotte nella versione aggiornata del programma) prendono la traduzione standard, le frasi già esistenti mantengono la traduzione personalizzata.
In un'installazione "semplice" l'ambito di personalizzazione è 10. La possibilità di avere più ambiti personalizzati è data per gestire installazioni complesse (multiazienda) :  si veda la documentazione specifica per gli installatori.

# Processo di traduzione
Per poter utilizzare correttamente un ambiente in lingua è necessario innanzitto effettuare una corretta installazione. Questo consente di predisporre gli ambienti sia per la gestione delle traduzioni che per l'utilizzo in ingua.

Una volta effettuata l'installazione, è necessario eseguire quelli che sono i 4 passi fondamentali : ua.
 * Estrazione delle frasi italiane da tradurre
 * Preparazione dell'archivio delle frasi da tradurre nelle diverse lingue
 * Traduzione
 * Generazione degli oggetti in lingua, ove necessario
