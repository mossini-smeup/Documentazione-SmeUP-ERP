## La scheda di interrogazione dei tracciati
E' visibile solo per utenti con USRLVL 01 o superiore.
Lo scopo di questa scheda è quello di permettere una prima analisi dei dati che stanno per essere inviati all'SdI, in base all'estrazione effettuata.
Ogni volta che si effettua l'estrazione delle fatture per la fatturazione elettronica viene generato un lotto di record sull'EDSEND.
I filtri selezionabili, anche in abbinamento, sono : 
* Messaggio. Permette di filtrare sul tipo di lotto creato. (£FE per le fatture da inviare, £AB01 per l'invio a Abletech, £AB02 per l'autenticazione su Abletech, £AB04 per gli esiti delle fatture trasmesse ad SDI e £AB05 per fatture inviate, ma non ancora veicolate all'SDI).
* Numero Lotto. E' il numero identificativo che raggruppa tutte le fatture estratte con lo stesso lancio
* Indirizzo origine e Indirizzo destinazione :  identificano il tipo di tracciato con cui viene creato l'EDSEND.
* Data iniziale e finale. Filtra tutti recordo nel range specificato. Se impostata solo la data finale, si comporta come un 'fino a'. Se impostata solo la data iniziale si comporta come un 'da'

Importante è analizzare lo stato di un lotto, se è 80 è stato generato correttamente e chiuso, se è 85 è stato generato con errori, se è 90 significa che i record sono stati annullati a seguito di una riestrazione della fattura.
Inoltre é possibile analizzare tutti i record che fanno parte del lotto cliccando sulla freccia a sx del record e scegliendo l'opzione 'Batch Detail'.
Nella videata successiva si possono selezionare i vari record e controllarne il contenuto.

### La scheda dei log di integrazione con il webservice
E' visibile solo per utenti con USRLVL 02.
Lo scopo di questa scheda è controllare i log della comunicazione con il webservice di invio.
E' molto importante perchè da questa scheda si possono analizzare eventuali errori di trasmissione e possono essere controllate le eventuali risposte fornite dal webservice.
I filtri selezionabili, anche in abbinamento, sono : 
* Data iniziale e finale. Filtra tutti recordo nel range specificato. Se impostata solo la data finale, si comporta come un 'fino a'. Se impostata solo la data iniziale si comporta come un 'da'
* Ora iniziale e finale. Filtra tutti recordo nel range specificato. Se impostata solo l'ora finale, si comporta come un 'fino a'. Se impostata solo l'ora iniziale si comporta come un 'da'
* Utente applicativo. è l'utente che ha lanciato i programmi di comunicazione con il webservice
* Funzione K11 e Metodo K11. Filtra su determinati funzioni e metodi della K11
* Subsezione A38. Filtra su determinate subsezioni A38
* Provider. Filtra su provider

### La scheda del log della coda dati
E' visibile solo per utenti con USRLVL 02.
Lo scopo di questa scheda è quello di andare ad analizzare le informazioni passate sulla coda dati.
La scrittura del log di quanto scritto sulla coda dati è attivabile in tabella JA1 (Attivazione log £G64).
Attenzione :  l'attivazione del log comporta la scrittura di una notevole mole di dati su JALOGT0F.
* Data iniziale e finale. Filtra tutti recordo nel range specificato. Se impostata solo la data finale, si comporta come un 'fino a'. Se impostata solo la data iniziale si comporta come un 'da'
* Ora iniziale e finale. Filtra tutti recordo nel range specificato. Se impostata solo l'ora finale, si comporta come un 'fino a'. Se impostata solo l'ora iniziale si comporta come un 'da'
* Utente applicativo. è l'utente che ha lanciato i programmi di scrittura su coda
* Errori. é un flag che se specificato estrae solo i record con errori
* Funzione K64 e Metodo K64. Filtra su determinati funzioni e metodi della K64
* Coda Dati. Filtra su una specifica coda dati
* Ambiente. Filtra la scrittura sulle code dati da uno specifico ambiente
* Programma.  Filtra la scrittura sulle code dati da parte di uno specifico programma
* Device.  Filtra la scrittura sulle code dati da uno specifico device
* Sessione.  Filtra la scrittura sulle code dati da una specifica sessione
* Testo presente e non presente. effettua dei filtri sul campo che contiene i dati.


## La scheda di controlli di sistema
Grazie a questa scheda è possibile verificare la corretta configurazione dell'ambiente ed il corretto funzionamento dei componenti utilizzati
In particolare è possibile vedere : 
* **Il programma impostato per l'invio.** Rappresenta il programma specifico utilizzato per gestire l'invio dell'XML al SdI. Il programma utilizzato rispetta la seguente sintassi :  V5_061A_XX dove XX rappresenta il suffisso del programma caricato in tabella V50 (campo T$V50O   Pgm invio ft a SdI)
* **Verifica dei parametri di comunicazione.** Specificati in tabella EDC, rappresentano i parametri di comunicazione per il provider. Ne sono presenti due, uno per l'autenticazione ed uno per la trasmissione. Entrambi puntano a specifiche sezioni dello script di configurazione LOA38_61. In caso d'errore, verificarne l'esistenza e la presenza delle sezioni richiamate.
* **Verifica congruenza ambiente con metodi di comunicazione.** Verifica la congruenza tra l'ambiente nel quale si è entrati ed i metodi di comunicazione utilizzati (ambiente di test con webservice di test e ambiente di produzione con webservice di produzione).
* **Controllo Provider.** Controlla che la coda provider di comunicazione con il webservice sia attiva
* **Controllo User e Password.** Controlla la presenza dei parametri di collegamento caricati sull'azienda (B£2) nell'estensione £56 (Utente e password)
* **Controllo Aooid.** Controlla la presenza del parametro Aooid caricato sull'azienda (B£2) nell'estensione £56
***Versione pacchetto Fatturazione Elettronica : ** indica la data di rilascio dell'ultimo Savf della fatturazione elettronica installato
***Criterio di completamento : **una volta lanciata la funzione con il bottone in basso a destra, espone l'esito dei controlli di completamento. Questa funzione effettua un controllo dell'impianto tabellare e sistemistico dell'installazione per garantirne il corretto funzionamento.

In caso non si fosse in possesso dell'Aooid (obbligatorio per la trasmissione delle fatture ad Abletech) è possibile richiederlo attraverso il pulsante in fondo alla scheda.
In casi di configurazione di test, il sistema utilizza dei parametri di collegamento al Webservice di demo, memorizzati all'interno dei programmi.

## La scheda del provider
Grazie a questa scheda è possibile verificare la impostazioni relative al provider definito in tabella V50.
Le informazioni inerenti alla fatturazione elettronica da controllare sono le seguenti voci di menù : 
* **Stato.** Sono descritti le informazioni principali riguardanti il provider tra cui data e ora di avvio, AS400 a cui è collegato, Utente e ambiente con cui viene lanciato e il nome della coda.
* **LOA38.** E' importante controllare che venga letto e caricato correttamente il LOA38 realtivo all'Interfaccia intermediari Sdi, in modo da assicurarsi che le impostazioni per la comunicazione della fatturazione elettronica siano coerenti. **Questo è verificabile controllando  che l'Albero Network abbia il nodo 61.**
