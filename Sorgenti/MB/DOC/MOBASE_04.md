# Generalità
A livello di server, sul Smeup, a partire dalla 4.1 sono disponibili una serie di funzionalità insite nell'applicazione standard, atte a semplificare e proporre funzionalità per lo sviluppo dell'applicazione mobile.

# Menù Iniziale "00"
Nella smedev viene fornito un sottosettore menù MEA di accesso "00", in essono sono contenute delle voci specifiche per il mobile.
Impostare come accesso per gli utenti il suddetto menù, attraverso il comando UP UT5, senza far null'altro si avranno a disposizione una serie di funzioni di navigazione ed interrogazione standard.

Le succitate funzionalità si basano sulla medesima struttura di navigazione prevista per il client loocup per modulo/oggetto. Semplicemente vengono presentate le sole voci che è previsto vengano attivate per il particolare device.

# Il menù iniziale
Se si decide di mantenere il menù 00 come menù iniziale, sarà possibile indicare come per tutti gli altri menù MEA azioni proprie, purchè si ponga attenzione a valorizzare i campi per l'attivazione dei device Phone e Tablet.

Pur mantenendo invariata la variabile *SMobile, che identifica la funzione di accesso è cmq possibile specificare nell'UP UT5 un menù di accesso differente. Valgono le medesime considerazioni del menù precedente, per le quali è importante flaggare i campi dei device.

Rimane la possibilità di poter sfruttare una funzione iniziale completamente differente, impostandola variabile di SCP_CLO *SMobile in modo differente.

# La funzione scheda "oggetto"
Sul device mobile, la funzione della scheda dell'oggetto viene automaticamente deviata (attraverso la logica prevista dalla /COPY £J11) sulla sottoscheda MOB dello script di scheda LOA12.

In essa sono previste due sezioni : 
* Nella prima possono essere elencate una serie di informazioni peculiari dell'oggetto. Tali informazioni possono essere predisposte nello standard (attraverso la definizione di uno schema PRW/P) oppure sovrascritte dal cliente attraverso le memorizzazioni imputabili dalla scheda della classe (Es. scheda OG//CNCLI, Setup, Scelta Schemi di default, Anteprima Phone).
* Nella seconda scheda vengono invece elencante le funzioni applicabili all'oggetto. Queste possono : 
** Essere proposte dallo standard :  sono fisse l'info e le note (se previste dall'oggetto), ma esse si possono affiancare altre funzioni (se. su clienti/fornitori abbiamo, chiamate telefoniche, situazioni incassi/pagammenti ecc.)
** Essere aggiunte attraverso la struttura B£H/B£J "A-". Come per la MEA anche sulla B£J è importante che vengano specificati in modo opportuno i campi relativi all'attivazione sui device.

Per quel che riguarda l'info inoltre va specificato che oltre all'interrogazioni delle differenti categorie di attributi, sarà possibile interrogare informazioni dell'istanza secondo schemi specifici (standard o personali). Per far questo è necessario che nella definizione dello schema venga attivata la volontà di utilizzare lo schema, non solo in lista, ma anche a livello di istanza.

# Gli schemi
Come anticipato al punto precedente gli schemi possono essere, dal punto di vista del mobile essere utilizzati sia in lista che sull'istanza.

A livello di standard possono inoltre essere predisposti degli schemi specifici di default (DFT/P) che come per gli schemi di anteprima possono essere sovrascritti con specifici del cliente attraverso le impostazioni presenti sulla scheda della classe (si riveda il punto precedente relativo allo schema di anteprima).

Di default gli schemi sono attivi per tutti i device, ma tramite gli attributi di definizione è possibile disattivarli per singolo device.

# Le Query
Le questi costituiscono uno dei principali modi di attivare interrogazioni personali sul device mobile.
Per farlo è sufficiente impostare la struttura, come per il client loocup, preoccupandosi solo di indicare, tramite gli specifici attributi per quali device la query vuole essere utilizzata (di default una query è attiva sul client loocup e disattiva sui device mobile).

Se la query è relativa ad un modulo su cui è attiva la navigazione su device mobile, automaticamente la query apparirà fra le possibili navigazioni.
In alternativa o viceversa la query potrà essere richiamata in una propria scheda sfruttando i TAG G.SUB.UQR/G.SET.UQR (si veda modulo LOSUIR).

# Le richiesta parametri
Per le richieste parametri è possibile sfruttare sia il costruttore A08 che le i TAG G.SUB.UCF/G.SET.UCF (quest'ultimi pur con alcune limitazioni es. non si possono usare le variabili $IN o decidere di non passare le risposte nell'INPUT), presentano una serie di funzionalità idonee a sfruttare la richiesta su più device (si veda modulo LOSUIR).

# Report preparati
I report preparati, costituiscono nel mobile un'importante fonte che permette di riepilogare in brevi tempi (fondamentali per l'applicazione mobile), importanti numeri di sintesi.
Nella DEV viene inoltre distribuita una serie di schede grafiche idonee alla navigazione fra questi dati.

# Identificazione del Device
L'indentificazione del device può essere identificata nei seguenti modi : 
* Negli script, attraverso la variabile di ambiente _&_AM.DV
* Nei programmi, attraverso il richiamo della /COPY £J18
Entrambe, funzionano anche su altri device (es. client loocup), e forniscono come risultato un'istanza dell'oggeto sme.up V2B£CDV.

