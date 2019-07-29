# Obiettivi
Fornire le indicazioni per configurare correttamente la risoluzione delle ricerche nel proprio ambiente applicativo.

# Modalità di risoluzione
Le funzioni di ricerca possono essere svolte secondo due particolari tecniche : 
* Tramite funzioni client, per tutti gli oggetti la cui risoluzione è gestita dal client loocup
* Tramite funzioni server, per tutti gli oggetti la cui risoluzione è gestita dal server.

## Modalità Client
La modalità client è prerogativa del client stesso e non può essere in nessun modo modificata o deviata. Essa riguarda però solo una piccola parte delle classi smeup, nello specifico, interviene per quasi tutti quegli oggetti che non sono riconducibili ad un'entità server. Sono infatti essenzialmente identificatili dall'iniziale "J" della classe (es. J1PATHFILE o J1PATHDIR) con l'aggiunta delle classi D8 (data) e I1 (istante).
Per questi oggetti la funzione di risoluzione della ricerca è specifica in relazione alle peculiarità della classe.

![B£EQRY_07](http://localhost:3000/immagini/B£EQRY_A01/BXEQRY_07.png)![B£EQRY_08](http://localhost:3000/immagini/B£EQRY_A01/BXEQRY_08.png)
## Modalità Server
Riguarda quindi la stragrande maggioranza delle classi di smeup e viene gestita dal server.

Ad oggi esistono tre strutture di risoluzione di tale modalità di ricerca, tutte pilotate dalla variabile *SEAMODE dell'SCP_CLO, la quale può assumere alternativamente i seguenti valori : 
* **"SCH"** :  da scheda. E' la modalità standard attuale di risoluzione delle ricerche. Salvo considerazioni particolari questo è il valore che la variabile dovrebbe contenere per l'ambiente.
* **"ADVANCED"** :  da componente grafico QRY. E' stata la modalità utilizzata per i primi anni di esistenza del client loocup. E' ora sostituita dalla modalità SCH, salvo considerazioni particolari non dovrebbe quindi più essere attiva.
* **"5250"** :  da componente grafico di emulazione. Con questo valore la ricerca viene direzionata sulla struttura di ricerca di smeup in modalità 5250. Anche questa salvo considerazioni particolari non dovrebbe essere più attiva

Per verificare il valore della variabile nel proprio ambiente, basta quindi accedere alla scheda della succitata variabile.
 :  : DEC T(J1) P(VAR) K(*SEAMODE)

Per tutti i capitolo successivi ci si concentrerà esclusivamente sulla prima modalità.

NOTA BENE :  questa variabile ha effetto solo sulla funzione di ricerca principale e non sulle ricerche tramite combo-box.

## Le ricerche dalle schermate di emulazione
Quanto riportato sinora non è sufficiente per attivare le suddette ricerche anche sulle funzioni che vengono risolte tramite schermate di emulazione 5250 (riconoscibili dall'iconcina UP in blu riportata in alto a sinistra in questa tipologia di schermate).  Quest'ultime continuano ad essere risolte attraverso le logiche che erano state previste dai pgm di emulazione a meno che non venga esplicitamente richiesta la risoluzione del client.
Questa richiesta può avvenire in due modalità : 
* Attraverso la valorizzazione della variabile globale di SCP_CLO *EMUSEARCHTYPE, valorizzata ad EXT (il comportamento opposto corrisponde al valore INT)
* Attraverso l'indicazione esplicita delle singole classi oggetti per le quali si vuole attivare la modalità di ricerca client, nella configurazione dell'emulazione
Il fatto che sia possibile scegliere fra queste due modalità è molto importante, sulla base di queste considerazioni : 
* Quando viene attivata la ricerca client (esterna) è il client sulla base delle informazioni che reperisce dal formato video a determinare la classe di ogni campo ed a decidere sulla base di quest'unica informazione a determinare quale funzione di ricerca lanciare. Questo al minimo necessario che la classe del campo sia correttamente identificata.
* Quando invece la ricerca è svolta dal pgm di emulazione, la ricerca è determinata dalla logica del singolo pgm di emulazione e può quindi essere pilotata anche in funzione di logiche locali specifiche che il client non può prendere in considerazione di per suo.
In base a tali considerazioni l'attivazione globale delle ricerche client in emulazione, va ben ponderata. Volendo attivare questo tipo di ricerca sull'emulazione la scelta consigliata è quella di attivarla solo per quelle classi oggetti che in linea generale possono escludere logiche di ricerca particolari, attraverso la configurazione dell'emulatore.

Qualora si optasse, invece per l'attivazione globale, va comunque notificato che è possibile condizionare secondo proprie logiche la risoluzione grafica o meno delle ricerche dell'emulazione, attraverso l'implementazione dell'exit B£EQRY_SEU (di cui è viene reso disponibile un esempio). In questa exit vengono ricevute le informazioni relative al nome del file video, del formato video, del campo video e dell'oggettizzazione di tale campo ed a partire da esse forzare la risoluzione interna o l'integrazione di tali informazioni.

Per verificare il valore della variabile nel proprio ambiente, basta quindi accedere alla scheda della succitata variabile.
 :  : DEC T(J1) P(VAR) K(*EMUSEARCHTYPE)

Per verificare invece gli oggetti che prevedono la forzatura per classe dalla configurazione dell'emulatore, va : 
* Aperta una schermata di emulazione, premuto tasto destro sulla barra in alto
* Scelta la voce "Carica/Gestisci Configurazione"
* Scelta l'opzione "Modifica" per la configurazione per utente/ambiente interessata
* Scelto il tab "SearchOptions". Anche qui si fa riferimento al concetto di ricerca "Interna - INT" (cioè svolta dal pgm di emulazione) ed "Esterna - EXT" (cioè svolta dal client).

![B£EQRY_26](http://localhost:3000/immagini/B£EQRY_A01/BXEQRY_26.png)![B£EQRY_27](http://localhost:3000/immagini/B£EQRY_A01/BXEQRY_27.png)![B£EQRY_28](http://localhost:3000/immagini/B£EQRY_A01/BXEQRY_28.png)




