# Comunicazione via Socket tra Looc.Up e server As.UP

In questo documento verrà illustrata la modalità di comunicazione tra il client Looc.UP (e Smeup Provider) e il
server As.UP.

# Modulo di comunicazione di Looc.UP e modalità di comunicazione

Il client Looc.UP comunica con il server di riferimento attraverso collegamenti socket. A seconda del sistema
di riferimento (iSeries, As.UP o altro) il relativo modulo di comunicazione deve implementare i servizi richiesti
implementando i servizi definiti nella classe astratta AbstractNetServer definita nel package
**Smeup.smec_s.net**

La classe AbstractNetServer implementa le funzionalità comuni a tutti i moduli di comunicazione (e indipendenti
dal tipo di server connesso) e definisce le funzionalità specifiche che devono essere implementate nei singoli
moduli di comunicazione.

Le funzionalità richieste da un generico modulo di comunicazione hanno questa classificazione di massima : 


- Connessione e disconnessione al server
- Verifica esistenza ed autenticazione di un utente
- Gestione code dati normali e per chiave (creazione, cancellazione, scrittura e lettura su coda)
- Call di un programma (in emulazione)
- Gestione del server (informazioni, connessioni)


e rappresentano le tipologie di messaggi scambiati tra una istanza del client Looc.Up e il server a cui è connesso.

# Moduli di comunicazione definiti in Looc.UP

All'interno del client Looc.UP sono stati implementati vari moduli di comunicazione. I due principali moduli di
comunicazione sono comunque quelli dedicati alla comunicazione verso iSeries e alla comunicazione verso
As.UP. Ai fini di questo documento il modulo di comunicazione di maggior interesse sarà quello verso As.UP,
che verrà pertanto spiegato con maggior dettaglio. Per maggiori informazioni sul modulo di comunicazione
iSeries (e sugli altri moduli di comunicazione presenti) fare riferimento ai documenti dedicati al modulo applicativo LO.

![MULOOC_04A](http://localhost:3000/immagini/MULOOC_04/MULOOC_04A.png)
## Modulo comunicazione verso IBM iSeries

E' il modulo di comunicazione di default per Looc.UP e consente la comunicazione verso il sistema ISeries IBM
attraverso le funzionalità offerte dal pacchetto di comunicazione Java Tool Box for iSeries (nella sua implementazione
open **JT400 Open**).

La classe base di implementazione è la **AS400NetServer** definita nel package **Smeup.smec_s.net.as400**

## Modulo di comunicazione verso server As.UP

E' il modulo che gestisce la comunicazione tra il client Looc.Up e un server As.UP.

La classe base di implementazione è la **AsupNetServer** definita nel package **Smeup.smec_s.net.asup**

In Looc.UP il modulo di comunicazione utilizzato per default è quello verso iSeries. Per fare in modo che Looc.UP si avvii connettendosi
verso un server As.UP è necessario abilitare il corretto modulo di comunicazione in fase di avvio del client. Questa cosa può essere
ottenuta in due modi alternativi : 


- Se si avvia Looc.Up utilizzando SmeupGO, è necessario creare una connessioni di tipo As.UP selezionando l'apposita
opzione delle proprietà del collegamento (per dettagli vedi la documentazione di SmeupGO).
- Se si avvia Looc.UP da linea di comando (ad esempio, all'interno di script di avvio di un server Smeup Provider) per abilitare
la comunicazione verso un server As.UP è necessario inserire l'opzione **--asup**


Come per la connessione verso l'iSeries, l'identificazione del server As.UP a cui collegarsi avviene specificando l'indirizzo IP
del server desiderato o un nome host conosciuto dal DNS di rete.

# Dettagli tecnici sulla comunizazione tra Looc.UP e server As.UP

![MULOOC_04B](http://localhost:3000/immagini/MULOOC_04/MULOOC_04B.png)
La comunicazione tra Looc.UP e il server As.UP avviene attraverso l'utilizzo di socket TCP/IP, attestati su porte specifiche.
Per analogia a quanto succede nella comunicazione verso iSeries, le porte di comunicazione utilizzate verso As.UP sono
le stesse utilizzate nella comunicazione verso iSeries. Il protocollo di comunicazione non è di tipo testuale ma è basato sulla
serializzazione sullo stream del socket di classi POJO. Le classi di comunicazione utilizzate dal modulo As.UP sono accessibili
all'interno del client Looc.UP perchè definite nella libreria **comobj.jar** distribuita con il prodotto. La presenza di questa
libreria nel classpath di Looc.Up è l'unico prerequisito richiesto lato client per consentiree la comunizazione con un server As.UP.

Dal lato server As.UP, i servizi di comunicazione sono forniti da appositi connettori, implementati all'interno del bundle
OSGI **com.smeup.erp.mu.looc.connector**

Vediamo in dettaglio i singoli servizi di comunicazione implementati lato server in As.UP : 


## Servizio di autenticazione

Fornisce l'accesso al servizio di autenticazione utente e creazione della sessione di connessione


- **Porta : ** 8476
- **Connettore lato As.UP : ** SignonSocketHandler nel package com.smeup.erp.mu.loocup.connector.signon
- **Classe di comunicazione : ** SignonRequestBean nel package com.smeup.asup.comobj


## Servizio di accesso alle code dati

Fornisce i servizi di accesso alle code dati


- **Porta : ** 8472
- **Connettore lato As.UP : ** DataQueueSocketHandler nel package com.smeup.erp.mu.loocup.connector.dtaq
- **Classe di comunicazione : ** QueueRequestBean nel package com.smeup.asup.comobj


## Servizio di invocazioni programmi

Fornisce i servizi di invocazione di programmi


- **Porta : ** 8475
- **Connettore lato As.UP : ** ProgramSocketHandler nel package com.smeup.erp.mu.loocup.connector.pgm
- **Classe di comunicazione : ** PgmcRequestBean nel package com.smeup.asup.comobj



## Shell telnet

Fornisce una console di accesso al sistema As.UP secondo il protocollo telnet


- **Porta : ** 8023


## Shell As.UP specifica per Looc.UP

Fornisce i servizi di comunicazione utilizzati dalla console As.UP implementata nel client Looc.UP


- **Porta : ** 8024
- **Connettore lato As.UP : ** LoocupShellSocketHandler nel package com.smeup.erp.mu.loocup.connector.shell



