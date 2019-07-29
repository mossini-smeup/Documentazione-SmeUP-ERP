 :  : TIT Logistica
# Generalità
La gestione e la movimentazione delle merci lungo tutta la filiera produttiva (dai fornitori alla consegna al cliente) è uno dei fattori critici di successo nella gestione di un'azienda manufatturiera o di distribuzione. Il controllo diretto dell'operatività porta ad un miglioramento del servizio, offrendo, in termini di efficacia : 
 * maggiore accuratezza delle operazioni, con riduzione degli errori
 * maggiore velocità e qualità di evasione
 * maggiore affidabilità e più tempestiva conoscenza delle giacenze
 * tracciabilità in ogni momento del livello di evasione degli ordini, con maggiore informazione per il cliente
 * migliore programmabilità dei tempi di lavorazione
 * migliore informazione a livello gestionale e commerciale.

![AAP_LOG_01](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_01.png)
Mentre in termini di efficienza,i vantaggi derivano dall'eliminazione o riduzione, da parte dei vari operatori, di iniziative personali e non coordinate, grazie al controllo integrato del processo; ottenendo così : 
 * riduzione di errori all'accettazione, nello stoccaggio, nel prelievo e nella spedizione, tramite anche la tracciabilità di  tutti i movimenti
 * riduzione delle conseguenze dovute a merce mancante
 * riduzione delle perdite di produzione per blocchi dovuti ad attività di inventario
 * ottimizzazione degli spazi e volumi delle varie aree di magazzino
 * riduzione delle scorte minime al livello strettamente necessario
 * riduzione dei percorsi e dei tempi di ricerca dei materiali, eliminazione dei tempi morti e dei viaggi a vuoto
 * maggiore produttività personale
 * riduzione dei danneggiamenti
 * maggiore precisione degli inventari
 * maggiore conoscenza dei cicli di vita dei prodotti, degli indici di rotazione, delle stagionalità, ecc., tramite statistiche dei movimenti ed elaborazioni esterne di tutte le informazioni disponibili.
La definizione di regole di funzionamento, configurabili in modo flessibile e facilmente personalizzabili, porta ad un miglioramento generale del processo logistico.

![AAP_LOG_02](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_02.png)
# Organizzazione logistica
Una caratteristica di Sme.UP è di non avere un ambiente logistico separato dal magazzino gestionale (es. gestione dei saldi giacenza a livello alto di gestionale e gestione delle ubicazioni e della movimentazione a livello di sistema dipartimentale). Sme.UP permette di spingersi fino al massimo dettaglio desiderato direttamente all'interno del magazzino gestionale, che in tal modo risulta essere l'unica informazione di giacenza a cui tutto il sistema accede.
Le giacenze di interesse per l'azienda possono essere : 
 * materiali di proprietà dell'azienda presenti in aree interne (magazzino componenti, magazzino prodotti finiti, area lavori incorso, ...)
 * materiali di proprietà dell'azienda in aree esterne (materiali in conto lavorazione, attrezzature in prestito d'uso, utensili in conto riparazione, ...)
 * materiali di proprietà di terzi presenti in azienda (componenti in consignment stock, strumenti in conto visione, contenitori in prestito d'uso, ...)

In Sme.UP la possibilità di gestire queste multiformi tipologie di giacenza è data da tre oggetti principali : 
 * Magazzino
 * Area di giacenza
 * Tipo giacenza

## Magazzino
Il termine Magazzino in Sme.UP è utilizzato come sinonimo di Plant, infatti a differenza dell'accezione comune, per noi il magazzino (plant) non è il luogo dove vengono gestite le scorte dei materiali ma rappresenta l'unità di pianificazione. L'unità di pianificazione è l'entità a fronte delle quale si svolge la pianificazione. Per spiegare il concetto di Unità di Pianificazione usiamo una esemplificazione : 
 * Tutti gli ordini cliente (domanda) e gli ordini di produzione (componenti) sottraggono materiali all'unità di pianificazione
 * Tutti gli ordini di produzione (prodotto) od acquisto apportano materiale all'unità di pianificazione
 * Le giacenze costituiscono il materiale presente nell'unità di pianificazione
 * I parametri di pianificazione (lottizzazione, lead times, politica di riordino, scorta minima, punto di riordino, ecc..) sono validi per un articolo in una unità di pianificazione.
Quindi se in una azienda abbiamo 2 unità di pianificazione, ad esempio un plant di produzione ed un plant di distribuzione un articolo potrà essere di produzione per il primo plant e di acquisto (acquisto intergruppo) per il secondo plant, e le politiche di pianificazione e la gestione MRP saranno logicamente separate per l'articolo che risiede in un plant e per lo stesso articolo che risiede nell'altro plant. Il magazzino è gestito nella tabella MAG ed il principale dato caratteristico è il magazzino fiscale di appartenenza :  in Sme.UP possiamo avere diversi magazzini (plant) dal punto di vista gestionale a fronte di un solo magazzino fiscale.

## Area di giacenza
I vari luoghi logici dove esiste del materiale sono chiamati aree, le aree possono essere : 
 * interne od esterne
 * il materiale può essere di proprietà dell'azienda o di terzi
 * dal punto di vista fiscale il materiale può essere o non essere rilevante
Facciamo degli esempi : 
 * un'area di un magazzino materie prime normalmente sarà : 
 ** interna
 ** di proprietà
 ** rilevante fiscalmente
 * un'area di conto lavoro passivo sarà : 
 ** esterna
 ** di proprietà dell'azienda
 ** rilevante fiscalmente
 * un'area per la gestione dei contenitori inviati dal cliente sarà : 
 ** interna
 ** di proprietà di terzi
 ** non rilevante fiscalmente
Sme.UP gestisce inoltre le aree di storno fiscale. Questo permette di gestire all'interno di aree di proprietà dell'azienda sia materiali propri che di terzi creando aree di storno dove totalizzare le giacenze dei materiali di terzi. Le aree di storno saranno portate in detrazione in sede di valorizzazione fiscale del magazzino. Esempi di aree di storno si hanno quando si vogliono gestire i materiali in consignment stock nell'area di magazzino materia prima comune, (deve essere alimentata anche un'area di storno solo con i materiali in consignment stock ). Un altro esempio si ha quando dei componenti forniti in conto lavoro attivo dal cliente si vogliono gestire nelle aree comuni di magazzino e produzione, anche in questo caso dovrà essere prevista un'area di storno.

## Tipo Giacenza
All'interno delle aree, la giacenza degli articoli può essere legata ad altre informazioni caratteristiche (es. ubicazioni di magazzino, commesse, fornitori, ubicazioni di produzione, ....), il tipo giacenza definisce i vari modi con cui viene caratterizzata la giacenza in un'area. Ad esempio potremmo avere : 
 * aree di magazzini chiusi, gestite per ubicazioni
 * aree di conto lavoro, gestite per fornitore
 * aree di spedizione clienti, gestite per cliente
 * aree di produzione, gestite per ubicazione di macchina
altre informazioni tipiche di una giacenza possono essere : 
 * lotto (per gestire la rintracciabilità)
 * contenitore (come informazione aggiuntiva o nella gestione movimentazione per unità di carico)
 * commessa (tipica nelle gestioni per commessa quando necessita identificare la giacenza dei materiali appartenenti ad una commessa)
Sme.UP permette di caratterizzare la giacenza utilizzando quattro elementi tipici dell'oggetto intestatario della giacenza stessa, ottenendo per esempio giacenze per : 
 * Articolo/Ubicazione /Lotto (per gestire al massimo livello di dettaglio le aree interne)
 * Articolo/Configurazione (se la configurazione differenzia gli oggetti)
 * Articolo/Commessa
 * Articolo/Fornitore o Cliente (per trattare le quantità in conto lavoro, deposito, visione
 * e, naturalmente, qualsiasi altra combinazione di questi oggetti.
È anche possibile aggiungere, per individuare la giacenza, il codice del contenitore.

![AAP_LOG_03](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_03.png)
## Integrazione
Un sistema logistico in un'azienda deve essere perfettamente integrato con il resto del sistema gestionale e deve potersi integrare con i sistemi di automazione e di campo eventualmente presenti.
Il sistema logistico di Sme.UP prevede integrazioni con : 
 * Gestione qualità, la logistica si integra con la gestione della qualità in accettazione (generazione dei lotti di collaudo) e la relativa movimentazione derivata dalle dichiarazioni degli esiti di collaudo (trasferimenti dall'area di accettazione verso l'area di magazzino o delle non conformità)
 * Pianificazione, i sistemi di pianificazione possono interrogare le situazioni di giacenza delle singole aree e con i gradi di dettaglio richiesti dalle specifiche funzioni di pianificazione (es. per una pianificazione strategica potrebbe bastare la giacenza per plant, mentre nella pianificazione per commessa è necessario il dettaglio della giacenza per commessa)
 * Contabilità, i documenti di entrata merci sono direttamente (senza duplicazione informazioni) utilizzati nel controllo fatture di acquisto, il prezzo effettivo calcolato in questa sede viene automaticamente riportato sui documenti. Le fatture di vendita vengono contabilizzate direttamente
 * Teminali radio frequenza, per la dichiarazione diretta di azioni di movimentazione, l'esecuzione dell'inventario fisico, la gestione delle missioni di versamento e prelievo
 * Dispositivi di campo quali bilance conta pezzi (nelle attività di ricevimento e spedizione), rulliere e sensori ottici (nelle attività di movimentazione interna e imballo).
 * Magazzini automatici

# Dettaglio funzionale
## Gestione della movimentazione
### Causali di movimentazione
Rappresentano lo strumento attraverso il quale vengono eseguite le variazioni delle quantità giacenti, ogni causale esegue un movimento di carico o scarico in una specifica area con un determinato tipo giacenza. Le causali sono classificate per tipo movimento (versamento produzione, da documento esterno, prelievo, rettifica, ...) e possono essere ulteriormente riclassificate secondo altri due elementi di raggruppamento. Le causali possono essere attivate manualmente (movimentazione manuale), oppure possono essere lanciate dalla esecuzione di attività su documenti interni ed esterni (versamenti, produzione, conto lavoro).

### Ubicazioni
Le ubicazioni sono utilizzate per gestire con un dettaglio più accurato le giacenze presso alcune aree interne. L'applicazione più comune è la gestione dettagliata del magazzino (materie prime o prodotti finiti), ma le ubicazioni possono essere anche utilizzate per descrivere in modo più puntuale la giacenza bordo macchina nelle aree di produzione o quella nelle aree di attesa spedizione. La codifica può avvenire in modo automatico (per coordinate) per costituire una mappa delle varie aree di magazzino (corsie, scaffali, ecc.). Le ubicazioni si differenziano poi per tipologia (monoarticolo, per prodotti di caratteristiche particolari, ecc.), che contribuisce alla scelta dell'ubicazione in fase di stoccaggio. Una menzione a parte meritano le "ubicazioni di linea", infatti possiamo definire uno o più tipi ubicazione aventi come oggetto di appartenenza una risorsa, in questo modo possiamo definire una logistica anche all'interno dei reparti produttivi ed introdurre modalità di gestione quali l'alimentazione kanban.

 ### Richieste di movimentazione
La richiesta di movimentazione è l'elemento su cui si basa l'intera logistica interna di Sme.UP. Essa rappresenta l'intenzione di movimentare un articolo (all'interno dell'azienda, oppure da o verso l'esterno), specificando l'origine e la destinazione, oppure, fissando una delle due, far scegliere l'altra al sistema, tramite regole parametriche. Un esempio verrà dato nel paragrafo seguente, relativo alle attività di spedizione. L'esecuzione della richiesta di movimentazione darà luogo alle effettive transazioni di magazzino.

### Attività di ricevimento merci
Il materiale ricevuto può transitare in un'area di accettazione, per poi essere trasferito alla destinazione finale. In presenza di aree gestite ad ubicazioni si possono utilizzare le richieste di movimentazione per far suggerire al sistema l'ubicazione più opportuna tenendo conto di una molteplicità di fattori quali : 
 * Peso
 * Volume
 * ABC picking stagionale o no
 * Pericolosità (infiammabilità, tossicità,...)
 * Presenza di mancanti
 * Valore e rischio di furto
 * Analisi portafoglio ordini nel breve periodo
 * ...

Collegata al ricevimento è la creazione del lotto o l'acquisizione della matricola che accompagnerà sempre il materiale permettendone così la tracciabilità. Normalmente si introduce l'area di accettazione quando vogliamo integrare il ricevimento merci con il sistema di gestione della qualità (Q9000), in questi casi alla generazione del lotto si può decidere se accettare l'entrata in free-pass oppure se controllare, e con quali piani di campionamento, i materiali in ingresso. L'esito del collaudo può attivare automaticamente la movimentazione dall'area di accettazione verso l'area di magazzino oppure verso l'area dei non conformi o quella degli scarti.

![AAP_LOG_04](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_04.png)
### Interrogazione giacenze
Come abbiamo visto in precedenza (Organizzazione logistica) la giacenza di un articolo può arrivare ad un grado di dettaglio notevole, di conseguenza serve uno strumento potente di interrogazione che permetta l'analisi delle giacenze secondo le viste più svariate (es. per articolo, per cliente, per ubicazione/lotto, ecc...). Lo strumento di interrogazione giacenze permette di definire "forme di presentazione" a piacere, tagliate sulle esigenze dell'utente, da utilizzare in sede di interrogazione giacenze.

### Movimentazione interna
La movimentazione interna di magazzino ha lo scopo di trasferire gli articoli da un luogo all'altro e di eseguire i prelievi ed i versamenti da e verso il magazzino. Tutte queste attività possono essere eseguite tramite richieste di movimentazione, che suggeriscono la scelta dell'origine e/o della destinazione del materiale.
Ad esempio :  nei trasferimenti interni esse sono d'ausilio : 
 * nella ricompattazione di un'area gestita ad ubicazioni
 * nell'assegnazione dell'ubicazione di stoccaggio quando si passa dall'area di collaudo al magazzino componenti
 * nella scelta dell'ubicazione di prelievo uscendo dal magazzino chiuso verso un'area di wip o di spedizione.
Nei prelievi di produzione si possono impostare regole di consumo FiFo (dal lotto più vecchio), così come nei versamenti sono gestibili regole di stoccaggio in aree diverse, in funzione delle caratteristiche dell'articolo (infiammabile, deperibile, ecc.). L'operazione di assegnazione delle richieste viene eseguita da un motore inferenziale, che esegue un set di regole fino al raggiungimento dell'assegnazione dell'intera quantità della richiesta. La flessibilità del metodo è data dal fatto che uno degli effetti dell'applicazione di una regola è la scelta della regola successiva, creando un percorso di assegnazione flessibile.C'è comunque la possibilità di eseguire prelievi, versamenti e trasferimenti, in modo diretto, qualora non si
desideri implementare una logistica avanzata.

### Movimentazione esterna
La movimentazione esterna avviene nelle aree esterne al perimetro aziendale (tipicamente aree di conto lavoro o aree di magazzini esterni) o nelle aree di confine (ricevimento e spedizione). Questi movimenti sono generalmente associati ai documenti del ciclo esterno e vengono lanciati eseguendo le attività di "collegamento" di tali documenti. Il dettaglio del movimento da eseguire viene governato dalle causali di movimentazione associate al documento.

### Attività di spedizione
La spedizione è un particolare flusso di documenti, nel quale un ordine di vendita si trasforma in un documento di uscita. L'attività di spedizione può essere guidata dalle richieste di movimentazione :  si stabilisce innanzitutto che cosa spedire (eventualmente in modo automatico tramite un'analisi dell'evadibilità) :  ciò genera una richiesta di movimentazione, in cui si fissa, ad esempio, che il materiale dovrà partire da un'area di spedizione. Se l'area dei prodotti finiti è gestita ad ubicazioni, le richieste di movimentazione, che conterranno le ubicazioni di prelievo, scelte con logiche parametriche, costituiranno il documento di picking. L'esecuzione della richiesta avrà l'effetto di registrare il trasferimento del materiale all'area di spedizione. All'atto della spedizione verrà prodotto il documento di spedizione che chiuderà la richiesta di  movimentazione. Nel flusso si possono inserire particolarità quali la stampa del documento di spedizione e di eventuali ulteriori documenti accompagnatori, l'aggiunta di righe non previste. È possibile inoltre definire i colli in cui si suddivide la spedizione, e comporre il relativo packing list. Più documenti di spedizione possono essere raccolti in un viaggio, qualora essi abbiano, anche in parte, un percorso comune. L'oggetto viaggio è la base per l'organizzazione delle spedizioni, sia a livello fisico (controllo del peso e/o del volume), sia a livello temporale (quando e che cosa spedire).

### Contenitori
La movimentazione può essere eseguita facendo riferimento ad unità fisiche (contenitori, colli, pallet), dette Unità di Movimentazione (UdM). In questo caso tutto il contenuto viene mosso. Sono previste anche attività di riempimento (con eventuale produzione del documento di identificazione), svuotamento, suddivisione e accorpamento. E' possibile assegnare ad ogni articolo il tipo di contenitore nel quale è previsto che venga mosso. In associazione con l'utilizzo di tecniche quali la radiofrequenza la movimentazione per UdM permette di raggiungere elevati standard di efficacia/efficienza in quanto possiamo associare ad un singolo codice (l'identificativo dell'UdM) tutta una serie di informazioni quali Articolo, Quantità, Lotto, Configurazione, Ubicazione fisica, ecc ... L'impiego delle UdM semplifica notevolmente anche le attività collegate all'inventario fisico.

![AAP_LOG_05](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_05.png)
## Gestione dei dati di giacenza
### Rintracciabilità lotti
All'atto del ricevimento di un articolo d'acquisto (o di conto lavorazione) o al versamento dell'ordine di produzione, è possibile registrare un nuovo lotto. Il lotto, oltre a scopi di controllo qualità, può risultare utile come base per l'analisi di tracciabilità. I prelievi di produzione dovranno essere intestati al lotto utilizzato, come pure per i versamenti dovremo registrare il lotto. In tal modo, tramite i movimenti di magazzino, si formeranno dei legami in base ai quali sarà possibile rispondere alle domande : 
 * quali lotti di un componente d'acquisto sono entrati in un lotto di prodotto finito?
 * un lotto di acquisto in quali lotti di assiemi superiori (a tutti i livelli) è entrato?
Va tenuto presente che per realizzare la tracciabilità completa è necessario, per i codici dei quali si intende percorrere la tracciabilità, dichiarare sempre il lotto, in modo da non interrompere la catena di informazioni.

## Inventario fisico
Per lo svolgimento di questa attività, si deve innanzitutto inserire il codice inventario, nel quale si definiscono le informazioni necessarie alla procedura di conta :  le modalità di estrazione (dalla giacenza attuale, ad una data impostata), il tipo costo per le valorizzazioni, le modalità di applicazione degli scostamenti. Ogni funzione richiede il codice dell'inventario. In tal modo è possibile tenere traccia degli inventari completati e programmare le risorse dedicate alla realizzazione di quelli in corso. Sono previste due modalità di registrazione dell'inventario : 
 * su lista di conta. La giacenza contata viene registrata direttamente sull'inventario estratto.
 * su cartellini distribuiti agli utenti. Si produce un archivio di cartellini, eventualmente raggruppati in lotti di conta. Essi vengono stampati, compilati, raccolti ed inseriti nel sistema con i dati identificativi (articolo, lotto, area, tipo giacenza, ubicazione, ecc.) e la quantità trovata. Con un passo successivo da essi si aggiorna l'inventario.
L'inventario, dopo essere stato compilato, può essere stampato o visualizzato, in varie modalità e sintesi, eventualmente valorizzando gli scostamenti, ed infine concluso con l'esecuzione automatica delle rettifiche inventariali.

![AAP_LOG_06](http://localhost:3000/immagini/MBDOC_VIS-AALOG/AAP_LOG_06.png)
## Fotografia di giacenza
E' una funzione che permette di memorizzare la situazione delle giacenze ad una qualsiasi data. Una fotografia può essere ottenuta a partire dalla giacenza attuale o dal magazzino fiscale, è' inoltre possibile ottenere fotografie incrementali come differenza di situazioni tra foto a due diverse date.La fotografia così ottenuta può essere visualizzata o stampata,
eventualmente riaggregata a livelli superiori e valorizzata secondo un tipo di costo selezionato.

# Magazzino fiscale
Questo modulo offre uno strumento per valorizzare le rimanenze di magazzino. È possibile definire più scenari, per simulare diverse modalità di valorizzazione. È inoltre data la facoltà di escludere alcune aree dalla valorizzazione, definendole non fiscali (materiale di terzi in azienda, scarti, ecc.).

# Applicazioni utilizzate
Le applicazioni Sme.UP a supporto della gestione logistica sono : 
 * **Ware.UP**, per la gestione delle giacenze, della movimentazione e di tutte le funzioni (gestionali e fiscali) correlate
 * **Trade.UP**, per la gestione dei documenti del ciclo esterno e delle attività di ricevimento e spedizione, oltre che alla organizzazione dei viaggi
A queste applicazioni se ne aggiungono anche altre con funzione di supporto : 
 * **Brec.UP**, per la gestione degli anagrafici di base (Articoli, Distinte, Cicli, Risorse, Enti, ...)
 * **Fiel.UP**, per l'integrazione dei dati di campo (gestione terminali R/F, raccolta dati attività di produzione da PLC di macchina, trasmissione part-program, interfaccia con bilance conta pezzi, ...)

### Alcuni esempi

![GMANIN_01](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GMANIN_01.png)
![GM_02_02](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GM_02_02.png)
![GMRN02_04](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GMRN02_04.png)
![GMUBIC_02](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GMUBIC_02.png)
![GMANIN_03](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GMANIN_03.png)
![GMMOVI_11](http://localhost:3000/immagini/MBDOC_VIS-AALOG/GMMOVI_11.png)