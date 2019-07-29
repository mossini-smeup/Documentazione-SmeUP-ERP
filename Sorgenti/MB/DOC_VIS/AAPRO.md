 :  : TIT Produzione
# Generalità
La funzione "Produzione" sovrintende all'esecuzione degli ordini di produzione (proposti dalla funzione di pianificazione oppure immessi manualmente) al fine di ottenere la disponibilità dei prodotti finiti da spedire al cliente nelle quantità, qualità e alle date richieste, rispettando gli obiettivi di costo.
Essa costituisce quindi il "cuore" delle attività quotidiane svolte dalle aziende manifatturiere. Il processo di produzione può configurarsi come una trasformazione di materie prime oppure come un assemblaggio di componenti.

Le fasi di un processo di produzione possono essere sinteticamente riassunte nei seguenti punti : 
 * la generazione delle "task" di produzione e l'assegnazione alle differenti unità produttive (nota, una task di produzione generalmente si traduce in un ordine di produzione, vi sono però anche casi in cui la produzione viene gestita senza ricorrere agli ordini ma ci si basa sullo spostamento fisico dei materiali attraverso le varie fasi produttive, altri casi in cui il processo è talmente veloce che si utilizzano solo le dichiarazioni di versamento)
 * la definizione dei fabbisogni materiali (generalmente la distinta di produzione)
 * la definizione dei fabbisogni risorse e la loro sequenza di utilizzo (generalmente il ciclo di produzione)
 * l'approvvigionamento dei materiali nel luogo in cui verranno utilizzati, con la possibilità di introdurre regole di consumo (fifo, uniformità dei lotti, ecc..)
 * la schedulazione fine :  assegnazione delle attività da eseguire alle risorse (centri di lavoro, macchine) e la loro sequenziazione su ciascuna di esse.
 * il consumo di componenti e materia prime
 * le dichiarazioni consuntive di produzione (avanzamento attività, tempo speso, lavorazioni eseguite presso terzisti)
 * il versamento dei prodotti, con l'eventuale assegnazione di identificativi (lotto, matricola).
 * la consuntivazione degli ordini per evidenziare scostamenti (di efficienza ed efficacia rispetto agli standard)
 * le verifiche di qualità, eseguibili in vari punti del processo
Tutte queste attività sono supportate direttamente dall'applicazione di gestione della produzione, o da applicazioni ad essa correlate.
Per l'analisi "a breve" della disponibilità dei materiali in funzione della priorità assegnata alla produzione, si può utilizzare l'applicazione JMRP, il cui obiettivo è proprio quello di evidenziare eventuali "mancanti" e quali solleciti eseguire.
Le dichiarazioni di produzione possono essere raccolte sia attraverso le funzioni normali di input/output che con l'utilizzo di dispositivi di campo quali terminali radiofrequenza o dispositivi collegati ai PLC delle macchine.

# Ordini di produzione
L'ordine di produzione ha lo scopo di programmare ed eseguire la realizzazione di una certa quantità di un articolo, per una data. Tale realizzazione richiede un definito consumo di materiali e di risorse, per determinare questo fabbisogno di materiali o di risorse necessarie, è possibile usare il ciclo, la distinta standard oppure definire specifici indicatori legati all'ordine di produzione.

![AAP_PRO_01](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/AAP_PRO_01.png)
Oltre agli ordini di produzione di un articolo si possono definire : 
 * **ordini di rilavorazione**, impostando come componente lo stesso articolo che si vuole ottenere.
 * **ordini di trasformazione** :  si imposta, oltre all'articolo che si vuole ottenere, anche l'articolo di partenza, che si vuole trasformare :  il sistema costruirà una distinta "dinamica", che conterrà come impegni i componenti presenti solo nell'articolo di arrivo e, come recuperi, quelli presenti solo nell'articolo di partenza mentre i componenti comuni verranno trascurati
È possibile sia assegnare un ordine di produzione ad un ordine "master" (quest'ultimo a più livelli in modo che si possa costituire una struttura ad albero); sia non intestare un ordine di produzione ad un articolo specifico ma sfruttarlo come un insieme di attività da eseguire e di materiali da consumare (ad esempio per compiere una manutenzione). Vi sono funzioni specifiche per realizzare il prelievo ed il versamento a magazzino oltre alla possibilità di realizzare il prelievo in automatico (a backflush) all'atto del versamento o dell'avanzamento.

# Impegni materiali e risorse
Gli impegni materiali costituiscono l'insieme degli articoli, con le relative quantità, necessari per produrre un assieme. Essi possono essere intestati ad oggetti diversi come ad esempio :  righe di documento, richieste d'acquisto, ordini di produzione. La costruzione degli articoli avviene in automatico a partire dalla distinta (dell'assieme o del documento) nettificata dai movimenti (di versamento, prelievo) già eseguiti. Gli impegni di risorse sono il corrispondente, per quanto riguarda il consumo di risorse. Anch'essi possono essere intestati ad oggetti diversi (righe di documento, ordini di produzione, contenitori). La loro costruzione è, anch'essa automatica, a partire dal ciclo dell'assieme, nettificato dalle attività eseguite. La generazione degli impegni di risorsa, che definiscono di quante ore sono caricati i centri di lavoro e le singole macchine, genera anche gli impegni di risorse produttive secondarie, ossia il fabbisogno di stampi, attrezzisti, utensili , etc.

# Consuntivazione attività
La consuntivazione si basa sulla rilevazione delle attività svolte nell'azienda :  le quantità prodotte con i relativi tempi, le improduttività e le attività indirette. La dichiarazione delle attività può essere intestata ad una fase di un ordine di produzione, ad una riga di un ciclo di lavorazione, oppure può essere un'attività di tipo estemporaneo. È possibile eseguire la dichiarazione a partire dalla lista degli impegni risorse residui di un ordine di produzione oppure di una risorsa; inoltre vi è la possibilità di effettuare la dichiarazione per persona :  le sue ore di presenza si distribuiscono
sulle varie attività eseguite nel giorno.  Se la dichiarazione è a fronte di un ordine di produzione, è possibile, in automatico, eseguire i prelievi dei materiali necessari alla fase che si sta dichiarando (proporzionalmente alla quantità in avanzamento), e, se riguarda l'ultima fase del ciclo, è possibile eseguire il versamento dell'assieme e l'aggiornamento dell'ordine di produzione. E' consentita anche l'operazione di gruppo :  la dichiarazione di una fase, (definita come master) induce la dichiarazione automatica di altre fasi, precedenti o successive (definite come automatiche).

# Alcuni esempi : 
![P5_0001](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/P5_0001.png)![P5_0002](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/P5_0002.png)![P5_0003](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/P5_0003.png)
### Interfaccia col campo
Le dichiarazioni di attività possono essere anche raccolte direttamente da apparecchiature di campo, le informazioni  consuntive pervenute vengono registrate alla stessa stregua dei consuntivi manuali.  La stessa applicazione può essere utilizzata anche in senso inverso, come ad esempio per mandare alle macchine i part program delle lavorazioni previste dall'ordine di produzione.

### Produzione a disponibilità chiamata
La produzione a disponibilità chiamata (PDC) è una particolare modalità di gestione della produzione, di nostra concezione, che ha lo scopo di rappresentare il processo produttivo in modo più "fisico" rispetto agli ordini di produzione. Essa si basa sull'assunto che la movimentazione in produzione avvenga per contenitori, e sulla rappresentazione "logistica" del ciclo produttivo come un insieme di risorse (centri di lavoro o macchine), ciascuna delle quali con un'ubicazione a monte e a valle. Gli ordini pianificati dall'MRP si traducono in contenitori pianificati. All'atto dell'inizio delle attività, essi si tramutano in contenitori effettivi. Il loro spostamento da un'ubicazione all'altra, induce una dichiarazione di avanzamento automatica nel caso che queste siano a monte e a valle di una risorsa (l'informazione logistica contiene, implicitamente, quella produttiva). Lo spostamento all'ubicazione finale rappresenta il versamento a magazzino.In tal modo non si introduce un livello di informazione immateriale (l'ordine di produzione, con le rigidità che esso comporta), ma ci si limita a registrare tutto ciò che avviene in fabbrica :  si riempiono e si spostano i contenitori, li si dichiara bloccati in caso di verifica della qualità, si sposta del materiale da un contenitore all'altro, ecc.. Inoltre, dato che gli ordini rimangono sempre pianificati, vengono "tirati" i contenitori di volta in volta più urgenti (lo strumento trae il nome da questa peculiarità :  si "chiama" la disponibilità presente in fabbrica, sotto forma di contenitori nelle diverse ubicazioni, e quindi a diversi gradi di completamento del ciclo produttivo).
![P5_V002_02](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/P5_V002_02.png)
### Conto lavorazione
Quando la produzione viene eseguita all'esterno ad opera di terzisti siamo in presenza di un processo di conto lavorazione (passivo). Si può distinguere tra : 
 * conto lavoro pieno, quando la lavorazione viene eseguita interamente da un terzista In questo caso l'ordine di conto lavoro è equivalente ad un ordine di produzione interna (si ottiene un assieme da un insieme di componenti), in quanto elabora un livello di distinta base.
 * conto lavoro di fase quando un terzista esegue una sola operazione (fase) di quelle previste dal ciclo dell'ordine di produzione. Le altre possono venire eseguite internamente o presso altri terzisti.

La gestione dei documenti di conto lavoro è a carico dell'applicazione Trade.UP, che, per quanto riguarda impegni materiali, dichiarazioni di produzione, versamenti e avanzamenti (nel caso del conto lavoro di fase) è strettamente integrata con la gestione della produzione.

### Analisi mancanti
Quando si deve avviare una produzione (es. lanciare un ordine) una informazione fondamentale è la presenza di tutti i materiali necessari o la conoscenza del loro arrivo per quando saranno necessari a soddisfare l'ordine. Questa funzione è svolta dall'applicazione JMRP che, dato un insieme di ordini ed una priorità assegnata segnala i possibili mancanti ed indica le relative coperture eventualmente da sollecitare.  Questa applicazione non sostituisce la pianificazione materiali, ma è uno strumento operativo che permette di prevenire i problemi che si possono presentare nel breve periodo.

### Schedulazione fine a capacità finita
La schedulazione costituisce uno strumento interattivo e grafico, che fa parte nativamente del sistema gestionale, atto a risolvere i problemi di allocazione delle risorse e di sequenziazione delle attività, che si presentano quotidianamente nelle aziende produttive e di servizi.
Le principali caratteristiche dell'applicazione sono : 
 * schedulazione di impegni risorse di vari tipi
 ** ordini di produzione in corso
 ** ordini pianificati
 ** righe di ciclo esterno
 ** contenitori, in presenza di produzione snella.
 * definizione di più scenari di schedulazione, per eseguire simulazioni, e scegliere di rendere definitivo il più efficace.
 * suddivisione in ambiti di competenza schedulabili separatamente (FABBRICHE VIRTUALI).
 * ampia scelta di dispatching rules (oltre a quelle implementate, possibilità di definirne di specifiche, anche come combinazione di quelle esistenti)
 * modellazione della strategia (rispetto della consegna, saturazione delle risorse, comunanze tecnologiche o di attrezzaggio, eventualmente combinate e messe in competizione tra di loro)
 ** rappresentazione estesa del processo
 ** sovrapposizione tra fasi successive dello stesso ordine
 ** accostamenti sulla stessa risorsa di fasi successive dello stesso ordine
 ** tempi d attrezzaggio parametrici (dipendenti dalla situazione esistente e da quella futura)
 ** appuntamenti statici tra ordini (rispetto di vincoli di priorità definiti esternamente) e vincoli esterni fissi (date al più presto)
 ** calendari ed efficienza definibili al massimo dettaglio
 ** definizione di risorse a capacità infinita trattate con tempo di attraversamento
 ** gestione dei batch (ordini eseguiti contemporaneamente, ad esempio stampi multiarticolo) trattati come un singolo ordine sia in fase di schedulazione, sia nell'operatività manuale.
 * integrazione completa con il sistema gestionale :  non solo assenza di duplicazione di dati e loro trasferimento, ma anche possibilità, dall'interno della schedulazione, di navigare verso tutti i dati e avendone l'autorizzazione, di operare modifiche, immediatamente recepite alla successiva rischedulazione, eseguita dall' interno di questa applicazione
 * calcolo dei principali indici di prestazioni (saturazione, earliness, tardiness, ecc,,) e loro storicizzazione
 * possibilità di modificare i risultati con azioni manuali
 ** di ordinamento della sequenza di schedulazione
 ** di forzatura delle risorse selezionate
 ** di congelamento della situazione
 * analisi dei materiali critici
 * analisi delle risorse secondarie critiche
 * possibilità di realizzazione di exit utente che permettono
 ** di modificare i dati di input e dei risultati
 ** di specializzare la strategia in 'spinta' (decidere dove eseguire la fase selezionata) e in 'tiro' (decidere quale fase eseguire subito dopo quella appena schedulata)
 ** di estendere le informazioni riportate nella presentazione dei risultati
 ** di realizzare forme di presentazioni 'ad hoc', integrate nella navigazione della presentazione dei risultati
La schedulazione si presenta in modalità grafica, con ampie possibilità di navigazione tra le varie rappresentazioni, e facilità di modifica manuale tramite metodologia "drag and drop".
Le principali visualizzazioni sono : 
 * Quadro sintesi di tutte le risorse caricate
 * Gantt del carico di una singola risorsa o di un gruppo di risorse omogenee
 * Rappresentazione dettagliata di una singola fase
 * Lista degli ordini con indici di criticità per ciascuno di essi
 * Gantt di un singolo ordine
 * Gantt delle code sulle risorse
 * Analisi dei materiali e delle coperture
 * Analisi delle risorse secondarie
 * Quadro degli indici della schedulazione in corso

![Fig_060](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/Fig_060.png)![Fig_065](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/Fig_065.png)![Fig_067](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/Fig_067.png)![Fig_072](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/Fig_072.png)![Fig_073](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/Fig_073.png)![S5_001B](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/S5_001B.png)![S5_001C](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/S5_001C.png)![S5_001D](http://localhost:3000/immagini/MBDOC_VIS-AAPRO/S5_001D.png)
# Applicazioni utilizzate
Le applicazioni Sme.UP a supporto della gestione della produzione interna sono : 
 * __Prod.UP__, per la gestione degli oggetti tipici della produzione interna (Ordini di produzione, Impegni materiali, Impegni risorse, ...)
 * __Fine.UP__, per la schedulazione fine a capacità finita degli ordini di produzione che insistono sulle risorse produttive
A queste applicazioni se ne aggiungono anche altre con funzione di supporto : 
 * __Brec.UP__, per la gestione degli anagrafici di base (Articoli, Distinte, Cicli, Risorse, Enti, ...)
 * __JMRP.UP__, per l'analisi mancanti in ordine di priorità
 * __Ware.UP__, per la gestione della movimentazione materiali (versamenti, consumi, trasferimenti interni)
 * __Trade.UP__, per la gestione del conto lavoro (ordini, invio in C/L, rientro da C/L, resi non lavorati)
 * __Q9000.UP__, per la gestione qualitativa dei lotti di produzione, dei cicli di collaudo e dei rilievi eseguiti
 * __Fiel.UP__, per l'integrazione dei dati di campo (gestione terminali R/F, raccolta dati attività di produzione da PLC di macchina, trasmissione part-program, interfaccia con bilance conta pezzi, ...)
