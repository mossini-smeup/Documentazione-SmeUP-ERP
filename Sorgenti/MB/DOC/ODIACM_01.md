# Server di interfaccia all' IBM ContentManager.

## Prerequisiti
Ad eccezione del servizio **CNTF** descritta di seguito, per funzionare correttamente l'estensione Loocup di interfaccia all'IBM Content Manager necessita di avere installato sulla macchina l'IBM DB2 Client da utilizzare come layer di comunicazione di base al database del Content Manager.

La seguente procedura va attuata per rendere il PC in grado di collegarsi al Content Manager tramite Loocup.

### Installazione Client Db2

- Unzip del file "DB2 v8 Runtime client.exe"
- Esecuzione del file "setup.exe" con installazione tipica (e nulla di più)
- Catalogare il database del content manager attivando la finestra dei comandi

![CM1](http://localhost:3000/immagini/ODIACM_01/CM1.png)
Immettendo le seguenti 2 righe : 
>db2 catalog tcpip node <nome fittizio> remote <IP CM> server <porta tcpip>
db2 catalog database icmnlsdb at node <nome fittizio della riga precedente> authentication server


### Installazione Information Integrator for content

- Eseguire il comando **DB2 Information Integrator for Content 8.2 Windows English.exe**
- Selezionare l'opzione **EIP Development Workstation**

![CM2](http://localhost:3000/immagini/ODIACM_01/CM2.png)
- Dopo aver impostato i path, selezionare il connettore per il Content Manager V8

![CM3](http://localhost:3000/immagini/ODIACM_01/CM3.png)
Ed esempi associati
![CM4](http://localhost:3000/immagini/ODIACM_01/CM4.png)
- Lasciare le impostazioni di default per la parte RMI
- Impostare l'indirizzo web http://dev01/CMConf/ come fonte condivisa con il server Content Manager (questo passo non mi è del tutto chiaro :  io ho messo, anziché dev01, l'indirizzo IP del server che ha installato il servizio Content Manager)

![CM5](http://localhost:3000/immagini/ODIACM_01/CM5.png)

- Impostare la password dell'utente "icmconct"

![CM6](http://localhost:3000/immagini/ODIACM_01/CM6.png)
Nota bene :  fare l'uncheck della voce "Catalog remote EIP database"!


- Ripetere l'immissione della password
- Fine per attivare l'installazione


### Setup ambiente di compilazione
 Le variabile CMBROOT e DB2HOME dovrebbero essere già imposte


## Fase di setup del client Loocup
**Questa fase e obbligatoria per qualsiasi funzione richieamata tramite il plugin**.
La fase di installazione del plugin per interfacciarsi all'IBM Content Manager prevede diversi step.

- Se si è mantenuto il default nell'installazione dei programmi IBM, copiare la cartella LIB presente in c : \CMBROOT ridenominandola come CM nella cartella lib presente nella cartella di installazione di Loocup.
- Copiare nella cartella CM appena creata anche i files db2java.zip, sqlj.zip, cmbxmlservice.jar, db2jcc.jar, db2jcc_.jar, db2jcc_license_cisuz.jar, db2jcc_license_cu.jar, TViewerDefaultIcons.jar. A questo punto nella cartella libs/CM presente nella cartella di installazione di Loocup il contenuto dovrebbe essere il seguente : 

> T(Directory di C : \Programmi\Loocup\libs\CM)
18/09/2006  18.11    < DIR >          .
18/09/2006  18.11    < DIR >          ..
02/09/2004  20.33         1.429.828 cmb81.jar.
02/09/2004  20.33         1.423.347 cmbcm81.jar.
02/09/2004  20.28           231.783 cmbdb281.jar.
02/09/2004  20.28           130.446 cmbdb2c81.jar.
02/09/2004  20.28           231.086 cmbdj81.jar.
02/09/2004  20.28           130.219 cmbdjc81.jar.
02/09/2004  20.38         1.461.184 cmbfed81.jar.
02/09/2004  20.38           979.306 cmbfedc81.jar.
02/09/2004  20.27         3.177.410 cmbicm81.jar.
02/09/2004  20.27         1.838.954 cmbicmc81.jar.
07/04/2003  13.27             9.722 cmbicmcup.jar.
02/09/2004  20.29           235.753 cmbjdbc81.jar.
02/09/2004  20.33           134.952 cmbjdbcc81.jar.
02/09/2004  20.29             6.771 cmblog4j81.jar.
02/09/2004  20.26        10.539.266 cmbsdk81.jar.
02/09/2004  20.26           105.478 cmbservlets81.jar.
02/09/2004  20.26            76.997 cmbtag81.jar.
02/09/2004  20.26            90.332 cmbupes81.jar.
02/09/2004  20.29           210.305 cmbutil81.jar.
02/09/2004  20.38            19.890 cmbutilfed81.jar.
02/09/2004  20.29            19.842 cmbutilicm81.jar.
02/09/2004  20.26             3.967 cmbutiljdbc81.jar.
02/09/2004  20.26         1.353.965 cmbview81.jar.
02/09/2004  20.27             2.619 cmbwas81.jar.
02/09/2004  20.26            38.082 cmbwcm81.jar.
02/09/2004  20.26           100.265 cmbxmlservice.jar.
24/10/2002  06.33         1.230.904 db2java.zip.
15/09/2004  17.59         1.230.597 db2java_.zip.
24/10/2002  06.33           663.346 db2jcc.jar.
15/09/2004  17.59             2.063 db2jcc_license_cisuz.jar.
15/09/2004  17.59             1.013 db2jcc_license_cu.jar.
07/04/2003  15.52             7.438 EIPUser2WF.jar.
07/04/2003  12.31         3.909.254 essrv.jar.
02/09/2004  20.27            97.830 icmrm81.jar.
15/09/2004  17.59         1.512.844 sqlj.zip.
07/04/2003  16.10             3.111 TViewerDefaultIcons.jar.
              37 File     32.640.169 byte
               2 Directory  16.599.687.168 byte disponibili


- Avviare Loocup.


## Fase di test delle nuove funzioni di Loocup

### Servizio RTVF (ReTrieVe File)
Con l'installazione delle nuove funzioni è disponibile un nuovo servizio **RTVF** sul server CM che reperisce dati e risorse sul server Content Manager.
Tale servizio è fornito di metodi che eseguono diversi tipi di accesso ai dati del Content Manager.
Tali tipi di acesso (che chiameremo metodi della funzione o metodi) sono :  DTA, IMG, VIE e VIE.OPN.
Questi metodi accettano alcuni parametri e restituiscono dei dati che possono essere visualizzati in schede di Loocup.
 T(Di seguito prenderemo in considerazione i metodi ed il loro utilizzo.)
- DTA fornisce i dati per una sezione tabella (EXB) della scheda di Loocup. Per il momento vengono ritornati tutti i campi presenti nel documentale con l'aggiunta di un campo nascosto di codice IMG-ID che riporta l'identificatore usato da loocup per identificare il file risorsa (per intenderci il .tiff salvato nel Content Manager) collegato. Nel campo parametro della funzione di Loocup accetta diversi tipi di valore : 
-- il Tipo Documento da ricercare ( I valori ammessi sono BOL o FAT) :  esprimibile tramite la sintassi TD(BOL) o TD(FAT). Se non viene espresso il default è la fattura;
-- il codice DOcumento corrispondente nel caso delle fatture con il campo Barcode del documento fattura sul Content Manager o il campo N. Protocollo del documento bolla sul Content Manager :  esprimibile tramite la sintassi DO(codice documento);
-- la DAta del documento corrispondente alla Data BEM nel caso della bolla o al campo Data fattura nel caso della fattura :  esprimibile tramite la sintassi DA(data fattura/BEM), compatibilmente con il formato della data registrata
-- il campo Ragione Sociale corrispondente a Ragione Sociale fornitore :  esprimibile tramite la sintassi RS(ragione sociale). Esempi : 
--- F(EXB;RTVF;DTA) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(TD(BOL) DO(051737224)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione matrice della scheda (EXB) relativi alle bolle con N. Protocollo 051737224
--- F(EXB;RTVF;DTA) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(RS(ACME SRL) TD(FAT)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione matrice della scheda (EXB) relativi alle fatture del fornitore con ragione sociale ACME SRL
--- F(EXB;RTVF;DTA) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(RS(ACME SRL) TD(FAT) DA(30/06/2005)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione matrice della scheda (EXB) relativi alle fatture del fornitore con ragione sociale ACME SRL in data 30 giugno 2005
--- F(EXB;RTVF;DTA) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(TD(FAT) DA(30/06/2005)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione matrice della scheda (EXB) relativi alle fatture registrate in data 30 giugno 2005
--- F(EXB;RTVF;DTA) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(TD(BOL) DO(051737224)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione matrice della scheda (EXB) relativi alla bolla con N. protocollo 051737224.

- IMG fornisce i dati per una sezione HTM della scheda di Loocup per l'accesso alle risorsa documento (il .tiff) salvato nel Content Manager e recuperate tramite il metodo DTA. Accetta come tipo di valore  della funzione un solo tipo valore : 
-- L'IDentificatore di Loocup che corrisponde al valore assunto dal campo IMG-ID esposto nel punto precedente. E' esprimibile tramite la sintassi LID(valore di IMG-ID). Esempi : 
--- F(EXB;RTVF;IMG) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(LID(A1001001A05I06A91928G64076)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione HTM per la visualizzazione del file che è stato caricato in una sezione matrice tramite il metodo DTA.

- VIE similmente al metodo precedente fornisce i dati per una sezione HTM della scheda di Loocup l'accesso alle risorsa documento (il .tiff) salvato nel Content Manager. A differenza del metodo IMG recupera il file utilizzando i parametri gestiti nel Content Manager : 
-- il Tipo Documento da ricercare ( I valori ammessi sono BOL o FAT) :  esprimibile tramite la sintassi TD(BOL) o TD(FAT). Se non viene espresso il default è la fattura;
-- il codice DOcumento corrispondente nel caso delle fatture con il campo Barcode del documento fattura sul Content Manager o il campo N. Protocollo del documento bolla sul Content Manager :  esprimibile tramite la sintassi DO(codice documento). Esempi : 
--- F(EXB;RTVF;VIE) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(DO(051009487) TD(FAT)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione HTM per la visualizzazione del file di fattura salvato nel Content Manager con barcode 051009487.

- VIE.OPN similmente al metodo precedente fornisce l'accesso ad una risorsa documento salvata nel Content Manager attraverso gli stessi parametri ma successivamente al suo reperimento ne provoca la visualizzazione attraverso l'applicazione che il sistema operativo ha registrato senza il veicolo della sezione di una scheda.
-- I parametri sono simili al metodo precedente. Esempi : 
--- F(EXB;RTVF;VIE.OPN) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(DO(051009487) TD(FAT)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  provoca la visualizzazione del file di fattura salvato nel Content Manager con barcode 051009487 tramite l'applicazione che il sistema operativo usa di default.


### Servizio CNTF (CoNnecT File)
Con l'installazione delle nuove funzioni è disponibile un nuovo servizio **CNTF** sul server CM che permette di visualizzare i file archiviati nel Content Manager attraverso il web server che esso mette a disposizione.
Tale servizio è fornito del metodo VIE che visualizza i files contenuti nel Content Manager.

 T(Di seguito prenderemo in considerazione i metodi ed il loro utilizzo.)
- VIE fornisce i dati per una sezione HTM della scheda di Loocup e da l'accesso alle risorsa documento salvato nel Content Manager collegandosi al web server di quest'ultimo. A differenza del metodo IMG recupera il file utilizzando i parametri gestiti nel Content Manager : 
-- il Tipo Documento da ricercare ( I valori ammessi sono BOL o FAT) :  esprimibile tramite la sintassi TD(BOL) o TD(FAT). Se non viene espresso il default è la fattura;
-- il codice DOcumento corrispondente nel caso delle fatture con il campo Barcode del documento fattura sul Content Manager o il campo N. Protocollo del documento bolla sul Content Manager :  esprimibile tramite la sintassi DO(codice documento). Esempi : 
--- F(EXB;CNTF;VIE) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P(DO(051009487) TD(FAT)) G(NFI) SP() SG()) NOTIFY()) SERVER(CM)  :  genera i dati per una sezione HTM per la visualizzazione del file di fattura salvato nel Content Manager con barcode 051009487.


## La sintassi delle interrogazioni
### I parametri
Il nome dei parametri è libero, quindi qualunque campo del record documento del Contentn Manager può essere usato come nome parametro per l'interrogazione con questa notazione NOMECAMPO(VALORE). Se il VALORE viene riportato con almeno una wildcard % l'operatore usato sarà LIKE, altrimenti sarà =. Di default le varie condizioni sui campi verranno messe in OR, a meno che nel parametro non si specifichi l'operatore di AND tramite OP(AND). In questo caso tutte le condizioni verranno messe in AND. Non c'è la possibilità di negare o di mescolare AND e OR. Per questo tipo di flessibilità è necessario usare il Query Language del Content Manager.
Di default le varie condizioni sui campi verranno messe in OR, a meno che nel parametro non si specifichi l'operatore di AND tramite OP(AND). In questo caso tutte le condizioni verranno messe in AND. Non c'è la possibilità di negare o di mescolare AND e OR. Per questo tipo di flessibilità è necessario usare il Query Language del Content Manager (vedi la sezione seguente).

### Il Content Manager Query Language
Un'altra possibilità di interrogare il Content Manager è quella di utilizzare una query espressa attraverso il Content Manager Query Language e passata nel campo P() della funzione tramite il parametro CMQuery(). Se è presente questa definizione all'interno del campo P() della funzione Loocup, tutto il resto eventualmente espresso in P() non viene considerato, quindi la query e solo quella viene passata al Content Manager. Purtroppo nella sintassi delle funzioni Loocup le parentesi graffe sono riservate al richiamo dei valori delle variabili, quindi, per questa incompatibilità sintattica fra il parser delle funzioni di Loocup e il Content Manager Query Language, le eventuali parentesi quadre presenti nella query vanno sostituite rispettivamente con  : 

- [ con &q
- ] con q&


Di seguito alcuni esempi di chiamate.

Le seguenti tre chiamate sono equivalenti nelle tre differenti sintassi supportate e rappresentano quella che ad ora è la funzione presente nella scheda COS001XCM : 

- Vecchia sintassi :  F(EXB;RTVF;VIE) P(TD(FAT) DO([DOCBCD])) SERVER(03)
- Content Manager Query Language (da notare la sostituzione delle parentesi quadre della query con &q e q&) :  F(EXB;RTVF;VIE) P(CMQuery(/FATTURE&q(@BARCODE = "[DOCBCD]")q&)) SERVER(03)
- Parametri liberi :  F(EXB;RTVF;VIE) P(TD(FATTURE) BARCODE([DOCBCD])) SERVER(03)


Altre funzioni di esempio : 

- F(EXB;RTVF;DTA) P(TD(FATTURE) CFRAG(%LA%) OP(AND) BARCODE(%0053%) FCPIV(%9%)) G(NFI) SERVER(03) ---- Fatture con LA nella ragione sociale e partita iva che contiene un 9
- F(EXB;RTVF;DTA) P(CMQuery(/FATTURE&q(@FCPIV LIKE "%9") AND (@BARCODE LIKE "%0053%") AND (@CFRAG LIKE "%LA%")q&)) G(NFI) SERVER(03) ---- Fatture con FCPIV (partita iva) che finisce per 9 e Barcode contenente 0053 e Ragione sociale contenente LA


## Utilizzo standalone dell'interfaccia al Content Manager
E' possibile utilizzare la libreria uicm.jar anche al di fuori di Loocup come estrattore di documenti contenuti nel Content Manager.
In questo caso l'applicazione si compone del file uicm.jar (il plugin Loocup per l'IBM Content Manager) e il file run.bat. Tramite il file batch run.bat è possibile, dopo averne sistemato la configurazione in esso contenuta, richiamare il file immagine del documento per la visualizzazione con l'applicazione relativa. Nel file batch sono presenti gli estremi per la sua configurazione.
Se si dispone di una installazione centralizzata di Loocup si può valutare di installare il file uicm.jar e il file run.bat nella cartella delle librerie di Loocup, mappandola poi come unità di rete per ovviare ai problemi che il file .bat presenta con i percorsi UNC.

E' necessario passare come parametro del file batch la funzione che serve per reperire il documento nel Content Manager.
Essa dovrà indicare il tipo documento e il codice documento (il barcode) con cui esso è stato caricato nel sistema.
La funzione in questione sarà del tipo **TD(FAT)DO(0112367)** ed è simile quella che viene inserita nel parametro P() delle funzioni Loocup per l'accesso ai documenti da Loocup.

Il richiamo del file batch, ad esempio da una sessione Client Access deve passare attraverso meccanismi di RPC come la G53 di Smeup, lo strpco dell'AS o applicazioni simili.

Per quanto rigurda la G53 di seguito un esempio di chiamata, attraverso la TST relativa, per la visualizzazione di un documento contenuto nel Content Manager : 

![G53](http://localhost:3000/immagini/ODIACM_01/G53.png)
### Parametri per l'utilizzo della G53
 T(Di seguito i parametri per la chiamata del visualizzatore da G53)
- **£G53FU** :  EXEC
- **£G53ME** :  PGM
- **£G53NF** :  run.bat
- **£G53PA** :  < percorso della cartella contenente il file run.bat >
- **£G53PP** :  dati relativi al tipo documento e codice documento. Per le regole sintattiche della G53/smens si rimanda alla documentazione relativa


Per vincoli relativi ai caratteri non supportati nei parametri della G53 la stringa che viene passata nella variabile £G53PP deve sottostare a tali vincoli :  i caratteri ( e ) non sono supportati e vanno sostituiti con i tag -ORB- (Open Round Brace) e -CRB- (Closed Round Brace). Quindi, come si nota nell'immagine per esprimere la stringa **TD(FAT)DO(0112367)**  nella variabile £G53PP si deve trasformare tale valore in **TD-ORB-FAT-CRB-DO-ORB-0112367-CRB-** . **N.B. : ** La caratteristica di poter sostituire caratteri proibiti con tag è supportata da versioni SMENS lato AS400 successiva al gennaio 2005.

L'utilizzo della G53 prevede la presenza (attivata) del server SMENS sul PC sul quale deve essere visualizzato il documento

**NB 1 : ** per poter utilizzare l'applicazione al di fuori di Loocup deve essere installata sul PC la Java Virtual Machine.

**NB 2 : ** per l'utilizzo standalone dell'estrattore di documenti devono sempre essere soddisfatti i prerequisiti riportati nei punti **1.1** e **1.2**

