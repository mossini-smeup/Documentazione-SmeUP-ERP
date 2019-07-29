
## Installazione locale del client Looc.Up con sincronizzazione su server

### Introduzione

Oltre alle modalità di installazione locale e su server viste nel paragrafo precedente, è possibile una terza modalità di installazione di Looc.Up che, a fronte di una procedura di installazione più complessa, unisce i vantaggi delle due modalità.
Il concetto di base è semplice :  installare su una macchina di rete (server) una copia di riferimento di Looc.Up e fare in modo che le installazioni locali di Looc.Up (client) presenti sui vari PC della rete si mantengano automaticamente allineati con la versione di riferimento presente sul server.

Questa tipologia di installazione presenta vari vantaggi : 

* Looc.Up viene installato in locale sulle singole macchine quindi ha prestazioni migliori rispetto ad una installazione server
* L'aggiornamento delle singole installazioni di Looc.Up non richiede l'intervento manuale su tutti i PC su cui il client è installato ma solo l'aggiornamento della copia di riferimento sul server.
* Oltre a facilitare l'aggiornamento di Looc.Up, il sistema di sincronizzazione permette di semplificare anche il processo di installazione dei singoli client.

Per contro, l'attivazione di una sincronizzazione richiede una procedura di installazione e setup più complessa rispetto a quella delle installazioni client o server.


### La soluzione

L'installazione di Looc.Up con sincronizzazione tra client e server richiede l'utilizzo del plugin **Loocup Rsync Plugin** scaricabile dal sito di distribuzione di Looc.Up.

Il Loocup RSync Plugin è uno specifico plugin di Looc.Up che consente la sincronizzazione automatica dei singoli client Looc.Up con una installazione di riferimento presente su un server condiviso.
In questa particolare modalità, ad ogni avvio di un client Looc.Up viene fatto un confronto tra la versione locale del programma e la versione di riferimento installata sul server. Nel caso vengano trovate delle differenze, il client locale viene automaticamente allineato allo stato del server e quindi aggiornato.
Il processo di controllo e aggiornamento viene effettuato prima dell'avvio di Looc.Up, in modo tale che quando il client si avvia sia sicuramente aggiornato.
E' quindi una modalità che consente di avere installazioni locali di Loocup mantenendo però la possibilità di effettuare upgrade centralizzati. Per aggiornare tutti le installazioni di Loocup presenti nella rete è sufficiente aggiornare la versione di riferimento sul server e attendere che l'aggiornamento si propaghi su tutte le macchine controllate al primo avvio di Loocup successivo all'aggiornamento.
Il Loocup RSync Plugin basa il suo funzionamento sul software cwRsync, versione per sistemi operativi Windows del noto comando RSync presente sui sistemi Linux.

Dal processo di sincronizzazione sono comunque esclusi alcuni file ed alcune cartelle di Looc.Up. Gli elementi esclusi sono gli elementi che non possono essere sincronizzati liberamente senza alterare il funzionamento del client stesso oppure gli elementi che contengono file di lavoro non distribuiti con l'installatore ma creati dal client durante il suo funzionamento.

 T(Attualmente, con la versione V3R2M120301 di Looc.Up, la lista degli elementi esclusi dalla sincronizzazione è la seguente : )
- Cartella "LOOCUP_CAH"
- Cartella "LOOCUP_CON"
- Cartella "LOOCUP_DAT"
- Cartella "LOOCUP_LOG"
- Cartella "LOOCUP_OUT"
- Cartella "LOOCUP_PRF"
- Cartella "LOOCUP_TMP"
- Cartella "LOOCUP_WRK"
- File "esclusioni.txt"
- Tutti i file con estensione *.log
- Il file "Loocup.exe"
- Il file "Smeupgo.exe"
- Il file "Loocup_w.exe"
- Il file "Loocup_con.exe"
- La cartella "cwrsync"



### Modalità di installazione

L'attivazione del Loocup RSync Plugin prevede l'installazione di un modulo server su una macchina di rete (solitamente il server di rete stesso) e l'installazione di un client su tutti i PC locali che si vorranno sincronizzare con il server.
Il pacchetto di installazione scaricato contiene due sottocartelle, una marcata server e una marcata client. La prima conterrà le istruzioni e i programmi necessari per l'installazione lato server, la seconda quelli necessari per il lato client.

### Installazione lato server

Sul server devono essere installati due moduli. Il servizio RSync, necessario per il motore di sincronizzazione, e la copia di Looc.Up che verrà considerata come riferimento per la sincronizzazione.
Per le seguenti istruzioni fare riferimento al contenuto della cartella "server" presente nel pacchetto di installazione.


- Se l'installazione avviene su un server con sistema operativo Windows 2003 eseguire le operazioni preliminari descritte nel file "patch_Win2003.txt"
- Installare sul server il prodotto utilizzando il file di installazione cwRsync_Server_4.0.4_Installer.exe. Si consiglia di avviare l'installatore con le autorizzazioni di amministratore :  per far questo, cliccare con il tasto destro del mouse sull'eseguibile dell'installatore e selezionare la voce "Esegui come amministratore" (se disponibile).Utilizzare le impostazioni di setup di default (installazione come servizio Windows). Viene installato un servizio denominato RSyncServer
- Nella lista dei servizi di Windows, selezionare il servizio RSyncServer e impostare l'avvio automatico del servizio all'avvio di Windows. Avviare il servizio. Se l'avvio non va a buon fine modificare l'utente associato  al servizio e impostare al posto dell'utente SwcwRsync un utente amministratore del sistema.
- Copiare nella directory di installazione del server cwRsync i file rsyncd.conf e esclusioni.txt.
- Installare sul server una copia di Looc.Up. Sarà l'installazone di riferimento per la sincronizzazione, quella che andrà aggiornata per propagare l'aggiornamento sui singoli client sotto controllo.
- Nel file rsyncd.conf settare correttamente la directory in cui è installata sul server la copia di riferimento di Loocup. Il formato di definizione delle directory è quello del framework cyg :  attenersi all'esempio inserito nel file rsyncd.conf per avere un esempio
  su come definire il path.
- Sempre nel file rsyncd.conf settare correttamente il path del file esclusioni.txt copiato al punto 3. Anche per questo punto vale la nota sul formato di definizione del path  vista al punto precedente.
- Sempre nel file rsyncd.conf settare correttamente la directory in cui è installata sul server la copia di riferimento di LoocupLibs (directory libs posta nella directory di installazione della copia di riferimento di Loocup sul server), sempre con il  formato cyg.



### Installazione lato client

Per le seguenti istruzioni fare riferimento al contenuto della cartella "client" presente nel pacchetto di installazione.

 :  : T04 Installazione con setup automatico (disponibile dalla versione V3R2M121109 Spighe Blu di Looc.Up)

Con questa modalità, l'installazione del client Looc.Up con sincronizzazione si limita a pochi passaggi.


- Scaricare dal sito di download di Looc.Up il file **Setup_Rsync_XXXXXX.zip** dove XXXX è il numero della versione corrente (ad esempio Setup_Rsync_V3R2M121109)
- Scompattare il file scaricato ed eseguire il file **setup_rsync.exe** in esso contenuto
- Seguire le indicazioni del wizard di installazione e completare il processo di installazione
- Sul desktop del PC viene creato un collegamento **Smeup RSync**. Cliccare con il tasto destro del mouse e selezionare la voce proprietà dal menù di popup.
- Nel campo "Destinazione" della finestra visualizzata sostituire la stringa XXX.XXX.XXX.XXX con l'indirizzo IP del server di sincronizzazione.
- Ripetere la stessa operazione del punto precedente per la voce "Sme.UP Rsync" del menù Sme.UP presente nel menù di avvio di Windows.



 :  : T04 Installazione manuale del client

Per l'installazione manuale  del client Looc.Up con sincronizzazione ci sono due diverse opzioni.
La prima  non prevede l'installazione del client Looc.Up sul PC in locale. Il client verrà scaricato automaticamente dal server al primo avvio, attraverso la sincronizzazione stessa.
La seconda opzione invece prevede l'installazione manuale del client Looc.Up sul PC locale. Con questa opzione, il client Looc.Up viene registrato sul sistema locale tra le applicazioni installate e vengono creati i link sul desktop.
A livello funzionale le due opzioni si equivalgono.

Prima opzione : 


- Copiare tutto il contenuto della cartella "client" (contenuta nel pacchetto Rsync scaricato) nella cartella del PC locale in cui si vorrà installare Looc.Up


Seconda opzione : 


- Installare il client Loocup sul PC locale, usando il setup apposito.
- Copiare la directory "cwrsync" (contenuta nella directory client del pacchetto Rsync scaricato ) nella directory dove è stato installato Looc.Up (di default è C : /Programmi/Loocup per i sistemi a 32 bit e C : /Programmi (x86)/Loocup per sistemi a 64 bit)


### Avvio del sistema e utilizzo


- Avviare il servizio RSync sul server di riferimento
- Sul client locale da sincronizzare, avviare loocup con il comando : 

 Smeupgo.exe --sync : XXX.YYY.ZZZ.KKK

dove

   XXX.YYY.ZZZ.KKK :  l'indirizzo IP del server su cui è installato ed attivo il server RSync.

L'opzione --sync può essere inserita in aggiunta alle altre opzioni già presenti nella linea di comando.

Esempio : 

      Smeupgo.exe AS400IP USER PWD --sync : 168.168.1.1

oppure (per versioni precedenti a Looc.UP Tarassaco Blu)

      Loocup.exe AS400IP USER PWD --sync : 168.168.1.1


**Nota per versioni di Looc.Up successive alla V3R2M120301**

L'esecuzione della procedura di sincronizzazione può essere attivata anche nel caso si scelga di avviare Looc.Up con la nuova procedura di avvio Smeup Go disponibile a partire dalla versione V3R2M130608 di Looc.Up. In questo caso la sincronizzazione non avviene alla partenza del client Looc.Up stesso, ma all'avvio del modulo di connessione, specificando il comando : 

Smeupgo.exe --sync : XXX.YYY.ZZZZ.KKK

la sincronizzazione avverrà prima della visualizzazione del modulo di gestione delle connessioni


