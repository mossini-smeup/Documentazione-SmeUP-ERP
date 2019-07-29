### UTILIZZO MEMORIZZAZIONI

In queste schede viene posta l'attenzione sull'utilizzo delle memorizzazioni delle risposte dell'utente su richieste di configurazione o query o parametri. In particolare si evidenzia che : 
* Tramite l'attributo UirNMe è possibile fare in modo ad ogni richiesta le risposte vengano sempre riazzerate
* E' disponibile la modalità grafica (attributo UirMGr) "E - Solo Richiesta". Tramite essa è possibile presentare in subsezione esclusivamente la richiesta configurazione o query o parametri.
* Tramite l'attributo UirVMe, sulle sole modalità grafiche per cui la sola richiesta parametri è in subsezione (cioè quando la modalità grafica è D o E) è possibile presentare nella stessa subsezione l'elenco delle memorizzazioni video aventi medesimo contesto e struttura della richiesta in essere.
** Anche se non è esemplificato, tramite l'attributo UirCtx è possibile estendere la chiave contesto della memorizzazione. Se tale estensione è opzionale nelle configurazioni e nelle query è obbligatoria nelle richieste parametri. Ad esso va posta particolare attenzione al fine di evitare  conflitti per la sovrapposizione di differenti richieste parametri.

* Solo per le richiesta configurazione e nella richiesta query (e non per la richiesta parametri) va inoltre notato che : 
** Tramite l'attributo UirMAm è possibile far si che la memorizzazione non sia per utente, ma per ambiente (viene scritta con utente **).

### NOTE OPERATIVE

* Le chiavi di memorizzazione sono le seguenti : 
** Per la richiesta configurazione sono :  la struttura corrispondente al configuratore + "UIR\" come contesto. Al contesto è come sopracitato, possibile attaccare un estensione qual'ora sia passato il parametro UirCtx.
** Per la richiesta query sono :  la struttura STR.MDV + "Q1\TipoOggettoParametroOggetto\CodiceQuery\" come contesto. Al contesto è come sopracitato, possibile attaccare un estensione qual'ora sia passato il parametro UirCtx.
** Per la richiesta parametri sono :  la struttura STR.MDV + "UIR\" come contesto. Al contesto è come sopracitato è necessario attaccare un estensione tramite il parametro UirCtx.

* Nella modalità di sola richiesta, va notato che : 
** La memorizzazione viene effettuata, in mancanza di errori nelle risposte per effetto del solo tasto invio
** Nella richiesta configurazioni e query alla conferma verrà emesso un messaggio video di conferma dell'avvenuta memorizzazione

* Anche se non è esemplificato in modo specifico, nella richiesta configurazione e nella richiesta query, in qualsiasi modalità grafica tramite il tasto F14 è possibile accedere alla scheda di gestione delle memorizzazioni, dalla quale è possibile, riprendere/modificare/cancellare/creare le memorizzazioni della struttura/contesto associate alla configurazione/query

* Quando si scegliere di evidenziare nella stessa subsezione la scheda delle memorizzazioni video è importante notare che tramite il piccolo bottone grigio posto all'estrema sinistra dell'elenco è possibile riprendere le risposte di una particolare memorizzazione inputandole alla richiesta di configurazione o query in essere.

