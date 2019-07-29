Lo standard Sme.Up fornisce alcuni cruscotti di produzione standard, parametrizzabilli attraverso una serie di configurazioni.

* **Cruscotto Lista di Macchine (UPP PH_038)** :  permette di definire un cruscotto di analisi di un insieme di macchine (che posso corrispondere ad un reparto o ad un qualsiasi altro raggruppamento di macchine si ritenga opportuno). Cliccando su un elemento della macchina presente nel cruscotto PH_038 si accede al dettaglio della singola macchina (PH_049).
* **Cruscotto Macchina(UPP PH_049)** :  permette di definire un cruscotto di analisi di una singola macchina. Questa SU richiama a sua volta una serie di ulteriori SU.
* **Azioni MES(PH_060)** :  permette di gestire la funzionalità di attrezzaggio/lavoro/fermo/stampa etichette di una macchina. Questi sono dei configuratori già preparati e personalizzabili tramite exit per le esecuzioni elementari richieste in una postazione MES.
* **Analisi/KPI MES(PH_048)** :  è la UPP che permette la configurazione e l'utilizzo di KPI richiamabili nei report/sinottici/cruscotti MES

Con il termine MES, Manufacturing Execution System, si intende un sistema informativo aziendale costituito da interfacce uomo/macchina, dispositivi di vario genere, sistemi di avanzamento della produzione al fine di rilevare dati e informazioni di fabbrica con l'obiettivo minimo di misurare in tempo reale le performance delle macchine e di intercettare nel più breve tempo possibile anomalie nell'area di produzione.
L'obiettivo principale che si pone un sistema MES è quello di ridurre il gap tra il mondo automation e il sistema gestionale.
Fanno parte di un macrosistema MES sia i collegamenti fisici con le macchine per rilevare pezzi prodotti / fermi macchina / temperature /pressioni e altre misure di processi produttivi, sia l'insieme di interfacce rese disponibili tramite tablet/computer fissi/pc industriali/televisori. Queste interfacce possono essere presenti sia nei terminali di ufficio (per il responsabile produttivo o il capo dell'azienda) sia installati direttamente in reparto in prossimità delle macchine. Tramite questi terminali vengono normalmente visualizzate una grande varietà diinformazioni ed eventi che man mano avvengono in produzione e la modalità con cui vengono presentati questi dati è tramite grafici, o semplici indicatori di performance, semafori di stato, gauge con percentuali di completamento. Su queste postazioni gli operai possono interagire in modo semplice con gli eventi che man mano avvengono al fine di causalizzare i fermi, dichiarare i cambi attrezzatura/cambi stampo, gestire i rilievi di un piano di collaudo, assegnare l'ordine in macchina scegliendolo dalla lista ordinata dallo schedulatore, scegliere il lotto di materia prima che verrà caricato in macchina, generare l' etichette dei colli di prodotto finito che man mano vengono prodotti, etc.

_2_ELENCO MACCHINE
Al terminale del capo reparto/responsabile invece viene dato l'accesso a più informazioni utili per analizzare l'insieme delle macchine di un reparto o andare in drill-down su specifici aree :  il pareto dei fermi, le performance delle macchine in un turno passato e altro.
Andremo ora a presentare le varie aree che SmeUp ERP propone come strandard del modulo MES.

_2_MONITOR MACCHINA (Multi operatore)
Nel monitor accessibile all'operatore vengono presentate una serie di macchine (parametrizzabili su postazioni) e con informazioni sintetiche : 
- Identificazione stato della macchina con colore :  attrezzaggio, ferma, in produzione
- Informazioni anagrafiche della macchina :  codice, descrizione
- Informazioni sull l'ordine di produzione e la Fase in corso :  numero, quantità prodotta, quantità residua, efficienza ordine di produzione
- Info legate allo stato in corso : 
-- Attrezzaggio :  operatore/i, tempo previsto, tempo consuntivo attuale
-- Lavorazione :  efficienza turno, efficienza turno precedente, efficienza target
-- Fermo :  causale fermo, descrizione causale, durata fermo attuale
Selezionando  un elemento della lista si entra in dettaglio nelle informazioni della singola macchina
In alto sono presentate dell voci di menù/azioni autorizzabili per la gestione di diverse sotto-aree : 
- Dashboard o area di produzione (Dati riassuntivi macchina Pezzi fatti/ordini in macchina/KPI)
-- Azioni per avanzamento dati produzione
-- Controlli qualità :  sottosezione attivabile con diverse modalità di gestione
-- Visualizzazione worklist prossimi ordini in macchina/sul CDL
-- Informazioni prodotto (disegni/documenti/video)
-- Informazioni ultimi eventi macchina con dati di dettaglio
-- Informazioni macchina (KPI) :  attivabile
-- Area statistica consumo colli/etichette sublotti
-- Informazioni macchina

_2_Dashboard o area di produzione
Nella dashboard sono identificabili due aree principali : 
Dati riassuntivi di macchina
Informazioni presenti  :  turno, macchina, descrizione macchina, stato macchina, ordine di produzione/fase, articolo, descrizione articolo, quantità prevista, quantità prodotta, quantità scarto, quantità residua, codice attrezzatura/stampo, numero impronte, pop up allarmi (controllo di qualità da eseguire,manutenzione programmata attrezzatura da eseguire)


_2_Azioni per avanzamento dati produzione
In questa seconda area sono presenti varie funzioni. Andremo ora a dettagliare le principali
* ATTREZZAGGIO/SMONTAGGIO  :  permettono di dichiare un tempo di setup scegliendo il prossimo ordine previsto dalla worklist
* STOP cliccando sull'azione di STOP fermo l'ordine, lo chiudo e lo saldo. N.B. Nel caso dello stop/sospensione è possible chiedere successivamente se fare un attrezzaggio di un altro ordine o un fermo gestionale in modo di semplificare l'operatività.
* FERMO  :  tramite il tasto di fermo posso imputare la causale specifica del fermo in corso. Se la macchina è ripartita la casualizzazione dei fermi avvenuti precedentemente la faccio tramite la voce specifica di gestione fermi del menù in alto del cruscotto. N.B. Fermi GESTIONALI :  è possibile imputare fermi di non attività non collegati a ordini specifici. Prima di dichiararli devo togliere l'eventuale ordine in corso. Esempi di fermi gestionali sono :  Mancanza ordine di produzione, Guasto macchina, Assemblee/scioperi
* SCARTI Con l'avanzamento (scarto) dichiaro le quantità scarto e non "disattrezzo l'ordine".
* BUONI Nel caso in cui voglia dichiarare i buoni e la macchina non mi restituisce i colpi faccio un versamento buoni manuale. Il versamento scarti viene normalmente gestita con indicazione della causale di movimentazione logistica degli scarti (sotto-causale). Gli scarti vanno a decurtare l'eventuale quantità di buoni
* DIC. COLLO (attribuzione della materia prima) Tramite questa funzione posso assegnare la materia prima al mio ordine. Il prelievo. Prima di accettare la dichiarazione di assegnazione della materia prima verificare che il lotto/collo sia in wip e blocco dell'attività in caso di assenza
* ETICHETTE (Stampa etichette logistica) E' possibile collegare qui tutte quelle funzioni di stampa ODL/etichette sublotti o in generale funzioni logische legate alla conclusione di una sotto dimensione della produzione in corso.
