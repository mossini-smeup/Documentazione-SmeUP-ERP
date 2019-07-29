# La scheda di impegno

La scheda di un impegno è il posto in cui normalmente vengono eseguiti gli impegni facendo avanzare i relativi ordini.
Si ricorda che, comunque, esistono casi in cui l'esecuzione di impegni avviene direttamente senza passare per la relativa scheda.

Di seguito vengono analizzate le parti fondamentali di cui si compone la scheda di un impegno : 

![WF-FIG0009](http://localhost:3000/immagini/WFBASE_024/WF-FIG0009.png)
## Impegno

È la descrizione dell'impegno che si sta eseguendo.

## Dati specifici

È una serie di schede in cui vengono presentati dati relativi agli oggetti su cui si sta operando nel corso del workflow.
Ovviamente variano da processo a processo, eventualmente da impegno a impegno.

## Dati di workflow

È una scheda in cui vengono fornite informazioni tecniche standard relative al workflow in corso.
Possono essere informazioni relative alla situazione dell'ordine, quali ad esempio : 
 * una worklist di impegni relativi all'ordine.
 * una rappresentazione grafica dello stato attuale dell'ordine.
 * il log delle attività svolte.

Inoltre vengono mostrate informazioni specifiche dell'impegno, ad esempio : 
 * dati relativi all'impegno (stato, data e ora di attivazione).
 * le istruzioni relative al tipo di lavoro da svolgere.

## Azioni di workflow

È il cuore della scheda di impegno :  in questa sezione il motore di workflow propone le azioni eseguibili da un utente sull'impegno.
È da qua che viene effettuato l'avanzamento dell'impegno e quindi dell'ordine.
Definiamo di seguito le due più importanti azioni eseguibili da un utente su un impegno.

### Presa in carico

La presa in carico ha una doppia valenza : 
 * da un lato serve ad assegnare a sè stessi l'impegno, se questo è eseguibile da diverse persone :  in questo caso l'utente che prende in carico diventa esecutore dell'impegno e l'impegno sparisce dalle worklist degli altri potenziali esecutori.
 * contemporaneamente segnala l'inizio del lavoro sull'impegno :  in questo modo è più facile per gli altri partecipanti al processo stimare per quando l'impegno sarà completato.
 * infine inibisce l'attivazione di eventuali impegni alternativi.

### Avanzamento

L'azione di avanzamento segnala il completamento del lavoro sull'impegno.
A seconda del processo e dell'impegno l'azione di avanzamento può essere una semplice dichiarazione oppure qualcosa di più complesso, come
l'inserimento di un oggetto Sme.up. Il motore di workflow controlla l'esecuzione delle azioni di workflow :  se non vengono completate non procede con l'avanzamento.
Mentre la presa in carico è facoltativa (in particolari impegni particolarmente veloci da eseguire potrebbe essere superflua), quella di avanzamento è sempre presente.

## Azioni esterne

In questa sezione possono essere inserite azioni utili allo svolgimento dell'impegno. La loro esecuzione è facoltativa e non controllata dal motore di workflow.
