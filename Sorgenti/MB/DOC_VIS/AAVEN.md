 :  : TIT Vendite
# Obiettivo
L' obiettivo delle vendite è perseguire gli obiettivi commerciali aziendali in termini di bilanciamento di fatturato, marginalità, market-share, soddisfazione e fidelizzazione del cliente. Sme.UP supporta questo processo dalla sua origine (banca dati di prospect e informazioni a loro inerenti), nella sua parte più propriamente esecutiva (acquisizione ed evasione dell' ordine) e nella attività di controllo della rispondenza delle operazioni rispetto alle politiche commerciali aziendali.

# Contesto
In un'azienda le Vendite sono al centro di un gruppo di processi che vede : 
 * le attività di marketing (contatti, visite, campionature, studi, ...) e le offerte sia su clienti che prospect
 * le richieste del cliente in termini di beni e servizi che gli devono essere forniti
 * le richieste soddisfatte all'interno delle condizioni commerciali definite, che possono essere quelle generali di fornitura oppure specificatamente concordate con il cliente
 * la determinazione e il rispetto della data di fornitura concordata sono un elemento fondamentale per la soddisfazione del cliente; la data di consegna pertanto deve considerare la figura della disponibilità datata di quanto viene richiesto/offerto. Il risultato è l'esecuzione della vendita stessa. Nella esecuzione della fornitura sono interessati i processi di evasione degli ordini, di logistica interna ed esterna, di fatturazione dopo la consegna al cliente dei beni o servizi richiesti si possono innescare dei processi di post-vendita che possono riguardare gli interventi o le riparazioni in garanzia, la gestione dei resi cliente la gestione degli upgrade/retrofit, nel caso la vendita abbia come oggetto macchinari o servizi.I processi vengono monitorati attraverso statistiche ed analisi che comprendono tutta la reportistica e gli strumenti associati all'evasione degli ordini, alla misurazione della performance della funzione, alla pianificazione delle attività (portafoglio ordini, fatturato, customer rating, analisi margine di contribuzione, budget di vendita, ecc..).

![AAP_VEN_01](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_01.png)
## Copertura funzionale
Sme.UP ha applicazioni in grado di supportare tutte le necessità di gestione relative alla funzione delle Vendite : 
 * Gestione anagrafico clienti
 * Dati aggiuntivi clienti
 * Relazioni con i clienti
 * Richieste di offerta e offerte
 * Listini di vendita
 * Ordini di vendita
 * Contratti
 * Budget delle vendite
 * Analisi evadibilità
 * Gestione spedizioni
 * Fatture
 * Gestione note di credito e note di debito
 * Gestione consignment stock
 * Gestione conto visione
 * Analisi e report
 ** Ordinato
 ** Fatturato
 ** Customer rating
 ** Puntualità e ritardi
 * ...

# Gestione dati di anagrafica
Rappresenta l'insieme delle attività correlate alla creazione ed al mantenimento delle informazioni legate ai clienti, ai potenziali clienti e alle condizioni commerciali. Tra i dati di anagrafica utilizzati nelle vendite possiamo menzionare : 
 * l'anagrafico clienti / potenziali clienti con le sue estensioni e la gestione della gestione delle dichiarazioni d'intento
 * i listini di vendita

# Clienti - Potenziali clienti
Nell'anagrafico Clienti vengono gestite le informazioni seguenti : 
 * dati identificativi :  ragione sociale, partita IVA, categoria, ecc.
 * dati ambientali :  lingua, valuta, indirizzo, ecc.
 * contatti :  nominativo, telefono, fax, e-mail, ecc.
 * dati pagamento :  tipo pagamento, banca, IBAN, ecc.
 * dati relazionali :  destinazioni, indirizzo corrispondenza, indirizzo contabile, vettore, ecc.
 * classificazioni :  categoria contabile, settore merceologico, ecc.
 * dati movimentazione merce :  consegna, spedizione, giorni chiusura, ecc.

![AAP_VEN_01](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_01.png)
Nelle estensioni dei clienti possiamo gestire altre categorie di informazioni quali :  calendario alternativo, documenti / allegati specifici, indirizzo internet; ecc.; questi dati possono essere presenti o meno per ogni cliente, inoltre possono essere un numero anche elevato a piacere per tipo, superando la classica limitazione del numero di campi disponibile in un normale archivio anagrafico. Attraverso la gestione dei dati cliente/articolo è possibile mantenere informazioni specifiche per gli articoli offerti ad un cliente (il codice e la descrizione propria che il cliente assegna all'articolo, l'unità di misura di vendita che potrebbe differire rispetto a quella utilizzata internamente, ecc.. ).
In Sme.UP è anche prevista le gestione delle dichiarazioni d'intento ricevute dai clienti che possono essere di tipo : 
 * singolo
 * per un periodo
 * fino al raggiungimento di un determinato importo

## Tipizzazione ente
Tutte le funzioni sopra menzionate valide per i clienti, possono essere utilizzate anche per la gestione dei dati anagrafici dei potenziali clienti, infatti attraverso la definizione del "tipo ente" possiamo distinguere tra cliente e potenziale.

## Listini di vendita
La gestione dei listini permette di associare a tre oggetti definiti in funzione dell'impostazione (clienti, articoli, classi materiale, zona geografica, ecc...) cinque valori, tipicamente prezzo base e sconti. I listini prevedono la gestione della data di validità (iniziale e finale) e delle scale prezzi per quantità, oltre che la gestione dei prezzi in valuta. Nella gestione del listino è prevista la possibilità di passare automaticamente dall'informazione di dettaglio (es. prezzo di un articolo per un cliente) a un livello di sintesi superiore (es. prezzo di un articolo valido per un gruppo di clienti). In aggiunta alle risalite automatiche vi sono delle "user exit" apposite che permettono di costruire il prezzo applicando regole specifiche, anche basate su elementi diversi, con una propria dinamica di prezzi indipendente l'una dall'altra. Ad esempio il prezzo di un particolare in alluminio calcolato come quota di produzione a cui si somma la quota di materiale variabile in funzione del prezzo medio dell'alluminio.

## Gestione del credito
Il credito del cliente viene determinato da una funzione che combina un insieme di informazioni (fido statico,  ordini in corso, fatture emesse non ancora in pagamento, insoluti, solleciti di pagamento, ecc...) configurabili secondo le necessità dell'azienda. La gestione del credito può operare come blocco in fase di autorizzazione dell'ordine o in fase di evasione al momento del prelievo o della spedizione.

## Disponibilità
Nella determinazione della disponibilità non si considera solo l'esistenza di magazzino, ma anche la disponibilità datata, cioè la disponibilità proiettata nel tempo risultante dalla combinazione di impegni (di vendita, di produzione) e coperture (di acquisto, di produzione). In Sme.UP il concetto di disponibilità è stato esteso alla "disponibilità libera" :  la quantità/data che posso promettere ad un cliente senza che altri ordini acquisiti in precedenza ne vengano penalizzati. La disponibilità libera è alla base del modulo ATP (Available to promise), che permette di datare automaticamente (o di suggerire una quantità evadibile) un ordine cliente, considerando sia la disponibilità libera a tutti i livelli di distinta, che la capacità produttiva (CTP - Capable to promise).

## Richieste del cliente
Possono essere relative a beni o servizi e, nel caso di oggetti fisici, deve esistere un processo di fornitura e produzione tale da rendere disponibili gli articoli alla data e nella quantità concordate. Si possono stabilire con il cliente dei contratti di fornitura con condizioni di fornitura livello di servizio definiti e in cui la spedizione effettiva avviene a fronte delle richiesta di consegna mandata dal cliente attraverso :  telefono, lettera, fax, mail, EDI o Internet.

# La gestione delle vendite
Si fonda principalmente sul "documento" che può essere : 
 * di vendita, o di conto lavoro attivo
 * un ordine chiuso oppure un ordine aperto / contratto seguito da delle richieste di consegna.

Nella gestione Sme.UP del documento sono previste : 
 * le revisioni documento, che possono provenire direttamente dall'esterno (es. via EDI) o essere gestite manualmente
 * l'analisi evadibilità, sia per il lancio del prelievo per la spedizione

## Il documento
La gestione di tutte le tipologie di documenti è concentrata in una struttura univoca, realizzata mediante : 
 * la testata, dedicata alla gestione dei dati relativi alla totalità del documento (numero documento, cliente intestatario, riferimento esterno, responsabile commerciale, destinazione, data di emissione, modalità di spedizione, modalità di pagamento, ecc..)
 * le righe che rappresentano l'oggetto dello scambio (articoli, servizi, oggetti non codificati, ecc...) e indicano le quantità, le date ed i prezzi convenuti.

![AAP_VEN_02](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_02.png)
Il raggruppamento in un'unica struttura permette il grande vantaggio di normalizzare e standardizzare tutte le funzioni di manutenzione di tutti i possibili documenti del ciclo esterno. L'unificazione inoltre fornisce la possibilità di estendere automaticamente alle gestioni di tutti gli altri tipi documento, migliorie ed implementazioni apportate ad un tipo di documento.

![AAP_VEN_01](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_01.png)
## Tipizzazione del documento
I documenti sono classificati secondo il "Tipo documento" che ne definisce la natura (un ordine, un contratto, una bolla, ecc.) e le caratteristiche di comportamento (controlli, sviluppi, influenza sui vari portafogli o registri, ..).

![AAP_VEN_03](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_03.png)
Per ogni tipo documento diverso è possibile ottenere opportune statistiche e interrogazioni, produrre stampe, gestire manutenzioni. All'interno di un tipo documento le testate possono essere differenziate attraverso il "Modello documento"  che rappresenta delle sotto-classificazioni necessarie per ragioni interne all'azienda (es. vendite nazionali piuttosto che CEE o ExtraCEE, oppure vendite di prodotti o di servizi); il modello determina inoltre il tipo ed il layout di stampa del modulo di output. Nel documento (e di conseguenza all'interno di uno specifico tipo documento) anche le righe sono ulteriormente caratterizzate da un "Tipo riga", che definisce :  l'oggetto della vendita, se quantità e/o prezzi sono obbligatori, quali sono le informazioni aggiuntive contenute ed i controlli da eseguire. Potremo quindi avere righe riferite ad articoli codificati, righe di oggetti non codificati, righe di conto lavoro, righe fatturabili e non, ecc.
In Sme.UP il tipo documento è riferito ad una tabella, dove sono descritte le principali caratteristiche del documento stesso, tra cui : 
 * gruppi di modelli ammessi
 * tipo ente di riferimento
 * 'gruppi flag' di testata e riga per 'guidare il comportamento' dei documenti
 * ecc.

## Documenti tipici di esempio
Di seguito riportiamo una lista, esemplificativa e non certamente esaustiva, dei documenti che possono essere gestiti nel ciclo attivo di Sme.UP, lista che permette facilmente di intuire le potenzialità dell'applicazione.

### Offerte
Tipologia relativa a tutti i documenti che precedono le attività vere e proprie di vendita.
Modelli : 

- Offerta / Quotazione, serve per registrare i dati relativi alla quotazione fatta ad un cliente per una determinata fornitura richiesta.

### Ordini
Tipologia che include tutti i documenti che governano le attività vere e proprie di vendita.
Modelli : 
 * Contratto quadro, è un accordo con il cliente per la fornitura di beni e/o servizi.
 * Richiesta di consegna, deriva direttamente dal precedente a cui si riferisce.
 * Ordine standard per fornitura di beni, è il classico ordine di vendita.
 * Ordine di autorizzazione alla restituzione, serve per autorizzare il reso di materiale.
 * Conto lavoro attivo, è un ordine nel quale il cliente richiede di eseguire delle lavorazioni su componenti propri forniti direttamente.
 * Ordine per la fornitura di servizi, serve per la fornitura di prestazioni d'opera, consulenze, ecc. Casi particolari di ordini di servizi sono :  Contratto di manutenzione, Contratto di affitto.

### Spedizioni
Trattasi dei documenti per la spedizione al cliente dei materiali ordinati.
Modelli : 

- Bolla accompagnamento materiali, è il documento usato per il trasporto della merce verso il cliente, può essere derivata da un  ordine oppure diretta.

### Fatture
Evoluzione del documento "bolla" :  associata al documento bolla esiste la stampa fattura, che assume caratteristiche differenti in base a quanto richiesto dal cliente.
Modelli : 
 * Fattura normale, che è il documento a fronte del quale il cliente paga e che contiene la lista dei materiali spediti ed i relativi prezzi.
 * Nota di addebito
 * Nota di accredito.
 * Fattura proforma, che, in alternativa alla bolla, ha un lay-out molto simile ad una fattura, ma la sua stampa non attiva lo stato di "fattura emessa" e la relativa contabilizzazione.
 * Fattura diretta, nel caso di fornitura diretta.

## Conto lavoro attivo
Gli ordini di conto lavoro attivo hanno una gestione in tutto e per tutto simile a quella dei normali ordini di vendita con in più la gestione della distinta dei materiali forniti dal cliente; in Sme.UP possiamo avere nello stesso documento sia righe di vendita che righe di conto lavoro. Possiamo avere una distinta di conto lavoro attivo diversa dalla distinta di produzione interna. Le distinte possono essere memorizzate con uno specifico tipo distinta oppure inserite di volta in volta durante la creazione della riga ordine.

## Revisioni
Per ogni variazione che viene apportata ad una riga d'ordine si può tenere l'immagine precedente in modo da poter stampare una visione completa del documento comprensiva anche dei livelli precedenti con indicazione di quali sono state le righe variate e in merito a quali dati (quantità, data, prezzo).

## Trasmissioni
Conferme d'ordine e documenti di spedizione / fatturazione possono essere automaticamente inviati ai clienti via fax o via e-mail o, più in generale, con strumenti EDI, tenendo traccia della data di spedizione.

## Impiego Workflow
Il Workflow è un'applicazione di supporto che permette di definire processi con funzioni e responsabilità diversificate.
Nella gestione delle vendite si possono attivare dei processi di workflow per : 
 * approvare un ordine inserito da altre funzioni (es. via WEB)
 * autorizzare l'attivazione dell'ordine, oppure la spedizione per un cliente fuori fido

## Esecuzione della spedizione
### Analisi evadibilità
L'analisi evadibilità permette di stabilire se può essere iniziato il processo di spedizione verso un cliente o un gruppo selezionato di clienti. Il programma permette di selezionare, secondo impostazioni utente, un gruppo di clienti e di righe d'ordine da spedire; all'insieme selezionato viene applicata l'analisi disponibilità che determina la fattibilità della spedizione.  Alla fine dell'analisi si può scegliere di creare le liste di prelievo.

### Prelievo ed imballo
A seconda che si sia in presenza di magazzini complessi o semplici la customizzazione può prevedere processi di prelievo, più o meno articolati, in cui il prelievo può generare un trasferimento della giacenza dal magazzino all'area di attesa spedizione. Alla gestione del prelievo si può far seguire l'imballo e la creazione della packing list con la stampa sia del documento packing list che delle etichette dei colli.

### Gestione documenti di spedizione
In Sme.UP il documento di spedizione viene processato attraverso un flusso di estrazione che deriva la bolla di vendita dagli ordini di riferimento. Il flusso permette di lanciare in sequenza una serie di elaborazioni elementari ciascuna specializzata a compiere una parte dell'intero processo. Ad esempio, in presenza di magazzini complessi in cui il processo di prelievo è gestito con liste, le righe  della bolla possono essere create con riferimento all'ordine di vendita, ma solo relativamente agli articoli / quantità effettivamente consuntivati nelle liste di prelievo. Alle funzioni elementari standard si possono aggiungere anche funzioni specifiche utente sviluppate ad hoc. La combinazione delle funzioni elementari standard, con l'aggiunta di eventuali funzioni utente, permette di realizzare elaborazioni complesse che rispondono a qualsiasi esigenza possa nascere.

![AAP_VEN_04](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_04.png)
### Gestione logistica esterna
Nell'applicazione si può attivare anche il modulo di gestione viaggi che permette di raggruppare sotto un singolo oggetto l'insieme delle bolle che devono fare lo stesso itinerario e che saranno affidate allo stesso vettore. Nella gestione dei viaggi è anche possibile gestire in modo cumulativo la data/ora di effettiva spedizione e le informazioni consuntive del trasporto (tipo di automezzo, targa, volumi, pesi, ecc...), utilizzabili nel controllo delle fatture di trasporto.

### Fatturazione
La fatturazione si collega alle bolle di vendita di cui è la naturale evoluzione; possiamo avere fatture contestuali alla spedizione, anche dirette (senza la bolla di vendita) oppure fatture differite generate periodicamente secondo un calendario di fatturazione. In accordo a regole utente è possibile raggruppare n. bolle in un'unica fattura cumulativa. Per l'insieme delle bolle selezionate possiamo avere una modalità di fatturazione batch o interattiva e quest'ultima prevede anche la possibilità di forzare il raggruppamento di bolle o di suddividere bolle che sarebbero normalmente raggruppate. Tra le funzioni di fatturazione c'è la possibilità di generare anche note di credito da stampare e inviare al cliente oppure di registrare note di debito ricevute dal cliente.

## Gestione post-vendita
Tra le attività successive alla vendita con Sme.UP possiamo gestire i processi seguenti : 
 * resi cliente,  per sostituzione in garanzia oppure per riparazione in garanzia o fuori garanzia
 * interventi di assistenza, su macchine installate presso il cliente, in garanzia o fuori garanzia
 * montaggio di upgrade, su macchine installate presso il cliente

### Resi cliente
Può essere creato un processo che prevede l'esecuzione del reso solo dopo la creazione di un apposito ordine di autorizzazione al reso. In questo caso sarà anche realizzato un flusso di estrazione che permette di generare il reso per derivazione dall'ordine. In altre realtà si preferisce costruire dei processi di reso che non abbisognano di autorizzazione, in cui il flusso di estrazione generalmente viene derivato dalla precedente bolla/fattura di vendita.
Il reso è collegato alla qualità attraverso la generazione di un lotto di reso cliente, con cui si può gestire tutto l'iter della non conformità fino a : 
 * restituzione del reso non riparato
 * restituzione dopo riparazione
 * reintegro con materiale equivalente
 * scarto definitivo e creazione di una nota di credito

### Interventi di assistenza
Gli interventi di assistenza sono dei particolari documenti fatturabili che contengono : 
 * gli articoli utilizzati come ricambi
 * il tempo impiegato dalle persone, con prezzi eventualmente differenziati in funzione della tipologia dell'intervento (meccanico, elettronico, idraulico, ecc...)
 * le spese di viaggio e alloggio sostenute

### Montaggio di upgrade
Si tratta di documenti concepiti come gli interventi di assistenza, con la differenza che gli articoli utilizzati sono quelli necessari per il potenziamento della macchina.

## Statistiche e analisi
### Schede Looc.UP
Sono disponibili "servizi" per la visualizzazione dei portafogli ordini e del fatturato, mentre sul cliente è possibile avere la sintesi degli articoli venduti e del prezzo relativo, nel periodo e negli anni precedenti.
I report possono essere visualizzati in Looc.UP oppure esportati per elaborazioni di strumenti di Business Intelligence.

![V5STAT_021](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/V5STAT_021.png)
![V5STAT_039](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/V5STAT_039.png)
![V5STAT_080](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/V5STAT_080.png)
## Customer rating
È un modulo dell'applicazione Q9000 normalmente usato nella valutazione dei fornitori, ma le cui funzioni possono essere utilizzate anche come autovalutazione nei confronti delle forniture ai clienti.
Si possono avere autovalutazioni in termini di : 
 * conformità del prodotto (dall'analisi dei resi cliente)
 * rispetto dei termini di consegna

## Budget
Il budget delle vendite può essere creato a partire dai consuntivi del venduto o del fatturato, permettendo sintesi dei dati per classificazioni degli articoli o dei clienti. La gestione del budget prevede funzioni di distribuzione in base a curve di stagionalità e lo split delle quantità da piani sintetici, ad esempio per zona/classe merceologica verso dettagli a livello cliente / articolo. Le quantità di budget possono essere valorizzate utilizzando un listino di budget oppure quello di vendita, tenendo conto anche dell'evoluzione del prezzo per data di validità.  Periodicamente possono essere lanciate delle funzioni di estrazione dagli ordini e dalle fatture per confrontare i consuntivi con il budget.

## Funzioni particolari
Grazie all'architettura del prodotto si possono costruire le funzioni a supporto delle più svariate necessità. A titolo di esempio di seguito ne riportiamo alcune : 

### Applicazioni WEB
Nel sito internet si possono gestire aree riservate dove il cliente autorizzato accede con un proprio profilo che gli permette di vedere le informazioni che gli vogliamo mettere a disposizione (es. i prezzi degli articoli che ordina, lo stato dei suoi ordini, le sue spedizioni e fatture, la giacenza di materiali a lui riservati, informazioni tecniche dei prodotti, ecc..). Si possono anche attivare funzioni di inserimento ordini direttamente da parte del cliente, lasciando alla organizzazione di vendita la gestione del credito e della conferma di quantità e data richieste.

### Consignment stock
Quando il fornitore consegna dei materiali che però restano di sua proprietà fino a quando il cliente non li consuma, oppure a scadenza di un intervallo limite.
Il sistema prevede la creazione di ordini di modello specifico ed una movimentazione adeguata, oltre che la possibilità di registrare spedizioni non fatturabili e dichiarazioni di consumo fatturabili con passaggio del materiale dall'area riservata di proprietà del fornitore alla giacenza interna al cliente (area di magazzino o di  wip).

### Registri di conti a partita
Si manifesta quando l'azienda invia al cliente materiali propri (tipico il caso di prodotti in conto visione) oppure quando riceve dal cliente materiali senza il passaggio della proprietà (tipico il caso di attrezzature in prestito d'uso). Il sistema prevede la creazione di appositi documenti di carico/scarico del conto, la possibilità opzionale di gestire un saldo giacenza e la creazione di opportuni registri.
Sono gestiti sia i casi di materiale di terzi presso l'azienda che quello di materiali dell'azienda presso terzi.

## CRM  :  gestione relazioni con il cliente / potenziale
Nel CRM possiamo distinguere : 
 * **CRM Operativo**, che include tutte le funzioni offerte dall'ERP per la gestione dei rapporti con il  cliente :  gestione anagrafici, offerte, ordini, fatture, gestione del credito, gestione resi cliente, ecc..
 * **CRM analitico**, che include tutte le funzioni statistiche di analisi dei dati del cliente. In Sme.UP possiamo elencare : 
 ** Schede oggetto, con situazioni da gestionale (offerte accettate / perse, ordini, fatture, articoli, prezzo medio, margine, ecc.)
 ** Business Intelligence
 * **CRM collaborativo**, che prevede : 
 ** la gestione del mailing verso i clienti
 ** l'archivio degli eventi (marketing, fiere, demo, presentazioni, ecc.)
 ** la gestione delle visite (pianificate / non pianificate) con la tenuta del report e dell'elenco dei partecipanti
 ** l'abilitazione di funzioni WEB per lo scambio di informazioni e per la gestione degli ordini.

## Provvigioni
Le provvigioni possono essere estratte automaticamente dai documenti di vendita. La liquidazione può essere gestita con differenti periodicità (annuale, mensile, trimestrale) ed effettuata sull'importo fatturato, sull'importo incassato o sull'importo saldato. È previsto il calcolo del piano dei contributi dell'agente (ritenute d'acconto, Enasarco, ISC, e FIRR), con la stampa della fattura proforma e la creazione opzionale di un documento di ciclo esterno sul quale verrà eseguito il controllo all'arrivo della fattura dell'agente. Le funzioni di contabilizzazione provvigioni permettono di attribuire i costi, nonché i contributi in funzione del loro periodo di competenza (e non in funzione della registrazione della fattura agente) : 

![V5PROV_002](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/V5PROV_002.png)
# Conclusioni - Impostazione concettuale
La struttura delle informazioni e le funzioni a supporto della gestione vendite sono state concepite con un elevato grado di astrazione in modo da avere una impostazione non direttamente collegata alle sole problematiche correnti ma da poter garantire un supporto anche a processi che nel tempo subiscono evoluzioni.
Così abbiamo ad esempio : 
 * la struttura dei dati di anagrafica che è adeguata alla gestione di tutti i soggetti che interagiscono con l'azienda (Banche, Clienti, Potenziali clienti, Fornitori, Agenti, Trasportatori, Collaboratori esterni, ecc..) nonché l'azienda stessa
 * il documento, grazie alla tipizzazione della testata (caratterizzata dal tipo documento e modello) e delle righe (caratterizzate dal tipo riga), permette di rappresentare una grande varietà di condizioni. Ad esempio il documento può essere un ordine di vendita o una bolla di spedizione, come pure una previsione di vendita, un'offerta, ecc...  Nelle righe possiamo avere sia articoli che oggetti non codificati (es. servizi, interventi, immobili, ...).
 * i flussi di estrazione, che permettono di creare un documento per derivazione, parziale o totale, da un altro documento origine. Possiamo avere flussi per estrarre delle bolle di vendita da un ordine, come estrazioni di richieste di consegna da contratti, oppure ordini da previsioni, e così via ...

![AAP_VEN_05](http://localhost:3000/immagini/MBDOC_VIS-AAVEN/AAP_VEN_05.png)
 * i listini :  che permettono di associare prezzi e sconti a tre oggetti variabili definiti nelle tabelle di impostazioni (fornitori, clienti, articoli, classi materiale, fasi di lavorazione ecc...)
 * il budget di vendita, basato su un'applicazione che a fronte di una coppia di oggetti (es. articolo, cliente, classe merceologica, zona, ecc...) può gestire piani di 120 periodi con ampiezza variabile di giorni, settimane, mesi, anche mista nello stesso piano in cui si possono esprimere le quantità oppure i valori ed i valori possono essere calcolati a prezzi budget o a prezzi di listino, usando listini effettivi o eventuali listini di simulazione ...

# Applicazioni utilizzate
Le applicazioni Sme.UP a supporto della gestione delle vendite sono : 
 * **Trade.UP**, per la gestione delle vendite (offerte, contratti, ordini, spedizioni, resi cliente, ...)
 * **Brec.UP**, per la gestione degli anagrafici di base (clienti, potenziali clienti, estensioni, dati cliente/articolo, ...)
 * **Clas.UP**, per la gestione dei listini e delle descrizioni in lingua

A queste applicazioni se ne aggiungono anche altre con funzione di supporto : 
 * **Marp.UP**, per la pianificazione materiali e la determinazione ATP
 * **Ware.UP**, per la gestione della movimentazione materiali (spedizioni, trasferimenti, versamenti, ...)
 * **Q9000**, per la gestione qualitativa dei lotti di reso dei cicli di collaudo, dei rilievi eseguiti, delle non conformità e delle azioni correttive
 * **Plan.UP**, per la gestione del budget
 * **Work.UP**, per la gestione dei processi di approvazione o che interessano funzioni diverse
