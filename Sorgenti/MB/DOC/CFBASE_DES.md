# Visione Configuratore
L'idea di base che ha ispirato lo sviluppo di Build.up è quella di fornire alle aziende un valido strumento informatico di supporto al delicato processo di configurazione di un prodotto.

## Necessità della configurazione
Prima di presentare le numerose funzionalità applicative offerte dal programma è necessario introdurre le problematiche tipiche del contesto operativo in cui il programma stesso si troverà ad operare.
Il problema della configurazione si presenta ogni qual volta un'azienda si trova nella situazione di dover definire completamente un prodotto raccogliendo in modo organico tutte le informazioni necessarie alla sua produzione e commercializzazione.

Di norma, la definizione di una configurazione richiede la raccolta di informazioni di tipo eterogeneo :  ad informazioni tecniche, come materiali, tipo di lavorazione, ecc., potrebbero essereaffiancate anche informazioni commerciali come modalità di pagamento o di fatturazione.

La quantità e la natura delle informazioni da raccogliere è variabile e dipende fortemente sia dal contesto operativo che dalla fonte di informazioni disponibile.
L'oggetto che permette la raccolta delle informazioni è il configuratore che, nel caso più semplice, potrebbe essere il classico questionario cartaceo caratterizzato da una struttura rigida e prefissata.
A prescindere dal tipo, è importante che il configuratore sia in grado di raccogliere tutte le informazioni necessarie alla definizione del prodotto e, se possibile, ottimizzare il processo alla raccolta alle sole informazioni effettivamente necessarie.

La definizione di un configuratore può avere vari livelli di sofisticazione la cui scelta è legata principalmente al grado di conoscenza del prodotto della persona o ente che fornirà le informazioni :  pertanto, mentre il questionario da sottoporre ad un cliente inesperto del prodotto dovrà essere maggiormente controllato per garantire la definizione di una configurazione effettivamente gestibile dall'azienda, quello destinato ad una persona esperta potrà garantire un numero maggiore di gradi di libertà e alleggerire il carico dei controlli.

Ovviamente, maggiori controlli comportano una maggiore sicurezza sui risultati ottenuti ma portanoad una minore elasticità, intesa come maggior difficoltà nella gestione di situazioni non previste all'atto della creazione del configuratore.

Il tipico processo di configurazione parte dalla descrizione generica di un prodotto, caratterizzata da una serie più o meno numerosa di varianti, per arrivare alla completa definizione di un oggetto specifico.

Lo schema di massima di questo processo è illustrato dalla figura 1.

![CFBASE_034](http://localhost:3000/immagini/CFBASE_DES/CFBASE_034.png)Figura 1 :  Schema generale del processo di configurazione


Ad ogni oggetto configurabile si associa un configuratore la cui compilazione, intesa come esecuzione dello stesso, porta alla definizione prima della configurazione e da essa dell'oggetto configurato.

Un configuratore può essere utilizzato sia per definire un prodotto singolo sia un insieme di prodotti appartenenti alla stessa famiglia :  pertanto, un'azienda può decidere di sviluppare un configuratore per ognuno dei prodotti in catalogo oppure un unico configuratore che gestisca contemporaneamente la definizione di tutti i prodotti disponibili.

In generale, una volta che un configuratore è stato creato viene utilizzato più volte :  quindi, mentre la definizione di un configuratore è un'operazione delicata, poco frequente e in genere eseguita da una o poche persone, la sua esecuzione è invece un'operazione che viene ripetuta molte volte e probabilmente da molte persone diverse.

# Il Configuratore Build.up
## Scopi del programma
Build.up si presenta sul mercato come un programma di gestione delle configurazioni di concezione moderna e basato su tecnologie sicuramente innovative per questo tipo di prodotti.
Rispetto al classico questionario su carta offre un ambiente di sviluppo visuale di sicuro interesse e funzionalità avanzate di grande utilità operativa.

Lo scopo di Build.up è sostanzialmente uno :  definire un oggetto in ogni sua parte attraverso un meccanismo di domande e risposte (un po' come nel gioco in cui si deve individuare un personaggio famoso ponendo una serie di domande ad una seconda persona).

Il primo passo è quello di individuare tutte le varianti nella definizione dell'oggetto configurabile cioè tutte le caratteristiche o informazioni che devono essere conosciute per la sua completa definizione.
Sulla base delle varianti individuate nella prima fase è possibile implementare un questionario per la raccolta di tutte le informazioni necessarie, questionario che verrà infine proposto ad un utente finale perché possa essere compilato.

Un questionario ben progettato e compilato con cura conterrà tutte le informazioni necessarie alla completa conoscenza dell'oggetto per cui è stato creato.
Le funzionalità di base di Build.up dovranno pertanto essere le seguenti : 

- _2_Definizione di un questionario :  Build.up offre un ambiente visuale per una agevole creazione e manutenzione di qualsiasi questionario. L'ambiente di sviluppo è semplice ed intuitivoed è strutturato in modo tale da "costringere" l'utente ad una corretta gestione dei dati, facilitando la creazione di questionari esaustivi. In Build.up un questionario è denominato configuratore.
- _2_Compilazione di un questionario :  una volta creato, un questionario deve essere proposto ad un utente perché possa essere compilato. In Build.up la compilazione di un questionario è detta esecuzione di un configuratore; questa operazione consiste nel visualizzare le domande in un ambiente grafico, raccogliere le risposte date dall'utente e, dopo averle controllate, memorizzarle nel modo opportuno. Un configuratore eseguito completamente dà luogo ad un oggetto chiamato configurazione, concettualmente un questionario compilato.
- _2_Memorizzazione della configurazione :  la configurazione, viene salvata in un file su AS400,che viene usato come contenitore di tutte le configurazioni realizzate. Una volta memorizzata, la configurazione deve essere utilizzata nell'ERP. Questa fase dipende strettamente dall'oggetto che si sta configurando. Se si sta configurando un ordine di vendita la configurazione può essere utilizzata per creare la distinta base, se invece si sta configurando una commessa deve essere istanziato su AS400 l'oggetto di tipo commessa che è stato configurato. Una soluzione generale non esiste ma deve essere creata ad hoc per ogni esigenza specifica.

È comunque garantita l'integrabilità con il sistema gestionale in quanto i risultati della configurazione sono disponibili su AS400 e quindi utilizzabili da qualunque applicazione ne abbia bisogno.

I prodotti finali di Build.up sono quindi due oggetti, il configuratore e la configurazione :  il primo definisce la struttura di un questionario, le sue domande e i suoi controlli mentre il secondo raccoglie le risposte date a seguito di una compilazione del questionario.

Se ben strutturato, l'insieme delle domande e delle relative risposte consente la completa definizione di qualsiasi oggetto; da notare che un configuratore può essere mandato in esecuzione più volte e quindi da un unico questionario possono essere generate più configurazioni,una per ogni compilazione.

Sia i dati contenuti nel configuratore che quelli delle relative configurazioni sono accessibili da parte di qualsiasi programma a cui possano servire e possono pertanto rappresentare la base per una grande varietà di elaborazioni successive.

Le principali caratteristiche tecniche di Build.up possono essere riassunte nei seguenti punti : 

- _2_Struttura client-server e web :  la costruzione del questionario avviene all'interno di LoocUp o via terminale 5250. La compilazione e l'interrogazione, avvengono sia in LoocUp sia via browser (richiesti browser di ultima generazione)
- _2_Ambiente di sviluppo grafico :  con una interfaccia visuale per una semplice definizione delconfiguratore :  la creazione del questionario è completamente guidata da pannelli di inserimento,di significato semplice ed intuitivo. Un configuratore può essere modificato in ogni momento ed adattato alle mutate esigenze operative in modo semplice e veloce.
- _2_Esecuzione dinamica del questionario :  le domande vengono sottoposte all'utente non in ordine prefissato ma secondo una sequenza definita dinamicamente in funzione delle risposte date e delle regole di esecuzione.
- _2_Possibilità di definire delle regole :  utilizzando un linguaggio proprietario di struttura semplice ed intuitiva. Si tratta di un linguaggio completo, che associa alla potenza offerta dai suoi costrutti la semplicità ed immediatezza del normale parlato. La scrittura delle regole è facilitata dalla presenza di un completo controllore sintattico, capace di suggerire le soluzioni adatte ad ogni tipo di errore di sintassi.
- _2_Struttura dinamica del questionario :  Possibilità di modificare la struttura del questionario durante la compilazione interagendo con un programma su AS400.
- _2_Generazione di PDF :  sulla base delle risposte fornite è possibile generare un PDF e di arricchirlo con dati prelevati dal gestionale.
- _2_Invio di e-mail multiple con allegati :  terminata la compilazione o consultando le precedenti configurazioni salvate è possibile inviare a una o più persone uno o più allegati dei PDF generati.
- _2_Gestione delle autorizzazioni :  tutte le funzioni del programma possono essere utilizzate solo dagli utenti autorizzati al loro utilizzo. E' prevista la definizione di autorizzazioni parziali e la gestione di gruppi di lavoro, intesi come gruppi di utenti con uguali autorizzazioni.
- _2_Integrazione con l'ambiente gestionale su AS/400 :  i dati prodotti da Build.up sono disponibili su oggetti AS/400 e sono pertanto utilizzabili da qualsiasi applicativo gestionale presente sul sistema.


## Funzionalità specifiche di Build.up
Build.up non si limita a riproporre in un contesto informatico le stesse funzionalità offerte da un questionario su carta; al contrario, il programma consente di impostare il lavoro di configurazione secondo un approccio dinamico ottimizzato alla raccolta di informazioni.

Le caratteristiche peculiari del programma si possono riassumere brevemente nei seguenti punti : 

- _2_Personalizzazione del configuratore :  la definizione del questionario è interamente personalizzabile in funzione delle diverse esigenze informative che si possono presentare ed offreun gran numero di gradi di libertà per favorire la perfetta adattabilità del configuratore alle esigenze più disparate. La definizione del questionario non è vincolata ad uno schema rigido ma può essere strutturata in modo da favorire un'organizzazione ottimale delle informazioniraccolte.
- _2_Manutenzione agevolata :  una volta creato, un configuratore può essere facilmente modificato in ogni momento senza richiedere la sua completa ridefinizione. E' quindi facile aggiornare un questionario per allinearlo a mutazioni improvvise delle esigenze aziendali. La semplicità di inserimento delle modifiche invita ad uno sviluppo incrementale del configuratore :  partendo da una prima definizione semplificata si può arrivare in poco tempo a configuratori moltocomplessi ed articolati operando di volta in volta piccole modifiche e valutando man mano gli effetti ottenuti.
- _2_Adattabilità al contesto operativo :  accade di frequente che all'interno di uno stesso contesto operativo si debbano raccogliere informazioni di tipo eterogeneo (ad esempio, un configuratore potrebbe raccogliere contemporaneamente informazioni tecniche ed informazioni commerciali). Build.up è in grado di trattare informazioni di qualsiasi tipo e di eseguire un rigoroso controllo sul tipo di risposta data in funzione di quella attesa.
- _2_Ottimizzazione del questionario :  un questionario su carta, basato su una struttura forzatamente fissa, non permette alcun controllo sulla sequenza con cui vengono poste le domande. In molte situazioni questo porta alla raccolta di una quantità di informazioni superiore a quella effettivamente necessaria alla definizione dell'oggetto, con la conseguenza di appesantire notevolmente la gestione dei dati. In Build.up la sequenza con cui vengono poste le domande viene costruita in modo dinamico in funzione delle risposte date dall'esecutore alle domande precedenti. L'utente dovrà pertanto rispondere alle sole domande necessarie alla definizione della configurazione e non verrà quindi sviato da domande incongruenti con il contesto operativo in cui sta operando.
- _2_Linguaggio delle regole :  Build.up consente l'introduzione nel questionario di regole scritte in un linguaggio semplice ed intuitivo (vedremo un esempio più avanti). Le regole hanno molteplici funzioni :  controllare la sequenza di esecuzione del configuratore, verificare le risposte date dall'utente, effettuare calcoli di vario tipo, gestire i valori di risposta predefiniti ed altro ancora. Attraverso le regole è possibile dare un'intelligenza propria al configuratore e garantirgli quel comportamento dinamico che lo rende unico nel suo genere. Per facilitare l'inserimento delle regole Build.up è dotato di un completo controllo sintattico in grado di suggerire per ogni errore le eventuali correzioni da introdurre.

Per quanto detto Build.up rappresenta un valido ausilio in tutti i processi in cui è necessaria una raccolta di informazioni ottimizzata, trova valide applicazioni in molti contesti applicativi ed in particolare nella definizione di offerte commerciali, nell'acquisizione di ordini clienti, nella definizione della distinta base di un prodotto e nella definizione dei cicli di produzione.

## Caratteristiche tecniche fondamentali
Dopo aver presentato a grandi linee le funzionalità di Build.up ci possiamo addentrare più a fondo nella comprensione dei meccanismi di funzionamento di questo programma.

Prima di affrontare la questione della creazione di un configuratore è necessario capire la struttura base di questo componente e quali sono gli oggetti principali che lo compongono. La Figura 2 riassume graficamente lo schema costruttivo di un configuratore generico.

![CFBASE_038](http://localhost:3000/immagini/CFBASE_DES/CFBASE_038.png)Figura 2 :  Struttura di un questionario Base

L'oggetto base è il configuratore, formato da una lista di sezioni definita in un ordine qualsiasi. Ogni sezione contiene un certo numero di domande, ognuna delle quali è di tipo prefissato, ed ha associato una variabile in cui si salverà la risposta data. Alcune domande possono avere associati anche una serie di valori che rappresentano le opzioni predefinite di risposta.
Si possono individuare nel configuratore cinque elementi fondamentali : 

| 
| .COL A="L" |
| ---|----|
| 
| .COL LunAut="1" |
| __Domande__ | sono l'elemento base del configuratore. Sono oggetti costituiti principalmente da una descrizione, che rappresenta il testo della domanda, e da una variabile in cui verrà salvata la risposta data dall'utente in fase di esecuzione. Sono stati definiti diversi tipi di domanda, in funzione del tipo di risposta prevista e del formato grafico di visualizzazione; nel seguito della relazione verranno descritti dettagliatamente. |
| __Sezioni__ | per garantire una migliore organizzazione del configuratore le domande vengono raggruppate all'interno di sezioni secondo criteri di omogeneità. La sezione rappresenta il modulo unitario di visualizzazione :  durante l'esecuzione del questionario le sezioni vengono visualizzate una per volta e le domande in esse contenute vengono sottoposte all'utente affinché possa rispondere. Non esiste alcuna connessione tra la sequenza con cui sono state create le sezioni e la sequenza con cui verranno visualizzate in esecuzione. |
| __Valori__ | i valori sono le opzioni (intese come possibili risposte) associate ad una domanda. In molti casi l'utente deve scegliere una risposta tra una lista di opzioni possibili :  i valori rappresentano i singoli oggetti tra cui l'utente può scegliere la sua risposta. |
| __Variabili__ | sono i contenitori in cui vengono salvate, durante l'esecuzione, le risposte date dall'utente. Ad ogni domanda creata deve essere associata una variabile di tipo conforme allanatura dei dati attesi come risposta :  pertanto, se una domanda chiede l'inserimento di un dato numerico la variabile ad essa associata dovrà essere anch'essa numerica. Ogni tentativo di salvarein questa variabile una risposta non numerica produrrà automaticamente un errore di tipo e l'immediata segnalazione all'utente. |
| __Regole__ | un discorso più approfondito è necessario per introdurre le Regole, data l'importanza di questi elementi nella definizione delle prestazioni di un configuratore. Grazie alle regole, infatti, il configuratore si comporta in modo diverso a seconda delle risposte che di volta in volta l'utente inserisce. Nel capitolo dedicato al linguaggio delle regole descriviamo approfonditamente questo argomento, ponendo particolare attenzione al lavoro svolto da noi nella definizione di questo linguaggio. |
| 


### La Struttura Estesa
Nella figura 3 trovate la struttura estesa del questionario : 

![CFBASE_025](http://localhost:3000/immagini/CFBASE_DES/CFBASE_025.png)Figura 3 :  La struttura del questionario estesa.

Come si può notare la versione estesa del questionario ammette quattro tipi di sezione : 

- _2_Le sezioni che contengono domande
- _2_Le sezioni ripetibili :  sono sezioni che vengono dichiarate ripetibili e che mediante regole, implicite o esplicite, l'utente può ripetere n volte. Contengono al loro interno domande.
- _2_Le sezioni che includono un questionario :  sono sezioni che non contengono domande ma che contengono un questionario. La sezione si esploderà quindi nelle sezioni contenute nel questionario incluso. La compilazione di una sezione di tipo questionario equivarrà allla compilazione delle n sezione incluse.
- _2_Sezioni che contengono un questionario e che sono ripetibili :  rappresentano l'unione dei concetti 2 e 3. Sezioni di questo tipo consentono di definire n elementi complessi all'interno di un questionario.

La nuova struttura consente la definizione di questionari multi livello poiché un questionario può essere composto da sezioni che sono a loro volta questionari. Si può così superare il vincolo di non poter definire n oggetti complessi in un'unica configurazione e di poter seguire più agevolmente la struttura di una distinta base.

Questa nuova struttura consente anche di definire e riutilizzare micro configuratori all'interno di strutture più complesse.

Tale divisione agevola la manutenzione perchè le domande in gioco in un micro configuratore sono meno di un unico grande configuratore e specifiche per una parte.

Un questionario può inoltre essere definito all'interno di script, rendendo più veloce la compilazione e la manutenzione in quanto tutte le informazioni sono in un unico membro del file SCP_CFG.

La nuova struttura impone un vincolo sul formato e sul luogo delle risposte raccolte :  venendo menol'assunto che il codice di una domanda sia univoco all'interno di un questionario si ha che le risposte descrivono un albero che segue la struttura del questionario. Le risposte risulteranno così suddivise per sezione.


## Integrazione col sistema gestionale
Quando si progetta un configuratore bisogna tenere presente che un suo prerequisito fondamentale deve essere la possibilità di interfacciarsi col sistema gestionale esistente nell'azienda. Interfacciarsi significa dare allo strumento la possibilità di estrarre, immettere, o elaborare informazioni significative per la gestione dell'azienda stessa. Uno strumento che raccoglie semplicemente informazioni (magari le risposte ad alcune domande) e le salva, per esempio, in un foglio Excel ha un'utilità relativa. Esso richiede comunque la presenza di un operatore che, leggendo tale documento, inserisce le informazioni nel posto giusto del sistema informativo. Questa fase del processo di introduzione dei dati (ad esempio un ordine di acquisto) può essere lunga e soprattutto non esente da errori. Un errore in questo punto vanifica tutto il lavoro compiuto per presentare una configurazione corretta. Anche l'impiego della configurazione nel gestionale dovrebbe dunque essere automatizzata.

A questo punto riteniamo doveroso fare una precisazione. Quando si costruisce uno strumento come il configuratore e si decidono quali funzionalità deve svolgere e quali problemi deve risolvere, bisogna considerare che i suoi utilizzatori finali possono essere di diversa natura e avere necessità differenti. Per questo motivo lo strumento che si realizza sarà composto sia da parti standard che da parti che dovranno essere soggette a personalizzazioni sulla base delle caratteristiche del cliente (o del suo sistema gestionale).

Riferendoci a Build.up questa separazione è abbastanza evidente soprattutto per quanto riguarda il livello di integrazione con l' E.R.P.

Quando si costruisce un questionario, infatti, si inserisce nel configuratore una serie di domande, alcune delle quali tipizzate. Ricordiamo che una domanda è tipizzata quando alla sua risposta è associato un Tipo di oggetto. Esempi di queste domande sono la richiesta di una data, che sulla base della risposta istanzia un oggetto applicativo di tipo Data, oppure la richiesta di un articolo che ha, tra le risposte possibili, l'elenco degli articoli (ognuno di essi è un oggetto applicativo) tra i quali l'utente può scegliere quello desiderato. In entrambi i casi viene stabilita una relazione tra l'oggetto che sto configurando e l'oggetto istanziato dalla risposta (la data) o l'oggetto scelto dall'elenco (l'articolo). Questo approccio produce una seriedi innegabili vantaggi. In primo luogo viene evitata la duplicazione dei dati perché decidendo, ad esempio, che una domanda è di tipo Articolo l'elenco di tutti gli articoli non deve essere copiato nel configuratore, ma il configuratore automaticamente si preoccupa di andare a leggere tale elenco nell'unico punto del gestionale in cui è presente. Evitare la duplicazione dei dati porta dei risparmi economici all'azienda, dovuti al risparmio delle spese di manutenzione e gestione dei dati stessi, nonché ad una limitazione dello spazio fisico occupato [13]. In secondo luogo la manutenzione dei questionari viene notevolmente ridotta, in quanto se inserisco un nuovo articolo nel sistema automaticamente questo sarà disponibile nell'elenco degli articoli associato alla domanda, senza dover compiere nessuna operazione particolare. Questa parte è standardizzata, in quanto i dati necessari al configuratore vengono letti direttamente nel database e passati in formato XML, indipendentemente dalla struttura gestionale sottostante.

La parte del configuratore, legata all'integrazione col gestionale, che non è standardizzabile è il processo che, partendo dalla raccolta delle risposte ad un questionario di configurazione di un prodotto porta, ad esempio, alla costruzione di una distinta base. Questo limite è dovuto al fatto che aziende differenti gestiscono la loro distinta base in modi differenti.

## Il Questionario visto da Looc.up
Anche il configuratore utilizza Looc.up come strumento di interfaccia verso l'utente.

Chi scrive questionari utilizzerà questo client grafico visibile in Figura 14.

Analizzando la Figura 14 possiamo vedere che sulla sinistra vengono elencate tutte le sezioni, mentre sulla destra si possono vedere le domande appartenenti alla sezione selezionata. Ad ogni domanda e sezione sono associate le regole PRE e POST; cliccando su queste regole si accede all'editor grafico preposto alla loro manutenzione (inserimento, modifica, salvataggio, compilazione).

Sempre sulla sinistra vengono mostrate tutte le funzioni necessarie alla gestione del configuratore, quali ad esempio "Nuova Domanda" e "Nuova Sezione" per inserire rispettivamente unadomanda ed una sezione, "Modifica definizione questionario" per reimpostare le caratteristiche del questionario (ad esempio come associargli le sezioni), "Elenco configurazioni" per visualizzare tutte le configurazioni (cioè i questionari compilati) e "Gestione configurazione" che lancia un browser Internet per utilizzare il configuratore e rispondere alle domande.

![CFBASE_029](http://localhost:3000/immagini/CFBASE_DES/CFBASE_029.png)Figura 11 - La gestione del questionario in Looc.up

### La Scheda del Configuratore
L'accesso alle funzioni del configuratore avviene mediante un'apposita scheda (CFBASE).

Questa scheda è accessibile dal menù delle applicazioni di Loocup con il seguente percorso :  Menù Ingresso utente, *AP :  Applicazioni, LOOC_Up Graphic Environment, Schede, configuratore.

Verrà visualizzata la seguente scheda (Figura 12) : 

![CFBASE_037](http://localhost:3000/immagini/CFBASE_DES/CFBASE_037.png)  Figura 12 - La scheda del configuratore (CFBASE)

Sulla sinistra si possono vedere cinque tab, quattro raggruppano i questionari in base al loro tipo.
Esistono quattro tipi di configuratori : 

- i questionari Q- sono quelli definiti dall'utente, hanno una struttura ad albero e sono quelli descritti in questo documento
- i questionari T-, sono questionari dedicati alla manutenzione tabelle
- i questionari L- sono i setup e i questionari dedicati a definire i wizard di script
- i questionari C- sono quelli ricavati dalle categorie parametri.


In questo documento analizzeremo solo quelli definiti dall'utente.

Per accedere alle funzioni disponibili sul questionario bisogna selezionarne uno dall'elenco di sinistra.
Sulla destra verrà caricata la scheda del questionario (RE) : 

### La scheda del questionario
E' composta da tre sotto schede :  una dedicata alla manutenzione della struttura del questionario (è la prima visibile e riporta la dicitura "Questionario"), una dedicata alla gestione delle configurazioni (riporta la dicitura "Configurazioni") e una dedicata alla manutenzione delle regole (riporta la dicitura "Regole").

In figura 13 possiamo vedere le 3 schede con in primo piano quella del questionario.

![CFBASE_036](http://localhost:3000/immagini/CFBASE_DES/CFBASE_036.png)Figura 13 - La scheda del questionario.

Analizziamo in dettaglio le 3 schede.
 - La sottoscheda del questionario
La sottoscheda del questionario consente la navigazione e la manutenzione del questionario e di tutti i suoi componenti logici (sezioni, domande e valori).

Le prime informazioni che compaiono sono gli attributi del questionario (Figura 13).

Per ogni oggetto contenuto è attivo un menù di popup sensibile al contesto. In figura 13 si vede il popup di una sezione :  le ultime due voci consentono di aggiungere una pre o post regola.
Se queste sono già definite per la sezioni in questione si entrerà in manutenzione.

 - La sottoscheda delle regole

Con un doppio click sul talloncino delle regole si ottiene che la scheda vada a pieno schermo : 

![regole](http://localhost:3000/immagini/CFBASE_DES/regole.png)
 Figura 14 - La scheda delle regole

qui si possono vedere tutte le regole nella zona "Elenco regole" e selezionandone una si può vedere la scomposizione sulla sinistra e la sua traduzione in italiano sulla destra.

In basso un pulsante che consente la manutenzione.

Per aggiungere nuove regole su sezioni o domande ci si posiziona sulla scheda del questionario e con il tasto destro si accede a queste funzioni.

 -  La sottoscheda della configurazione

La sottoscheda elle configurazioni, visibile in figura 15, riporta sulla sinistra l'elenco delle configurazioni create, e sulla parte destra l'elenco delle risposte.

Posizionandosi su una configurazione e utilizzando il tasto destro, sotto la voce "Questionario" si hanno le azioni di Gestione, Visualizza o Elimina.

![CFBASE_026](http://localhost:3000/immagini/CFBASE_DES/CFBASE_026.png)Figura 15 - La sotto scheda della configurazione e il popup di gestione


### la compilazione di un questionario
Compilare un questionario porta alla creazione di una configurazione.

La creazione di una nuova configurazione avviene con il tasto F8 mentre la modifica di una precedentemente salvata avviene con la voce "Gestione questionario" e poi  "Gestione (Imm/Cop/Del)"  del popup della configurazione.

![CFBASE_024](http://localhost:3000/immagini/CFBASE_DES/CFBASE_024.png)Figura 16 -  La compilazione di un questionario in LoocUp


![CFBASE_039](http://localhost:3000/immagini/CFBASE_DES/CFBASE_039.png)sezione successiva, auto compilazione)
![CFBASE_022](http://localhost:3000/immagini/CFBASE_DES/CFBASE_022.png)visualizza la storia di esecuzione in tabella non ordinabile, visualizza in tabella ordinabile e filtrabile)
![CFBASE_021](http://localhost:3000/immagini/CFBASE_DES/CFBASE_021.png)regole, attiva ricerca all'interno delle regole, traduci le regole in italiano, esegui controllo su ricerca domande e/o sezioni duplicate)

## La compilazione su WEB
### Prerequisiti.
Buildup è integrato in WEB-Up e pertanto necessario avere un Web-Server con installato WEB-Up. Per le ulteriori informazioni si rimanda alla documentazione di WEB-Up.

### L'interfaccia WEB.
La compilazione su WEB è simile a quella che avviene in LoocUp. Visto l'ambiente nel quale ci si trova viene disattivata la traccia di esecuzione delle regole. Mancano anche i pulsanti relativi ai possibili controlli (duplicazione domande, controllo sintattico, rigenerazione motore regole).

Nella figura 17 si può vedere l'interfaccia della finestra di compilazione : 

![CFBASE_023](http://localhost:3000/immagini/CFBASE_DES/CFBASE_023.png)Figura 17 -  La compilazione di un questionario mediante browser.

In questa versione l'albero delle sezioni è stato portato in alto. Le sezioni percorse appaiono n grigio chiaro, quella corrente ha il testo in grassetto mentre quelle ancora da percorrere sono con lo sfondo grigio scuro.

Le sezioni disabilitate non vengono mostrate.

L'interfaccia è facilmente personalizzabile attraverso la modifica di fogli di stile che definiscono colori e dimensioni dei principali componenti.

Si possono anche aggiungere o rimuovere pulsanti secondo specifiche esigenze.

## Glossario
_2_Application Server. È un server che riceve la richiesta di una pagina che deve ancora essere creata; esegue del codice coinvolgendo solitamente anche altri moduli, quali ad esempio un database server e scrive il risultato della richiesta in una pagina HTML (quindi statica) che restituisce al web server che l'ha richiesta.

_2_Colloquio di configurazione. Durante la fase iniziale del processo di configurazione si svolge la raccolta delle informazioni sulle caratteristiche del prodotto richieste dal cliente. Questa fase prevede un colloquio, denominato appunto "colloquio di configurazione", tra commerciale e cliente in cui il cliente risponde a domande che riguardano le diverse possibilità di scelta previste, le risposte date permettono la completa specificazione del prodotto.

_2_Configuratore. È lo strumento che serve per realizzare un questionario e per utilizzarlo. Permette quindi l'inserimento di domande e regole e gestisce il suo comportamento. Sulla base cioè delle risposte che l'utente fornisce e dell'interpretazione delle regole sceglie quali altre domande devono essere poste.

_2_Configurazione. È il risultato della compilazione di un questionario. Una configurazione è l'elenco delle risposte fornite alle domande del questionario e identifica una particolare variante di prodotto.

_2_Distinta base. È l'elenco di tutti gli articoli che costituiscono il prodotto finale, unitamente alla loro quantità.

_2_Looc.up. È il client grafico di SME.up. Fornisce un'interfaccia grafica al gestionale Sme.up.

_2_Mass Customization. È un nuovo modo di concepire la produzione dei beni, con il riconoscimento della centralità delle esigenze e dei desideri dei clienti, ma senza nessuna rinuncia all'efficienza, all'efficacia ed al contenimento dei costi.

_2_Oggetto applicativo. È l'entità su cui si basano le azioni di inserimento e di reperimento delle informazioni del sistema gestionale Sme.up. Ogni oggetto è individuato dalla classe di appartenenza (chiamata "tipo") e dall'identificativo che è univoco all'interno della classe stessa; per alcune classi si identifica anche la sottoclasse (chiamata "Parametro"). Ad ogni oggetto sono associate delle funzioni che determinano quali azioni possono essere eseguite sull'oggetto stesso.

_2_Pagina dinamica. È una normale pagina basata su codice HTML che però viene generata da un server, con parametri e metodologie diverse a seconda delle circostanze. Esempi di tecnologie che realizzano pagine dinamiche sono gli script CGI (Common Gateway Interface) e le JSP (Java Server Pages).

_2_Prodotto configurabile. È un tipo di prodotto offerto, non corrisponde ad un oggetto fisico ma ad una categoria di prodotti potenzialmente realizzabili.

_2_Prodotto configurato. È una singola variante del prodotto configurabile e corrisponde ad un oggetto fisico, costruito o da costruire. Il prodotto configurato si ottiene personalizzando (precisando la scelta delle caratteristiche configurabili) un prodotto configurabile.

_2_Questionario. È l'insieme di tutte e sole quelle domande che servono a definire univocamente un prodotto. La compilazione del questionario, cioè le risposte fornite alle domande, permettono di identificare la variante di prodotto desiderata.

_2_Variante di prodotto. È uno fra i possibili prodotti che si ottengono modificando i parametri e le caratteristiche di un prodotto configurabile.

_2_Web server. Viene detto anche HTTP Server, è un programma che, avendo ricevuto delle richieste da parte del browser, spedisce il documento richiesto (o un messaggio di errore) al browser stesso.

_2_Web.up. È un modulo aggiuntivo di Sme.up. E' pensato per fornire strumenti di aiuto all'inserimento di dati prelevati dal database aziendale in pagine HTML.

## Conclusioni
Questa breve presentazione del prodotto Build.up ha mostrato le principali caratteristiche del programma nella speranza di offrire una panoramica d'insieme che possa rendere giustizia alle effettive qualità del pacchetto proposto.

La versione attuale di Build.up rappresenta quanto di meglio è oggi ottenibile nel settore dei configuratori :  la struttura fortemente modulare di Build.up, tipica di tutti i prodotti di SME.up, lascia comunque aperte molte strade di sviluppo e miglioramento e rende più agevole la manutenzione del pacchetto stesso anche in funzione delle nuove tecnologie che si renderanno disponibili in futuro.
