## OBIETTIVO

Registrare le informazioni techiche di funzionamento di tutti i moduli del client

## ATTIVAZIONE

Alcuni log sono sempre attivi, altri attivabili dalla riga di comando di LoocUp.
Il contenuto dei log può cambiare in base alla modalità di funzionamento di Loocup, in particolare la modalità di debug, incrementa il dettaglio delle informazioni registrate.

Aggiungento il parametro --dbg sul comando di apertura di LoocUp viene attivata la modalità di debug. Questa modalità fa incrementare le informazioni registrate nei vari log e inoltre attiva la loggatura delle comunicazione del modulo base verso l'AS400 la scheda e l'emulatore, viene inoltre attivata la loggatura dei ping.

Aggiungento il parametro --logcom sul comando di apertura di LoocUp viene attivata la modalità di loggatura della comunicazione. Questa modalità attiva la loggatura delle comunicazione del modulo base verso l'AS400 la scheda e l'emulatore, viene inoltre attivata la loggatura dei ping.


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


### Log sempre attivi

Quasi tutti i componenti generano uno specifico log, che, in funzione della modalità di fgunzionamento di Loocup contiene più o meno informazioni.
Vediamo una panoramica dei log comuni : 

 * CONSOLE
 ** estensione .log
 ** contiene le informazioni di funzionameno di loocup. Le righe normalmente contengono data - ora e messaggio. In caso di eccezione viene registrato un testo disposto su più righe. Quando in Loocup viene richiesta la viosualizzazione della console, viene creato un file CONSOLE_DUMP che contiene la copia di quanto scritto nel file CONSOLE. Questo viene fatto perchè il file potrebbe essere allocato in scrittura e certi editor (ad esempio Wordpad) richiedono un lock anche in scrittura.
 * LOCBAS
 ** estensione .log
 ** Descrizione :  log del modulo BAS, logga la comunicazione da e verso l'AS400 in modalità di debug
 ** Scrittura : 
 *** avviene in modalità debug  (--dbg)
 *** oppure in modalità di loggatura della comunicazione (--logcom)
 ** Tipo log :  tecnico.
 ** Contenuto : 
 *** Data,
 *** Ora,
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** indice relativo
 *** ambiente
 *** tipo lettura (richiesta / risposta)
 *** progressivo
 *** messaggio composto da coppie attributi-valore e dai primi 1000 caratteri della lettura / scrittura su coda
 ** Separatore campi :  tabulazione


 * LOCEMU - comunicazione
 ** estensione .cmn
 ** contiene le informazioni sulla comunicazione
 * LOCEXD - comunicazione
 ** estensione .cmn
 * LOCEXD
 ** estensione .err
 ** errori (creato solo in caso di errori)
 * LOCINFO
 ** estensione.log
 ** riempito solo se loocup avviato in modalità di loggatura della comunicazione
 ** contiene le informazioni di ambiente della macchina su cui lavora e della jvm utilizzata
 * LOCLOG
 ** estensione .log
 ** contiene :  le informazioni di funzionamento del JA_00_05 e le informazioni scritte dalla classe che gestisce le colonne aggiuntive.
 ** NOTE :  dovrebbe essere il file di log di loocup, di tutte le parti generali che non hanno un modulo/componente specifico.

### Log specifici dei componenti

Questi log si creano solo quando il componente relativo gestisce un log specifico e quando il compontente viene richiamato in LoocUp.

Hanno tutti estensione .log

Vediamo i log specifici dei componenti

 * LOCG30 : 
 ** Descrizione :  Log del modulo G30
 ** Scrittura :  avviene in modalità debug  (--dbg)
 ** Tipo log :  tecnico utilizzato per lo sviluppo / test del modulo.
 ** Contenuto : 
 *** Data,
 *** Ora,
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** messaggio lunghezza libera
 ** Separatore campi :  tabulazione

 * LOCDBM : 
 ** Descrizione :  log del modulo DBM per importazione/esportazioni DB
 ** Scrittura :  creato alla prima invocazione di una funzione DBM e mantenuto per esecuzione successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di una funzione DBM
 ** Contenuto : 
 *** Data
 *** Ora
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** Stringa libera

 * LOCDOC : 
 ** Descrizione :  log del modulo DOC per generazione documentazione PDF/Latex
 ** Scrittura :  creato alla prima invocazione di una funzione DOC e mantenuto per esecuzione successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di una funaione DOC
 ** Contenuto : 
 *** Data
 *** Ora
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** Stringa libera

 * LOCREP : 
 ** Descrizione :  log del modulo REP per generazione report
 ** Scrittura :  creato alla prima invocazione di una funzione REP e mantenuto per esecuzione successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di una funzione REP
 ** Contenuto : 
 *** Data
 *** Ora
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** Stringa libera

 * LOCIMD : 
 ** Descrizione :  log del modulo IMD per generazione dinamica immagini
 ** Scrittura :  creato alla prima invocazione di una funzione IMD e mantenuto per esecuzione successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di una funzione IMD
 ** Contenuto : 
 *** Data
 *** Ora
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** Stringa libera

 * LOCWFD : 
 ** Descrizione :  log del modulo WFD per creazione grafica workflow
 ** Scrittura :  creato alla prima invocazione di una funzione WFD e mantenuto per esecuzione successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di una funaione WFD
 ** Contenuto : 
 *** Data
 *** Ora
 *** Stringa libera

 * LOCFLU : 
 ** Descrizione :  log del modulo FLU per la gestione dei flussi
 ** Scrittura :  viene creato alla prima invocazione di un flusso e mantenuto per le esecuzioni successive all'interno della stessa sessione di Looc.Up
 ** Tipo log :  tecnico, traccia i passi di esecuzione di un flusso
 ** Contenuto : 
 *** Data,
 *** Ora,
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** messaggio lunghezza libera
 * LOCSET
 ** Descrizione :  log del gestore dei setup
 ** Scrittura :  avviene in modalità debug  (--dbg)
 ** Tipo log :  tecnico utilizzato per lo sviluppo / test del modulo.
 *** Contenuto : Data,
 *** Ora,
 *** tipo messaggio (DBG, INFO, ERRORE),
 *** messaggio lunghezza libera
 ** Separatore campi :  tabulazione


### Log Generali

 * LOQUE
 ** estensione .log
 ** contiene tutta la comunicazione di loocup da e verso l'AS400 e da e verso i moduli Delphi (Emulatore e Scheda). Per questioni di dimensioni del file, vengono registrati solo i primi 1000 caratteri che transitano

come quelli in modalità di debug ma non vengono incrementate le informazioni di log dei moduli.

 * LOCINFO
 ** Descrizione :  contiene le informazioni di sistema del client
 ** Scrittura :  avviene in modalità debug  (--dbg)
 ** Tipo log :  informativo.
 *** Contenuto :  Data,
 *** Ora,
 *** tipo messaggio (DBG),
 *** attributo (30 caratteri)
 *** valore (1000 caratteri)
 ** Separatore campi :  tabulazione

 * LOPING
 ** Descrizione :  contiene le informazioni di ping
 ** Scrittura :  avviene in modalità debug  (--dbg) o di log della comunicazione
 ** Tipo log :  informativo.
 ** Contenuto : 
 *** Data,
 *** Ora,
 *** tipo log
 *** nome log
 *** ambiente
 *** id connessione
 *** libreria coda
 *** nome coda
 *** evento
 ** Separatore campi :  tabulazione

 * LOQUE
 ** Descrizione :  contiene le informazioni lette e scritte sulle code e sui socket. Vengono registrati gli XML che transitano da e verso l'AS400 e da e verso i moduli Delphi (Emulatore e Scheda). Per limitare la dimensione del file, vengono registrati solo i primi 1000 caratteri che transitano.
 ** Scrittura :  avviene in modalità debug  (--dbg) o di log della comunicazione
 ** Tipo log :  informativo.
 ** Contenuto : 
 *** Data,
 *** Ora,
 *** tipo log
 *** indice relativo
 *** ambiente
 *** classe java che effettua l'operazione
 *** tipo operazione (lettura/scrittura/evento)
 *** porta o metodo
 *** primi 1000 caratteri transitati
 ** Separatore campi :  tabulazione

 * LOCLOG
 ** Descrizione :  contiene le informazioni di funzionamento di loocup di carattere generale.
 ** Scrittura :  avviene in modalità debug  (--dbg)
 ** Tipo log :  informativo.
 *** Contenuto :  Data,
 *** Ora,
 *** tipo messaggio (DBG,INFO,ERR),
 *** messaggio
 ** Separatore campi :  tabulazione
