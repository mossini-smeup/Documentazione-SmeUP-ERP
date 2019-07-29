# Architettura Sme.up

## Gli Oggetti Applicativi
Le attività svolte dai Sistemi Informativi Gestionali sono sostanzialmente due :  l'inserimento ed il reperimento delle informazioni.
Entrambe queste attività, sia per poter rappresentare in modo sufficientemente potente la realtà aziendale, sia per potersi adeguare alle sue naturali evoluzioni, devono poter avere comportamenti eterogenei. L'inserimento di una informazione può comportare delle verifiche precedenti ad esso,che ne abilitano o ne condizionano l'esecuzione, ma anche degli effetti successivi.
Ad esempio, l'inserimento di un ordine può essere condizionato dal controllo del fido del cliente,mentre quello di un nuovo articolo può indurre l'invio di un messaggio ad un altro utente perchè ne completi i dati anagrafici.
Anche il reperimento delle informazioni è eterogeneo poiché esse possono : 

- essere inserite direttamente dall'utente (es. :  la descrizione di un articolo);
- essere derivate da altre informazioni tramite più di una lettura (es. :  le caratteristiche di un articolo definite nella classe a cui esso appartiene);
- essere frutto di un'elaborazione (es. :  il valore complessivo di un ordine, in base alla quantità e ai prezzi unitari delle righe che lo compongono);
- nascere all'atto della richiesta dell'informazione, in quanto dipendenti, ad esempio, dal trascorrere del tempo (come il numero di giorni di ritardo di consegna di un ordine non ancora evaso);
- corrispondere alla combinazione delle precedenti.


![BLV0001-01](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-01.png)>Figura 1 - Schema generale di un Oggetto in Sme.up

Tale complessità può essere affrontata in questo modo : 

- all'atto dell'inserimento dell'informazione, non si deve essere obbligati a predefinire in modo rigido i vincoli e le modalità in cui essa entra nel sistema;
- nel reperimento dell'informazione, non si deve essere obbligati a predefinire in modo rigido, né la modalità con cui essa viene ottenuta, né limitare le informazioni derivabili da essa.

Per ottenere questi scopi, si devono distinguere : 

- chi chiede di introdurre l'informazione e chi la introduce;
- chi chiede di reperire un'informazione e chi la reperisce.

In questo modo si ottiene il beneficio di centralizzare il punto in cui l'informazione viene immessa o ritornata :  quindi un suo miglioramento o modifica viene immediatamente recepito da tutto il sistema informativo.
Per cogliere pienamente i benefici di questo approccio, si deve pensare poi al colloquio a più livelli :  chi ritorna  l'informazione può, a sua volta, avere la necessità di richiederne altre, per completare la risposta (es. :  a chi ritorna il valore di un ordine, se estero, serve la valuta del giorno corrente).
Si deve, d'altra parte, rendere il dialogo uniforme per non dover variare la parte della richiesta, nonostante possa cambiare il modo di soddisfarla.
Nasce quindi l'esigenza di definire delle entità su cui basare le azioni di inserimento e di reperimento delle informazioni, che in Sme.up corrispondono agli _2_"Oggetti Applicativi".

Un oggetto applicativo è l'elemento a cui si fa riferimento, sia nell'inserimento, sia nel reperimento delle informazioni.
Gli Oggetti risiedono permanentemente nel sistema e sono le entità con cui gli utenti interagiscono quotidianamente :  gli articoli, gli ordini, i movimenti di magazzino.
In Sme.up abbiamo definito altri oggetti, di significato meno evidente, al fine di sfruttare l'uniformità dell'approccio. Ad esempio, definiamo "oggetto applicativo" la memorizzazione di un video utilizzato per raggruppare vari parametri di esecuzione.
Ogni oggetto è individuato dalla classe di appartenenza (in Sme.up corrisponde al >"tipo") e per alcune classi si identifica anche la sottoclasse (In Sme.up è il >"parametro") e dall'identificativo, che è univoco all'interno della classe stessa.

Esempi di classi sono : 

- gli articoli (il tipo è 'l'Articolo', mentre l'identificativo è il codice dell'articolo);
- le bolle (il tipo è 'Documento Esterno',  il parametro è 'Bolla e l'identificativo è il numero di bolla);
- le fatture  (il tipo è sempre 'Documento Esterno',  il parametro è 'Fattura e l'identificativo è il numero di fattura).


![BLV0001-02](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-02.png)>Figura 2 - Schema Dettagliato degli Oggetti Applicativi in Sme.up

Nell'inserimento delle informazioni di un oggetto la classe interviene nei seguenti modi : 

- si possono definire, a livello di classe, delle azioni eseguibili all'atto dell'inserimento, variazione, copia e annullamento di un oggetto;
Sono inoltre definite delle funzioni sia specifiche della classe, sia generali (in questo caso con comportamento polimorfo), tramite le quali si eseguono variazioni ai singoli attributi di un oggetto (es. :  la variazione di stato della riga di un ordine viene eseguita tramite una funzione generale che controlla l'ammissibilità del passaggio di stato definita a livello di classe).


![BLV0001-03](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-03.png)> Figura 3 - Albero e Legenda


- nel reperimento delle informazioni di un oggetto :  per ogni classe esistono, infatti, degli attributi primari, reperibili tramite un'interfaccia predefinita;
- si possono definire liberamente ulteriori attributi, inseriti direttamente dall'utente, e configurare attributi derivati, impostandone la modalità di reperimento.
Un esempio della combinazione di questi due ultimi casi è il seguente :  si definiscono due nuovi attributi nella classe articolo, che sono la lunghezza e la larghezza. Si definisce un ulteriore attributo, dato dal prodotto dei due precedenti, che, nel caso in cui l'articolo sia una lamiera, ne definisce l'area.
È importante sottolineare che tutti gli attributi, compresi i primari, sono reperibili singolarmente in un'unica modalità.


![BLV0001-04](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-04.png)Oggetti applicativi JAVA

Esempi di parametro di tipo

## Un Software a Oggetti Applicativi
### Introduzione
Sme.up è un software ERP a oggetti applicativi. Dato che la sigla ERP (Enterprise Resource Planning) è diventata abbastanza familiare nel mondo dell'informatica, iniziamo con l'esposizione di che cosa intendiamo per 'software ad oggetti applicativi'.

### Un po' di Storia
Negli ultimi dieci anni il termine "object oriented" è entrato in modo pervasivo nell'informatica,ma la sua valenza principale è stata tecnologica. Si parla di linguaggi object oriented più o meno puri (C++, Smalltalk, Eifel, Java), ma la potenzialità del paradigma Object Oriented è stata in qualche modo limitata.
Esso non era nato per scrivere software in modo più rapido ed efficiente, ma traeva la sua origine dagli studi di intelligenza artificiale di rappresentazione della conoscenza, per meglio emulare con strumenti logico-informatici la rappresentazione del mondo che ognuno di noi si costruisce nella propria mente.
Chi volesse approfondire questi temi, può consultare il paragrafo seguente, che riporta un estratto del volume _R_'Intelligenza artificiale' di D. Fum.

### Sme.up e l'Object Oriented
Nella piccola fetta di realtà che ha a che fare con i sistemi gestionali, vale a dire la rappresentazione delle informazioni e degli eventi all'interno di un'azienda di produzione o servizi, ci è sembrato utile riferirci alla rappresentazione mediante oggetti per sfruttarne la potenza applicativa :  questa è l'origine del termine _2_'oggetti applicativi'.
Gli oggetti applicativi sono le realtà formali con cui l'organizzazione aziendale ha a che fare nella quotidianità :  gli articoli, i clienti, gli ordini, le bolle.
Trattarli come oggetti, in modo astratto, indipendentemente dalla loro specificità, dà una serie di vantaggi : 

- Abbiamo realizzato un insieme di funzioni generali, valide per tutti gli oggetti, secondo i principi del polimorfismo. Un esempio sono le note strutturate, vale a dire una gestione commenti (con alcune funzionalità di text editor), collegabili in modo automatico a tutti gli oggetti (esistenti e futuri). Un nuovo oggetto quindi non nasce 'nudo', ma già corredato di queste funzioni, con evidenti vantaggi di modularità e uniformità.

- Si possono realizzare strutture a contenuto generalizzato, che non contengono solo il codice dell'oggetto, ma anche il suo tipo (l'informazione che esso è un articolo, un cliente).
La corrispondenza con i termini classici object oriented è la seguente : 
-- tipo oggetto = classe
-- codice oggetto = istanza
Ad esempio, nelle righe dei documenti (ordini, bolle), si può scegliere l'oggetto intestatario della riga stessa, che non è obbligatoriamente un articolo, ma può essere una prestazione o una spesa.
Un esempio più articolato è la distinta base, intesa come struttura che lega due oggetti qualsiasi, non necessariamente articoli. Se si decide di trattare i dipendenti, essa diventa lo strumento con cui si rappresenta l'organigramma aziendale.

- Ogni oggetto è visto dal resto dell'applicazione in un unico modo, tramite un'interfaccia pubblica, mentre la sua struttura privata di reperimento delle informazioni è inaccessibile (realizzando, in termini object oriented, l'incapsulamento).
Questo approccio controllato al passaggio delle informazioni ha una conseguenza rilevante :  Sme.up può trattare informazioni di altre applicazioni, senza duplicazione di dati. È sufficiente realizzare la struttura privata di reperimento delle informazioni e restituirle secondo le convenzioni definite dall'interfaccia pubblica.
Non vale necessariamente il contrario :  gli oggetti Sme.up possono essere visti da un'altra applicazione solo se essa è realmente object oriented e prevede a sua volta un'interfaccia pubblica, a cui Sme.up dovrà adeguarsi.
Un esempio concreto di questa impostazione è l'applicazione di controllo qualità >Q9000 :  essa convive con qualsiasi prodotto gestionale di cui vede articoli, clienti, fornitori,  ordini di vendita, di acquisto e di produzione.

- Ragionare per oggetti porta inoltre a realizzarne di meno evidenti, con la costruzione di una forma mentale che ci spinge a cercare 'oggetti' in ogni nuova realizzazione, con vantaggi di uniformità ed astrazione.
Un esempio è l'oggetto >arrotondamento, che definisce gli scaglioni (limite inferiore e superiore) e il modo di arrotondare per ognuno di essi. L'insieme di queste informazioni viene intestato ad un codice arrotondamento, a cui ci si può riferire, ad esempio, nella variazione dei valori di un listino.
In sostanza, la richiesta da parte delle aziende di sempre nuove informazioni e di rappresentazioni di processi sempre più sofisticati e complessi, ci ha fatto concludere che il terreno su cui i sistemi gestionali si confrontano è quello della loro potenza applicativa intrinseca :  non, o non solo, il numero di funzioni implementate o di informazioni presenti, ma la possibilità di implementarne di nuove e aggiungere nuove informazioni, con il minor sforzo possibile, disponendo di una struttura di base sufficientemente rigorosa, ma malleabile, che ne permette la realizzazione.
(_R_Crf. Oggetti Applicativi, per una descrizione più approfondita di questi temi).

Una conferma della validità del nostro approccio è stato il fatto che l'utilizzo degli oggetti applicativi tramite la tecnologia Java (nel mondo web-based) è stato ottenuto in modo semplice e diretto :  un oggetto applicativo, appena creato sull'AS/400, è immediatamente visibile nel mondo Internet.

### I Must di Sme.up
Le "parole d'ordine" di Sme.up sono : 

- **Astrazione**
Se due funzioni presentano forti similitudini, è meglio farle diventare due casi particolari di un'altra, più generale. Eliminando del codice senza ridurre le funzionalità è tanto utile quanto introdurre una nuova funzionalità.

- **Modularità**
Una funzione va implementata in un solo programma :  in tutto Sme.up c'è un unico punto in cui è realizzata la gestione delle note di un oggetto, con vantaggi per chi deve modificarla / estenderla, o per chi deve comprenderla.

- **Parametrizzazione**
Se una funzione può avere comportamenti diversi, non prefissarne uno in modo aprioristico, ma farlo decidere all'utente, o a chi imposta il sistema, ottenendo l'ulteriore beneficio di rendere le scelte il più possibile evidenti, e non nascoste nel codice.
Ad esempio, nella pianificazione materiali, si può scegliere se trattare i giorni solari oppure il calendario aziendale in modo separato per i suggerimenti di produzione, acquisto e lavorazione esterna.

- **Ereditarietà**
Le informazioni vanno inserite al livello di sintesi più alto possibile, per eliminarne la ridondanza.
Ad esempio, se tutti gli articoli di una certa classe hanno lo stesso tempo di approvvigionamento,si inserisce l'informazione a livello di classe, conservando la possibilità di definirlo, come eccezione, a livello di un singolo articolo.

- **Libertà**
Non costituire vincoli impliciti, che possono limitare i comportamenti (ovviamente con la possibilità di costruirne in modo esplicito, tramite la parametrizzazione) :  un comportamento che sembra privo di significato, in certe situazioni può diventare utile.
Es. :  Tra i parametri di pianificazioni materiali ci sono il lotto minimo e massimo, che identificano la quantità minima da produrre e la quantità massima che si produce contemporaneamente. Non vi è alcun controllo che il lotto mimino sia inferiore al lotto massimo. Si può decidere, ad esempio, che non si producano mai meno di 100 pezzi (lotto minimo), a gruppi di 10 (lotto massimo).

- **Specificità**
Nessun prodotto di gestione aziendale può ritenersi omnicomprensivo e immodificabile :  spesso delle specificità non sono realisticamente riconducibili a funzioni standard. Per superare questo scoglio abbiamo realizzato programmi di exit strutturati in ogni punto, in cui si può decidere di estendere o modificare il comportamento del software. In questo modo, per implementare determinati comportamenti, si scrive ">nuovo codice personale" invece di personalizzare il codice esistente.
Questo ha numerosi vantaggi : 
-- realizzazione di piccoli programmi orientati alla soluzione del problema, che non interferiscono con il resto del codice e diventano un'autodocumentazione dei comportamenti specifici dell'azienda, accessibile al personale tecnico;
-- essendo il richiamo delle exit comandato in tabella, il comportamento dell'applicazione è confrontabile in presenza e assenza della exit stessa;
-- l'installazione di nuovi rilasci risulta velocizzata, non essendo necessario riportare le personalizzazioni sulla nuova versione del codice. È naturalmente nostra cura mantenere inalterata la modalità di richiamo delle exit.
Un esempio è il programma di controlli aggiuntivi all'inserimento e variazione dell'anagrafica articoli, in cui si possono eseguire sia controlli incrociati sia semantici;
-- uniformità di colloquio tra le varie funzioni, per permetterne la composizione in modo nativo;
-- rappresentazione 'profonda' dei fenomeni aziendali :  cogliendone la reale struttura, nuove esigenze possono essere già contemplate, perché sono manifestazioni diverse di uno stesso disegno concettuale.


### Conclusioni
Tutto questo non è solo object oriented, ma il rigore con cui va affrontato questo paradigma spinge ad affrontare in modo altrettanto rigoroso tutti gli aspetti del concepimento e della realizzazione del software applicativo.
In conclusione, Sme.up è un insieme di oggetti, moduli, funzioni e impostazioni, che permettono di modellare in modo diversificato e potente gli aspetti organizzativi e gestionali delle aziende e quindi supportarle nella sfida della complessità che esse devono affrontare, giorno dopo giorno,per la loro stessa sopravvivenza nel mercato.

### Frame e Slot
Riportiamo i seguenti paragrafi (pagg. 212 / 223) tratti dal volume _R_"INTELLIGENZA ARTIFICIALE - Teoria e Sistemi", Editrice Il Mulino 1994, del Prof. Danilo Fum (Dipartimento di Psicologia dell'Università degli Studi di Trieste), che ringraziamo per la gentile concessione alla pubblicazione dei suddetti paragrafi.

3. Frame
Un formalismo che presenta diversi punti di somiglianza con le reti semantiche è costituito dai cosiddetti frame. È difficile dire chi abbia avuto per primo l'idea di usare queste strutture per rappresentare le conoscenze necessarie a supportare i complessi processi che stanno alla base di attività come l'elaborazione del linguaggio naturale, la visione artificiale e simili. Molti dei principi che stanno a fondamento di questo formalismo erano in qualche modo già noti quando Marvin Minsky [1975] pubblicò il lavoro che viene generalmente riconosciuto come il "manifesto" della teoria dei frame. Selz [1922] e Bartlett [1932] avevano infatti da tempo introdotto in psicologia il concetto di "schema". Nell'IA, come ricorda lo stesso Minsky, idee simili erano state in qualche modo prefigurate da Abelson [1973],  Newell e Simon [1972], Norman [1973] e Schank [1973].
In quello che è universalmente noto come il frame paper, Minsky cerca di dare una veste sistematica a tutte queste idee proponendo il nucleo di una teoria coerente e unificata.
Ecco l'essenza della teoria. Quando si incontra una nuova situazione (o si cambia in modo sostanziale il proprio punto di vista riguardo il problema corrente) si sceglie dalla memoria una struttura, detta frame. Questa rappresenta un quadro di riferimento da adattare per adeguarsi alla realtà, modificandone i dettagli, come necessario. Un frame è una struttura dati che viene utilizzata per rappresentare delle situazioni stereotipate, come trovarsi in un certo tipo di soggiorno o partecipare a una festa di compleanno per bambini. Attaccati a ciascun frame vi sono diversi tipi di informazioni, alcune delle quali riguardano il modo di usarlo; altre riguardano che cosa potrebbe accadere in seguito; altre ancora guidano su cosa fare qualora queste aspettative non venissero confermate. [Minsky 1975, 212]
L'idea di frame trae origine dall'osservazione che le persone usano un insieme strutturato di conoscenze - derivate dalle loro esperienze precedenti con oggetti, luoghi, persone, ecc... - per interpretare le diverse situazioni da affrontare. In una situazione nuova, gli individui non partono da zero, ma, al contrario, recuperano dalla loro memoria una rappresentazione a carattere generale (un frame, per l'appunto), che viene poi raffinata e modificata per render conto dei dettagli della situazione corrente.
Un frame è dunque la struttura che costituisce le conoscenze generali che un individuo ha riguardosituazioni, luoghi, oggetti e personaggi stereotipati. Essa fornisce una cornice concettuale in cui i nuovi dati vengono interpretati, alla luce delle conoscenze derivate dall'esperienza precedente.
Ad esempio, andando per la prima volta in un nuovo ristorante, non siamo del tutto spaesati, ma, in un certo senso, sappiamo già quello che vi troveremo (ci aspettiamo di vedere tavoli, stoviglie, camerieri e sappiamo già anche quello che, grosso modo, accadrà nel ristorante :  un cameriere porterà la carta, noi la leggeremo e ordineremo del cibo).
Tutto questo insieme di conoscenze strutturate usate nell'affrontare la nuova situazione, costituisce un frame. In altre parole, abbiamo attivato nella nostra base di conoscenze un frame «ristorante» che controlla il modo nel quale interpretiamo la situazione che stiamo per affrontare.

L'utilizzo dei frame permette a un sistema di avere delle aspettative. Se, una volta aperta la porta, trovassimo in mezzo alla sala del ristorante una poltrona da dentista rimarremmo sconcertati e non sapremmo come interpretare tale anomalia.
L'utilizzo dei frame può inoltre aiutare il processo di interpretazione di situazioni ambigue. Ad esempio, un oggetto metallico con le impugnature divaricate, anche qualora fosse parzialmente coperto da un tovagliolo, verrebbe ugualmente riconosciuto come uno schiaccianoci, mentre lo stesso oggetto, coperto da uno straccio su un bancone di officina, verrebbe probabilmente preso per una pinza. L'ipotesi che i sistemi intelligenti siano guidati da un ricco insieme di aspettative nella loro interazione con il mondo, permette di spiegare molti dei loro comportamenti. I frame servono per l'appunto ad organizzare le conoscenze relative ad un dato dominio, in modo da facilitare il reperimento delle informazioni e i processi inferenziali necessari per agire in modo intelligente.
Sebbene gli esempi riportati nel frame paper fossero ugualmente divisi fra percezione e linguaggio- e Minsky considerasse i frame come strutture necessarie per supportare entrambi i tipi di processi - le applicazioni basate su frame riguardanti il linguaggio sono risultate in numero molto maggiore rispetto a quelle dedicate alla percezione. In particolare, gran parte della ricerca teorica sui frame è stata condotta nel contesto della comprensione di storie. Come esempiodi processi di riconoscimento, interpretazione e predizione derivati dall'uso dei frame, consideriamo le due sequenze di frasi sotto riportate, adattate da Schank e Abelson [1977] : 

- **Sequenza A**. Giacomo andò al ristorante. Chiese al cameriere una bistecca con patatine. Pagò il conto ed uscì.
- **Sequenza B**. Giacomo andò al parco. Chiese al nano un topolino. Prese la scatola e se ne andò.

Sebbene siano costituite da frasi paragonabili per struttura sintattica e complessità semantica, considerate da un punto di vista globale, le due sequenze risultano molto differenti. Mentre la sequenza A ha un senso compiuto e risulta facilmente comprensibile, la sequenza B, pur dotata di significato, provoca un senso di disorientamento. Questo è dovuto al fatto che, nel comprendere lasequenza A, è possibile accedere ad una struttura di conoscenza ad alto livello (il frame del ristorante - o meglio, lo script (copione), nella terminologia di Schank e Abelson [1977] - che integra e organizza le varie frasi). Nel caso di B, invece, una tale struttura non è immediatamente disponibile e le singole informazioni risultano più difficili da collegare.
Utilizzando strutture di questo tipo, Schank e collaboratori (_R_Crf Schank e Riesbeck [1981])costruirono SAM (Script Applier Mechanism), un programma in grado di rispondere a domande come «Giacomo è stato in piedi o seduto?», «Cosa ha mangiato Giacomo?» relative a informazioni non esplicitamente menzionate nelle storie, di tradurre le storie da una lingua all'altra, di riassumere il contenuto delle stesse.
SAM e numerosi altri programmi di elaborazione del linguaggio naturale si basano proprio su strutture a frame che supportano i processi inferenziali necessari alla comprensione del testo.

_2_NB. :  I frame, uguali in ciò alle reti semantiche, sono strutture che rappresentano le conoscenze in modo dichiarativo, ma privo di semantica formale. Quando si parla di frame bisogna quindi presupporre l'esistenza di procedure in grado di utilizzare le informazioni in essi contenute e di eseguire i processi inferenziali necessari per riconoscere un oggetto, comprendere un testo in linguaggio naturale o altro ancora. I frame non sono comunque strutture esclusivamente dichiarative; in essi, come vedremo, è possibile inserire anche conoscenze di tipo procedurale. Conoscenze dichiarative e procedurali sono intimamente connesse all'interno di un frame e ciò permette di dar vita a computazioni flessibili ed estremamente efficienti.
Nell'articolo sopra citato, Minsky dà solo vaghi suggerimenti circa il tipo di entità che i frame rappresenterebbero. Il suo lavoro è oggi (giustamente) famoso più per le intuizioni e gli spunti in esso contenuti che per una precisa descrizione di metodologie e tecniche in grado di supportare i diversi tipi di processi inferenziali. Egli concepi l'idea di organizzare i frame in un sistema costituito da un insieme di oggetti correlati tra loro in una struttura gerarchica, rappresentabile in forma di rete; introdusse gran parte della terminologia oggi utilizzata e, soprattutto, diede vita ad una tradizione di ricerca, che ben presto si divise in due linee distinte. Da un lato, infatti, vi furono coloro che si preoccuparono di approfondire gli aspetti teorici dei frame e del loro uso; dall'altro vi fu chi si interessò soprattutto di sviluppare dei linguaggi in grado di implementare in modo efficiente strutture di questo tipo. Analogamente a quanto succede per le reti semantiche, non è possibile parlare oggi di una teoria generale dei frame. Esistono diversi sistemi basati su frame che recepiscono istanze teoriche differenti e si diversificano l'uno dall'altro per aspetti anche sostanziali.
La descrizione che segue cerca di cogliere i tratti comuni alla maggior parte di questi sistemi.

3.1. Frame e rappresentazione delle conoscenze
I frame sono stati originariamente concepiti come strutture dati per rappresentare situazioni stereotipate e oggetti tipici. È interessante chiedersi come queste stesse conoscenze siano organizzate negli essere umani.
Come rilevato dagli studi della Rosch e collaboratori [_R_Crf. Rosch 1975; Rosch e Lloyd 1978],le persone organizzano in modo naturale i loro concetti in tre livelli gerarchici : 

- un livello che potremmo chiamare di base;
- un livello superordinato;
- un livello subordinato.

Cosi, per fare un esempio, il concetto di «sedia» è un concetto di base, il concetto di «mobile» è superordinato rispetto a quello di sedia, mentre «sedia_a_dondolo» rappresenta un caso di concetto subordinato. I concetti di base costituiscono il modo naturale di categorizzare gli oggetti e le entità del nostro mondo :  essi rappresentano le prime categorie che gli esseri umani apprendono, mentre gli altri concetti vengono acquisiti in un momento successivo e derivano da un'evoluzione delle categorie di base. Così i concetti superordinati traggono la loro origine da una generalizzazione di tali categorie mentre i concetti subordinati provengono da una loro specializzazione. Una volta formatesi, le varie categorie tendono ad avere una struttura che accentua la somiglianza fra i membri della medesima categoria e rende massime le differenze fra membri appartenenti a categorie diverse.
Non tutti i membri di una categoria sono però uguali fra loro. Secondo la Rosch, le categorie concettuali utilizzate dagli esseri umani non hanno confini fissi e definiti. I concetti «naturali» (tazza, sedia, albero, ecc...), a differenza dei concetti «artificiali» che si incontrano per esempio nelle scienze (triangolo rettangolo, forza, differenza di potenziale, ecc...), non possono venir definiti, aristotelicamente, mediante genus et differentia, per cui non è sempre agevole stabilire se un esemplare sia o meno un membro di una data classe. L'appartenenza categoriale non viene cioè caratterizzata mediante un elenco di attributi necessarie sufficienti, ma nei termini di una maggiore o minore somiglianza rispetto a membri tipici della categoria (o prototipi). Così, un passero rappresenta un miglior esemplare della categoria di «uccello» rispetto ad un airone e quest'ultimo, a sua volta, è più «uccello» di uno struzzo. Dal momento che un uccello prototipo vola, noi siamo normalmente portati a considerare la proprietà di volare come tipica di tali animali mentre il possedere una tale capacità non è una condizione nè necessaria né sufficiente per essere definito un uccello (esistono infatti, come sappiamo ormai molto bene, uccelli che non volano e animali che volano senza essere uccelli).
Queste idee della Rosch, relative al modo in cui i concetti vengono rappresentati nella memoria semantica degli individui, sono state recepite in misura più o meno rilevante nei linguaggi di rappresentazione dei frame. KRL [Bobrow e Winograd I977; 1979] e NETL [Fahlman 1979] per esempio, permettono di rappresentare il concetto di membro tipico di una data classe. Associata al frame «uccello», potremo cosi avere in tali linguaggi la descrizione di alcuni esemplari tipici di uccelli, come i passeri o le rondini. KRL tiene inoltre conto della tassonomia che distingue fra categorie di base, superordinate e subordinate e rappresenta queste classi mediante tipi di dati diversi. In altri sistemi, invece, tale distinzione non gioca alcun ruolo.
In generale, comunque, tutti i sistemi di frame permettono di ragionare intorno a classi di oggetti usando delle rappresentazioni prototipiche che, valide in linea di massima, hanno bisogno di venir talvolta adattate e modificate per considerare la complessità del mondo reale, in cui le eccezioni abbondano e i confini tra le diverse classi risultano spesso sfumati. Tutti i sistemi di frame, inoltre, organizzano le conoscenze in strutture gerarchiche i cui elementi sono collegati fra loro da relazioni tipo isa o ako (a kind of), che consentono la trasmissione ereditaria delle proprietà. Le proprietà dei frame ad alto livello restano fisse, in quanto rappresentanti fatti che sono tipicamente veri per la classe di oggetti o di situazioni presi in considerazione, mentre i livelli più bassi, che corrispondono a sottoclassi o ad istanze individuali, possono essere contraddistinti da proprietà specifiche, magari in contrasto con quelle delle superclassi.
Per quanto riguarda la distinzione fra classi ed individui va fatto notare come essa non sia sempre «naturalmente» determinata - tipo :  Fido è un individuo mentre setter è una (sotto)classe - ma come essa dipenda invece spesso dal livello al quale si intenda manipolare i diversi tipi di conoscenze. Cosi in un sistema di diagnosi medica, i pazienti verranno considerati come classe ed ogni singolo ammalato verrà considerato come un'istanza particolare di tale classe. Un tipo di organismo, per esempio un agente patogeno, verrà invece classificato come istanza e non come classe anche se esistono milioni di diversi individui di quel determinato tipo. Il motivo di questa scelta risiede nel fatto che, mentre siamo interessati alle caratteristiche individuali di ogni paziente, non abbiamo alcun interesse a raccogliere informazioni specifiche riguardanti ciascun singolo batterio. Essendo la distinzione tra classi e individui in un certo senso arbitraria, parleremo semplicemente di oggetti qualora non si voglia esplicitamente distinguere fra i nodi terminali della gerarchia (individui) ed i nodi che stanno in posizione intermedia (classi).
3.2. Struttura dei frame
Un frame è dunque una struttura che raccoglie ed unifica le conoscenze che si hanno a disposizione su un determinato oggetto (istanza o classe) del dominio. Ogni frame ha ovviamente un nome il quale identifica in maniera univoca l'oggetto che esso rappresenta. Per restare all'esempio del sistema di diagnosi medica, paziente e cultura-batterica possono essere nomi di classi di oggetti mentre anna_giorgi o pseudomonas rappresentano nomi di specifici oggetti individuali. In un dominio diverso, potremmo avere i frame ristorante, pizzeria e bella_napoli per rappresentare rispettivamente una classe, una sua sottoclasse e un'istanza di quest'ultima.
Un frame rappresenta le caratteristiche dei vari oggetti mediante un insieme di slot, che può essere interpretato come una casella nella quale inserire un determinato tipo di informazione. Ad esempio, il frame ristorante può avere slot relativi alla categoria, indirizzo, giornata di chiusura, tipo di cucina, numero di «stelle», carte di credito accettate, numero di coperti, costo medio di un pasto, ecc...
Dato un particolare frame, i valori dei suoi slot possono essere noti o meno (possiamo conoscere il nome e l'indirizzo di un ristorante, ma non il giorno di chiusura) e talvolta, pur senza conoscere l'esatto valore di uno slot, è possibile fare delle supposizioni che, in mancanza di informazioni specifiche più dettagliate, possiamo ritenere vere, fino a prova del contrario.

![BLV0001-08](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-08.png)>Fig. 5.15. Struttura di un frame

I valori per default vengono usati come valori provvisori e approssimativi in assenza dei valori reali. Alcuni sistemi di frame ammettono la possibilità per uno slot di avere sia un valore reale sia un valore per default. In tale caso, ovviamente, il valore reale prevale su quello default. I valori per default possono essere associati direttamente ad un determinato slot e venir specificati durante la creazione del frame stesso, oppure, più comunemente, possono derivare da frame a livello superiore mediante il meccanismo dell'eredità :  se il valore cercato è specificato (come valore reale o per default) nel frame in questione, allora esso è immediatamente disponibile; in caso contrario si accederà allo slot con lo stesso nome di un frame di livello gerarchico più elevato e, posto che il valore venga trovato, esso si trasmetterà di padre in figlio. Così, ad esempio, il fatto che lo slot dieta compaia sia nel frame anna_giorgi sia nel frame paziente indica che Anna Giorgi ha una sua dieta personalizzata, mentre lo slot di paziente serve a contenere le prescrizioni valide per quelle persone che non hanno esigenze o necessità specifiche.


![BLV0001-09](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-09.png)>Fig. 5.16. Una gerarchia di frame

In base a quanto rappresentato nella figura, Anna Giorgi osserva una dieta individualizzata ipocalorica, mentre Maria Bianchi segue la dieta normale. Dal canto suo, Maria Bianchi soffre di una specifica allergia al polline, mentre per Anna Giorgi non si dispone di alcuna informazione a questo riguardo, nemmeno sfruttando il meccanismo dell'eredità. La conoscenza che Anna Giorgi e Maria Bianchi sono femmine deriva per eredità dallo slot sesso del frame paziente. Se il nostro sistema fosse installato in un reparto di ostetricia e ginecologia questo sarebbe un assunto realistico. E, supposto che in tale reparto venisse ricoverato un uomo (supponiamo per far fronte ad un'emergenza nel caso in cui non vi fossero più posti disponibili in altri reparti, sarà sempre possibile registrare il valore maschio nello slot sesso di tale paziente. La gerarchia illustrata nella figura è una struttura arborea :  ogni figlio ha infatti un unico padre. In questo caso il processo di eredità delle proprietà avviene senza problemi. Alcuni sistemi di frame ammettono la possibilità di avere eredità multipla e, di conseguenza, possibili conflitti fra i valori ereditati. I diversi sistemi si differenziano per il modo nel quale viene gestito tale meccanismo di ereditarietà. I più flessibili permettono di scegliere la strategia di ricerca (profondità vs. ampiezza), di limitare il numero di livelli entro i quali va cercato il valore desiderato, di definire un frame universale che viene consultato sempre e comunque, e cosi via.
Finora abbiamo preso in considerazione dei casi in cui i valori di uno slot (reali o per default che fossero) erano sempre di tipo elementare. Può risultare utile, per certe applicazioni, ammettere la possibilità per uno slot di avere come valore delle strutture complesse. In questo caso lo slot non registrerà direttamente il valore desiderato ma includerà un puntatore ad un altro frame nel quale si troveranno le informazioni volute.

![BLV0001-10](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-10.png)>Fig. 5.17. Frame come valore di uno slot

Oltre ad una parte dichiarativa, i frame possono avere anche una parte procedurale e, in particolare, è possibile attaccare ai vari slot delle procedure (pezzi di codice), in modo da rendere la computazione più efficiente. Abbiamo già visto come, in mancanza di un valore reale, il contenuto di uno slot possa essere stabilito ricorrendo all'eredità o ad un valore per default. Eredità e default rappresentano dei metodi relativamente semplici per determinare i valori di uno slot. Questi metodi generali possono venir però integrati da conoscenze specifiche sul dominio e da euristiche particolari. Un modo per sfruttare queste euristiche consiste nel far ricorso alle cosiddette procedure if-needed, che codificano dei metodi ad hoc mediante i qualiè possibile determinare il contenuto di uno slot qualora ciò sia richiesto dal processo di elaborazione in corso. Ad esempio, invece di inserire direttamente il dato relativo all'età di un paziente, lo slot età di ogni singolo frame di tipo paziente può far riferimento (mandandolo in esecuzione) ad un pezzo di programma che calcola tale età sottraendo l'anno di nascita del paziente dall'anno in corso.
Un altro tipo di attaccamento procedurale che si può avere in un frame è costituito dalle procedure if-added (dette talvolta anche demoni). Anche queste procedure sono associate agli slot e rimangono silenti finchè non si tenta di riempire con un qualche valore lo slot al quale sono attaccate. In questo caso le procedure vengono mandate in esecuzione, controllando che il valore in questione soddisfi certi vincoli o requisiti stabiliti a priori in base a conoscenze specifiche del dominio.
Esistono anche altri tipi di attaccamenti procedurali (alcuni sistemi, per esempio, permettono di definire delle procedure if-removed, in grado di eseguire determinate operazioni qualora si intenda cancellare o sostituire il valore di uno slot).

![BLV0001-11](http://localhost:3000/immagini/B£OGAT_ARC/BLV0001-11.png)>Fig. 5.18. Attaccamenti procedurali ad uno slot

C'è ancora un punto da mettere in rilievo. Come abbiamo visto, le informazioni che entrano a far parte di uno slot possono essere di tipo diverso :  possono infatti rappresentare dei valori reali, valori per default, puntatori ad altri frame, nomi di procedure di diverso tipo. È necessario che il sistema sappia come interpretare ciascuna di queste informazioni, in modo da tenere sempre un comportamento adeguato. Il modo nel quale va interpretato il contenuto di uno slot ne indica l'aspetto (o facet), definito associando allo slot un'etichetta che ne identifichi il tipo.

3.3. Frame, logica e oggetti
I frame, come le reti, non hanno una semantica formale, perciò risulta difficile paragonare fra loro le caratteristiche dei diversi sistemi di frame. A questo riguardo sono stati fatti numerosi tentativi di «tradurre» i frame nel linguaggio del calcolo dei predicati e di formalizzare i processi di eredità delle proprietà.
Nelle discussioni riguardanti l'argomento frame vs. logica - cosi come capitava nelle discussioni reti semantiche vs. logica - non è raro trovare affermazioni sul fatto che i frame rappresenterebbero, nel caso migliore, delle varianti notazionali di qualche dialetto della logicae, nel caso peggiore, delle notazioni vaghe e inconsistenti. C'è stato chi ha preso queste osservazioni in positivo ed ha iniziato a considerare i frame come strutture di rappresentazione ad alto livello alle quali, volendo, è possibile fornire una semantica formale traducendole in termini di logica. In questo modo, si è pensato di trarre il massimo vantaggio dai due formalismi,coniugando l'espressività di un linguaggio ad alto livello con il rigore della logica. In effetti, molti dei sistemi di frame si sono trasformati oggi in sistemi ibridi, che comprendono sia una parte logica sia una parte strutturata ad oggetti.
Un'altra linea di sviluppo che è possibile intravedere per i sistemi di frame è quella che li vede confluire nei cosiddetti linguaggi di programmazione orientati agli oggetti (interamente object-oriented alla SMALLTALK, o che ammettono comunque un'estensione orientata agli oggetti tipoCLOS, C++ e simili). Un linguaggio di programmazione object-oriented utilizza delle gerarchie di classi di oggetti a cui sono associati degli slot per rappresentare variabili di stato e metodi in grado di manipolare tali variabili (e altri oggetti). I metodi e gli slot vengono ereditati attraverso la gerarchia di classi. Quando il programmatore dichiara che un oggetto rappresenta un'istanza di una data classe, tale oggetto viene ad acquisire l'insieme di variabili tipiche della classe stessa e ha accesso ai metodi ad essa associati.
Tutto sommato la distinzione che è possibile fare tra sistemi di frame e linguaggi orientati agli oggetti riguarda più una differenza di accento che questioni sostanziali. Mentre un linguaggio orientato agli oggetti costituisce un reale linguaggio di programmazione in grado di competere con i linguaggi tradizionali, i sistemi di frame tendono a venir usati solo a livello sperimentale per la costruzione di basi di conoscenze.
