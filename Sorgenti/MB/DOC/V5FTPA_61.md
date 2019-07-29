# Il Cruscotto di Invio Fatture

## Operatività
Il Cruscotto di Invio Fatture è lo strumento che permette l'invio delle fatture all'intermediario (es. Abletech) il quale si occuperà di inoltrare il flusso al Sistema di Interscambio (SdI) e gestire l'informazione di ritorno dell'esito dell'invio.
La scheda è richiamabile dalla voce di menù "Cruscotto invio fatture" del modulo V5FTPA "Fatturazione Elettronica"

Attualmente si compone di 7 sezioni : 

* La dashboard di riepilogo
* La scheda di invio ed il cruscotto d'avanzamento invio
* La scheda di visualizzazione dei tracciati (USRLVL 01)
* La scheda dei log di integrazione con il webservice (USRLVL 02)
* La scheda del log della coda dati (USRLVL 02)
* La scheda di controlli di sistema
* La scheda del provider (USRLVL 02)

**Prerequisito all'invio è l'impostazione di alcuni parametri la cui mancata o non corretta compilazione sarà segnalata direttamente nel cruscotto sopra le linguette di selezione delle 6 sezioni sopra elencate.
Nel caso di parametri mancanti o di componenti necessari non correttamente configurati, sarà opportuno verificare il problema tramite la tab "Controllo di sistema" e correggerlo prima di effettuare l'invio.


### La dashboard di riepilogo
In questa dashboard è presente un grafico a barre di riepilogo sullo stato di invio delle fatture elettroniche.
Su ogni record di EDSEND utilizzato per l'invio, infatti, è presente l'indicazione dello stato dell'invio della fattura stessa.

Al momento, gli stati possibili sono 6 : 

* **0** - Da elaborare :  Rappresentano le fatture per le quali non è ancora stato generato l'XML
* **1** - XML errato :  Rappresentano quelle fatture per le quali l'XML è stato generato ma presenta errori formali ed quindi necessario ricreare l'XML in questione, dopo aver controllato le stampe di errore e aver sistemato le cause.
* **2** - Da inviare :  Sono le fatture con XML generato e pronte per essere inviate
* **3** - Invio in corso :  sono le fatture per cui è stata lanciata la procedura di invio, ma che sono ancora in attesa di essere trasmesse.
* **4** - Errore nell'invio :  Sono quelle fatture per le quali è stato tentato l'invio ma è fallita la trasmissione all'intermediario.
* **5** - Inviate :  Sono le fatture correttamente trasmesse e ricevute dall'intermediario

La dashbord riepilogativa in questione mostra, in forma di grafico a barre, il numero complessivo di fattura con XML errato e quelle in attesa di essere inviate.


### La scheda di invio
Questa scheda permette di avere un riepilogo generale su tutte le fatture estratte (inviate, da inviare, in errore, etc...) mediante l'impostazione dei filtri nonché di procedere materialmente all'invio delle fatture stesse.
I filtri selezionabili, anche in abbinamento, sono : 
* **Tipo selezione**. Permette di filtrare sugli stati di invio visti al punto precedente
* **Data iniziale e finale**. Filtra tutte le fatture la cui data fattura è nel range specificato. Se impostata solo la data finale, si comporta come un 'fino a'. Se impostata solo la data iniziale si comporta come un 'da'
* **Tipo ente fattura** e **codice ente fattura**. Corrispondono all'ente di fatturazione dei documenti da cui è composta la fattura.
* Registro iva
* **Numero fattura da** e **numero fattura a**. Filtra, con lo stesso criterio sopra espresso per le date, sul numero fattura
* **Anno**. E' l'anno di emissione della fattura

L'unico filtro obbligatorio è il tipo selezione, che condiziona anche le azioni eseguibili sull'elenco di fatture che verrà estrapolato.
Risulta infatti abilitato il pulsante per la trasmissione solo per le selezioni 'Da inviare' e 'Errore nell'invio'.
Una volta eseguito il filtro, comparirà l'elenco delle fatture che soddisfano i requisiti sopra impostati. Sono visibili tutte le principali informazioni riepilogative delle fatture e lo stato dell'invio.
Se impostato un tipo selezione che consente l'invio, nella matrice sarà visibile come prima colonna la spunta di selezione della fattura stessa.
E' possibile selezionare o deselezionare singolarmente le fatture oppure mediante i due pulsanti 'Seleziona tutto' e 'Deseleziona tutto' effettuare la sezione/deselezione di massa. Ovviamente saranno soggette ad invio le sole fatture selezionate.
L'invio delle fatture avviene tramite sottomissione batch del lavoro (pulsante 'Trasmetti (BATCH)' della scheda). Una volta lanciato l'invio verrà aperto un nuovo cruscotto che riepilogherà in tempo reale lo stato dell'invio con un grafico e con una matrice delle singole fatture da inviare.
Tale cruscotto è descritto nel paragrafo a seguire.

E' inoltre possibile visualizzare il contenuto del tracciato della fattura. Può essere utile in caso di errori o incongruenze.
Cliccando infatti sulla lente d'ingrandimento si accederà infatti ad una specifica sezione in cui sarà possibile visualizzare in dettaglio il contenuto dei dati estratti, suddiviso per tracciato. Sono tutte le informazioni che verranno trasmesse e che sono contenute nel file XML estratto.

### Il cruscotto d'avanzamento invio fatture
Una volta avviato l'invio in batch delle fatture selezionate verrà aperto la dashboard di riepilogo sull'avanzamento dell'invio.
La dashboard è suddivisa in due sezioni :  a sinistra troviamo il grafico ed a destra l'elenco delle fatture presenti nell'invio in corso.

Il grafico a torta, con refresh automatico ogni 20 secondi, mostra : 

* In grigio la porzione di fatture in attesa di essere inviate
* In verde la porzione di fatture inviate per le quali è stato restituito l'esito di invio positivo
* In rosso la porzione di fatture inviate per le quali è stato restituito l'esito di invio negativo

E' possibile forzare il refresh cliccando sulla barra del titolo del grafico.
Il grafico mostra, come etichetta, la percentuale per ogni porzione mentre sotto al grafico è presente una piccola tabella riepilogativa che fornisce le stesse informazioni del grafico ma in termini numerici.
Sulla parte destra della dashboard è invece presente l'elenco delle fatture in elaborazione con i dati essenziali e riepilogativi delle fatture stesse. Inizialmente è visibile l'elenco completo, ma cliccando sugli appositi pulsanti sopra le intestazioni della matrice è possibile selezionare anche solo quelle in attesa dell'invio, quelle già trasmesse o quelle per le quali si è verificato un errore durante l'invio.
Un'icona all'inizio di ogni riga, comunque, restituirà l'informazione relativa allo stato dell'invio. Questa matrice non è in aggiornamento automatico. Per aggiornare la matrice è sufficiente agire sui pulsanti sopra la matrice stessa.
Questa scheda non verrà chiusa al termine dell'esecuzione dell'invio ma andrà chiusa manualmente (quando dal grafico si evincerà che non sono più presenti fatture in attesa di invio).
Si è scelto di non chiudere la scheda anche per consentire un analisi sulla matrice di riepilogo dell'invio.

**N.B. :  La chiusura anticipata della dashboard non pregiudicherà né interromperà il processo d'invio, che proseguirà in bacth. L'esito dell'invio, peraltro, può comunque essere visualizzato dalla scheda di partenza (quella di selezione delle fatture per l'invio) agendo sugli appositi filtri di selezione.

A chiusura della dashbord della scheda di riepilogo, si verrà riportati nella scheda di selezione delle fatture da inviare, aggiornandone il contenuto.

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

