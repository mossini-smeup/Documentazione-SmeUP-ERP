## Obiettivo
La scheda standard LOA08 permette di porre una serie di domande. A seguito della compilazione delle stesse si potrà semplicemente memorizzare le risposte o eseguire una scheda o una sottoscheda.

L'immagine definisce il funzionamento di base.

![LOCCOS_002](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA08/LOCCOS_002.png)
Le risposte alle domande verranno passate alla scheda richiamata in due modalità : 
* Come variabili di scheda, dal nome definibile dalla struttura di definizione delle domande oppure secondo una codifica automatica (G30nnn, dove nnn è il numero della domanda).
* Come parametro di input A08_VAR che come contenuto ha al suo interno l'elenco di tutto i parametri (con la codifica sopracitata) con i rispettivi valori.

## Richiamo del costruttore

Il costruttore può essere richiamato in scheda esplicitando i parametri riportati a seguire. Questo può essere un esempio : 
D.FUN.STD F(EXD;*SCO;) 1(CF;S-ccccc/s;*JOB) 2(MB;SCP_SCH;LOA08) 4(;;ORI) P(SCH(Scheda da Eseguire)  NDE(1) MDE(1) CTX(CF\S-cccccc/s\Contesto)) INPUT(EIM(1))

Dove : 
con ccccc si indica lo script del file SCP_CFG
con s si indica la sezione dello script
NOTA : 
Il nome dello script e la sezione vengono usate come parametro dell'oggetto CF, pertanto la lunghezza, comprensiva del simbolo "/", non deve superare gli 8 caratteri.
Normalmente si usano 5 o 6 caratteri per identificare lo script, e uno per il nome della sezione.

## Parametri di Definizione della Forma Grafica

* Nel richiamo diretto della scheda LOA08 l'informazione va indicata nell'oggetto 4 con uno dei seguenti valori : 
** " " - Per richiesta dati in versione Verticale con esecuzione scheda/sottoscheda
** "ORI" - Per richiesta dati in versione Orizzontale con esecuzione scheda/sottoscheda
** "SCE" - Per richiesta dati solo per scelta e memorizzazione parametri

* Parametri P
** SZA :  Permette di forzare la dimensione che si vuole attribuire alla sezione dei parametri. Se viene passato un numero è il numero di pixel, se viene passato un numero concatenato ad una % è la percentuale di occupazione della sezione.
** NDE :  Disattiva la presentazione delle descrizioni a meno che per queste non sia stata prevista la relativa forzatura nel configuratore (si veda l'help del configuratore sul campo "Cosa Emettere")
** NC :  Solo per scheda di "Solo Scelta", attribuisce un comportamento simile alla verticale (messaggi di segnalazione sopra e non nella barra messaggi). Utilizzato nelle schede UIR
** MS :  Se valorizzato ad 1 forza che la barra messaggi (attributo ShowMsgBar) vena omessa, e che i messaggi di errore vengano invece presentati con una finestra di dialogo specifica.

* Parametri di INPUT
** EIM :  Determina il modo in cui verrà eseguita la funzione richiamata : 
*** "1" = Tramite Tasto Invio
*** "2" = Esecuzione Immediata (in questo caso non dovrebbero essere previsti campi obbligatori)
*** " " = Tramite Tasto Funzione F06 di Conferma
** LAY :  Forza l'utilizzo di un layout applicato alla presentazione dell'input panel
** DSP :  Forza utilizzo di un DSPF per la costruzione dell'input panel. Vale la regola adottata per tutti gli altri formati, per i quali i campi video di descrizione devono avere codice corrispondente al campo di riferimento concatenato ad "_D", mentre i campi contenenti i tipi oggetto concatenati ad "_T"
** FMT :  E' obbligatorio se presente il precedente campo. Tramite esso viene determinato il formato video del DSPF.
** FCO :   Forza il n° di campi per colonna (solo per versione orizzontale). Se valorizzato con un valore superiore ad uno, questo verrà utilizzato per forzare un numero corrispondente di campi per ogni "colonna" dell'input panel.
** Q3 :  Valorizzandolo con un codice oggetto viene attivato il tasto funzione F13 per il richiamo della relativa scheda di filtro
** QRY :  In concomitanza con il campo precedente attiva che l'F13 vada sul filtro di ricerca (E/*RIC) invece che sul filtro di job (E/*JOB)
** TIT :  Se valorizzato viene attribuito come titolo della sezione di richiesta parametri
** TBS :  Forza l'attributo ToolBarState sulla sezione dell'input panel
** CLO :  Solo per scheda di "Solo Scelta", attiva un tasto funzione che forza la chiusura della scheda

## Parametri di Definizione delle Domande/Risposte

Le domande (e della loro memorizzazione) possono essere definite in tre modalità :  tramite un pgm _G30, tramite una configurazione o tramite il richiamo di un servizio che ritorni la schiera di una griglia (£JAXSWK). Di seguito vengono riportati i parametri interessati a questa definizione.

* Comuni : 
** Parametri P : 
*** EXIT :  Nome pgm di controllo per exit. NOTA BENE :  questa indicazione, se si sfrutta il configuratore, può essere specificata direttamente a livello di script di configurazione tramite il TAG di testa A08. E' questa la scelta consigliata, salvo casistiche particolari.
*** NME :  Disattiva la ripresa dei parametri memorizzati. Al caricamento tutti i parametri verranno riproposti con i valori di default.
** Parametri INPUT : 
*** RIS :  Permette di passare alla scheda una serie di risposte pre-compilate alle domande in questo formato :  RIS(CodiceRisposta1(ValoreRisposta1) CodiceRisposta2(ValoreRisposta2)). E' possibile inoltre specificare opzionalmente il trattamento grafico che si vuole attribuire a quel campo (fra i valori H,O,B per nascondere, proteggere, modificare il campo). In questo caso dopo aver esplicitato il valore va apposto un ";" seguito dall'attributo grafico come da seguente esempio :  RIS(CodiceRisposta1(ValoreRisposta1;H) CodiceRisposta2(ValoreRisposta2;O)).
*** RIV :  Permette di passare alla scheda come voglio essere trattate le risposte pre-compilate  Questo attributo non ha effetto quando viene utilizzato un formato video o quando nelle risposte viene specificato un attributo di trattamento specifico per la risposta. Può assumere i valori : 
**** H =  le risposte passate saranno nascoste
**** O = le risposte passate non saranno modificate
**** B = lascia modificare le risposte
*** NFC :  Non Confrollare le risposte. Disattiva il controllo di consistenza su tutti i campi
*** MDE :  Se valorizzato a 1, i dati non verranno memorizzato sul codice della configurazione passata (tipicamente *JOB), ma verranno memorizzati applicando come context della memorizzazione il contenuto del successivo parametro A08Ctx
*** CTX :  Contesto per il quale veranno effettuate le memorizzazioni della configurazione. Questo parametro viene preso in considerazione solo in compresenza del parametro MDE valorizzato a 1.
*** UTE :  forza un utente per salvare la configurazione diverso da quello del job
*** HLP :  attiva una sezione di help in cui è possibile vedere l'help del campo su cui sia ha il fuoco nell'input panel
*** MOD :  Se viene passato 15, l'input panel viene presentato in modalità visualizzazione
** T :  Forza l'attivazione di una modalità di test per cui gli errori non vengono più controllati
** T1 :  Tipo Oggetto 1 della scheda da richiamare
** P1 :  Parametro Oggetto 1 della scheda da richiamare
** K1 :  Codice Oggetto 1 della scheda da richiamare

* Se tramite pgm _G30
** Parametri P
*** AMB :  Nome MDV in cui salvare i propri parametri. Se non passato assume il valore G30+nomescheda da aprire (parametro SCH).
*** G30 :  Nome pgm della G30
*** PRO :  Parametro per pgm G30
*** CON :  Parametro per pgm G30
*** FUN :  Parametro per pgm G30
*** MET :   Parametro per pgm G30

* Se tramite Configurazione
** Oggetto 1 :  Se l'individuazione delle domande avviene tramite una configurazione, quest'ultima va passata come Oggetto 1 (es. 1(CF;S-xxxx;*JOB) )
** Parametri di Input
*** MDE :  se valorizzato a 1, i dati non verranno memorizzato sul codice della configurazione passata (tipicamente *JOB), ma verranno memorizzati applicando come context della memorizzazione il contenuto del successivo parametro CTX
*** CTX :  contesto per il quale veranno effettuate le memorizzazioni della configurazione. Questo parametro viene preso in considerazione solo in compresenza del parametro MDE valorizzato a 1.

* Se tramite Griglia fornita da un Servizio
** Parametri P
*** SER :  Nome del servizio da richiamare
*** SEF :  Funzione da passare al servizio da richiamare
*** SEP :  Parametri da passare al servizio da richiamare
** Parametri INPUT
*** CTX :  contesto per il quale veranno effettuate le risposte. Se non viene valorizzato, verrà assunta come chiave la combinazione del parametri sopracitati.

## Parametri di Definizione Scheda/Sottoscheda da eseguire

* Parametri P
** SCH :  Nome scheda a aprire
** SSC :  Nome sottoscheda (Facolativo)
** PAR :  Parametri P da passare alla scheda/sottoscheda che si vuol richiamare
** FIL :  Nome file della scheda da aprire (Viene assunto SCP_SCH)
** SI :  Forza la creazione di una variabile A08_SI nella quale in forma descrittiva vengono riportate le scelte effettuate. Può essere utile per evidenziare in una label le scelte effettuate.
** VLOO :  Setta le risposte come variabili di loocup. Il livelo della variabile (Sch, Loo, Ssc) dipende dal contenuto di VLOO
** VSER :  Setta le risposte come variabili di G91, il contesto è il contenuto della variabile VSER

* Parametri INPUT
** T1/P1/K1 :  Oggetto 1 da passare alla scheda
** INP :  Parametri INPUT da passare alla scheda/sottoscheda che si vuol richiamare
** PAR :  Parametri P da passare alla scheda/sottoscheda che si vuol richiamare
** VA :  Se valorizzato ad 1 le risposte vengono passate nei parametri input, ma contenute tutte in un unico parametro di input A08_VAR
** FOC :  Se valorizzato a No, forza che alla conferma delle questionario non venga dato il fuoco alla scheda di esecuzione
** LOF :  Attiva l'esecuzione della scheda finale sul dinamismo Lost Focus
** ITS :  Attiva l'esecuzione della scheda finale sul dinamismo ItemSelected
** NOT :  Attiva l'aggiornamento di una sezione che non sia quella della scheda finale, identificata dal contenuto del parametro NOT

## Struttura dell'exit

La struttura dell'exit prevede come parametri di entry : 
* Una campo funzione specifico dell'exit.
* Tutta la definizione dei parametri di richiesta, nella struttura della /COPY G11, a cui si aggiunge una schiera X11X per la gestione dei valori estesi (cioè i campi aventi lunghezza oltre i 20 caratteri)
* Tutta la DS della funzione di richiamo del servizio

In relazione alle possibiltà dell'exit è importante notare che : 
* Tipizzazioni dinamiche o gestione di ricerche particolari vanno gestite definendo il tipo oggetto del campo con blank o con ** o con tipo oggetto dinamico (cioè con le parentesi quadre). In questo modo tramite l'exit e le ricerche speciali (che vengono automaticamente attivate in presenza dei sopracitati tipi oggetto e pgm di exit) sarà possibile ottenere questi risultati.

Le funzioni per le quali viene richiatama l'exit sono le seguenti : 
* LOAD_PRE o RIC_PRE :  per modificare la struttura della richiesta parametri
* UPDATE o RIC_ESE :  per modificare il valore dei campi della richiesta parametri
* SET_SEA :  per modificare/aggiungere funzioni di ricerca specifiche
* SET_COM :  per modificare/aggiungere funzioni di ricerca combo specifiche

NOTA BENE :  nelle funzioni LOAD_PRE e RIC_PRE la struttura può essere modificata con queste limitazioni : 
* Non può essere modificato il numero di campi
* Non può essere modificato il codice dei campi
* Non può essere modificato il tipo oggetto dei campi, se si ha l'esigenza di rendere dinamica la tipizzazione di un campo sarà necessario aggiungere esplicitamente un campo nascosto in cui mettere il tipo oggetto variabile e far puntare il campo tipizzato dinamicamente al campo contenente il tipo oggetto

Per comprendere le possibilità dell'exit viene riportata di seguito la struttura specifica di elaborazione del flusso di gestione del costruttore : 

* _2_ESECUZIONE INIZIALE
** Carica dati e MDV
** Richiamo Exit con funzione _3_LOAD_PRE (modifica £11A, griglia ..), qui tutte le chiamate all'xit vengono fatte con XDAT valorizzata " " per indicare che sto elaborando i dati i fase di caricamento
** Controlli G11 standard (server)
** Richiamo Exit con funzione _3_UPDATE per £11M (valori) e £11E (errori)
** Richiamo Exit con funzione _3_SET_SEA (per ricerche aggiuntive ..)
** Richiamo Exit con funzione _3_SET_COM (per ricerche combo aggiuntive ..)

* _2_INIZIO LOOP
** Client :  se non prima volta ed OK esce e prosegue col dinamismo. Presenta :  si ferma Immissione dati ed enter (chiamato senza controlli). Se rinuncia esce.
** Esecuzione ricerche client + ricerche speciali (tramite lavoro aggiuntivo di emulazione LO_S per elaborazione di una singola ricerca alla volta). Per quest'ultime ogni chiamata è così strutturata : 
*** Richiamo Exit con funzione _3_LOAD_PRE interviene sulla griglia
*** Esecuzione G11 per controlli standard
*** Richiamo Exit con funzione _3_UPDATE per esecuzione ricerche speciali
*** Torna a client il campo di ricerca
** Viene rieseguita l'intera _2_ESECUZIONE INIZIALEma stavolta con la variabile XDAT valorizzata a "b" per indicare che sto elaborando i dati "before" della griglia
** Carica dati dal video in schiere G11
** Richiamo Exit con funzione _3_LOAD_PRE (modifica £11A, griglia ..), da qui in poi con la variabile XDAT valorizzata ad "a" per indicare che sto elaborando i dati "after" della griglia
** Griglia cambiata ? Se sì Richiamo Exit con funzione _3_UPDATE
** Controlli standard G11
** Richiamo Exit con funzione _3_UPDATE con errori di G11 (può togliere o aggiungere errori)
** Richiamo Exit con funzione _3_SET_SEA (per ricerche aggiuntive ..)
** Richiamo Exit con funzione _3_SET_COM (per ricerche combo aggiuntive ..)

* _2_FINE LOOP

### Cambiare i valori fissi nell'exit

Caso mai nasca l'esigenza di condizionare i valori fissi nell'exit vanno fatte queste considerazioni : 
* Essendo i valori fissi parte della definizione, i valori vanno reimpostati con le funzioni LOAD_PRE, RIC_PRE
* Il ricalcolo è opportuno che venga reimpostato solo al cambio delle condizioni tramite cui vengono determinati i valori da reimpostare. Il risultato di tale elaborazione dovrà essere poi salvato in schiere parallele e ripristinato poi per ogni chiamata. Questo perchè a seconda delle chiamate le schiere £11V posso arrivare, nella versione originale o nella versione già ritoccata dalle logiche dell'exit.

Per un esempio si rimanda all'exit LOA08_ES.

## Limitazioni.
Dal 17/12/2010 è possibile utilizzare più LOA08 come sottoschede della stessa scheda; da tale data perchè questo costruttore funzioni è necessaria una versione di Looc.up aggiornata almeno al 06/12/2010.
NB :  affinchè le più chiamate in parallelo possano funzionare è necessario che la chiamata al LOA08 avvenga in una scheda con titolo impostato (non *NONE), cioè :  G.SUB.SCH Tit="Titolo" D.FUN.STD F(EXD;JATRE18C;) 2(MB;SCP_SCH;LOA08) ecc...
