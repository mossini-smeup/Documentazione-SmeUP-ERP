 :  : TIT Approvvigionamenti
# Obiettivo
L'obiettivo degli Approvvigionamenti è procurare, dall'esterno all'azienda, i materiali e i servizi che servono al funzionamento dell'azienda stessa. Sme.UP supporta questo processo per ottenere il corretto bilanciamento delle esigenze di qualità, tempestività ed economicità da un lato e la efficienza e completezza di gestione delle attività esecutive.

# Contesto
In un'azienda gli approvvigionamenti sono al centro di un gruppo di processi che vede : 
 * la determinazione del fabbisogno dei materiali necessari alla produzione e alla commercializzazione che devono essere procurati all'esterno. Generalmente tale fabbisogno viene determinato da un sistema di pianificazione e/o gestione delle scorte.
 * le richieste di beni e servizi accessori necessari al funzionamento dell'azienda; che possono pervenire agli Approvvigionamenti attraverso varie strade. Quella più appropriata, all'interno di un ERP, è costituta dalle richieste di acquisto (RDA) e da un workflow di approvazione.
 * il conto lavoro con le sue particolarità ( conto lavoro di fase, l' approvvigionamento del terzista con i materiali di proprietà dell' Azienda necessari al terzista, trasferimenti di materiale di proprietà dell' Azienda da terzista a terzista, ... ) costituisce un processo a cavallo tra gli approvvigionamenti e la produzione in senso stretto.
 * fabbisogni e richieste accessorie vengono soddisfatte dal parco fornitori, con l'emissione di un ordine al fornitore o di "chiamate" su piani di consegne, nel quadro delle condizioni di fornitura contrattate. Tra questi processi possiamo elencare la qualificazione dei fornitori con la gestione delle loro informazioni anagrafiche, la determinazione dei prezzi di fornitura (listini) e delle modalità di pagamento ed in generale delle condizioni di fornitura (tempi di consega da rispettare, confezionamento, ...)
 * il risultato è il monitoraggio costrante della fornitura stessa ed in particolare delle attività conseguenti al ricevimento della fornitura effettiva dei beni e servizi, con il collegamento alla qualità per la verifica quantitativa e qualitativa, o la dichiarazione di approvazione del servizio reso, e la destinazione logistica della merce ricevuta. L'esecuzione della  fornitura si sviluppa ulteriormente nel controllo della "validità" della fornitura, con possibili esiti di accettazione (ok al pagamento, e conseguente registrazione contabile) o di contestazione nei confronti del fornitore che può dar luogo alla restituzione dei beni, ed eventuale blocco della fattura con richiesta di una nota di credito.
 * i processi vengono monitorati attraverso statistiche ed analisi che comprendono tutta la reportistica e gli strumenti associati al controllo dell'attività dei fornitori, alla misurazione della performance della funzione, alla pianificazione delle attività (portafoglio ordini, fatturato, vendor rating, analisi prezzi medi, budget di acquisto, ecc..).

![AAP_ACQ_01](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_01.png)
# Copertura funzionale
Sme.UP ha le applicazioni che possono supportare tutte le necessità di gestione relative alla funzione degli Approvvigionamenti : 
 * Gestione anagrafico fornitori
 * Dati aggiuntivi fornitori
 * Relazioni con i fornitori
 * Richieste di acquisto
 * Richieste di offerta e offerte
 * Listini di acquisto
 * Ordini di acquisto, di conto lavoro pieno, di conto lavoro di fase
 * Contratti
 * Ordini aperti e richieste di consegna
 * Budget degli acquisti
 * Gestione entrata merce - dichiarazione servizio reso
 * Controllo fatture passive
 * Gestione note di credito e note di debito
 * Gestione consignment stock
 * Analisi e report
 * Ordinato
 * Fatturato
 * Vendor rating
 * Puntualità e Ritardi
 * ...

## Gestione dati di anagrafica
Rappresenta l'insieme delle attività correlate alla creazione ed al mantenimento delle informazioni legate alle condizioni di fornitura. Tra i dati di anagrafica utilizzati negli approvvigionamenti possiamo menzionare : 
 * l'anagrafico fornitori con le sue estensioni e la gestione della gestione delle dichiarazioni d'intento
 * i listini di acquisto

### Gestione anagrafici fornitori
Dal punto di vista degli Approvvigionamenti nell'anagrafico fornitori vengono gestite le informazioni seguenti : 
 * dati identificativi :  ragione sociale, partita IVA, categoria, ecc...
 * dati ambientali :  lingua, valuta, indirizzo, ecc...
 * contatti :  nominativo, telefono, fax, e-mail, ecc...
 * dati pagamento :  tipo pagamento, banca, IBAN, codice SWIFT, ecc...
 * dati relazionali :  destinazioni, indirizzo corrispondenza, indirizzo contabile, vettore, ecc...
 * classificazioni :  categoria contabile, classe abilitazione, settore merceologico, ecc...
 * dati movimentazione merce :  consegna, spedizione, giorni chiusura, ecc...

![AAP_ACQ_01](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_01.png)
Nelle estensioni dei fornitori possiamo gestire altre categorie di informazioni quali :  lettere di esenzione, calendario alternativo, piani / livelli di campionamento forzati, documenti / allegati specifici, persone da contattare, indirizzi internet. Questi dati possono essere presenti o meno per ogni fornitore, inoltre possono essere un numero anche elevato a piacere per tipo superando la classica limitazione del numero di campi disponibile in un normale archivio anagrafico.
Attraverso la gestione dei dati fornitore/articolo è possibile mantenere informazioni specifiche per gli articoli acquistabili presso un fornitore (la percentuale di assegnazione, il codice e la descrizione propria che il fornitore assegna all'articolo, l'unità di misura di acquisto che potrebbe differire rispetto a quella utilizzata internamente, la quantità minima di acquisto, ecc.. ).
In Sme.UP è anche prevista le gestione delle dichiarazioni d'intento, che possono essere emesse verso i fornitori e possono essere di tipo : 
 * singolo
 * per un periodo
 * fino al raggiungimento di un determinato importo.

### Listini di acquisto
La gestione dei listini permette di associare a tre oggetti definiti in funzione dell'impostazione (fornitori, clienti, articoli, I listini prevedono la gestione della data di validità (iniziale e finale) e delle scale prezzi per quantità, oltre che la gestione dei prezzi in valuta. Nella gestione del listino è prevista la possibilità di passare automaticamente dall'informazione di dettaglio (es. prezzo di un articolo per un fornitore) a un livello di sintesi superiore (es. prezzo di una famiglia / classe di articoli valido per un fornitore). In aggiunta alle risalite automatiche sono previste delle "user exit" apposite che permettono di costruire il prezzo applicando regole specifiche, anche basate su elementi diversi con una propria dinamica di prezzi indipendente l'una dall'altra. Ad esempio il prezzo di un particolare in alluminio calcolato come quota di produzione a cui si somma la quota di materiale variabile in funzione del prezzo medio dell'alluminio.

### Approvazione suggerimenti MRP
L'MRP di Sme.UP genera suggerimenti di :  produzione, acquisto, o conto lavorazione. Nella generazione dei suggerimenti si possono applicare anche regole di attribuzione al fornitore preferenziale, di distribuzione a vari fornitori secondo quote di assegnazione, di collegamento a contatti in essere, o implementare strategie specifiche (ad esempio assegnazione per quantità :  sotto una certa soglia ad un fornitore, sopra ad un altro). È inoltre possibile definire lotti minimi e multipli di fornitura e tempi di approvvigionamento (a livello generale o per singolo fornitore). L'approvazione dei suggerimenti MRP di acquisto o di lavorazione può creare in automatico degli ordini o delle richieste di acquisto. L'approvazione può essere cieca oppure con richiesta del fornitore e/o dell'ordine a cui accodare le righe, l'approvazione prevede anche la possibilità di modificare la quantità rilasciata rispetto a quella suggerita.

### Richieste di acquisto
Si possono utilizzare sia per richiedere l'approvvigionamento di materiali di produzione che per l'acquisto di beni e servizi accessori. Possono essere viste come un particolare tipo di documento in cui la testata non è assegnata ad un unico fornitore ma all'azienda in generale. La richiesta di acquisto può essere soggetta ad un "workflow" con diversi livelli di approvazione e precorsi diversi costruiti sul processo e sull'azienda. Alla fine del workflow alle righe delle RDA viene applicato un flusso di estrazione che genera degli ordini di acquisto o di conto lavoro. L'utente che ha generato la RDA può in ogni momento controllare lo stato di avanzamento della sua richiesta e sapere in quale ordine di acquisto è sfociata, allo stesso modo dall'ordine di acquisto è possibile risalire alla RDA origine. Correlata alla gestione delle RDA possiamo avere anche la gestione delle richieste di offerta, estratte dalle richieste di acquisto ed inviate ad un gruppo di possibili fornitori, la ricezione delle offerte permette la costituzione dei listini.

## La gestione degli approvigionamenti
Si fonda su documento "ordine" che può essere : 
 * di acquisto, o di conto lavoro
 * un ordine chiuso oppure un ordine aperto / contratto seguito da delle richieste di consegna.
Nella gestione Sme.UP dell'ordine sono previste : 
 * le revisioni d'ordine, che possono essere suggerite dall'MRP oppure applicate manualmente
 * la gestione dei solleciti, sia per la conferma della data di consegna da parte del fornitore, sia per il sollecito dei materiali realmente necessari alla continuità dell'attività

### Ordine
In Sme.UP l'ordine viene gestito con il "documento", che è costituito da una testata e una o più righe : 
 * la testata è dedicata alla gestione dei dati relativi alla totalità del documento (numero documento, fornitore intestatario, riferimento esterno, buyer, data di emissione, modalità di fornitura, modalità di pagamento, ecc..)
 * le righe rappresentano l'oggetto dello scambio (articoli, servizi, materiali non codificati, ...) e indicano le quantità, le date ed i prezzi convenuti.

![AAP_ACQ_02](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_02.png)
### Tipizzazione
I documenti sono classificati secondo il "Tipo documento" che ne definisce la natura (un ordine, un contratto, una bolla, ecc...) e le caratteristiche di comportamento (controlli, sviluppi, influenza sui vari portafogli o registri, ..).

Il documento può rappresentare ad esempio : 
 * un contratto quadro
 * una richiesta di consegna (a fronte del contratto)
 * un ordine di acquisto materiali o di conto lavoro
 * un ordine di acquisto servizi
 * una bolla entrata merce
 * una bolla invio in conto lavoro
 * una bolla restituzione a fornitore o terzista
 * un benestare per servizio reso
 * ...

![AAP_ACQ_03](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_03.png)
Per ogni tipo documento diverso è possibile ottenere opportune statistiche e interrogazioni, produrre stampe, gestire manutenzioni. All'interno di un tipo documento le testate possono essere differenziate attraverso il "Modello documento" che rappresenta delle sotto-classificazioni necessarie per ragioni statistiche o di processo (es. acquisti nazionali piuttosto che CEE o ExtraCEE, oppure acquisti materiali per produzione o acquisti di servizi), il modello determina il tipo ed il layout di stampa del modulo di output. Nel documento (e di conseguenza all'interno di uno specifico tipo documento) anche le righe sono ulteriormente caratterizzate da un tipo riga che definisce :  l'oggetto dello scambio, se quantità e/o prezzi sono obbligatori, quali sono le informazioni aggiuntive contenute ed i controlli da eseguire. Potremo quindi avere righe riferite ad articoli codificati, righe di oggetti non codificati, righe di conto lavoro, righe fatturabili e non, ecc...

![AAP_VAP_11](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_VAP_11.png)
## Conto lavoro
Il conto lavoro può essere : 
 * pieno, quando l'intera lavorazione o trasformazione viene eseguita da un solo terzista
 * di fase, quando si richiede al fornitore di eseguire una fase del ciclo di lavorazione dell'assieme da realizzare (ad esempio un trattamento termico, preceduto da una lavorazione meccanica e seguito da una verniciatura, entrambe realizzate internamente all'azienda).

È possibile definire ordini totalmente di conto lavoro, oppure inserire nello stesso ordine righe di conto lavoro e di fornitura piena. Il ricevimento merce è "trasparente" al conto lavoro. Chi registra il materiale in entrata deve unicamente identificare l'oggetto e la sua origine (l'ordine che viene soddisfatto). Le attività specifiche (scarico della quantità presso il terzista, collegamenti con l'ordine di produzione in caso di conto lavoro di fase, ecc..) vengono svolte in modo automatico dal sistema. Possiamo avere una distinta di conto lavoro diversa dalla distinta di produzione interna (es. quando una parte dei componenti vengono procurati direttamente dal terzista stesso). I materiali possono essere inviati in relazione alla quantità e distinta dell'ordine, oppure a "bilanciamento" in cui le quantità da inviare vengono calcolate bilanciando i fabbisogni degli ordini in corso con la giacenza di componenti già presenti presso il fornitore; in questo modo sono facilitate le spedizioni per "confezione" o a rifornimento saltuario.

### Revisioni
Per ogni variazione che viene apportata ad una riga d'ordine si può tenere l'immagine precedente in modo da poter stampare una visione completa del documento comprensiva anche dei livelli precedenti con indicazione di quali sono state le righe variate e in merito a quali dati (quantità, data, prezzo).

### Solleciti
Prevede la possibilità di selezionare nel portafoglio ordini, attraverso criteri di priorità stabiliti dall'utente, i fornitori e le righe ordine da sollecitare. Può essere sollecitata la conferma di data e quantità richieste oppure la fornitura del materiale. Il sollecito può essere inviato automaticamente dal sistema sotto forma di e-mail.

### Trasmissioni
Ordini e solleciti possono essere automaticamente inviati ai fornitori via fax o via e-mail. o, più in generale, con strumenti EDI, tenendo traccia della data di spedizione.

### Triangolazioni
Sia gli acquisti che il conto lavoro possono essere triangolati direttamente verso un altro terzista od un cliente.

## Esecuzione della fornitura
Principalmente si parla di entrate merci. In Sme.UP l'entrata merci viene processata attraverso un flusso di estrazione che deriva il documento di entrata merci dagli ordini di acquisto a cui la fornitura è riferita. Il flusso permette di lanciare in sequenza una serie di elaborazioni elementari ciascuna specializzata a compiere una parte dell'intero processo; in questo modo si possono sviluppare funzioni specifiche utente da inserire nel flusso insieme alle funzioni standard. La combinazione delle funzioni elementari standard, con l'aggiunta eventuale di funzioni utente, permette di realizzare elaborazioni complesse che rispondono a qualsiasi esigenza possa nascere. L'esecuzione della fornitura si collega con le attività logistiche di trasferimento del materiale ricevuto. In questo ambito si possono avere comportamenti diversificati, per tipologia di materiale o per necessità produttive. Ad esempio si possono destinare materiali urgenti direttamente in linea.

![AAP_ACQ_04](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_04.png)
## Controllo qualità in accettazione
L'entrata merci attiva il controllo di qualità in accettazione, se il lotto non viene accettato viene generata una non conformità. Le non conformità in accettazione entrano nella valutazione globale del fornitore. I lotti non accettati possono essere restituiti al fornitore attraverso dei flussi di restituzione che generano una bolla di invio al fornitore a partire dalla bolla entrata merci. La bolla di restituzione può dar luogo alla riapertura dell'ordine di acquisto oppure ad una "attesa nota di credito" da parte del fornitore. Tra le opzioni possibili c'è anche la generazione di una nota di debito da spedire al fornitore.

## Controllo fatture
Il controllo fatture si collega ai documenti di entrata merci ed ai documenti di servizio reso per la certificazione di quantità e prezzi. Anche durante il controllo fatture si possono generare delle non conformità, ad esempio per differenza prezzo o per delta quantità, la fattura resta bloccata fino alla risoluzione della causa del blocco. La quadratura tra bolle e fatture unitamente all'assenza di blocchi qualitativi da luogo alla registrazione automatica in contabilità, e all'autorizzazione al pagamento.

## Statistiche Schede Looc.UP
Sono disponibili dei servizi per la visualizzazione in Looc.UP dei portafogli ordini e del fatturato passivo, mentre nella scheda fornitore possiamo avere la sintesi degli articoli forniti e del prezzo medio, nel periodo e negli anni precedenti.

![V5STAT_080](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/V5STAT_080.png)
## Analisi entrate merce
Dato un periodo, si confrontano i prezzi effettivi delle entrate merci con i listini di acquisto, si può anche calcolare il prezzo medio e con questo aggiornare un particolare tipo costo dell'articolo oppure utilizzarlo nella valorizzazione delle rimanenze di magazzino.

## Vendor rating
È un modulo dell'applicazione Q9000 che permette di valutare in forma continuativa l'andamento dell'affidabilità dei fornitori in termini di : 
 * conformità del prodotto
 * rispetto dei termini di consegna
 * osservanza dei termini contrattuali in fatto di certificazioni valide e disponibilità a collaborare per risolvere eventuali situazioni di criticità in essere.
Le informazioni per la classificazione del fornitore sono : 
 * andamento delle tempistiche di consegna
 * sensibilità all'aspetto qualitativo del prodotto
 * rispetto della certificazione del prodotto consegnato e dell'obbligo di conservazione documentazioni secondo le prassi stabilite.

## Budget
Nel processo del budget aziendale viene gestito anche il budget acquisti, nel quale articoli/quantità/data possono essere ricavati per esplosione del budget di produzione, agli articoli possono essere associati i fornitori preferenziali (dai dati fornitore / articolo) eventualmente applicando le quote di fornitura. Per la valorizzazione si può utilizzare un listino di budget oppure il listino di acquisto. Il budget acquisti può essere utilizzato per la definizione dei contratti di fornitura oppure per la stima degli esborsi finanziari pianificati per il prossimo periodo. Periodicamente saranno lanciate delle funzioni di estrazione dagli ordini e dalle bolle entrata merce per confrontare i consuntivi con il budget.

## Funzioni particolari
Grazie all'architettura del prodotto si possono costruire le funzioni a supporto delle più svariate necessità, a titolo di esempio di seguito ne riportiamo alcune : 

### Consignment stock
Quando il fornitore consegna dei materiali che però restano di sua proprietà fino a quando il cliente non li consuma, oppure a scadenza di un intervallo limite. Il sistema prevede la creazione di ordini di modello specifico ed una movimentazione adeguata, oltre che la possibilità di registrare entrate merci non fatturabili e dichiarazioni di consumo fatturabili con passaggio del materiale dall'area riservata di proprietà del fornitore alla giacenza interna al cliente (area di magazzino o di wip).

### Registri di conti a partita
Quando l'azienda invia al fornitore materiali propri (tipico il caso del prestito d'uso di attrezzature) oppure quando riceve dal fornitore materiali senza il passaggio della proprietà (tipico il caso del conto visione). Il sistema prevede la creazione di appositi documenti di carico/scarico del conto e la possibilità opzionale di gestire un saldo giacenza e la creazione di opportuni registri. Sono gestiti, sia i casi di materiale di terzi presso l'azienda, che quello di materiali dell'azienda presso terzi.

## Relazioni con il fornitore (VRM)
Sfrutta le stesse funzionalità previste per il CRM, possiamo avere : 
 * il **VRM Operativo**, che include tutte le funzioni offerte dall'ERP per la gestione dei rapporti con il fornitore :  gestione anagrafici, offerte, ordini, fatture, gestione resi fornitore, ecc..
 * il **VRM analitico**, che include tutte le funzioni statistiche di analisi dei dati del fornitore, ad esempio : 
 ** Schede oggetto, con situazioni da gestionale (offerte, ordini, fatture, articoli, prezzo medio, margine, ecc.)
 ** Business Intelligence
 * Il **VRM collaborativo**, che prevede : 
 ** la gestione del mailing verso i fornitori
 ** la gestione delle visite (pianificate / non pianificate) con la tenuta del report e dell'elenco dei partecipanti
 ** l'abilitazione di funzioni WEB per lo scambio di informazioni e per la gestione degli ordini.

## Conclusioni - Impostazione concettuale
La struttura delle informazioni e le funzioni a supporto della gestione approvvigionamenti sono state concepite con un elevato grado di astrazione in modo da avere una impostazione non direttamente collegata alle sole problematiche correnti ma da poter garantire un supporto anche a processi che nel tempo subiscono evoluzioni.
Così abbiamo ad esempio : 
 * la struttura dei dati di anagrafica che è adeguata alla gestione di tutti i soggetti che interagiscono con l'azienda (Banche, Clienti, Fornitori, Agenti, Trasportatori, Collaboratori esterni, ecc..) nonché l'azienda stessa
 * il documento, grazie alla tipizzazione della testata (caratterizzata dal tipo documento e modello) e delle righe (caratterizzate dal tipo riga), permette di rappresentare una grande varietà di condizioni. Ad esempio il documento può essere un ordine di acquisto o una bolla entrata merce, come pure una bolla invio in conto lavoro o una previsione di vendita, ecc... Nelle righe possiamo avere sia articoli che oggetti non codificati (es. servizi, cespiti, immobili, ...).
 * i flussi di estrazione, che permettono di creare un documento per derivazione, parziale o totale, da un altro documento origine. Possiamo avere flussi per estrarre delle bolle entrata merci da un ordine di acquisto, come estrazioni di richieste di consegna da contratti, oppure ordini da previsioni, e così via ...

![AAP_ACQ_05](http://localhost:3000/immagini/MBDOC_VIS-AAACQ/AAP_ACQ_05.png)
 * i listini :  che permettono di associare prezzi e sconti ad una terna di oggetti variabili definiti nelle tabelle di impostazioni (fornitori, clienti, articoli, classi materiale, fasi di lavorazione ecc...)
 * il budget di acquisto, basato su un'applicazione che a fronte di una coppia di oggetti (es. articolo, fornitore, classe merceologica, ecc...) può gestire piani di 120 periodi con ampiezza variabile di giorni, settimane, mesi, anche mista nello stesso piano in cui si possono esprimere le quantità oppure i valori ed i valori possono essere valorizzati a costi standard o a prezzi di listino, usando listini effettivi o eventuali listini di simulazione ...

# Applicazioni utilizzate
Le applicazioni Sme.UP a supporto della gestione degli approvvigionamenti sono : 
 * **Trade.UP**, per la gestione degli acquisti e del conto lavoro (ordini, entrata merci, invio in C/L, rientro da C/L, resi non lavorati, ...)
 * **Brec.UP**, per la gestione degli anagrafici di base (fornitori, estensioni, dati fornitore/articolo, ...)
 * **Clas.UP**, per la gestione dei listini e delle descrizioni in lingua

A queste applicazioni se ne aggiungono anche altre con funzione di supporto : 
 * **Marp.UP**, per la pianificazione materiali e l'emissione dei suggerimenti di acquisto
 * **Ware.UP**, per la gestione della movimentazione materiali (versamenti, consumi, trasferimenti interni)
 * **Q9000**, per la gestione qualitativa dei lotti di produzione, dei cicli di collaudo e dei rilievi eseguiti
 * **Plan.UP**, per la gestione del budget
