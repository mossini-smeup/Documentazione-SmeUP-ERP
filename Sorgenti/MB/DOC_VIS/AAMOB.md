 :  : TIT Mobile Platform
# Introduzione
Il fenomeno delle tecnologie mobili continua a crescere; infatti negli ultimi cinque anni i lavoratori che per lavoro si spostano, sono cresciuti considerevolmente. Dai tradizionali operatori di vendita che devono registrare gli ordini o conoscere la situazione dei pagamenti aggiornati al momento dei clienti, al personale che trasporta o distribuisce beni, gli addetti alla logistica di magazzino per l'entrata e l'uscita delle merci, i tecnici di aziende che danno assistenza a macchine e o impianti di cui curano la manutenzione, gli addetti alla raccolta delle prenotazioni dei pasti per il catering, i medici negli ospedali che hanno bisogno di accedere velocemente alla storia clinica del paziente, i manager aziendali che vogliono visualizzare dal loro dispositivo palmare i valori aggiornati delle vendite o della produzione o i dati di gestione economica.
Forti della significativa esperienza nello sviluppo di soluzioni mobili, Newtone Sistemi e Sme Up hanno sviluppato una piattaforma che consente di prototipare velocemente soluzioni mobili per le aziende. Questa piattaforma non è una soluzione in sé, è un ambiente dove nascono le applicazioni; per questo diciamo che TwinPulse Mobile Platform non è una soluzione ma è una tecnologia.

# Twinpulse Mobile Platform
TwinPulse Mobile Plarform è stato sviluppato interamente con tecnologia Microsoft.Net C-; dai webservices al software dei clienti installato nei dispositivi mobili. Siamo convinti che la tecnologia mobile andrà indubitabilmente verso il sistema operativo Microsoft Mobile. Oltre alla nostra esperienza, vi sono alcune conferme dal mercato che la strada verso le tecnologie mobili di Microsoft è quella corretta; ad es. l'ultimo dispositivo lanciato da Palm è venduto sul mercato con Sistema operativo Mobile di Microsoft.
Tuttavia al di là della tecnologia di Microsoft è stato scelto di non lavorare solo con i prodotti di questa società. Si è ritenuto che anche Linux fosse un altro ambiente con cui lavorare. Per questo motivo si è scelto Postgres come DB, dove far vivere gli scenari. Questa scelta per il DB ci consente di far lavorare la nostra piattaforma anche in ambiente Linux attraverso il progetto Mono.
La piattaforma contiene una serie di componenti che lavorano tra loro, per ottenere applicazioni stabili e sicure.
Questi componenti sono i seguenti :  TwinPulse SyncServer, TwinPulse Application Builder, TwinPulse Everywhere, TwinPulse Data Engine e TwinPulse Business Objects.

# Twinpulse Syncserver
Questo componente è un elemento chiave della piattaforma. Il server è il contenitore dei webservices sviluppati con Microsoft.Net C- e utilizza Postgres come motore di database.
Come abbiamo più sopra affermato, esso può essere installato in un server con sistema operativo Microsoft 2003 o con sistema operativo Linux sotto il progetto Mono.
SyncServer ha due scopi fondamentali :  memorizzare gli scenari sviluppati con TwinPulse Application Builder e lavorare come sincronizzatore dei dispositivi mobili, sia per le applicazioni che per i dati. Il software per il client installato nei palmari è chiamato TwinPulse Everywhere.
È chiaro che i dati e gli scenari (ovvero le applicazioni) sono memorizzati nel DB della piattaforma. Più oltre chiariremo la definizione di scenari.
![AAP_MOB_01](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_01.png)
# Twinpulse Application Builder
Questo è il tool grafico dove il programmatore lavora per lo sviluppo delle applicazioni mobili. Anche questo componente è stato sviluppato con Microsoft.Net C- e gira esclusivamente in ambiente Windows.
L' Application Builder non è strettamente collegato a un particolare SyncServer, ma è possibile connettersi con diversi SyncServers in diverse locazioni. Sottolineiamo che con questo tool è possibile sviluppare in remoto, avendolo installato in un semplice notebook. Posso connettermi al SyncServer del cliente A, lavorare alle modifiche nei suoi scenari, poi connettermi al SyncServer del cliente B e fare altri sviluppi o modifiche.
Quando l'Application Builder è connesso a un server remoto, come avviene nel caso del SyncServer, quest'ultimo ha la missione di gestire il database del cliente. Ciò significa che l' Application Builder non duplica il database ma si connette, attraverso i webservices del SyncServer, al database Postgres dove risiedono le informazioni aziendali.
Abbiamo affermato in diverse occasioni che l' Application Builder è usato dal programmatore per creare e modificare gli scenari; ci focalizziamo ora non solo sugli scenari, ma anche su tutti i componenti che girano in questo tool.
L' Application Builder è più che un designer di schermate (form). Esso è lo strumento fondamentale che interviene dalla creazione delle applicazioni alla gestione delle autorizzazioni per gli utenti che potranno usare le applicazioni stesse. Ora esploriamo quali sono le attuali funzioni di questo modulo.
Il primo concetto è quello di scenario, che serve come contenitore di utenti e form. All'inteno di una azienda vi sono in genere diversi possibili scenari. Ad es. lo scenario dell'area commerciale con accessi ai file clienti e prodotti, il caricamento degli ordini, la giacenza dei prodotti e la visualizzazione dei valori economici per ogni singolo cliente. D'altra parte
vi può essere lo scenario del post-vendita, con accessi ai file clienti e prodotti, il caricamento dei servizi erogati e la giacenza dei prodotti. Partendo da quanto sviluppato per l'area commerciale, è possibile creare altri possibili scenari.
Uno scenario è costituito da form e utenti. Il concetto di scenario è stato di fondamentale importanza per la riutilizzazione delle form. In altre applicazioni (non prodotte con TP) è possibile creare gli scenari, ma non è possibile riutilizzarli in altre applicazioni; generalmente si fanno delle copie degli scenari che ci sono già e si introducono in diverse applicazioni, ma questo comporta un notevole problema di allineamento nel caso di modifiche sulle form.
![AAP_MOB_02](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_02.png)In TwinPulse Application Builder esiste un unico contenitore di form, dove esse sono create e manutenzionate e un unico contenitore degli utenti aziendali. Dentro alle form possiamo inserire immagini e collezioni di dati. Quando parliamo di immagini, intendiamo ad es. il logo della compagnia, le immagini dei prodotti, foto di persone o altro. Anche le immagini sono in un opportuno contenitore e possono essere usate in diverse form.
Le collezioni di dati sono delle comuni tabelle del tipo codici postali, codici Abi e Cab, matricole di dipendenti o altro. Le collezioni sono gestite con lo stesso concetto del contenitore di form o di immagini, per questo anche le collezioni sono create una sola volta e usate ovunque.
È importante ricordare che immagini, form, utenti, collezioni e applicazioni non risiedono nel computer in cui TwinPulse Application Builder viene eseguito; esse si trovano nel server dove gira TwinPulse SyncServer, l'accesso al quale avviene via webservices.
![AAP_MOB_03](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_03.png)Nel contenitore di collezioni si possono creare due tipi di collezioni. Il primo tipo è quello che tradizionalmente crea la coppia valore-testo. Questo può essere fatto anche attraverso l'importazione di file di testo preventivamente preparati.
Le collezioni automatiche possono essere create anche con istruzioni sql (Standard Query Language). Quando viene eseguita l'istruzione sql, la collezione con tutti i valori viene creata nel dispositivo mobile. Questo permette di importare informazioni che vanno oltre alla tradizionale coppia di valori valore-testo.
![AAP_MOB_04](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_04.png)Una volta che immagini e collezioni sono state definite, possiamo iniziare a usare l'editor delle form. Una form è una schermata del palmare, e per questo sono state costruite una serie di componenti predefiniti.
In questo rilascio i componenti disponibili sono i seguenti :  Label, TextBox, TextArea, Numeric Box, Button, CheckBox, Choice, Data Picker, Time Picker, Drop List, Cascade, Multiple Selection, Slider, Image, Sign, Browser, LookupMatrix & PopupGrid. È importante considerare che altri componenti sono in via di sviluppo o si è deciso di svilupparli, spesso su suggerimento dei distributori nazionali, e saranno inseriti nei prossimi rilasci del prodotto.
Ogni componente ha una serie di proprietà adeguate al tema che deve descrivere. Ciò significa che una volta aggiunto alle form possiamo, se può servire, scrivere altri frammenti di software in ciascuno di essi. Continuando con la nostra filosofia di sviluppo questi frammenti dovrebbero essere scritti in C-, ma è stato creato il primo testo in grado di accettare frammenti scritti con altri linguaggi di programmazione.
Come abbiamo già detto, uno scenario è una collezione di form e utenti. Questo è il motivo per cui dall' Application Builder abbiamo un contenitore dove tutti gli utenti di una azienda sono dichiarati e a ciascuno può essere assegnato più di uno scenario.
![AAP_MOB_05](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_05.png)![AAP_MOB_06](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_06.png)![AAP_MOB_07](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_07.png)Dopo la creazione di uno scenario, possiamo procedere ad aggiungere in esso i form che dovranno farne parte. Questa attività si può fare semplicemente con il tasto destro del mouse, scegliendo Attach Forms.
![AAP_MOB_08](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_08.png)Eseguita questa operazione, il sistema mostra la lista di tutti i form disponibili, da cui scegliere quelli che servono.
![AAP_MOB_09](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_09.png)Per concludere, con lo sviluppo dello scenario è necessario aggiungere gli utenti che saranno autorizzati a operare.
![AAP_MOB_10](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_10.png)Definito lo scenario con le sue proprietà, occorre occuparsi dei palmari che saranno connessi al TwinPulse SyncServer.
![AAP_MOB_11](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_11.png)# Twinpulse Everywhere
![AAP_MOB_12](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_12.png)Questo componente è installato in ogni client e ha il duplice scopo di organizzare le comunicazioni con il sincronizzatore SyncServer e consente all'utente l'uso delle possibilità operative previste dagli scenari.
Sviluppato anch'esso con la tecnologia Microsoft.Net C-, incorpora il motore di DB Microsoft SQL Mobile. Con questo DB, l'utente può lavorare off line e scaricare le informazioni acquisite in relazione alle possibilità di collegamento.
Oltre a scaricare gli scenari, il client trasferisce al server tutti i dati gestionali raccolti. Ciò significa che l'utente può impegnare i prodotti e stabilirne la consegna con il palmare. Questa informazione è registrata nel database interno del dispositivo che, quando si connette al server, provvede al suo trasferimento.
Questo è il motivo per cui nel database di TwinPulse Mobile Platform sono registrati non solo tutti gli scenari, form, immagini, collezioni e utenti ma anche tutti i dati applicativi raccolti dal dispositivo mobile.
![AAP_MOB_13](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_13.png)
# Twinpulse Data Engine
Questo componente ha lo scopo di provvedere alla connessione con i diversi Sistemi informativi aziendali ovvero con i loro DB. Le sezioni create per ciascun palmare sono conservate nel TwinPulse Data Engine.  TwinPulse Data Engine è stato scritto con la tecnologia Microsoft.Net C- ed è fondamentalmente un motore di trasformazione XSLT. Attraverso semplici file scritti con tag predefiniti dal livello di XSLT, vengono create le particolarizzazioni
per diversi database.
![AAP_MOB_14](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_14.png)
# Twinpulse Business Objects
TwinPulse Mobile Platform è nato come un progetto per provvedere alle esigenze di mobilità delle aziende poichè sviluppa applicazioni all'altezza delle esigenze e le trasferisce al server di sincronizzazione. Naturalmente l'efficienza migliore si raggiunge con la maturità di un prodotto.
Nell'ultimo rilascio di prodotto, molte delle funzioni della piattaforma sono state migliorate ed espanse e altre di nuove si sono aggiunte. Questo significa che sono state generate nuove tabelle nel database e naturalmente nuovi webservices, con lo scopo di gestire le informazioni in modo sempre più funzionale e specializzato.
In accordo con la nostra esperienza, abbiamo creato una serie di oggetti preconfigurati che sono stati aggiunti al database e accessibili con gli appositi webservices.
Quando parliamo di oggetti di business ci riferiamo a clienti , fornitori, articoli, ordini, fatture clienti o fornitori, locazioni di magazzino ecc.. Ciascuno di questi oggetti può essere raggiunto da webservice creati specificatamente allo scopo.
L'insieme dei webservice che gestiscono gli oggetti di business è chiamato TwinPulse Business Objects. Essi sono accessibili via TwinPulse Everywhere, ma vi si potrebbe accedere anche da applicazioni esterne.
![AAP_MOB_15](http://localhost:3000/immagini/MBDOC_VIS-AAMOB/AAP_MOB_15.png)
# Twinpulse Mobile Applications
Questo documento vuole chiarire che con questa tecnologia si possono creare applicazioni per palmari che coprono le più svariate esigenze.
Tra le applicazioni che sono state sviluppate troviamo : 

### AUTOMAZIONE DELLE FORZA DI VENDITA
 * Gestione di contatti
 * Gestione degli ordini clienti
 * Amministrazione dei Punti vendita (POS)
 * Configurazione e prezzo dei prodotti

### SERVIZI AI CLIENTI
 * Gestione e traccia delle chiamate
 * Gestione dei clienti e dei ricambi
 * Guide di supporto tecnico e documentazione di prodotto
 * Gestione delle firme e approvazioni

### OPERAZIONI COLLEGATE ALL'ERP
 * Inventario
 * Logistica
 * Raccolta dati di produzione
 * Invio dati all'azienda per le attività svolte o ordini ricambi.
 * Cespiti
 * Gestione fianziaria

### APPLICAZIONI VERTICALI
 * Sanità :  Controllo e gestione della storia clinica dei pazienti.
 * Servizi di assistenza automobilistica.
 * Servizi di auditing.
 * Servizi di training :  Monitoraggio corsi e loro gestione.
 * Servizi di catering :  Prenotazione pasti e loro gestione.
