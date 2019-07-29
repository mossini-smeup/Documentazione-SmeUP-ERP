# Avvio Looc.UP con As.UP

## Avvio Looc.UP da connessione Smeup.GO

Per l'avvio di una istanza di Looc.Up verso un server As.UP, è necessario creare in Smeup.GO
un collegamento come da seguente figura : 

![MULOOC_05A](http://localhost:3000/immagini/MULOOC_05/MULOOC_05A.png)

Il client Looc.UP per default assume che il sistema server sia un server iSeries. Per questo motivo
quando si crea una connessione verso un sistema As.UP è necessario specificarlo nel link di comunicazione.
Questo può essere fatto selezionando la voce As.UP all'interno del pannello di creazione di una connessione
Looc.UP.

Ovviamente quando si imposta il flag As.UP tutte le credenziali di connessione (IP, utente, password e ambiente)
saranno relative al server As.UP a cui ci si intende collegare.


## Avvio Looc.UP da linea di comando

Nei casi in cui è necessario avviare Looc.UP da linea di comando (ad esempio, nella installazione di un Looc.UP
service provider come servizio Windows) è necessario impostare la connessione di tipo As.UP inserendo nella
chiamata il parametro --asup

Esempio di chiamata a linea di comando : 


**Loocup.exe MUAS01 UTENTE *NONE 0020 --asup**

che avvia una istanza di Looc.UP connessa al server As.UP MUAS01 con l'utente UTENTE, password richiesta in fase
di avvio e ambiente opperativo 0020.
