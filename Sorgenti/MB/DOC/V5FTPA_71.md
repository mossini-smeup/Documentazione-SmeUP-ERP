# Cruscotto esito fatture

## Operatività
Il Cruscotto esito fatture è lo strumento che permette all'utente di mantenere sotto controllo la situazione delle fatture emesse una volta effettuato l'invio al Sistema di Interscambio (SdI) dell'Agenzia delle Entrate.
La scheda è richiamabile dalla voce di menù "Controllo Esiti" del modulo V5FTPA "Fatturazione Elettronica".

Verranno qui presentate una serie di funzionalità di seguito descritte.

### Situazione Esiti
In questa scheda è presente l'elenco dei documenti inviati al SdI e che sono ancora in uno stato transitorio.

Vengono considerate fatture in stato transitorio : 
* Fatture di cui non è conosciuto l'esito (valore 1)
* Consegnata ad SDI (valore A). Quando c'è di mezzo un intermediario, questo stato indica il fatto che la fattura ha passato i controlli dell'intermediario ed è stata veicolata all'SDI.
* Scartate (valore 2). Scartata non è considerato come uno stato definitivo in quando sarà necessario verificare il motivo dello scarto ed operare poi in modo opportuno al fine di gestire il problema.
* Rifiutata da ufficio PA (valore 6). Valgono le medesime considerazioni del punto precedente.
* Mancata consegna a ufficio PA (valore 3) e Impossibilità recapito (8). Questi stati dovranno evolvere negli stati X e Y, che indicano il fatto l'emissione delle fatture è stata notificata al cliente. Per il passaggio a tale stato c'è l'apposita voce che verrà a descritta a seguire, ma nulla vieta di sviluppare anche specifiche procedure interne atte a gestire tale indicazione.

Sono invece considerati stati definitivi : 
* Consegnata a destinatario (valore 4)
* Accettata da ufficio PA (valore 5)
* Decorrenza termini (valore 7)
* Notificata da mancata consegna PA (valore X)
* Notificata da impossibilità recapito (valore Y)

In alto è presente un grafico a torta che rappresenta un riepilogo sulla situazione in cui si trovano le fatture già trasmesse all'intermediario o al Sistema di Interscambio, accanto al grafico troviamo i valori dai quali è composta e che vengono acquisiti dalla matrice sottostante.

In alto a sinistra, al grafico viene riportata la possibilità, tramite bottoni di : 
* di lanciare la procedura di aggiornamento immediato degli esiti (con evidenza dell'ultimo momento in cui questo è stato effettuato)
* di lanciare la gestione della spunta notifica delle fatture non recapitate (funzione che verrà descritta a seguire).

In basso è presentato il dettaglio delle fatture che sono sintetizzate nel grafico.
L'elenco delle fatture è raggruppato per tipologia di esito ed il documento viene descritto all'interno delle seguenti colonne : 

* Codice ente, è il codice del destinatario documento;
* Ragione sociale, è la ragione sociale del destinatario documento;
* Partita IVA, è la P.IVA del destinatario documento;
* Codice fiscale, è il codice fiscale del destinatario documento;
* Registro IVA, è il registro IVA sul quale il documento è protocollato;
* Numero fattura, è il numero del documento;
* Data fattura, è la data del documento;
* Importo, è l'importo del documento;
* Esito, è lo stato in cui si trova il documento dopo essere stato inviato al Sistema di Interscambio;

Le colonne seguenti descrivono attraverso una rappresentazione a "semaforo" la situazione del documento.

* Creazione XML, se rosso indica che l'xml del documento è stato generato con errori, se invece è verde indica che l'xml del documento è stato generato senza problemi. Quando il semaforo è giallo l'xml è in fase di elaborazione;
* Invio, se rosso indica che l'xml del documento è stato inviato con errori al Sistema di Interscambio, se invece è verde indica che l'xml del documento è stato inviato senza problemi all'SdI. Quando il semaforo è giallo l'xml è in fase di invio;
* Ricevuto SDI, se rosso indica che il SdI ha avuto problemi nel ricevere l'xml, se invece è verde indica che l'xml del documento è stato ricevuto senza problemi. Quando il semaforo è giallo il SdI non ha ancora comunicato se l'xml è arrivato a destinazione o se ha avuto problemi legati all'incorrettezza dell'xml oppure all'impossibilità di consegnare al nostro cliente il documento;
* Ricevuta consegna, se rosso indica che il SdI ha constatato che l'xml è formalmente errato, se invece è verde indica che l'xml del documento è corretto e consegnato al cliente, in questo caso la riga di questo documento verrà spostato nella scheda "Storico documenti". Quando il semaforo è giallo il SdI ha ricevuto l'xml ma non ho ancora la ricevuta della consegna;
* Mancata consegna, se rosso indica che il SdI ha constatato che l'xml è formalmente errato, se invece è verde indica che l'xml del documento è corretto e consegnato al cliente, in questo caso la riga di questo documento verrà spostato nella scheda "Storico documenti". Quando il semaforo è giallo il SdI ha ricevuto l'xml ma non ho ancora la ricevuta della consegna;

### Lancio procedura aggiornamento esiti
Lanciando questa procedura verrà richiesta un ulteriore conferma di esecuzione.
Confermando verrà aperto la dashboard di riepilogo sull'avanzamento dell'aggiornamento.
La dashboard è suddivisa in due sezioni :  a sinistra troviamo il grafico ed a destra l'elenco delle fatture in elaborazione (tutte le fatture che non hanno un esito definitivo).

Il grafico a torta, con refresh automatico ogni 20 secondi, mostra : 

* In grigio la porzione di fatture in attesa di essere elaborate
* In verde la porzione di fatture elaborate per le quali l'aggiornamento è andato a buon fine
* In rosso la porzione di fatture elaborate per le quali l'aggiornamento non è andato a buon fine

E' possibile forzare il refresh cliccando sulla barra del titolo del grafico.
Il grafico mostra, come etichetta, la percentuale per ogni porzione mentre sotto al grafico è presente una piccola tabella riepilogativa che fornisce le stesse informazioni del grafico ma in termini numerici.
Sulla parte destra della dashboard è invece presente l'elenco delle fatture in elaborazione con i dati essenziali e riepilogativi delle fatture stesse. Inizialmente è visibile l'elenco completo, ma cliccando sugli appositi pulsanti sopra le intestazioni della matrice è possibile selezionare anche solo quelle in attesa di elaborazione, quelle già elaborate o quelle per le quali si è verificato un errore durante l'elaborazione.
Un'icona all'inizio di ogni riga, comunque, restituirà l'informazione relativa allo stato dell'invio. Questa matrice non è in aggiornamento automatico. Per aggiornare la matrice è sufficiente agire sui pulsanti sopra la matrice stessa.
Questa scheda non verrà chiusa al termine dell'esecuzione dell'invio ma andrà chiusa manualmente (quando dal grafico si evincerà che non sono più presenti fatture in attesa di invio).
Si è scelto di non chiudere la scheda anche per consentire un analisi sulla matrice di riepilogo dell'elaborazione.

**N.B. :  La chiusura anticipata della dashboard non pregiudicherà né interromperà il processo d'invio, che proseguirà in batch. L'esito dell'invio, peraltro, può comunque essere visualizzato dalla scheda di partenza (quella di selezione delle fatture per l'invio) agendo sugli appositi filtri di selezione.

A chiusura della dashboard della scheda di riepilogo, si verrà riportati nella scheda di selezione della situazione esiti, aggiornandone il contenuto.

### Spunta fatture non recapitate
Lanciando questa scheda si avrà la possibilità di gestire manualmente l'indicazione del fatto che il cliente intestatario di una fattura non recapitata sia stato effettivamente informato dell'emissione della fattura. Tale indicazione farà si che la fattura scompaia dalla scheda situazioni esiti.

Nella scheda vengono presentate due sezioni : 
* Spunta Notifica Fatture Non Recapitate :  presenta solo le fatture che non risultano notificate. Da qui sarà possibile in modo immediato andare a spuntare quelle per cui il cliente è stato informato. La modifica è definitiva.
* Controllo Storico :  presenta solo le fatture già spuntate e permette di effettuare un eventuale controllo o anche di annullare un'eventuale spunta erroneamente attribuita.

### Interrogazione storico
E' un interrogazione che mostra un dettaglio molto simile a quelle presente nella situazione esiti, con la sola differenza che è possibile interrogare tutto lo storico delle fatture con l'evidenza dello stato attuale (che sia definitivo o meno).

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

