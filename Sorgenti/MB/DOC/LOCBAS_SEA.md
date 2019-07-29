# Esempio di architettura Looc.Up in una installazione client-server completa

In questo documento verrà mostrato un esempio completo di architettura Looc.Up client-server, con tutti gli elementi che possono entrare in gioco. Verranno inoltre illustrate le modalità che regolano la comunicazione tra i vari elementi del sistema e spiegato come è possibile inviare comandi e funzioni alle varie entità.

# Struttura client-server complessa di esempio

La seguente immagine mostra la struttura della rete client server di esempio che andremo ad analizzare : 

![LOCBAS_027](http://localhost:3000/immagini/LOCBAS_SEA/LOCBAS_027.png)

 T(Andiamo ora ad analizzare in dettaglio gli elementi che compongono questa rete client-server di esempio : )
- La rete è composta da 3 macchine fisiche, denominate PC1, PC2 e PC3, da una macchina server, denominata PCSERVER e da un sistema AS400. Le singole macchine sono identificate dai rettangoli rossi tratteggiati.
- Sulla macchina PC1 è attivo un Looc.Up avviato in modalità normale, quindi connesso solo al sistema AS400 attraverso le code di comunicazione
- Sulla macchina PCSERVER è attivo un Looc.Up Server, identificato dal codice LOSRVA. Il server di Looc.Up è connesso al sistema AS400 con le code di comunicazione tipiche di un qualsiasi client Looc.Up (freccia bianca) ed è in ascolto delle richieste provenienti da AS400 su una coda specifica dedicata a tal scopo (freccia in giallo nel disegno).
- Il Looc.Up Server ha due serventi attivi (oggetti V3-CSE). Il primo è identificato dal codice SRVA ed è un servente generico. Il secondo è invece identificato dal codice riservato BATCH ed è il servente che si occupa della esecuzione delle richieste di tipo batch.
- Sulla macchina PC3 è attivo un Looc.Up avviato in modalità client. Questo Looc.Up è connesso al sistema AS400 e al server Looc.Up, dal quale è riconosciuto con il codice univoco LOCCLB
- Anche sulla macchina PC2 è attivo un Looc.Up avviato in modalità client. Questo Looc.Up è riconosciuto dal server con il nome univoco LOCLIA. Su questo client è anche attivo un servente locale identificato dal codice SRVB.


# Come individuare il destinatario di una funzione

Come già noto, all'interno di una istanza di Looc.Up l'esecuzione di qualsiasi azione passa dall'esecuzione di una funzione, codificata con la nota struttura funizzata, del tipo : 

F(XX;YY;ZZ) 1(T1;P1;K1) 2(T2;P2;K2) 3(T3;P3;K3) 4(T4;P4;K4) 5(T5;P5;K5) 6(T6;P6;K6) P()

Se non viene specificato nulla la funzione viene eseguita dall'istanza di Looc.Up stesso.

E' però possibile alterare la normale esecuzione della funzione andando a specificare due ulteriori campi.

## Selezione del servente

E' possibile fare in modo che una particolare funzione non venga eseguita dal sistema AS400 ma venga eseguita da un servente registrato sull'istanza di Looc.Up. Il servente è un oggetto di tipo V3-CSE ed è specificato nel campo SERVER della funzione.
La struttura della funzione è quindi la seguente : 

F(XX;YY;ZZ) 1(T1;P1;K1) 2(T2;P2;K2) 3(T3;P3;K3) 4(T4;P4;K4) 5(T5;P5;K5) 6(T6;P6;K6) P() **SERVER(COD_SERVENTE)**

Ad esempio, nella nostra struttura se sul client Looc.Up LOCLIA viene richiesta la funzione : 

F(XX;YY;ZZ) 1(T1;P1;K1) P() **SERVER(SRVB)**

la funzione viene sempre eseguita sul client LOCLIA ma il servizio non viene richiesto all'AS400 ma al servente SRVB, attivo sul client stesso.

Se una funzione viene richiesta ad un servente non esistente o non attivo, viene segnalato un errore e la richiesta di esecuzione viene abortita.

## Selezione del client

All'interno di una rete di tipo client server, è possibile far eseguire una funzione ad una istanza di Looc.Up diversa da quella attuale. Nell'esempio in figura è quindi possibile che il client LOCLIA attivo sulla macchina PC2 possa richiedere un servizio o una funzione ad un client LOCLIB attivo su un'altra macchina (in questo caso PC3).

Questa cosa è possibile specificando il campo CLIENT nella funzione : 

F(XX;YY;ZZ) 1(T1;P1;K1) 2(T2;P2;K2) 3(T3;P3;K3) 4(T4;P4;K4) 5(T5;P5;K5) 6(T6;P6;K6) P() **CLIENT(COD_CLIENT)**

questo formato richiede l'esecuzione della funzione sul client remoto COD_CLIENT.

Ad esempio, se sul client LOCLIB richiediamo la funzione : 

F(XX;YY;ZZ) 1(T1;P1;K1) P() **CLIENT(LOCLIA)**

otterremo l'effetto di avviare remotamente da LOCLIB una funzione sul client LOCLIA.

E' anche possibile richiedere l'esecuzione di un servizio ad un client remoto :  la differenza tra richiesta di funzione e richiesta del servizio sta nella risposta. Con una richiesta di funzione si chiede che il client remoto esegua una certa azione per cui non è prevista una risposta. La richiesta di servizio invece prevede che il chiamante riceva una risposta in formato XML da parte del client remoto.

Per invocare una funzione remota come servizio è sufficiente inserire il codice XML come programma di invocazione della funzione.
Quindi : 

F(**XML**;YY;ZZ) 1(T1;P1;K1) 2(T2;P2;K2) 3(T3;P3;K3) 4(T4;P4;K4) 5(T5;P5;K5) 6(T6;P6;K6) P() **CLIENT(COD_CLIENT)**

 T(Vediamo alcune osservazioni molto importanti : )
- Sia l'istanza di Looc.Up richiedente il servizio che quella che lo fornisce devono essere istanze di Looc.Up di tipo client attive e registrate sul server
- L'istanza richiedente e quella fornitrice del servizio possono stare sulla stessa macchina fisica o su macchine diverse.
- Anche Looc.Up server è registrato come client sulla rete, con il codice predefinito SERVER. Pertanto un qualsiasi Looc.Up client può richiedere una qualsiasi funzione al server specificando il parametro CLIENT(SERVER)
- Anche un Looc.Up avviato in modo normale e non registrato come client sul server Looc.Up può comunque richiedere l'esecuzione di una funzione del server Looc.Up. E' sufficiente specificare il paramentro CLIENT(SERVER.CODSRV), dove CODSRV è il codice del server che deve ricevere la richiesta. In questo caso però il client non può ricevere alcuna risposta.


## Selezione combinata di client e servente

All'interno della funzione è possibile specificare contemporanemamente sia il campo SERVER che il campo CLIENT.
**In questo caso specifico viene prima elaborato e gestito il campo CLIENT e successivamente il campo SERVER.

Per capire a fondo il comportamento vediamo un esempio, riferito alla struttura mostrata in figura.
Supponiamo di avere la funzione : 

F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(LOCLIA) SERVER(SRVB)

richiesta sul client LOCLIB

 T(La funzione viene gestita nei seguenti passi : )
- Il client LOCLIB registra la richiesta di funzione, vede che il campo CLIENT è valorizzato e capisce che la funzione non deve eseguirla lui ma un client diverso.
- Il client LOCLIB spedisce la funzione al server LOSRVA perchè la recapiti al client che la deve eseguire
- Il server LOSRVA cerca tra i client collegati quello identificato dal codice LOCLIA
- Una volta individuato il client, gli viene spedita la richiesta di funzione F(XX;YY;ZZ) 1(T1;P1;K1) SERVER(SRVB), cioè la funzione originaria senza campo CLIENT
- Il client LOCLIA riceve la funzione e si accorge che ha un campo SERVER definito. Cerca quindi tra i suoi serventi registrati quello che ha codice SRVB.
- Al servente SRVB attivo sul client LOCLIA viene inviata la richiesta di funzione F(XX;YY;ZZ) 1(T1;P1;K1), cioè la funzione originaria senza i campi di indirizzamento.
- Se la funzione originaria è una richiesta di servizio (cioè è di tipo F(EXB..), il servente SRV fornisce la risposta XML al client LOCLIA che, sempre attraverso la mediazione del server LOSRVA, la spedisce al richiedente originario, cioè il client LOCLIB


In altre parole, la funzione : 

F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(LOCLIA) SERVER(SRVB)

quando eseguita in una rete client-server come da nostro esempio può essere intesa come : 

"Richiedi remotamente al servente SRVB attivo sul client Looc.Up identificato dal codice LOCLIA la funzione F(XX;YY;ZZ) 1(T1;P1;K1)"


# Richiesta di esecuzione di una funzione batch sul server

Un caso particolare, è la richiesta di esecuzione di una funzione batch sul server. Per capire cos'è una funzione batch e come si possano gestire questa tipologia di funzioni, fare riferimento alla documentazione specifica. Per gli scopi di questo documento è sufficiente sapere che una funziona batch è una funzione che può essere eseguita in un ambiente non presidiato (non richiede interazione con l'utente) e quindi demandata ad un sistema terzo per evitare che la sua esecuzione possa interferire con il lavoro attuale.

Una delle funzionalità previste dal Looc.Up server è appunto quella di eseguire funzioni non presidiate. Per implementare questa funzionalità, il server attiva uno speciale servente identificato dal codice riservato **BATCH** e abilitato in modo automatico ogni volta che un Looc.Up viene avviato in modalità server.

**Il servente speciale BATCH può essere attivato come qualsiasi altro servente ma può girare solo su un Looc.Up di tipo server. Pertanto perchè sia possibile lanciare esecuzioni di funzione batch è necessario che nella rete ci sia almeno un server Looc.Up attivo.

Per capire il funzionamento della sottomissione di richieste batch vediamo un esempio riferito alla nostra struttura.

Supponiamo che il client LOCLIB attivo sulla macchina PC3 abbia la necessità di eseguire una funzione F(XX;YY;ZZ) 1(T1;P1;K1) lenta, la cui esecuzione non richiede interazione con l'utente. La funzione deve qundi essere eseguita sul server LOSRVA, all'interno del servente BATCH dedicato a questo tipo di esecuzioni.

 T(Pertanto è necessario aggiungere alla funzione originaria due informazioni : )
- Quale Looc.Up deve eseguire la funzione :  in questo caso l'esecutore è il server quindi è sufficiente aggiungere alla funzione la notifica CLIENT(SERVER), ricordando che il server stesso è uno dei client interpellabili ed è identificato dal codice fisso SERVER.
- Chi esegue la funzione batch :  è il servente BATCH, quindi alla funzione originaria occorre aggiungere la notazione SERVER(BATCH)


La funzione originaria, da eseguire sul client LOCLIB diventa quindi : 

F(XX;YY;ZZ) 1(T1;P1;K1) **SERVER(BATCH) CLIENT(SERVER)

Con questa notazione la richiesta F(XX;YY;ZZ) 1(T1;P1;K1) viene ricevuta dal servente BATCH attivo sul server LOSRVA, cioè il server a cui  è collegata la macchina LOCLIB su sui era stata invocata la funzione.

 T(Il servente BATCH esegue la funzione richiesta nel seguente modo : )
- Il servente BATCH avvia sul server stesso un Looc.Up client chiamato "Processo Batch" con l'ambiente richiesto per l'esecuzione della funzione batch
- Appena avviato, il client "Processo batch" si collega al server e all'AS400 e si comporta come un qualsiasi Looc.Up client connesso al server
- Non appena il server LOSRVA si accorge che il processo batch si è attivato gli invia la richiesta di esecuzione della funzione da eseguire come batch, cioè la F(XX;YY;ZZ) 1(T1;P1;K1)
- Il processo bacth esegue la funzione e non appena terminata notifica al server la fine esecuzione e l'eventuale risposta
- Il server riceve la notifica di fine esecuzione. Chiude il client "Processo Batch" e spedisce l'eventuale risposta al client che aveva richiesto l'esecuzione della funzione.



La sottomissione di una funzione come batch può avvenire anche da un Looc.Up non avviato come client, come l'istanza attiva sul PC1 in figura.

Basta eseguire la funzione come : 

F(XX;YY;ZZ) 1(T1;P1;K1) **SERVER(BATCH) CLIENT(SERVER.LOSRVA)**

In questo caso è possibile inviare la richiesta al server ma non è possibile ricevere una risposta .

# Invio di richieste da AS400 al server Looc.Up

Come già detto in precedenza, una delle caratteristiche del server Loo.Up è quella di creare delle code di comunicazione verso AS400 sulle queli si mette in attesa per la ricezione di comandi.

 T(Le code di comunicazione AS400-Looc.Up server sono create automaticamente all'avvio del server e sono : )
- **ESTC + NOMESERVER** :  coda che consente l'invio di richieste da AS400 verso Looc.Up server. Su questa coda il Looc.Up server è in attesa di ricevere le richieste di funzione. E' una coda normale.
- **ECTS + NOMESERVER** :  coda di risposta. Su questa coda il sistema AS400 si deve mettere in attesa di una risposta dopo aver richiesto un servizio. E' una coda a chiave.


Come si nota, la coda di richiesta  una coda normale mentre la coda di risposta è un coda a chiave. Questa cosa è necessaria per avere un funzionamento asincrono della comunicazione, cioè fare in modo che il sistema AS400 possa richiedere più funzioni contemporaneamnete e non dover aspettare la risposta dopo ogni richesta inviata.

 T(Il meccanismo con cui il sistema AS400 può richiedere una funzione al server è il seguente : )
- Supponiamo che il sistema AS400 debba richiedere al server LOSRVA la funzione F(XX;YY;ZZ) 1(T1;P1;K1)
- Il sistema AS400 scriverà sulla coda ESTCLOSRVA la funzione F(XX;YY;ZZ) 1(T1;P1;K1) 6(;;123456). Da notare che nel campo codice 6 è stato inserito un codice 123456 che è il codice univoco della richiesta. In pratica il sistema AS400 assegna una chiave alla richiesta. Il formato della richiesta è basato sulla stessa DS che Looc.Up invia al sistema AS400 quando richiede servizi. Dopo aver inviato la richiesta, il sistema AS400 si mette in ascolto della coda di risposta ECTSLOCRVA in attesa della risposta con chiave 123456.
- Il Looc.Up serve esegue la funzione (o demanda l'esecuzione al client a cui è diretta) e alla fine risponde su coda ECTSLOSRVA marcando la risposta con chiave 123456
- Il sistema AS400 riceve la risposta e considera chiusa la richiesta


Da notare che il sistema AS400 può inviare al Looc.Up server qualsiasi funzione. Pertanto può richiedere funzioni che possono essere eseguite dal server stesso, oppure utilizzando i campi CLIENT e SERVER può fare in modo che la funzione venga eseguita su un client connesso al Looc.Up server.

Ad esempio, se il sistema AS400 inviasse al server la funzione F(XX;YY;ZZ) 1(T1;P1;K1) 6(;;123456) CLIENT(LOCLIA) SERVER(SRVB) otterrebbe come effetto di richiedere l'esecuzione della funzione F(XX;YY;ZZ) 1(T1;P1;K1) al servente SRVB attivo sul client LOCLIA .


# Esempi


- Dal client LOCLIA richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul client LOCLIB : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(LOCLIB)**


- Dal client LOCLIB richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul servente SRVB attivo sul client LOCLIA : 

 **F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(LOCLIA) SERVER(SRVB)**


- Dal client LOCLIA richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul server LOSRVA : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER)**


- Dal client LOCLIA richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul servente SRVA attivo sul server LOSRVA : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER) SERVER(SRVA)**


- Dal client Looc.Up attivo su PC1 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul server LOSRVA : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER.LOSRVA)**


- Dal client Looc.Up attivo su PC1 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul servente SRVA attivo sul server LOSRVA : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER.LOSRVA) SERVER(SRVA)**


- Dal client Looc.Up attivo su PC1 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul client LOCLIB : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER.LOSRVA.LOCLIB)**


- Dal client Looc.Up attivo su PC1 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul servente SRVB attivo sul client LOCLIA : 

**F(XX;YY;ZZ) 1(T1;P1;K1) CLIENT(SERVER.LOSRVA.LOCLIA) SERVER(SRVB)**


- Da AS400 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul server LOSRVA : 

**F(XX;YY;ZZ) 1(T1;P1;K1)** scritta su coda ESTCLOSRVA


- Da AS400 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul client LOCLIB : 

**F(XX;YY;ZZ) 1(T1;P1;K1)  CLIENT(LOCLIB)** scritta su coda ESTCLOSRVA


- Da AS400 richiedere l'esecuzione di una funzione F(XX;YY;ZZ) 1(T1;P1;K1) sul servente SRVB attivo sul client LOCLIA : 

**F(XX;YY;ZZ) 1(T1;P1;K1)  CLIENT(LOCLIA) SERVER(SRVB)** scritta su coda ESTCLOSRVA







