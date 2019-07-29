# Generalità
Tutti i programmi di gestione prevedono la memorizzazione automatica dei dati di impostazione, l'effetto è che quando l'utente richiama un programma utilizzato in precedenza, questo si presenta con le ultime impostazioni fatte dall'utente.

Quando le impostazioni sono particolarmente complesse è possibile utilizzare la funzione di "_2_Memorizzazioni multiple" che permette di salvare queste parametrizzazioni con un nome in modo da poterle richiamare in un tempo successivo per riutilizzarle.

Esiste anche una funzione di servizio, di uso normalmente demandato al gestiore del sistema, attraverso la quale si possono copiare memeorizzazioni da un utente all'altro o cancellare, per un utente/programma, delle memorizzazioni esistenti.

# Gestione memorizzazioni multiple
Questa funzione è comune e le modalità di utilizzo sono le stesse in tutto Sme.up.

Alle memorizzazioni dati video si accede inserendo uno dei caratteri di ricerca classici di Smeup ('!' '?') nel campo presente in alto nei formati di parzializzazione o nei formati di richiesta parametri : 

![B£_03_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£MDV0/BX_03_01.png)
viene presentata la lista delle memorizzazioni già presenti (X per selezionarne una già creata).

## Creazione / Modifica / Cancellazione
Dopo aver inserito nel formato di input i parametri di impostazione o le parzializzazioni da memorizzare si apre la lista delle memorizzazioni e, con l'opzione 1, se ne crea una nuova inserendo il nome e la descrizione. Con INVIO la memorizzazione è già creata.

Per modificarne una presente :  inserire o cambiare le impostazioni sul formato di input quindi aprire la lista delle memorizzazioni e utilizzare l'opzione 2.
Viene presentata una finestra di conferma di aggiornamento, inserire 1 nel campo modifica dati e confermare col tasto F6 : 

![B£_03_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£MDV0/BX_03_02.png)
Per cancellare una memorizzazione usare l'opzione 4 dalla lista.

## Default utente
Se dalla lista delle memorizzazioni si preme il tasto F6 l'impostazione viene memorizzata come _2_"default utente", questo significa che ogni volta che l'utente entra in quella funzione i parametri vengono sempre impostati in accordo alle impostazioni memorizzate nel default utente indipendentemente dalle impostazioni presenti l'ultima volta che l'utente ha utilizzato la funzione.

## Memorizzazioni multiple utente
Le memorizzazioni multiple che abbiamo visto sono disponibili a tutti gli utenti, esiste una seconda famiglia di memorizzazioni multiple che è specifica per l'utente.

Per attivare questa seconda gestione, dalla finestra di lista delle memorizzazioni multiple inserire un carattere di ricerca nel campo di input immediatamente superiore all'ambiente : 

![B£_03_04](http://localhost:3000/immagini/MBDOC_OGG-P_B£MDV0/BX_03_04.png)
viene presentata la lista delle memorizzazioni per utente già presenti (X per selezionarne una già creata).
La gestione è analoga alle memorizzazioni multiple con la differenza che il codice è lungo 1.

_1_Nota :  se presente, il default utente è quello con codice = _2_"*"  (asterisco).

# Manutenzione memorizzazioni video
Questa funzione serve per modificare le memorizzazioni video relative a qualsiasi programma ed a qualsiasi utente; è anche possibile copiare i parametri di scelta tra programmi diversi per utenti diversi.
_2_Nota bene; si deve fare molta attenzione nel copiare MDV tra programmi diversi per evitare incompatibilità dovute a programmi con formato incompatibile.

## Formato guida
![B£BASE_03](http://localhost:3000/immagini/MBDOC_OGG-P_B£MDV0/BXBASE_03.png)
 * _2_UTENTE :  Se si inserisce solo il nome di un Utente e successivamente si preme invio compare il "Formato di Scelta" dove è possibile scegliere se Variare, Annullare, Interrogare i parametri video per ogni programma elencato.
 * _2_PROGRAMMA :  Viceversa inserendo solo il nome di un programma appare il "Formato di Scelta" con le opzioni Variazione, Annullamento e Interrogazione riferite alle scelte video degli utenti di cui esistono i parametri relativi al programma inserito.

Per questi due campi è previsto l'utilizzo della stringa "**" di inserimento generico.

Se si compilano i campi _2_"Copia da" il programma copia le memorizzazioni da un altro utente/programma.

Completata la fase di scelta si accede al prossimo formato video che appare in modalità "Immisione" se non esistono parametri di scelte video, altrimenti appare in modalità "Variazione".

## Formato dettaglio
![B£BASE_04](http://localhost:3000/immagini/MBDOC_OGG-P_B£MDV0/BXBASE_04.png)In questo formato video sotto il titolo compare la modalità operativa (Immissione o Variazione), in seguito sono riportati il nome dell'utente, il nome del programma, e la data dell' ultima modifica.
La tabella sottostante rappresenta un record di 300 byte dove è possibile modificare o inserire in modo sequenziale i parametri delle scelte video.

La lettera "_2_A" nel campo Annullamento cancella il record di memorizzazione.
