# Concetti base Hypermenu

Di seguito vengono chiariti i principali concetti che sono oggetto dell''Hypermenu.
Nell'immagine si può vedere l'Hypermenu sulla parte sinistra della scheda.
![B£MENU_001](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_001.png)

## Dashboard
Il primo concetto che incontriamo dando un'occhiata all'Hypermenu è quello di DASHBOARD, il quale è una sorta di cruscotto.
![B£MENU_002](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_002.png)
Il dashboard è la prima scheda che viene visualizzata. In modo automatico il sistema mostra nella sezione di destra la parte relativa a questa funzione.
Nonostante il sistema mostri come prima cosa il dashboard, l'Hypermenu è dotato di una pratica caratteristica, quella di memorizzare l'ultima voce interrogata dall'utente. Quindi se nella parte destra come prima cosa vedrò sempre il dashboard (la cui voce verrà comunque evidenziata ma in modo meno evidente) nella parte sinistra, quella quindi del mio menu vedrò ben evidenziata l'ultima voce interrogata.
Questo per dare all'utente la possibilità di accedere velocemente all'ultima schermata vista.
![B£MENU_013](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_013.png)
Torniamo alla definizione di cruscotto, quest'ultimo permette di andare ad interrogare una scheda "base" relativa al modulo o l'oggetto che stò interrogando, che contenga le informazioni principali e più importanti.
Questa scheda può contenere diversi componenti :  la matrice, grafici, gauge, semafori, ecc.

Talvolta non viene aperto completamente il dashboard, ma per motivi di ottimizzazione, è stato scelto di aprirne solo la ricerca iniziale (in alto nella scheda di destra) per fare in modo di limitare i dati caricati.
![B£MENU_012](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_012.png)Per caricare il risultato del dashboard, l'utente deve scegliere i filtri e confermando (con l'invio) verrà mostrata la scheda. Oltre ai filtri iniziali è possibile anche impostare ulteriori filtri più dettagliati con l'F13.
Per la forma di visualizzazione di alcune matrici, sono stati previsti degli schemi standard.


## MySmeup
Questa funzionalità è presente sia sulle schede degli oggetti (es. ordini di produzione) che su quella dei moduli.
La voce MySmeup però non sempre è visibile, i casi in cui verrà visualizzata nell'Hypermenu sono : 
- quando esiste una scheda personalizzata per quell'oggetto o legata a quel modulo, e se si è deciso di agganciarla alla scheda standard.
- quando esistono delle azioni personalizzate legate al modulo o all'oggetto .

Ad esempio sull'ordine di produzione abbiamo una serie di azioni : 
![B£MENU_010](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_010.png)Quindi in sintesi la voce MySmeup permette di legare alla scheda standard (di oggetto o modulo) l'elenco di tutte quelle schede e azioni personalizzate create adhoc per una installazione custom.


## Actions
Le Actions permettono di fare attività di modifica o aggiunta di alcune delle informazioni legate all'oggetto o al modulo. Quindi la funzione "Actions" può riguardare : 
- la voce di gestione delle tabelle
![B£MENU_008](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_008.png)- il richiamo di programmi che vanno a modificare i dati (es. estrarre dati in archivi, stampa di lettere, gestione dettaglio, stampe generiche, riallineamento dati, ecc)
- il richiamo di programmi che permettono la consultazione di informazione relative all'oggetto o modulo.


## Surf
Il Surf può essere distinto in : 
- Surf del modulo
- Surf dell'oggetto
Il significato basilare di Surf è sostanzialmente quello di interrogazione a partire da un informazione di origine, passando poi alla navigazione/esplorazione di tutti gli attributi collegati ad essa, pur sempre mantendosi nel contesto di partenza, ossia all'interno dello stesso modulo.

### Surf del modulo
![B£MENU_003](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_003.png)Il Surf di un modulo quindi permette all'utente di entrare nel dettaglio di un particolare oggetto del modulo rimanendo nel contesto.
Ad esempio se mi trovassi sul modulo P5IMPE (impegni materiali), utilizzare il Surf significa utilizzare una delle interrogazioni che mi permettono di vedere l'informazione originaria del modulo, quindi gli impegni, tramite metodi di accesso che sono gli attributi degli impegni materiali stessi, quindi per esempio la commessa, la data impegno, l'articolo, l'ente, etc.). Quindi scegliendo un Surf per ente (un cliente specifico ad esempio), vedo tutti gli impegni del materiale impiegato per soddisfare le esigenze di quel cliente (quindi vedrò gli ordini di produzione che hanno creato questi impegni).

C'è una corrispondenza uno a uno tra modulo ed oggetto, quindi un modulo sostanzialmente si riferisce ad un oggetto specifico.
Ad esempio nel caso del modulo GMMOVI dei movimenti di magazzino, l'oggetto sul quale vado in esplorazione è il movimento stesso (la registrazione del movimento).
Con il Surf quindi potrò esplorare i movimenti secondo differenti chiavi, queste chiavi come detto precedentemente sono attributi dell'oggetto di partenza (il movimento).
Le esplorazioni sull'oggetto del modulo sono di due tipi : 
- riguardano un'altro oggetto collegato ad esso, e hanno dei filtri corrispondenti.
- riguardano una data.

Particolarità sui filtri : 
- potrebbero esserci dei filtri che cambiano a seconda dell'impostazione dell'ambiente (per esempio il PLANT sul modulo dei movimenti rimane nascosto se il magazzino di cui si sta parlando è mono-plant).
- i filtri relativi a date possono essere tranquillamente espressi con date dinamiche.

### Surf di un oggetto
![B£MENU_007](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_007.png)Il Surf sull'oggetto è inteso come la possibilità di effettuare interrogazioni su quell'oggetto nel contesto di partenza, passando dal dettaglio per attributi riferiti a quello oggetto.
Un esempio può essere sull'oggetto movimento di magazzino (l'informazione di origine), in questo caso posso usare il Surf sull'articolo di quel movimento :  ottenendo tutti i movimenti (contesto originale) dell'articolo.

Il Surf sull'oggeto è interrogabile tramite Hypermenu o anche cliccando sull'oggetto con il tasto destro, nel popup avrò le stesse funzionalità.
![B£MENU_017](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_017.png)
## Fly
FLY è una funzione che consente all'utente, a partire da un oggetto origine (come gli ordini di produzione per esempio), di navigare trasversalmente e quindi cambiare contesto, su altri oggetti collegati e dipendenti da quello di partenza (come i movimenti di magazzino collegati a quell'ordine di produzione dal quale sono partito).
![B£MENU_009](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_009.png)Oltre ad essere una voce dell'hypermenu, viene anche visto come azione sul popup dell'oggetto.
![B£MENU_018](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_018.png)Quindi se dalla scheda dell'ordine di produzione apro il popup sulla cella con il numero ordine vedrò le stesse voci viste nell'Hypermenu di questo oggetto (ordine di produzione).
Allo stesso tempo però dalla scheda dell'ordine di produzione posso vedere il FLY anche sul popup degli altri oggetti legati a questo contesto (es. l'articolo).
![B£MENU_011](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_011.png)
## Info
Il concetto di "Info" si affianca a quella che era la lista degli attributi di un oggetto, ovvero l'insieme delle informazioni, parametri, attributi, ecc collegati all'oggetto sul quale si sta lavorando.
![B£MENU_015](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_015.png)Tutti gli oggetti hanno questa funzione, che corrisponde sostanzialmente all'F10 - Lista campi.


## Focus
Il FOCUS non è una scheda che si può trovare su tutti gli oggetti e moduli. Questa è una sorta di "Info" più evoluta.
![B£MENU_005](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_005.png)
Questa scheda permette di visualizzare attributi, parametri e quant'altro legati all'oggetto, riclassificati e arricchiti da altre informazioni e strumenti (grafici, ecc).
Un esempio l'abbiamo sull'oggetto OR degli ordini di produzione : 
![B£MENU_022](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_022.png)

## Educations
In questa voce dell'Hypermenu vengono raggruppate 2 funzionalità : 
- l'accesso ai manuali di documentazione (operativa, tecnica, applicativa e glossario)
- l'accesso al modulo relativo alla formazione, dal quale è possibile accedere a video, skills, ecc.

Per quanto riguarda la formazione, si possono avere manuali di modulo : 
![B£MENU_021](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_021.png)Oppure legati all'oggetto : 
![B£MENU_004](http://localhost:3000/immagini/MBDOC_OPE-B£MENU_01/BXMENU_004.png)