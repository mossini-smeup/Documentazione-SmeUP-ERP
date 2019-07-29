# Definizione
Il menù di un oggetto è l'insieme di voci e azioni che viene attribuito a ciascuna entità riconosciuta da SmeUP (articoli, clienti, movimenti di magazzino, ordini di produzione, etc.). Un'entità "particolare", meritevole di un approfondimento, è il MODULO che, pur non essendo un oggetto vero e proprio, è stato dotato di un proprio menù. Procederemo nel  seguito di questo documento a presentare le caratteristiche  di base di queste due strutture (menù di un oggetto generico e menù di oggetto modulo) .

# Struttura Applicativa

Per definizione il menù di oggetto è l'insieme di azioni che possono essere applicate ad un particolare oggetto di SmeUP.

# Interfaccia Grafica

In ambiente grafico LoocUP, il menù di oggetto è richiamabile in queste due modalità : 
* All'interno della scheda dell'oggetto, qualora sia stata prevista per questa la forma grafica dell'hyper menù (figura 1).
* Attraverso il menù a tendina (chiamato anche popup), contestuale all'oggetto, che può essere invocato in qualsiasi punto in cui l'oggetto sia identificabile nella schermata video (es. cella di matrice o nodo albero) attraverso la pressione del tasto destro del mouse.
* Il menu di modulo è invece richiamabile, dopo aver selezionato un'applicazione, cliccando la sua icona nella parte a destra del menu iniziale (figura 2).

![B£MENU_039](http://localhost:3000/immagini/B£MENU_05/BXMENU_039.png)![B£MENU_040](http://localhost:3000/immagini/B£MENU_05/BXMENU_040.png)
**NOTA** :  come si può vedere dalle immagini appena riportate, il menù di un oggetto (fig.1) e il menù di un modulo (fig.2) appaiono molto simili, per lo meno nella loro struttura. Per facilitare la navigazione all'interno di LoocUP e rendere l'utilizzatore finale in grado di capire in ogni momento in quale punto di trovi, è stato pensato di colorare gli sfondi di tali menù con tonalità differenti. Nello specifico, i menù di un oggetto hanno sempre uno sfondo giallo paglierino (fig.1), mentre lo sfondo dei menù dei moduli è sempre grigio (fig.2).

In ambiente 5250, il menù di oggetto è richiamabile a seconda che l'oggetto sia un modulo o un'altro oggetto nei seguenti modi : 
* I menù oggetto dei moduli, sono inclusi nelle schermate dei menù di accesso standard. Essendo questi organizzati per applicazione, all'interno di ognuno di questi menù si trovano le voci dei moduli appartenenti alla particolare applicazione. I moduli sono immediatamente identificabili nei titoli di primo livello (che tecnicamente hanno come tipo azione "D" nell'elemento della tabella MEA).
* I menù di qualsiasi altro oggetto, possono essere richiamabili, apponendo il carattere "%" al codice in un campo di imputazione di un particolare oggetto e dando invio, o indicando il carattere "%" all'interno dell'opzioni di riga (pur essendo una tendenza generale in SmeUP, quest'ultima possibilità è presente solo qualora sia stata prevista dallo specifico programma)

## Composizione Standard
Sempre mantenendo la suddivisione fra moduli ed altri oggetti, viene qui riportata la composizione dei menù oggetto standard.

### Moduli
![B£MENU_042](http://localhost:3000/immagini/B£MENU_05/BXMENU_042.png)
* **Dashboard** :  è la funzione che viene richiamata ogni volta che si accede al modulo e di norma permette di eseguire un'elaborazione statistica dei dati di competenza del modulo. Il nome della scheda da richiamare viene ritornato dalla funzione £J11 e, salvo alcune eccezioni,  è definito dal nome del modulo stesso seguito da "_CRU". Dal punto di vista dei contenuti, come accennato in precedenza, questo Dashboard riporta delle informazioni statistiche specifiche del modulo ricavate dagli archivi di competenza. Unica eccezione è il modulo base (denominato XXBASE, dove XX è la sigla dell'applicazione), che ha alcune particolarità. Nei Dashboard dei moduli base infatti, viene presentata la lista dei moduli da cui, cliccando, si presenta il dashobard relativo. Se il modulo base ha un archivio "proprio" (ad esempio i dati di articolo/pianificazione per il  modulo M5BASE), viene presentato anche un dashboard specifico.

* **Info** :  visualizza le informazioni tecniche del modulo (è presentata solo per gli utenti aventi USLVL > 00)

* **Surf** :  visualizza tutte le funzioni di navigazione all'interno dei dati di competenza del modulo. La composizione delle voci di questo titolo si basa su tre elaborazioni : 
** La /COPY £G46 che costruisce le funzioni di navigazione grafica standard
** Le query riferite all'oggetto intestatario del modulo (si vedano /COPY £K01, £IQ1 e modulo B£EQRY)
** Le voci della MEAxx (xx è l'applicazione di riferimento del modulo) riempiendo il campo "Modulo Appartenenza" con il codice del modulo ed il campo "Surf" valorizzato ad "1", e lasciando il campo "No Modulo su Std" vuoto. Di seguito un esempio di actions sulle distinte : 
![B£MENU_043](http://localhost:3000/immagini/B£MENU_05/BXMENU_043.png)
* **Actions** :  sono le funzioni applicative peculiari del modulo. Queste sono reperite all'interno della voci della MEAxx (dove xx è l'applicazione di riferimento del modulo) in cui il campo "No Modulo su Std" è stato lasciato vuoto, sul campo "Modulo Appartenenza" è stato riportato il codice del modulo e il campo "Surf" è stato lasciato vuoto. In questa sezione ci sono le seguenti voci standard : 
** Tabelle, che contiene le tabelle utilizzate nel modulo (settori, campi di un settore, singoli elementi), divise in tabelle del modulo e tabelle dell'applicazione, e organizzate per importanza e per appartenenza al modulo. L'impostazione di questi oggetti va eseguita negli script O_XX di SCP_SET, dove XX è la sigla dell'applicazione.
** Funzioni applicative (USLV>00) per simulare funzioni (UP FUN richiamato con la sigla dell'applicazione) (solo per il modulo base)
** Funzioni sugli archivi (USLV>00) per eseguire azioni specifuche sugli archivi. NB :  questa opzione è "libera", non riceve l'applicazione per filtrare gli archivi (solo per il modulo base).
** Stampa informazioni generali (USLV>00) per ottenere un report tecnico degli oggetti relativi all'applicazione (solo per il modulo base).
** Modello dinamico :  per navigare tra le relazioni tabellari impostate per l'applicazione (attenzione :  questa è la versione originale, a carattere, del modello dinamico, legata unicamente all'applicazione.) (solo per il modulo base).
** Lista api (USLV>00) che presenta le api definite nello script definito in precedenza. Da questa lista è possibile richiamare la scheda della singola api, da cui accedere, tra l'altro, alla sua documentazione e al programma di test (solo per il modulo base).

* **Education** :  contiene le funzioni propedeutiche alla conoscenza ed alla comprensione del modulo
** Documentazione :  lancia la scheda della documentazione del moduo
** Formazione :  lancia la scheda da cui si accede a tutti gli strumenti di aiuto, esterni alla documentazione (video, faq, corsi, ecc..)
** Modello dinamico :  lancia la scheda di navigazione delle relazioni tabellari impostate per questo modulo.

* **Properties** :  presenta tutte le funzioni per gestire i dati "tecnici" collegati al modulo (è presentata solo per gli utenti aventi USLVL > 00).

* **Cambio ddddd** :  se il modulo è parametrato, e ddddd è la descrizione del parametro (ad esempio tipo documento V5, tipo distinta) attualmente attivo, viene presentata questa voce per cambiare il parametro attivo per le funzioni di questo modulo. Questa voce è presentata solo se, per il modulo, c'è più di un parametro possibile. NB :  in presenza di modulo "naturato" (ad esempio BRRISOM :  risorse di natura macchine), la scelta dei parametri è limitata a quelli che hanno la stessa natura del modulo.

* **Go** :  riporta delle funzioni di navigazione che per permettono di spostarsi su oggetti collegati al modulo.
** Hypermenu applicazione :  lancia la scheda dell'applicazione
** Classe Moduli Applicazioni :  presenta la scheda dell'oggetto di classe TAB£AMO e di istanza nome del membro (Uslv>00)
** Settore tabella moduli applicazioni (Uslv>00) lancia la lista degli elementi del sottosettore di tabella B£AMO (tutti i moduli presenti dell'applicazione a cui appartiene il modulo)
** In caso si modulo parametrato, viene lanciata ???? (Uslv>00).

* **Fly** :  se è impostato che un surf è agganciato (in fly) dall'oggetto modulo, verrà riportato in questa sezione. Un esempio è l'esplorazione dei parametri che è lanciata da tutti i moduli BR (oggetti TAB£AMO BRxxxx).

* **Setup** :  permette di lanciare le funzioni per impostare/configurare il modulo (è presentata solo per gli utenti aventi USLVL > 00).
** Gestione documentazione :  permette di modificare la documentazione del modulo
** Oggetti del modulo, che presenta gli oggetti (tabelle, archivi, api) utilizzati nel modulo, definiti nello script O_XX, illustrato in precedenza.

* **Help menù** :  se presente, è una voce che permette di accedere a un documento che spiega, voce per voce, tutte le varie azioni che compongono il menù nel quale questa voce si trova. Il documento che viene visualizzato è il documento completo, ma in realtà ogni singolo titolo di questo documento può essere consultato separatamente premendo F1 in corrispondenza della voce di menù di cui si vuole conoscere il significato e l'utilità.

* **Menu mgmt** (uslv>00) Permette di gestire lo script relativo al menu del modulo (NB :  viene presentato lo script utilizzato, al livello di risalita trovato).

Per approfondimenti tecnici vedere anche
 :  : DEC T(V2) P(LOCOS) K(A12) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£IQ1) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£J11) L(1)
 :  : DEC T(TA) P(B£AMO) K(B£EQRY) L(1)

### Altri Oggetti

![B£MENU_044](http://localhost:3000/immagini/B£MENU_05/BXMENU_044.png)* **Dashboard** :   è la funzione che viene richiamata ogni volta che viene aperta la schermata dell'oggetto e di norma presenta una schermata dove sono messe in evidenza le caratteristiche peculiari dell'oggetto. Il nome della scheda da richiamare viene ritornato dalla funzione £J11. La scheda standard può essere sovrascrivibile attraverso la configurazione dell'elemento della tabella  B§K£O con codice corrispondente alla classe.  Attraverso la stessa tabella è inoltre possibile decidere di disattivare l'immediata esecuzione del dashboard all'accesso della scheda.

* **Azioni Rapide** :  non hanno un loro titolo in quanto, nella scheda sono riportate al di sotto del titolo dashboard (si veda la figura relativa), mentre nel popup sono le prime azioni specifiche dell'oggetto. Sono le azioni che l'utente richiama più frequentemente. Possono essere reperite nei seguenti modi : 
** qualora siano state previste delle voci dello Script SCP_MNU della classe, con l'indicazione dell'attributo "PoR Posizione di Riferimento" valorizzata a "K" .
** qualora siano state compilate degli elementi della tabella B£Jxx corrispondenti alla definizione del flusso "A-" della classe con il campo "Sezione menù" valorizzato ad "R".

* **Info** :  lancia una funzione che presenta tutte le informazioni caratteristiche dell'oggetto (oav, parametri,  note, documenti). E' una funzione standard presente in tutti gli oggetti ed è la stessa funzione richiamata anche nel menu del modulo (con la differenza che, per l'oggetto, non vi è la limitazione all'Uslv>00).

* **Focus** :  lancia una funzione che presenta un'insieme di informazioni specifiche dell'oggetto (diverse da oggetto a oggetto). E' presente soltanto negli oggetti più importanti.

* **Fly** :  contiene le funzioni di navigazione sui dati del gestionale, eseguibili a partire dall'istanza. Permette di passare ad una lista dell'oggetto di arrivo, a partire dall'oggetto di questa scheda. Ad esempio, tra i fly dell'articolo c'è quello verso i movimenti di magazzino, che presenta la lista dei movimenti di magazzino relativi all'articolo della scheda. La composizione delle voci si basa su tre elaborazioni : 
** La /COPY £G46 che costruisce le funzioni di navigazione grafica standard
** Le voci dello script SCP_MNU corrispondenti alla classe oggetto, per cui è stato compilato l'attributo "Fly" con il modulo di riferimento
** Le voci della tabella B£Jxx richiamate dalla struttura dei flussi "A-" della classe con il campo "Sezione menù" valorizzato ad "F"

* **Surf** :  contiene le funzioni di navigazione sui dati dell'archivio di appartenenza dell'oggetto, basate sulle relazioni implicite dell'istanza (es. di un articolo vedo tutti gli articoli dello stesso tipo). Sono attivi solo i surf "contestuali" :  ad esempio, a partire da un movimento di magazzino, la presentazione della voce "surf per commessa" è condizionata dalla presenza della commessa stessa nel movimento della scheda. La composizione delle voci si basa su tre elaborazioni : 
** La /COPY £G46 che costruisce le funzioni di navigazione grafica standard
** Le voci dello script SCP_MNU corrispondenti alla classe oggetto, per cui è stato compilato l'attributo "Surf" con il modulo di riferimento
** Le voci della tabella B£Jxx richiamate dalla struttura dei flussi "A-" della classe con il campo "Sezione menù" valorizzato ad "S"

* **Specifiche** :  contiene le funzioni peculiari dell'oggetto. La composizione delle voci si basa su tre elaborazioni : 
** Le voci dello script SCP_MNU corrispondenti alla classe oggetto, che non sono state classificate come azioni rapide, fly o surf.
** Le voci della tabella B£Jxx richiamate dalla struttura dei flussi "A-" della classe con il campo "Sezione menù" vuoto
** La scheda con codice Classe_X, se previsto dall'elemento della tabella B§K£O con codice corrispondente alla classe
** Le voci recuperate dall'elaborazione del programma JAPOP_ALT (azioni standard)
** Le voci recuperate dall'elaborazione dei pgm B£FUN0_xx qualora per queste sia stata prevista la forzatura di utilizzo in LoocUP (azioni standard)

* **Gestione** :  contiene le funzioni di gestione dell'istanza stessa (tipicamente inserimento, modifica, copia, cancellazione, interrogazione). L'elaborazione è basata su quanto definito nel programma B£GES0, nello script B£GES0 in SCP_SET e, in risalita, dalla gestione del workflow, se attiva per l'oggetto (si veda comunque la /COPY £G99)

* **Go** :  contiene le funzioni di navigazione verso altri oggetti in relazione con l'oggetto stesso.
** Scelta altro oggetto :  lancia la scheda di un'altra istanza dello stesso oggetto.
** Passa alla scheda dell'applicazione
** Passa alla scheda del modulo
** Passa alla scheda della classe dell'oggetto :  classe OG, istanza tipo + parametro (Uslv 01)

* **Properties** :  presenta tutti i dati i collegati all'oggetto. E' la stessa funzione presente nel menu del modulo.

* **Education** :  presenta le informazioni relative alla comprensione dell'oggetto E' la stessa funzione presente nel menu del modulo.

Per approfondimenti tecnici vedere anche
 :  : DEC T(V2) P(LOCOS) K(A12)  L(1)
 :  : DEC T(MB) P(QILEGEN) K(£J11)  L(1)
 :  : DEC T(MB) P(QILEGEN) K(£G99)  L(1)
 :  : DEC T(MB) P(QILEGEN) K(£IMP)  L(1)

# Personalizzazione dei menù oggetto

I menù oggetto possono essere personalizzati attraverso i seguenti strumenti : 
* l'aggiunta di voci di menù personali
* l'inibizione di voci standard attraverso le autorizzazioni

## Aggiunta voci

Per l'aggiunta di voci personali va fatta nuovamente la distinzione fra moduli ed altri oggetti : 
* Per i MODULI, le voci personali vanno aggiunti con la modalità prevista per le voci dei menù di accesso (si veda il capitolo specifico della documentazione dei menù di accesso)
* Per gli ALTRI OGGETTI, l'aggiunta di nuove voci si basa sulla compilazione struttura dei flussi "A- Azioni popup utente" dell'oggetto, e dalla compilazione dell'elemento della tabella B§K£O intestato alla classe oggetto (per forzare la presenza di una scheda sostitutiva/aggiuntiva).

## Autorizzazione voci

Le voci possono essere omesse attraverso l'utilizzo delle autorizzazioni. Le autorizzazioni delle voci di menù, presentano una struttura variegata, dato che su di esse convergono più logiche di autorizzazione (tutte con la consueta risalita utente / gruppo utenti /**).

* La forma di autorizzazione più semplice è __l'autorizzazione sulla "voce" di menù__. Questa forma di autorizzazione si appoggia alla classe MNU e permette di autorizzare/disautorizzare la singola voce di menù. Rispetto ad essa è importante sottolineare questi aspetti : 
** La funzione della classe MNU è così composta :  ME;parametrovocemenù;vocemenù. Il parametro della voce può essere identificato attraverso l'oggetto MP (corrispondente alla /COPY £IMP), mentre la voce attraverso l'oggetto ME (corrispondente alla /COPY £IME). Nota; non è strettamente necessario conoscere tali informazioni perchè sono disponibili funzionalità che facilitano l'accesso e la gestione delle autorizzazioni.
** E' prevista una funzione in particolare così composta :  ME;parametrovocemenù;**, attraverso cui è possibile disattivare di default tutte le voci del menù, ad eccezione di quelle esplicitamente autorizzate. Relativamente a questo aspetto è importante notare che se la voce inibita è un titolo, automaticamente vengono omesse tutte le voci che stanno al di sotto di essa sia che esse risultino o meno autorizzate
** All'interno del menù del modo esistono alcune voci che non sono autorizzabili tramite la classe menù (e per le quali le azioni di gestione dell'autorizzazione sono appositamente inibite e/o deviate). Queste voci sono : 
*** Le azioni sotto il titolo "Gestione", che vanno specificamente gestite tramite la classe prevista per la classe (si veda la scheda di classe). Quanto detto è valido nel caso in cui le voci non siano gestite tramite il workflow; in alternativa le voci sono totalmente dipendenti dalla logica prevista dal workflow.
*** Le azioni aggiunte tramite la struttura della B£H "A-Azioni popup utente" :  per queste continua a sussistere la storica modalità di autorizzazione (si veda quanto previsto dalla documentazione delle tabelle B£H/B£J).

* Al di sopra di questo livello si pone __l'autorizzazione sull'oggetto e/o sulla classe oggetto. La classe interessata per tale livello è l'OGG.MAS (per la quale la funzione viene così composta :  OG;;codiceclasse quando si vuole autorizzare la classe o tipooggetto;parametroclasse;codiceistanza quando si vuole autorizzare l'istanza). Si veda, per maggiori dettagli la documentazione specifica delle autorizzazioni per oggetto.

* La sopraccitata forma di autorizzazione ha un impatto esclusivamente tecnico, in relazione alla singola voce di menù. Le voci dei menù di accesso (quelli standard, e quelli personali che sono stati realizzati con una struttura di applicazioni e menu), assumono però anche un significato applicativo :  ad esse infatti corrispondono oggetti quali applicazioni e modulo, il cui impiego ha impatto in vari punti del gestionale. Per tale motivo, se si intende disattivare un'intera applicazione o un intero modulo, si consiglia l'utilizzo dell'autorizzazione a questo livello. La classe interessata per tale livello è l'OGG.MAS (dove la funzione viene così composta :  TA;B£A;xx o TA;B£AMO;xxxxxx). In queste autorizzazione viene utilizzata la relazione gerarchica che sussiste fra i moduli e l'applicazione :  se viene disautorizzata l'applicazione vengono automaticamente omessi tutti i moduli che fanno ad essa riferimento. Un caso tipico all'interno dei menù, è quello delle azioni di "Fly" in cui ogni voce è riferita ad un modulo/applicazione.

* In aggiunta a queste autorizzazioni si pone __l'autorizzazione USRLVL__. E' una classe che va obbligatoriamente impostata a livello di utente/gruppo utente, al fine di individuarne il ruolo. Essa è fondamentale in quanto persistente in tutto il gestionale. Dal punto di vista dei menù di accesso, questa classe verrà utilizzata per effettuare il confronto fra il livello di un utente e le seguenti istanze : 
** Voce di menù, se previsto nella singola voce di menù della tabella MEAxx
** Modulo, se previsto nell'elemento della tabella B£AMO
** Applicazione, se previsto nell'elemento della tabella B£A
** La classe dell'oggetto, se fissata nella £K04. Per alcune classi tecniche, è impostato un Uslv>00 (all'interno di questa routine).
* E' importante notare che la classe utente USRLVL tiene conto delle gerarchie fra titoli e voci di menù ad essa appartententi ed applicazione/modulo.

* Infine rispetto ai titoli va fatta questa considerazione generale : 
** Se tutte le voci al di sotto di un titolo sono disautorizzate, automaticamente anche il titolo verrà omesso
** Se viene disautorizzato un titolo, anche tutte le voci che sono al di sotto di esso verranno omesse. Attenzione :  questa autorizzazione opera solo "localmente" :  le voci sottostanti non risentono dell'autorizzazione del menu se sono richiamate in modo diverso (Es. aggiungo una voce di menù sotto ad un certo titolo ad un preferito, se disattivo successivamente il titolo, nel menù tale voce non sarà visibile, ma sarà cmq visibile/richiamabile nei preferiti)

Queste relazioni vengono esplicitate/evidenziate nella scheda di gestione delle autorizzazione dei menù. Tale scheda può essere raggiungibile nei seguenti modi : 
* tramite le apposite voci predisposte nei menù dei moduli B£MENU e B£AUTO (sotto voce "autorizzazioni menù di accesso")
![B£MENU_045](http://localhost:3000/immagini/B£MENU_05/BXMENU_045.png)* attraverso la specifica voce di popup che si apre sulla voce di menù nell'interrogazione del menù stesso.
![B£MENU_046](http://localhost:3000/immagini/B£MENU_05/BXMENU_046.png)NOTA BENE :  per la natura "dinamica" delle voci di menù, nella scheda di gestione, qualora sia richiesto è sempre opportuno indicare l'istanza dell'oggetto di riferimento del menù (si veda anche il documento relativo agli oggetti MP/ME).

Il controllo delle autorizzazioni è demandato alle /COPY £AUO e £AUA.
 :  : DEC T(MB) P(QILEGEN) K(£AUO) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£AUA) L(1)

La gestione delle suddette autorizzazioni è richiamabile dai seguenti punti : 
* Menù del modulo B£MENU
* Menù del modulo B£AUTO
* Tasto destro su qualsiasi azione di menù
* Azione "Controllo Autorizzazioni" sotto il titolo "Properties" del menù/popup di un oggetto

Va infine fatta questa considerazione sul popup :  le voci del popup controlla le autorizzazioni per effetto di queste condizioni : 
* La voce è stata ricavata da un elaborazione dello script di menù LOA12 (se non esiste lo script specifico dell'oggetto viene elaborato lo script "O_")
* Alla funzione indicata nello script SCP_SCHPOP è stato attribuito un parametro virtuale "MNU" attraverso il quale viene imposto di controllare l'autorizzazione della corrispondente voce di menù
Voci che non hanno tali caratteristiche rimangono al di fuori del controllo delle autorizzazioni.

# Struttura Tecnica

Tecnicamente la struttura dei menù oggetto è abbastanza articolata. Si descrivono qui, solo per quel che riguarda la versione dell'ambiente grafico LoocUP, le principali caratteristiche.

## Metodo di Costruzione
Il metodo di costruzione del menù di oggetto è diverso a seconda se è richiamato nel menù a tendina o direttamente nella scheda dell'oggetto :  le voci sono le stesse, ma presentano alcune differenze peculiari della modalità grafica stessa e, a tutti gli effetti, l'elaborazione di costruzione è differente.
* Il menù a tendina, comunemente chiamato anche popup di oggetto, è costruito a partire dall'elaborazione del servizio JATRE_06C, basata a sua volta sugli script SCP_SCHPOP (di regola sul membro OG) e come caratteristiche peculiari presenta, per esempio il richiamo della scheda dell'oggetto (che nella scheda stessa non avrebbe senso). Tale funzionalità è presente per tutti gli oggetti.
* Il menù nella scheda oggetto si basa invece sull'elaborazione dell'hypermenù (cioè del servizio LOA12_SE), che è basata a sua volta sugli script SCP_MNU. Come caratteristiche peculiari presenta, ad esempio, il richiamo della sezione dashboard (che nel menù a tendina perde senso coincidendo di fatto con il richiamo della scheda oggetto stessa). E' importante notare che il menù nella scheda oggetto appare solo qualora ciò sia stato previsto per l'oggetto, cioè solo qualora sia stato previsto uno script SCP_MNU corrispondente alla classe oggetto.

Per approfondimenti tecnici vedere anche
 :  : DEC T(OJ) P(*FILE) K(SCP_SCHPOP) I(Script definizione menù a tendina/popup) L(1)
 :  : DEC T(OJ) P(*FILE) K(SCP_MNU) I(Script definizione menù a tendina/popup) L(1)
 :  : DEC T(V2) P(LOCOS) K(A12) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£J11) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£IMP) L(1)

Come si è potuto intuire dal contenuto di questo documento, gli elementi che compongono il menù di un oggetto, sia esso un modulo o un oggetto vero e proprio, possono provenire da fonti diverse (MEA, script di SCP_SET, SCP_MNU, etc...). Per capire la genesi di ciascuna voce e per conoscere il punto da cui questa voce proviene, è stata implementata l'informazione "Origine" all'interno del popup delle voci presenti nei vari hypermenù.
