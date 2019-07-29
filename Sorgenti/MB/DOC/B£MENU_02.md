# Definizione

Il menù di accesso è la struttura di voci attraverso cui l'utente opera all'interno delle applicazioni.

# Struttura Applicativa

Per sua stessa definizione, il menù di accesso permette all'utente di accedere alle applicazioni. Per tale motivo le voci e i livelli del menù di accesso, proposti dallo standard, rispecchiano la struttura applicativa basata sulla gerarchia applicazione-moduli, che coincide con i primi due livelli di definizione dei menù (primo livello :  Applicazioni, secondo livello :  Moduli).

# Struttura Tecnica

Dal punto di vista puramente tecnico, la struttura di tutti i menù si appoggia alla tabella MEA. A differenza delle precenti versioni di Sme.UP, nelle quali la gestione della MEA era limitata alla sola emulazione, a partire dalla V4R1 la modifica di questa tabella e di tutti i suoi elementi è stata demandata al modulo (B£MENU), che garantisce un approcio semplice e diretto.
Dal punto di vista standard, la MEA prevede : 

1)  Un **sottosettore per ogni applicazione** (ogni sottosettore della MEA coincide con un elemento presente nella tabella delle applicazioni B£A), all'interno dei quali trovano luogo le voci di menù di tutti i moduli standard.
La corrispondenza tra i sottosettori della MEA e i codici codificati nella tabella B£A è garantita per tutte le applicazioni standard, eccezion fatta per i sottosettori V4 e V6 della MEA che non coincidono con delle vere e proprie applicazioni (in tabella B£A non esistono infatti degli elementi V4 e V6). Questi due sottosettori sono da considerarsi come derivazioni specifiche dell'originaria applicazione V5, che era di fatto adibita alla gestione sia del ciclo attivo che di quello passivo. In questo modo ora è possibile trovare nel sottosettore V4 le voci di gestione delle richieste di acquisto, nel V6 quelle relative alle vendite mentre nel sottosettore di MEA V5 le sole voci di gestione degli acquisti.
Ecco di seguito un estratto che risporta la corrispondenza degli elementi della B£A (a destra) e dei sottosettori della MEA (a sinistra) : 

![B£MENU_038](http://localhost:3000/immagini/B£MENU_02/BXMENU_038.png)
All'interno di ogni sottosettore della MEA (e quindi per tutte le applicazioni) è stato previsto che : 
* esista una voce scpecifica per ciascun modulo di una applicazione, che garantisca l'accesso alla scheda del modulo stesso. Tale richiamo è governato dal campo T$MEAE "Tipo Azione" che deve essere compilato con il valore "D" (_per maggiori informazioni si rimanda alla documentazione specifica del campo raggiungibile con l'F1 dalla tabella).
* tutte le voci della MEA siano abbinate a un modulo specifico tramite il campo T$MEAL "Modulo appartenenza", nel quale deve essere indicato un elemento della tabella B£AMO (il campo è tipizzato e pertanto è soggetto a controlli di consistenza)._ Per maggiori informazioni si rimanda alla documentazione specifica del campo raggiungibile con l'F1 dalla tabella.
2) **un sottosettore "00"** che racchiude tutte le voci del menù completo di ingresso.
In questo sottosettore trovano posto sia degli elementi, tipicamente lunghi quattro caratteri (es :  **1005**  BR - dati di base), che rappresentano le applicazioni standard, sia altri elementi rappresentativi del nuovo concetto di area applicativa. Come vedremo in seguito, ciascuna area applicativa rappresenta un criterio di raggruppamento delle varie applicazioni.
Per comprendere meglio quanto detto, si consideri l'area applicativa "Gestione anagrafici". All'elemento "000020 - Gestione Anagrafici" sono state associate le applicazioni : 
- BR  :  Basic records (applicazione)
- CF  :  Configuratore (applicazione)
- MT  :  Modifiche tecniche (applicazione)
L'abbinamento area applicativa/applicazione è stato gestito riordinando le voci presenti nel sottosettore 00 attraverso il campo T$MEAS "Ordinamento" _(per maggiori informazioni si rimanda alla documentazione specifica del campo).

In questo modo si ottiene una struttura  organizzata a più livelli e così configurata : 
Livello 0 :  AREA APPLICATIVA 1 (è un elemento del sottosettore 00 della MEA)
Livello 1 :  APPLICAZIONE XX (è un elemento del sottosettore 00 della MEA)
Livello 2 :  MODULO XX1234 (è un elemento del sottosettore XX della MEA, con azione "D" nel campo "Tipo Azione")
Livello 3 :  Azione di un modulo (elemento del sottosettore XX, con XX1234 nel campo "Modulo appartenza")

che in termini applicativi si traduce in : 

Livello 0 :  _7_AREA APPLICATIVA - Gestione Anagrafici  (elemento del sottosettore 00)
* Livello 1 :  >APPLICAZIONE :  BR Basic records  (elemento del sottosettore 00)
** Livello 2 :  __MODULO :  BRARTI  Articoli__ (elemento del sottosettore BR con Tipo azione "D")
*** Livello 3 :  AZIONE 1 :  Gestione articoli (elemento del sottosettore BR con Modulo appartenza "BRARTI")
*** Livello 3 :  AZIONE 2 :  Stampa articoli (elemento del sottosettore BR con Modulo appartenza "BRARTI")
** Livello 2 :  __MODULO :  BRCOMM Commesse__ (elemento del sottosettore BR con Tipo azione "D")
*** Livello 3 :  AZIONE :    Gestione commesse (elemento del sottosettore BR con Modulo appartenza "BRCOMM")
*** Livello 3 :  AZIONE :    Stampa commesse (elemento del sottosettore BR con Modulo appartenza "BRCOMM")
* Livello 1 :  >APPLICAZIONE :  CF Configuratore  (elemento del sottosettore 00)
** Livello 2 :  __MODULO :  CFBASE  Base__ (elemento del sottosettore CF con Tipo azione "D")
*** Livello 3 :  etc...
Come verrà esposto in seguito nella documentazione del menù di oggetto, questa struttura non è esaustiva della totalità delle azioni del menù del modulo, ma della sola parte descritta nella MEA (compresa sotto il titolo Actions).

Questa è la struttura proposta dallo standard, ma è comunque possibile realizzare strutture di MEA personali a tutti i livelli.
Il consiglio operativo è quello di rimanere nella struttura standard, personalizzandola in modo opportuno attraverso : 
* l'aggiunta di voci di menù personali nei menù standard
* l'aggiunta di sottosettori personali della MEA (se possibile da far coincidere con equivalenti elementi della tabella B£A) per la definizione di "applicazioni" personali
* l'omissione di voci/sottosettori standard attraverso le autorizzazioni.

A questo punto è bene fare una precisazione.
Questa nuova struttura, così come viene proposta, non  impatta solo a livello di riorganizzazione delle voci del menù, ma ha degli effetti anche a livello applicativo. Ciascuna voce infatti, essendo riconducibile in modo univoco a un modulo/applicazione, eredita da questi le autorizzazioni applicative.

 :  : DEC T(ST) P() K(B£A) I(Applicazioni)
 :  : DEC T(ST) P() K(B£AMO) I(Moduli)
 :  : DEC T(SS) P() K(MEA) I(Sottosettori della Tabella MEA)

 :  : INI Richiamo Gestione Ingressi Utente
 :  : CMD CALL B£UT55
 :  : FIN

# Client e interfaccia Grafica
I menù di accesso vengono resi graficamente in due modi differenti a seconda che l'accesso avvenga attraverso l'utilizzo di un client 5250 o del client Loocup.

## Accesso 5250
Accedendo tramite 5250, il menù di ingresso che viene visualizzato è il classico menù ad albero, strutturato in nodi e foglie e organizzato in più livelli. Il primo livello di questo menù corrisponde alle aree applicative introdotte nella MEA00, mentre esplodendo uno di questi nodi è possibile visualizzare tutte le applicazioni a essa abbinate.
![B£MENU_032](http://localhost:3000/immagini/B£MENU_02/BXMENU_032.png)Esplodendo poi ciascuno di questi nodi è possibile visualizzare prima i nodi relativi ai singoli moduli (ovvero a quelle voci di MEA che, in corrispondenza del campo T$MEAE "Tipo azione", hanno la "D") e, scendendo ancora di livello, le singole azioni di gestione.

## Accesso da Looc.UP
L'accesso tramite client Loocup, propone una schermata grafica composta da due sezioni : 
* La prima di sinistra che propone le voci organizzate ad albero corrispondenti alle aree applicative e applicazioni (vedi MEA sottosettore 00);
* La seconda di destra, predisposta al caricamento delle voci di dettaglio (elenco di moduli) legate all'applicazione selezionata nell'albero di sinistra.
I moduli che vengono caricati possono presentarsi in due formati grafici. La scelta di quale formato utilizzare per visualizzarli deve essere impostata nel campo "Grafica azione menù" (T$MEAQ di MEA00) sul codice dell'applicazione di appartenenza ovvero sull'elemento che identifica l'applicazione nel sottosettore 00. Le scelte possibili sono : 
* IMAGE LIST, ovvero una sequenza di icone (si veda la prima figura)
* ALBERO tradizionale aperto o chiuso (seconda figura).
Il risultato è il seguente : 
![B£MENU_033](http://localhost:3000/immagini/B£MENU_02/BXMENU_033.png)![B£MENU_034](http://localhost:3000/immagini/B£MENU_02/BXMENU_034.png)
Una precisazione :  ricordiamo che, nella sezione di destra vengono caricate tutte e sole le voci che nella MEA hanno il campo "tipo azione" compilato a "D" (Scheda del modulo), ovvero tutte le voci che corrispondono potenzialmente a un modulo. Perchè all'interno di questa riorganizzazione, il modulo ha assunto un ruolo di fondamentale importanza, essendo questo l'elemento rispetto cui sono state riviste tutte le azioni che appaiono sotto la voce "Actions", all'interno della scheda del modulo (per maggiori dettagli si veda il capito specifico "menù dell'oggetto" che spiega le regole che governano la composizione delle voci di menù di un oggetto).

## I menu personali (sottosettori X)
Per i propri menù (di sottosettori X) è invece possibile decidere liberamente se applicare la stessa impostazione a image list, oppure ad albero (monolivello) o ad albero a espansione dinamica, impostando il campo specifico T$MEAQ "Grafica azione menù"  nell'elemento di MEA del livello gerarchicamente più alto, con l'unica avvertenza che il menù di secondo livello in forma image list può essere utilizzato solo se il menù da presentare è monolivello (ovvero tutte le voci dipendenti non devono poter essere esplose e devono essere quindi delle semplici foglie).

## Il risultato in Looc.UP :  esempi di schermate
Per capire meglio quanto detto fino ad ora, si consideri l'esempio seguente.
Facendo riferimento alla figura, che riporta la videata standard di accesso di Looc.UP, si può notare : 
* la parte di sinistra, evidenziata dal riquadro rosso, che riporta nella struttura ad albero, l'elenco delle aree applicative e delle relative applicazioni
* la parte di destra, evidenziata invece dal riquadro giallo, in cui trovano posto le voci di secondo livello relative ai moduli dell'applicazione selezionata a sinistra, che possono essere presentate in formato "image list" o  ad "albero".
![B£MENU_035](http://localhost:3000/immagini/B£MENU_02/BXMENU_035.png)Cliccando su una icona si accede alla scheda del modulo corrispondente (nel caso in esame il BRARTI).
Le voci che compaiono sotto al titolo "Actions" sono invece gli elementi di MEABR che hanno il campo "modulo di appartenenza" compilato con BRARTI.
Per comprendere meglio le logiche che sono state seguite per la creazione degli elementi della MEA, si osservi la figura seguente che riporta in forma matriciale, la definizione delle actions del BR. Ricordiamo che questa immagine è stata ricavata dalla scheda di gestione deì menu presente nel modulo B£MENU.
![B£MENU_036](http://localhost:3000/immagini/B£MENU_02/BXMENU_036.png)![B£MENU_037](http://localhost:3000/immagini/B£MENU_02/BXMENU_037.png)
Il riquadro rosso della figura precedente riporta l'elenco delle voci di MEABR. Come si può vedere, le voci legate al BRARTI sono in totale 5 : 
* Codice azione 0100 :  è la scheda del modulo. Questo lo si uintuisce dalla presenza del valore "D" nel campo "Tipo azione" _(si veda il cerchio verde dell'immagine)_;
* Codice azione 0101 :  "Gestione articoli" è la prima voce che troviamo tra le actions del modulo;
* Codice azione 0102 :  "Stampa articoli" corrisponde alla seconda voce che troviamo tra le actions;
* Codice azione 0109 :  "Funzioni per articolo" non compare tra le actions del modulo poichè questa voce, avendo il campo "Solo emulaz/Looc.UP" a "1", compare solo nel menù di 5250 _(si veda il cerchio blu).
* Codice azione 0110 :  "Accesso facilitato", come la voce 0109, non compare tra le actions del modulo poichè ha "1" nel campo "Solo emulaz/Looc.UP" _(si veda il cerchio blu)._

**NOTA 1 : ** Occorre fare una precisazione per quanto riguarda i moduli naturati e/o parametrati. Consideriamo per esempio il modulo generico BRENTI che, a seconda della natura, può essere declinato in BRENTI1, BRENTI2, BRENTI3, etc. L'attuale struttura dei menù dei moduli prevede che al modulo BRENTI1 vengano collegate tutte le voci di MEA che abbiano nel campo  "Modulo appartenenza" sia il valore BRENTI1 che il valore BRENTI. Questo meccanismo di risalita è valido anche per i moduli per i quali è stato esplicitato e fissato il parametro. Se infatti consideriamo il modulo BRENTI1CLI (1=natura; CLI=parametro), nelle sue actions troveremo le voci di MEA che sono state abbinate al modulo BRENTI1CLI, BRENTI1 e BRENTI.

**NOTA 2 : ** Un discorso a parte deve essere fatto per i moduli così detti BASE, ovvero quei moduli presenti in tutte le applicazioni e che raccolgono quelle azioni di base che possono essere considerate comuni ai vari moduli dell'applicazione. Le actions di questi moduli, salvo alcune eccezioni, non sono state definite nella MEA come accade per tutte le altre voci, ma traggono la loro origine da un'altra fonte. Rimandiamo la spiegazione di questo punto al documento "menu di un oggetto".

# Aggiornamento/Popolamento delle voci standard dei menù di accesso.

Per generare le voci di menù standard è sufficiente lanciare l'esecuzione del pgm B£MNU0, che cancella e riscrive tutti i sottosettori della tabella MEA corrispondenti agli elementi della tabella B£A (in questa rigenerazione solo le voci con codice alfabetico che vengono riconosciute come personalizzazioni non vengono toccate). Il pgm può anche essere richiamato applicazione per applicazione.
Tale aggiornamento è fortemente consigliato ed è sempre compreso nelle PTF di upgrade di SMEUP.

 :  : INI Richiamo pgm di allineamento dei menù di accesso.
 :  : CMD CALL B£MNU0
 :  : FIN

# Personalizzazione dei menù di accesso

Come anticipato, i menù standard possono essere personalizzati attraverso i seguenti strumenti : 
* 1) l'aggiunta di voci personali a menù standard
* 2) l'aggiunta di sottosettori personali della MEA (se possibile da far coincidere con equivalenti elementi della tabella B£A) per la definizione di "applicazioni" personali
* 3) l'inibizione o abilitazione delle voci di menù attraverso le autorizzazioni per utente o gruppo utente.

Vediamo ora in dettaglio ognuno di questi tre punti.

## 1) Aggiungere voci personali a menù standard
L'aggiunta di voci personali nei menù standard consiste nell'inserimento di nuovi elementi ai sottosettori della tabella MEA corrispondenti ad applicazioni standard (elementi della tabella B£A che non iniziano per X o Y). Fra tutte le voci standard, quelle personalizzate si riconoscono dalla presenza di __almeno una lettera nel codice dell'elemento__ dal momento che le voci standard sono caratterizzate da codici esclusivemente numerici.
L'inserimento di una voce personale nella MEA standard può avere effetti a livelli diversi a seconda di come questa voce viene configurata. Definendo in modo opportuno questa nuova voce, essa può trovare posto : 
*  Tra le ACTIONS di un MODULO, compilando correttamente il campo T$MEAL "modulo appartenenza". _Riempiremo quindi questo campo con "BRARTI" se vogliamo inserire nelle actions di questo modulo una nuova voce di menù; è ovvio che tale voce personale dovrà essere inserita nel sottosettore BR, essendo il BRARTI  un modulo di questa applicazione (le prime due lettere del modulo indicano l'applicazione cui esso appartiene).
* Tra i MODULI di una APPLICAZIONE, mettendo la "D" nel campo  T$MEAE "Tipo Azione" e lasciando invece il campo T$MEAL "modulo appartenenza" vuoto. _Questo avrà come effetto quello di aggiungere una voce all'interno della sezione di destra della schermata iniziale di Looc.UP. Se la voce che andiamo ad aggiungere è una voce persoanle, che vogliamo appartenga a un applicazione standard, dovremo compilare il campo  _T$MEAP_ "No modulo su std" con la lettera **N.**
* Nel MENU DI ACCESSO, ovvero nella sezione di sinistra della scheda di partenza, a livello di area applicativa/applicazione :  in questo caso sarà necessario aggiungere la voce personale al menù di accesso dell'utente nel sottosettore 00.

Nell'aggiunta delle voci personali a un menù standard, un caso che richiede particolare attenzione è quello dei moduli parametrati. Ricordiamo che i moduli parametrati sono moduli intestati a oggetti che prevedono un parametro obbligatorio (per conoscere le caratteristiche di un modulo si veda la /COPY £K01- Funzioni su Modulo).
Esempi di moduli parametrati sono il V5DOCU (declinato in tutte le sue nature V5DOCU1, V5DOCUA...), dove il parametro è il tipo documento o il BRENTI (anche questo declinato in tutte le sue nature BRENTI1, BRENTI2...) dove il parametro è invece il tipo ente. Nella scheda di questi moduli e nelle varie actions a essi collegate, viene quindi sempre richiesta l'identificazione dell'istanza del parametro (ovvero viene sempre richiesto il TIPO dell'oggetto), al fine che tutte le voci del menù del modulo ne tengano conto. Alla luce di quanto illustrato, può nascere la necessità di creare un accesso diretto e facilitato a un modulo con parametro fisso (esempio :  BRENTI1CLI per vedere tutti gli enti di natura 1 e di tipo CLI).
Questo effetto può essere ottenuto seguendo queste due istruzioni : 
1) Aggiungere come prima cosa il codice ottenuto dalla concatenazione del modulo e del parametro agli elementi della tabella dei moduli B£AMO (es. se parlo dei clienti creo l'elemento BRENTI1CLI nella tabella B£AMO).
2) Aggiungere poi nel sottosettore corrispondente della MEA (nel nostro caso sottosettore BR), una voce di menù personalizzata che abbia la "D" nel campo T$MEAE "Tipo Azione" e il nome del modulo concatenato (BRENTI1CLI) nel campo T$MEAL "modulo appartenenza".

Riportiamo i seguito un breve prospetto che riassume le regole da seguire per la concatenazione di modulo/natura/parametro.
Definiamo con MMMMMM il modulo, con N la sua natura e PPP un suo possibile parametro. A seconda delle caratteristiche del modulo possiamo avere : 
* un modulo personale senza natura e parametri (6 caratteri) :  MMMMMM.
* Un modulo parametrato non naturato (il parametro è obbligatorio ma tutti i parametri sono equivalenti). In questo caso il modulo parametrato risultante sarà :  MMMMMMPPP
* Un modulo parametrato con natura facoltativa (ad esempio le risorse). Si può aggiungere un modulo **MMMMMMPPP**, oppure **MMMMMMNPPP** (NB :  la congruenza tra natura N e parametro PPP è a cura di chi inserisce l'elemento di tabella).
* Un modulo parametrato con natura obbligatroria (ad esempio gli enti) :  si può aggiungere un modulo **MMMMMMNPPP** (NB :  anche in questo caso la congruenza tra natura N e parametro PPP è a cura di chi inserisce l'elemento di tabella).

## 2) Aggiungere menù personali
L'aggiunta di menù personali consiste nella creazione di nuovi sottosettori della tabella MEA (per ogni nuovo menù di accesso occorre definire un nuovo sottosettore di MEA). Per non creare sovrapposizioni con i menù proposti dalla standard, i codici di questi nuovi menù personali devono iniziare  tassativamente con X o Y, oppure devono avere un codice totalmente numerico diverso da 00. Tali menù potranno poi essere strutturati come i menù standard, per applicazione/modulo, oppure come semplici menù d'azioni.
Essi possono venire richiamati : 
* Come menù di accesso degli utenti. Ciò significa che un utente, cui è stato associato un menù X1, si vedrà nella sezione di sinistra le voci presenti nella MEAX1.
* Come richiamo nel menù di accesso (una delle voci del menù di accesso richiama il menù X1). In questo caso il menù X1 può essere visto al ari di una applicazione.
* Come richiamo all'interno di altri menù

## 3) Togliere voci standard
Le voci standard possono essere inibite attraverso l'utilizzo delle autorizzazioni. Le autorizzazioni delle voci di menù, presentano una struttura articolata, in quanto su di esse convergono più logiche di autorizzazione (tutte con la risalita utente / gruppo utenti / **) : 
* La forma di autorizzazione più semplice è __l'autorizzazione sulla "voce" di menù__. Questa forma di autorizzazione si appoggia alla classe MNU e permette di autorizzare/disautorizzare la singola voce di menù. Rispetto ad essa è importante sottolineare questi aspetti : 
** La funzione della classe MNU è così composta :  ME;parametrovocemenù;vocemenù. Il parametro della voce può essere identificato attraverso l'oggetto MP (corrispondente alla /COPY £IMP), mentre la voce attraverso l'oggetto ME (corrispondente alla /COPY £IME). Tale informazione non è così poi così importante come verrà esposto di seguito, viste le funzionalità disponibili per l'accesso alla gestione delle autorizzazioni, in questa sede si cita solo che il parametro può corrisponde a questa forma *applicazione (es. ME;*xx;nnnnn) o alla forma M_codicemodulo (es. ME;M_codicemodulo;nnnnn) se la voce è stata attribuita ad un modulo.
** E' prevista una funzione in particolare così composta :  ME;parametrovocemenù;**, attraverso cui è possibile disattivare di default tutte le voci del menù, ad eccezione di quelle esplicitamente autorizzate.
Relativamente a questo aspetto è importante notare che se la voce disautorizzata è un titolo, automaticamente vengono omesse tutte le voci che stanno al di sotto di essa sia che esse risultino autorizzate.

* Un modo più robusto di autorizzare in modo più esteso le voci della MEA è il seguente. Una voce di Mea può (e nello standard deve) appartenere ad un'applicazione e ad un modulo. Disautorizzando l'applicazione (TA;B£A;xx) con la classe **OGG.MAS**, vengono disautorizzati tutti i moduli e tutte le loro voci, ovunque vengano richiamati. Disautorizzando il modulo (TA;B£AMO;xxxxxx), con la stessa classe OGG.MAS,vengono disautorizzate tutte le sue voci, ovunque vengano richiamate. **NOTA BENE** :  la verifica delle autorizzazioni OGG.MAS viene effettuata attraverso la /COPY £AUO. Tale classe viene richiamata in questo modo : 
** Quando la voce presenta l'indicazione di un modo viene verificata l'autorizzazione del modulo, sempre con risalita al test dell'applicazione di appartenenza del modulo
** In generale per verificare se "l'applicazione" è autorizzata non viene verificata direttamente l'applicazione, ma il sottosettore della MEA. Se poi il sottosettore corrisponde ad un'applicazione allora la £AUO sposta il controllo sull'applicazione. Unica eccezione a tale considerazione è il SS;MEA;V5 :  essendo il menù dell'applicazione V5 spezzato sui sottosettore V4/V5/V6 (richieste d'acquisto, acquisti, vendite) il test viene sempre effettuato solo a livello di sottosettore (quindi se voglio verificare l'autorizzazione su menù C5 viene verificata l'autorizzazione su TA;B£A;C5, mentre se voglio testare l'autorizzazione sul menù V5, viene testatao SS;MEA;V5).

* Trasversalmente alle autorizzazioni citate sinora si pone poi l'autorizzazione USRLVL. Questa è una classe che va obbligatoriamente impostata a livello di utente/gruppo utente, al fine di individuare il ruolo dell'utente. Questa classe è fondamentale in quanto persistente in tutto il gestionale. Dal punto di vista dei menù di accesso essa viene utilizzata per effettuare un confronto fra il livello di un utente e queste istanze : 
** Voce di menù, se previsto nella singola voce di menù della tabella MEAxx
** Modulo, se previsto nell'elemento della tabella B£AMO
** Applicazione, se previsto nell'elemento della tabella B£A

* Anche la classe utente USRLVL tiene conto delle gerarchie fra titoli, e voci di menù appartententi ad applicazione / modulo, con la validità locale delle autorizzazione delle voci sottostanti ad un titolo, e la validità generale dell'autorizzazione delle voci di una applicazione/modulo.

Le sopracitate autorizzazioni verranno sempre verificate anche per le azioni aggiunte ai preferiti. Quindi se ad un certo punto un utente cambia le sue autorizzazioni, le azioni preferite corrispondenti ad azioni non più autorizzazione verranno omesse. Tecnicamente questo è possibile perchè nei menù i singoli nodi riportano le informazioni relative ai livelli di autorizzazioni controllati e tali informazioni vengono memorizzate quando il preferito viene salvato.

* Infine va fatta questa considerazione generale rispetto ai titoli : 
** Se tutte le voci al di sotto di un titolo sono disautorizzate, automaticamente anche il titolo, verrà omesso
** Se viene disautorizzato un titolo, anche tutte le voci che sono al di sotto di esso verranno omesse. Attenzione :  questa autorizzazione opera solo "localmente" :  le voci sottostanti non risentono dell'autorizzazione del menu se sono richiamate in modo diverso (Es. aggiungo una voce di menù sotto ad un certo titolo ad un preferito, se disattivo successivamente il titolo, nel menù tale voce non sarà visibile, ma sarà cmq visibile/richiamabile nei preferiti)

Questa struttura di autorizzazioni viene presentata nella scheda di gestione delle autorizzazione dei menù, che si raggiunge nei seguenti modi : 
* tramite le apposite voci predisposte nei menù dei moduli B£MENU e B£AUTO (sotto voce "autorizzazioni menù di accesso")
* attraverso la specifica voce di popup che si apre sulla voce di menù nell'interrogazione del menù stesso.

Il controllo delle autorizzazioni è principalmente demandato alla /COPY £AUO.
 :  : DEC T(MB) P(QILEGEN) K(£AUO) L(1).

La gestione delle suddette autorizzazioni è richiamabile dai seguenti punti : 
* Menù del modulo B£MENU
* Menù del modulo B£AUTO
* Tasto destro su qualsiasi azione di menù




























