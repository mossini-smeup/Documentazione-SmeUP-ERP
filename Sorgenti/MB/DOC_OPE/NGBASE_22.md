# Gestione Attività Negozi

## Gestione Attività Negozi

## Premessa

La procedura qui descritta permette la Gestione delle Attività dei Negozi. In questo modo è possibile ricordare al Negozio di effettuare alcune Operazioni, come ad esempio Compilare Chiusure di Cassa Mancanti, Sistemare il Negozio per l'Inventario, Controllare la Merce Ricevuta, Preparare Merce da Inviare, etc..
Sono previste le seguenti funzioni : 

 * Gestione Attività. Dal _Menu>Principale>Anagrafiche di Base>Gestione Attività_

 * Visualizzazione Stato Attività. Dal _Menu>Visualizza>Analisi Stato Attività_

La gestione delle Attività del Negozio (generazione e chiusura) potrà anche essere effettuata automaticamente da Negoziando, nel Ricevimento Merce da Colli, nel Workflow e negli Eventi Inventariali.

**Per configurare le Attività legate al Ricevimento Merce da Colli**

Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Tipi Documento Magazzino e Causali>Pannello Ricevimento Merce da Colli occorre definire la parte relativa al Controllo Differito, impostando : 

 * Numero Giorni per Controllo Carico. Giorni calcolati a partire dal Ricevimento della merce
 * Codice per Registrazione Attività Negozio. Occorre aver precedentemente inserito l'Attività nella Tabella ATTI (vedi Definizione Tabella Attività del Negozio)
 * Giorni da Escludere per Calcolo Data Scadenza Controllo. Se il negozio fosse chiuso di domenica, ad esempio, sarebbe possibile escludere quel giorno dal conteggio

La prima funzione **Ricevimento Merce da Collo (Carico Amministrativo)** effettuerà la registrazione dell'Attività di **Controllo Contenuto Colli** impostandone le scadenza in base ai valori
specificati in Configurazione, la seconda funzione **Controllo Ricevimento Merce da Colli** provvederà a chiudere l'attività una volta effettuato tale controllo.

(Vedi Ricevimento Merce da Colli.)

**Per configurare le Attività legate agli Eventi Inventariali**

_Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Tipi Documento Magazzino e Causali>Rettifiche Inventariali  specificare il Codice Attività Notifica Eventi nella parte relativa agli Inventari Parziali (Tabella ATTI)
In sede verrà inserito un nuovo Modello Evento Inventariale e, alla pressione del Tasto F11 Conferma Evento, scatterà la segnalazione dell'Attività.

**Per configurare le Attività legate al Workflow**

Dopo aver definito la configurazione del Workflow e dopo aver creato l'Attività relativa, creare un Commento per la Generazione dell'Attività.
Dal Menu>Anagrafiche di Base>Gestione Commenti premere F6 Inserisci. Definire un Codice Commento e Confermare. Aggiungere una Descrizione, selezionare una Tipologia Commento per Gestione Attività W.F. e Confermare.
A questo punto verrà richiesto di definire : 

 * Codice Attività
 * Attività per Negozio
 * Attività per Utente
 * Attività per Operatore
 * Data Inizio/Scadenza Attività
 * Priorità
 * Numero/Data Riferimento
 * Annotazioni

Tutti i campi NON gialli possono anche essere compilati premendo F2 Inserisci Variabile


_Menu>Principale>Anagrafiche di Base>Gestione Tabelle>Tabella WFLX - Transizioni Workflow_ e compilare la Richiesta Defionizione Commento per Generazione Attività

## Definizione Tabella Attività del Negozio

Per attivare questa funzionalità occorre definire i Codici di Attività nelle Tabelle di Negoziando.
Dal _Menu>Principale>Anagrafiche di Base>Gestione Tabelle>Tabella ATTI - Attività Negozi_ e definire tali Codici. Premere F6 Inserisci per aggiungere una nuova Attività. Definire un Codice Attività e confermare. A questo punto impostare : 

 * Descrizione Attività
 * Priorità
 * Forzata Chiusura. Impostare questa richiesta per determinare se la Chiusura dell'Attività in questione può essere Forzata o meno dalla funzione di **Analisi Stato Attività**.
 ** Ammessa
 ** Non Ammessa


## Gestione Attività

Dal _Menu>Principale>Anagrafiche di Base>Gestione Attività_ è possibile attivare la funzione di Gestione delle Attività.
La funzione prevede inizialmente l'indicazione (facoltativa se elaborazione di Sede) del Codice Negozio, Utente e Operatore a cui le Attività sono destinate
La richiesta del Codice Negozio e dell'Utente è bloccata nel caso sia impostato nella Configurazione di Negoziando il Codice del Negozio
Una volta effettuata la selezione iniziale vengono elencate le Attività esistenti, tutte quelle che risultano aperte.
Le Attività sono ordinate per Negozio, Data/Ora Scadenza Attività e nella schermata vengono evidenziati : 

 * Codice Negozio
 * Data/Ora Scadenza Attività
 * l'Utente a cui è stata Assegnata l'Attività
 * L'Operatore a cui è stata Assegnata l'Attività
 * Il Codice e la Descrizione dell'Attività (dalla Tabella ATTI)
 * Lo Stato dell'Attività (Aperta/Completata/Forzata Chiusura)
 * Eventuale Numero e Data di Riferimento.
 ** In caso di Attività legata al Ricevimento Merce, il Numero di Rif. sarà il Numero della Bolla e la Data sarà quella del Ricevimento
 ** In caso di eventi Inventariali saranno legati al numero dell'Evento
 * Le Annotazioni della fase di Registrazione
 * L'Utente che ha registrato l'Attività
 * L'Operatore che ha registrato l'Attività
 * La Data/Ora di Inizio Attività
 * La Data/Ora di fine Attività
 * Il Codice Gruppo Attività (nel caso di Attività registrata per un Gruppo di Negozi)

N.B. Le Attività Scadute e Aperte vengono evidenziate con un triangolo giallo sulla sinistra.
Quelle Scadute ma Completate oppure Chiuse Forzatamente vengono rappresentate con la Spunta Verde

Oltre ai tasti funzionali Standard sono a disposizione : 

 * F2 Forza Chiusura
 * F3 Elimina Forzata Chiusura
 * F5 Visualizza Note Forzata Chiusura
 * F8 Attività Aperte
 * F9 Attività Scadute
 * F10 Attvità Aperte, del Giorno e Scadute
 * F11 Tutte le attività

E' da tenere presente che nella fase di Gestione sarà possibile effettuare la Forzata Chiusura di tutte le Attività, indipendentemente dalle impostazioni della Tabella ATTI.

## Inserimento Attività

Premendo F6 dalla videata dell'elenco è possibile effettuare l'Inserimento di Nuove Attività.
Se elaborazione di Sede verrà richiesto di selezionare a chi è destinata questa attività : 

 * Singolo Negozio
 * Elenco di Negozi
 * Selezione Negozi da Lista. In questo caso sarà possibile definire in Dettaglio quali sono i Negozi a cui l'attività è destinata. Verrà attivato il tasto funzionale F8 per la selezione dei Negozi

Indicare le seguenti informazioni : 

 * Codice attività (Tabella ATTI)
 * Annotazioni
 * Utente a cui è destinata l'Attività
 * Operatore a cui è destinata l'Attività
 * Data/Ora di Inizio Attività
 * Data/Ora di Scadenza Attività

Premere Invio per Confermare

(Nel caso di Elaborazione da Negozio viene impostato automaticamente, senza richiesta, Singolo Negozio).

Se l'Attività è prevista per un Gruppo (Codice Elenco Negozio o Selezione Negozi da Lista) verrà richiesta una Conferma per l'Inserimento dell'Attività.

## Selezione Negozi

Se nella selezione iniziale viene indicato **Selezione Negozi da Lista** sarà obbligatorio indicare in dettaglio i Negozi ai quali destinare l'Attività.
Apparirà l'elenco dei Negozi, premere : 

 * F7 Da Elaborare SI/NO per Selezionare/Deselezionare il Singolo Negozio
 * F8 Imposta Da Elaborare su Gruppo per contrassegnare un Gruppo di Negozi precedentemente filtrati

Viene inizialmente presentato l'elenco dei soli negozi Aperti, è possibile utilizzare il tasto funzionale F5 per Visualizzarli Tutti.

## Modifica Attività

Premendo Invio dalla videata dell'elenco è possibile effettuare la modifica di una Attività.
Se l'Attività selezionata è rivolta ad un Gruppo, viene richiesto inizialmente se la modifica deve riguardare l'Attività Selezionata o tutte le Attività del Gruppo.
Una volta effettuata tale selezione si passerà alla videata con l'indicazione delle informazioni dell'Attività.
E' da tenere presente che la modifica dell'Attività non permette la modifica del Gruppo di Negozi a cui è destinata e che, nel caso venga selezionata la modifica dell'Attività Selezionata, questa verrà sganciata dal Gruppo a cui apparteneva in precedenza.

## Elimina Attività

Premendo F4 Elimina dalla videata dell'elenco è possibile annullare un'Attività.
Come per la modifica, se l'Attività appartiene ad un Gruppo, verrà richiesto inizialmente se la cancellazione deve riguardare la Singola Attività o Tutte le Attività del Gruppo. Verrà poi richiesta conferma sulla Cancellazione della/delle Attività

## Forzatura Chiusura

Premendo F2 dalla videata dell'elenco è possibile Forzare la Chiusura di una Attività.
Come per la modifica e per la cancellazione, se l'Attività appartiene a un Gruppo verrà richiesto se si intende Forzare la Chiusura solo dell'Attività Selezionata  o di Tutte le Attività del Gruppo.
La Forzata Chiusura prevede l'indicazione Obbligatoria delle Annotazioni. Indicare tali Annotazioni e premere F6 per Confermare.

## Elimina Forzata Chiusura

Premendo F3 dalla videata dell'elenco sarà possibile eliminare una eventuale errata Forzata Chiusura.
Come per la operazioni precedenti, se l'Attività appartiene ad un Gruppo, verrà richiesto di indicare se eliminare la Forzata Chiusura sulla singola Attività o sul Gruppo.

## Visualizza Note Forzata Chiusura

Premendo F5 dalla videata dell'elenco è possibile visualizzare le annotazioni registrate in fase di Forzata Chiusura.

## Visualizzazione Stato Attività del Negozio

Dal _Menu>Visualizza>Analisi Stato Attività_ è possibile consultare le Attività in essere per il Negozio.
Come per la funzione di Gestione, questa funzione prevede inizialmente l'indicazione del Codice Negozio, Utente e Operatore. Come sopra, la richiesta del Codice Negozio e dell'Utente è bloccata nel caso il Codice del Negozio sia impostato nella Configurazione di Negoziando.
Una volta definiti i parametri di ricerca iniziali, vengono elencate le Attività relative.
Inizialmente vengono elencate solo le attività Aperte e sono ordinate per Data/Ora Scadenza Attività.
Vengono evidenziati : 

 * Data/Ora Scadenza Attività
 * L'Utente a cui è stata Assegnata
 * L'Operatore a cui è stata Assegnata
 * Il Codice e la Descrizione dell'Attività (Tabella ATTI)
 * Lo Stato dell'Attività (Aperta/Completata/Forzata Chiusura)
 * Eventuale Numero e Data di Riferimento
 * Le Annotazioni della fase di Registrazione
 * L'Utente che ha registrato l'Attività
 * L'Operatore che ha registrato l'Attività
 * La Data/Ora di Inizio Attività
 * La Data/Ora di fine Attività

N.B. Le Attività Scadute e Aperte vengono evidenziate con un triangolo giallo sulla sinistra.
Quelle Scadute ma Completate, oppure Chiuse Forzatamente, vengono rappresentate con la Spunta Verde

Sono a disposizione i seguenti tasti funzionali : 

 * F8 Attività Aperte
 * F9 Attività Scadute
 * F10 Attività Aperte, del Giorno e Scadute
 * F11 Elenca Tutte le Attività

In base alle impostazioni della tabella delle Attività e se ne esiste almeno una per la quale è possibile forzarne la Chiusura, potranno essere attivati anche i tasti funzionali : 

 * F2 Forza la Chiusura dell'Attività
 * F5 Visualizza Note Forzata Chiusura

In fase di utilizzo del tasto F2 Forza Chiusura verrà verificato se per l'Attività selezionata è ammessa o meno tale operazione.

## Segnalazione Automatica delle Attività da Completare/Scadute

E' possibile attivare la segnalazione automatica delle Attività da Completare/ Scadute al Negozio.
Per attivare questa funzionalità occorre impostare la Configurazione di Negoziando dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Altri Parametri>Pannello Altri Parametri 
Specificando SI alla richiesta **Visualizza Alert Attività**. In questo modo, all'attivazione del Menu di Negoziando verrà presentata automaticamente una finestra con le Attività da effettuare nella Giornata e le eventuali Attività Scadute.
Esiste poi la Richiesta **Controllo Attività ogni XX MInuti**. Se impostato un Valore, verrà attivato un Timer che, alla scadenza dei minuti definiti nella configurazione, presenterà automaticamente, se esistente, l'elenco delle Attività Scadute del Negozio.


