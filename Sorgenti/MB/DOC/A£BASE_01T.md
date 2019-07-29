## Trasferimento di un file da una libreria all'altra
### Trovare l'elenco dei file che voglio  copiare
Prima di procedere alla spiegazione dell'operazione specifica di copiatura, è necessario controllare i file che intendo copiare.
Per farlo, è utile il comando WO inizio_nome_file* (es. WO CA*), il quale mi apre l'elenco di programmi, file, librerie inizianti per questa parola.

Una volta stabilite le 2 librerie interessate, ovvero la libreria d'origine e quella di destinazione posso iniziare i lavori.

### Sottomissione lavori
Tutte le volte che si vanno a copiare dei file, è buona norma utilizzare il comando SBMJOB (Submit job), che sottomette il lavoro. Un lavoro avviato attraverso il comando SBMJOB utilizza
"Codice contabile" (ACFCDE) del lavoro che inoltra il lavoro. Le specifiche ACFCDE nella descrizione del lavoro (JOBD) e nel profilo utente (USRPRF) inoltrati vengono ignorate.

Dopo aver digitato il comando SBMJOB sulla linea di comandi dare F4 e di seguito utilizzare le istruzioni per la copia del file spiegate nel capitolo successivo.

### Comando di copia
Dalla schermata che si presenta per l'immissione dei lavori sottomessi, è necessario inserire il comando da eseguire nello spazio apposito.
Nel nostro caso il comando è CRTDUPOBJ permette di duplicare l'oggetto che andrò a specificare in un'altra libreria. Dopo aver digitato il comando con F4 passo alla schermata successiva
che mi permette di immettere le scelte di copia.

Devo inserire in nome dell'oggetto (per il file generalmente i primi 5 caratteri seguiti dall'asterisco es. CALBA* permettendo così di copiare oltre al file fisico anche i logici), la libreria di origine e quella di destinazione,
ed infine il tipo di oggetto, nel nostro caso *FILE.

Prima di confermare le scelte, con F10 mi compaiono altri campi, tra cui "Duplicazione dati" che va messo a SI in modo da copiare anche tutto quello che il file contiene.
Dopo aver compilato correttamente la videata, con un invio il programma dovrebbe tornare alla schermata dello SBMJOB.

ATTENZIONE :  Per quanto riguarda la coda lavori, è possibile sceglierne una in cui indirizzare con priorità il lavoro, nel nostro caso non cambieremo nulla, così finirà in quella di default.
Per coda di default si intende la cosa relativa all'utente che sta effettuando l'operazione.

Con un semplice invio partirà il lavoro.
Un lavoro (o job) è un oggetto di sistema ocme tale ha delle caratteristiche, queste caratteristiche possono essere predefinite da una "Job description" che è a sua volta un oggetto di sistema (per saperne di più GO CMDJOBD = Comandi descrizione lavoro).
Lo stesso stesso vale per la JOBQ che invece è la coda lavori in cui viene invece incanalata l'esecuzione del lavoro.

Per verificare che la copia sia stata eseguita correttamente, è necessario andare nell'ambiente in cui il file è stato copiato; dalla riga comandi digitare "F nomefile" e da qui verificare se la libreria è corretta. Poi con F15 verificare che il file si sia portato dietro i logici.
Infine con il comando F20 entro nella gestione delle query, dando invio senza filtrare posso vedere se sono stati copiati i dati.
