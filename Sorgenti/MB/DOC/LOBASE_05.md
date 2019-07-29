# Connessioni Sme.Up

## Riferimenti

Questo documento andrà a descrivere la nuova funzione "Connessioni Sme.Up" aggiunta al modulo base di Looc.Up.

 T(I riferimenti tecnici all'interno di Sme.Up sono i seguenti : )
- Modulo di appartenenza :  **LOBASE**
- Codice funzione :  **LOBASE_05**



## A cosa serve

Il gestore delle connessioni di Sme.Up ha lo scopo di fornire all'utente finale del client grafico  Looc.Up un sistema grafico per la selezione e gestione delle connessioni.
L'idea di base è quella di replicare all'interno di Looc.Up un sistema simile a quello dell'Operation Navigator for iSeries di IBM.

Il risultato voluto è che alla partenza di Looc.Up venga visualizzato un modulo simile al seguente : 

![LOBASE_108](http://localhost:3000/immagini/LOBASE_05/LOBASE_108.png)

La connessione è definita come l'insieme dei parametri necessari per l'avvio di Looc.Up :  comprende principalmente informazioni sul sistema a cui connettersi, l'utente da utilizzare, la password di autenticazione e l'ambiente operativo da selezionare. Oltre a queste informazioni, necessarie per stabilire un collegamento, ci sono tutta una serie di parametri aggiuntivi di tipo facoltativo che attivano particolari funzionalità o modalità di esecuzione del programma.
Fino ad oggi l'unico modo per fornire a Looc.Up le informazioni necessarie al collegamento era quello di passare queste informazioni a linea di comando in fase di chiamata al programma. Oppure non passare alcuna informazione e compilare ogni volta la finestra di connessione visualizzata alla partenza del programma.


 T(Le connessioni vengono visualizzate secondo la seguente logica : )
- **Le connessioni sono associate agli utenti Windows, non agli utenti del sistema AS400.** Quindi le connessioni disponibili su una certa macchina sono identificate dal codice utente WIndows utilizzato per il login alla macchina stessa.
- Ogni singola connessione è identificata da un oggetto che contiene tutte le informazioni necessarie alla creazione del collegamento
- Le connessioni possono essere raggruppate in gruppi secondo una logica di aggregazione scelta a piacere dall'utente o dall'amministratore del sistema
- La finestra iniziale di visualizzazione consente la sola visualizzazione e selezione delle connessioni.


L'interfaccia grafica è semplice e lineare ed è organizzata in cinque parti principali.


xxFIG M(LOBASE) P(LOBASE_109) R(40) C(Struttura della finestra di selezione delle connessioni)

 T(La finestra di connessione è divisa nelle seguenti aree : )
- Gruppi di connessioni condivise
- Gruppi di connessioni personali
- Connessioni disponibili nel gruppo selezionato
- Gestione gruppi e connessioni
- Comandi vari (avvio Looc.Up in modo classico, chiusura ecc ecc)


## Avvio di Looc.Up con la finestra di connessione

Dopo l'installazione di Looc.Up sul PC viene creato sul desktop un link che punta all'eseguibile **Smeupgo.exe** presente nella cartella
di installazione Looc.Up.

 T(L'avvio di Looc.Up può avvenire in due modalità diverse : )
- Invocazione dell'eseguibile Loocup.exe con parametri passati a linea di comando  --> Looc.Up si avvia e si collega direttamente al server passato senza mostrare nulla
- Invocazione dell'eseguibile Loocup.exe senza parametri passati a linea di comando --> Viene mostrata la finestra di selezione delle connessioni


Nel primo caso Looc.Up parte attivando direttamente la connessione identificata dai parametri passati a linea di comando, senza mostrare nulla.

Nel secondo caso invece (chiamata senza alcun parametro) Looc.Up si avvia mostrando la finestra graficadi selezione delle connessioni. Ovviamente, essendo la prima volta che Looc.Up viene avviato dopo la sua installazione, viene per forza di cose mostrata una finestra di connessione vuota.


![LOBASE_110](http://localhost:3000/immagini/LOBASE_05/LOBASE_110.png)

In questa condizione, l'unica operazione possibile da parte dell'utente è quella di creare delle nuove connessioni e popolare la finestra. Questo nell'ipotesi che l'amministratore di sistema abbia previsto la possibilità per l'utente di gestire in prima persona le proprie connessioni. In caso contrario sarà l'amministratore stesso ad eseguire le operazioni di creazione delle connessioni dopo la prima installazione di Looc.Up e l'utente finale si ritroverà con un pannello di connessione già popolato con le connessioni a cui è autorizzato.

### Dove vengono salvate le connessioni

Le connessioni personali vengono cercate e salvate nell'ordine, in : 

- Cartella LOOCUP_CON allo stesso livello della cartella di Loocup (per retro compatibilità)
- Cartella LOOCUP_CON interna alla cartella di Loocup (per retro compatibilità)
- Cartella %appdata%/SmeupGo (default)
- Cartella cartella scritta nel file XML di configurazione

Le connessioni di gruppo vengono cercate e salvate in : 

- Cartella cartella scritta nel file XML di configurazione

### Il file di configurazione

Smeup GO prevede un file di configurazione.
E' possibile gestirlo in Funzioni Avanzate -> Gestione Configurazione

Il file viene cercato in
- Cartella di installazione di Looc.UP
- %appdata%/SmeupGo

## Connessioni condivise

Si è deciso che la gestione delle connessioni condivise non è possibile all'interno del pannello di selezione ma viene gestita all'interno di una scheda specifica di Looc.Up.

 T(Questa scelta, che a prima vista può sembrare scomoda, porta con se una serie di vantaggi : )
- Si centralizza in un sol punto la gestione delle connessioni per tutti gli utenti
- All'interno di una scheda è possibile trattare i gruppi e le connessioni come oggetti Sme.Up, con tutti i vantaggi del caso
- La scheda facilita la gestione delle autorizzazioni


Per accedere alla scheda di gestione delle connessioni è sufficiente entrare in Looc.Up. Non essendo disponibili connessioni, la prima volta è necessario avviare Looc.Up selezionando la voce **"Avvia Looc.Up"** presente nella finestra di connessione in basso a sinistra.
Con questa azione si richiede un avvio Looc.Up con richiesta di immissione dei parametri di connessione in fase di avvio, allo scopo di entrare nel programma e poter accedere alla scheda di gestione delle connessioni.

### La scheda di gestione

Una volta avviata una istanza di Looc.Up è possibile entrare nella scheda di gestione delle connessioni selezionando una delle seguenti opzioni (a seconda
dell'aggiornamento di Sme.Up) : 

 T(Prima opzione : )
- Voce di menù "MyLoocup"
- Selezionare la sottovoce "Gestire il sistema"
- Selezionare il tab "Connessioni"


 T(Seconda opzione : )
- Voce di menù "MyLoocup"
- Selezionare la sottovoce "Gestire il sistema"
- Selezionare la voce "Consultazioni" e poi "Configurazione generale" nel menù opzioni
- Nel pannello che viene visualizzato a destra, selezionare la voce "Gestione connessioni"




Verrà mostrata la seguente scheda : 

![LOBASE_111](http://localhost:3000/immagini/LOBASE_05/LOBASE_111.png)
Per maggiore chiarezza, la scheda mostrata contiene già degli elementi definiti ed è relativa al pannello di connessione visualizzato come primo esempio in questo documento.

Come si nota dalle evidenziazioni grafiche, la scheda è suddivisa in 4 sezioni disposte orizzontalmente.

 T(Le sezioni sono le seguenti : )
- (rosso) Sezione per la gestione dell'utente
- (blu) Sezione per la gestione dei gruppi di connessioni
- (verde) Sezione per la gestione delle connessioni contenute in un gruppo
- (giallo) Sezione per la gestione delle immagini


Da notare che ognuna delle sezioni è a sua volta suddivisa in due parti, in senso verticale. Nella parte alta c'è una sezione di visualizzazione e selezione degli elementi, nella parte bassa c'è una sezione contenente le azioni disponibili sull'oggetto selezionato.

 T(La struttura della scheda di gestione delle connessioni suggerisce direttamente la logica con cui le connessioni sono trattate)
- Le connessioni sono create per utente.
- Ogni utente può creare dei gruppi entro i quali catalogare le connessioni. Il gruppo può essere visto come una cartella contenente più connessioni.
- All'interno di un gruppo si creano le connessioni. Se nessun gruppo viene definito si utilizza il gruppo preimpostato "Predefiniti"
- Ai gruppi e alle connessioni possono essere associate delle immagini specifiche



Andremo ora a vedere come si creano delle connessioni eseguendo un esempio passo per passo


### Creazione di un utente (sezione 1)

Il primo passo per la creazione delle connessioni è la selezione dell'utente per il quale si stanno definendo le connessioni stesse.
Alla prima partenza di Looc.Up viene mostrata una sezione utente di questo tipo : 

![LOBASE_112](http://localhost:3000/immagini/LOBASE_05/LOBASE_112.png)
Si nota che per default il sistema crea e propone un utente con lo stesso nome dell'utente del sistema Windows che ospita il client Looc.Up in esecuzione.
L'ipotesi sottointesa è che quando un utente avvia un Looc.Up su un certo PC, sul quale è connesso con un accredito Windows, voglia creare delle connessioni specifiche per quel contesto operativo. Quindi è logico pensare che voglia creare delle connessioni associate all'utente di sistema.

**NOTA BENE :  gli utenti gestiti nella scheda di setup delle connessioni sono sempre e soli gli utenti WIndows. Quindi se si vuole creare delle connessioni per uno specifico utente è necessario utilizzate il codice  con cui quell'utente è conosciuto nella rete Windows. Le connessioni non sono mai associate all'utente AS400.

 T(Quindi a questo livello l'utente può fare tre cose : )
- Selezionare il proprio utente Windows sotto il tab "Utente" per modificare le proprie connessioni
- Selezionare un utente diverso sotto il tab "Tutti gli utenti" per modificare le connessioni di un altro utente (se autorizzato)
- Selezionare il tab "Gruppi Smeup" e creare delle connessioni condivisibili tra più utenti (se autorizzato)


Per ora non analizziamo il tab identificato con "Gruppi Smeup", il cui scopo è quello di creare e gestire connessioni condivise. Questo punto verrà ripreso e spiegato a fondo nellìultima parte di questo documento.

### Creazione di un gruppo (sezione 2)

Una volta selezionato un utente, è possibile creare un nuovo gruppo operando all'interno della sezione 2. All'inizio viene creato in automatico un gruppo denominato **"Predefinito"** che può essere utilizzato così com'è se non si ha intenzione di creare dei gruppi specifici per l'utente. In caso contrario è possibile ridenominare questo gruppo con un nome a propria scelta ed eventualmente aggiungere nuovi gruppi.
Tutte le operazioni che possono essere effettuate sui gruppi sono nella parte inferiore della sezione.

![LOBASE_113](http://localhost:3000/immagini/LOBASE_05/LOBASE_113.png)
Nella parte inferiore della sezione è anche mostrata l'icona associata al gruppo selezionato. L'icona puà essere modificata andando nella sezione 4 della scheda di gestione, e selezionando una immagine tra quelle proposte che potrà essere associata al gruppo selezionato utilizzando l'apposito bottore **"Associa immagine al gruppo..."**.

### Creazione di una nuova connessione (sezione 3)

Selezionato un utente e un gruppo, è possibile definire una nuova connessione utilizzando i comandi presenti nella sezione 3 della scheda di gestione. Inizialmente non esiste alcuna connessione predefinita pertanto la prima cosa da fare è creare una nuova connessione selezionando l'azione **"Crea nuova connessione"**.

Una volta creata una nuova connessione, assegnandole un nome univoco, è possibile andare a configurare i parametri della connessione stessa selezionando la voce **"Modifica connessione"**.

Viene mostrata una finestra di input di questo tipo : 

![LOBASE_114](http://localhost:3000/immagini/LOBASE_05/LOBASE_114.png)
Questa finestra consente di specificare tutti i parametri della connessione che si sta creando.

 T(I parametri principali da immettere sono i seguenti : )
- L'indirizzo del sistema AS400 a cui ci si deve connettere
- L'utente di connessione
- La password
- L'ambiente operativo


In alternatica all'inserimento dell'utente e password è possibile attivare l'opzione Single Sign On, sempre che tale funzionalità sia stata abilitata sul sistema in oggetto.

La finestra di input consente di definire anche tutti i parametri opzionali previsti per Looc.Up. Questi parametri sono organizzati nei  tab successivi a quello principale che li raccolgono in gruppi tematici.

Come per i gruppi, anche per alla connessione è possibile associare un'immagine specifica che aiuti l'utente finale ad individuare agevolmente il tipo e la natura della connessione. Ad esempio, in un contesto multiaziendale è possibile associare il logo dell'azienda alla sua connessione dedicata.

### Gestione dell immagini (sezione 4)

La sezione 4 contiene gli strumenti base per la gestione delle immagini da assegnare ai singoli oggetti di connessione.

 T(All'interno di questa sezione è possibile : )
- Assegnare una immagine ad un gruppo
- Assegnare una immagine ad una connessione
- Aggiungere alla lista delle immagini disponibili una immagine reperita su una risorsa esterna


Le immagini gestite in questa sezione devono essere obbligatoriamente in formato PNG.


## Gestione e manutenzione delle connessioni

La scheda di gestione delle connessioni consente anche la gestione e la manutenzione delle connessioni dopo la loro creazione. Le operazioni di manutenzione disponibili e applicabili a tutti gli oggetti interessati (utenti, gruppi e connessioni) sono le seguenti.

 T(Operazioni disponibili : )
- Creazione di utente/gruppo/connessione
- Modifica di connessione
- Copia di utente/gruppo/connessione
- Ridenominazione di utente/gruppo/connessione
- Cancellazione di utente/gruppo/connessione
- Asseganzione di immagine a gruppo/connessione
- Aggiunta di una immagine alla lista delle immaginidisponibili
- Esportazione delle impostazioni di un profilo in uno zip
- Importazione delle impostazioni di un profilo da uno zip (generato con la funzione precedente)


I bottoni per la richiesta delle singole azioni di gestione sono posti nella relativa sezione in funzione dell'oggetto su cui verrà applicata l'azione stessa. Quindi le azioni sugli utenti saranno nella parte bassa della sezione 1, quelle sui gruppo nella sezione 2 e così via.


