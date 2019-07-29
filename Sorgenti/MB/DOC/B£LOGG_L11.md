## OBIETTIVO

Tracciare le performance del client nelle elaborazioni dell'emulatore e della scheda.

## ATTIVAZIONE

Per l'emulatore il log è sempre attivo.

Per la scheda, invece l'attivazione è opzionale.
La sua gestione è richiamabile dal setup della scheda.
Il setup della scheda è richiamabile dall'icona verde in alto a sinistra di tutte le finestre di scheda di loocup.
Da li con tasto destro, va richiamata la voce "Carica/Gestisci Configurazione"
Si aprirà quindi la schermata con le configurazioni al momento presenti. Da questa schermata si può evincere il fatto che l'attivazione può essere fatta a livello di utente/ambiente o per tutti gli utenti/tutti gli ambienti (tramite l'indicazione nell'apposito campo del codice ** piuttosto che dell'istanza precisa (va comunque considerato che queste scelte vengono memorizzate nel file B£MEDE0F e che quindi l'attivazione su più ambienti dipende anche dal posizionamento di questo file).
Entrano inserimento o modifica della configurazione il log potrà essere gestito tramite il campo "Abilita Log Utente" sotto l'etichetta "Debug".

## GESTIONE DATI DEL LOG

I log di loocup sono salvati in  file locali, organizzati per sessione
## I log prodotti dal client Loocup
Alla data del 27/11/2007, versione di test di loocup, i file di log sono stati concentrati nella cartella identificata dal percorso
_7_%APPDATA%\Loocup\LOG.

La variabile di windows %APPDATA%, corrisponde alla variabile di Loocup ***APPDATA**.

Se il sistema operativo è Windows XP la variabile viene risolta in : 
C : \Documents and settings\utente_di_windows\Dati Applicazioni\Loocup\
## Durata dei log
I log vengono mantenuti per 7 giorni.
## Nomenclatura
I file hanno  il nome composto secondo due sintassi : 

Sessione_Utente_LOCComponente.estensione
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LOC :  è una costante
- Componente :  è il codice del componente Loggato (J1GRA)
- estensione può essere
-- PR :  indica log di performance (scritti dai componenti EXD e EMU)
-- ERR :  indica log di errore (scritti dai componenti EXD e EMU)
-- CMN :  indica log di comunicazione (solo per il componente EMU)
-- log :  indica log generali o di altri componenti


Sessione_Utente_LOTipoLog.log
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LO :  è una costante
- TipoLog :  è il tipo di log. Attualmente sono definiti i seguenti due tipi
-- PING :  memorizza i messaggi di ping inviati all'AS400 (sono i messaggi necessari a mantenre attivi i lavori su AS400)
-- INFO :  memorizza le informazioni di sato del client


I log di performance sono identificati fra gli altri tramite l'estensione ".PR".

I dati in essi contenuti saranno interrogabili e gestibili tramite le schede specifiche.

In base a quanto descritto è importante notare questi due aspetti : 
* Visto che i dati vengono memorizzati sul client, anche se la configurazione viene attivata per tutti gli utenti, nelle interrogazioni avrò la possibilità di vedere solo i log del client su cui sono.
* I dati pur essendo manutenzionabili tramite le schede vengono comunque automaticamente eliminati ogni 7 giorni.

Per questi motivi è possibile utilizzare nella scheda una  funzione che permette di copiare i file di log dalla cartella dell'utente ad una cartella di installazione di loocup (nell'assunzione che loocup sia installato su un server disponibile a più utenti). Per questo motivo nelle interogazioni è predisposta sia l'interrogazione della cartella di log dell'utente che quella di installazione di loocup.



