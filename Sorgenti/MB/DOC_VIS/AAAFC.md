# Amministrazione Finanza e Controllo

## Introduzione
Obiettivo di questa applicazione è la gestione di tutti gli aspetti civilistici e fiscali così come gestionali e di business cui le aziende devono provvedere. Attraverso Keep.UP si vuole inoltre fornire uno strumento in grado di soddisfare le esigenze di gruppi aziendali nel processo di internazionalizzazione e rendere più efficiente e veloce il processo di budgeting e reporting.
Le caratteristiche principali che consentono il raggiungimento di tali obiettivi sono la multiaziendalità, la possibilità di definire più divisioni all'interno della stessa azienda, il trattamento di tutti i valori in doppia valuta, il continuo aggiornamento e allineamento alla normativa fiscale vigente.
Chiariremo, ora, gli aspetti più significativi ed originali di questa applicazione.

### Impostazione ad oggetti
Come ogni altra applicazione di Sme.UP, questa applicazione è stata suddivisa in moduli tra loro indipendenti. Questo ha facilitato la convivenza dell'applicazione con altre applicazioni di SmeUP senza comportare duplicazione di archivi ed ha permesso di utilizzare alcuni moduli in presenza di applicazioni contabili di terzi, per integrarne le funzionalità (ad esempio la gestione dei solleciti, le riclassifiche di bilancio).
Sfruttando il concetto di Oggetto applicativo è stato possibile  rappresentare in modo efficace i fenomeni contabili :   il conto, la registrazione, la rata, il sollecito, il cliente, la banca sono oggetti che beneficiano di funzioni generali (collegamento a note e parametri, flussi di inserimento/modifica/annullamento, azioni eseguibili, ecc.) e consentono di sfruttare appieno la funzione di navigazione. La navigazione permette (a chi ne ha le opportune autorizzazioni) di accedere, partendo da una qualsiasi interrogazione, ad ogni altra interrogazione ad essa collegata. Ad esempio, dall'estratto conto di un cliente, sarà possibile passare all'analisi dei solleciti che gli sono stati inviati, e da questa all'analisi storica dei suoi ritardi di pagamento.

Analizziamo ora le principali caratteristiche dell'applicazione focalizzandoci su quelli che riteniamo essere gli aspetti più qualificanti del prodotto.

## Piano dei conti
La struttura del piano dei conti non segue la tradizionale suddivisione in mastro/conto/sottoconto (a tre o quattro livelli), ma assegna semplicemente ad ogni conto  riclassifiche, ciascuna delle quali è un attributo, anche virtuale, del conto. Con questo modello si possono definire strutture del piano dei conti del tutto libere e di profondità variabile per coprire le più diverse esigenze di rappresentazione aggregata del bilancio, tra le quali il bilancio CEE.

![AAP_AFC_06](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_06.png)
## Registrazioni contabili
Ogni registrazione è suddivisa in due parti :  una testata, in cui sono riportati i dati comuni (informazioni fiscali, natura della registrazione) e le righe, che contengono le scritture contabili (conti, importi). In questo modo si riduce al minimo la duplicazione di informazioni. Le caratteristiche principali della testata di una registrazione sono :  l'esercizio contabile di appartenenza, la pertinenza (contabile, gestionale, comune) e la condizione (attiva, sospesa, simulata).

## Modelli di registrazioni
Particolare cura è stata posta nella definizione di modelli preimpostati per le registrazioni contabili :  l'esecuzione della registrazione consiste nel richiamare un modello, completandolo con i dati opportuni. È possibile inoltre intestare il modello ad un oggetto (ad esempio un canone ricorrente ad un fornitore), nel qual caso per eseguire la registrazione è sufficiente, all'atto dell'inserimento, richiamare l'oggetto intestatario.

## Pratiche amministrative
È stato introdotto il concetto (e quindi l'oggetto) di _Pratica amministrativa_, che costituisce il raggruppamento di un insieme di oggetti su cui eseguire azioni comuni. In tal modo si uniforma la rappresentazione di funzioni eterogenee quali la costruzione di una distinta effetti, di un elenco solleciti per pagamento scaduti, di un documento Iva. Naturalmente ogni tipo diverso di pratica ha una propria modalità di composizione.

## Gestione e controllo pagamenti
La registrazione, se prevede un pagamento futuro, si sviluppa in una o più rate (sia in modo automatico sia inseribili manualmente), che costituiscono la base su cui si svilupperà la gestione dei crediti e dei debiti. La rata è un oggetto distinto dalla riga di registrazione, che ne rappresenta una possibile origine. Questo disaccoppiamento è dovuto al fatto che una rata è collegabile a qualsiasi oggetto. Ad esempio, da una riga di un ordine di vendita o d'acquisto si possono generare le rate delle previsioni di pagamento (in valore e data), che costituiscono le informazioni su cui si baserà l'esposizione dei flussi di cassa.
Per un controllo puntuale dei pagamenti, abbiamo introdotto il concetto di rata di dovuto e di pagato :  la rata generata da una registrazione che prevede un pagamento futuro è una rata di dovuto. La registrazione di pagamento genera invece una rata di pagato, che si collega esplicitamente ad una ed una sola rata di dovuto (qualora il pagamento chiuda più rate di dovuto il sistema genera automaticamente più rate di pagato per mantenere l'accoppiamento).
Attraverso il concetto di Pratica Amministrativa è possibile raggruppare rate ancora aperte, secondo diverse modalità (di un cliente, da presentare come effetti ad una banca, con residuo al di sotto di un valore, ecc.).
La registrazione dei pagamenti può essere eseguita richiamando una pratica composta in precedenza, oppure selezionando interattivamente le rate da saldare, sia in modo cieco (ad esempio fino alla copertura di un importo prefissato), sia in modo visualizzato. In questa fase è possibile far generare dal sistema movimenti di oscillazione cambi e di abbuono per saldare una rata.

![AAP_AFC_02](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_02.png)
## Solleciti
Dalle rate di dovuto ancora aperte è possibile generare periodicamente segnalazioni di sollecito, con opportuni filtri (esclusione di clienti, soglia di importo) che costituiscono un archivio storico consultabile secondo varie modalità. La stessa rata di dovuto, se rimane aperta, può generare, nel tempo, diverse segnalazioni di sollecito, di gravità crescente. Un sollecito viene dichiarato chiuso all'atto della registrazione della rata di pagato.

![AAP_AFC_07](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_07.png)
## Analisi crediti e debiti
Questa funzione si basa sull'accoppiamento tra le rate di dovuto e di pagato. Di ogni documento può essere presentata una situazione per data di pagamento (atteso o eseguito) oppure il bilanciamento all'interno di ogni scadenza, oltre alla consueta sintesi per registrazione. Per ogni scadenza vengono calcolati i giorni di ritardo di pagamento e viene valorizzato il ritardo. L'analisi può essere effettuata sia ad oggi, sia nel passato, in modo da ricostruire dinamicamente una situazione pregressa.

## Controllo DDT/Fatture
È presente uno strumento di registrazione contabile delle fatture con controllo dei documenti di trasporto che le originano. Tale controllo può essere attivato oltre che per il ciclo passivo (come di consueto ) anche per il ciclo attivo, in modo da ottenere anche in questo caso una migliore integrazione fra documenti e registrazioni. È possibile scegliere le anomalie da rilevare (differenza prezzo, quantità, pagamento, ecc.) e le azioni da intraprendere al loro verificarsi :  apertura di non conformità, invio di e-mail, blocco dei pagamenti o altro ancora.

Sono presenti, nel ciclo passivo, varie modalità operative : 
 * viene eseguito il controllo; in un secondo tempo viene eseguita la registrazione contabile per le sole fatture corrette;
 * il controllo e la registrazione contabile vengono eseguiti contemporaneamente, con sole segnalazioni non bloccanti;
 * viene eseguita la registrazione contabile sia per un singolo documento, sia di massa, (anche partendo dalle fatture ricevute via EDI), mentre il controllo viene eseguito in un secondo tempo.

È inoltre possibile eseguire in modo automatico la registrazione delle fatture da ricevere e da emettere, che verranno in seguito stornate (dalla registrazione della fattura se di un esercizio successivo, manualmente se nello stesso esercizio). In tal modo si tiene conto del valore in attesa fattura, sia nel ciclo attivo sia in quello passivo.

## Ritenute d'acconto
La gestione delle ritenute d'acconto è completamente integrata nella registrazione contabile. All'atto della registrazione della fattura, se l'ente è definito come percipiente, viene presentato un formato ulteriore in cui si inseriscono le informazioni specifiche della ritenuta. All'atto del pagamento della ritenuta, viene generata in modo automatico una riga di registrazione di chiusura. È prevista inoltre la stampa delle lettere di certificazione e la produzione dell'archivio relativo al modello 770.

## Gestione IVA
Oltre all'adempimento degli obblighi fiscali, sono presenti le seguenti funzioni : 
 * gestione del plafond
 * gestione settori per attività in riferimento all'oggetto aziendale
 * calcolo del prorata
 * IVA a esigibilità differita
 * imputazione automatica dell'Erario con IVA
 * protocollazione di registrazioni non IVA.

## Contabilità analitica
Allo scopo di fornire un maggior livello di dettaglio alle righe di registrazioni contabili è possibile assegnare, a ciascuna, fino a tre oggetti per specificarne la natura ed altri tre per specificarne la destinazione. La guida per questa funzione è il conto contabile, in cui sono definite le tipologie degli oggetti che definiscono la natura e la destinazione e, opzionalmente, i valori ammessi od assunti. È possibile iimpostare modelli di registrazione che contengono la suddivisione percentuale dell'importo della registrazione stessa; se le informazioni predefinite sono esaustive (oggetti e percentuali di suddivisione), la registrazione analitica viene eseguita in modo totalmente automatico. In caso contrario essa va inserita manualmente, all'interno della funzione di immissione della registrazione contabile.

![AAP_AFC_03](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_03.png)
## Analisi di bilancio
È possibile redigere il bilancio oltre che per le classiche riclassifiche del piano dei conti e CEE - per qualsiasi altra riclassificazione si voglia utilizzare e secondo criteri fiscali o gestionali. È prevista la possibilità di analizzarne struttura ed indici nonché di confrontare bilanci di periodi diversi e/o di altre aziende del gruppo e di verificarne gli scostamenti.

## Contabilità gestionale
L'obiettivo della contabilità gestionale consiste nella possibilità di applicare il principio di competenza anche nei periodi mensili oltre che annuali. Applicare il principio di competenza significa imputare i costi/ricavi in base alla loro effettiva competenza temporale :  ci sono, quindi, costi/ricavi che devono essere imputati ad un differente mese (ad esempio fatture la cui consegna è avvenuta in un mese differente rispetto alla rilevazione della fattura stessa) oppure la cui imputazione deve essere suddivisa su più mesi (ad esempio canoni di assicurazione annuali che dovranno essere suddivisi sui 12 mesi cui il canone fa riferimento).
Ciò si traduce nella creazione automatica di registrazioni gestionali del costo/ricavo in base alla competenza collegate alla registrazione contabile.

## Tesoreria
Sono state realizzate alcune funzioni di tesoreria che, utilizzando opportune tabelle contenenti le condizioni specifiche al rapporto bancario, consentono : 
 * riconciliazione automatica o semiautomatica dei movimenti da estratti conto per data valuta e/o data operazione;
 * analisi dei rapporti di conto corrente, conti valutari, anticipi, castelletto;
 * calcolo numeri e relativo scalare interessi;
 * proposte di convenienza economica nelle funzioni di presentazione effetti e pagamenti a fornitori;
 * calcolo automatico delle spese e commissioni in funzione del tipo di operazione;
 * proiezioni saldi di conto corrente;
 * proiezione castelletto;
 * situazioni riepilogative di disponibilità dei rapporti (con ordinamenti diversi, con o senza movimenti)

## Analisi disponibilità finanziaria
L'Analisi Disponibilità Finanziaria (ADF) è uno strumento atto a riprodurre, in base alle migliori conoscenze attuali dei fenomeni futuri, l'andamento nel tempo dei flussi finanziari. In stretta analogia con l'analisi disponibilità dei materiali, si possono definire fonti attuali (saldi di conti di liquidità) e fonti future (entrate o uscite di liquidità previste ad una data). Queste ultime vengono estratte, tramite opportune interfacce, dalle applicazioni gestionali (cicli attivi e passivi, piani MPS, ecc.), con diverse possibilità di ritorno dei dati (ad esempio, nel ciclo attivo, l'ordinato residuo al netto o al lordo di quanto già in bolla).

È possibile comprendere nell'analisi anche fonti di soluzioni applicative non SME.UP, sia attuali che future. Ogni fonte ritorna un evento elementare, (caratterizzato da un segno, un importo, una data e un codice valuta) ed un oggetto intestatario dell'evento, caratteristico della fonte, che costituisce l'elemento di maggior dettaglio dell'analisi.
Sono possibili sia analisi per oggetto elementare, sia, ricorsivamente, per un suo elemento di aggregazione, inoltre questa funzione è applicabile al singolo ente (per il controllo del fido) ed anche, globalmente, per l'intera azienda (per il controllo della disponibilità futura di cassa).


## Dichiarazione d'intento
È stata implementata la gestione del registro delle dichiarazioni di intento ricevute nonché la sua trasmissione in via telematica all'Agenzia delle Entrate, inoltre è presente la gestione dell'invio delle dichiarazioni di intento dell'Azienda ai suoi fornitori.

## Intrastat e Black List
Vengono generati i file da trasmettere alla Dogana e all'Agenzia delle Entrate riguardanti le operazioni IntraCee e quelle con operatori Black List. I dati di tali modelli vengono reperiti in modo automatico partendo dalle informazioni contabili e dai documenti.

## Cespiti
L'applicazione Cespiti ha lo scopo di risolvere tutte le problematiche connesse alla determinazione degli ammortamenti dei beni di proprietà dell'azienda. Le principali caratteristiche applicative sono le seguenti : 
 * Calcolo dell'_Ammortamento fiscale_, secondo la normativa vigente
 * Impostazione e calcolo di diversi _Ammortamenti industriali_
La possibilità di gestire diverse aliquote e piani di ammortamento si ottiene introducendo il concetto di _linea di ammortamento_ (simile allo scenario in pianificazione e schedulazione) che costituisce un ambiente separato in cui vengono impostati i parametri di calcolo e registrati gli ammortamenti risultanti. Per ogni linea si può infatti definire un piano di ammortamento esplicito per il singolo cespite, oppure impostare valori (sia importi sia percentuali, per il singolo esercizio o globali) a livello di cespite, di categoria, oppure generali, con ricerca per risalita, in modo da inserire il dato al suo massimo livello, senza introdurre ridondanze. È inoltre possibile inserire movimenti manuali  relativi ad una singola linea, in modo da poter simulare rivalutazioni, svalutazioni, ecc.. Ogni elaborazione di calcolo degli ammortamenti registra tutta la storia futura dei cespiti presenti nel sistema. In tal modo sono facilmente ottenibili, per ogni linea, sia analisi 'verticali' (piano di ammortamento di un singolo cespite), sia 'orizzontali' (valore totale dei cespiti in un qualsiasi esercizio futuro). È inoltre stato predisposto il collegamento dalla contabilità generale, per introdurre nell'applicazione i movimenti di apertura (acquisti), ed il collegamento verso la contabilità generale, per eseguirvi la registrazione degli ammortamenti.

![AAP_AFC_08](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_08.png)
## Controllo di gestione
L'obiettivo del controllo di gestione si può riassumere nella frase : 

**(far) Conoscere per Decidere**

Gli scopi di queste decisioni possono essere molteplici e sono influenzati da diverse variabili quali :  la tipologia di mercato in cui l'azienda si trova ad operare, la struttura organizzativa dell'azienda e gli obiettivi di medio/ lungo termine circa l'assetto societario dell'azienda. I temi più frequentemente affrontati dal controllo di gestione sono : 
 * fissare il prezzo di un prodotto
 * sostituzione o eliminazione di un prodotto
 * make or buy
 * sostituzione di un fornitore
 * accettazione di una commessa
 * controllare i livelli di spesa
 * determinare la profittabilità di una linea di prodotti
 * determinare la profittabilità di un'area geografica
Per poter rispondere in modo puntuale e attendibile ai quesiti di cui sopra è necessario misurare valori Contabili e Tecnici

### Valori contabili
Contabilità Generale e Contabilità Analitica con le diverse tipologie di registrazione

### Valori tecnici
> Distinte base            Materie prime componenti semilavorati
 Cicli di lavorazione    Impegni risorse uomo e macchina

Sme.UP risponde a queste esigenze non con una specifica impostazione del controllo di gestione, ma fornisce l'insieme di strumenti di base necessari ad una grande gamma di possibili impostazioni. Ciò è ottenuto realizzando strutture di dati "neutre", che contengono, tra le proprie informazioni, il significato degli oggetti e dei valori, oltre agli oggetti e ai valori stessi.

In particolare si utilizzano : 

**Le strutture simmetriche del modulo MPS**
(rappresentano, per un gruppo di oggetti, lo sviluppo nel tempo, secondo una periodicità definita, di un singolo valore.)
La struttura dell'MPS, permette di rappresentare lo sviluppo di budget e consuntivi nel tempo, quali, ad esempio : 
 * la quantità prevista per articolo cliente nei prossimi 12 mesi
 * la quantità venduta per articolo cliente negli ultimi 12 mesi
 * l'aumento pianificato per fornitore e classe materiale nei prossimi 5 anni
 * le spese per centro di costo
 * il piano di produzione per articolo nelle prossime 12 settimane
 * il carico dei centri di lavoro per giorno

**L'archivio del modulo Controllo Costi**
(rappresenta, sempre per lo stesso gruppo di oggetti, per un singolo periodo, un insieme di 99 valori a significato variabile.)
La struttura dei costi, permette di rappresentare budget e consuntivi analitici, relativi ad un periodo, quali, ad esempio : 
 * scomposizione del costo del lavoro mensile, per dipendente
 * scheda di costo per centro di costo
 * sintesi valori per cliente/articolo (ordinato, spedito, a quantità e valore)
 * indici di servizio per cliente e classe di prodotto
 * scheda dei costi per commessa

Per entrambe queste strutture sono state realizzate funzioni di ripresa di sintesi delle informazioni del gestionale, che possono essere composte in un flusso di attività, ed eventualmente integrate con funzioni di ripresa specifiche. Questi due moduli vengono poi integrati con l'effettivo modulo di controllo di gestione Delt.UP

### Caratteristiche salienti dell'MPS
 * **Periodicità variabile** :  si può diversificare per grandezze diverse e per la stessa grandezza può assumere valori diversi per ogni periodo (ad esempio all'inizio in giorni, poi in settimane ed infine in mesi).
 * **Disponibilità di una serie di funzioni**, sia di natura generale (operazioni aritmetiche, confronti tra due viste, suddivisione di una vista in altre in base ad una tabella di pesi, ecc.), sia di natura applicativa, partendo da una vista per ottenere le viste dei suoi componenti di distinta base o delle risorse del ciclo di produzione, oppure partendo da un articolo per ottenere l'andamento della disponibilità futura, valorizzare una vista in base ad un costo prefissato, sintetizzare in una vista i movimenti di magazzino eseguiti in un periodo, oppure le righe di ciclo esterno, passate o future. Queste funzioni possono essere composte liberamente in un flusso sequenziale di azioni, eventualmente arricchite da funzioni specifiche, in modo da realizzare un processo articolato, sia di preventivazione, sia di consuntivazione, come la definizione di un budget a partire da dati storici, ed il suo sviluppo in consumi materiali e risorse, sia in termini di quantità sia di valore; oppure la definizione del piano principale di produzione, in base al portafoglio ordini e alle previsioni di vendita, eventualmente combinati con regole specifiche; oppure ancora l'analisi dell'impatto sulle risorse dei risultati della pianificazione materiali, realizzando uno strumento di CRP.

### Caratteristiche salienti del modulo controllo costi
 * Struttura del costo dell'articolo, suddivisa in 99 componenti elementari definibili liberamente e liberamente raggruppabili.
 * Possibilità di determinare, per lo stesso articolo, più tipi di costo.
 * Storicizzazione del costo in modo da poter tenere traccia delle variazioni subite nel tempo.

È possibile inoltre definire un oggetto a livello superiore dell'articolo, risultante per esempio dalle abbinate : 
 * articolo - configurazione
 * articolo - commessa
 * articolo - plant produttivo
Questo oggetto diviene poi l'elemento di analisi dei costi.

### Il controllo di gestione attraverso Sme.UP
All'interno del complesso processo di analisi e controllo della gestione, Delt.UP svolge il ruolo fondamentale di collegamento ed elaborazione dei dati provenienti dai differenti sistemi gestionali conferenti. Con l'ottica di fornire una visione d'assieme dei fenomeni, Delt.UP reperisce, riordina, elabora e rende disponibili i dati attraverso l'interfaccia grafica di Looc.UP o alimentando datawarehouse. L'implementazione di un corretto modello di controllo di gestione richiede la presenza in azienda di una adeguata gestione operativa degli eventi oggetto del controllo di gestione stesso. Delt.UP non è una struttura rigida di controllo di gestione, ma un insieme di strumenti elementari che permettono l'implementazione di flussi di reperimento, elaborazione ed emissione di dati atti ad ottenere il modello desiderato dall'azienda. I consulenti possono essere propositivi nella realizzazione di un determinato modello in funzione dell'esperienza acquisita, ma obiettivo primario è quello di implementare il modello adatto all'azienda senza forzature al metodo indotte dallo strumento.

Nella nostra realizzazione abbiamo seguito le seguenti linee guida, nello spirito di tutte le applicazioni Sme.UP : 
 * Impostazione dei dati di base al livello più alto possibile (ereditarietà delle proprietà ai livelli inferiori)
 * Indipendenza dall'ambiente gestionale
 * Modularità dei vari passi della pianificazione
 * Possibilità di simulare a video ogni singolo passo
 * Ampia parametrazione delle scelte

### Logica di funzionamento
Delt.UP vede il gestionale come un insieme di "sistemi conferenti". Tali sistemi rendono disponibili i dati in essi contenuti sotto forma di "eventi elementari", caratterizzati da una causale guida, da dei codici di oggetti applicativi, e da una serie di valori/numeri. Il sistema elabora gli eventi mediante una sequenza di passi configurabili che depositano i valori nelle tabelle di risultato (finale o intermedie). Le tabelle di risultato sono concettualmente simili ad un foglio di calcolo elettronico :  i valori in esse registrati possono essere rielaborati con formule, possono dar luogo a ulteriori passi di algoritmo di trasformazione, oppure possono costituire la base per l'interrogazione, la stampa o l'output ad altro sistema di trattamento dati.

**Oggetto/Tema**
Ogni oggetto applicativo può essere titolare di un numero libero di "temi". Il tema è l'unione di  : 
 * una tripletta di oggetti (facoltativi)
 * un periodo (facoltativo)
 * una griglia di valori liberamente definita

Viene qui riportato un esempio : 

![AAP_AFC_04](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_04.png)

La griglia è un insieme di 99 valori ai quali è possibile
 * definire il significato
 * associare formule
 * associare riclassifiche
 * definire un valore come di totale
 * definire un valore come risultato di un calcolo da programma


**Budget**
Il budget è il sistema attraverso il quale, in fase preventiva, l'azienda definisce gli obiettivi strategici, i ricavi e i costi previsti nella loro distribuzione temporale, il modo con cui i costi vengono allocati alle diverse risorse in via preventiva per definire il costo previsto dei prodotti o delle attività della vendita. Delt.UP mette a disposizione vari strumenti a supporto di tali attività. Alcuni sono nelle funzioni generiche di base, altri sono specifici di questo modulo. Il budget può scomporsi in budget sezionali :  budget commerciale, budget della produzione, budget degli acquisti, budget finanziario ecc. Rimane valido il principio secondo il quale è più proficuo gestire ed archiviare le informazioni al livello opportuno. Ad esempio : 
 * Mediante la struttura dei "listini" potremo pianificare le percentuali di aumento per fornitore e famiglia di prodotto.
 * Potremo usare la "distinta" generica per definire associazioni di risorse (esempio distinta delle risorse critiche e relativo consumo)

Lo sviluppo del budget utilizza le funzioni standard del modulo MPS. Sarà così possibile associare previsioni con periodicità libera (giorno/settimana/mese o combinazione di questi) ad ogni coppia di oggetti,
Ad esempio : 
> Cliente/articolo              quantità di vendita prevista
 Agente/Nazione                fatturato
 Zona/modello                  volumi


Si possono tramite questo ottenere : 
 * Analisi a valore
 * Fabbisogni di materiali
 * Carichi per risorsa
 * Ecc.

Inoltre l'utilizzo della struttura tipica "oggetto/tema" permette di associare dei fattori specifici ad ogni combinazione prevista di oggetti applicativi. Citiamo ad esempio il costo per unità d'opera oppure numero previsto di righe d'ordine di acquisto ecc.

**Consuntivo**
Tutti gli strumenti cui si è fatto riferimento per il budget sono a disposizione anche delle funzioni di determinazione del consuntivo. Il consuntivo si ottiene attraverso l'elaborazione di un flusso di azioni che agiscono in modo parametrico sui sistemi conferenti per ottenere dati intermedi ed eventualmente da questi altri dati intermedi fino al risultato desiderato. Sviluppiamo quanto detto con un esempio abbastanza semplice : 
 * dal sistema conferente "dichiarazioni di attività produttive" ricavo i seguenti fattori
 ** per centro di costo
 *** ore di produzione effettiva
 *** ore previste a standard per le quantità effettive
 *** ore di fermo ecc.
 ** per dipendente / centro di costo
 *** ore di presenza
 *** ore di produzione effettiva
 * dal sistema conferente "gestione del personale" ricavo i seguenti fattori
 ** per dipendente
 *** ore lavoro ordinarie
 *** ore straordinarie
 *** costo
 * dal sistema conferente "contabilità generale" ricavo i seguenti fattori
 ** per centro operativo
 *** costo (dettagliato per natura)
 * elaboro
 ** attribuzione ai centri dei costi se dipendenti da indici (esempio energia in base a potenza e ore di funzionamento)
 ** ribaltamento dei costi dei centri ausiliari sui centri produttivi
 * ricavo
 ** per centro
 *** costo per unità di produzione (nel nostro esempio ore)
Il risultato ottenuto sarà input per elaborazioni successive quali il calcolo del costo del prodotto ecc.

**Analisi dei dati**
I dati generati saranno poi consultabili attraverso il modulo grafico Looc.UP oppure sarà possibile alimentare datawarehouse specifici.

## In sintesi
Sme.UP è un insieme di oggetti, moduli, funzioni e impostazioni, che permettono di modellare in modo diversificato e potente tutti gli aspetti organizzativi e gestionali delle aziende e quindi supportarle nella sfida della complessità che esse devono affrontare nel mercato attuale e futuro e verso qualsiasi approccio di tipo on demand.
La nostra convinzione è che gli attuali scenari in cui le aziende si trovano ad operare richiedono al software gestionale non solo un'elevata potenza applicativa esplicita ma un'altrettanta elevata potenza applicativa potenziale che possa essere resa esplicita rapidamente, con il minor sforzo possibile e senza intaccare la rigorosità delle applicazioni già rilasciate.
![AAP_AFC_05](http://localhost:3000/immagini/MBDOC_VIS-AAAFC/AAP_AFC_05.png)