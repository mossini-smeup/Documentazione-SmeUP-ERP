 :  : TIT Sme.UP - Visione applicativa
# ERP effettivo Generalità
Le definizioni di ERP (Enterprise Resources Planning) per una soluzione gestionale sono le più disparate e spesso in disaccordo tra loro.Secondo la nostra visione, questa tipologia di software deve tassativamente avere alcune categorie di requisiti : 
 * una copertura applicativa tale da supportare i principali processi aziendali attraverso una piena e libera navigabilità tra le differenti informazioni
 * la capacità di soddisfare, attraverso interventi parametrici, le più varie esigenze funzionali delle aziende di produzione, di distribuzione e di servizi
 * la flessibilità e la modellabilità necessari per seguire l'impresa lungo le evoluzioni organizzative che necessariamente avvengono nel tempo
 * un insieme di caratteristiche generali che ne permettano l'installazione in diverse nazioni
 * la disponibilità di strumenti decisionali integrati, che aiutino Titolari e Manager nel momento di prendere una decisione.
In questo documento viene esposto il modo in cui Sme.up offre la sua risposta a questi requisiti.

# Caratteristiche Generali
# Interfaccia utente
Iniziamo da questo aspetto che non è affatto estetico o commerciale, come appare in prima battuta. Le soluzioni ERP hanno come punto di forza l'abbondanza di dati analitici e di funzionalità. Ma questa stessa caratteristica si rivela un elemento addirittura critico, in particolare per Titolari e Manager :  non è facile accedere direttamente ad informazioni chiave, indispensabili per decidere.
Per "capire" la situazione reale di un cliente, tanto per fare un esempio, può essere necessario passare dal fido ai pagamenti ed agli insoluti, dagli ordini alla redditività e così via. Troppi passaggi che fanno perdere il filo e minacciano la bontà della valutazione d'assieme. È indispensabile uno strumento capace di portare l'informazione giusta al posto giusto nel momento giusto.
Nei sistemi tradizionali le informazioni sono accessibili attraversi metodi di ricerca gerarchica, ad esempio da una fattura di vendita, si può accedere alla testata della bolla che l'ha generata e da questa al cliente a cui è riferita, seguendo un altro ramo si attraversa il dettaglio per arrivare all'articolo ed alle informazioni commerciali e di magazzino collegate.

![AAP_VAP_01](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_01.png)
Sme.up, grazie alla sua struttura ad oggetti applicativi ed alle possibilità fornite dall'interfaccia grafica permette una migliore navigazione attraverso i dati passando dalle informazioni caratteristiche di un oggetto a quelle di un altro qualsiasi oggetto ad esso collegato e così via utilizzando un sistema di navigazione reticolare.

![AAP_VAP_02](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_02.png)
L'interfaccia grafica (Looc.up), a cui rimandiamo per i dettagli, è semplice da utilizzare ma estremamente potente e comprende le più significative funzionalità tipiche dei fogli Excel e degli strumenti di Business Intelligence.

# Integrabilità con applicazioni esistenti
Sostituire un ERP ricostruendo pazientemente sul nuovo applicativo le peculiarità del precedente è un'operazione lunga, complessa e costosa. Non sempre l'azienda ha tutte le capacità di analisi adeguate per indirizzare opportunamente il fornitore di software o la disponibilità di personale esperto e qualificato a sufficienza per guidare un'evoluzione che coinvolga tutte le aree e tutte le funzioni. Inoltre l'impatto sull'azienda del cambiamento del sistema informatico nella sua totalità arreca un notevole disturbo aziendale.

![AAP_VAP_03](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_03.png)
È molto meglio operare con gradualità, focalizzando l'attenzione su problematiche specifiche.

Uno dei punti di forza di Sme.up deriva dalla sua struttura rigorosamente ad oggetti attraverso la quale ogni modulo (anzi :  ogni singola funzionalità) può ricevere informazioni, senza duplicazioni di dati, da altri applicativi e quindi costituire un sistema informativo "ibrido".
**Nota bene**; Sme.up può leggere in modo nativo le informazioni presenti negli altri gestionali e quindi opera egregiamente come "client", mentre per quanto riguarda l'utilizzo da parte degli altri gestionali dei dati elaborati internamente a Sme.UP, questo dipende dalla capacità del gestionale in questione, nel caso sia assente bisogna sviluppare degli opportuni programmi di scrittura.

Risulta sempre conveniente potenziare l'esistente piuttosto che sostituirlo, qualora esso risulti in alcune sue parti ancora adeguato alle esigenze aziendali. È possibile, ad esempio, installare solo la pianificazione materiali di Sme.up, che riceve le informazioni di disponibilità dagli applicativi esistenti (giacenze, ordini e impegni in corso) ed applica i propri suggerimenti (con scrittura di nuovi ordini) verso di essi. I parametri che guidano la pianificazione (lotti, tempi, politiche) vengono guidati da Sme.up, anche se fanno riferimento ai dati degli articoli esistenti in un data base differente.

Questo modo di procedere che noi chiamiamo "Rilascio per processi" limita fortemente l'impatto sull'intero sistema azienda e fa di una apparente debolezza (il tempo totale di implementazione) un punto di forza in quanto consente a tutte le persone dell'azienda coinvolte nell'implementazione una migliore comprensione delle logiche e della filosofia di Sme.up in modo di collaborare con gli installatori ed i customizzatori ad una riuscita ottimale del progetto.

![AAP_VAP_04](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_04.png)
Come confermano le installazioni in numerosi paesi europei, Sme.up è predisposto per una completa internazionalizzazione attraverso una serie di caratteristiche tra le quali : 
 * **Traduzione** :  il prodotto è già disponibile in una decina di lingue diverse :  la traduzione viene guidata attraverso opportune tabelle, nessuna parte del codice viene duplicata; tecnicamente, le parole e le frasi sono state trasformate in 'oggetti' e beneficiano quindi dei numerosi vantaggi di questi
 * **Lingua** :  ogni singolo utente può scegliere la lingua attraverso la quale interagire con il sistema
 * **Date** :  scelta del formato di presentazione della data :  giorno/mese/anno oppure  mese/giorno/anno, senza che differisca il formato interno di memorizzazione
 * **Numeri** :  si può scegliere, nell'editazione dei numeri, tra il formato italiano (punti separatori di migliaia e virgola per i decimali) ed il formato anglosassone (l'opposto del precedente).
In aggiunta, sono state già realizzate alcune localizzazioni in linea con le disposizioni fiscali di singoli paesi.

# Multiaziendalità
La multiaziendalità è trattata diversamente in ambito contabile ed in ambito gestionale. Nell'ambito contabile è implementato un sistema intrinsecamente multiaziendale :  ogni oggetto contiene, tra i suoi attributi, l'azienda a cui appartiene. All'ingresso dell'applicazione si imposta l'azienda su cui si opera, che si può sempre modificare rimanendo nella funzione in cui ci si trova. È possibile definire impostazioni tabellari comuni a più aziende. Le consultazioni legate al mondo delle rate (scadenzari, partitari, ecc.) possono esporre anche i dati di tutte le aziende. Sono presenti inoltre analisi di bilancio ottenute come confronti tra più aziende.
Nell'ambito gestionale, invece, la multiaziendalità è intesa come condivisione di oggetti comuni a più aziende, anziché l'attribuzione del codice dell'azienda ad ogni record dei vari archivi. Ciò è possibile perché ogni archivio (in cui risiedono gli oggetti) contiene informazioni omogenee, e indipendenti da quelle di altri archivi (a meno che vi siano legami naturali, come tra le giacenze ed i movimenti di magazzino). In questo modo si può costituire una struttura articolata di librerie (anche a più livelli), che permette di condividere alcuni archivi, mentre altri sono specifici di una sola azienda.

Un esempio è costituito dall'anagrafica articoli e dalla distinta base : 

Comunemente il livello minimo (informazione della massima profondità in cui un articolo è presente in distinta base) viene riportato nell'anagrafica articoli, con l'inconveniente di legare indissolubilmente questi due archivi;

In Sme.up invece, l'anagrafica articoli riporta solo caratteristiche descrittive; è presente inoltre un archivio specifico dove sono contenute le informazioni dell'articolo dipendenti dalla distinta base (il livello minimo, il numero di assiemi e componenti, ecc.). In questo modo è possibile avere un'anagrafica articoli comune a più aziende, ed una distinta base specifica per ogni azienda :  se l'intero processo produttivo è realizzato, verticalmente, in più aziende, si suddivide la distinta nella parte di competenza di ognuna di esse.

Le informazioni di pianificazione, a loro volta sono contenute in un altro archivio, specifico di ogni azienda :  quindi, un articolo che per una di esse è un componente d'acquisto, diventa, per quella che la rifornisce, un prodotto finito.

Infine le tabelle, che costituiscono la base di parametrizzazione di tutto il sistema, possono singolarmente essere condivise o meno da più aziende. In tal modo è possibile unificare comportamenti generali (ad esempio le unità di misura o i tipi distinta), e differenziare le specificità (ad esempio le aree di magazzino).

# Strumenti per la comprensione
La complessità dei sistemi ERP rende la loro documentazione un fattore vitale per la corretta installazione ed un proficuo utilizzo. D'altra parte, la vastità dei comportamenti possibili e la diversificazione delle figure professionali che interagiscono con il sistema, rende impossibile, e forse nemmeno proficua, la realizzazione del 'Libro' che contiene tutte le risposte.
Il nostro sforzo è stato quello di realizzare strumenti diversificati che facilitino la comprensione del prodotto nella sua struttura, nella sua parametrizzazione e nel suo utilizzo.

**Help**
 * __Di tabella__ :  nelle tabelle ogni campo è provvisto di un help contestuale. Dato che le tabelle costituiscono i mattoni elementari della parametrizzazione del sistema, particolare cura è stata posta nella completezza ed accuratezza di questa documentazione.
 * __Di programma__ :  è presente nei programmi che eseguono funzioni particolarmente importanti. È possibile, da parte dell'utente, integrare questi help, oltre a realizzare help specifici per programmi che ne sono privi.

**Books**
Sme.up mette a disposizione testi che descrivono, in generale, le finalità e la struttura di ogni applicazione ("documenti di visione"). In aggiunta, vi sono testi ("soluzioni particolari") che affrontano in profondità argomenti specifici (ad esempio le alternative di ciclo, la gestione del multiplant, l'ATP, ecc..).

**Documentazione attiva**
Ogni modulo è corredato da un documento di guida all'installazione con caratteristiche ipertestuali, che permettono di passare alla manutenzione di quanto viene descritto nel testo. Ad esempio, dal documento che descrive le linee di ammortamento dei cespiti, si può accedere alla manutenzione della tabella delle linee, e quindi tornare al testo. All'interno dei documenti di questo tipo è inoltre possibile realizzare controlli che evidenziano, nel testo, anomalie ed incompletezze dell'impianto.

**Modelli dinamici**
Ogni implementazione realizza un "impianto" costituito dall'insieme della customizzazione delle tabelle e della struttura dati e programmi che è specifico. Abbiamo realizzato una rappresentazione visiva (liberamente navigabile) di questo impianto, che abbiamo definito 'modello', in quanto è una rappresentazione dell'implementazione, e 'dinamico' in quanto variabile in modo automatico al modificarsi della struttura. Ad esempio, partendo dai modelli testata di un ordine di ciclo esterno, si può passare alle tipologie di riga ammesse per ogni modello testata, e da queste ultime alle corrispondenti causali del movimento di magazzino, per poi accedere alle aree giacenza che esse movimentano.

**Set & Play**
Per i processi di una certa complessità si è ritenuto utile realizzare delle funzioni di simulazione che, impostando liberamente l'input e inserendo i parametri opportuni, eseguono la funzione interessata e ne presentano il risultato. Un esempio è la simulazione dell'MRP :  inserendo manualmente i fabbisogni e le coperture (oppure importandoli dall'ambiente di lavoro) e impostando i parametri relativi (politiche, tempi di approvvigionamento, lotti), se ne vedono immediatamente i risultati della pianificazione.
Un altro esempio è, nella gestione cespiti, la visualizzazione dell'andamento dell'ammortamento negli anni al variare delle impostazioni del piano e della linea.

**API**
In Sme.up vi è un cospicuo numero (oltre 300) di funzioni elementari (API) richiamate all'interno dei programmi. Per documentare il loro comportamento, facilitandone la conoscenza e l'utilizzo, sono state realizzate funzioni di simulazione (TST) che, impostando a video i dati di input, eseguono la funzione presentando i risultati, oltre ad esporre le modalità di richiamo ed il modo di includerle all'interno dei programmi.

**News**
Le novità tecniche ed applicative via via sviluppate, vengono descritte in documenti di NEWS che vengono distribuite via e-mail a chi ne fa richiesta oppure sono disponibili via Internet.
L'archivio delle News è consultabile nel sito www.smeup.com (http://www.smeup.com) all'interno delle aree riservate a Clienti e Partner, con varie modalità di ricerca (per modulo, data, campi del testo, ecc..). Esso costituisce un patrimonio di informazioni che documenta il costante arricchirsi del prodotto, utile per chi, a sistema avviato, vuole risalire ad una novità della quale aveva avuto notizia via e-mail.

# Gli "oggetti" e le loro estensioni
Tra i vantaggi della metodologia ad oggetti applicativi, c'è che a ciascuno di loro (articolo, cliente, commessa, ordine, cespite, ...) è possibile collegare varie informazioni che ne arricchiscono le caratteristiche e le funzionalità in modo omogeneo, dato che sono comuni a tutti quelli di una medesima categoria.

**Note Strutturate**
È un insieme di note, nella forma di descrizioni a formato libero e senza limiti di dimensione, disponibili ad essere presentate e stampate nei punti desiderati dell'applicazione. Ad esempio, ad un articolo si possono collegare note di diverso tipo :  alcune da stampare nell'ordine d'acquisto, altre nel documento di spedizione, altre ancora nella fattura di vendita.

**Descrizioni Estese**
È un set di descrizioni alternative, ciascuna delle quali può essere usata per : 
 * integrare la descrizione standard dell'oggetto, come avviene quando sono necessarie descrizioni tecniche dettagliate
 * sostituire la descrizione standard, come nel caso della decodifica in lingue differenti necessaria per esporre nei documenti verso l'esterno (conferme d'ordine, fatture, ...) la descrizione congruente con la nazionalità del cliente.

**Parametri**
In numerose realtà aziendali risulta indispensabile memorizzare informazioni eterogenee, anche molto specifiche in relazione alla tipologia di lavoro dell'azienda. Si tratta di dati che non possono certo essere presenti negli archivi standard di qualsiasi applicazione. La gestione parametri risponde a questa esigenza :  ad ogni oggetto è possibile associare una serie ampia a piacere di informazioni, la cui natura è definita dall'utente. Ad esempio, si può fissare che, per gli articoli appartenenti alla classe delle lamiere, si memorizzino le opportune caratteristiche chimiche e meccaniche. Questa metodologia realizza un arricchimento potenzialmente illimitato delle informazioni disponibili, senza alcun intervento di personalizzazione, senza implicazioni negative per la manutenzione del prodotto ed imediatamente "visibili" dalle restanti parti del sistema.

**Flussi**
È possibile associare alle varie operazioni eseguite su un oggetto (inserimento, variazione, annullamento, collegamento, interrogazione) una serie di azioni, lanciate in successione. Ad esempio, dopo l'inserimento di un articolo, si può inviare una comunicazione (anche via e-mail) ad un utente che deve completarne le caratteristiche, oppure presentare la manutenzione della distinta base per poterla inserire contestualmente.

**OAV**
OAV è un acronimo per Oggetto/Attributo/Valore e costituisce una modalità di disaccoppiamento tra la localizzazione dell'informazione ed il suo reperimento. In sintesi, l'uso di un'informazione non è legato ad una sua presenza fisica nell'archivio ma alla possibilità di ottenerla, anche dinamicamente. Un esempio è l'esposizione di un cliente :  un valore ottenuto dall'analisi di una serie di informazioni, distribuite in più punti del data base. Con questa struttura è possibile arricchire liberamente il corredo degli attributi di un oggetto. Oltre a quelli definibili in fase di installazione, Sme.up fornisce una serie di OAV predefiniti, che arricchiscono dinamicamente le informazioni sugli oggetti. Ad esempio, per gli ordini di produzione sono ritornate le date di :  ultima attività, prelievo, versamento, ricavate dai movimenti e dalle dichiarazioni eseguite.

**Azioni su oggetti**
Per ogni oggetto viene fornito l'insieme di azioni (pop.up) eseguibili su di esso da un particolare utente in un particolare momento, fondendo azioni provenienti da punti diversi in un'unica lista accessibile da tutto Sme.up.
Le azioni di un oggetto sono : 
 * __Multilivello__. Ad esempio per un determinato oggetto il livello 1 è costituito dalle voci : 
 ** Scheda oggetto
 ** Gestione (apre un sottolivello di azioni di inserimento, modifica, ...)
 ** Azioni specifiche azienda
 ** Navigazione (apre un sottolivello di azioni per raggiungere oggetti con proprietà simili)
 ** ...e così via
 * __Sensibili all'istanza dell'oggetto__ :  per un particolare articolo potrebbe essere attiva la modifica mentre per un altro no
 * __Ridefinibili da script__ :  è suggerito un pop.up standard valido per tutti i tipi, poi per particolari oggetti questo può essere specializzato mediante script
La centralizzazione della gestione delle azioni rende possibile l'integrazione nativa del modulo di workflow con gli oggetti di Sme.up :  cedendo il controllo sulla gestibilità degli oggetti al modulo di workflow stesso si abilita una gestione molto potente degli oggetti di Sme.up, comandata dai processi aziendali.

![AAP_VAP_05](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_05.png)
# Strumenti di base
**Tabelle**
Un apposito strumento di utilità permette la gestione di archivi non complessi, senza la necessità di scrivere alcuna riga di codice. I campi dell'archivio ed i controlli a cui devono essere sottoposti vengono definiti in modo immediato e diretto. Questa impostazione standard è stata utilizzata per la gestione di tutte le tabelle di Sme.up, vale a dire degli elementi che guidano il funzionamento dell'applicazione (causali, classi, tipologie). È inoltre a disposizione dell'utente per realizzare applicazioni personali.

**Codifica guidata**
Gli incrementi di potenza e ricchezza applicativa degli attuali sistemi portano in sé anche una crescente complessità :  le informazioni da inserire sono via via più numerose ed una errata codifica può provocare comportamenti anomali e di difficile individuazione. In Sme.up è presente uno strumento che favorisce la costruzione "armonica" degli archivi anagrafici, fino dall'atto del loro inserimento :  a fronte di una serie di domande, impostabili parametricamente, è possibile ottenere la costruzione automatica del codice (di cui si definisce la struttura, qualora si adotti una codifica parlante) ed i campi vengono "popolati" in modo congruente in base alle risposte fornite.

**Organizzazione menu utenti**
L'accesso facilitato alle informazioni e l'individuazione della via più breve per accedere ad un dato sono tra le esigenze più sentite dall'utente di un ERP. Sme.up risponde a questa istanza con più modalità : 
 * quella standard prevista dal sistema operativo
 * una gestione alternativa a definizione tabellare, con il controllo preventivo dell'autorizzazione dell'utente ad eseguire l'azione e la possibilità di intestare ogni menu ad un oggetto specifico; ad esempio, se vi è un cliente particolarmente strategico, sul quale si esegue una serie di funzioni, le si può raccogliere in un menu intestato al cliente stesso
 * la navigazione libera tra i dati realizzata attraverso Looc.up

**Presentazione dei dati**
In tutte le interrogazioni e le stampe viene data la possibilità di scegliere quali informazioni presentare, in modo da poterle ottenere senza eseguire nessuna personalizzazione al software. La scelta di quello che si desidera stampare non è limitata alle sole caratteristiche dell'oggetto applicativo che si sta presentendo, ma è estesa ai suoi "attributi". Ad esempio, nella visualizzazione delle righe di un ordine di vendita è possibile riportare, oltre al cliente, qualsiasi sua caratteristica, sia anagrafica sia calcolata dinamicamente quali indirizzo, persona di riferimento o valore dello scoperto.

**Autorizzazioni e riservatezza**
In un ambiente con un gran numero di utenti, è indispensabile tenere in massima considerazione le logiche di autorizzazione all'accesso. Sme.up riserva particolare cura per garantire che ogni singolo dato possa essere inserito e/o consultato soltanto da chi ne ha le rispettive autorizzazioni. Il gestore del sistema ha a disposizione gli strumenti che gli permettono di impostare i livelli di autorizzazione per utenti (oppure anche per classi di utenti) e funzioni che vincolano gli accessi fino a livello di singolo campo.

**Workflow**
L'applicazione Workflow si occupa della gestione di processi aziendali, intesi come insiemi di compiti (impegni) svolti da diverse persone per il conseguimento di un obiettivo. Molte attività aziendali possono essere viste come processi, ad esempio : 
 * studio di un nuovo articolo
 * revisione di documentazione tecnica (come in figura)
 * vendita, dall'ordine alla consegna
L'applicazione guida gli utenti nell'esecuzione dei processi : 
 * attiva gli impegni non appena diventano eseguibili
 * rende visibili gli impegni a tutti e solo gli utenti che li possono eseguire
 * porta negli impegni tutte le informazioni necessarie per svolgere il lavoro :  oggetti Sme.up, documentazione, chiamate di menù...
Dal punto di vista dell'utente questo si traduce nella consultazione di una worklist, che contiene i diversi compiti da svolgere :  selezionando uno di questi gli verranno presentate tutte le informazioni utili e le azioni da eseguire. Portato a termine il compito, sarà il sistema ad avanzare il lavoro in maniera automatica ed immediata, portando le attività successive nelle worklist dei relativi utenti.

![WF-FIG0001](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/WF-FIG0001.png)
**Ricerche**
Ogni volta che viene richiesto un codice, oltre alle consuete ricerche (per lo stesso codice e alfabetica) sono presenti le seguenti funzioni : 
 * __ricerca contestuale__, che presenta i soli codici significativi in quello specifico contesto; ad esempio, quando si richiede un assieme nella manutenzione distinta base, è possibile richiamare una lista dei soli codici che sono presenti nella distinta come assiemi
* __ricerca estesa__, che permette selezioni mirate, impostando un tipo ricerca ed un codice di selezione; ad esempio, per gli articoli è prevista la ricerca per codice dei prodotti alternativi :  in questo caso, impostando un articolo, vengono presentati in lista tutti i suoi codici alternativi
 * __richiamo delle funzioni dell'oggetto__, che presentata una lista di funzioni, definibile dall'utente, che possono essere eseguite da quel punto; ad esempio, ad un articolo è possibile collegare l'interrogazione della distinta base, del ciclo di lavoro, l'andamento della sua disponibilità nel tempo.

**Memorizzazione impostazioni personali**
Particolare cura è stata prestata negli strumenti di impostazione preventiva delle informazioni da inserire, allo scopo di ridurre le complessità operative e migliorare contemporaneamente la fruibilità dell'ERP. Ogni volta che un singolo utente rientra in un formato video di richiesta informazioni, gli vengono proposte le impostazioni che aveva adottato in occasione dell'ultimo utilizzo.  È possibile memorizzare, e quindi richiamare, una impostazione specifica; è prevista, per ogni utente, la definizione di un'impostazione di "default" che viene presentata ogni volta che egli entra nel formato, c'é la possibilità di memorizzare anche gli estremi di una parzializzazione desiderata; ad esempio, un utente può decidere di entrare in una funzione sugli articoli con un accesso sempre filtrato sui soli prodotti finiti.

# Looc.up :  interfaccia puntata alla produttività
# Un motore per prendere decisioni
Il passaggio dall'interfaccia a caratteri a quella grafica ha portato ad ogni utente numerosi vantaggi in termini di possibilità operative (come l'impiego dei 'bottoni' oppure dei "combo box") e di capacità di ospitare su una singola mappa video molte più informazioni, grazie all'uso delle "linguette" ed alla maggiore risoluzione consentita. Sme.up mette a disposizione entrambe queste tipologie di rappresentazione ma ha portato avanti in modo assolutamente originale una ulteriore interfaccia che potremmo definire di tipo evolutivo, piuttosto che sostitutivo. Questo ambiente grafico offre opportunità che estendono in modo sostanziale le funzionalità dell'applicazione, senza assolutamente stravolgere il modo di operare tradizionale. I punti cardine di Looc.up si possono ridurre a due :  la capacità di riconoscere il tipo di "oggetto applicativo" di ogni campo presentato, il richiamo di tutte le funzioni collegate, quali il passaggio dalle informazioni inerenti ad un oggetto a quelle di un altro relazionato; ad esempio una navigazione diretta dall'anagrafica cliente alle righe d'ordine che lo riguardano e dall'articolo che queste contengono al fornitore che lo produce l'implementazione di una ricca serie di componenti specifici richiamabili sia dalle funzioni di un oggetto (in caso di emulazione) sia in modo indipendente (ingresso diretto dell'ambiente grafico).

# Componenti grafici ed applicativi
L'interfaccia Looc.UP dispone di una ricchissima gamma di componenti originali, interamente realizzati dal Centro di Sviluppo di Sme.UP. Di seguito ne ricordiamo i principali, dopo aver sottolineato peraltro che tutte le funzionalità vengono eseguite direttamente sul data base originale e che non è prevista alcuna forma di duplicazione dei dati, nemmeno provvisoria.

**Scheda**
È il contenitore che raccoglie in una stessa mappa informazioni eterogenee collegate ad uno stesso oggetto. Ne offre un'immagine completa, data la sua capacità di gestire contestualmente le classiche informazioni gestionali (come i dati anagrafici, le giacenze, la disponibilità, la distinta base, i costi per un articolo) accanto ad altre di differente (quali la fotografia, gli andamenti grafici, i semafori che segnalano non conformità o sotto scorta). All'interno della Scheda possono essere richiamate le altre componenti.

![AAP_VAP_06](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_06.png)
**Matrice**
Chiunque abbia adoperato un foglio elettronico è rimasto colpito dalla duttilità di utilizzo :  riordinamenti su una o più colonne, filtri di selezione dei contenuti, eliminazione o spostamento di intere colonne ed altro ancora. La Matrice ne ricalca il meglio delle caratteristiche, riportando un archivio o la parte prescelta in forma tabellare e rielaborando i dati allo stesso modo di quanto avviene con Excel e le sue tabelle Pivot. In aggiunta, è disponibile la funzione tipica delle modalità OLAP negli strumenti di Business Intelligence che permette di "sintetizzare" una o più delle dimensioni :  ad esempio i dati di vendita possono essere evidenziati, su richiesta, per zona, agente, famiglia di prodotti o qualsiasi altra caratteristica. La funzione "__colonne aggiuntive__" premette di arricchire le dimensioni della scheda con gli attributi (impliciti o calcolati) degli oggetti rappresentati, in questo modo partendo da schede semplici si possono ottenere report ritagliati sulle esigenze dello specifico utente. Altre informazioni preziose possono derivare da calcoli automatici che è possibile eseguire sui dati, quali il totale di una colonna, i valori medi, i massimi o i minimi. Questa impostazione consente di razionalizzare e sostituire in modo immediato e produttivo qualsiasi tipo di statistica.
Un'ultima caratteristica rende preziosa l'esposizione a Matrice, che già consente una visione più ampia e completa di una base dati :  l'aggiornamento. Qualsiasi dato contenuto in una cella può essere variato a piacere da un utente autorizzato.
__Nota__ :  Per evidenti motivi di sicurezza, la funzione di aggiornamento viene inibita quando si operi su basi dati che non siano quelle proprietarie di Sme.UP. Infatti, solo all'interno del nostro ERP la Matrice sa riconoscere i livelli di autorizzazione necessari perché la funzione di aggiornamento sia sicura, e dispone dei controlli di congruenza che sovrintendono alla integrità del data base.

![AAP_VAP_07](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_07.png)
**Albero**
L'abitudine di rappresentare le informazioni in forma di "albero" è generalmente limitata a pochi casi, come la presentazione della distinta base oppure il layout dei menu nell'ambiente Windows. Sme.UP ha valorizzato la potenza espressiva di questa rappresentazione in qualsiasi situazione nella quale sia conveniente ed espressivo esprimere le relazioni tra oggetti in forma gerarchica. Ad esempio, la visualizzazione ad albero di un magazzino suddiviso in aree, corridoi, scaffali ed ubicazioni si rivela molto più immediata di qualsiasi altra più tradizionale.

**Grafico**
È noto che la rappresentazione grafica migliora e rende più immediata la percezione dei fenomeni e delle informazioni contenute in un archivio. Sme.UP mette a disposizione una gamma estremamente ampia e sofisticata di modalità di rappresentazione in grado di descrivere una o più serie numeriche. Una caratteristica da mettere in evidenza è il fatto che si tratta di immagini attive, cioè di informazioni sulle quali è possibile indagare attraverso un doppio click del mouse che dà accesso ai dati sottostanti.

![AAP_VAP_08](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_08.png)
**Diagramma di Gantt**
Prezioso per qualsiasi funzione applicativa che abbia la necessità di presentare attività che si collocano in un intervallo di tempo. La schedulazione della produzione, lo sviluppo temporale della distinta di un prodotto finito ai vari livelli ne sono solo due esempi. Anche il Diagramma di Gantt dispone delle caratteristiche di immagine attiva comune alle altre rappresentazioni grafiche, come descritto in precedenza.

![S5_001C](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/S5_001C.png)
**Testo**
Considerando che il "contenitore" rappresentato dalla Scheda di Sme.UP fa da raccordo a informazioni di qualsiasi tipo, questa modalità sfrutta le proprietà di un ambiente visuale che permettono funzioni quali copia o taglia/incolla, preziose per realizzare, ad esempio, la documentazione di una funzione applicativa o per registrare le istruzioni d'uso.

**Questionari**
Risolvono un'ampia gamma di problematiche connesse alla catalogazione e alla presentazione di un set di domande ed alla gestione ed archiviazione delle relative risposte che, in funzione del contenuto (tipo :  sì/no o conforme/non conforme), a loro volta sono in grado di indirizzare i livelli inferiori del questionario verso i "rami" opportuni. Accanto agli impieghi tradizionali del questionario come la gestione dei Sistemi Qualità oppure il Configuratore di prodotto Sme.UP ne permette l'adozione in tutta una serie altri campi quali la creazione di una scheda per l'acquisizione di un nuovo cliente o una griglia per la codifica automatica di un nuovo articolo.

**Altre funzioni di utilità**
 * __Collegameto a business intelligence__ :  alimentazione dei cubi multidimensionali del data warehouse trasferendo direttamente sia le informazioni che la loro gerarchia.
 * __Collegameto a fogli elettronici__ :  popolati attraverso un semplice comando dalle informazioni provenienti dalle rappresentazioni "a Matrice" del sistema gestionale.
 * __Documenti Pdf__ :  costruzione facilitata con la possibilità di inserire testi e immagini, in varie modalità grafiche, per produrre schede prodotti, cataloghi, offerte, manuali di istruzione o altro.
 * __Accesso ai documenti__ :  di un oggetto, con la possibilità di definire in modo strutturato i collegamenti :  singoli oggetti, oggetti che rispondono a determinate caratteristiche, tutti i documenti di una cartella, ecc.

# Copertura applicativa
Per il modo con cui Sme.UP è stato concepito, è estremamente arduo predisporre una descrizione esaustiva dei processi che è in grado di svolgere e dei comportamenti che è in grado di assumere.

![B£BASE_088](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/BXBASE_088.png)
Questa affermazione si basa sulle seguenti caratteristiche : 
 * __la rigorosa architettura ad oggetti__, dato che la potenza funzionale deriva dall'efficacia descrittiva la modularità, con le funzioni elementari che si compongono per realizzare processi articolati;
 * __la parametrizzazione__, considerando che la combinazione delle singole scelte applicative tabellari porta a comportamenti eterogenei
 * __l'estendibilità__, perché le exit specifiche a disposizione dell'azienda modificano o estendono le funzioni esistenti.
Possiamo in ogni caso dare un'idea di massima della copertura applicativa, suddivisa nelle aree principali di cui si compone un sistema informativo gestionale : 
 * la descrizione degli oggetti che rappresentano le entità aziendali che vengono trattate
 * l'esecuzione delle attività operative, estemporanee oppure precedute da una pianificazione
 * la gestione degli aspetti contabili e fiscali
 * il controllo delle attività eseguite.
Nell'esposizione delle varie funzioni applicative svolte da Sme.UP, verrà dato maggior rilievo alle sue peculiarità, rimandando ai documenti di visione specifici per una esposizione più completa.

# Descrizione
# Organizzazione logistica
Rappresenta la realtà fisica dell'azienda :  se essa è formata da più plant (di produzione o soltanto di distribuzione) o se è costituita da un'unica sede. All'interno del plant, si individuano poi le aree in cui possono risiedere i materiali (ricevimento, magazzino materie prime, magazzino semilavorati, corso lavoro, spedizione, ecc.), e le aree esterne collegate al plant stesso (materiale in conto lavoro presso fornitori, in conto deposito, visione, presso fornitori o clienti). A loro volta, le aree possono essere, opzionalmente, suddivise in ubicazioni fisiche. Si individuano poi le risorse produttive :  centri di lavoro, macchine, linee di produzione, secondo una struttura gerarchica a definizione libera (ad esempio ogni centro di lavoro può essere composto da più macchine). Le aree di magazzino, oltre che in ubicazioni, possono essere suddivise in risorse; una rappresentazione realistica può essere la seguente : 
 * le aree di ricevimento e spedizione non hanno ulteriori suddivisioni
 * le aree chiuse (magazzini di materie prime, semilavorati e prodotti finiti) si suddividono in ubicazioni,
 * le aree di corso lavoro si suddividono in risorse, in modo da tenere sotto controllo la giacenza a piede macchina
Si definiscono le unità di movimentazione (colli, pallet, contenitori, ecc..) tramite le quali si possono eseguire gli spostamenti fisici tra le varie aree.

![AAP_LOG_04](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_LOG_04.png)
# Articoli
Gli articoli sono tutti gli oggetti fisici con cui si ha a che fare nella gestione aziendale, sia per tenere traccia della loro quantità (articoli gestiti a magazzino), sia soltanto per poterli muovere (all'interno dell'azienda oppure da o verso l'esterno), oppure per scopi descrittivi (in questi ultimi casi si tratterà di articoli non gestiti a magazzino). Sono articoli, oltre alle materie prime, ai semilavorati e ai prodotti finiti, anche gli stampi, gli utensili, gli attrezzi, i materiali accessori. La tipologia dell'articolo permette di identificare ciascuna di queste sottoclassi.

# Configurazioni
La configurazione è un insieme di caratteristiche che completa la definizione di un oggetto. In tal modo, ad esempio, in una riga di vendita è possibile, oltre all'articolo, definire le varianti e le opzioni richieste dal cliente. La modalità di costruzione della configurazione è totalmente libera :  può essere, ad esempio, un insieme di attributi codificati, con eventuali controlli incrociati di obbligatorietà e congruenza, oppure essere selezionata all'interno di un set di configurazioni codificate, oppure derivare dalle risposte di un questionario. La configurazione può estendere, in modo totale, il codice articolo, nei costi, nella giacenza, nella pianificazione materiali, nella valorizzazione fiscale.

# Esponenti di modifica
È possibile intestare ad un oggetto un esponente di modifica, con le informazioni di inizio validità (per data, per progressivo). La gestione dell'esponente di modifica può essere a vari livelli :  si parte dall'esposizione, nei documenti esterni, dell'esponente di modifica valido alla data di emissione, eventualmente con la memorizzazione nella riga del documento del suo valore, e si può arrivare ad una gestione completa, con giacenza e pianificazione per esponente di modifica.

# Matricole
La matricola è una informazione che può essere associata ad ogni istanza di un oggetto. Il suo utilizzo più comune è in abbinamento all'articolo. Si possono ricevere articoli matricolati dal fornitore, matricolare articoli di produzione propria (con regole di numerazione parametriche), includere un componente matricolato in un assieme a sua volta matricolato, ed infine spedire articoli matricolati. Si ottiene cosi una tracciabilità completa tra le matricole, naturalmente limitata agli articoli per i quali la si ritiene necessaria. La matricola può essere inoltre associata all'articolo nelle eventuali movimentazioni successive alla vendita (reso da cliente, rilavorazione interna, nuova spedizione, ecc.).

# Risorse
Col termine di risorsa si intendono tutti gli oggetti che danno disponibilità di tempo per svolgere le attività produttive aziendali. Ogni risorsa è definita da un tipo che la individua (reparto, centro di lavoro, macchina, ecc.) e da un gruppo che la caratterizza all'interno del tipo (ad esempio, tra le macchine, le frese ed i torni). Particolarmente utile risulta la gestione parametri, che per ogni gruppo permette la catalogazione di informazioni specifiche. È possibile assegnare una risorsa ad un oggetto (ad esempio un'altra risorsa), in modo da costituire una gerarchia :  ad esempio i centri di lavoro con le macchine che gli appartengono.

# Prodotto e processo
La distinta base permette di descrivere il modo in cui si compongono gli articoli per realizzare assiemi superiori. Grazie alla possibilità di poter avere più versioni dello stesso legame (differenziate dal tipo distinta) si possono ottenere diverse distinte per lo stesso assieme, (ad esempio distinte di pianificazione, di progettazione, di attrezzature). Inoltre, dato che permette di legare qualsiasi coppia di oggetti, (sia omogenei sia eterogenei), la distinta di Sme.UP è predisposta a rappresentare qualsiasi relazione gerarchica riconducibile ad un albero :  ad esempio legami tra disegni (complessivo e particolari), legami tra clienti (casa madre, magazzini periferici, dettaglianti). La distinta è filtrata dalla configurazione (che permette di escludere o modificare legami sia con una serie di criteri parametrici presenti in Sme.UP, sia realizzandone di specifici). Ogni legame inoltre può essere modificato o escluso tramite exit specifiche, in cui si possono implementare, ad esempio, particolari formule di calcolo per determinare la quantità di legame, oppure stabilire criteri di validità stagionali (un componente di una formula chimica che si utilizza solo d'estate).

I cicli di produzione sono invece lo strumento atto a descrivere il processo produttivo. Hanno le stesse peculiarità della distinta :  la possibilità di legare più coppie di oggetti (un assieme che deve essere prodotto con le risorse fornite dai componenti), la possibilità di avere diversi tipi cicli per lo stesso assieme (di pianificazione, critici, di controllo), il filtro dato dalla configurazione e la possibilità di modificare le informazioni tramite exit specifiche. L'effettivo utilizzo di risorse viene specificato attraverso dieci quantità a significato variabile, in funzione della risorsa stessa. Si caratterizza così il processo produttivo nel modo più vicino possibile agli effettivi parametri definiti e misurati. Ad esempio, oltre ai classici tempi di lavoro, macchina e attrezzaggio, si possono definire tempi di attesa, di riposo, tempi fissi per lotto, ecc.. In Sme.UP è fornito un set di base, per coprire le realtà produttive più comuni; è comunque possibile definire nuovi insiemi di valori, realizzando una exit specifica dove si determina il modo in cui essi contribuiscono al carico e al costo. Si possono definire cicli alternativi, ed operazioni alternative all'interno dello stesso ciclo. Nel caso di cicli alternativi, è possibile inserire una testata ciclo, che lo caratterizza globalmente (ad esempio il numero massimo di pezzi per cui è possibile o conveniente scegliere quel ciclo).

Per meglio caratterizzare il processo, è possibile collegare ad ogni fase di lavoro, un insieme eterogeneo di informazioni, componibili a piacere, che costituiscono le risorse produttive secondarie, quali le attrezzature, gli stampi, le competenze.

Particolare cura è stata prestata nella definizione delle alternative di fase è possibile descrivere compiutamente il percorso da compiere (quindi anche una rappresentazione a più stadi) :  ad esempio, una singola fase può essere alternativa di più fasi che si eseguono in serie.

# Enti
Gli enti sono tutti i soggetti esterni con cui viene in relazione l'azienda :  essi sono individuati da una tipologia e da un codice. Si possono così rappresentare, in uno stesso ambiente, clienti, fornitori, agenti, vettori, probabili clienti, segnalatori, ecc.. In un ambiente multiazienda è possibile l'utilizzo di un unico anagrafico enti in cui l'ente può giocare ruoli diversi, avremo così il "nominativo" che raggruppa i principali dati anagrafici e varie viste (fornitore, cliente, agente, potenziale cliente, ...) in base alle vesti che il nominativo assume per una particolare azienda o processo di business. Il data entry può essere customizzato in funzione delle esigenze e delle peculiarità dell'utente. Tutte le informazioni associate all'ente possono essere gestite con data di validità (date effective); i dati possono anche essere configurati in funzione di una specifica azienda o azienda/linea (dimension effective).

# Calendario
Il calendario è lo strumento tramite il quale si definisce la disponibilità nel tempo che offre un oggetto. Tale disponibilità può essere costituita, oltre ad un numero di ore per giorno, anche da altri fattori quantitativi quali, ad esempio, la capacità di immagazzinaggio (volume disponibile giornaliero). È possibile definire calendari aziendali, calendari per gruppi di oggetti od oggetti singoli, sia stabilendo il comportamento normale, sia introducendo eventuali eccezioni. La capacità effettiva di un oggetto, in un determinato intervallo di tempo, viene ottenuta determinando, per ogni giorno, il valore immesso al livello di maggior dettaglio.

# Listini / Condizioni
L'archivio listini/condizioni, permette di rappresentare tutti i casi in cui si presenta la necessità di attribuire un insieme di valori ad uno o più oggetti, in modo che i valori inseriti vengano utilizzati dalle altre applicazioni. Il significato dei valori ed il tipo degli oggetti è fissato dalla tipologia del listino. Con questa struttura è possibile rappresentare un gran numero di condizioni :  prezzi, sconti, provvigioni, per articoli, classi di articoli, clienti, agenti. È attiva l'ereditarietà :  (ad esempio, se non è definito lo sconto per articolo/cliente, si risale a quello per classe/cliente). I valori sono inoltre definibili in un intervallo di tempo, in modo da poter rappresentare promozioni o stagionalità, e per una soglia di quantità, per comprendere il caso, ad esempio, di sconti per scaglioni di quantità ordinata.

# Commesse
La commessa rappresenta un elemento di aggregazione di attività (previste ed eseguite), orientate alla realizzazione di un manufatto o di un servizio. Le sue caratteristiche sono ampiamente parametrizzabili :  è possibile definire una serie di date e di valori a significato variabile, dipendente dalla tipologia della commessa. È possibile inoltre collegare una commessa ad un'altra (realizzando il legame commessa-sottocommessa, anche a più livelli). Ogni attività prevista (ordine d'acquisto, di vendita, di produzione) può essere assegnata ad una commessa, è inoltre possibile tenere la giacenza in dettaglio per singola commessa, ed inoltre eseguire la pianificazione materiali separata per commessa (ovviamente per gli articoli di cui lo si ritiene necessario). I movimenti di magazzino e le attività eseguite a fronte di una commessa ne riportano il codice, costituendo la base per la sua consuntivazione.

# Esecuzione delle attività operative
# Documento Esterno
Il documento descrive un'attività di trasferimento da o verso l'esterno, sia prevista (ordine), sia effettiva (bolla di entrata o di uscita). Si compone di una testata, in cui si definiscono le caratteristiche generali, a cominciare dall'ente con cui si interagisce, e da un insieme di righe, in ciascuna delle quali è definito l'oggetto che si trasferisce (non necessariamente un articolo), la quantità di trasferimento (prevista o effettiva), oltre ad un insieme di caratteristiche specifiche (prezzi, sconti, provvigioni). Questa impostazione astratta dell'oggetto documento, permette di unificare il trattamento di un insieme di entità diverse, quali, ad esempio : 
 * ordini di vendita
 * ordini di acquisto
 * bolle di entrata
 * bolle di uscita
 * previsioni di vendita
 * ordini quadro
 * contratto
Ciascuna di esse viene individuata dal tipo documento, che permette di differenziare i comportamenti specifici.

![AAP_VAP_11](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_11.png)
# Flusso di documenti
Un documento si trasforma in un altro (generalmente di tipo diverso) attraverso un flusso di attività, vale a dire un insieme di passi elementari, quali la richiesta dell'ente interessato, del documento di origine, la scelta delle righe da trasferire, con le relative quantità. Ogni passo è ampiamente parametrizzabile (ad esempio si può impostare di accettare documenti solo in un certo stato), ed inoltre è possibile aggiungere passi personali che, essendo scritti rispettando le convenzioni del colloquio, vengono richiamati in modo naturale dalla funzione di esecuzione del flusso.

# E.D.I.
Questo modulo ha lo scopo di far colloquiare, in termini generali, l'applicativo con il mondo esterno, tramite il trasferimento di un "messaggio", che contiene le informazioni inviate e ricevute, ed è composto da una parte fissa (dati relativi al colloquio) e da una parte specifica. Non è suo compito eseguire il trasferimento "fisico", ma svolgere tutte le attività che sono comprese tra il colloquio fisico e l'estrazione o l'inserimento del messaggio nell'applicativo.

# Richieste di movimentazione
La richiesta di movimentazione è l'elemento su cui si basa l'intera logistica di Sme.UP. Essa rappresenta l'intenzione di movimentare un articolo (all'interno dell'azienda, oppure da o verso l'esterno), specificando l'origine e la destinazione, oppure, fissando una delle due, far scegliere l'altra al sistema, tramite regole parametriche. Un esempio verrà dato nel paragrafo seguente, relativo alle attività di spedizione. L'esecuzione della richiesta di movimentazione darà luogo alle effettive transazioni di magazzino.

# Spedizioni e viaggi
La spedizione è un particolare flusso di documenti, nel quale un ordine di vendita si trasforma in un documento di uscita. L'attività di spedizione può essere guidata dalla richieste di movimentazione :  si stabilisce innanzitutto che cosa spedire (eventualmente in modo automatico tramite un'analisi dell'evadibilità) :  ciò genera una richiesta di movimentazione, in cui si fissa, ad esempio, che il materiale dovrà partire da un'area di spedizione. Se l'area dei prodotti finiti è gestita ad ubicazioni, le richieste di movimentazione, che conterranno le ubicazioni di prelievo, scelte con logiche parametriche, costituiranno il documento di picking. L'esecuzione della richiesta avrà l'effetto di registrare il trasferimento del materiale all'area di spedizione. All'atto della spedizione verrà prodotto il documento di spedizione che chiuderà la richiesta di movimentazione. Nel flusso si possono inserire particolarità quali la stampa del documento di spedizione e di eventuali ulteriori documenti accompagnatori, l'aggiunta di righe non previste. È possibile inoltre definire i colli in cui si suddivide la spedizione, e comporre il relativo packing list. Più documenti di spedizione possono essere raccolti in un viaggio, qualora essi abbiano, anche in parte, un percorso comune. L'oggetto viaggio è la base per l'organizzazione delle spedizioni, sia a livello fisico (controllo del peso e/o del volume), sia a livello temporale (quando e che cosa spedire).

# Ricevimenti
Il ricevimento materiali dall'esterno è un altro esempio di utilizzo del flusso di attività. Il materiale ricevuto può transitare in un'area di accettazione, per poi essere trasferito alla destinazione finale, eventualmente tramite richieste di movimentazione :  ad esempio se l'area componenti è gestita ad ubicazioni, il sistema suggerisce l'ubicazione più opportuna. Collegata al ricevimento è la creazione del lotto, che accompagnerà il materiale nel collaudo, ed eventualmente nella sua destinazione di magazzino, se l'articolo necessita della tracciabilità.

# Trasferimenti
Quando l'azienda è disposta su più posizioni geografiche i trasferimenti di materiale tra uno stabilimento e l'altro possono essere gestiti attraverso flussi di attività che sono la combinazione di flussi di spedizione e di ricevimento. Si può gestire un'area intermedia che rappresenta il "viaggiante" tra i due stabilimenti oppure l'uscita da uno stabilimento può caricare direttamente un'area di giacenza dello stabilimento di destinazione.

# Provvigioni
Esiste un archivio delle provvigioni che può essere popolato sia in automatico, estraendo i dati dalle fatture di vendita, che manualmente per l'immissione di provvigioni manuali (premi, anticipi, ecc...). La liquidazione delle provvigioni agli agenti può essere gestita con differenti periodicità (annuale, mensile, trimestrale) ed effettuata sull'importo fatturato, sull'importo incassato oppure sull'importo saldato della fattura (queste informazioni vengono automaticamente ricavate dalla contabilità). Tutte le liquidazioni effettuate vengono storicizzate, permettendone una consultazione in qualsiasi momento. Viene inoltre calcolato il piano dei contributi dell'agente (ritenute d'acconto, Enasarco, ISC, e FIRR), con la stampa della fattura proforma, e la creazione opzionale di un documento di ciclo esterno sul quale verrà eseguito il controllo all'arrivo della fattura dell'agente. Apposite stampe riepilogano la situazione contributiva del singolo agente e dell'azienda.
Esistono apposite funzioni di contabilizzazione che premettono di attribuire i costi, nonché i contributi in funzione del loro periodo di competenza (e non in funzione della registrazione della fattura agente) : 
 * Contabilizzazione Provvigioni, suddivisa fra : 
 ** Costo (contabilizza i costi provvigioni in funzione della loro competenza)
 ** Liquidato (contabilizza le fatture da ricevere per le provvigioni liquidate in un periodo)
 * Contabilizzazione Contributi, suddivisa fra : 
 ** Enasarco
 ** FIRR

Al momento della contabilizzazione della fattura agente i contributi Enasarco / FIRR vengono trattati in modo separato.

# Richieste d'Acquisto
Questo modulo automatizza gli aspetti burocratici connessi all'inserimento della richiesta di acquisto di un bene da parte di un utente, e della successiva approvazione, a vari livelli di responsabilità a seconda del valore del bene. Le richieste validate vengono trasformate in ordini di acquisto, eventualmente raggruppando più richieste omogenee nella stessa riga, ed assegnando, qualora non sia già presente, il fornitore. Viene tenuto traccia del legame tra richiesta ed ordine, in modo da poter seguire lo stato di avanzamento dell'ordine generato da una richiesta. Vi è la possibilità di inserire anche richieste di conto lavoro (sia pieno sia di fase), nel qual caso vengono generati i relativi impegni di materiale.
Le richieste di conto lavoro pieno normalmente provengono dalla pianificazione materiali, qualora si decida di non trasformare i consigli direttamente in ordini ma di passare dalle richieste. Le richieste di conto lavoro di fase sono invece generate a partire dagli impegni risorse degli ordini di produzione eseguiti esternamente, sempre nel caso in cui non si decida di passare direttamente agli ordini di conto lavoro.

# Ordini di produzione
L'ordine di produzione ha lo scopo di programmare la realizzazione di un articolo, in una quantità e per una data. Tale realizzazione necessita di un consumo di materiali e di risorse (vedi il punto successivo). È possibile usare il ciclo o la distinta standard, oppure definirne di specifici. Ciò si realizza sfruttando la possibilità di intestarli ad oggetti che non sono articoli :  in questo caso si intesta, ad esempio, la distinta all'ordine di produzione, con il vantaggio, per l'utente, di usare la funzione di manutenzione della distinta base. Le stesse considerazioni valgono per il ciclo dell'ordine. Si possono definire ordini di rilavorazione, impostando come componente lo stesso articolo che si vuol ottenere ed aggiungendo, eventualmente, i componenti da sostituire e togliendo quelli da smontare (recuperi). È possibile assegnare un ordine di produzione ad un ordine "master", e questo a più livelli, in modo che si possa costituire una struttura ad albero. Si possono definire anche ordini di trasformazione :  si imposta, oltre all'articolo che si vuole ottenere, anche l'articolo di partenza, che si vuole trasformare :  il sistema costruirà una distinta "dinamica", che conterrà come impegni i componenti presenti solo nell'articolo d'arrivo, e come recuperi quelli presenti solo nell'articolo di partenza, mentre i componenti comuni verranno trascurati. È presente la schedulazione a capacità infinita degli ordini di produzione (sia al più presto sia al più tardi, sia entrambe) che, oltre a dare una idea di massima del carico, e quindi costituire la base del CRP, fornisce le informazioni per determinare gli indici di avanzamento dell'ordine (slack time, critical ratio, ecc..), utilizzabili come dispatching rules nella schedulazione a capacità finita. È possibile inoltre non intestare un ordine di produzione ad un articolo specifico, ma sfruttarlo come un insieme di attività da eseguire e di materiali da consumare, ad esempio per compiere una manutenzione. Vi sono funzioni specifiche per realizzare il prelievo ed il versamento a magazzino. C'è inoltre la possibilità di realizzare il prelievo in automatico a backflushing, all'atto del versamento o dell'avanzamento. Maggiori particolari verranno esposti nella descrizione della movimentazione interna.

![AAP_VAP_10](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_10.png)
# Impegni materiali e risorse
Gli impegni materiali costituiscono l'insieme degli articoli, con le relative quantità, necessari per produrre un assieme. Essi possono essere intestati ad oggetti diversi (righe di documento, richieste d'acquisto, ordini di produzione). La loro costruzione è automatica, a partire dalla distinta base dell'assieme, nettificata dai movimenti già eseguiti. Gli impegni risorse sono il corrispondente, per quanto riguarda il consumo di risorse. Anch'essi possono essere intestati ad oggetti diversi (righe di documento, ordini di produzione, contenitori). Pure la loro costruzione è automatica, a partire dal ciclo dell'assieme, nettificato dalle attività eseguite.

# Conto lavoro e materiale di terzi e presso terzi
In Sme.UP non esiste un modulo specifico per il conto lavorazione, ma esso viene ottenuto combinando funzioni già presenti nel sistema. Il conto lavoro attivo (realizzazione del prodotto in azienda con materiale di terzi) si ottiene attravesro una riga di ordine cliente a cui si collegano gli impegni materiali. Al ricevimento dei componenti si caricano in un'area specifica per ente. All'atto della spedizione del prodotto si chiudono gli impegni materiali, scaricando i componenti da quell'area. Il conto lavoro passivo (realizzazione presso terzi con materiale fornito dall'azienda), si divide in due tipologie.
* si ha il conto lavoro pieno quando il terzista esegue un livello completo di distinta :  si ottiene una riga di conto lavoro collegando ad una riga di acquisti gli impegni materiali. Questa riga può convivere, all'interno dello stesso ordine, con righe di puro acquisto. La spedizione dei componenti trasferisce i materiali dall'area interna a quella esterna (per terzista). Al ricevimento del finito, si scaricano i componenti da quest'area;
 * si ha invece il conto lavoro di fase quando il terzista esegue una o più fasi del ciclo di produzione. In questo caso la riga di conto lavoro è collegata ad un ordine di produzione origine. Il ricevimento dell'assieme può eseguire automaticamente anche una dichiarazione di attività su quest'ordine.

La gestione di materiale di terzi in azienda e di materiale dell'azienda presso terzi, si configura definendo aree opportune (rispettivamente interne ed esterne, e di proprietà aziendale e di terzi), per le varie suddivisioni (conto deposito, visione, prestito d'uso, ecc.) ed inserendo, di volta in volta documenti di trasferimento da un'area all'altra.

# Giacenze
Una caratteristica di Sme.UP è di non avere un ambiente logistico separato dal magazzino gestionale, ma di permettere di spingersi fino al massimo dettaglio desiderato, direttamente all'interno del magazzino gestionale, che in tal modo risulta essere l'unica informazione di giacenza a cui tutto il sistema accede. Ciò è stato realizzato con una composizione parametrica dell'oggetto intestatario della giacenza, che, oltre a contenere il plant, l'articolo e l'area, può avere fino ad un massimo di quattro altri codici che lo caratterizzano.
In tal modo i seguenti dettagli di giacenza sono compresi in questa struttura : 
 * Articolo/Ubicazione /Lotto (per gestire al massimo livello di dettaglio le aree interne)
 * Articolo/Configurazione (se la configurazione differenzia i codici)
 * Articolo/Commessa
 * Articolo/Fonitore o Cliente (per trattare le quantità in conto lavoro, deposito, visione,...) e, naturalmente, qualsiasi altra combinazione di questi oggetti.

È inoltre possibile aggiungere, per individuare la giacenza, il codice del contenitore, che costituisce una chiave univoca di accesso. In tal modo, se ad esempio si ha la giacenza per articolo/ubicazione, specificando il contenitore, si conosce che cosa contiene (l'articolo), quanto contiene (la giacenza) e dove è situato (l'ubicazione).

# Movimentazione interna
La movimentazione interna di magazzino, ha lo scopo di trasferire gli articoli da un luogo all'altro e di eseguire i prelievi ed i versamenti di produzione. Tutte queste attività possono essere eseguite tramite richieste di movimentazione, che suggeriscono la scelta dell'origine e/o della destinazione del materiale. Ad esempio, nei trasferimenti interni, esse sono d'ausilio nella ricompattazione di un'area gestita ad ubicazioni, nell'assegnazione dell'ubicazione di stoccaggio nel passaggio dall'area di collaudo al magazzino componenti, o nella scelta dell'ubicazione di prelievo nel passaggio da un magazzino chiuso ad un'area di wip o di spedizione. Nei prelievi di produzione, si possono impostare, ad esempio, regole di consumo fifo (dal lotto più vecchio), nei versamenti regole di stoccaggio in aree diverse in funzione delle caratteristiche dell'articolo (infiammabile, deperibile, ecc.). L'operazione di assegnazione delle richieste, viene eseguita da un motore inferenziale, che esegue un set di regole, fino al raggiungimento dell'assegnazione dell'intera quantità della richiesta. La flessibilità del metodo è data dal fatto che uno degli effetti dell'applicazione di una regola è la scelta della regola successiva, creando un percorso di assegnazione flessibile. C'è comunque la possibilità di eseguire prelievi, versamenti e trasferimenti, in modo diretto, qualora non si desideri implementare una logistica avanzata.

# Ubicazioni
Tramite la definizione delle ubicazioni viene suddiviso in modo più dettagliato il magazzino. La codifica può avvenire in modo automatico (per coordinate) in modo da costituire una mappa delle varie aree di magazzino (corsie, scaffali, ecc.). Le ubicazioni si differenziano poi per tipologia (monoarticolo, per prodotti di caratteristiche particolari, ecc.), che contribuisce alla scelta dell'ubicazione in fase di stoccaggio.

# Contenitori
La movimentazione può essere eseguita facendo riferimento ad unità fisiche (contenitori, colli, pallet). In questo caso tutto il contenuto viene mosso. Sono previste anche attività di riempimento (con eventuale produzione del documento di identificazione), svuotamento, suddivisione e accorpamento. È possibile assegnare ad ogni articolo il tipo di contenitore nel quale è previsto che venga mosso.

# Tracciabilità lotti
All'atto del ricevimento di un articolo d'acquisto (o di conto lavorazione) o al versamento dell'ordine di produzione, è possibile registrare un nuovo lotto. Oltre a scopi di controllo qualità, può risultare utile come base per analisi di tracciabilità. I prelievi di produzione dovranno essere intestati al lotto utilizzato :  in tal modo, tramite i movimenti di magazzino, si formeranno dei legami in base ai quali sarà possibile rispondere alle domande : 
 * quali lotti di un componente d'acquisto sono entrati in un lotto di prodotto finito?
 * un lotto di acquisto in quali lotti di assiemi superiori (a tutti i livelli) è entrato?
Va tenuto presente che per realizzare la tracciabilità completa è necessario, per i codici dei quali si intende percorrere la tracciabilità, dichiarare sempre il lotto, in modo da non interrompere la catena di informazioni.

# Inventari
Per lo svolgimento di questa attività, si deve innanzitutto inserire il codice inventario, nel quale si definiscono le informazioni necessarie alla procedura di conta :  le modalità di estrazione (dalla giacenza attuale, ad una data impostata, con una exit utente), il tipo costo per le valorizzazioni, le modalità di applicazione degli scostamenti. Ogni funzione richiede il codice dell'inventario :  in tal modo è possibile tener traccia degli inventari completati. Sono previste due modalità di registrazione dell'inventario : 
 * su lista di conta. La giacenza contata viene registrata direttamente sull'inventario estratto.
 * su cartellini distribuiti agli utenti. Si produce un archivio di cartellini, eventualmente raggruppati in lotti di conta. Essi vengono stampati, compilati, raccolti ed inseriti nel sistema con i dati identificativi (articolo, lotto, area, tipo giacenza, ubicazione, ecc.) e la quantità trovata. Con un passo successivo da essi si aggiorna l'inventario.
L'inventario, dopo essere stato compilato, può essere stampato o visualizzato, in varie modalità e sintesi, eventualmente valorizzando gli scostamenti, ed infine concluso con l'esecuzione automatica delle rettifiche inventariali.

# Fotografia di magazzino
È una funzione che permette di memorizzare la situazione delle giacenze ad una qualsiasi data. È inoltre possibile ottenere fotografie incrementali (differenze tra le situazioni a due date), oppure dalla giacenza attuale, oppure dal magazzino fiscale. La fotografia così ottenuta può essere visualizzata o stampata, eventualmente riaggregata a livelli superiori, e valorizzata secondo un tipo di costo selezionato.

![GMANIN_01](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/GMANIN_01.png)
# Magazzino fiscale
Questo modulo offre uno strumento per valorizzare le rimanenze di magazzino. È possibile definire più scenari, per simulare diverse modalità di valorizzazione. È inoltre data la facoltà di escludere alcune aree dalla valorizzazione, definendole non fiscali (materiale di terzi in azienda, scarti, ecc.).

# Consuntivazione attività
La consuntivazione delle attività si basa sulla rilevazione delle attività svolte nell'azienda :  le quantità prodotte con i relativi tempi, le improduttività e le attività indirette. La dichiarazione delle attività può essere intestata ad una fase di un ordine di produzione, ad una riga di un ciclo di lavorazione, oppure può essere un'attività estemporanea. È possibile eseguire la dichiarazione a partire dalla lista degli impegni residui di un ordine di produzione, oppure di una risorsa. È possibile inoltre effettuare la dichiarazione per persona :  le sue ore di presenza si distribuiscono sulle varie attività eseguite nel giorno. Se la dichiarazione è a fronte di un ordine di produzione, è possibile, in automatico, eseguire i prelievi dei materiali necessari alla fase che si sta dichiarando (proporzionalmente alla quantità in avanzamento), e, se è l'ultima fase del ciclo, eseguire il versamento dell'assieme e l'aggiornamento dell'ordine di produzione. È presente il concetto di operazione di gruppo :  la dichiarazione di una fase, (definita come master) induce la dichiarazione automatica di altre fasi, precedenti o successive (definite come automatiche).

# Analisi disponibilità
L'analisi disponibilità (proiezione nel tempo della giacenza prevista di un articolo) è lo strumento su cui si fonda la pianificazione materiali, e tutti gli strumenti di analisi fattibilità e copertura. L'elemento di base è la fonte, che costituisce il canale di comunicazione da parte del sistema gestionale. Si impostano fonti presenti (giacenze e scorte) e future (ordini di acquisto, vendita, produzione, impegni, ecc.), con varie possibilità di parametrizzazioni :  ad esempio, si selezionano le giacenze di un'area specifica, gli ordini di vendita solo in uno stato di confermati, ecc..
Si raccolgono quindi le fonti desiderate, in un gruppo fonti, che costituisce, insieme all'articolo, l'input per la disponibilità. Diversi gruppi fonti permettono di ottenere diversi profili di disponibilità, che rispondono a diverse esigenze.
Ad esempio, si può valutare l'effetto dell'inclusione della scorta minima, oppure di un budget che si aggiunge al portafoglio vendite. È inoltre possibile filtrare la disponibilità con una serie di oggetti. Ad esempio, si può fissare : 
 * la commessa, (qualora si abbiano giacenze separate per commessa)
 * la configurazione (se è un elemento che diversifica l'articolo)
 * il fornitore (per decidere i rifornimenti ad un terzista)

# Budget (MPS)
L'MPS (Master Production Schedule) è lo strumento con cui vengono rappresentati, in Sme.UP, gli sviluppi temporali di una quantità legata ad una coppia di oggetti. L'astrazione di questo modello ne permette un utilizzo non limitato al budget, o all'MPS in senso stretto, ma esteso ad ogni grandezza, sia preventiva sia consuntiva, di cui interessa seguire l'andamento nel tempo. La periodicità è variabile :  si può diversificare per grandezze diverse e, per la stessa grandezza può assumere valori diversi per ogni periodo (ad esempio all'inizio in giorni, poi in settimane ed infine in mesi). Si definisce vista lo sviluppo temporale di una grandezza (legata ad una coppia di oggetti di tipo qualsiasi). È stata realizzata una serie di funzioni, sia di natura generale (operazioni aritmetiche, confronti tra due viste, suddivisione di una vista in altre in base ad una tabella di pesi, ecc.), sia di natura applicativa (partendo da una vista ottenere le viste dei suoi componenti di distinta base, delle risorse del ciclo di produzione, partendo da un articolo ottenere l'andamento della disponibilità futura, valorizzare una vista in base ad un costo prefissato, sintetizzare in una vista i movimenti di magazzino eseguiti in un periodo, oppure le righe di ciclo esterno, passate o future). Queste funzioni possono essere composte liberamente in un flusso sequenziale di azioni, eventualmente arricchite da funzioni specifiche, in modo da realizzare un processo articolato, sia di preventivazione, sia di consuntivazione :  come la definizione di un budget a partire da dati storici, ed il suo sviluppo in consumi materiali e risorse, sia in termini di quantità sia di valore; oppure la definizione del piano principale di produzione, in base al portafoglio ordini e alle previsioni di vendita, eventualmente combinati con regole specifiche; oppure ancora l'analisi dell'impatto sulle risorse dei risultati della pianificazione materiali, realizzando uno strumento di CRP.

# Pianificazione materiali
La pianificazione materiali (MRP) si caratterizza per la scelta di una ricca parametrizzazione, che consente di affrontare situazioni complesse, avendo cura di non appesantire l'impostazione nei casi più semplici. È stato quindi fatto un uso esteso dell'ereditarietà (tempi di approvvigionamento, lotti di produzione, politiche di pianificazione definiti, singolarmente, al livello più alto possibile). È stato realizzato un strumento di simulazione, che può partire dai dati del sistema oppure immessi manualmente dall'utente, che ha lo scopo di fornire una conoscenza diretta delle tecniche MRP (si imposta l'input e si vede immediatamente il risultato della pianificazione), e di permettere una regolazione del funzionamento della pianificazione (si varia un parametro e, senza modificare l'input, si vede come varia l'output, se quindi la nuova impostazione ha raggiunto gli scopi prefissati).
Tra le caratteristiche più rilevanti della pianificazione materiali, segnaliamo : 
 * la possibilità di definire, per ogni articolo, o classe, l'insieme dei fabbisogni e delle coperture (ad esempio la giacenza in un'area di controllo qualità è considerata solo per alcuni articoli)
 * la possibilità che l'oggetto della pianificazione non sia solo l'articolo, ma l'articolo abbinato alla commessa, o alla configurazione, o all'ente (in modo da realizzare una catena logistica di fornitura)
 * la segnalazione delle eccedenze (quantità superflue non eliminabili, perché giacenti o per effetto della lottizzazione)
 * la possibilità di definire orizzonti variabili per il raggruppamento dei fabbisogni
 * la pianificazione interattiva di un singolo codice (e di tutti i suoi componenti che subiscono variazioni, fino all'ultimo livello di distinta base)
 * la presenza contemporanea di più ambienti di pianificazione, che consentono simulazioni di vario tipo (ad esempio senza considerare la lottizzazione)
 * la realizzazione di un algoritmo che ottimizza l'emissione di nuovi ordini in luogo di un eccessivo anticipo
 * la possibilità di trascurare automaticamente piccoli fabbisogni, la cui copertura, per effetto del lotto minimo, gonfierebbe in modo perverso i fabbisogni del livello e dei livelli inferiori.
 * la possibilità, in modo analogo, di non emettere ordini pianificati che coprono unicamente una frazione (sotto una soglia prefissata) della scorta minima, in modo da evitare effetti perversi simili a quelli descritti nel punto precedente.
 * la possibilità di schedulare a capacità infinita (sia al più presto sia al più tardi, sia entrambe) gli ordini di produzione pianificati, per ottenere una stima del carico a medio/lungo termine.
 * la pianificazione integrata multiplant, in cui, per ogni articolo, si esegue una pianificazione separata di ogni plant utilizzatore con emissione di ordini pianificati di trasferimento dal plant di produzione, e successivamente si pianifica quest'ultimo plant con i fabbisogni propri e quelli provenienti dagli altri plant, con la possibilità di tener conto dei tempi di trasferimento e della merce in transito.
I risultati della pianificazione sono consultabili con una potente funzione di presentazione con navigazione, che, a partire da una forma per articolo, o per ente, o per tipo di suggerimento, permette di : 
 * passare ad ogni altra forma
 * risalire agli assiemi e di scendere ai componenti, a qualsiasi livello, realizzando l'equivalente di un'esplosione e implosione di distinta base
 * passare ad una rappresentazione sintetica periodicizzata
 * esporre il suggerimento in modo colloquiale
 * simulare l'impatto della variazione di una copertura (riduzione della quantità e posticipo della data) sui fabbisogni fino al livello dell'assieme.
I suggerimenti (sia di nuovi ordini sia di azione sull'esistente) sono applicabili, per chi ne ha l'autorizzazione, direttamente da questa funzione. Data la completa modularità del disegno, la pianificazione materiali può essere inserita, senza alcuna duplicazione di dati, in qualsiasi sistema gestionale :  i dati dell'ambiente (articoli, fabbisogni, coperture) vengono integrati dai dati di pianificazione (inseriti in Sme.UP). L'applicazione dei suggerimenti è realizzata in modo che la scrittura dei dati sull'ambiente (ordini di produzione e d'acquisto), venga realizzata con una interfaccia specifica.

![M5CMRP_022](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/M5CMRP_022.png)
# ATP (Available To Promise)
L'ATP è uno strumento che permette di datare al più presto una quantità richiesta dal cliente, in funzione della disponibilità dell'articolo e dei suoi componenti (ad ogni livello), dei tempi di approvvigionamento, ed opzionalmente di vincoli di capacità produttiva. Esso può funzionare sia come simulazione (imputando un articolo ed una quantità viene presentata la miglior data), sia in effettivo (all'atto della conferma di una riga di ordine cliente datata con ATP vengono impegnate le disponibilità dell'articolo o dei suoi componenti che vengono usate per poter rispettare la data di consegna proposta). Ricordiamoci che questo strumento, che è ai primissimi posti nella hit parade dei desideri degli utenti di sistemi informativi gestionali, per poter dare risultati attendibili (e quindi non sottoposti ad una successiva revisione manuale), necessita che il resto dell'applicazione (giacenze, ordini e impegni futuri, in corso e pianificati) sia ad un livello di affidabilità pressoché totale, e comunque assai superiore a quanto richiesto per un funzionamento accettabile della pianificazione materiali.

# Mancanti per commessa
È un modulo operativo che, a partire da un insieme di fabbisogni principali, impostabili manualmente (una lista di articoli, quantità e date), oppure estraendoli dal sistema (ordini clienti, di produzione, commesse), ne esamina la fattibilità, a tutti i livelli, in base alle coperture esistenti, segnalando i mancanti. A differenza dalla pianificazione materiali, che esamina la totalità degli impegni, (indipendenti e dipendenti), questo strumento cerca di soddisfare soltanto quelli derivati dai fabbisogni principali impostati :  è come se l'intera azienda, nel breve periodo, avesse come unico obiettivo il loro soddisfacimento. La segnalazione dei mancanti è puramente operativa :  non tiene conto di lotti minimi e multipli. Per contro, le coperture vengono soddisfatte al più presto, eventualmente anche spezzandole in più date, qualora sia possibile una copertura parziale. Questo modulo risponde alle esigenze di esaminare le criticità e le urgenze, che si determinano a fronte di imprevisti nel processo produttivo. In particolare, in una gestione a commessa, permette di tenere sotto controllo i materiali necessari per ciascuna di esse. Sono attive visualizzazioni che permettono di navigare dalle coperture agli impegni, a tutti i livelli di distinta base, con filtri sulle criticità (tutti i fabbisogni, esclusione di quelli coperti da giacenza, o da ordini in corso o pianificati).

![JM_01_05](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/JM_01_05.png)
# Schedulazione operativa
La schedulazione Fine.UP costituisce uno strumento interattivo e grafico, che fa parte nativamente del sistema gestionale, atto a risolvere i problemi di allocazione delle risorse e di sequenziazione delle attività, che si presentano quotidianamente nelle aziende produttive e di servizi.

Le principali caratteristiche dell'applicazione sono : 
 * schedulazione di impegni risorse di vari tipi
 ** ordini di produzione in corso
 ** ordini pianificati
 ** righe di ciclo esterno
 ** contenitori, in presenza di produzione snella;
 * definizione di più scenari di schedulazione, per eseguire simulazioni, e scegliere di rendere definitivo il più efficace;
 * suddivisione in ambiti di competenza schedulabili separatamente;
 * ampia scelta di dispatching rules (oltre a quelle implementate, possibilità di definirne di specifiche, anche come combinazione di quelle esistenti);
 * modellazione della strategia (rispetto della consegna, saturazione delle risorse, comunanze tecnologiche o di attrezzaggio, eventualmente combinate e messe in competizione tra di loro);
 * rappresentazione estesa del processo
 ** sovrapposizione tra fasi successive dello stesso ordine
 ** accostamenti sulla stessa risorsa di fasi successive dello stesso ordine
 ** tempi d attrezzaggio parametrici (dipendenti dalla situazione esistente e da quella futura)
 ** appuntamenti statici tra ordini (rispetto di vincoli di priorità definiti esternamente) e vincoli esterni fissi (date al più presto)
 ** calendari ed efficienza definibili al massimo dettaglio
 ** definizione di risorse a capacità infinita trattate con tempo di attraversamento;
 * integrazione completa con il sistema gestionale :  non solo assenza di duplicazione di dati e loro trasferimento, ma anche possibilità, dall'interno della schedulazione, di navigare verso tutti i dati e, avendone l'autorizzazione, di operare modifiche, immediatamente recepite alla successiva rischedulazione, eseguita dall' interno di questa applicazione;
 * calcolo dei principali indici di prestazioni (saturazione, earliness, tardiness, ecc,,) e loro storicizzazione;
 * possibilità di modificare i risultati con azioni manuali
 ** di ordinamento della sequenza di schedulazione
 ** di forzatura delle risorse selezionate
 ** di congelamento della situazione
 * analisi dei materiali critici;
 * possibilità di realizzazione di exit utente che permettono
 ** di modificare i dati di input e dei risultati
 ** di specializzare la strategia in 'spinta' (decidere dove eseguire la fase selezionata) e in 'tiro' (decidere quale fase eseguire subito dopo quella appena schedulata)
 ** di estendere le informazioni riportate nella presentazione dei risultati
 ** di realizzare forme di presentazioni 'ad hoc', integrate nella navigazione della presentazione dei risultati.

![S5_001B](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/S5_001B.png)
# Produzione a disponibilità chiamata
La produzione a disponibilità chiamata (PDC) è una particolare modalità di gestione della produzione, di nostra concezione, che ha lo scopo di rappresentare il processo produttivo in modo più "fisico" rispetto agli ordini di produzione. Essa si basa sull'assunto che la movimentazione in produzione avvenga per contenitori, e sulla rappresentazione "logistica" del ciclo produttivo come un insieme di risorse (centri di lavoro o macchine), ciascuna delle quali ha un'ubicazione a monte e a valle. Gli ordini pianificati dall'MRP si traducono in contenitori pianificati. All'atto dell'inizio delle attività, essi si tramutano in contenitori effettivi. Il loro spostamento da una ubicazione all'altra, induce una dichiarazione di avanzamento automatica, nel caso che le ubicazioni siano a monte e a valle di una risorsa (l'informazione logistica contiene, implicitamente, quella produttiva). Lo spostamento all'ubicazione finale rappresenta il versamento a magazzino. In tal modo non si introduce un livello di informazione immateriale (l'ordine di produzione, con le rigidità che esso comporta), ma ci si limita a registrare tutto ciò che avviene in fabbrica :  si riempiono contenitori, li si sposta, li si dichiara bloccati in caso di verifica della qualità, si sposta del materiale da un contenitore all'altro, ecc.. Inoltre, dato che gli ordini rimangono sempre pianificati, vengono "tirati" i contenitori di volta in volta più urgenti (lo strumento trae il nome da questa peculiarità :  si "chiama" la disponibilità presente in fabbrica, sotto forma di contenitori nelle diverse ubicazioni, e quindi a diversi gradi di completamento del ciclo produttivo).

# Sistema Qualità ISO 9000
È un insieme di moduli atto a supportare l'azienda nella gestione di tutti gli aspetti connessi all'introduzione e al mantenimento di un Sistema Qualità in linea con le Norme ISO 9000 nella più recente versione nota come "Vision 2000".
È suddiviso nelle seguenti aree : 
 * __sistema di controllo__ :  comprende i moduli che, richiamati dalla gestione aziendale quotidiana, alimentano il sistema di qualità :  la gestione degli strumenti di misura, dei piani di campionamento, dei cicli di collaudo, dei lotti, delle dichiarazioni di collaudo con i rilievi associati, delle non conformità, il collegamento a sistemi SPC;
 * __sistema di supporto__ :  in essa si inseriscono informazioni che sono pretese dalle normative ma che risultano estremamente produttive per la gestione aziendale nel suo complesso :  la formazione del personale, la matrice delle responsabilità, la gestione e il controllo della documentazione, la FMEA, la gestione degli Audit e delle richieste di intervento;
 * __sistema di analisi e supervisione__ :  offre una serie di strumenti di sintesi delle situazioni rilevate e numerose statistiche, tra cui la definizione di indici (realizzati in modo parametrico), con cui ottenere una misura oggettiva dell'andamento del livello qualitativo aziendale; comprende l'analisi dei lotti, delle non conformità, degli indici di qualità, la valutazione dei fornitori.

# Manutenzione Impianti
Permette di definire gli impianti con i loro componenti, e di schedulare gli interventi programmati, con varie politiche (ad esempio ogni 'n' giorni, ogni 'n' pezzi lavorati), associandoli ai materiali necessari. Consente di dichiarare l'effettuazione sia degli interventi programmati (che vengono chiusi e riprogrammati nel futuro), sia di quelli straordinari, registrando tempi, materiali, costi aggiuntivi, ed eventuali documenti associati. Queste registrazioni costituiscono la base per poter effettuare analisi statistiche e ricavare indici di prestazioni.

# Modifiche tecniche
L'introduzione delle modifiche del prodotto o del processo, è seguita in tutte le sue fasi, dalla proposta, all'approvazione (eventualmente su più livelli), all'applicazione agli archivi effettivi aziendali. È possibile riunire in un progetto più modifiche che devono entrare in funzione contemporaneamente (ad esempio la sostituzione di un componente che comporta la variazione del ciclo produttivo). È possibile inoltre analizzare l'impatto economico dell'introduzione della modifica tecnica, in termini di obsolescenza che essa introduce.

# Contabilità e finanza
# Contabilità
Questa applicazione offre una copertura completa per quanto riguarda gli obblighi fiscali vigenti, permette inoltre la gestione dei crediti e dei debiti, dei rapporti con gli istituti di credito e i percipienti, e offre gli strumenti di base per il controllo di gestione.
Caratteristiche principali : 
 * Perfetta integrazione con tutto il gestionale (Documenti, Cespiti, Provvigioni, Anagrafiche Enti, Controllo gestione, Qualità, EDI);
 * Multiazienda (archivi unici, interrogazioni aggregate);
 * Gestione dati di impostazione a livello di gruppo e a livello di azienda;
 * Set'n play di impostazione (Periodi e Date, Piano dei Conti, Analitica ecc.);
 * Multidata (registrazione, competenza, date bancarie);
 * Multivaluta;
 * Multipertinenza (fiscale/gestionali) e multicondizione (attive/simulate);
 * Righe e registrazioni automatiche;
 * Elaborazioni in modalità provvisoria/definitiva/ristampa annullamento (es. giornale, registri iva, generazione reg. apertura/chiusura ecc.);
 * Gestione lettere.

![AAP_VAP_12](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_12.png)
# Piano dei conti / Riclassifiche
La struttura del piano dei conti non segue la tradizionale suddivisione in mastro/conto/sottoconto (a tre o quattro livelli), ma assegna semplicemente ad ogni conto 'n' riclassifiche, ciascuna delle quali è un attributo, anche virtuale, del conto. Con questo modello si possono definire strutture del piano dei conti del tutto libere e di 'profondità' variabile, per coprire le più diverse esigenze di rappresentazione aggregata del bilancio, tra le quali il bilancio CEE.

# Registrazioni contabili
La registrazione è suddivisa in due parti :  una testata, in cui sono riportati i dati comuni (informazioni fiscali, natura della registrazione) e le righe, che contengono le scritture contabili (conti, importi). In questo modo si riduce al minimo la duplicazione di informazioni. Una testata di registrazione è caratterizzata dall'appartenere ad un esercizio contabile, dall'avere una pertinenza (contabile, gestionale, comune) ed una condizione (attiva, sospesa, simulata).

# Modelli di registrazioni
Particolare cura è stata posta nella definizione di modelli preimpostati per le registrazioni contabili :  l'esecuzione della registrazione consiste nel richiamare un modello, completandolo con i dati opportuni. È possibile inoltre intestare il modello ad un oggetto (ad esempio un canone ricorrente ad un fornitore), nel qual caso per eseguire la registrazione è sufficiente, all'atto dell'inserimento, richiamare l'oggetto intestatario.

# Rate
La registrazione, se prevede un pagamento futuro, si sviluppa in una o più rate (sia in modo automatico sia inseribili manualmente), che costituiscono la base su cui si svilupperà la gestione dei crediti e dei debiti. La rata è un oggetto distinto dalla riga di registrazione, che ne rappresenta una possibile origine. Questo disaccoppiamento è dovuto al fatto che una rata è collegabile a qualsiasi oggetto. Ad esempio, da una riga di un ordine di vendita o d'acquisto si possono generare le rate delle previsioni di pagamento (in valore e data), che costituiscono le informazioni su cui si baserà l'esposizione dei flussi di cassa. Per un controllo puntuale dei pagamenti, abbiamo introdotto il concetto di rata di dovuto e di pagato :  la rata generata da una registrazione che prevede un pagamento futuro è una rata di dovuto La registrazione di pagamento genera invece una rata di pagato, che si collega esplicitamente ad una ed una sola rata di dovuto (qualora il pagamento chiuda più rate di dovuto il sistema genera automaticamente più rate di pagato per mantenere l'accoppiamento).

![C5D010_033](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/C5D010_033.png)
# Pratiche amministrative
È stato introdotto il concetto (e quindi l'oggetto) di "pratica amministrativa", che costituisce il raggruppamento di un insieme di oggetti su cui eseguire azioni comuni. In tal modo si uniforma la rappresentazione di funzioni eterogenee quali la costruzione di una distinta effetti, di un elenco solleciti per pagamento scaduti, di un documento Iva. Naturalmente ogni tipo diverso di pratica ha una propria modalità di composizione.

# Registrazione pagamenti
La composizione della pratica di distinta effetti è il primo passo, opzionale, della registrazione dei pagamenti :  si possono raggruppare rate, ancora aperte, secondo diverse modalità (di un cliente, da presentare come effetti ad una banca, con residuo al di sotto di un valore). La registrazione dei pagamenti può essere eseguita richiamando una pratica composta in precedenza, oppure selezionando interattivamente le rate da saldare, sia in modo cieco (ad esempio fino alla copertura di un importo prefissato), sia in modo visualizzato. In questa fase è possibile far generare dal sistema movimenti di oscillazione cambi e di abbuono per saldare una rata. Tutti gli automatismi nella registrazione dei pagamenti possono essere corretti manualmente, in quanto essa non è una funzione specifica ma, essendo richiamata dall'interno della registrazione, può essere seguita, prima della conferma, dalla manutenzione della registrazione stessa.

# Solleciti
Dalle rate di dovuto ancora aperte, è possibile generare periodicamente segnalazioni di sollecito, con opportuni filtri (esclusione di clienti, soglia di importo), che costituiscono un archivio storico consultabile secondo varie modalità. La stessa rata di dovuto, se rimane aperta, può generare, nel tempo, diverse segnalazioni di sollecito, di gravità crescente. Un sollecito viene dichiarato chiuso all'atto della registrazione della rata di pagato.

# Analisi crediti e debiti
Questa funzione si basa sull'accoppiamento tra le rate di dovuto e di pagato :  di ogni documento può essere presentata una situazione per data di pagamento (atteso o eseguito); oppure il bilanciamento all'interno di ogni scadenza, oltre alla consueta sintesi per registrazione. Per ogni scadenza vengono calcolati i giorni di ritardo di pagamento, e viene valorizzato il ritardo. L'analisi può essere effettuata sia ad oggi, sia nel passato, in modo da ricostruire dinamicamente una situazione pregressa.

# Controllo DDT / Fatture
È presente uno strumento di registrazione contabile delle fatture con controllo dei documenti di trasporto che le originano. Tale controllo può essere attivato oltre che per il ciclo passivo (come di consueto ) anche per il ciclo attivo, in modo da ottenere anche in questo caso una migliore integrazione fra documenti e registrazioni. È possibile scegliere le anomalie da rilevare (differenza prezzo, quantità, pagamento, .ecc.) e le azioni da intraprendere al loro verificarsi :  apertura di non conformità, invio di e-mail, blocco dei pagamenti, ecc. Sono presenti, nel ciclo passivo, varie modalità operative : 
 * viene eseguito il controllo. In un secondo tempo viene eseguita la registrazione contabile per le sole fatture corrette;
 * il controllo e la registrazione contabile vengono eseguiti contemporaneamente, con sole segnalazioni non bloccanti;
 * viene eseguita la registrazione contabile sia per un singolo documento, sia di massa, (anche partendo dalle fatture ricevute via EDI), mentre il controllo viene eseguito in un secondo tempo;
 * è inoltre possibile eseguire in modo automatico la registrazione delle fatture da ricevere e da emettere, che verranno in seguito stornate (dalla registrazione della fattura se di un esercizio successivo, manualmente se nello stesso esercizio). In tal modo si tiene conto del valore in attesa fattura, sia nel ciclo attivo sia in quello passivo.

![C5C040_005](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/C5C040_005.png)
# Ritenute d'Acconto
La gestione delle ritenute d'acconto è completamente integrata nella registrazione contabile. All'atto della registrazione della fattura, se l'ente è definito come percipiente, viene presentato un formato ulteriore in cui si inseriscono le informazioni specifiche della ritenuta. All'atto del pagamento della ritenuta, viene generata in modo automatico una riga di registrazione di chiusura. È prevista inoltre la stampa delle lettere di certificazione e la produzione dell'archivio relativo al modello 770.

# Gestione IVA
Oltre all'adempimento degli obblighi fiscali, sono presenti le seguenti funzioni :  gestione del plafond, gestione settori per attività in riferimento all'oggetto aziendale, calcolo del prorata, IVA a esigibilità differita, imputazione automatica dell'Erario conto IVA, protocollazione di registrazioni non IVA.

# Contabilità analitica
Allo scopo di fornire un maggior livello di dettaglio alle righe di registrazioni contabili :  è possibile assegnare fino a tre oggetti per specificarne la natura, ed altri tre per specificarne la destinazione. La guida per questa funzione è il conto contabile, in cui sono definite le tipologie degli oggetti che definiscono la natura e la destinazione, ed opzionalmente, i loro valori ammessi od assunti. È possibile inoltre suddividere l'importo della registrazione in più valori. Sono impostabili modelli di registrazione che contengono la suddivisione percentuale dell'importo della registrazione. Se le informazionipredefinite sono esaustive (oggetti e percentuali di suddivisione), la registrazione analitica viene eseguita in modo automatico. In caso contrario essa va inserita manualmente, all'interno della funzione di immissione della registrazione contabile.

![AAP_VAP_13](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_13.png)
# Contabilità gestionale
Pertinenza/Condizione a vari livelli Date competenza : 
 * Registrazione Ratei/Risconti
 * Registrazione Fatture da Emettere/Ricevere
 * Registrazione Stanziamenti Registrazioni autostornanti Analisi Registrazione Rettifiche di chiusura periodo

# Analisi di bilancio
È possibile redigere il bilancio oltre che per le classiche riclassifiche del piano dei conti e CEE per qualsiasi altra riclassificazione si voglia utilizzare e secondo criteri fiscali o gestionali, con la possibilità di analizzarne struttura ed indici nonché di confrontare bilanci di periodi diversi e/o di altre aziende del gruppo e di verificarne gli scostamenti.

![C5E010_006](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/C5E010_006.png)
# Stanziamenti
Il fine delle registrazioni di stanziamento consiste nella possibilità di applicare il principio di competenza anche nei periodi mensili oltre che annuali. Applicare il principio di competenza significa imputare i costi/ricavi in base alla loro effettiva competenza temporale :  ci sono perciò costi/ricavi che devono essere imputati ad un differente mese (ad esempio fatture la cui consegna è avvenuta in un mese differente rispetto alla rilevazione della fattura stessa) oppure la cui imputazione deve essere suddivisa su più mesi (ad esempio canoni di assicurazione annuali che dovranno essere suddivisi sui 12 mesi cui il canone fa riferimento). Ciò si traduce nella creazione di registrazioni gestionali del costo/ricavo in base alla competenza (registrazione di stanziamento) collegate alla registrazione contabile. È possibile impostare modelli per eseguire la compilazione automatica degli stanziamenti al momento dell'inserimento delle registrazioni contabili rilevanti. Tramite questa gestione è inoltre possibile la rilevazione automatica dei ratei/risconti sia a livello mensile che annuale.

# Tesoreria
Sono previste le funzioni basilari di controllo del conto corrente bancario :  impostazione delle condizioni per ogni rapporto, riconciliazione dell'estrattoconto e dello scalare interessi, controllo dell'affidamento (sia come funzione autonoma sia come ausilio alla generazione delle distinte). È presente inoltre la gestione dei finanziamenti :  apertura, chiusura, versamenti, con controlli del residuo e della situazione dei pagamenti. Tramite l'impostazione delle varie condizioni, è possibile attivare la determinazione automatica delle spese bancarie. È prevista infine la possibilità di realizzare comunicazioni remote da e verso l'istituto di credito.

# Analisi disponibilità finanziaria
L'Analisi Disponibilità Finanziaria (ADF) è uno strumento atto a riprodurre, in base alle migliori conoscenze attuali dei fenomeni futuri, l'andamento nel tempo dei flussi finanziari. In stretta analogia con l'analisi disponibilità dei materiali, si possono definire fonti attuali (saldi di conti di liquidità) e fonti future (entrate o uscite di liquidità previste ad una data).

![C5D050_083](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/C5D050_083.png)
Queste ultime vengono estratte, tramite opportune interfacce, dalle applicazioni gestionali (cicli attivi e passivi, piani MPS, ecc.), con diverse possibilità di ritorno dei dati (ad esempio, nel ciclo attivo, l'ordinato residuo al netto o al lordo di quanto già in bolla). Un insieme di fonti forma il gruppo fonti, che costituisce la base su cui si fonda l'ADF. È possibile comprendere nell'analisi anche fonti non Sme.UP, sia attuali sia future, in modo che essa risulta uno strumento generalizzato, indipendente dal contesto applicativo. Ogni fonte ritorna un evento elementare, (caratterizzato da un segno, un importo, una data e un codice valuta), ed un oggetto intestatario dell'evento, caratteristico della fonte, che costituisce l'elemento di maggior dettaglio dell'analisi. Ad esempio, il documento di ciclo esterno è l'oggetto intestatario dell'importo spedito, l'ente del fido, il conto contabile del saldo iniziale. Sono possibili sia analisi per oggetto elementare, sia, ricorsivamente, per un suo elemento di aggregazione. Questa funzione è applicabile sia al singolo ente (per il controllo del fido), sia globalmente per l'intera azienda (per il controllo della disponibilità futura di cassa).

# Dichiarazione d'intenti
È implementata la gestione del registro delle dichiarazioni di intento ricevute nonché la sua trasmissione in via telematica all'Agenzia delle Entrate. È presente inoltre la gestione dell'invio delle dichiarazioni di intento dell'Azienda ai suoi fornitori.

# Comunicazioni Valutarie Statistiche
Ai fini statistici, per la bilancia dei pagamenti, è obbligo comunicare all'ufficio italiano cambi le operazioni valutarie poste in essere dagli operatori non bancari :  la gestione informatizzata delle CVS (Comunicazioni Valutarie Statistiche) consente l'automatizzazione della compilazione dell'apposito modulo di comunicazione alla banca.

# Intrastat
Integrazione con registrazione
 * Interattiva
 * Scrittura/Estrazione cieca
Integrazione informazioni documenti
Estrazione da documenti conto lavoro
Data entry di gestione e controllo movimenti intrastat
Controllo e produzione file di trasmissione

# Cespiti
L'applicazione Cespiti ha come scopo di risolvere le problematiche connesse alla determinazione degli ammortamenti dei beni di proprietà dell'azienda.
Le principali caratteristiche applicative sono le seguenti : 
 * è possibile il calcolo dell'ammortamento fiscale, secondo la normativa vigente, di quello civilistico, e di 'n' diversi ammortamenti industriali. Ciò è ottenuto introducendo il concetto di linea di ammortamento (simile allo scenario in pianificazione e schedulazione) che costituisce un ambiente separato in cui vengono impostati i parametri di calcolo e registrati gli ammortamenti risultanti.
 * per ogni linea si può infatti definire un piano di ammortamento esplicito per il singolo cespite, oppure impostare valori (sia importi sia percentuali, per il singolo esercizio o globali), a livello di cespite, di categoria, o generali, con ricerca per risalita, in modo da inserire il dato al suo massimo livello, senza introdurre ridondanze.
 * è inoltre possibile inserire movimenti manuali relativi ad una singola linea, in modo da poter simulare rivalutazioni, svalutazioni, ecc..
Ogni elaborazione di calcolo degli ammortamenti registra tutta la storia futura dei cespiti presenti nel sistema. In tal modo sono facilmente ottenibili, per ogni linea, sia analisi 'verticali' (piano di ammortamento di un singolo cespite), sia 'orizzontali' (valore totale dei cespiti in un qualsiasi esercizio futuro). È inoltre stato predisposto il collegamento dalla contabilità generale, per introdurre nell'applicazione i movimenti di apertura (acquisti), ed il collegamento verso la contabilità generale, per eseguirvi la registrazione degli ammortamenti.

![A5BASE_003](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/A5BASE_003.png)
# Controllo
# Costi
Questa applicazione permette di determinare il costo del prodotto, suddiviso in 99 componenti elementari definibili liberamente e liberamente raggruppabili. Per lo stesso articolo si possono determinare più tipi di costo (diversificati, ad esempio, per il tipo ciclo o distinta scanditi, per i costi dei materiali di base assunti). Ogni tipo costo può essere caratterizzato da una data di calcolo, in modo da poter tener traccia delle variazioni subite nel tempo. È possibile inoltre determinare i costi ad un livello di dettaglio superiore all'articolo (ad esempio articolo/configurazione, articolo/commessa). Per ogni articolo si determinano i costi dei materiali (dalla distinta base), del lavoro (dal ciclo), degli scarti, ecc.. I costi unitari di input (costi dei materiali d'acquisto e tariffe dei centri di costo), potranno essere il risultato di precedenti elaborazioni. Ad esempio il controllo di gestione determinerà il costo orario (preventivo o consuntivo) dei centri di costo. Le fatture dei fornitori saranno la fonte di determinazione dei costi medi di acquisto e/o conto lavoro. Ovunque è richiesta la valorizzazione di un articolo, (ad esempio nella valorizzazione di magazzino, della disponibilità, ecc.), si deve precisare il tipo del costo, la data di calcolo, l'eventuale ulteriore scomposizione (commessa, configurazione ecc.), ed il livello del costo, che definisce la somma di un insieme delle componenti elementari, e consente di ottenere dinamicamente costi "parziali", quali il costo dei materiali del livello, degli scarti, il costo diretto, ecc..

# Controllo di gestione
Come per altri moduli, Sme.UP non vuole essere collegato ad una specifica impostazione del controllo di gestione, ma fornire l'insieme di strumenti di base necessari ad una grande gamma di possibili impostazioni. Ciò, come sempre, è ottenuto realizzando strutture di dati "neutre", che contengono, tra le proprie informazioni, il significato degli oggetti e dei valori, oltre agli oggetti e ai valori. In particolare si sfruttano due strutture generali simmetriche che sono state già presentate :  l'MPS e l'archivio di scomposizione del costo. La prima rappresenta, per un gruppo di oggetti, lo sviluppo nel tempo, secondo una periodicità definita, di un singolo valore. La seconda rappresenta, sempre per lo stesso gruppo di oggetti, per un singolo periodo, un insieme di 99 valori a significato variabile. Per entrambe queste strutture sono state realizzate funzioni di ripresa di informazioni dal gestionale e di sintesi, che possono essere composte in un flusso di attività, ed eventualmente integrate con funzioni di ripresa specifiche.
La struttura dell'MPS, permette di rappresentare lo sviluppo di budget e consuntivi nel tempo, quali, ad esempio : 
 * la quantità prevista per articolo cliente nei prossimi 12 mesi
 * la quantità venduta per articolo cliente negli ultimi 12 mesi
 * l'aumento pianificato per fornitore e classe materiale nei prossimi 5 anni
 * le spese per centro di costo
 * il piano di produzione per articolo nelle prossime 12 settimane
 * il carico dei centri di lavoro per giorno
La struttura dei costi, permette di rappresentare budget e consuntivi analitici, relativi ad un periodo, quali, ad esempio : 
 * scomposizione del costo del lavoro mensile, per dipendente
 * scheda di costo per centro di costo
 * sintesi valori per cliente/articolo :  ordinato, spedito, a quantità e valore
 * indici di servizio per cliente e classe di prodotto
 * scheda dei costi per commessa.

![AAP_VAP_14](http://localhost:3000/immagini/MBDOC_VIS-AAVAP/AAP_VAP_14.png)
# Sinergie con ambienti e sistemi esterni
# Internet
Il Web rappresenta inconfutabilmente lo strumento dal potenziale più rivoluzionario che la tecnologia abbia messo a disposizione dei Sistemi Informativi negli ultimi dieci-quindici anni anni. Perché tutta questa potenzialità venga scaricata a terra in ambiente ERP, è indispensabile peraltro che la soluzione applicativa ne sfrutti due elementi chiave :  la struttura di comunicazione e, forse ancora prima, le possibilità che offre per ripensare in maniera originale la gestione e supervisione di alcuni processi. Si pensi semplicemente al Cliente che può accedere attraverso la Rete ad un catalogo elettronico ed immettere i propri ordini, piuttosto al coordinamento di più unità produttive in una Supply Chain integrata.
Obiettivo di Sme.UP verso il mondo Internet è quello di rendere disponibili dati e funzioni all'interno di un browser lasciando ogni libertà di impostazione grafica. Per fare ciò è stato realizzato il modulo Web.UP costituito da un insieme di "TAG" generiche che possono essere inserite in una pagina HTML per costruire pagine dinamiche. Il concetto di informazione dinamica è legato alla metodologia con cui vengono reperite le informazioni contenute in una pagina HTML :  normalmente, tutta l'informazione contenuta in una pagina statica è fissata nel codice HTML della pagina stessa. Un pagina dinamica contiene invece delle informazioni che vengono costruite nel momento stesso il cui un utente remoto richiede la visualizzazione della pagina :  sono quindi informazioni che rispecchiano lo stato di un sistema nel momento preciso in cui un utente ne richiede la visualizzazione.

 :  : REM
xxIMG P([SME.IMG]\TAB£A\GM\GMAIN\XXXXXXXXXXXXXXXX_01.png) R(70) A(C) C(Scheda XXXXXXXXXXXXXXXXXXfoto giacenza)
 :  : REM.END

Web.UP ha le seguenti caratteristiche : 
 * definizione di una serie di strumenti per l'accesso ad informazioni gestionali dall'interno di pagine web; il gestionale di riferimento per il progetto è Sme.UP ma è possibile, tramite l'uso di apposite interfacce, estendere l'accesso a qualsiasi altro gestionale
 * identificazione di una serie di moduli di base a cui possano essere associate delle funzioni dinamiche fondamentali; ad esempio, la lettura di attributi associati ad un oggetto o l'esecuzione di una funzione complessa come la visualizzazione di una distinta o l'inserimento di un nuovo ordine
 * completa indipendenza tra gli oggetti dinamici e la parte statica delle pagine web :  i moduli dinamici sono il più possibile indipendenti dal codice HTMLstatico e il loro utilizzo non richiede competenze superiori a quelle normalmente in possesso ad un progettista di pagine web statiche; non è necessario che le problematiche relative al collegamento con il programma gestionale siano note al progettista Web.UP
 * gli oggetti dinamici sono caratterizzati da forte atomicità ed ogni oggetto può essere identificato in base a tre elementi fondamentali :  le informazioni richieste (input), la funzione svolta (elaborazione) e il tipo di risultato prodotto (output); questi tre elementi sono esaustivi nel definire le proprietà e le metodologie di utilizzo dell'oggetto dinamico; per l'uso corretto di un oggetto dinamico non devono di norma essere conosciute caratteristiche tecniche intrinseche al funzionamento dell'oggetto stesso (secondo il principio dell'incapsulamento).
 * la struttura del progetto consente in ogni momento lo sviluppo di nuovi moduli dinamici o la semplice modifica dei moduli esistenti; i moduli sono il meno possibile correlati tra loro per evitare che modifiche su uno di essi si possano ripercuotere negativamente sugli oggetti eventualmente collegati.

# Dati di campo
In numerosi settori di attività -ed in particolare nel mondo manifatturiero -un monitoraggio efficiente dei processi pretende informazioni ricevute in tempo reale. Questo può avvenire solo attraverso l'acquisizione diretta dei dati di campo, che vengono messi in relazione con le altre indicazioni e condizioni contenute nell'ERP. Considerando che la soluzione è fortemente condizionata dalla struttura hardware presente in ogni azienda, Sme.UP è predisposto per collegarsi in modo facile con sistemi di campo specifici.
Sono previsti i seguenti interfacciamenti : 
 * collegamento a terminali in radiofrequenza che diventano a tutti gli effetti, terminali del Sistema (con un video di dimensioni ridotte) per cui possono essere utilizzati per eseguire transazioni elementari o presentare un set ridotto di informazioni; a tal fine abbiamo definito la possibilità di costruire, mediante tabelle, menu per questa categoria di terminali, con i quali normalmente si eseguono azioni elementari su un oggetto (ad esempio :  chiamata dei materiali in un'ubicazione, caricamento di un contenitore su un viaggio)
 * preparazione di una struttura di messaggi per comunicare, nei due sensi, con un sistema esterno che emula un video per ricevere informazioni dal campo (ad esempio, collegareun programma alla lettura di un badge o ad una pesata di bilancia); in modo simmetrico si possono realizzare funzioni (associabili ad oggetti) che hanno il loro effetto in sistemi di campo (ad esempio accendere la lampadina dello scaffale dove si trova un certo articolo).

# Sinergie con ambienti e sistemi esterni
Il modello OAV (Oggetti, Attributi e Valori), intesi come informazioni atte ad arricchire il corredo di un oggetto per facilitarne il reperimento, si estende ad oggetti presenti in file system esterni all'AS/400. L'individuazione dell'oggetto esterno può infatti essere eseguita colloquiando con un prodotto di gestione documentale che permette di navigare nel file system, e di integrare gli OAV che caratterizzano l'oggetto (aggiungendone di specifici). Inversamente Sme.UP può fornire i propri OAV alla gestione documentale. Una volta individuato, l'oggetto può essere eseguito,concordemente alla sua natura; visualizzazione di un'immagine o di un filmato, esecuzione di un brano acustico, ecc... Ad esempio, noto un cliente, è possibile individuare le tipologie dei suoi documenti (offerte, contratti, ordini, ecc,,), da ciascuna di esse presentarne l'elenco (eventualmente filtrato con attributi, ad esempio un intervallo di date), ed infine visualizzare il singolo documento.

# CRM
In un ambiente ad oggetti, l'acronimo CRM assume un significato limitante, per quanto riguarda il suo primo termine (Customer = Cliente). La gestione della relazione (RM = Relation Management) può infatti proficuamente estendersi a tutti gli altri soggetti che interagiscono con l'azienda (fornitori, collaboratori, dipendenti, ecc..). Ciascuno di essi è un tipo di soggetto a cui si possono associare sia informazioni specifiche del proprio tipo, sia comuni a tutta la classe. Data la natura eterogenea delle informazioni, ci è risultato naturale l'utilizzo della scheda, componente grafico che permette di raccoglierle e di presentarle in varie modalità (matrici, immagini, andamenti, allarmi, alberi). Alcune informazioni sono presenti nel sistema, o ricavabili da esse (ordini in corso, situazione del fido e degli insoluti, indici di servizio, statistiche a vari livelli di aggregazione), altre invece vengono reperite all'esterno (Siti Internet, modo di raggiungere la sede, ecc..).
