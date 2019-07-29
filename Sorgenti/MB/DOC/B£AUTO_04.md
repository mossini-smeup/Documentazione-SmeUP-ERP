# Introduzione
Per configurare correttamente il menù che gli utenti si trovano davanti quando si collegano a Sme.UP occorre seguire una logica deduttiva, partendo quindi dalle voci più generali del menù (aree applicative e applicazioni) per arrivare a quelle più particolari (gestione di un oggetto). La presentazione riguarderà la configurazione del menù standard, ma le logiche che vengono applicate possono essere ripetute anche per eventuali menu personali.
Partiremo quindi dalle autorizzazioni del livello generale di area applicativa per poi arrivare alle voci di dettaglio degli oggetti.
![B£AUTO_01](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_01.png)Per maggiori dettagli sui nuovi menù si rimanda alla documentazione specifica : 
- [Menù di Accesso Utente](Sorgenti/MB/DOC/B£MENU_02)

# Autorizzazioni di MENU

## 1. Dove impostare le autorizzazioni del menù
La prima cosa da fare è impostare le voci di menu della MEA, utilizzando la nuova scheda delle autorizzazioni raggiungibile dalla voce _Autorizzazione Menù_ del modulo B£AUTO. In realtà queste impostazioni di carattere generale possono essere definite anche all'interno del modulo B£MENU, attraverso la voce _Autorizzazione Menù Accesso_. Le due strade portano alla stessa scheda.

## 2. Come procedere nella definizione
Si deve partire prima di tutto con le voci del SS della MEA, quelle cioè che formano il menù iniziale di accesso (ovvero quello per aree applicative).

Per abilitare o disabilitare le voci di questo menù possiamo agire su tre colonne : 
* __SS della MEA disabilitato : __ da usare se si vuole inibire un intero SS della MEA. Spuntando questa colonna, tutte le voci del SS si evidenziano di rosso, a prova del fatto che per l'utente impostato nei filtri, quel preciso SS è stato disabilitato.
* __Applicazione disabilitata__ :  mantenendo il valore della colonna precedente pulito, questa colonna consente di autorizzare sempre nell'ambito del SS 00, le varie applicazioni. Spuntando un'applicazione, tutte le sue voci vengono disabilitate automaticamente. Operando in questo modo, l'applicazione non solo sparisce dal menù iniziale di Looc.UP ma risulta essere inibita anche in tutte le varie navigazioni successive (FLY).
* __Voce disabilitata__ :  svolge la stessa funzione della colonna precedente, ma il suo effetto è meno restrittivo perché, benché l'applicazione disabilitata non compaia comunque all'interno del menù iniziale, questa rimane visibile nelle navigazioni proprie di Looc.UP come i FLY.

![B£AUTO_02](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_02.png)Per comprendere meglio il significato di questa matrice, riportiami una breve legenda che spiega l'intestazione di alcune colonne : 
* **V** = Autorizzazione VOCE
* **M** = Autorizzazione MODULO
* **A** = Autorizzazione  APPLICAZIONE
* **S** = Autorizzazione SOTTOSETTORE

Lo scopo di queste colonne è di segnalare in forma sintetica e immediata la mancanza/preseenza di un'autorizzazione, informazione che è comunque reperibile consultando tutte le altre colonne della matrice. In base al valore contenuto da ciascuna cella, queste colonne possono contenere le seguenti lettere che assumono il significato riportato di seguito : 
a) **n** = l'elemento, sia esso una voce, un modulo una applicazione o un sottosettore NON è autorizzato;
b) **u** = manca l'autorizzazione a livello di USER LEVEL (classe di autorizzazione USRLVL);
c) **n-u** = l'elemento è disautorizzato e lo userlevel dell'utente non è compatibile con quello richiesto.
d) **g** = la voce è disabilitata globalmente. Questa lettera compare nel momento in cui è stato inserito un record di autorizzazione di claase MNU e funzione ME;*xx;**

Una volta che sono state impostate le autorizzazione del SS 00 della MEA, è possibile aumentare il livello di dettaglioper impostare le autorizzazioni all'interno di ogni singola applicazione. Per fare questo è sufficiente cliccaee sulla lente di ingrandimento presente nella seconda colonna della matrice. La lente, come consueto,  sta a indicare la possibilità di entrare nel dettaglio di una voce :  in questo caso ci permette di entrare nella gestione dei moduli di una applicazione.

Una precisazione. Se si vuole utilizzare il modulo B£MENU per imposatre le autorizzazioni del SS 00 della MEA per utente o gruppo utente, lo si può fare usando la vcoe _Autorizzazione menù iniziale. LA scehda che si apre presenta prima l'elenco degli utenti suddivisi in gruppi e, nella parte bassa, la matrice che abbiamo appena presentato. Per il suo utilizzo si rimanda a quanto detto sopra.

La lente di ingrandimento presente all'inizio di ciascuna riga di queste matrici, permette di visualizzare in un formato simile a quello presentato fino a ora, le voci specifiche della'pplicazione :  i moduli. A questo punto è possibile impostare le autorizzazioni sfruttando le tre colonne : 
* __Applicazione disabilitata__ :  questa colonna permette di disabilitare in modo netto e completo l'accesso all'applicazione e di conseguenza anche quello ai suoi moduli.
* __Modulo disabilitato__ :  ci permette di abilitare o disabilitare completamente quei moduli che si vogliono mantenere protetti.
* __Voce disabilitata__ :  come la colonna precedente, anche questa permette d proteggere i moduli togliendoli dal menù iniziale di accesso. Questa protezione è però, a differenza della precedente, meno robustaperchè in realtà non agisce sulle navigazioni FLY di Looc.UP. Questo significa che se si vuole proteggere un modulo rendendolo inaccessibile agli utenti, questo solo flag non basta perchèin realtà non inibisce la sua apertura né dai FLY né dalle ricerche con l'F4.
Per comprendere meglio gli effetti di queste colonne, riportiamo di seguito questo prospetto : 

TABELLA

L'utilizzo della matrice in scheda nella costruzione dei menù di accesso semplifica notevolmente l'attività di configurazione iniziale, dal momento che ogni spunta inserita in matrice corrisponde a un preciso record del file delle autorizzazioni, di classe OGG.MAS con una funzione legata alla tabella B£A o B£AMO a seconda che si tratti di applicazioni o moduli. Uniche eccezioni a queste funzioni sono quelle legate alle pseudo-applicazioni V4/V5/V6 che, non essendo elementi specifici della tabella B£A (in cui troviamo la sola V5), vengono gestite con funzioni legate al SS della MEA corrispondente. Troveremo quindi record di classe OGG.MAS con funzione SS;MEA;V4 o record del tipo OGG.MAS con funzione TA;B£A;BR,
 Inutile ribadire che la scrittura manuale di questi record richiederebbe molto tempo e particolare attenzione.

## 3. Menu personali e versioni precedenti di Sme.UP :  la compatibilità delle autorizzazioni
Chi ha avuto modo di impostare menù e autorizzazioni con versioni precedenti all V4R1, avrà sicuramente notato il grande abisso che separa queste nuove impostazioni da tutto ciò che c'era prima. Esempi di queste differenze sono le impostazioni del primo menù di accesso, la suddivisione per aree applicative e applicazioni, la rappresentazione in image list, etc. A fronte di tutto questo, la prima domanda che sorge spontanea è come è possibile mantenere e adattare i vecchi menù, soprattutto quelli personali, e le relative autorizzazioni al nuovo sistema.
La risposta è semplice.

Partiamo dai menù.

1) La prima differenza che si nota è la __forma grafica dei menù__ (si è passati dal vecchio albero delle applicazioni e dei moduli al nuovo menù a image list). per poter riporatre il menù standard della V4R1 alla forma grafica ad albero, occorre intervenire nella voce di MEA e togliere la **"I"**, per le applicazioni che devono essere visualizzate ad albero (sottosettore 00 della MEA), dal campo  _Grafica Azione Menù_. Questo farà in modo che i moduli dell'applicazione vengano caricati tramite albero e non più con le icone.

2) __Menù personali__, tipo X1. Tutti i menù personali definiti come sottosettore della tabella MEA hanno in questa versione la stessa valenza che avevano in quelle precedenti. Nella V4R1 sarà quindi ancora possibile fare in modo che un utente si colleghi a un menù X1 specifico e che veda nella parte centrale della schermata, tutte le voci definite in tabella. L'unica accortezza che bisognerà avere con questa nuova versione, sarà quella di impostare in che modalità grafica questo menù si dovrà vedere, se a icone o ad albero.
Per poter adeguare i vecchi tracciati della MEA a quelli nuovi, sono state create due PTF, la numero **££30901A** e la **B£30901V** , che si preoccupano di fare proprio questo.
Sebbene l'inetnto di questa documentazione non sia quello di spiegare l'applicazione di questa PTF, ci prendiamo la libertà di sottolineare che questa Pre-PTF deve essere OBBLIGATORIAMENTE applicata prima di qualsiasi altra PTF o pre-PTF per il passaggio alla V4R1, in quanto comporta l'esecuzione di azioni che vanno fatte in ambienti con in linea ancora i programmi della release precedente.
DEC T(MB) P(PTF) K(££30901A)
DEC T(MB) P(PTF) K(B£30901V)

3) Le autorizzazioni. Anche per il recupero di queste sono state implementate delle PTF, atte sia all'adeguamento delle autorizzazioni vecchio formato che all'inizializzazione di alcuni nuovi record.
Ne riportiamo alcune : 
DEC T(MB) P(PTF) K(B£30901S)
DEC T(MB) P(PTF) K(B£30901U)
DEC T(MB) P(PTF) K(££30901B)


# Autorizzazioni di menù particolari :  il bottone UP £L e il menù di sezione £S
Il menù £L e il menù £S sono due nuovi menù introdotti nella V4R1. Per conoscerli meglio, rimandiamo alla loro documentazione specifica : 
- [Due nuovi menu&-x3a; £L e £S](Sorgenti/MB/DOC/B£MENU_03)

# Autorizzazioni ingressi master :  note tecniche
Rimandiamo al documento successivo il dettaglio relativo ai tecnicismo alla base del funzionamento di queste autorizzazioni : 
- [Autorizzazione ingressi&-x3a; generalità e tecnicismi](Sorgenti/MB/DOC/B£AUTO_09)


# Esempi di autorizzazioni

## Applicazione abilitata per un solo utente
Ci proponiamo come obiettivo quello di impostare delle autorizzazioni legate all'applicazione BR per un generico gruppo utente. Vogliamo che tutti gli utenti di questo gruppo non accedano a questa applicazione, eccezione fatta per un singolo utente.
![B£AUTO_E1](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_E1.png)Scegliere la voce Autorizzazione menù e impostare il gruppo utente e il menù  00 negli appositi campi. Impostare quindi per tutto il gruppo utente il flag nella colonna Applicazione Disabilitata in corrispondenza della riga BR. Questo ci assicura che tutti gli utenti del gruppo non avranno accesso all'applicazione né dal menù iniziale, né dai FLY di navigazione. A questo punto, per l'utente che invece deve essere autorizzato, possiamo procedere a togliere questo stesso flag abilitandolo così alla visualizzazione della BR, dopo che nell'input panel avremo indicato esattamente il suo codice utente. Questo quindi si traduce in un record di tipo OGG.MAS/**GU/TA;B£A;BR con valore 91 e un record OGG.MAS/utente/TA;B£A;BR con valore 99.

## Un solo modulo autorizzato per un utente
Ci proponiamo come obiettivo quello di impostare delle autorizzazioni legate a un preciso modulo, quello degli articoli BRARTI, dell'applicazione BR. In particolare vogliamo che l'utente possa accedere soltanto a questo modulo e non a tutti gli altri presenti nell'applicazione BR.
Impostare quindi il codice utente e l'applicazione BR nell'input panel e premere invio.
![B£AUTO_E2](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_E2.png)A questo punto occorre fare in modo che : 
1) L'intera applicazione risulti abilitata :   questo lo si capisce dal fatto che la matrice non presenta record evidenziate in rosso.
2) Il modulo BRARTI rimanga accessibile :  non bisogna impostare nessun flag nelle colonne  voce/modulo/applicazione  disabilitata.
3) Tutti gli altri moduli siano protetti :  occorre impostare il flag nella colonna Modulo Disabilitato se si vuole una protezione forte, o nella colonna voce disabilitata se si vuole una protezione debole.

![B£AUTO_E3](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_E3.png)
E questo è il risultato.

![B£AUTO_E4](http://localhost:3000/immagini/B£AUTO_04/BXAUTO_E4.png)
Come si può vedere l'utente può accedere solamente al modulo degli articoli.
