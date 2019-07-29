# Modulo esecuzione richieste batch

Per funzioni batch si intendono delle funzioni F eseguite in modo non presidiato all'interno di un ambiente non interattivo.
Tipicamente si tratta di funzioni che richiedono tempi di esecuzione medio lunghi e che non prevedono un output grafico su schermo ma la produzione di output cartacei o su file. Esempio tipico può essere la richiesta di un flusso di funzioni che porti alla produzione di un report stampato.

Le caratteristiche di una funziona batch sono le seguenti : 

 * Esecuzione non presidiata. La funzione deve essere entrocontenuta e deve essere autosufficiente in fase di esecuzione. Tutte le informazioni necessarie per l'esecuzione della funzione devono essere intrinseche nella funzione stessa e non deve mai essere richiesto l'input di informazioni aggiuntive.
 * Se previsto, l'output della funzione deve essere in un formato che non richiede interazione con l'utente. Quindi una funzione di tipo batch può produrre stampe, scrivere file, mandare mail ma non può visualizzare pannelli grafici informativi che richiedano una iterazione con l'utente.
 * Una funzione di tipo batch può essere eseguita in un determinato ambiente operativo e con un determinato utente. Ambiente e utente che possono essere diversi da quelli attivi nel momento in cui si richiede la sottomissione in batch di una funzione.
 * Deve essere fornito un pannello di controllo che consenta l'analisi dello stato di esecuzione delle funzioni batch sottomesse. Il pannello di controllo deve fornire tutte le informazioni utili a determinare lo stato di una richiesta batch ed eventualmente fornire indicazioni sulle cause di una eventuale default.

# Architettura operativa

Per la sua natura, l'esecuzione di una funzione batch non può avvenire su un normale client Looc.Up ma deve avvenire all'interno di una istanza di Looc.Up sempre attiva. Tipicamente la richiesta di esecuzione di una funzione batch viene inviata a una istanza di Looc.Up attiva in modalità server e costantemente reperibile nella rete.

Perchè una istanza di Looc.Up possa eseguire richieste in modalità batch è necessario che si verifichino le seguenti condizioni : 

 * L'istanza di Loocup deve essere sempre attiva (o per lo meno essere attiva quando è attivo il sistema AS400 servente)
 * L'istanza di Loocup deve essere accessibile da parte da tutte le altre istanze di Looc.Up presenti nella rete nonchè dal sistema AS400 stesso. Questo vuol dire che qualsiasi client Loocup presente sulla rete può inviare al server Looc.Up una richiesta di esecuzione di una funzione batch. Idem per l'AS400. Deve quindi esistere un canale di comunicazione che consenta l'invio al server Looc.Up delle richieste di esecuzione.
 * L'istanza di Loocu.Up deve poter avviare processi figli con ambienti e utenti diversi da quelli dell'istanza stessa.

L'elemento centrale dell'architettura per l'esecuzione di funzioni bacth è pertanto il Looc.Up server.


## Il server Looc.Up

Looc.Up Server è una istanza del client Looc.Up avviata in modo tale da abilitare e rendere disponibili alcune funzionalità tipiche di un server.

Rispetto ad una normale istanza di Looc.Up, una istanza di Looc.Up Server ha le seguenti prerogative : 

 * Un Looc.Up Server oltre ad abilitare le normali code di comunicazione verso AS400, abilita anche una coda speciale che consente l'invio di richieste da AS400 verso il server Looc.Up stesso. In altre parole, un normale client Looc.Up usa le code dati per inviare al sistema AS400 delle richieste di servizio e leggere i risultati, un Looc.Up Server consente anche l'inverso, cioè consente al sistema AS400 di inviare richieste al server e leggere i risultati. In pratica un Looc.Up Server può fornire servizi al sistema AS400 nello stesso modo in cui il sistema AS400 normalmente fornisce servizi al Looc.Up client.
 * Looc.Up Server fornisce il supporto ad una architettura client server. E' possibile fare in modo che un qualsiasi client Looc.Up che si avvii nella rete si registri anche sul server e venga creato un canale di comunicazione tra il server Looc.Up e tutti i client attivi nella rete e registrati sul server. Questa struttura client-server consente alcune forme di comunicazione normalmente non disponibili in un normale sistema basato sui soli client Looc.Up. In ogni momento il server Looc.Up può conoscere quali sono i client Looc.Up attivi sulla rete e, attraverso la loro identificazione univoca, può contattare il singolo client e inviare messaggi o richieste di esecuzione di funzioni. Sono quindi possibili una serie di funzionalità aggiuntive figlie di questo tipo di architettura centralizzata :  ad esempio, un client registrato può inviare messaggi o richiedere l'esecuzione di una funzione ad un altro client registrato. Oppure, il sistema AS400 può sfruttare il canale di comunicazione con il server Looc.Up per interagire con uno qualsiasi del client registrati, ad esempio chiedere che una data funzione F venga eseguita su un determinato client.
* Infine, un Looc.Up avviato in modalità server è il supporto ideale per l'esecuzione di funzioni batch. La presenza di un canale di comunizazione con AS400 consente al sistema gestionale di spedire richieste di esecuzione batch direttamente al Looc.Up server. Server che per sua natura è sempre attivo e quindi disponibile all'esecuzione delle funzioni richieste anche con schedulazioni particolari. Analogamente, qualsiasi istanza di Looc.Up attiva sulla rete e registrata al server può anch'essa sottomettere richieste batch al server, sfruttando i normali canali di comunicazione tra client e server. Infine, anche le istanze di Loocup non registrate possono comunque richiedere l'esecuzione di funzioni batch attraverso apposite funzioni che sfruttano il canale di comunicazione AS400-Looc.Up server.



Una istanza di Looc.Up può essere avviata in modalità server utilizzando l'opzione -server nella linea di comando.  Il server Looc.Up viene identificato attraverso un codice univoco, assegnato in fase di avvio del server stesso. L'assegnamento può avvenire in due modi distinti (ed esclusivi) : 

 * A linea di comando (opzione da preferire) :   l'istanza di Looc.Up che si vuole rendere server viene avviata con l'opzione aggiuntiva **--server : CODSRV : PORT** dove CODSRV (__max 6 caratteri) è il codice identificativo del server, mentre PORT è la porta socket usata dal server per la comunicazione con i client collegati e registrati. La specifica della porta socket è necessaria quando due istanze distinte di Looc.Up server vengono avviate su una stessa macchina.
 * Come property della JVM :   nella stringa di comando java che avvia il server Looc.Up aggiungere delle property java nel formato -DSmeup.smeui.uiserverside.name=CODSRV e -DSmeup.smeui.uiserverside.port=PORT. Questa soluzione è più adatta nei casi in cui l'avvio del server viene inserito come passo di uno script windows o unix e richiede una maggiore conoscenza tecnica dell'ambiente java.

## Esecuzione di una funzione batch

Supponiamo di avere una generica funzione : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho))

non è importante entrare nel merito della funzione stessa. E' solo importante sapere che questa funzione è l'esecuzione di un flusso di azioni abbastanza complesso che porta alla produzione di un report cartaceo spedito per email. E' quindi una tipica funzione che ben si adatta ad una sottomissione in batch, visto che non richiede iterazione con l'utente, è asincrona e lunga da eseguire ed ha un output di tipo non grafico.

Per poter eseguire la funzione in modalità batch sono due i problemi da risolvere : 

 * Fare in modo che la funzione venga in qualche modo riconosciuta da Looc.Up come funzione da eseguire in modalità batch
 * Fare in modo che la funzione sia effettivamente eseguita in modalità batch all'interno di un ambiente abilitato all'esecuzione di questo tipo di funzioni

Analizziamo distintamente le due problematiche.

## Problema 1 :  richiedere l'esecuzione di una funzione in modalità batch

Il primo problema (richiedere che una funzione sia eseguita in batch) si risolve indirizzando l'esecuzione della funzione verso uno specifico plugin denominato BATCH. All'interno di Looc.Up l'esecuzione di una qualsiasi funzione può essere reindirizzata verso uno specifico modulo indicando nel campo SERVER della funzione il codice del plugin che dovrò gestirla.

Quindi, per fare in modo che una funzione qualsiasi sia eseguita in modalità bacth **è sufficiente aggiungere alla funzione stessa la notazione SERVER(BATCH) ed eseguire la funzione stessa in un Looc.Up avviato in modalità server.

Nel caso specifico la funzione precedente diventa : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho))**SERVER(BATCH)**


Il plugin BATCH è attivo solo in istanze di Looc.Up avviate in modalità server, quindi la precedente richiesta di funzione verrà eseguita in modalità batch solo se richiesta ad una istanza di Looc.Up che si trovi in questa modalità. Se la precedente richiesta di funzione fosse richiesta ad una normale istanza client di Looc.Up si riceverebbe una segnalazione di errore e la funzione verrebbe abortita senza alcuna esecuzione.

Nella maggioranza dei casi, l'esecuzione di una funzione di tipo batch richiede l'immissione di alcune informazioni aggiuntive che specifichino meglio l'ambiente operativo di esecuzione.

Tipicamente, è necessario specificare il contesto con cui verrà eseguita la funzione, ambiente che verrà identificato dall'utente e dall'ambiente AS400.

Queste informazioni possono essere inserite all'interno del campo P della funzione da sottomettere in batch, specificando i parametri **BchUsr**, **BchPwd** e **BchEnv**.

La funzione precedente diventerà quindi del tipo : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)**BchUsr(UTENTE)BchPwd(PASSWORD)BchEnv(0010)**)**SERVER(BATCH)**

la precedente notazione indica che la funzione F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)) venga eseguita in modalità batch in un ambiente identificato dall'utente UTENTE (con password PASSWORD) e ambiente operativo 0010.

Si noti che in questa prima versione del modulo di esecuzione batch la pwd dell'utente di esecuzione deve essere specificata in chiaro all'interno della richiesta di funzione stessa. Verrà comunque criptata in una successiva versione oppure sostituita con un meccanismo centralizzato di gestione delle pwd basato sul modulo Single Sign On.


## Problema 2 :  inviare la funzione da eseguire in batch ad un server Looc.Up

Nel punto precedente si è visto come dichiarare, all'interno della sintassi di una funzione, che la funzione stessa venga eseguita in modalità batch all'interno di un certo ambiente.

Ora il problema è quello di fare in modo che la richiesta di esecuzione arrivi ad un server Looc.Up, cioè fare in modo che l'esecuzione della funzione avvenga in un ambiente abilitato all'esecuzione di funzioni di questo tipo.

Come già detto in precedenza, il supporto alle funzioni di tipo batch prevede che nella rete ci sia un server Looc.Up attivo e correttamente configurato. Questo server sarà il luogo deputato all'esecuzione di tutte le funzioni batch necessarie, a prescindere da dove provenga la richiesta. Quindi a prescindere dalle condizioni in cui ci si trovi, la possibilità di eseguire o meno in batch una determinata funzione è legata direttamente alla possibilità o meno di sottomettere questa funzione sul server Looc.Up

Fissiamo quindi un ambiente operativo di esempio, che vede la presenza all'interno di una rete di un server Looc.Up configurato e avviato e univocamente identificato da un codice CODSRV.

Le richieste di esecuzione di una funzione in modalità batch possono provenire da vari attori : 

 * Dal sistema AS400
 * Da un client Looc.Up registrato e identificato sul server Looc.Up
 * Da un client Looc.Up attivo sulla rete ma non registrato sul server Looc.Up
 * Da sistemi esterni (schedulatore di Windows, programmi esterni...)


Analizziamo le varie casistiche.

### Richieste provenienti da AS400 (costruttore LOA27)

E' il caso in cui il sistema AS400 di riferimento deve richiedere al server Looc.Up identificato dal codice CODSRV l'esecuzione di una specifica funzione in modalità batch.

Un esempio molto frequente legato a questa casistica è quello dello schedulatore di sistema dell'AS400 :  questo modulo fornisce la possibilità di schedulare l'esecuzione di alcune funzioni in modalità batch con frequenza e occorrenza definite da opportune regole di schedulazione. In questo caso il sistema gestionale decide quando eseguire determinate funzioni e si trova nella necessità di inviare la richiesta di esecuzione in modalità batch direttamente al server Looc.Up di riferimento.

La sottomissione di una richiesta batch verso un server fa uso del programma **LOA27_BT**.
La sintassi del progrmma è del tipo : 

CALL PGM(LOA27_BT) PARM('COD_SCRIPT')

dove COD_SCRIPT è il codice univoco che identifica la funzione da eseguire all'interno dello script di setup (SCP_SET) della funzione LOA27.

Vediamo un esempio di script, più precisamente lo script 01 salvato nel membro LOA27_01 della libreria SCP_SET : 

 :  : PAR T(Esempio script LOA27_01 in SCP_SET) F(04)

   -  :  : SEZ Cod="A01" Txt="Funzioni singole"
   -  :  : SUB Cod="B01" Txt="Esempio 1"
   -  :  : A27.BTC CdSrv="SRVSVI" CdUsr="USER" CdPwd="PWD" CdIu=""  Fun="A(EMU;B£SER_85;MAI.OGG) 1(;;01.A02.B06) INPUT(SJ(PDF Vendor Rating) TX(In allegato Vendor Rating))"

   -  :  : SEZ Cod="A02" Txt="Flussi"

   -  :  : SUB Cod="B01" Txt="Esempio Flusso 1"
   -  :  : A27.BTC CdSrv="SRVSVI" CdUsr="USER" CdPwd="PWD" CdIu=""  Fun="F(FLU;LOA11_SE;FLU.ESE)  1(;;53.01.03)"

   -  :  : SUB Cod="B02" Txt="Esempio Flusso 2"
   -  :  : A27.BTC CdSrv="SRVSVI" CdUsr="USER" CdPwd="PWD" CdIu="P_SVI"  Fun="F(FLU;LOA11_SE;FLU.ESE)  1(;;98.A01.B01)"

   -  :  : SUB Cod="B03" Txt="Esempio Flusso generazione PDF in SMEDEV"
   -  :  : A27.BTC CdSrv="SRVTST" CdUsr="USER" CdPwd="PWD" CdIu="SVI"  Fun="F(FLU;LOA11_SE;FLU.ESE)  1(;;ES.A01.B09)"





Il precedente scrip definisce 4 funzioni batch : 

 * 01.A01.B01 :  funzione A(EMU;B£SER_85;MAI.OGG) 1(;;01.A02.B06) INPUT(SJ(PDF Vendor Rating) TX(In allegato Vendor Rating)) lanciata su server SRVSVI con utente USER e password PWD
 * 01.A02.B01 :  funzione F(FLU;LOA11_SE;FLU.ESE)  1(;;53.01.03) lanciata si server SRVSVI con utente USER e pwd PWD
 * 01.A02.B02 :  funzione F(FLU;LOA11_SE;FLU.ESE)  1(;;98.A01.B01) lanciata sul server SRVSVI con utente USER, password PWD e ambiente P_SVI
 * 01.A02.B03 :  funzione F(FLU;LOA11_SE;FLU.ESE)  1(;;ES.A01.B09) lanciata sul server SRVTST con utente USER, password PWD e ambiente SVI

In particolare, una singola funzione batch è identificata dai seguenti parametri : 

 * **Codice** :  codice univoco che identifica nello sctipr SCP_SET/LOA27_nn la funzione batch (ad esempio, 01.A01.B01)
 * **CdSrv** :  codice del server che dovrà eseguire la funzione batch
 * **CdUsr** :  utente di esecuzione della funzione batch
 * **CdPwd** :  password utente esecutore della funzione batch (in chiaro)
 * **CdIu** :  ambiente (oggetto IU) di esecuzione della funzione batch
 * **Fun** :  funzione da eseguire in batch

L'editazione dello script di setup della funzione LOA27 può avvenire direttamente nella scheda LOA27 attraverso la selezione dell'azione Set'n Play disponibile all'interno della scheda stessa.

### Richieste provenienti da un client Looc.Up registrato

Un client Looc.Up è registrato sul server quando è stato avviato utilizzando la modalità --client. In questa modalità il client non appena avviato si registra sul server e apre un canale di comunicazione privilegiato che gli permette di ricevere o di inviare messaggi o richieste di comando verso il server o verso qualunque altro client registrato.

Supponiamo che il client debba richiedere al server su cui è registrato l'esecuzione in modalità batch della funzione F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho))

La richiesta può essere semplicemente immessa eseguendo sul client la funzione : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)BchUsr(USR)BchPwd(PWD)BchEnv(ENV)) SERVER(BATCH) CLIENT(SERVER)

Analizziamo la sintassi : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)**BchUsr(USR)BchPwd(PWD)BchEnv(ENV)**) **SERVER(BATCH)** CLIENT(SERVER)

le parti in neretto sono state aggiunte per trasformare la richiesta di funzione da normale funzione in funzione batch, secondo quento detto in precedenza.

A questo punto è necessario forzare l'esecuzione della funzione su un client diverso da quello attuale. Questo si ottiene con la seguente notazione : 

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)BchUsr(USR)BchPwd(PWD)BchEnv(ENV)) SERVER(BATCH) **CLIENT(SERVER)**

che va letta come "esegui la funzione in un client diverso da quello in cui è stata richiesta e identificato dal codice SERVER". Dato che in una architettura Loocup client-server anche il server viene identificato come se fosse un client della rete stessa, la notazione CLIENT(SERVER) equivale a dire "esegui sul server".


### Richieste provenienti da un client Looc.Up non registrato

Anche se non è una soluzione consigliabile, è comunque possibile che un client Looc.Up possa inviare una richiesta di esecuzione di una funzione batch verso un server Looc.Up su cui non è registrato.

Il meccanismo è simile al caso precedente, con una sola piccola differenza, evidenziata in neretto nella stringa di comando seguente.

F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)BchUsr(USR)BchPwd(PWD)BchEnv(ENV)) SERVER(BATCH) CLIENT(SERVER**.CODSRV**)


Questa notazione identifica il server verso cui inviare la richiesta attraverso il suo codice identificativo CODSRV.

In pratica, la funzione precedente va letta come :  _"esegui la funzione F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01 .03) P(For(NSho)) in modalità batch con ambiente USR-ENV sul server identificato dal codice CODSRV (anche se il client non è collagato direttamente a quel server)"




### Richieste provenienti da un programma esterno

Attraverso le API di sistema fornite da Looc.Up, è possibili richiedere ad un server Looc.Up l'esecuzione di una specifica funzione in modalità bacth.

Ad esempio, consideriamo il seguente spezzone di script bat di Windows.

_
cd C : \Programmi\LoocUp
set classpath=.\Loocup.jar;.\libs\jt400.jar;.\libs\jwebbrowser\jna-3.0.7.jar;.\libs\jwebbrowser\jna_WindowUtils.jar;
java Smeup.smeui.uiserverside.UILoocupServerTester AS400_ID USR PWD SRV_CODE "F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01.03) P(For(NSho)) SERVER(BATCH)"


Questo script sottomette sul server Looc.Up identificato dal codice SRV_CODE l'esecuzione in bacth della funzione F(FLU;LOA11_SE;FLU.ESE) 1(;;53.01.03) P(For(NSho)).

La sottomissione passa dal sistema AS400 verso cui è collegato il server Looc.Up, identificato dalla tripletta AS400_ID, USR e PWD







