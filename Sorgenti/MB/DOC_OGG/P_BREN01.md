# Obiettivo

La funzione ha l'obiettivo di gestire tutti i dati di anagrafica relativi ai contatti che interessano la gestione aziendale, tra i contatti possiamo elencare : 
 * L'azienda stessa
 * Clienti
 * Fornitori
 * Agenti
 * Collaboratori esterni
 * Banche


Ciascuna di queste diverse tipologie di ente è caratterizzata dal _2_Tipo ente. La tabella BRE raccoglie tutte le impostazioni principali del tipo ente.

## Formato guida

Selezionando la voce di Gestione anagrafica verrà aperta le seguente schermata in cui è necessario indicare il codice dell'ente che si vuole gestire e la relativa opzione : 

![BRENTI_013](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_013.png)
In particolare, le opzioni disponibili sono : 
 * 01 - Inserimento
 * 02 - Modifica
 * 03 - Copia
 * 04 -Cancella
 * 05 - Visualizza
 * 06 - Stampa

La scelta del codice ente potrà essere effettuata utilizzando i classici caratteri di ricerca. Per maggiori informazioni su questi caratteri si veda il seguente link : 

- [Ricerche](Sorgenti/MB/DOC_OPE/B£_RIC)

Dal formato guida è possibile accedere alle parzializzazioni tramite il tasto F13 o digitando il relativo bottone : 

![BRENTI_023](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_023.png)
Attraverso le parzializzazioni è possibile filtrare la lista di enti restituita dall'interrogazione. Sono presenti due schermate di campi attraverso cui è possibile filtrare la lista :  in particolare nella prima schermata è possibile indicare l'ordinamento dei record, lo schema di visualizzazione e filtrare sui principali campi dell'anagrafica enti. Nella parte inferiore della schermata è possibile eseguire una scansione del codice o della descrizione dell'ente. Questa funzione è particolarmente utile nel caso in cui si conosca solo una parte della descrizione o del codice dell'ente ma non si sappia in che posizione si trovi la parte conosciuta. Ipotizziamo ad esempio di voler visualizzare tutti i clienti che abbiano all'interno della descrizione "Avvocato" allora potremo compilar eil campo Scansione Descrizione con *Avvocato*.
Dalla prima schermata delle parzializzazioni digitando nuovamente F13 si accede alla seconda schermata delle parzializzazioni attraverso cui è possibile filtrare su altri campi : 

![BRENTI_024](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_024.png)
Nel caso in cui venga spesso eseguito uno stesso filtro sui record del formato lista è possibile memorizzare il filtro stesso attraverso le Memorizzazioni.

Per maggiori dettagli sulle parzializzazioni e sulle memorizzazioni si rimanda alla seguente documentazione : 

- [Parzializzazioni](Sorgenti/MB/DOC_OPE/B£_PAR)

## Formato dettaglio
Il formato di dettaglio che si presenta è il seguente : 
![BRENTI_014](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_014.png)
Entrando nell'anagrafico dell'ente selezionato è possibile vedere che le voci sono raggruppate per informazioni contenute. In particolare è possibile visualizzare le seguenti macroclassi :  dati identificativi, livello e stato, dati ambientali, dati di contatto, dati fiscali, dati di incasso/pagamento, dati di spedizione, dati di classificazione, dati di fatturazione, dati di movimentazione merce, dati provvigionali e dati aggiuntivi. Vediamo le principali voci che compongo questi gruppi.

 * Dati identificativi. Sono le caratteristiche identificative dell'ente :  ragione sociale, partita IVA, codice fiscale e rapporto fiscale. in particolare, questo ultimo campo permette di distinguere i percipienti dai non percipienti e le persone fisiche da quelle giuridiche.
 * Stato. Da qui è possibile impostare stato e livello dell'ente.
 * Dati ambientali. All'interno di queste voci è possibile definire la lingua, la valuta e gli indirizzi legali della società.
 * Dati di contatto. Sono i recapiti di contatto dell'ente :  telefono, fax, mail, responsabili da contattare,ecc.
 * Dati fiscali. All'interno di questa voce sono riportate le informazioni relative all'assoggettamento IVA principale dell'ente e alle diichiarazioni presentate (che vengono registrate all'interno dell'applicazione BR). Questi dati vengono poi ripresi all'interno delle testate di documenti e registrazioni e considerati per il calcolo dell'IVA.
 * Dati di incasso/pagamento. All'interno di questo gruppo è possibile riportare informazioni relative al pagamento preferenziale dell'ente e i dati relativi allo stesso (banca e conto contabile). All'interno di questi dati è possibile indicare sia la banca dell'ente che la banca aziendale; quest'ultima andrà indicata nel campo 'Banca azienda'.
 * Dati di spedizione. All'interno di questo gruppo è possibile riportare le informazioni circa le spedizioni verso l'ente. E', infatti, possibile definire come ente di spedizione un codice cliente oppure codificare una tipologia di ente apposita per le spedizioni.
 * Dati di classificazione. E' obbligatorio inserire la categoria contabile a cui appartiene l'ente; il campo 'Insollecitabilità' viene compilato nel momento in cui si voglia impedire di inviare solleciti all'ente; il campo 'Raggruppamento documenti' riguarda la creazione di fatture partendo da bolle :  compilando questo campo alla generazione delle fatture le bolle verranno presentate raggruppate in un unico documento (è possibile dividerle in un secondo momento). Il campo 'Cumulo' serve, invece, per la gestione delle pratiche e dichiara se sia obbligatorio o meno cumulare le rate dell'ente.
 * Dati provvigionali. In questa sezione è possibile indicare agenti e relative provvigioni associati al cliente.

Tutti i campi dell'anagrafica sono sottoposti ad autorizzazione, di conseguenza, vengono presentati e/o resi disponibili alla manutenzione solo i dati a cui l'utente è autorizzato :  ad esempio un utente commerciale potrà gestire l'indirizzo, oppure la lingua o il listino, mentre un utente contabile potrà gestire la partita IVA o la categoria contabile, ecc.

### Informazioni particolari - dati relazionali

Nei dati relazionali possono essere indicati eventuali enti che sono in relazione con quello in gestione : 
![BRENTI_015](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_015.png)
I campi si compilano solo quando le funzioni a cui sono relativi vengono svolte da altri codici
 * _2_Ente di spedizione, viene utilizzato nel caso all'ente in gestione sia associato uno ed un solo indirizzo di spedizione (quando possono esistere diversi indirizzi di spedizione merce si passa alla gestione dei dati aggiuntivi ente)
 * _2_Ente di contabilizzazione, identifica il codice da utilizzare quando si passa alla contabilizzazione dei documenti relativi a questo ente
 * _2_Ente di trattamento prezzo, viene utilizzato per accedere al listino
 * _2_Ente di corrispondenza, viene utilizzato per l'invio di documenti "cartacei" es. la conferma d'ordine (nota, in sostituzione ai documenti cartacei possiamo utilizzare questo ente per l'invio di e-mail)
 * _2_Ente vettore, nel caso l'ente abbia un vettore preferenziale e questo sia codificato in anagrafico come un altro ente

Questi vari codici ente vengono utilizzati nella gestione dei documenti, tipica del ciclo esterno (applicazione V5).

## Particolarità - Attivazione nuova gestione azioni
Quando è stata sviluppata l'applicazione "Workflow" è nata la necessità di gestire determinati oggetti da parte del workflow e quindi i normali programmi di gestione potevano avere comportamenti contrastanti rispetto al processo disegnato con il workflow (es. se viene messa sotto workflow l'anagrafica clienti il processo potrebbe decidere che solo l'utente che ha iniziato la creazione è autorizzato alla modifica delle descrizione, questo potrebbe contrastare la gestione autorizzazioni per la quale tutti gli utenti autorizzati possono modificare la descrizione indipendentemente da quale utente abbia creato il codice). Per omogeneizzare le necessità del workflow e quelle della gestione anagrafica degli oggetti si è sviluppata una nuova modalità di gestione azioni che passa da un unico programma di lancio e poi agisce differentemente a seconda dell'oggetto da gestire. Se questa nuova gestione è attivata il formato guida si presenta con una forma leggermente diversa : 
![BRENTI_016](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_016.png)
# Particolarità - Attivazione nuova gestione enti
La gestione enti ha avuto nell'ultimo periodo una evoluzione verso una gestione enti multiaziendale (lo stesso anagrafico è utilizzato da varie aziende e può essere visto a seconda dell'azienda sotto ruoli diversi es. fornitore per un'azienda e cliente per un'altra). Se attiva questa gestione nasce la necessità di configurare il formato gestione dati a seconda dell'azienda e della funzione che deve visualizzare o gestire le informazioni associate all'ente, è stato quindi sviluppato un nuovo programma in grado di gestire il data entry configurabile : 
![BRENTI_017](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/BRENTI_017.png)
## Gestioni specifiche
A seconda che si utilizzi questa funzione per gestire un fornitore, un cliente o una banca si dovranno seguire delle regole e gestire delle informazioni specifiche, di seguito riportiamo le più significative.

### Gestione anagrafica aziende
La contabilità è _2_multiaziendale; ciò significa che un singolo utente può agire alternativamente su un'azienda e successivamente su un'altra semplicemente modificando il campo 'Azienda' compilato al lancio delle funzioni.

La voce di menù relativa all'anagrafica aziendale, si trova tra i "Dati base" sotto la voce 'Azienda'.
![C5BASE_001](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_001.png)Da questa schermata è possibile accedere alla gestione dell'anagrafica azienda, che essendo vista come un ente viene gestita dal file BRENTI0F.
In questo file infatti, vengono definiti tutti gli enti (cioè banche, clienti, fornitori, collaboratori, ecc).

All'interno del formato guida è possibile selezionare l'azione che si vuole eseguire, l'azienda e la prospettiva, ovvero la sezione di anagrafica che si vuole visualizzare : 

![C5BASE_002](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_002.png)
![C5BASE_003](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_003.png)
Dopo aver scelto i parametri di visualizzazione si aprirà la schermata relativa all'anagrafica dell'azienda scelta : 

![C5BASE_004](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_004.png)
I dati obbligatori sono :  la ragione sociale, la partita IVA e il rapporto fiscale (persona giuridica, fisica, ecc...).
Oltre a questi è possibile inserire altre informazioni : 

 * codice fiscale
 * partita IVA CEE
 * stato e livello
 * lingua
 * valuta
 * dati di contatto (indirizzi, telefoni, mail, persone da contattare, .. )
 * dati fiscali (assoggettamenti IVA, eventuali dichiarazioni d'intento ed esenzioni)
 * dati di incasso (pagamento preferenziale  e dati relativi alle banche aziendali)
 * dati di spedizione e consegna
 * dati di fatturazione
 * dati relativi alle provvigioni.

### Parametri fissi azienda (Dati base - Contabilità)

![C5BASE_006](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_006.png)
In tutto Sme.UP è possibile associare ad ogni oggetto dei parametri che vannoaggiungere dettegli, informazioni ulteriori all'oggetto. Per l'azienda questi parametri assumono particolare importanza, per questo sono riportati all'interno del menù della contabilità sotto la voce 'Parametri fissi' : 

![C5BASE_007](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_007.png)
Le informazioni sono divise in categorie :  Dati generali, Dati IVA, Dati giornale, Identificazione, Concessioni, Fonti fisse ADF, Cespiti, Varie.

Analizzeremo qui di seguito alcuni dei campi principali di questa schermata : 

DATE GENERALI
 * La **Divisione unica**  (elemento della tabella C5Q) è un campo significativo per la contabilità, che individua la presenza di settori nell'azienda, questo viene fatto allo scopo di suddividere l'attività contabile.
 * La **Divisione fiscale**  è un campo creato allo scopo di suddividere i registri IVA, ed altri aspetti fiscali, per quelle aziende che si dividono in più settori d'attività. E' un campo che può assumere valore SI/NO.
 * Il campo **Lista librerie** elenca le librerie utilizzate dall'applicazione (elementi della B£B).

DATI IVA
 * I campi :  **Periodo/Giorno Liquidazione IVA** e **% Interessi Liquid.**, riguardano i dati relativi all'IVA, ovvero il periodo di liquidazione (mensile, trimestrale o annuale), l'indicazione del giorno in cui l'IVA va liquidata e l'eventuale tasso di interesse da calcolare sul modello F24 in caso di ritardato pagamento dell'IVA stessa.
 * L' **Azienda compensazione IVA**, riporta il codice della capogruppo che verserà l'IVA al fisco, ovvero quella su cui confluiranno crediti e debiti delle altre aziende del gruppo.
 * Se i campi **Dati integrativi registri IVA** e **Sintesi registri riepilogativi IVA** hanno valore 1 (SI), in fondo alla stampa del registro IVA verrà riportato un breve riepilogo.
 * **Plafond mobile** :  è sostanzialmente il tetto massimo di acquisti che possono essere effettuati senza assoggettamento IVA, e può essere inteso come plafond mensile o annuale. Questo campo nasce dall'esigenza delle aziende che esportano molto, e che hanno quindi difficoltà a recuperare l'IVA (perchè i clienti esteri non la pagano). Lo Stato allora mette a disposizione la possibilità di dichiarare la percentuale di fatturato dovuto alle esportazioni e chiedere ai fornitori di emettere fatture esenti IVA (art. 8/c legge 633/72) fino al raggiungimento di un certo importo attraverso una dichiarazione d'intento. Le aziende che effettuano sia prestazioni esenti da IVA, che prestazioni soggette a IVA, non possono detrarre completamente l'IVA degli acquisti dall'ammontare che devono pagare al Fisco ma possono detrarne solo una % proporzionale al volume di prestazioni soggette a IVA (art. 19bis DPR 633/72). Questa percentuale è chiamata pro-rata ed è determinata una volta all'anno basandosi sulle operazioni eseguite l'anno precedente con la seguente formula :  A/(A+B) dove A sono le operazioni che danno diritto a detrazione e B quelle esenti. Se a fine anno la % risulta differente si dovrà effettuare un conguaglio. Riassumento in questo campo va semplicemente indicato se vi è questa possibilità a disposizione dell'azienda.
 * La **% Pro-rata** serve alla aziende, come già detto sopra, per definire la percentuale di detrazione dell'IVA acquisti da applicare nel caso siano presenti vendite che non danno diritto a detrazioni.
 * Il campo **Registri Riferimento Esigibilità Differita**, se presente, è un elemento della C5R che riporta il registro su cui vengono riportate le registrazioni di IVA differita; in poche parole, le aziende che hanno come clienti enti pubblici hanno la possibilità di pagare l'IVA sulle fatture emesse al verificarsi del pagamento della fattura stessa (che spesso avviene anni dopo l'emissione). Viene, quindi, creato un registro IVA apposito in cui vengono riportate le registrazioni di IVA differita, il sistema è in grado di gestire in modo differente queste registrazioni pagando l'IVA solamente nel momento in cui viene incassata la fattura.
 * La **Cessione del credito IVA**  viene fatta al fine di coprire un debito, ad esempio anticipo i soldi ad un fornitore cedendogli la mia IVA a credito.
 * Il **Plafond in liquidazione IVA**  è un campo nato con lo scopo di aggiungere al documento IVA, un'ulteriore informazione relativa al plafond usato.

DATI GIORNALE
Nascono allo scopo ultimo della contabilità e sono l'elenco cronologico di tutte le registrazioni effettuate nel periodo. Il libro giornale è un libro obbligatorio e soggetto a bollatura.
 * La **Stampa bollato estesa** permette di impostare il numero di caratteri stampati per riga sul libro giornale. (se è flaggato a SI è possibile stampare a 198 caratteri, altrimenti a 132).
 * **Paginazione bollato** :  riguarda la stampa del numero di pagina.
 * **Descrizioni aggiuntive su bollato** :  permette di aggiungere descizioni sul libro giornale.
 * **Note E4/E5 su bollato** :  rispettivamente gli oggetti E4 e E5 sono l'oggetto di testata (file C5TREG0F) e l'oggetto riga (file C5RREG0F) delle registrazioni contabili, ai quali possono essere associate delle note, che possono o meno essere riportate sul libro giornale impostando questi campi.
 * Il campo **Anno riferimento da data inizio** riporta l'anno a cui si riferisce il giornale, è un campo non utilizzato.
 * I campi **Progressivo giornale**, **Ultima riga giornale** e **Ultima pagina giornale** si riferiscono alle informazioni di chiusura di un giornale e che devono essere riprese sul giornale successivo.
 * Il libro giornale deve essere bollato ma non su tutte le pagine :  con il campo **Pagina Bolli su Bollato posso dichiarare su quali pagine è stato messo il bollo.

IDENTIFICAZIONE
E' caratterizzato dall'insieme dei campi di identificazione della società :  capitale sociale, data inizio attività, casella postale, dati della camera di commercio, ecc.

CONCESSIONI
Qui invece sono riportate tutte le informazioni circa le concessioni dell'azienda.

FONTI FISSE ADF
Le fonti fisse ADF sono relative ai flussi di cassa, e quindi più in generale riguardano l'analisi della disponibilità finanziaria. In particolare le fonti fisse sono i dati minimi (le informazioni sui clienti, fornitori e sui conti), nello specifico sono gli estratti conto e gli scadenziari di clienti e fornitori, la situzione di cassa e i pagamenti attesi.

CESPITI
Nel campo **Dettaglio movimenti stampa libro** viene deciso se riportare a libro giornale tutti i movimenti dettagliati dei cespiti.

VARIE
Sotto questa voce vengono riportati diversi parametri relativi all'azienda come il contenitore delle note o il rappresentante legale (ovvero chi è autorizzato a depositare bilanci e altre dichiarazioni telematiche).

### Gestione banche
Attraverso questa voce di menù è possibile gestire l'anagrafica banche : 

![C5BASE_017](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_017.png)
Nella schermata che si  apre alla richiesta da parte dell'utente è necessario selezionare l'azione da eseguire e il codice della banca. In Sme.UP la banche sono codificate tramite il loro codice ABI- CAB che consente di identificarle in modo univoco; di conseguenza, nel caso in cui si abbia la necessità di inserire una nuova banca la si deve identificare con i suoi codici ABI-CAB.

![C5BASE_018](http://localhost:3000/immagini/MBDOC_OGG-P_BREN01/C5BASE_018.png)
una volta selezionata l'azione da eseguire e la banca è possibile confermare e, quindi, visualizzare l'anagrafica della banca per completarla.
