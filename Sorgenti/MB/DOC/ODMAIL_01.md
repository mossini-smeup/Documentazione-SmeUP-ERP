# Obiettivi e panoramica sulla soluzione
La finalità del progetto è quella di accedere ad un account IMAP di un server di posta e poter interagire con i messaggi in esso contenuti con funzioni di ricerca, riorganizzazione, _registrazione_.
La soluzione si basa su un collegamento IMAP diretto ad un account di posta e sulle funzioni Loocup necessarie all'interazione con esso.

Le tipologie degli oggetti principalmente coinvolti sono due :  i Folder e i Messaggi e prevede le seguenti funzioni

- GESTIONE DEI  FOLDER
-- Apertura del folder (anche tramite ricerca _like_ sul nome)
-- Creazione dei folder
-- ...
- INTERROGAZIONE DEI FOLDER
-- Interrogazione dei Folder per identificare uno o più messaggio
-- ...
- GESTIONE DEI MESSAGGI
-- Estrazione degli attributi del messaggio
-- Estrazione ed eventuale visualizzazione degli allegati del messaggio
-- Copia di un messaggio in altro Folder
-- Eliminazione di un messaggio
-- Registrazione di un messaggio tramite configurazione
-- ...


## Il server
Il server cui ci si può collegare è un normale server IMAP di posta.
Al server si accede tramite il suo indirizzo e le credenziali (utente e password) di un account esistente su tale server.
Un account è composto da differenti Folder (o Cartelle) anche annidate in una struttura ad albero che ha come radice la cartella INBOX e di cui non è limitato l'annidamento.
Il path di una cartella è espresso in questi termini INBOX.SUBFOLDER1.SUBFOLDER2 dove SUBFOLDER1 è contenuto in INBOX e contiene SUBFOLDER2
Il folder quindi può contenere o altri folder o messaggi.
I messaggi sono comunemente noti anche come mail.
## Il login
Il login avviene alla prima richiesta al server e la sessione di collegamento viene mantenuta per tutta la sessione Loocup salvo effettuare un cambio connessione o una chiusura connessione esplicite tramite le funzioni previste.
I parametri di connessione possono essere forniti nelle modalità espresse nel documento relativo alle **Funzioni**in due modi : 
## I Folder
I folder sono caratterizzati da attributi quali :  Nome, numero messaggi contenuti, letti, non letti, eliminati, scrivibilità/leggibilità, se è foglia o meno, ...
L'elenco dei folder può essere ottenuto con l'apposita funzione eventualmente per parti di nome
## I Messaggi
I messaggi sono l'ultimo elemento (e il protagonista) del modulo in oggetto.
### I componenti del messaggio
I messaggi sono composti da differenti elementi : 

- Mittente
- Destinatari di diverso livello (To, Cc, Bcc)
- Subject
- Testo
- Allegati
- Headers

### Gli elementi classici
Gli elementi più noti che caratterizzano il messaggio sono quelli visibili in qualunque programma di posta :  il mittente, i destinatari, il testo, il subject e gli allegati e su questi non diremo altro per il momento.
### Gli headers
Le caratteristiche nascoste di un messaggio sono racchiuse invece sotto la generica voce di headers.
Fra questi headers ci sono le informazioni che segnalano il ciclo di vita del messaggio :  Id del messaggio, da dove è partito, che server l'ha spedito, il cliente che l'ha spedito, il server dove è stato consegnato, se il messaggio è stato letto, la priorità, la richiesta di ricevuta, etc.
Queste sono quasi tutte informazioni invisibili agli utenti.
Le funzioni che mette a disposizione il modulo ODMAIL permettono di interrogare il messaggio per estrarne sia i contenuti comuni che gli headers. Oltre a ciò esistono funzioni che permettono anche di aggiungere o modificare informazioni negli headers.
### La registrazione del messaggio
Il modulo ODMAIL annovera fra le sue funzioni, elencate nell'apposito file di documentazione, anche la funzione di registrazione dei messaggi. Con registrazione dei messaggi s'intende che il messaggio viene caratterizzato con alcune informazioni in base alle quali sarà possibile recuperarlo qualora ce ne sia bisogno.
Una volta identificato il messaggio in base al folder cui appartiene e al suo ID è possibile effettuarne la registrazione. Tale procedura prevede che Loocup richiami un servizio AS400 (il LOSER_33, metodo IMA.TRM) per ottenere gli attributi che verranno utilizzati per inserire un header chiamato SM-UIKey nel messaggio. Scritto tale header, potrà essere poi utilizzato per le ricerche.
### La de-registrazione del messaggio
Così come è possibile registrare un messaggio è possibile anche de-registrarlo con l'apposita funzione. La de-registrazione non consiste altro che nella cancellazione del header SM-UIKey.
