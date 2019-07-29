## Installazione Java vm
### Introduzione
Looc.up funziona su piattaforma Java della Sun Microsystem. Pertanto per il corretto funzionamento del programma è necessario che sul sistema sia presente e registrata una Java Virtual Machine (JVM) di versione corretta. L'installazione della JVM è necessaria sia nel caso di installazione client, sia nel caso di installazione di tipo client-server.

### Requisiti di sistema
I requisiti minimi di sistema consigliati per l'installazione di Looc.up sono i seguenti : 


- PC con processore Pentium IV o superiore.
- Almeno 512 Mbyte di memoria (consigliati 1 Gbyte o superiori)
- 300 Mbyte di spazio su disco disponibile.
- Sistema operativo
-- Windows 95 e Windows ME :  non supportati
-- WindowsNT con SP4 :  compatibile solo con versioni Looc.Up precedenti alla V3R1M101121
-- Windows2000 :  compatibile solo con versioni Looc.Up precedenti alla V3R1M101121
-- Windows 2000 Server :  compatibile solo con versioni Looc.Up precedenti alla V3R1M101121
-- Windows XP :  richiede service pack 3 per windows
-- Windows Vista :  richiede JVM in versione 1.6 o superiori
-- Windows 2003 server :  richiede JVM in versione 1.6 o superiori.
-- Windows 2008 server :  richiede JVM in versione 1.6 o superiori, in versione a 32 bit anche su sistemi a 64 bit.
-- Windows 7 :  richiede JVM in versione 1.6 o superiori, in versione a 32 bit anche su sistemi a 64 bit.
-- Linux :  Loocup non è disponibile in forma nativa per Linux. Può però essere eseguito all'interno di una macchina virtuale Windows.
-- Apple Mac :  Loocup non è disponibile in forma nativa per piattaforma MAc OS. Può però essere eseguito all'interno di una macchina virtuale Windows.
- Java Virtual Machine in versione 1.5.2 fino alla 1.6.0_02. Consigliata 1.6.02 o superiori (presente sul CD).
-- Per Windows Vista, Windows 2003, Windows 7 e Windows 2008 è richiesta una JVM in versione 1.6.0 o superiori.
-- Per sistemi operativi è a 64 bit, è comunque necessario utilizzare JVM a 32 bit. Looc.Up non funziona con JVM native a 64 bit.
-- Le versioni di Looc.Up a partire dalla V3R1M101121 non funzionano con la JVM 1.5 ma richiedono versioni 1.6 o superiori



### Verifica della Java Virtual Machine (JVM) Installata
**NOTA : ** Le versioni della JVM sono identificate da un numero di 3 cifre ad esempio 1.4.2 o 1.5.10. Dalla versione 1.5.0 la Sun (azienda produttrice della JVM) ha iniziato ad indicare la versione principale usando solo la seconda cifra.
Se pertanto si indica **versione 6.2** si avrà che il codice della versione è 1.6.2, analogamente alla versione**5.10** corrisponderà il codice **1.5.10**

Per verificare se sul pc è già installata una JVM utilizzate uno dei seguenti modi : 

-  Aprire il "Pannello di controllo" di Windows e fare doppio click sull'icona "JAVA". Cliccare su "Informazioni su" (tab Generale). Comparirà una finestra di dialogo che indicherà la versione. Sii troverà in alto una scritta del tipo "Java Platform Standard Edition 6" **Java 2 Runtime Enviroment ver. YYYY dove YYYY è la versione della Java Virtual Machine installata sul sistema.

![LOBASE_01](http://localhost:3000/immagini/LOBASE_031/LOBASE_01.png)
- Aprire il "Pannello di controllo" di Windows e selezionare la voce "Installazione applicazioni". Cercare nella lista di applicazioni installate sul sistema la voce :  **Java 2 Runtime Enviroment ver. YYYY  dove YYYY è la versione della Java Virtual Machine installata sul sistema.
- Aprire una shell DOS di sistema e inserire il comando :  **java -version**(java spazio meno version). Nel caso ci sia una JVM installata, la risposta sarà del tipo :  **java version "1.4.2_01" Java(TM) 2 Runtime Environment,
Standard Edition (build 1.4. Java HotSpot(TM) Client VM (build 1.4.2_01-b06, mixed mode) da cui si deduce la versione della JVM installata (1.4.2_01 nel caso in esempio) oppure del tipo **java version "1.6.0-oem"** Java(TM) SE Runtime Environment (build 1.6.0-oem-b104) Java HotSpot(TM) Client VM (build 1.6.0-oem-b104, mixed mode)

Se la JVM è già installata e la versione è adeguata al tipo di sistema operativo (vedi sezione requisiti del client per capire la versione corretta da usare) allora il pc è a posto e si può procedere all'installazione di Loocup (Cfr. Procedura di installazione Looc.up). In caso contrario passare al punto seguente.

### Installazione della Java Virtual Machine (JVM)
Per l'installazione di una JVM la procedura da seguire è la seguente : 

- Se sul sistema è già presente una JVM ma in versione anteriore alla 1.4.2 o posteriore alla 6.2  (nota anche come 1.6.2) richiesta da Looc.up, è necessario disintallare la vecchia versione prima di procedere con l'installazione della nuova JVM. Per far ciò, selezionare nella lista delle applicazioni installate la voce che si vuole disintallare e selezionare "rimuovi".
- Se sul sistema sono installate più JVM va disinstallata quella che risponde al comando **java -version
- Installare la JVM corretta. La JVM può essere scaricata gratuitamente dal sito della Sun Microsystem (http://java.sun.com). Per comodità, una copia della JVM è contenuta anche nel CD di installazione di Looc.up, all'interno della directory Java. Il file di installazione è :  _7_j2re-XXXX.exe, che una volta selezionato consente l'avvio della procedura automatica di installazione della JVM. Il setup proporrà durante la fase di installazione tutta una serie di opzioni dedicate ad utilizzatori esperti. Per un corretto funzionamento di Looc.up è sufficiente mantenere le opzioni proposte di default dalla procedura di installazione.


### Informazione Tecnica - Editor Xml.
Per chi sviluppa schede e o servizi, è fortemente consigliato che installi un apposito editor di documenti XML, questo perchè il supporto fornito da INTERNET EXPLORER non è sufficiente a coprire le esigenze. Con il CD di installazione di Loocup viene distribuito XMLMarker, un software free.
In alternativa il programma può essere scaricato al seguente indirizzo : 

 :  : DEC T(J1) P(PATHFILE) [http://www.download.com/XML-Marker/3000-7241-10202365.html?part=dl-XMLMarker&subj=dl&tag=button](http://www.download.com/XML-Marker/3000-7241-10202365.html?part=dl-XMLMarker&subj=dl&tag=button)

## Reperimento Oggetti Necessari
### In internet
Collegarsi al sito www.smeup.com o utilizzare il link seguente : 
[http://www.smeup.com/it/soluzioni/looc-up-download](http://www.smeup.com/it/soluzioni/looc-up-download)
 T(Sulla pagina in oggetto potete trovare)
- copia del CD di installazione (circa 580 MB)
- copia del setup (circa 90 MB)
- gli aggiornamenti (circa 10-30 MB)
- il setup della JVM (circa 40 MB)
- i setup e gli aggiornamenti di tutte le versioni precedenti di Looc.Up ancora supportate
- una copia di riferimento delle versioni precedenti di Looc.Up non più supportate


### Sul CD di installazione
Se non avete un CD di installazione potete crearne uno copiando quanto prelevato sul server o da internet

### Dalla DEV
Nella Smedev viene inserito l'ultimo Loocup stabile rilasciato. Utilizzare il comando UP UT3.

### Reperimento aggiornamenti
Vedi punti precedenti.

## Procedura Installazione
### Installazione di LoocUp di tipo client (o esclusiva)
E' la tipica installazione stand-alone. Con questa modalità di installazione, Looc.up deve essere installato su ognuna delle macchine su cui si intende utilizzarlo.
La procedura da seguire è la tipica procedura di installazione di un programma in ambiente Windows e si attesta su un programma automatico di setup che svolge tutte le operazioni necessarie per una corretta installazione del prodotto.
I passi da seguire sono i seguenti : 

- Disinstallare eventuali vecchie versioni di Looc.up presenti sulla macchina. **Non tentare mai l'installazione di una nuova versione senza aver prima disinstallato quella vecchia (vedi sotto).
- Avviare il programma _7_setup.exe presente nel CD di Looc.up
- Seguire le istruzioni a video proposte dal programma di installazione.
- Terminata la procedura di installazione, nel menu **Avvio ---> Programmi** di Windows sarà presente una nuova voce di menu Looc.up da selezionare per l'avvio del client grafico e dell'editor RPG.

Durante la procedura di installazione è possibile personalizzare alcuni parametri della installazione stessa (directory di installazione, link di avvio del programma, ecc. ecc.).
E' comunque possibile (e consigliabile) non variare i valori proposti di default.

### Disinstallare una eventuale installazione precedente
Per la disinstallazione, seguire la normale procedura Windows : 

- aprire il pannello di controllo
- selezionare **Installazione applicazioni**
- cercare la voce **Looc.up**
- selezionare **Rimuovi**


_2_NON INSTALLARE MAI LOOCUP SU UNA VERSIONE PRECEDENTE

### Installazione di tipo client-server
E' una forma installazione di tipo centralizzato, dove Looc.up viene posizionato su un unica macchina ed utilizzato in maniera condivisa da più client contemporaneamente attraverso una condivisione di rete.

Questa forma di installazione richiede la presenza nella rete di una macchina, che espleterà funzioni di "file server", di prestazioni sufficienti al carico di lavoro previsto. La soluzione client-server è consigliata soprattutto nei casi in cui si preveda l'utilizzo del client grafico Looc.up su un numero consistente di macchine. Centralizzando l'installazione in un unico punto è possibile mantenere un miglior controllo sulla distribuzione del prodotto ed assicurarsi in modo semplice che tutti gli utilizzatori usino la stessa versione. Inoltre alcune opzioni di personalizzazione come i Preferiti, la cronologia, le immagini gestite da Looc.up saranno sensibili all'utente e/o all'ambiente e/o al sistema del collegamento all'AS.

_3_NOTA; questo tipo di installazione richiede un server che esponga funzionalità di tipo File Server in quanto funge solo da deposito degli eseguibili e dei file temporanei/lavoro.
Loocup gira sul client pertanto il server potrebbe essere anche una macchina con sistema operativo linux o l'AS400 stesso.
L'installazione di Looc.up sull'IFS dell'AS400 è tuttavia sconsigliata in quanto l'IFS ha performance inferiori ad altri file system.

### Procedura Installazione di tipo  client-server
La procedura per l'installazione di Looc.up sul server è del tutto simile alla procedura descritta al capitolo precedente a riguardo della installazione di tipo client. Si
rimanda pertanto a questo punto per la procedura da seguire.
Scegliere con attenzione la directory del server su cui andrà installato il prodotto, ricordando che questa directory verrà condivisa in rete e dovrà essere visibile ed accessibile da tutti i client previsti in rete.

Di seguito vengono riportate le notizie relative alla configurazione delle autorizzazioni sulle cartelle della parte server.

**Installazione della parte client.**
La procedura di installazione della parte client di Looc.up dovrà essere eseguita su tutti i client su cui si prevede di utilizzare l'interfaccia grafica. L'operazione di installazione
del client è necessaria al corretto funzionamento del sistema e, di norma, una volta eseguita non dovrà più essere ripetuta anche a fronte di aggiornamenti della parte server. Uniche eccezioni potrebbero riguardare eventuali aggiornamenti strutturali del sistema.

**La procedura di installazione sul lato client è la seguente : **
Creazione del link al programma eseguibile di avvio di Looc.up, dislocato sul server.

I passi sono i seguenti : 

- Assicurarsi che il PC abbia risorse sufficienti al funzionamento di Looc.up e che abbia una Java Virtual Machine installata. Per questi due punti, fare riferimento al documento al paragrafo dove viene trattata l'installazione della Java vm.
- Creazione di un collegamento. Sul Desktop di Windows premere il tasto destro del mouse e selezionare la voce "Nuovo" - "Collegamento".
- Nella finestra di wizard proposta fare in modo che il collegamento che si sta creando punti al file LoocUp.exe presente nella directory del server su cui è stato installato Looc.up. Ovviamente perchè questo sia possibile è necessario che la directory del server che contiene Looc.up sia visibile da tutti i client. Il file da linkare è loocup.exe.
- Assegnare al collegamento creato il nome Looc.up e posizionarlo nella locazione che si ritiene più opportuna (Desktop di Windows, Menu di avvio o altro menù).
- Selezionare il collegamento appena creato. Se tutto è andato a buon fine deve comparire la maschera iniziale di avvio del programma.


### Le autorizzazioni sulle cartelle del server nell'installazione client-server
**Localizzazione dell'installazione**
Non installare in _7_C : \Programmi\Loocup come suggerito dal setup, che utilizza un default caratteristico dell'installazione standalone. Installarlo in una cartella o partizione fuori da quelle di sistema (Es :  _7_D : \Loocup o simili).

### Creazione della condivisione e autorizzazioni sulla stessa
Creare la condivisione Everyone --> Full Control, questo permette di accedere via rete a tutte le risorse dell'installazione, sottoponendosi però alle autorizzazioni che vengono impostate sul File System locale e di cui diremo di seguito : 

![share](http://localhost:3000/immagini/LOBASE_031/share.png)
### Impostazioni delle autorizzazioni sul File System
Per il Livello di protezione procedere come segue.
Nella cartella principale di installazione : 
![srvauth1](http://localhost:3000/immagini/LOBASE_031/srvauth1.png)ricordandosi di **togliere** il flag di eredità delle autorizzazioni dalla cartella padre.
Propagare a tutte le sottocartelle e files le autorizzazioni.
Ora passare alle sottocartelle e ad una ad una, ricordandosi di **togliere** il flag di eredità delle autorizzazioni dalla cartella padre, quelle che ne hanno bisogno e citerò di seguito, impostare la protezione come segue : 
![srvauth2](http://localhost:3000/immagini/LOBASE_031/srvauth2.png)Le cartelle su cui bisogna allargare il set di autorizzazioni poiché nel corso del programma possono dover essere "scritte" sono le seguenti :  LOOCUP_DAT, LOOCUP_CAH, LOOCUP_TMP, LOOCUP_WRK e LOOCUP_OUT.

### NOTA
Dopo aver completato l'installazione si può verificare la disponibilità di aggiornamenti collegandosi al sito www.smeup.com utilizzando il link seguente : 
[http://www.smeup.com/it/soluzioni/looc-up-download](http://www.smeup.com/it/soluzioni/looc-up-download)
Se è presente un'aggiornamento compatibile con la versione installata si può scaricare e copiare il contenuto dell'archivio nella cartella di installazione di LoocUp.

## Collegamento all'AS400
Una volta installato Looc.up sul client secondo le modalità precedenti avviare looc.up come una normale applicazione PC
Verrà visualizzata una finestra di collegamento dove si deve specificare : 
 * nome del sistema As400 (così come conosciuto dal client :  indirizzo IP o nome)
 * utente (vedi sezione LATO SERVER AS400)
 * password
 * codice ambiente

E' possibile anche specificare nel link di collegamento dei parametri aggiuntivi che mi permettono di predisporre delle risposte automatiche alle suddette domande. I parametri vengono riconosciuti in base all'ordine dei parametri stessi.
Quindi in questa modalità : 
- \\pathdirdiinstallaizone\Loocup.exe nomesistemaas400 utente password codiceambientesmeup

 :  : PAR F(01)
PORTE SOCKET NECESSARIE PER LA COMUNICAZIONE LOOCUP-AS400
---------------------------------------------------------
Per la corretta comunicazione tra il client grafico LoocUp e l'AS/400 è necessario che sulla linea di collegamento siano aperte le seguenti porte di comunicazione : 

Porta 449  (servizio as-srvmap)
Porta 8470 (servizio as-central)
Porta 8472 (servizio as-dtaq)
Porta 8475 (servizio as-rmtcmd)
Porta 8476 (servizio as-signon)

La mancanza o la non disponibilità di una sola di queste porte rende impossibile la comunicazione tra Looc.up e AS400 e rende di fatto impossibile il funzionamento del client grafico.


## Problemi noti

### Prestazioni della JVM nell'esecuzione di Looc.Up
Sono stati riscontrati dei problemi di lentezza o di non funzionamento della JVM su alcuni PC. Questi problemi possono dipendere dal fatto che Looc.Up viene avviato invocando direttamente il file Loocup.jar senza passare gli opportuni parametri di ottimizzazione della Java Virtual Machine. Per questo motivo è consigliato avviare Looc.Up invocando sempre i programmi Loocup.exe o Loocup_w.exe che si occupano di avviare la JVM con gli opportuni settaggi di memoria.
Si ricorda comunque che le prestazioni del client Looc.Up dipendono principalmente dalla quantità di memoria disponibile sul PC e solo in seconda battuta dalla velocità del processore (che mantiene comunque una certa importanza). E' inoltre fondamentale fare in modo che i sistemi su cui gira Looc.Up siano il più possibile aggiornati; quindi è opportuno aggiornare costantemente il sistema operativo installando i service pack che si rendono man mano disponibili. Looc.Up non ha invece grandi esigenze di elaborazione grafica e non richiede l'utilizzo di hardware grafici particolari.

### Esecuzione su file server win2003
Nel caso di installazione centralizzata di Looc.up su server con sistema operativo Windows 2003, all'avvio di Looc.up da client con sistema operativo Windows XP o Vista, potrebbe venire visualizzata questa finestra di conferma : 
![LOCBAS_021](http://localhost:3000/immagini/LOBASE_031/LOCBAS_021.png)
Per eliminare questa richiesta di conferma, è necessario seguire i seguenti passi : 
 - aprire dal pannello di controllo le "opzioni internet"
 - selezionare la _linguetta_ "Protezione" (o "sicurezza" in base alle varie versioni di sistema operativo)
 - cliccare su "siti attendibili" e quindi sul pulsante "siti"
 - aggiungere l'indirizzo del server su cui è installato Looc.up

Nel caso sul client sia installato Internet Explorer 7 potrebbe essere necessario effettuare anche altre operazioni : 
 - cliccare sul pulsante "livello personalizzato..."
 - andare alla voce "Varie" - "Avvio di applicazioni e file non sicuri" e selezionare "attiva"

### Problemi legati all'aggiornamento della Java Virtual Machine (JVM)
Su alcuni PC si è riscontrato un problema nella gestione dei fuochi con versioni di JVM successive alla 6.2. Risulta pertanto fondamentale, una volta installata la JVM, disabilitare l'aggiornamento automatico. Per compiere questa operazione andare nel pannello di controllo, cliccare sull'icona **JAVA** (riconoscibile perchè riporta una tazzina di caffè) andare sul pannello **Aggiornamento** e togliere la spunta (se c'è) dal campo **Controlla automaticamente la presenza di aggiornamenti** e poi confermare la scelta cliccando su **Non controllare

### Installazione su Window Vista e versioni successive
Nel caso si installi Loocup su Windows Vista, Windows 7 o Windows 2008 è necessario installare la Java Virtual Machine in versione 6.

### Installazione su Window NT/2000
Nel caso si utilizzi il prodotto su sistema Windows 2000/NT è necessaria l'installazione dei service pack aggiornati all'ultima versione disponibile (vedi sito Microsoft Update per dettagli). In caso contrario la Java Virtual Machine potrebbe dare luogo ad instabilità e problemi di funzionamento sia con LoocUp che con eventuali altri programmi Java presenti sul sistema

### Installazione su Windows 98
Looc.Up può in teoria funzionare su Windows 98. Non è però garantito il funzionamento in quanto non sono svolti test su questa piattaforma. A questo proposito si ricorda comunque che le versioni 95/ME/98 di Windows sono da tempo non supportate nemmeno dalla Microsoft stessa ed è quindi probabile che con il tempo diventino inutilizzabili con tutti i programmi di nuova concezione. Se si decide comunque di usare Looc.up su queste piattaforme è possibile ricevere un messaggio di errore di tipo "Spazio di ambiente esaurito" all'avvio del programma. Questo errore è dovuto al limite di 256 caratteri nella lunghezza dei comandi di avvio e può essere semplicemente risolto aggiungendo nel file di sistema config.sys la riga : 
_7_Shell = C : \COMMAND.COM C : \ /e : 32000 /p

### Problemi legati all'acceleratore grafico
Su alcuni sistemi HW (soprattutto portatili con Win XP),Looc.up può manifestare dei problemi di incompatibilità grafica che possono portare ad errori di sistema e al blocco della macchina. Secondo informazioni della Sun questi problemi sono dovuti al driver Direct3D che su alcune macchine potrebbe essere non aggiornato o non pienamente conforme allo standard. L'effetto di questi malfunzionamenti è il blocco improvviso della macchina e la comparsa dello schermo blu tipico degli errori fatali in ambiente Windows. A seguito dell'errore la macchina non può più essere utilizzata se non riavviandola. Looc.up a partire dalla versione 1.0 è stato opportunamente modificato per evitare questa tipologia di errori. In particolare è stata impostata una procedura di avvio che disabilita in automatico il supporto Direct3D e, a fronte di una modesta perdita di prestazione, assicura un corretto funzionamento al sistema. Perchè questa procedura di avvio possa essere aplicata, è necessario avviare Looc.up usando uno dei due file di avvio disponibili (_7_Loocup.exe o _7_Loocup_w.exe) ed evitare l'avvio del programma diretto dal file LoocUp.jar. E' comunque consigliabile aggiornare all'ultima versione disponibile il driver Direct3D della propria scheda grafica. Gli aggiornamenti di solito si trovano sul sito del produttore.

### Problemi nella disintallazione di vecchie versioni di LoocUp
A partire dalla versione 0.8 Looc.up dispone di una procedura automatica di installazione che, oltre a rendere agevole l'installazione del prodotto, si cura anche di rendere semplice la fase di disinstallazione. Normalmente la procedura di disintallazione può essere avviata semplicemente andando nella lista dei programmi intallati (accessibile dal pannello di controllo di Windows) e selezionando Looc.up come programma da eliminare. Questa procedura di installazione non era però disponibile per le versioni più vecchie di Looc.up nonchè per alcune versioni più recenti ma afflitte da un bug nel motore di disistallazione. Per questo può succedere di avere installato una copia di Looc.up sulla propria macchina senza averne traccia nella lista delle applicazioni installate sul sistema. In questi casi la cancellazione di Looc.up e la sua completa eliminazione dal sistema può essere ottenuta cancellando manualmente la directory che contiene i suoi files :  a tal proposito si ricorda che tutti i file di Looc.up sono installati in una sola directory (normalmente la _7_C : \programmi\Looc.up) e che l'installatore non modifica in alcun modo lo stato dei registri del sistema. Pertanto la cancellazione manuale della directory del programma e l'eliminazione di tutti i link a lei riferiti porta alla completa disintallazione del programma senza compromettere la sicurezza e la stabilità del sistema. Comunque, quando presente, si consiglia di procedere alla disintallazione usando sempre la procedura automatica offerta dal programma.

### Imperfezioni legate al multimonitor
La gestione del multimonitor in loocup non è perfetta.
Loocup si avvia sempre nel monitor principale, quindi anche se viene spostato nel secondario, al successivo riavvio non "ricorda" questa impostazione.
Inoltre le finestre di emulazione non sempre "ricordano" in quale monitor sono state aperte, anche all'interno della stessa sessione di loocup.

Si coinsiglia di utilizzare loocup sempre nel monitor principale.

Nel caso di utilizzo PC portatile con monitor esterno, è possibile impostare il monitor esterno come principale. Utilizzando loocup sempre in quel monitor, non ci dovrebbero essere problemi.
Poi una volta scollegato il monitor esterno, tutte le finestre "tornano" nel monitor del portatile. Infatti se da una situazione con doppio monitor se ne scollega uno, tutte le finestre diventano disponibili nel monitor principale, anche senza dover riavviare looc.up. Le finestre correntemente aperte nel monitor secondario si "spostano" nel primario. E al riavvio di loocup tutte si aprono correttamente in quello primario (l'unico rimasto collegato).

Esistono programmi che consentono di impostare il monitor del portatile piuttosto che quello esterno come principale all'avvio di un'applicazione (es. Ultramon). Si potrebbero sfruttare per fare in modo che all'avvio di loocup quello esterno diventi il principale.

In alcune vecchie versioni di loocup erano presenti problemi che causavano l'impossibilità di visualizzare alcune finestre una volta scollegato il secondo monitor. Se si verificano problemi di questo tipo è necessario aggiornare il client ad una versione almeno V2R3M090119 con upgrade almeno del 28 luglio 2009.

### Problemi di primo avvio di Loocup su Windows 7
Su Windows 7, dopo aver installato Loocup in locale sulla macchina, il primo avvio può non riuscire. L'effetto che appare è che in avvio Loocup non va oltre la selezione ambiente.
Il problema nasce dal fatto che, se, come suggetiro dal setup, si installa in %ProgramFiles%, non sempre l'utente con cui si opera, pur avendo i diritti di Amministratore, riesce a fare la prima creazione di alcuni files necessari a Loocup.
Il problema si risolve eseguendo una prima volta Loocup come Amministratore, quindi, facendo click destro su Loocup.exe, selezionare Esegui come amministratore.

### Installazione della JVM su macchine con sistema operativo a 64 bit.
L'installazione della JVM su macchine con sistema operativo a 64 bit richiede alcuni prerequisiti aggiuntivi. Fare riferimento alla sezione "WIndows 7 a 64 bit" per maggiori dettagli.

## Dipendenza da altri prodotti
Alcune funzioni di Looc.up si appoggiano a software esterni. L'assenza di tali prodotti sulla macchina in cui è in esecuzione Looc.up non ne permette la fruizione.
Le funzioni che sono dipendenti da software esterni sono le seguenti : 
 * i servizi del menù di finestra di Loocup contenute in **Servizi--->Servizi AS400** ad eccezione del menù "Emulatore telnet 5250"
 * la visualizzazione di files (xml, pdf, doc, xls, etc.).
 * le **uscite Excel** delle matrici.

### I servizi di accesso alle funzioni di sistema AS400
Tali funzionalità, che genericamente indicheremo come 'Servizi AS400', si appoggiano sulla gestione di sistema fornita dall' Operation Navigator. Questo software è fornito a chi possiede il sistema operativo OS400 **senza necessità di ulteriore licenza se non quella del sistema operativo dell' AS400 .

Per poter utilizzare questi servizi è però necessario che il collegamento di loocup al server AS400 **NON venga effettuato tramite l'indirizzo IP** :  è necessario utilizzare un nome simbolico (ad esempio AS400.AZIENDA.IT).

Per far questo è possibile agire in due modi. La soluzione migliore è quella di configurare il DNS della rete aziendale definendo una corrispondenza tra l'IP dell'AS400 e un nome simbolico. In caso questo non sia possibile, è possibile inserire tale corrispondenza nel file hosts dei PC che utilizzano loocup.

Per controllare se esiste già un nome simbolico associato all'indirizzo IP che normalmente si utilizza per il collegamento, è possibile digitare da una finestra DOS il comando _7_ping -a <indirizzo-IP>. Nella prima riga di risposta è possibile controllare se esiste un nome simbolico associato a tale IP.
Attenzione che se non si vede il nome simbolico non significa che non esista al 100%. Per sicurezza è meglio chiedere comunque a chi gestisce la rete aziendale.

Esistono però delle eccezioni a questa obbligatorietà. Se nel DNS aziendale è inserito un nome simbolico associato all'IP dell'AS400 ed è stao definito anche il relativo record di risoluzione DNS inversa, allora è possibile utilizzare i "Servizi AS400" anche collegandosi con l'indirizzo IP. Un comportamento analogo inoltre può essere sfruttato anche con la tecnica del file hosts. Dato che il record inserito nel file hosts serve sia per la risoluzione diretta che quella inversa, una volta inserito il record nel file hosts è quindi possibile collegarsi sia utilizzando nome simbolico che IP. E' comunque sempre consigliato collegarsi utilizzando il nome simbolico.

Esistono inoltre ulteriori limitazioni sul nome simbolico utilizzato. Non tutti i nomi simbolici utilizzabili sono compatibili con i "servizi AS400" citati precedentemente. Per poterli utilizzare, tale nome deve essere composto solo da lettere, numeri e il carattere ".". Inoltre ogni gruppo alfanumerico separato dal "." non può essere più lungo di 10 caratteri e non può iniziare con un numero. Non sono quindi validi nomi mnemonici di questo tipo : 
 * NOMEAS400AZIENDALE (più lungo di 10)
 * NOMEAS400.QUESTAAZIENDA (secondo "blocco" più lungo di 10)
 * NOME.AS.400 (il terzo "blocco" inizia con una cifra)

Da notare che loocup si collegherebbe comunque correttamente (il nome simbolico è valido a livello di rete), l'unica cosa che non funzionerebbe sarebbero i "servizi AS400". Si otterrebbe in tal caso il seguente messaggio (The system name is not a valid AS/400 system name.) : 
![LOCBAS_024](http://localhost:3000/immagini/LOBASE_031/LOCBAS_024.png)
è invece valido anche per i "servizi AS400" il seguente indirizzo :  NOME.AS400.AZIENDALE (anche se in totale sono più di 10 caratteri, i singoli "blocchi" sono più corti).

Si segnala inoltre che in alcune vecchie versioni di operation navigator è necessario impostare una connessione con lo stesso nome simbolico utilizzato per il collegamento di loocup. Con le versioni più recenti invece l'inserimento di una connessione viene fatta automaticamente al primo utilizzo. La presenza corretta di tale configurazione è particolarmente importante nei casi in cui Loocup sia utilizzato per accedere diversi AS400. In tal caso, infatti, se la richiesta di servizi AS400 avanzata da Looc.up non trova una corrispondenza corretta nella configurazione dell'Operation Navigator, quest'ultimo potrebbe avviare sempre e comunque il primo collegamento che trova.

Di seguito vengono elencate tutte le voci che vanno spuntate nel programma di installazione del Client Acces : 

-  programmi obbligatori
-- programmi facoltativi
--- guida per l'utente
-- i series navigator
--- supporto di base
--- operazioni di base
--- gestione lavoro
--- file system
- accesso ai dati
-- odbc
--- supporto formato lotus 123
- AFP Workbench Viewer
- Toolbox per java
- emulazione video e stampanti 5250
--    (vanno bene i default)
- programmers toolkit
-- intestazioni


### La visualizzazione di files.
La visualizzazione di files (xml, pdf, doc, xls, etc.) prevede la presenza del relativo software in grado di gestire il file richiesto.

### Le uscite in Excel.
Le **uscite Excel** delle matrici prevedono la presenza di **Microsoft Excel** o **OpenOffice** sulla macchina.

## Looc.Up sotto CITRIX
### Prerequisiti
 * Client citrix installato, accedere utilizzando Microsoft Internet Explorer
 * Java Virtual Machine Installata sul server citrix
 * tool di verifica dell'installazione che abbia dato esito positivo.

## Accesso al server in laboratorio
L'installazione attuale è ancora in fase di test.

Per l'accesso utilizzare il link http://citrix.softia.it/CitrixAccess/auth/login.aspx.

E' possibile accedere utilizzando l'utente di dominio **testcitrix** che è  amministratore del server la password è conosciuta da Lancini, Foresti, Maestrelli, Fortini, Cestana.

Con questo utente si può utilizzare Loocup con l'unica limitazione che se c'è una scheda o riferimento a macchine del dominio del laboratorio tali accessi sono bloccati.

 :  : PAR  L(PUN)
- utilizzando l'utente loocuptest non è possibile accedere al server  in quanto, volutamente, è stato creato un'utente locale al server.
- per evitare malfunzionamenti ho dovuto impostare che l'utente loocuptest avesse accesso in lettura scrittura su tutte le cartelle LOOCUP_xxx. Il default era acesso il lettura.


Errori conversione di numeri

- se la lingua dell'utente è inglese la parte delphi quando converte i numeri non li riconosce correttamente (non riconosce la virgola come separatore dei decimali)
- analogo problema nella gestione delle date :  la parte delphy suppone che il formato della data sia gg/mm/yy o yyyy. Genera una data sbagliata quando il formato di rappresentazione della data è americano :  mm/gg/yyyy


### Configurazione attuale client CITRIX
>Microsoft Windows [Version 5.2.3790]
(C) Copyright 1985-2003 Microsoft Corp.

C : \WINDOWS\system32>set
ALLUSERSPROFILE=C : \Documents and Settings\All Users
APPDATA=C : \Documents and Settings\testcitrix\Application Data
CLIENTNAME=SMEA.IT-TESTCITRIX
ClusterLog=C : \WINDOWS\Cluster\cluster.log
CommonProgramFiles=C : \Program Files\Common Files
COMPUTERNAME=SRVCITRIX
ComSpec=C : \WINDOWS\system32\cmd.exe
HOMEDRIVE=C : 
HOMEPATH=\Documents and Settings\testcitrix
LOGONSERVER=\\SMEA.IT\DFS_ROOT
NUMBER_OF_PROCESSORS=1
OS=Windows_NT
Path=C : \WINDOWS\system32;C : \WINDOWS;C : \WINDOWS\System32\Wbem;C : \Program Files\Ci
trix\System32\Citrix\IMA;C : \Program Files\Citrix\System32\Citrix\IMA\Subsystems;
C : \WINDOWS\System32\Citrix\IMA;C : \Program Files\Citrix\system32;C : \PROGRA~1\COMM
ON~1\Odbc\FILEMA~1;C : \PROGRA~2\IBM\CLIENT~1;C : \PROGRA~2\IBM\CLIENT~1\Shared;C : \P
ROGRA~2\IBM\CLIENT~1\Emulator;
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH
PROCESSOR_ARCHITECTURE=x86
PROCESSOR_IDENTIFIER=x86 Family 6 Model 11 Stepping 1, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=0b01
ProgramFiles=C : \Program Files
PROMPT=$P$G
SESSIONNAME=ICA-tcp-3
SystemDrive=C : 
SystemRoot=C : \WINDOWS
TCP_NODELAY=1
TEMP=C : \DOCUME~1\TESTCI~1\LOCALS~1\Temp\3
TMP=C : \DOCUME~1\TESTCI~1\LOCALS~1\Temp\3
USERDNSDOMAIN=SMEA.IT
USERDOMAIN=SMEA
USERNAME=testcitrix
USERPROFILE=C : \Documents and Settings\testcitrix
windir=C : \WINDOWS

