## Caratteristiche tecniche fondamentali
Dopo aver presentato a grandi linee le funzionalità di Build.up ci possiamo addentrare più a fondo nella comprensione dei meccanismi di funzionamento di questo programma.

Prima di affrontare la questione della creazione di un configuratore è necessario capire la struttura base di questo componente e quali sono gli oggetti principali che lo compongono. La Figura 2 riassume graficamente lo schema costruttivo di un configuratore generico.

![CFBASE_038](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_038.png)Figura 2 :  Struttura di un questionario Base

L'oggetto base è il configuratore, formato da una lista di sezioni. Ogni sezione contiene un certo numero di domande, ognuna delle quali è di tipo prefissato, ed ha associato una variabile in cui si salverà la risposta data.
Le domande possono essere chiuse o aperte, a risposta singola o multipla e di tipo semplice o configurato.

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

![CFBASE_025](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_025.png)Figura 3 :  La struttura del questionario estesa.

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

## Le Domande
Le domande all'interno del configuratore sono oggetti applicativi. Il loro inserimento quindi consiste nella compilazione di un questionario. Ogni domanda, infatti, possiede degli attributi e la creazione di una domanda implica la configurazione della domanda stessa. Le domande, dopo essere state configurate sono salvate su AS400.

Oltre alle domande "tradizionali", alle quali l'utente deve dare solo una risposta, Build.up implementa un altro tipo di definizione domande :  le domande configurate. Se un utente ha bisogno di ordinare un prodotto deve sicuramente poter specificare il nome del modello; è possibile però che abbia la necessità di specificare una quantità, scegliere una tipologia di sconto o inserire la data entro il quale vuole che il prodotto sia consegnato. Invece di fare quattro domande diverse, come dovrebbe fare se avesse a disposizione solo le domande "tradizionali", può avvalersidelle domande configurate; esse consentono di chiedere informazioni legate al prodotto che si vuole configurare su una sola riga, memorizzando una sola domanda su AS400 anche se in realtà le domande sono di più.

Di seguito vengono illustrati e commentati i diversi campi a cui bisogna rispondere quando si configura una domanda, e vengono mostrate delle figure che rappresentano la veste grafica con cui vengono presentate le domande all'utente che compila un questionario.

![CFBASE_028](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_028.png)Figura 4 - La finestra di definizione di una domanda

La Figura 4 mostra un esempio di come si presenta la schermata di Build.up quando si crea una nuova domanda, seguita da una descrizione del significato dei campi che devono essere compilati : 

- _2_Descrizione :  è il testo della domanda, quello cioè che viene presentato all'utente che compila il questionario. La massima lunghezza di questo campo è di 30 caratteri.
- _2_Categoria domanda :  stabilisce quali caratteristiche deve avere la risposta associata alla domanda. In questo campo è possibile inserire uno dei codici a due caratteri contenuti nella Tabella 1.


| 
| .COL Txt="Codice" A="L" |
| ---|----|
| 
| .COL Txt="Significato" A="L" |
| 
| .COL Txt="Descrizione" LunAut="1" |
| 
| .COL Txt="Esempio" A="L" |
| **01** | Valore singolo | con questa opzione all'utente viene mostrata una casella in cui può inserire la risposta. Il valore che si inserisce deve essere compatibile con il tipo di oggetto associato alla domanda | fig. 4 |
| **02** | Scelta in lista  | con questa opzione l'utente vedrà una lista di possibili risposte dalla quale sceglierà quella desiderata | 5 |
| **03** | Gestione in lista | l'utente può costruire una lista di valori aggiungendo un campo ad ogni risposta | 6 |
| **04** | Aggiunta a lista | l'utente aggiunge una risposta alla volta ad una lista di risposte. Il valore che aggiunge può essere in seguito cancellato, ma non modificato. | 7 |
| **F-** | File | la domanda è composta da tante domande (posizionate tutte sulla stessa riga, comeaccade per le domande configurate) quanti sono i campi del file il cui nome è specificato alla voce Par. presentazione (vedi dopo). Il testo delle domande è costituito dalle descrizioni dei campi del file. | |
| **T-** | Tabella | comportamento analogo a quello della voce precedente, tranne per il fatto che il testo delle domande è costituito dalle intestazioni delle colonne della tabella, specificata anch'essa alla voce Par. presentazione. | |
| **Q-** | Questionario | in questo caso la domanda è composta da tutte le domande del questionarioil cui nome è specificato alla voce Par. presentazione. | |
| **C-** | Cat. Parametri | analogo ai precedenti, ma il testo delle domande è formato dai parametri di un oggetto specificato alla voce Par. presentazione. | |
| 

Tabella 1 - Le categorie di una domanda


- _2_Par.presentazione :  valori opzionali di personalizzazioni grafiche o comportamenti avanzati. E' un campo posizionale vediamo le opzioni possibili in tabella 2.


| 
| .COL Txt="Posto" A="L" |
| ---|----|
| 
| .COL Txt="Significato" A="L" |
| 
| .COL Txt="Valori possibili" LunAut="1" |
| **1** | Carattere 1 | D = Solo descrizione domanda; S = Solo titolo di una subsezione; Blank = Domanda Normale |
| **2** | Cosa Emettere | Blank = Sia codice che decodifica; D = Descrizione in COMBOBOX; C = Codice in COMBOBOX; E = Codice - Descrizione - Immagine; F = Codice - Immagine; G = Descrizione - Immagine |
| **3** | Nota | N = Gestire la nota; Blank = Non gestire la Nota |
| **4** | Tipo compilazione | T = In finestra separata (tabella); A = Lista con 10 elementi; B = Lista con 15 elementi; 1 = Come check box su 1 colonna; 2 = Come check box su 2 colonne; 3 = Come check box su 3 colonne; Blank = Default |
| **5** | Soggetto condizionamento | Indico, mediante una lettera, che la variazione della rispostadi questa domanda provoca l'aggiornamento delle domande che hanno nell'oggetto di condizionamento la stessa lettera |
| **6** | Oggetto condizionamento  | Domande la cui risposta viene modificata dalla variazione di un'altra domanda. Vedi 'Soggetto condizionamento' |
| **7** | Protezione | Blank =  Modificabile; 1 = Non modificabili; 2 = Non visualizzato |
| **8** | Ricarica questionario | SI/NO = Abilita Disabilita il reload del questionario dopo una modifica -  NON IMPLEMENTATO |
| **9** | Conversione carattere | Blank = Non convertire; U = Converti in MAIUSCOLO; L = Converti in minuscolo |
| **10** | Immagine / Formato | Blank = Non mostrare immagine; 1 = Immagine piccola; 2 = Immagine media; 3 = Immagine grande; L = Formato libero; D = Dimensioni come default |
| **11** | Risalita immagine | SI/NO = Abilita la ricerca delle immagini con la risalita |
| **12** | Forzatura regole | SI/NO = Abilita la possibilità di forzare le regole sulla domanda |
| **13** | Ricerca per Descriz. | SI/NO = Imposta come default la ricerca per descrizione |
| **14** | Attivato da regole | SI/NO = Disabilita la domanda. |
| **15** | Non utilizzato  | |
| 

Tabella 2 :  Valori campo Parametro Presentazione
 Per esempio si può scegliere di non visualizzare il codice di un possibile valore di risposta, ma mostrarne solo la descrizione.

Nel caso la domanda appartenga alla categoria F-, T-, Q-, o C- questo campo contiene il nome di un file, di una tabella, di un questionario o di un oggetto rispettivamente.

- _2_Multipla :  questo campo accetta solo i valori '1' e ' ' (blank). Nel primo caso si permetteall'utente di inserire più risposte, nel secondo solamente una.
- _2_Obbligatoria :  questo campo accetta solo i valori '1' e ' ' (blank). Nel primo caso non è possibile accedere a sezioni successive senza aver risposto alla domanda, nel secondo all'utente viene lasciata la possibilità di scegliere se rispondere o no.
- _2_Accetta altro :  se impostato a '1' accetta, su richiesta dell'utente, risposte libere.
- _2_Tipo oggetto :  in questo si inserisce il codice che identifica l'oggetto SmeUp associato alla domanda.
- _2_Lunghezza :  In questo campo viene inserito un numero intero che stabilisce il numero massimo di caratteri della risposta. Per tutti gli oggetti SmeUp si suggerisce la lunghezza di 15 caratteri.
- _2_Decimali :  Definisce il numero di decimali accettati dalla risposta, nel caso il tipo oggetto di quest'ultima sia un numero.
- _2_Filtro risposta :  In questo campo si immette il tipo dell'oggetto SmeUp utilizzato per parzializzare le scelte dell'utente
- _2_Param. Filtro :  Bisogna inserire il parametro dell'oggetto SmeUp utilizzato per parzializzare le scelte dell'utente, se è stato selezionato un filtro per la risposta.
Il filtro risposta e il suo parametro consentono di specificare un elenco di valori :  la tabella CFV è pensata per questo scopo :  contiene infatti tutti i possibili valori di risposta dei questionari.

Si può scegliere una delle seguenti opzioni : 

| **Configuraz. risposta : ** | **Param. Configurazione** |
| ---|----|
| Nessuna | - |
| BA / Quantità/Prezzo/Sconto/Data/Nota | una sigla che identifica i campi scelti :  es. 23 significa prezzo e sconto, 1 3 5 significa Quantità Sconto Nota ecc |
| SE Sezione del questionario | Il codice di una sezione |
| 

Tabella 3 :  Valori campo Parametro Presentazione

## Le Sezioni
Un questionario è diviso in sezioni che contengono domande; solitamente le sezioni raggruppano domande di significato omogeneo, anche se all'utente è lasciata completa libertà di scelta. Le sezioni sono memorizzate in un settore di tabella dell'AS400 chiamata CFS.

Le domande possono essere associate alle sezioni in vari modi (descritti in seguito). Esse possonoessere viste come dei contenitori di domande. Quali tipi di domande debbano contenere è deciso al momento della configurazione delle sezioni. Essendo a loro volta degli oggetti, infatti, quandovengono create, le sezioni devono essere configurate; perciò, la creazione di una sezione è ancora la compilazione di un questionario.

Di seguito vengono illustrati e commentati i diversi campi a cui bisogna rispondere quando si configura una sezione.

Viene riportata in Figura 5 la schermata mostrata da Build.up quando si crea una nuova sezione.

![CFBASE_032](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_032.png) Figura 5 - Creazione di una nuova sezione

_2_Descrizione :  è il nome della sezione, quello che viene presentato all'utente che compila il questionario. La lunghezza massima di questo campo è di 30 caratteri.

_2_Metodo costr. domande e Parametro Costruzione Domande :  nel primo si inserisce un codice che identifica il criterio con il quale le domande vengono aggiunte alla sezione creata e nel secondo viene specificato un parametro aggiuntivo.

Esistono 8 possibilità : 

| 
| .COL Txt="Opz." A="L" |
| ---|----|
| 
| .COL Txt="Tipo di costruzione" A="L" |
| 
| .COL Txt="Descrizione" LunAut="1" |
| **1** | Domande con Prefisso = Sezione | vengono inserite nella sezione le domande il cui prefisso del codice coincide con il codice della sezione stessa. In una ipotetica sezione il cui codice sia S010 vengono inserite tutte le domande il cui codice comincia con S010. In questo caso il Parametro Costruzione Domande è vuoto. |
| **2** | Definite in parametro | L'utente può specificare quali domande appartengono alla sezione scegliendo tra tutte quelle definite definendo anche l'ordine. |
| **3** | Con prefisso indicato | Vengono inserite nella sezione le domande che iniziano con il prefisso specificato. |
| **4** | Da programma utente | L'utente può invocare un programma che calcola le domande da inserire nella sezione |
| **5** | File | Le domande sono costruite analizzando l'intestazione dei campi del file specificato |
| **6** | Tabella | Come l'opzione File ma i dati vengono prelevati dalla tabella specificata |
| **7** | Questionario | Vengono inserite tutte le domande lette da un altro questionario. |
| **8** | Cat. parametri | Il testo delle domande inserite nella sezione è la descrizione dei parametri associati all'oggetto specificato in Param. Costr. Domande. |
| 

Tabella 4  Valori campo Parametro Presentazione

_2_Induzione Dinamica :  specifica quale programma chiamare su AS400 al cambio di sezione per ottenere un aggiornamento nella struttura/risposte del questionario. Vengono passate le risposte finora fornite e il programma può restituire, la nuova sezione, nuove domande, nuovi valori o nuove risposte.

_2_Tipo ripetizione e Numero o Domanda :  specifica come la sezione è ripetibile. Se il tipo è numero allora il parametro che segue definisce quante volte la sezione va ripetuta. Si definisce in modo statico il numero di ripetizioni. Se invece si indica una domanda, allora il numero di ripetizioni dipende dalla risposta fornita.

_2_Questionario legato :  è il codice del questionario da cui verranno estratte le sezioni.

## Il Questionario
Dopo aver creato le domande e le sezioni non resta che configurare un questionario che le contenga. Le sezioni possono essere associate al questionario in modi differenti (descritti in seguito). Il questionario può essere considerato un raccoglitore di sezioni, che a loro volta, come detto prima, sono dei raccoglitori di domande.

Anche il questionario, come le domande e le sezioni, è un oggetto applicativo e per essere definito deve essere configurato. I questionari sono salvati su AS400 all'interno di un settore di tabella chiamato CFQ.

Analogamente a quanto fatto precedentemente vengono illustrati e commentati i campi che si devono compilare per una corretta configurazione del questionario.
La Figura 6 mostra la videata di Loocu.up quando si vuole creare un questionario.

![CFBASE_033](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_033.png) Figura 6 - Creazione di un nuovo questionario

_2_Descrizione :  è il nome del questionario. La lunghezza massima di questo campo è di 30 caratteri.

_2_Livello :  indica lo stato del questionario, ammette quattro possibilità.

| 
| .COL |
| ---|----|
| 
| .COL |
| **1** | Immesso non attivo :  è un questionario non ancora validato e pertanto non utilizzabile per la compilazione |
| **2** | Attivo :  un questionario valido, |
| **3** | Chiuso :  un questionario non modificabile |
| **4** | Annullato :  un questionario non più valido |
| 

_2_Subs. Sezioni/Domande :  in questo campo viene inserito il codice del subsettore della tabelladelle sezioni e delle domande da associare al questionario.

_2_Metodo costr. Sezioni :  in questo campo si inserisce un codice che identifica il criterio con il quale le sezioni vengono aggiunte al questionario creato. Sono possibili tre modalità : 

| 
| .COL |
| ---|----|
| 
| .COL |
| **1** | Tutte le sezioni :  vengono inserite nel questionario tutte le sezioni contenute nel subsettore associato al questionario. L'ordine di inserimento è dato dall'ordine alfabetico del codice delle sezioni. |
| **2** | Definite in parametro :  alla sezione appartengono le sezioni specificate nel parametro di costruzione delle sezioni |
| **3** | Con prefisso indicato :  vengono inserite nel questionario le sezioni che iniziano con il prefisso specificato in Param. Costr. Sezioni. |
| 

_2_Parametro costr. Sezioni :  in base alla scelta fatta al punto precedente è possibile inserirediverse opzioni.

| 
| .COL |
| ---|----|
| 
| .COL |
| **1** | Tutte le sezioni :  rimane vuoto. |
| **2** | Definite in parametro :  specifico il parametro che contiene l'elenco delle sezioni |
| **3** | Con prefisso indicato :  specifico il prefisso che identifica le sezioni da includere. |
| 

_2_Progr. di stampa :  va indicato quale programma si occuperà della stampa. Una volta finita la fase di compilazione del questionario è data la possibilità all'utente di stampare in formato PDF il risultato della configurazione.

_2_Identificativo :  fornisce la chiave d'accesso al file nel quale sono salvate le configurazioni create. Si possono specificare tre chiavi d'accesso differenti. Se la chiave che si definisce è unica e automatica, allora la chiave del configuratore è definita dal programma che esegue il salvataggio su AS400.

_2_Gestione Configurazioni :  Non Utilizzato. Il modo di salvare le configurazioni è definito nell'identificativo.

_2_Eseguire regole :  consente di disabilitare le regole, farle eseguire al cambio di sezione o farle eseguire ad ogni risposta fornita. Quest'ultimo comportamento è disponibile solo per la compilazione in LoocUp.

_2_Aspetto :  specifica come si deve presentare il questionario. Sono possibili tre modalità :  In un'unica sezione, con le sezioni disposte in pannelli affiancati, con la sezione corrente e l'albero di navigazione.

_2_Dati ausiliari :  richiede la gestione di variabili ausiliarie. Di seguito l'elenco di quelle gestite : 

- *DE è la descrizione della configurazione
- *QU è il codice del questionario
- *DC è la data di creazione
- *IC l'ora di creazione
- *DM è l'utente che ha modificato la configurazione
- *IM l'ora di modifica
- *UM è l'utente che ha modificato
- *UC è l'utente che ha creato la configurazione

Queste variabili vengono salvate su AS400 ma sono anche accessibili tramite la funzione getAuxResp("codice"), dove codice è il codice della domanda senza l'asterisco.

_2_Riepilogo :  flag che abilita la visualizzazione delle risposte fornite come ultima sezione. Ha senso solo per le compilazioni che avvengono in ambito WEB.

_2_Struttura Ingresso :  Specifica quale è il formato dell'XML delle risposte ricevuto in input dal configuratore. Sono disponibili 3 formati : 

- CDATA - a larghezza delimitata - disponibile per i questionari composti da una sola sezione
- Risposta - le risposte sono identificate dal codice della domanda. Ogni domanda è univoca pertanto questo formato non è adatto a gestire i questionari multi livello
- Sezione :  le risposte sono raggruppate per sezione. Se il questionario è multilivello questo formato viene impostato di default.

Se questo parametro non è impostato il sistema cerca di interpretare le risposte che riceve in ingresso.

_2_Struttura Uscita :  Specifica quale è il formato dell'XML delle risposte fornito in output dal configuratore. I formati disponibili sono gli stessi del parametro Struttura Ingresso.

_2_Salvataggio Esteso :  Specifica se salvare la configurazione sul file B£MEDE0F o se usare i default. Se il questionario è multilivello la sua configurazione viene salvata obbligatoriamente nel B£MEDE e pertanto questo parametro risulta non considerato. Se il questionario non è multilivello allora, si può forzare il salvataggio sul B£MEDE invece che sul CFVARI.

_2_Motore Regole :  Mantenuto per compatibilità con le versioni precedenti alla V2R2M070214. Consente di specificare il tipo di motore, statico o dinamico. Dalla versione V2R2M070214 non esistono differenze tra il motore statico e quello dinamico. I questionari multi livello necessitano del motore dinamico. Il valore di default per questo parametro è dinamico.

![CFBASE_030](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_030.png)Figura 7a - L'ordine di esecuzione delle regole al cambio di sezione

![CFBASE_041](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_041.png)Figura 7b - L'ordine di esecuzione delle regole quando viene fornita una risposta


## Il linguaggio delle Regole
Questo linguaggio di regole non è case sensitive e non fa quindi differenza tra lettere minuscole e lettere maiuscole (quindi la funzione AddVal è la stessa sia se invocata come "ADDVAL" che come "addval"). Inoltre non è posizionale e non tiene conto degli eventuali spazi bianchi compresi nelle chiamate alle procedure

Tutte le regole sono espresse utilizzando i seguenti costrutti : 

- SE condizione ALLORA azione
- SE condizione ALLORA azione1 ALTRIMENTI azione2
- Azione
- Commento

Le prime due strutture permettono di controllare se una parte di codice deve essere eseguita in base al risultato di una condizione. Se la condizione è vera vengono eseguiti i comandi della parte ALLORA, in caso contrario quelli della parte ALTRIMENTI (se si utilizza il secondo costrutto).
La sintassi è la seguente : 

SE ((condizione booleana) [E/O (condizione booleana)] ) ALLORA [azione]

Oppure

SE ((condizione booleana) [E/O (condizione booleana)] )ALLORA [azione] ALTRIMENTI [azione]

Le parentesi quadre prima dell'istuzione ALLORA non fanno parte della sintassi. È una notazione che indica che il loro contenuto può essere ripetuto.

Le lettere "E" e "O" sono utilizzate per indicare due operatori booleani And e Or.

## La condizione booleana
La condizione booleana ha la seguente forma : 

(**condizione booleana** )

dove **condizione booleana** è composta da

_7_valore sinistro  > operatore di confronto _7_valore destro

Se si ha necessità di concatenare più condizioni booleane va utilizzata la sintassi

( (**condizione booleana** ) E oppure O (**condizione booleana** )  .... )

Si possono annidare condizione booleane senza nessun limite di profondità :  ad esempio

SE ( ( ( A > B ) E (A > C) ) O ( (A < D ) E (C > B ) ) ) equivale a
A > B and A > C or A < D and C > B

Nella tabella 5 sono elencati i tipi di operatori di confronto disponibili.

| **Valore sinistro** | **Operatore di confronto** | **Valore destro** |
| ---|----|----|
| Espressione | == (uguale) |  Espressione |
| Espressione |  < (minore) |  Espressione |
| Espressione | <= (minore uguale) |  Espressione |
| Espressione |  > (maggiore) |  Espressione |
| Espressione |  >= (maggiore uguale)|  Espressione |
| Espressione |  <> (diverso) |  Espressione |
| Variabile | IN (VAL1<variabile<VAL2 | Range |
| Variabile | =IN (VAL1<=variabile<VAL2 | Range |
| Variabile | IN= (VAL1<variabile<=VAL2 | Range |
| Variabile | =IN= (VAL1<=variabile<=VAL2 | Range |
| Variabile | OUT (variabile<VAL1 oppure variabile>VAL2 con VAL1<VAL2| Range |
| Variabile | =OUT (variabile<=VAL1 oppure variabile>VAL2 con VAL1<VAL2| Range |
| Variabile | OUT= (variabile<VAL1 oppure variabile>=VAL2 con VAL1<VAL2| Range |
| Variabile | =OUT= (variabile<=VAL1 oppure variabile>=VAL2 con VAL1<VAL2| Range |
| Variabile | IN_LISTA (Variabile 1 deve essere compreso tra le risposte di Variabile2)| Variabile2 |
| Variabile | OUT_LISTA (Variabile 1 non deve essere compreso tra le risposte di Variabile2)| Variabile2 |
|  |
| 

Tabella 5 - I possibili operatori di confronto

Dove Espressione può essere : 
_2_Valore :  identifica un valore costante, per esempio il numero 10 viene espresso con la stringa :  '10'.
_2_Variabile :  identifica la risposta fornita dall'utente.
_2_Proprietà di una domanda o della Sezione :  posso accedere alla definizione della struttura della domanda o della sezione ed eseguire controlli sulla struttura o cambiarne la visibilià.
Nell'esempio che segue controlliamo il tipo della domanda V02_01 e se il tipo è numerico assegnamoil valore della domanda V01_01 incrementato di 5.
_1_SE D.V02_01.TACFDC == 'NR' ALLORA V02_01 = V01_01 + '5'
_2_Attributo Sme.up oggetto risposta :  data una risposta ad una domanda viene identificato un oggetto Sme.up, identificato l'oggetto posso accedere ai suoi attributi.
Se per esempio richiedo un agente, posso poi testare la sua data di nascita, se è tra i suoi attributi.
_2_Espressione :  è una struttura del tipo operando1 operatore operando2. Operando 1 e Operando2

Range è definito come 'VALORE1'..'VALORE2'

## Le Funzioni
Le funzioni che questo linguaggio delle regole può implementare sono le seguenti : 

### Le funzioni sui valori e di filtro

- _2_AddVal (cod_domanda; valore (o range)) :  aggiungo un valore o un gruppo di valori alla domanda selezionata.
- _2_RmvVal (cod_domanda; valore) :  rimuovo un valore o un gruppo di valori alla domanda selezionata.
- _2_AddAll (cod_domanda) :  abilito tutti i valori della domanda selezionata
- _2_RmvAll (cod_domanda) :  disabilito tutti i valori della domanda selezionata
- _2_AddFunVal() e RmvFunVal() : possono aggiungere o rimuovere una lista di valori letta da AS400 utilizzando un servizio che restituisca una griglia. I parametri ammessi sono i seguenti :  domanda a cui vanno aggiunti/rimossi i valori, funzione da invocare, codice colonna che contiene valori, codice colonna di filtro e valore filtro. Gli ultimi due valori sono opzionali. Per rendere dinamica la chiamata da fare all'AS400 si possono inserire le variabili del configuratore con la sintassi "aperta quadra" codice_domanda "chiusa quadra". Se la variabile è multipla vengono eseguite n chiamate, una per ogni valore. La funzione accetta fino a 3 variabili.
- _2_SetFiltro ( cod_domanda; cod_filtro; param1 filtro; ...; param N filtro) :  imposto un filtro sulle possibili risposte fornite. Se si desiderano utilizzare i filtri definiti nella JAC il codice del filtro deve diventare *JAC
- _2_ResetFiltro(cod_domanda) :  annullo il filtro


### Le funzioni sui messaggi

- _2_AddMsgT(testo) emette un messaggio bloccante :  la compilazione si arresta.
- _2_AddMsgW(testo) emette un messaggio di avviso.
- _2_AddMsgI(testo) emette un messaggio informativo.
- _2_ClrMsg ( ) rimuove tutti i messaggi della sezione alla quale la regola appartiene.


### Le funzioni matematiche
Operano tutte su parametri numerici.

- _2_abs(VAR) Restituisce il valore assoluto di VAR.
- _2_acos(VAR) Restituisce l'arcocoseno dell'angolo VAR in radianti da 0 a PI
- _2_asin(VAR) Restituisce l'arco seno dell'angolo VAR da -PI/2 a PI/2
- _2_atan(VAR) Restituisce l'arco tangente dell'angolo VAR da -PI/2 a PI/2
- _2_ceil(VAR) Approssima VAR all'intero successivo. Es. Ceil('12.23') = 13.
- _2_cos(VAR)  Restituisce il coseno di VAR.
- _2_exp(VAR)  Restituisce il numero di Eulero elevato alla potenza di VAR.
- _2_floor(VAR) Approssima VAR all'intero precedente. Es. Flor('12,77') = 12.
- _2_log(VAR) Restituisce il logaritmop naturale di VAR.
- _2_max(VAR_A, VAR_B) Restituisce massimo tra i due valori
- _2_min(VAR, VAR_B) Restituisce il minimo tra i due valori.
- _2_pow(VAR, VAR_B) Eleva VAR alla potenza di VAR_B
- _2_random() Genera un numero casuale compreso tra 0 e 1
- _2_sin(VAR) Restituisce seno di VAR
- _2_sqrt(VAR) Restituisce la radice quadrata di VAR
- _2_tan(VAR) Restituisce la tangente di VAR
- _2_toDegrees(angRad) Converte un angolo espresso in gradi in radianti
- _2_toRadians(angDeg) Converte un angolo espresso in radianti in gradi.


### Le funzioni sulle stringhe o di conversione

- _2_concat(String a, String b) restituisce la stringa formata dal concatenamento di a e b
- _2_substring(String A, Number B, Number C) restituisce la sottostringa di A che inizia dall'indice B e termina all'indice C escluso :  esempio substring('ABCDEF',0,3) = ABC; substring('ABCDEF',2,3) = C
- _2_substringFrom(String A, Number B) restituisce la sottostringa di A che inizia dall'indice B e va fino alla fine. Esempio substringFrom('ABCDE';2)=CDE
- _2_number2string(a[,b,c]) converte il numero a  in una stringa. Esempio number2string('12345.6789') restituisce '123456.6789'. Se vengono specificati anche i parametri b e c allora il numero viene convertito in una stringa lunga b con c decimali, senza uso della virgola come separatore dei decimali. Esempio number2string('12345.6789'; '7', '2') restituisce 1234567 mentre - _2_number2string('12345.6789'; '10','2') restituisce '0001234567'
- _2_string2number() converte una stringa formattata secondo lo standard AS400 in numero. Esempio string2number('1234567'; '5'; '2' ) restituisce 123,45


### Le funzioni di accesso alle risposte multiple e/o configurate

- _2_getResponseAtIndex(cod_domanda; indice) restituisce la risposta della domanda di dato indice :  si usa con le domande a risposta multipla.
- _2_getRespAt(cod_domanda; indice) forma abbreviata della precedente.
- _2_getNRRespAtIndex(cod_domanda; indice) restituisce la risposta di dato indice in formato numerico.
- _2_getNRRespAt(cod_domanda; indice) forma abbreviata della precedente.
- _2_getDescRespAt(cod_domanda; indice) restituisce la descrizione della risposta di dato indice.
- _2_getDescResp( cod_domanda) restituisce la descrizione della risposta (se la domanda è a risposta multipla restituisce la descrizione della prima risposta).
- _2_getObjDesc(tipo; parametro; codice) restituisce la decodifica dell'oggetto identificato dalla terna tipo-parametro-codice. Tipo parametro codice sono espressioni.
- _2_getAuxResp('nome domanda ausliaria senza asterisco') restituisce la risposta ausiliaria. Le domande ausiliarie sono le seguenti : 
-- *DE è la descrizione della configurazione
-- *QU è il codice del questionario
-- *UC è l'utente che ha creato la configurazione
-- *DC è la data di creazione
-- *IC l'ora di creazione
-- *DM è l'utente che ha modificato la configurazione
-- *IM l'ora di modifica
-- *UM è l'utente che ha modificato
Esempio getAuxResp('UM') restituisce il codice dell'utente che ha modificato la configurazione. Queste informazioni ausiliarie sono disponibili solo se nel questionario si specifica di aggiungere queste informazioni.
- _2_getLoocupVarValue('cod_LoocupVariable') restituisce il valore della variabile di ambiente di Loocup. Le variabili di ambiente includono i dati relativi all'applicazione (es. posizione icone), i dati relativi alla macchina e i dati della JVM utilizzata. Maggiori dettagli sono disponibili nella documentazione di LoocUp.


### Le funzioni di modifica delle risposte multiple e/o configurate

- _2_setNota(cod_domanda; testo_nota) aggiunge una nota ad una domanda. Sono ammesse le sole lettere e i numeri.
- _2_setRespAt(cod_domanda; nuova_risposta; indice_risposta) consente di variare una risposta di dato indice.


### Le funzioni di test
_2_IsEmpty(cod_domanda) restituisce vero se alla domanda identificata da cod_domanda non è stata fornita nessuna risposta.

## I Commenti
E' possibile inserire dei commenti alle regole. Queste porzioni di testo non vengono interpretate dal sistema, ma servono solo all'utente per documentare il lavoro fatto.
Per inserire dei commenti è sufficiente farli precedere dalla stringa '//' (doppia barra); tutto quello compreso tra tale stringa e la fine della riga è considerato commento.

## I Messaggi
Build.up permette la visualizzazione di messaggi di testo definibili dall'utente. Esistono tre tipi di messaggi :  bloccanti (identificati dalla lettera "T" ), di avviso ("W") e informativi ("I").

I primi, quando vengono emessi, bloccano l'esecuzione del questionario ed obbligano l'utente a correggere le risposte sbagliate date in precedenza. I messaggi di avviso, invece, comunicano all'utente che i valori immessi potrebbero non essere corretti, ma lasciano proseguire la compilazione del questionario. Infine il terzo tipo di messaggio (informativo) serve per comunicare all'utente informazioni aggiuntive di carattere generale.

I messaggi vengono emessi scrivendo, nelle regole, opportune funzioni. Ogni funzione richiede due parametri, un codice e una testo. Se il codice è vuoto significa che il messaggio è del questionario, altrimenti è della sezione o della domanda identificata.

La rimozione dei messaggi è eseguita con la funzione CLRMSG( ) :  elimina tutti i messaggi dati fino a questo punto della compilazione.

La funzione ADDMSGT visualizza un messaggio bloccante ( T sta per Terminale) nella sezione alla quale appartiene la regola che richiama questa funzione.
Ecco un esempio :  _2_ADDMSGT ( ' Hai inserito un valore fuori dal range consentito ' )
Mentre la altre due servono per emettere messaggi di avviso o informativo.
Ecco alcuni esempi del loro utilizzo : 

- _2_ADDMSGW ( ' Questo è un messaggio di avviso' )
- _2_ADDMSGI ( ' Questo è un messaggio di informativo ' )

La funzione CLRMSG ( ) rimuove tutti i messaggi della sezione alla quale la regola appartiene.

## L'editor delle regole
Per facilitare l'inserimento e la manutenzione delle regole del questionario è stato sviluppato un apposito editor ed il suo aspetto è mostrato in Figura 8 : 

![CFBASE_028](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_028.png)Figura 8 - L'editor delle regole

E' dotato di tutti gli strumenti di un classico editor di testo (funzioni di salvataggio, stampa, taglia, copia, incolla, help, etc') e facilita la lettura delle regole, evidenziando con colori differenti le parole riservate del linguaggio e i valori delle variabili.

Il tasto "Compila" manda in esecuzione il parser che abbiamo realizzato al fine di validare sintatticamente la regola digitata. Quando si preme il tasto "Salva" viene comunque eseguito questo controllo per garantire che qualsiasi regola inserita sul server AS400 sia almeno sintatticamente corretta.

l grande vantaggio di questo editor sta nella presenza del "Wizard", ossia di una procedura che guida l'utente nell'inserimento delle regole. Il Wizard, in base al punto in cui l'utente si trovacol cursore durante la scrittura della regola, suggerisce tutte le possibili opzioni valide tra le quali l'utente può selezionare quella desiderata. Ad esempio quando l'utente digita il "SE"il Wizard mostra la finestra riportata in figura 12, nella quale propone la scelta dell'oggetto (variabile) da testare nella condizione booleana, ed in seguito propone l'elenco dei possibili valori della parte destra dell'operazione di confronto, prendendo questa lista direttamente dalla tabella memorizzata su AS400 alla quale la domanda stessa è associata. Il processo guidato continua fino alla terminazione della regola.

![CFBASE_035](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_035.png)Figura 9 - Il wizard dell'editor delle regole con la finestra di selezione degli operatori

### La messa a punto delle regole

In LoocUp non esiste un debugger interattivo vi è però la possibilità di visualizzare tutte le operazioni compiute.
Durante la compilazione viene, di default, tenuta traccia delle azioni compiute dalle regole. Questa traccia è visibile dalla finestra di compilazione di LoocUp. I pulsanti preposti sono quelli che riportano una pergamena.
La storia di esecuzione si può disabilitare con l'apposito pulsante oppure mediante parametri :  se nella richiesta di configurazione si inserisce nel parametro P il valore DEBUG(0).
La storia di esecuzione può diventare molto grande. Se si desidera analizzare un particolare gruppo di regole si può cancellarla o tenerla disabilitata fino al momento opportuno.

Esistono due modi di visualizzarla :  in una tabella non riordinabile (molto veloce) oppure in una matrice. La seconda strada, se le regole eseguite sono molte è più lenta, ma permette inoltre di esportare la matrice in formato EXCELL e di eseguire ricerche più accurate.

L'esportazione in EXCEL risulta molto utile quanto non si capisce quale regole abbia agito su una determinata domanda.

## Correlazione tra oggetti e regole
Per creare un questionario occorre, oltre che definire sezioni e domande, scrivere le regole. E' attraverso di esse che si riesce a dare al configuratore un comportamento dinamico, attivando o disattivando la visualizzazione di sezioni e di domande, o svolgendo funzioni particolari. Le regole legano tra loro gli oggetti che costituiscono un configuratore (li correlano), confrontandoli o modificandone i valori.

Ad esempio, una regola potrebbe dover confrontare i valori di Oggetto1 e Oggetto2 e impostare il valore di un terzo oggetto chiamato Oggetto3. Al crescere della complessità del questionario aumenta, però, in proporzione, anche la possibilità che lo stesso oggetto compaia in più regole. E' facile quindi arrivare ad avere una struttura "ingarbugliata" del questionario, costituita da numerosissimi legami invisibili tra oggetti e regole. Il questionario, inoltre, non ha una struttura che, una volta realizzata, rimane tale per sempre. Viene sottoposto continuamente a modifiche e aggiornamenti perché il prodotto che viene configurato può avere nuove varianti, o certe sue parti possono finire fuori produzione ecc... Chi implementa questi cambiamenti ha quindila necessità di avere a disposizione strumenti che lo aiutino nell'apportare tali modifiche.

Solitamente la sua necessità è quella di poter sapere in quali regole compare un determinato oggetto o, viceversa, dato un oggetto poter risalire a conoscere in quali regole compare :  nella figura che segue vediamo lo strumento di analisi delle regole : 

![CFBASE_027](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_027.png)Figura 10 - La finestra Correlazione Regole

Questo strumento riceve dall'AS400 tutte le regole di un questionario. Per ognuna di esse estrae tutti gli oggetti che la compongono e li inserisce in una tabella bidimensionale. Ad ogni riga corrisponde un oggetto di una regola; se lo stesso oggetto compare in più regole ci saranno più righe con quell'oggetto ma associate a regole diverse. Le colonne sono 8 e ognuna identifica una caratteristica dell'oggetto o della regola che caratterizzano la riga.

In particolare sono : 

- Questionario :  è il nome del questionario a cui la regola appartiene;
- Tipo regola :  dice se la regola è una regola di domanda, di sezione o di questionario;
- Codice regola :  è il codice della sezione o della domanda alla quale la regola è associata;
- Significato :  è il testo della domanda se la regola è associata alla domanda, è invece il nome della sezione se la regola è associata alla sezione;
- Tipo oggetto :  è il tipo dell'oggetto che, assieme alla regola, identifica la riga;
- Oggetto :  è l'oggetto trovato nella regola, con la regola identifica univocamente la riga;
- Significato :  è la descrizione dell'oggetto. Ad esempio, se l'oggetto è una domanda, rappresenta il testo della domanda;
- Regola :  è la regola nella quale l'oggetto compare.

A questo punto è possibile operare su questa tabella per ottenere informazioni sui legami che esistono tra oggetti e regole (la loro correlazione).

L'idea è quella di poter "guardare" la tabella da diversi punti di vista, ognuno dei quali mette a fuoco determinati aspetti. Le righe della tabella possono essere riordinate secondo un ordine deciso dall'utente. Quest'ultimo si limita a scegliere quale ordinamento dare alle colonne.

Se per esempio si vuole sapere in quali regole compare l'oggetto XXXX basta scegliere nell'ordine le colonne "Oggetto" e "Regola". A questo punto compare l'elenco di tutti gli oggetti presenti nelle regole; se espandiamo la riga dell'oggetto XXXX troviamo tutte le righe della tabella originale che avevano tale oggetto nella propria regola, ordinate per regola.

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

![CFBASE_029](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_029.png)Figura 11 - La gestione del questionario in Looc.up

### La Scheda del Configuratore
L'accesso alle funzioni del configuratore avviene mediante un'apposita scheda (CFBASE).

Questa scheda è accessibile dal menù delle applicazioni di Loocup con il seguente percorso :  Menù Ingresso utente, *AP :  Applicazioni, LOOC_Up Graphic Environment, Schede, configuratore.

Verrà visualizzata la seguente scheda (Figura 12) : 

![CFBASE_037](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_037.png)  Figura 12 - La scheda del configuratore (CFBASE)

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

![CFBASE_036](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_036.png)Figura 13 - La scheda del questionario.

Analizziamo in dettaglio le 3 schede.
 :  : T04 La sottoscheda del questionario
La sottoscheda del questionario consente la navigazione e la manutenzione del questionario e di tutti i suoi componenti logici (sezioni, domande e valori).

Le prime informazioni che compaiono sono gli attributi del questionario (Figura 13).

Per ogni oggetto contenuto è attivo un menù di popup sensibile al contesto. In figura 13 si vede il popup di una sezione :  le ultime due voci consentono di aggiungere una pre o post regola.
Se queste sono già definite per la sezioni in questione si entrerà in manutenzione.

 :  : T04 La sottoscheda delle regole

Con un doppio click sul talloncino delle regole si ottiene che la scheda vada a pieno schermo : 

![regole](http://localhost:3000/immagini/CFBASE_TEC/regole.png)
 Figura 14 - La scheda delle regole

qui si possono vedere tutte le regole nella zona "Elenco regole" e selezionandone una si può vedere la scomposizione sulla sinistra e la sua traduzione in italiano sulla destra.

In basso un pulsante che consente la manutenzione.

Per aggiungere nuove regole su sezioni o domande ci si posiziona sulla scheda del questionario e con il tasto destro si accede a queste funzioni.

 :  : T04 La sottoscheda della configurazione

La sottoscheda elle configurazioni, visibile in figura 15, riporta sulla sinistra l'elenco delle configurazioni create, e sulla parte destra l'elenco delle risposte.

Posizionandosi su una configurazione e utilizzando il tasto destro, sotto la voce "Questionario" si hanno le azioni di Gestione, Visualizza o Elimina.

![CFBASE_026](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_026.png)Figura 15 - La sotto scheda della configurazione e il popup di gestione


### la compilazione di un questionario
Compilare un questionario porta alla creazione di una configurazione.

La creazione di una nuova configurazione avviene con il tasto F8 mentre la modifica di una precedentemente salvata avviene con la voce "Gestione questionario" e poi  "Gestione (Imm/Cop/Del)"  del popup della configurazione.

![CFBASE_024](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_024.png)Figura 16 -  La compilazione di un questionario in LoocUp


![CFBASE_039](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_039.png)sezione successiva, auto compilazione)
![CFBASE_022](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_022.png)visualizza la storia di esecuzione in tabella non ordinabile, visualizza in tabella ordinabile e filtrabile)
![CFBASE_021](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_021.png)regole, attiva ricerca all'interno delle regole, traduci le regole in italiano, esegui controllo su ricerca domande e/o sezioni duplicate)

## La compilazione su WEB
### Prerequisiti.
Buildup è integrato in WEB-Up e pertanto necessario avere un Web-Server con installato WEB-Up. Per le ulteriori informazioni si rimanda alla documentazione di WEB-Up.

### L'interfaccia WEB.
La compilazione su WEB è simile a quella che avviene in LoocUp. Visto l'ambiente nel quale ci si trova viene disattivata la traccia di esecuzione delle regole. Mancano anche i pulsanti relativi ai possibili controlli (duplicazione domande, controllo sintattico, rigenerazione motore regole).

Nella figura 17 si può vedere l'interfaccia della finestra di compilazione : 

![CFBASE_023](http://localhost:3000/immagini/CFBASE_TEC/CFBASE_023.png)Figura 17 -  La compilazione di un questionario mediante browser.

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
