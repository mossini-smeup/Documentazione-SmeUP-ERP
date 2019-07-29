Ultima modifica :  01/12/2016

# Ambienti di sviluppo per As.UP

## Introduzione

All'interno del progetto As.UP sono previsti i seguenti ambienti di sviluppo, in ordine decrescente di copertura sul progetto : 


- **A) Core : ** ambiente di sviluppo completo
- **B) Plugin : ** ambiente per sviluppo plugin As.UP
- **C) Parser : ** ambiente per lo sviluppo di grammatiche AntLR o LPG
- **D) Application : ** ambiente applicativo As.UP


L'ambiente Core è l'ambiente più completo, consente di operare su tutte le componenti del progetto As.UP e dispone di
tutte le dipendenze necessarie allo sviluppo. Gli altri tre ambienti sono invece dei contesti operativi ridotti, dedicati a
specifiche attività sul progetto.

## Elementi comuni a tutti gli ambienti (importante)

Gli elementi che accomunano tra loro tutti gli ambienti di sviluppo sono i seguenti tre : 


- **Eclipse**
- **Java SDK**
- **Plugins aggiuntivi per Eclipse**


### 1) Eclipse

Tutti gli ambienti di sviluppo sono attestati su piattaforma **Eclipse**.
L'ultima versione disponibile  è la **4.6 Neon** ed è quella di riferimento per il resto di questo documento. Nelle descrizioni
dei singoli ambienti operativi verrà indicato il link da cui scaricare Eclipse e la versione precisa da utilizzare. Eclipse è disponibile
sia per macchine Windows che per macchine Linux ed è disponibile in versione a 32 e a64 bit. Se l'architettura del proprio PC
lo consente, si consiglia la versione a 64 bit. Eclipse non ha un tool di installazione predefinito ma viene distribuito come un
file zip contenente tutto il necessario. Per installare l'IDE è quindi sufficiente scompattare il contenuto del file zip in una
qualsiasi cartella del proprio PC e avviare il prodotto utilizzando il file eseguibile contenuto al sui interno.

Una bella introduzione alla piattaforma Eclipse e al suo utilizzo base si può trovare nel seguente documento : 

[http://www.vogella.com/tutorials/Eclipse/article.html](http://www.vogella.com/tutorials/Eclipse/article.html)

### 2) Java SDK

Prerequisito necessario al funzionamento di Eclipse è l'installazione sulla macchina del **Java Developer Kit (JDK). La
versione Java di riferimento per il progetto As.UP è la 1.8 e anche in questo caso, se il PC la supporta, è preferibile installare la
versione del JDK a 64 bit.
Se si è installata una versione di Eclipse a 64 bit allora sarà obbligatorio scegliere una JDK che sia anch'essa a 64 bit,
pena in non funzionamento del sistema.

La JDK da installare può essere scaricata al seguente link : 

 :  : DEC T(J1) P(URL) [http://www.oracle.com/technetwork/java/javase/downloads/index-jsp-138363.html-javasejdk](http://www.oracle.com/technetwork/java/javase/downloads/index-jsp-138363.html-javasejdk)

dove è possibile trovare la JDK corretta per il proprio sistema operativo (previa accettazione di una licenza di utilizzo).
Una volta scaricato il file di installazione è sufficiente lanciare l'eseguibile e seguire le indicazione a video (in genere è
sufficiente confermare tutti i default proposti).

## 3) Plugins aggiuntivi per Eclipse

Infine, per la configurazione dei vari ambienti operativi è necessario l'installare all'interno di Eclipse dei tools aggiuntivi
necessari al progetto, chiamati nel gesrgo Eclipse **plugins**. I plugins vengono installati in Eclipse utilizzando il
motore di aggiornamento interno denominato **P2**. Il motore di aggiornamento P2 è in grado di installare i plugins
aggiuntivi prelevandoli da dei punti di distribuzione registrati dentro l'IDE, chiamati **repository P2**. All'interno di un
repository P2 i plugin possono essere o meno catalogati in **Categories**. L'installazione dei plugins può quindi
avvenire selezionando uno per uno i plugins che si vuole installare oppure selezionando direttamente una o più categorie
(in questo caso saranno installati tutti i plugin registrati nelle categorie selezionate)

 T(La procedura di installazione di un plugin si può quindi riassumere nei seguenti passi : )
- Registrazione in Eclipse del repository P2 che distribuisce uno specifico tool
- Apertura del repository registrato e selezione dei plugin da installare tra quelli offerti. La lista dei plugin è visualizzata
con un raggruppamento per categorie.


Per maggiori dettagli sulla procedura di installazione dei plugin fare riferimentoal seguente documento : 

 :  : DEC T(J1) P(URL) [http://www.vogella.com/tutorials/Eclipse/article.html-updates-and-installation-of-plug-ins](http://www.vogella.com/tutorials/Eclipse/article.html-updates-and-installation-of-plug-ins)

Nella descrizione dei singoli ambienti verranno elencati i repository P2 da registrare in Eclipse nonchè i plugin
da installare per quello specifico ambiente.


## A) Ambiente per lo sviluppo Core

E' l'ambiente di sviluppo completo, che consente di intervenire in ogni parte del progetto As.UP e di gestire i
sorgenti applicativi.

### A.1) Versione di Eclipse richiesta : 

**Eclipse Modeling Tools versione 4.6 (Neon)** :  attenzione, per questo ambiente è consigliabile partire dal
pacchetto Eclipse Modeling Tools. Questo pacchetto è composto da un Eclipse base con preinstallato i plugins
necessari alla gestione della modellazione (EMF).

Scaricabile da : 

[http://www.eclipse.org/downloads/eclipse-packages/](http://www.eclipse.org/downloads/eclipse-packages/)

### A.2) Repository P2 : 

Registrare in Eclipse il seguente repository P2

**http://smeup.github.io/com.smeup.asup.p2.eclipseide.site**

questo repository contiene tutti i plugin necessari all'ambiente di sviluppo completo di As.UP. Si tratta per lo
più di plugin sviluppati dal progetto Eclipse con l'aggiunta di alcuni plugin specifici di As.UP.

Una volta registrato il repository P2 di Eclipse installare le seguenti categorie di plugin : 

* Category
** ECF  (da http://download.eclipse.org/rt/ecf/3.11.0/site.p2)
** DTP  (da http://download.eclipse.org/datatools/updates/1.12)
** As.UP Parser tools (da As.UP project)
** AJDT (da  http://download.eclipse.org/tools/ajdt/45/dev/update/)
** Net4J (da Eclipse Modeling Project)
** As.UP EMF tools (da As.UP project)

## B) Ambiente per lo sviluppo di plugins As.UP

E' l'ambiente di sviluppo per i plugin As.UP; un plugin As,UP è un modulo che definisce e gestisce oggetti
tipizzati all'interno del framework (ad esempio, JOBD, DTAQ, MSGF) cioè tutti gli oggetti che possono
essere registrati nel registro di sistema.

### B.1) Versione di Eclipse richiesta : 

**Eclipse Modeling Tools versione 4.6 (Neon)** :  attenzione, per questo ambiente è consigliabile partire dal
pacchetto Eclipse Modeling Tools. Questo pacchetto è composto da un Eclipse base con preinstallato i plugins
necessari alla gestione della modellazione (EMF).

Scaricabile da : 

[http://www.eclipse.org/downloads/eclipse-packages/](http://www.eclipse.org/downloads/eclipse-packages/)


### B.2) Repository P2 : 

Registrare in Eclipse il seguente repository P2

**http://smeup.github.io/org.smeup.sys.p2.site**

Una volta registrato il repository installare i plugin registrati nella seguente categoria : 

* Category
** As.UP features for system


## C) Ambiente di sviluppo per parser

E' l'ambiente di sviluppo da utilizzare nel caso si vogliano creare o modificare grammatiche scritte
con AntLR o LPG. Tutte i parser di linguaggio utilizzati all'interno di As,UP sono costruiti partendo
da grammatiche LPG o AntLR, questo ambiente consente di operare su queste grammatiche
mettendo a disposizione i tool necessari all'editing, compilazione e controllo.

### C.1) Versione di Eclipse richiesta : 

**Eclipse IDE for Java Developers versione 4.6 (Neon)** :  è il pacchetto base di Eclipse, sufficiente per
questo ambiente di sviluppo.

Scaricabile da : 

[http://www.eclipse.org/downloads/eclipse-packages/](http://www.eclipse.org/downloads/eclipse-packages/)

### C.2) Repository P2 : 

Registrare in Eclipse il seguente repository P2

**http://smeup.github.io/com.smeup.asup.p2.eclipseide.site**

Una volta registrato il repository installare i plugin registrati nella seguente categoria : 

* Category
** As.UP Parser Tools


## D) Ambiente applicativo As.UP

E' l'ambiente in cui sviluppare contenuti applicativi in As,UP. In questo contesto è possibile : 


- Convertire programmi da iSeries in Java
- Scrivere programmi e servizi per As.UP sfruttando le funzionalità del framework
- Avviare istanze As.UP con diverse configurazioni


### D.1) Versione di Eclipse richiesta : 

**Eclipse Modeling Tools versione 4.6 (Neon)** :  attenzione, per questo ambiente è consigliabile partire dal
pacchetto Eclipse Modeling Tools. Questo pacchetto è composto da un Eclipse base con preinstallato i plugins
necessari alla gestione della modellazione (EMF).

Scaricabile da : 

[http://www.eclipse.org/downloads/eclipse-packages/](http://www.eclipse.org/downloads/eclipse-packages/)

### D.2) Repository P2 : 

Questo ambiente richiede la registrazione in Eclipse di 3 diversi repository P2.

### D.2.1) Repository per ambiente di sviluppo

Registrare in Eclipse il seguente repository P2

**http://smeup.github.io/com.smeup.asup.p2.eclipseide.site**

questo repository contiene tutti i plugin necessari all'ambiente di sviluppo completo di As.UP. Si tratta per lo
più di plugin sviluppati dal progetto Eclipse con l'aggiunta di alcuni plugin specifici di As.UP.

Una volta registrato il repository P2 in Eclipse installare le seguenti categorie di plugin : 

* Category
** DTP  (da http://download.eclipse.org/datatools/updates/1.12)
** Eclipse ECF Plugin  (da http://download.eclipse.org/rt/ecf/3.11.0/site.p2)
** Net4J Eclipse Plugin(da Eclipse Modeling Project)
** As.UP Parser tools (da As.UP project)
** As.UP EMF tools (da As.UP project)
** AJDT (da  http://download.eclipse.org/tools/ajdt/45/dev/update/)

### D.2.2) Repository per l'installazione del framework di base di As.UP

Questo repository contiene tutti i plugin che compongono il framework di base di As.UP

Repository da registrare : 

**http://smeup.github.io/org.smeup.sys.p2.site**

Una volta registrato il repository installare i plugin registrati nella seguente categoria : 

* Category
** As.UP features for system

### D.2.3) Repository per l'installazione dei componenti di As.UP di Sme.UP

Questo repository contiene tutti i plugin di As.UP che sono specifici del gestionale Sme.UP.

Repository da registrare : 

**http://smeup.github.io/org.smeup.mu.p2.site**

Una volta registrato il repository installare i plugin registrati nella seguente categoria : 

* Category
** As.UP MU gen features

## Gestione dei sorgenti e versioning

La gestione dei sorgenti all'interno del progetto As.UP si basa su **repository GitHUB**.

GitHub è un servizio di hosting per progetti software. Basato sul protocollo GIT, consente di creare
dei repository in cui salvare i sorgenti dei propri progetti e al tempo stesso gestire il processo di
sviluppo condiviso e versioning.

GitHUB consente la creazione di repository ad accesso pubblico o privato :  i primi sono repository il
cui contenuto è aperto a tutti gli utenti registrati in GitHUB. Sono quindi adatti per la condivisione di
sorgenti open source e per la gestione di progetti aperti. I repository privati sono invece accessibili
solo dagli utenti autorizzati dall'amministatore del progetto, Sono quindi adatti per lo sviluppo
condiviso di software proprietario o per progetti a sviluppo chiuso.

Eclipse dispone nativamente di tutti gli strumenti per l'accesso a repository remoti GitHUB e per la
replica in locale di questi repository.

L'utilizzo del versione control GIT all'interno della piattaforma Eclipse è descritto in dettaglio nel
seguente documento : 

[http://www.vogella.com/tutorials/EclipseGit/article.html](http://www.vogella.com/tutorials/EclipseGit/article.html)

I sorgenti del progetto As,UP sono suddivisi in tre distinti repository GitHUB (identificati dalla sintassi del protocollo GIT) : 

*  **git@github.com : smeup/asup.git** :  repository pubblico che contiene i sorgenti del frameworl base As.UP
*  **git@github.com : smeup/smeup-mu.git** :  repository privato che contiene i sorgenti del framework As.UP legati al gestionale Sme.UP
*  **git@github.com : smeup/smeup-gen.git** :  repository privato che contiene i sorgenti ottenuti dal processo di conversione del gestionale Sme.UP

I primi due repository contengono i sorgenti del framework As.UP e interessano quindi gli
sviluppatori interessati allo sviluppo architetturale del framework. Per poter essere
usati devono essere importati all'interno di un ambiente di sviluppo As.UP di tipo **Core**.

Il terzo repository contiene invece i sorgenti prodotti dal convertitore RPG-Java a partire
dai programmi RPG che compongono ll gestionale Sme.UP. Questi sorgenti possono
essere importati sia in un ambiente **Core** (serve però importare anche i primi due repository)
ma anche in un ambiente di sviluppo As.UP di tipo **Application** (e in questo caso non serve
importare i sorgenti dai primi due repository).








