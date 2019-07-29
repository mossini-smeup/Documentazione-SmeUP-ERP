# Caratterizzazione temporale degli impegni

E' possibile caratterizzare le transizioni di un workflow con informazioni temporali volte a definire i tempi massimi di esecuzione dei relativi impegni. Lo scopo di queste informazioni è duplice : 

- Tracciare le performance dell'esecuzione degli impegni, in modo da poter analizzare il processo per eliminare eventuali colli di bottiglia.
- Evidenziare gli impegni più urgenti, anche se non ancora scaduti.
- Sollecitare, durante l'esecuzione di un ordine di workflow, l'esecuzione di eventuali impegni in ritardo.


## Assegnazione

Il lead time di assegnazione indica quanto tempo (in ore) può trascorrere da quando l'impegno corrispondente viene attivato (sono soddisfatti tutti i suoi requisiti) a quando l'impegno viene assegnato ad un utente univoco.
Si ricorda che l'assegnazione può avvenire in push (un responsabile di assegnazione forza l'utente di esecuzione) o in pull (un utente tra quelli abilitati ad eseguire l'impegno lo prende in carico).

## Esecuzione

Il lead time di esecuzione si riferisce a quanto tempo può passare tra quando l'impegno è assegnato a quando è eseguito.
Il tempo assegnato di esecuzione indica quante ore si stima vengano impiegate nell'esecuzione dell'impegno.

## Calcolo dei vincoli temporali.

All'attivazione vengono calcolate : 

- Data/ora richieste di assegnazione :  Data/ora attuale + lead time di assegnazione.
- Data/ora richieste di esecuzione :  Data/ora attuale + lead time di assegnazione + lead time di esecuzione.


All'assegnazione viene rivista la data/ora richiesta di esecuzione, in base all'istante di assegnazione : 

- Data/ora richieste di esecuzione :  Data/ora attuale + lead time di esecuzione.


Per gli impegni fuori dalla rete di Petri (slave, extra-rete) i vincoli temporali vengono calcolati alla creazione degli impegni; questi poi possono essere rivisti da chi sta creando o modificando tali impegni.


## Forzatura dei vincoli temporali (SV)

Sarà possibile forzare un tempo (data/ora) di richiesta di esecuzione diverso da quello indicato dal calcolo tramite lead time.


# Tracciabilità dei tempi di esecuzione

Per ogni impegno vengono tracciate n attività relative alla sua "vita" (attivazione, presa in carico, esecuzione...).
Per ogni attività vengono segnate data e ora effettiva di esecuzione. Per alcune di queste attività viene tenuto traccia anche della data/ora richieste, in particolare : 

- Data/ora richieste di assegnazione vengono aggiunte all'attività di assegnazione (o presa in carico, se l'assegnazione è avvenuta in pull).
- Data/ora richieste di esecuzione vengono aggiunte all'attività di dichiarazione.

Confrontando le date/ora effettive con quelle richieste si avrà modo di valutare le performance degli impegni (e, di conseguenza, dei processi e degli utenti che li svolgono), sia per quanto riguarda l'assegnazione che l'esecuzione effettiva del lavoro.


# Solleciti (SV)

Da fare
