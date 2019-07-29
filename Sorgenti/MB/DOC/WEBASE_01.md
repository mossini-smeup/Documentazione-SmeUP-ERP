# Installazione di Web.UP

L'installazione di WebUP si riassume in tre attività principali : 
1 - Installazione/configurazione software di terze parti (contesto :  Application server, Windows/Linux, Java)

2 - Installazione/configurazione software SmeUP (contesto :  SmeUP Provider)
- Per l'installazione di rimanda a : 
- [Sme.UP Provider&-x3a; Set and play](Sorgenti/MB/DOC/LOCBAS_SPI)

3 - Configurazione connessione/login (contesto :  WebUP / SmeUP ERP / Windows / Linux)

Allo stato attuale, WebUP può essere installato su macchine Windows o Linux, SmeUP Provider invece solo su macchine Windows.
E' possibile far coesistere installazioni WebUP e SmeUP Provider su medesima macchina o su due macchine differenti (e/o con diversi sistemi OS).
Dati I benefici della scalabilità, è utile virtualizzare le macchine.

Prima dell'installazione, verificare con il committente tutti i requisiti. Nel documento seguente è riportata la checklist da verificare

- [Checklist installazione webup](Sorgenti/MB/DOC/WEBASE_07)


# Requisiti minimi software

- Java JDK1.8 a 64bit.
La versione a 32 bit può usare al massimo 1024Mb di ram, pertanto può essere utilizzata solamente in ambito di test o con pochissime connessioni (meno di 5). In un ambiente di produzione la mancanza di memoria porta a crash dell'applicazione.
E' possibile effettuare un'installazione standalone della jvm nel caso non si voglia utilizzare la jvm di sistema.
- [Installazione jvm standalone per Payara](Sorgenti/MB/DOC/WEBASE_012)
- Application Server Payara 4.1.1.162 (http://www.payara.fish/)
- WebUP all'ultima versione (viene distribuito in un'unico file "war")
- SmeUP Provider, reperibile sul sito istituzionale (http://www.smeup.com), sezione download.


![WEBASE_001](http://localhost:3000/immagini/WEBASE_01/WEBASE_001.png)
# Requisiti minimi server

- Windows Server 2012 / Ubuntu Server 14.04.2 LTS
- CPU Quad core
- 4GB RAM
- 40GB HDD

Le risorse di cui sopra variano in funzione all'utilizzo del server, quindi è consigliabile virtualizzare per usufruire dei vantagggi della scalabilità.

**N.B :  Per ovvie ragioni, se si opta per l'opzione Windows, è fortemente sconsigliato l'utilizzo di un os che non sia una release "server". 


# Esempio di procedura di installazione Application Server Payara (linux o windows)

Per la procedura aggiornata e per tutti i dettagli (ad esmepio configurazione https) consultare il sito di payara : 
http://www.payara.fish/

Riportiamo un esempio di procedura di installazione da noi testata : 
- È preferibile creare un utente dedicato (es. payara)
- Installare Java JDK1.8 (è possibile anche puntare ad un'installazione jdk dedicata, qualora si vogliano far coesistere più installazioni jdk.)
- Decomprimere archivio (unzip o tar -xzvf) di payara.zip/tar.gz in una folder del server con permessi di lettura/scrittura.
- Avviare payara da riga comandi (prompt msdos / shell linux) mediante il comando : 
c : \Users\payara\.....\glassfish\bin\asadmin.bat
oppure
/home/payara/....../glassfish/bin/./asadmin.sh
Una volta avviato l'interprete dei comandi, è possibile conoscere la versione dell'application server digitando la keyword :  **version

Per avviare l'application server è sufficiente inserire il comando **start-domain** nell'interprete di comandi di payara

A questo punto, dal browser si può verificare che l'application server sia attivo, semplicemente puntando l'url: http://localhost:8080
e verificando che il server risponda running.
L'interfaccia grafica per la configurazione dello stesso risponde all'url: http://localhost:4848
Anche mediante l'interfaccia grafica, posizionandosi sulla voce "server" del menu principale di sinistra, è possibile conoscere la versione
dell'application server.

Ai fini di facilitare eventuali interventi da remoto, è utile abilitare un servizio ssh.

**N.B :  il default d'installazione di payara prevede che l'interfaccia grafica sia disabilitata per gli accessi da remoto (cioè che non arrivino da "localhost").

Si rimanda alle documentazioni online di Payara e di Windows/Linux/Oracle relativamente a : 
- ottimizzazioni (thread, memoria...)
- abilitazioni di funzionalità (cambio porte, accessi da remoto...)
- installazione servizi, avvii/spegnimenti schedulati
- modifica del jdk di default...

**N.B :  il default d'installazione di payara prevede che la memoria allocata sia di 512MB, e che java sia avviato in modalità "client". E' bene quindi effettuare un tuning dell'application server per ottimizzarne le performance.
E' indispensabile configurare almeno i seguenti parametri (dipendenti dalle caratteristiche del server : 
- parametro -server (di default è -client)
- memoria allocata all'avvio (parametro -Xms....m ) indicativamente 2GB, quindi -Xms2048m.
- memoria massima utilizzata (parametro -Xmx....m ) indicativamente 4GB, quindi -Xmx4096m.
I parametri di cui sopra sono configurabili accedendo alla console d'amministrazione tramite browser su porta 4848 (es. http://localhost:4848), nella sezione Configurations -> server-config -> JVM Settings.
Ovviemante la documentazione ufficiale Oracle rimane la più aggiornata ed esaustiva.

# Installazione e configurazione WebUP

La vera e propria installazione di WebUP avviene mediante l'attività denominata "deploy", effettuata tramite payara mediante interfaccia grafica, raggiungendo col browser l'indirizzo : 
http://localhost:4848
e selezionando la voce "Applicazioni" e poi "deploy", selezionando l'opportuno file "war".


# Avvio

Se l'installazione (deploy) è andata a buon fine e se NON si tratta della prima installazione (quindi sul server erano presenti installazioni precedenti e già configurate) puntando ad http://localhost:8080/<nome_contesto>,
si dovrà verificare che l'application server risponda "running"


**N.B.
la configurazione dell'applicazione (file configuration.properties) ed i parametri di login (<nomemodoulo>.properties) vengono memorizzati su archivi di testo presenti sul server d'installazione all'indirizzario : 
root/etc/webup/<nome_contesto> con root = directory utente. (es :  c : \Users\payara\etc\webup\WebUP )




# Configurazione dei Login

Web.UP supporta diverse modalità di login contemporaneamente, nella stessa applicazione.

E' possibile configurare una serie di proprietà globali dell'applicazione, tra cui le diverse modalità di connessione/autenticazione (moduli di login).
E' possibile poi configurare tramite interfaccia grafica tutta una serie di tipologie di login, a seconda dell'esigenza.



# Tipologie di login

E' possibile entrare in più ambienti e utilizzare diverse modalità di qualificazione.

- [Moduli Login](Sorgenti/MB/DOC/WEBASE_011)

# Main Config - custom settings e configurazione

Web.UP permette una grande libertà di personalizzazione a livello grafico e di configurazione a livello tecnico.
L'accesso ai settaggi è fornito dalla form Main Config (nel medesimo contesto dei moduli di login)

- [Configurazione Main](Sorgenti/MB/DOC/WEBASE_013)

* Sfondi :  è possibile specificare lo sfondo del login e lo sfondo delle pagine interne. Vedere il file configuration.properties
* Loghi :  è possibile specificare un logo per ogni modulo di login e lo sfondo delle pagine interne. Vedere il file configuration.properties
* Css :  è possibile definire un proprio file css che verrà aggiunto a quello standard, permettendo così di ridefinire la maggior parte delle regole grafiche. Questo tipo di personalizzazione necessita di competenze specifiche sui fogli di stile CSS.

Alcuni esempi di WebUP in diversi stili ed ambiti applicativi : 
![WEBASE_054](http://localhost:3000/immagini/WEBASE_01/WEBASE_054.png)
![WEBASE_055](http://localhost:3000/immagini/WEBASE_01/WEBASE_055.png)
![WEBASE_056](http://localhost:3000/immagini/WEBASE_01/WEBASE_056.png)

## Header personalizzato
Webup da la possibilità di definire un Header personalizzato al posto della barra standard che compare di default nella parte alta della pagina.
Dopo aver attivato la modalità di sviluppo da terminale, per inserire il proprio header personalizzato è necessario : 
* accedere alla pagina delle configurazioni (icona dell'ingranaggio che si trova in alto a destra)
* attivare l'opzione custom header enabled
* disabilitare l'opzione Menu enabled
* inserire il codice html personalizzato nella parte "Optional header" dedicata a tale scopo
**Funzioni disponibili nel customer header**
Per comunicare con WebUP sono state definite delle funzioni javascript. Alcune di queste funzionalità sono : 
* back
* lettura titolo della scheda
* lettura delle variabili webup
**Back**
Per navigare all'interno di webup e tornare ad una scheda precedentemente visualizzata, è sufficiente richiamare la funzione javascript back all'interno del codice html personalizzato.
Esempio
    <a href="javascript : back();" class="back_btn">Indietro</a>

**Titolo della scheda**
Il titolo di una scheda può essere reperito attraverso un meccanismo di funzioni javascript che : 
* indica a webup quale funzione richiamare ad ogni cambio scheda per l'impostazione del titolo (funzione smeupCustomHeaderSetup() richiamata al load della pagina);
* esegue l'assegnazione del titolo all'elemento html opportuno.
Esempio

<h1 class="title"/>

<script>
     function setTitle(title){
           $(".title").html(title);
     };

     $(window).load(function(){
            smeupCustomHeaderSetup(&-91;{name : 'titleCallback', value  : 'setTitle'}&-93;);
      });

</script>

Nota :  la funzione smeupCustomerHeaderSetup(..) imposta la funzione di callback che verrà richiamata ad ogni cambio scheda. La funzione riceve come parametri di ingresso un array di elementi con le proprietà nome -> valore. Nell'esempio viene impostata la proprietà titleCallback con il valore setTitle

**Lettura variabili webup**
La funzione javascript da chiamare per ottenere il valore di una variabile è smeupGetVariableValue(); indicando il nome della variabile da leggere e la funzione di callback da chiamare per recepire il valore della variabile richiesto.

Esempio
smeupGetVariableValue(&-91;{name : 'variable', value  : '*LOGINMODULE'}, {name : 'callback', value  : 'setTitle'}&-93;);

# Incompatibilità note

E' stata rilevata un'incompatiblità di Glassfish 3.x e 4.1  con WebUP1.8.8.
Il problema non sussiste invece con Glassfish 4.1.1.
Resta comunque fortemente consigliato l'utilizzo di Payara 4.1.1.162.
