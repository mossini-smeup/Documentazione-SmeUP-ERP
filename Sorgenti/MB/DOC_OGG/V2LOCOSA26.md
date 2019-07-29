# Introduzione
Il costruttore A26 è stato pensato come interfaccia generica per l'integrazione di Smeup con documentali.
Il costruttore non è stato pensato per un documentale specifico ma cerca di raggruppare delle caratteristiche comuni a più documentali per poter definire un insieme di funzionalità comuni.

## Tipologia di archiviazione
Il servizio base di archiviazione si chiama LOA26_SE.  Esiste uno script di configurazione chiamato LOA26SET presente in SCP_SET.
In questo script vengono definiti i parametri per il collegamento al server preposto all'archiviazione è possibile : 
* definire la tipologia di archiviazione con il tag **A26.SET Tip="XX"** dove **"XX"** è il codice identificativo del modulo di archiviazione. (Es :  AB=Archibox; ME=Medusa), questo parametro definisce anche il nome del pgm di exit LOA26_XX;
* definire la cartella base del software di archiviazione con il tag **A26.KEY Mod="KEY" Cod="IFSDIRBASE";
* definire la cartella metadata con il tag **A26.KEY Mod="KEY" Cod="IFSDIRDATA"**, questa sarà la cartella dove verranno depositati i file xml o txt di transito neccesari alla generazione dell'etichetta per l'archiviazione (archiviazione passiva);
* definire la cartella allegati con il tag **A26.KEY Mod="KEY" Cod="IFSDIRALL"**, questa sarà la cartella dove verranno depositati i file prodotti dal gestionale pronti per essere trasferiti al software di archiviazione (archiviazione attiva);
* definire l'indirizzo ip del server documentale con il tag **A26.KEY Mod="KEY" Cod="IPSER"**;
* definire l'user e la password per l'accesso al server documentale con i tag **A26.KEY Mod="KEY" Cod="USER"** e **A26.KEY Mod="KEY" Cod="PWD"**;
* definire l'archivio di default con il tag **A26.KEY Mod="KEY" Cod="ARCDFT"**;
* definire il path base per il reperimento dei documenti **A26.KEY Mod="KEY" Cod="SRVDIRBASE"**;
di seguito un esempio : 
// Esempio
SUB Cod="B02" Txt="Archiviatore generico"
 A26.SET Tip="XX"
 A26.KEY Mod="KEY" Cod="IFSDIRBASE" Des="Cartella base     " Val="/Cartella/base/"
 A26.KEY Mod="KEY" Cod="IFSDIRDATA" Des="Cartella metadata " Val="file_dainserire"
 A26.KEY Mod="KEY" Cod="IFSDIRALL"  Des="Cartella allegati " Val="allegati_da_spedire"
 A26.KEY Mod="KEY" Cod="IPSER"      Des="Server Documentale" Val="172.16.2.60"
 A26.KEY Mod="KEY" Cod="USER"       Des="User              " Val="Administrator"
 A26.KEY Mod="KEY" Cod="PWD"        Des="Password          " Val=""
 A26.KEY Mod="KEY" Cod="ARCDFT"     Des="Archivio def.     " Val="smea"
 A26.KEY Mod="KEY" Cod="SRVDIRBASE" Des="Directory base    " Val=""
 A26.KEY Mod="KEY" Cod="IPCLIENT"   Des="Client per gestione" Val="172.16.2.61"


### Funzioni archiviazione
L'archiviazione è predisposta per soddisfare una serie di funzioni base. Il servizio LOA26_SE è predisposto per soddisfare o dichiarare alcune funzioni rimandando la specifica implementazione di archiviazione alle exit dichiarate nello script di configurazione.
Le funzioni disponibili sono : 
* Archiviazione tramite chiamata "batch" BTC.ARC (richiamabile o in LoocUp o tramite £UID da un prrogramma di stampa)
* Archiviazione "batch" in cui non passo il file da allegare BTC.ARC.NF (richiamabile o in LoocUp o tramite £UID da un prrogramma di stampa)
* Archiviazione tramite scheda di LoocUp LOC.ARC
* Matrice contenente i documenti archiviati di un oggetto ALL.DOC (dato oggetto e catalogo)
* Esistenza documento archiviato ESI.DOC (ritorna V2 SI/NO richiamabile tramite A(EMU;LOA26_SE;ESI.DOC)  )
* Scansione esistenza oggetto SCA.ESI (ritorna un albero SE GRU.A26 con gli elementi trovati);


* Matrice raccoglitori MAT.RAC (ritorna una matrice di documenti) (todo)
* Matrice documenti MAT.DOC (ritorna la matrice  dei documenti - ogni documentale sceglie la modalità di filtri e di presentazione) (todo)


## Script di configurazione costruttore A26
Tramite lo standard di script definito dal costruttore A07 le categorie di archiviazione sono realizzate tramite la relazione : 
SCRIPT - SEZIONE DELLO SCRIPT - SOTTOSEZIONE

Ad esempio potremmo avere
nello script in SCP_SET **LOA26_01** : 
* SEZIONE A01 - SOTTOSEZIONE B01 che potrebbe rappresentare archiviazioni con documentale 01(a livello di script), archiviazione di documenti (a livello di sezione), archiviazione fatture passive (a livello di sottosezione)
* SEZIONE A01 - SOTTOSEZIONE B02 che potrebbe rappresentare con documentale 01(a livello di script), archiviazione di documenti (a livello di sezione), archiviazione fatture attive (a livello di sottosezione)
* SEZIONE A02 - SOTTOSEZIONE B01 che potrebbe rappresentare con documentale 01(a livello di script), archiviazione di disegni CAD (a livello di sezione), archiviazione disegni CAD commesse (a livello di sottosezione)

nello script in SCP_SET **LOA26_02** : 
* SEZIONE A01 - SOTTOSEZIONE B01 che rappresenta archiviazioni con documentale 02(a livello di script), archiviazione di disegni CAD (a livello di sezione), archiviazione disegni CAD commesse (a livello di sottosezione)

Gli elementi qui sopra sono identificati univocamente dalle triplette di codici 01-A01-B01, 01-A01-B02, 01-A02-B01, 02-A01-B01 ...

### Elementi dello script

Andremo ora ad analizzare una singola sottosezione (elemento dello script SUB) che identifica una specifica archiviazione.
L'elemento A26.SET identifica una serie di impostazioni x la sottosezione. Tra le chiavi abbiamo : 
* **TipArc  **&nbsp;&nbsp;la tipologia di documentale (lo stesso codice inserito nel tag A26.SET Tip="XX" dello script di configurazione);
* **Rac  **&nbsp;&nbsp;il cod. raccoglitore che rappresenta il contenitore per quella tipologia di documenti;
* **TpOg**  e  **PaOg  **&nbsp;&nbsp;permettono di identificare il tipo e parametro dell'oggetto di riferimento passato a questa subsezione;
* **Tpcfg  **&nbsp;&nbsp;non operativo;
* **CdCfg  **&nbsp;&nbsp;non operativo;
* **Ope  **&nbsp;&nbsp;operazione su archiviazione INSERT per inserire un nuovo file, UPDATE per modificarlo, DELETE per cancellarlo (oprativo INSERT, il resto da implementare);
* **Arc  **&nbsp;&nbsp;archivio al quale puntare per il reperimento dei documenti;

Gli elementi A26.KEY definiscono le chiavi per quel particolare raccoglitore definito nel A26.SET.
E' possibile esprimere il valore della chiave in due modi, scrivendo un valore fisso, oppure reperimento tramite OAV dell oggetto definito nei parametri **TpOg**  e  **PaOg**

Esempio con valori fissi : 

 A26.KEY Mod="KEY" Cod="DTAIMM" Val="20101001" Des="Data immissione foto"
 A26.KEY Mod="KEY" Cod="NRPIX" Val="1024" Des="Numero di pixel"
 A26.KEY Mod="KEY" Cod="TIPIMG" Val="JPEG" Des="Tipo di immagine"

identifica le tre chiavi passate con 3 valori di default (i campi **Val**)

Esempio con OAV per tipo "DO" : 

**Codice ente documento  **A26.KEY Mod="OG" Cod="FIELD1" Val="**&OA.I/17**" Des="Cliente"
**Ragione sociale  **A26.KEY Mod="OG" Cod="FIELD2" Val="**&OD.I/17**" Des="Ragione sociale"
**data documento  **A26.KEY Mod="OG" Cod="FIELD3" Val="**&OA.I/03**" Des="Data Doc" Tip="D8"  Par="*DMYY" SpD8="/"; in questo caso, avendo l'attributo di ritorno tipo e parametro D8*YYMD, è possibile specificare il formato della data ed il separatore da utilizzare **Tip="D8"  Par="*DMYY" SpD8="/" per avere una data in questo formato GG/MM/AAAA;
**anno della data  **A26.KEY Mod="KEY" Cod="ANNO"   Val="&OA.I/03%J/B09"   Des="Anno" è possibile con la sintassi **&OA.I/03%J/B09** avendo l'attributo **I/03** come tipo e parametro "D8*YYMD" è possibile concatenare con il carattere "&" un attributo relativo all'oggetto, in questo caso **J/B09** che è l'anno dell'oggetto data;

identifica le quattro chiavi passate con 4 valori reperiti da OAV (i campi **Val**)


## Servizio di archiviazione
L'archiviazione può essere effettuata in due modalità : 
* archiviazione interattiva in LoocUp
* archiviazione batch

Il servizio che si occupa di archiviare è il costruttore LOA26_SE.
Tramite la scheda LOA26 è possibile provare la modalità di archiviazione interattiva.
Per richiamare il costruttore in modalità batch si veda il programma di esempio LOA26_BT.
Esempio : 
 **A(EMU;LOA26_SE;BTC.ARC)  1(CN;COL;Q1) 2(;;ES.A01.B01)  INPUT(FileName(arctest.txt) FilePath(/DOORuP/archivist) DTAIMM(20110102) NRPIX(512) TPIMG(GIF))

dove nel cod. 1 definisco il cod. di riferimento dell'archiviazione, nel cod. 2 la sezione dello script e nel campo di input il file da archiviare (FileName), il path da cui recuperare il file (FilePath) e le chiavi eventualmente valorizzate nel caso non si voglia sfruttare il valore di default dello script o la modalità di calcolo tramite OAV.

## Tipologie di operazioni
Tramite il tag Ope del setup della subsezione è possibile indicare varie modalità di utilizzo del costruttore : 
* archiviazione
* collegamento (o graffetta) tra due documenti archiviati

### Archiviazione
Permette di archiviare un documento secondo la logica vista nel paragrafo Servizio di archiviazione

### Collegamento (graffetta)
Tramite l'operazione di graffetta è possibile "allegare" ad un documento archiviato 1 o più documenti archiviati che per qualche logica devono essere collegati ad esso. Ad esempio ad un documento di fattura del raccoglitore FATCLI possono essere collegate le sue bolle del raccoglitore BOLCLI.

Esempio di subsezione per graffettare una fattura con una bolla : 
SUB Cod="B04" Txt="Graffetta/Collega fattura con bolla"
A26.SET Tip="ARCHIBOX" Rac="FATCLI" TpOg="FT" PaOg="" Ope="GRAFFETTA"
A26.KEY Mod="RIF" Cod="BOL01" Tip="DODA" Des="Bolla collegata" Rac="BOLCLI"

Richiamando più volte in modo questa sub sezione è possibile collegare le varie bolle.

## TODO Archiviazione - aggiornato al 27/04/12
### Alta priorità
- **Generale** - Gestione luoghi
* Un luogo ha delle proprietà
* Un luogo ha un percorso
* Un luogo ha un tipo, è un oggetto ?
* Nei luoghi devo includere note strutturate/script/mod. tecniche
* Un luogo ha associato un flusso (zippa/rinomina) o un workflow
* un luoghi chiamama il motore di archiviazione e se non ha tutti gli elementi parte un G30 con questionario
- **Generale** - Spostare la definizione dei parametri di archiviazione dalla tabella provvisioria X01 ad uno script FATTO GIAGI 30/04/12
- **Generale** - Spostare gestione JATRE_23C in un costruttore introducendo il concetto di autorizzazioni/vincolo immagini-funzioni FATTO CC 30/04/12
- **Generale** - Portare un esempio semicompleto dei luoghi di un cliente con flussi  e altro
- **Generale**  - Collegarsi a lavoro di Oliviero su copia/incolla
- **Archibox** - Lettura web service  da AS400
- **Medusa** - capire come fare ad avere un modellino in sviluppo

### Media priorità
- Feedback sulla sostitutiva (dovrebbe ricalcare quanto fatto per il feedback)
- Scrivere documento creazione raccoglitore in Archibox. Documentare template di raccoglitore Archibox
- Loggare su JALOGT dei dati inviati con la tabella PGM
- Riusciamo ad archiviare mail post lettura IMAP servizio JA_00_03 (capire bene la tematica e mettere giù passi)
### Bassa priorità
- Un documento applicativo che serve per illustrare a clienti/colleghi cosa si intende archiviazione documentale e alle sue possibili soluzioni (tra cui Archibox)
- Verificare che nell'installazione siano indicati precisamente i prerequisiti per fare in modo che la soluzione nata in Sviluppo sia replicabile anche presso un cliente (installazione Archibox sia server che client, configurazione degli script AS400, installazione del plugin di Smeup che legge il web service di Archibox, installazione del web service SmeUp che permette di ricevere il feedback da Archibox ... altro)
- Web Service di Feedback. Pensare a una modalità di richiamo multiplo di un web service e di autenticazione utente che esegue un operazione sul web service.
-- Per esempio :  il web service potrebbe notificare archiviazione di file per 3 realtà aziendali diverse. Concetto di autenticazione utente che gestisce le connessioni del Web Service verso AS400.(utente applicativo/utente di connessione)
- Autorizzazioni in lettura raccoglitori : 
-- Capire se introdurre il tema di autenticazione di un utente su un catalogo (autorizzazioni specifiche)
-- Capire autorizzazioni di Archibox (non importante) vedere con loro se tenerle allineate

## Vedi anche
- [Server Archibox](Sorgenti/MB/DOC_OGG/V3_CSE_09)
- [Interfaccia Archiviazione Archibox](Sorgenti/MB/DOC/ODIAAB)
- [Interfaccia Archiviazione Medusa](Sorgenti/MB/DOC/ODIAME)

