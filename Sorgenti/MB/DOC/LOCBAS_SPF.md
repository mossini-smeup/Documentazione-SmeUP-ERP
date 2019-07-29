# Sme.UP HTTP Restful API

Sme.UP, tramite Sme.UP Provider, espone delle API Restful, che permettono di eseguire delle fun (chiamate standard ai programmi Sme.UP).

## Comunicazione
La comunicazione avviene in tre fasi
- Autenticazione :  crea la sessione di lavoro e restituisce un token
- Chiamata :  esegue le chiamate (fun), usando il token
- Disconnessione :  chiude la sessione e rilascia il token

# Elenco dei servizi

##  AuthenticateService
Servizio per l'autenticazione e la verifica di una sessione.

### Metodo 1 :  Autenticazione
Serve per autenticare un utente ad operare con il provider.
L'autenticazione viene svolta con le credenziali che l'utente utilizza per collegarsi all'AS400.
Viene creata una sessione nello SmeupProvicer analoga a quella che si crea quando un utente si collega con Loocup.

http(s)://indirizzo_provider:porta/AuthenticateService?server=nome_as400&usr=utente_As400&pwd=password_AS400&env=ambiente_smeup&device=dispositivo

|  Nam="Parametri AuthenticateService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| 
| .COL Txt="Note" |
| server|Nome AS400|Nome AS400 a cui collegarsi |Facoltativo|se non fornito usato quello del provider |
| usr|Utente|Utente AS400|Obbligatorio| |
| pwd|Password|Password utente|Obbligatorio| |
| env|Ambiente|Ambiente applicativo|Obbligatorio| |
| device|Dispositivo|Tipo di dispositivo utilizzato per collegarsi |Facoltativo|Se non passato usa C (cliente grafico) |
| enc|Smeup Encoding|Chiave del file encodings.xml|Facoltativo|Se non passato usa il default del file |
| 


Viene restituito un XML di questo tipo : 
<Base>
  <Oggetto Codice="1432823301049_424" J8_HASH_KEY="uyjkceERTygrcuiogeKLWEFD" ProviderTime="20150528142831"/>
    <Messaggi>
      <Messaggio Testo="L'utente XXXYYY è autorizzato ad accedere al server srvyyyzzz.smeup.com, ambiente SVI" Livello="20" Tipo="INFO"/>
      <Messaggio Testo="Autenticato il 28.maggio.2015 16 : 28 : 31 : 221" Livello="20" Tipo="INFO"/>
      <Esito Stato="OK"/>
   </Messaggi>
</Base>

Il nodo Oggetto ha i seguenti attributi : 
 * Codice :  è Il codice di connessione univoco che andrà usato in tutte le richieste successive
 * J8_HASH_KEY :  è la chiave di hash (se definita)
 *  ProviderTime :  è l'ora in cui il provider ha risposto, riportata al GMT. Serve per determinare le differenze temporali tra il client e il provider.

### Metodo 2 :  check
Serve per verificare se una sessione è ancora attiva.
Restituisce OK se lo è oppure un'eccezzione ser non lo è.

URL chiamata : 

http(s)://indirizzo_provider:porta/AuthenticateService?check=codice_connessione

|  Nam="Parametri" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| check|Controlla| Controlla la sessione :  verifica che il valore poassato sia di una sessione attiva|Obbligatorio |
| 



## DisconnectService :  servizio per la chisura di una sessione (disconnessione)

http(s)://indirizzo_provider:porta/DisconnectService?codcon=codice_connessione


|  Nam="Parametri DisconnectService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| codcon|Codice Connessione|Codice Connessione|Obbligatorio |
| 

N.B. Le sessioni vengono mantentute da SmeupProvider per 30 minuti

## XMLService :  servizio per la lettura di XML
Riceve una Fun e restituisce un XML.
esempio
http(s)://indirizzo_provider:porta/XMLService?codcon=codice_connessione&fun=F(EXB;......)&timestamp=0150203155433&hash=sgnfkcqcweafhjjhdfcjhsfdgjhugjh&outfor=JSON/XML

Casi particolari : 
Se riceve come fun = PING, non richiama l'AS400 ma azzera il timeout sulla sessione.
Se la richiesta è di tipo
 * F(G53;....
 * F(EXC;....
 * F(FRM;...
 * F(REP;...
non viene restituito l'XML ma viene eseguita la funzione come se fosse un'azione grafica e il file generato viene restituito al chiamante.


|  Nam="Parametri XMLService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| codcon|Codice Connessione|Codice Connessione|Obbligatorio |
| fun|Funzione|La funzione da richiamare|Obbligatorio |
| hash|Hash|l'hash di codice connessione, fun e timestamp|Facoltativo |
| timestamp|Timestamp|Il timestamp della richiesta nel formato AAAAMMGGhhmmss nel greenwich time epurato del delta client server|Facoltativo |
| outfor|outfor|Formato della risposta per la matrice. Default XML, se uguale a JSON genera output in formato JSON|Facoltativo |
| 



**Paginazione**
Nel caso il risultato di una chiamata ad una FUN fosse un XML con paginazione, per ottenere le "n" pagine di dati successive, occorre effettuare "n" chiamate alla FUN contenuta nell'attributo Exec del nodo XML di tag  <UIPopup> che ha Codice="*NEXT" ,  vediamo un esempio : 

La seguente FUN restituisce un xml con paginazione : 
F(EXB;LOA10_SE;EQR) 1(;;) 2(;;) INPUT(Q1Tip(TA) Q1Par(B£AMO) Q1Qry(*KEY) Qry(Yes) Focus() NAg())

come si può notare, la porzione di XML sottostante mostra la relativa FUN da chiamare (nodo Oggetto Testo="SEGUE") per ottenere i successivi record : 
...
<Riga Fld="|000102|TAB£AMO|CQAUDT|Audit"/>
<Riga Fld="|000102|TAB£AMO|CQBASE|Base Qualità"/>
</Righe>
-<UIPopup>
<Oggetto Testo="F07=INSERIMENTO".../>
<Oggetto Testo="SEGUE" Fld="" Exec="F(EXB;LOA10_SE;EQR) 1(TA;B£AMO;) INPUT(Q1Tip(TA) Q1Par(B£AMO) Q1Qry(*KEY) Qry(Yes) Focus() NAg() PAG_NRI(100) QRPAG(CQBASE)) SS(Context(B£EQRY_SEA/List) CGr(EXB) ID({FBBBD136-6CDB-400D-ADCC-6DFF85021D13}) CONAP(B£))" Codice="*NEXT" Parametro="KEY" Tipo="J1" Leaf="" Mode="EXT.PAG" Nome=""/>
<Oggetto Testo="BASE" .../>
<Oggetto Testo="F13=GESTIONE FILTRO" .../>
<Oggetto Testo="F22=SET'N PLAY {01}" .../>
</UIPopup>
...

richiamando quindi la FUN contenuta nell'attributo Exec="....", e aggiungendo nel P il PAG(YES), si otterranno i dati della pagina successiva.
Ovviamente l'XML potrebbe a sua volta contenere nuovamente la FUN da rilanciare per la successiva pagina.
Nel caso in cui invece esista il nodo UIPopup, con Codice="*NEXT" ma senza Exec, dovrà essere rilancata la fun iniziale, indicando sempre PAG(YES) nel P.

## CommandService
Riceve una fun ed esegue il comando relativo. Se il comando è di aprire una scheda, si avrà l'effetto che sul provider verrà aperta la relativa scheda. Questo servizio va pertanto utilizzato solo in quei casi in cui il comando è senza emissione di grafica.

Casi particolari : 
se la modalità grafica della fun è G(BCH) viene eseguita senza attendere la risposta

esempio : 
http(s)://indirizzo_provider:porta/CommandService?codcon=codice_connessione&fun=F(EXB;......)&timestamp=0150203155433&hash=sgnfkcqcweafhjjhdfcjhsfdgjhugjh


|  Nam="Parametri CommandService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| codcon|Codice Connessione|Codice Connessione|Obbligatorio |
| fun|Funzione|La funzione da richiamare|Obbligatorio |
| hash|Hash|l'hash di codice connessione, fun e timestamp|Facoltativo |
| timestamp|Timestamp|Il timestamp della richiesta nel formato AAAAMMGGhhmmss nel greenwich time epurato del delta client server|Facoltativo |
| 



##  ResourceService :  servizio per la gestione delle risorse remote.
Con risorse remote si intendono file raggiungibili da SmeupProvider tramite protocollo SMB.
ResourceService espone le seguenti funzionalità : 
 * Consente di restituire un file al chiamate (se è nei path a cui è stato autorizzato tramite la variabile PROVIDER_PATHS)
 * elencare il contenuto di una cartella
 * cancellare un file e o cartelle (se sono  nei path a cui è stato autorizzato tramite la variabile PROVIDER_PATHS)
 * verificare l'esistenza di file e o cartelle

esempio di chiamata : 
http(s)://indirizzo_provider:porta/ResourceService?codcon=codice_connessione&path=\\server001\azienda01\clienti\C0010\offerte\offerta01.doc&timestamp=0150203155433&hash=sgnfkcqcweafhjjhdfcjhsfdgjhugjh


|  Nam="Parametri ResourceService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| codcon|Codice Connessione|Codice Connessione|Obbligatorio |
| action|Azione da compiere|Azione da copiere :  valori possibili list, delete, check|Facoltativo |
| path|Percorso|Percorso della risorsa|Obbligatorio |
| hash|Hash|l'hash di codice connessione, fun e timestamp|Facoltativo |
| timestamp|Timestamp|Il timestamp della richiesta nel formato AAAAMMGGhhmmss nel greenwich time epurato del delta client server|Facoltativo |
|  |
| 


L'azione di default è get, ovvero viene restituito un file, altrimenti viene restituito un XML.

## UploadService :  servizio per uplodare risorse sul server

Funziona in POST, la chiamata va quindi eseguita o tramite una pagina HTML mettendo nell'action del form http(s)://indirizzo_provider:porta/UploadService, oppure in modo programmatico.


|  Nam="Parametri UploadService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| codcon|Codice Connessione|Codice Connessione|Obbligatorio |
| WTX_FILE|File da uplodare|Part|Obbligatorio |
| WTX_FSDEST|Destinazione|Cartella o path di destinazione. E' possibile caricare risorse solo nelle cartella a cui il provider è stato autorizzato tramite la variabile PROVIDER_PATHS|Obbligatorio |
| WTX_DESTYPE|Tipo destinazione|Indica se la destinazione indicata è un file o una cartella valori FILE o DIR|Facoltativo |
| WTX_OVERWRITE|Sovrascrivi|Abilita la sovrascrittura se vale 1|Facoltativo |
| WTX_LASTMODIFIED|Data modifica|Numerico che indica la data di ultima modifica come timestamp|Facoltativo |
|  |
| 



##  UpdaterService :  servizio di updater
Questo servizio viene utilizzato dall'updater per gestire gli aggiornamenti del client.

Funzionamento



|  Nam="Parametri UpdaterService" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| action|Azione|Azioni ammesse :  info-restituisce il file version.info, md5-restituisce il file con l'md5 dell'archivio. Se non fornito l'azione di default è download |Facoltativo |
| op|Operation|Operazione se vale RELEASE, faà scaricare tutta la cartella dell'installazione specificata dal parametro version. Se definito il file force_version.info viene ingorato|facoltativo |
| version|Versione|La versione di cui fornire le informazioni |Obbligatorio |
| p|Parametri|Parametri aggiuntivi, liberamente gestiti dal client|Facoltativo |
|  |
| download|Download|Consente di specificare un file da inviare al client. il file deve essere nella cartella di installazione del provider, sottocartella download|Facoltativo |
|  |
| 


# Appendice

## L'algoritmo di calcolo dell'hash

Il calcolo dell'hash è eseguito usando
* **l'algoritmo di hashing**, SHA1.
* **il character encoding** UTF-8 (da verificare)
* codice di connessione parametro **codcon**
* timestamp parametro **timestamp**
* **un segreto condiviso** tra le due applicazioni, secondo quanto definito nel file di configurazione
* i parametri facoltativi

L'ordine in cui vengono concatenati i campi
Suppondendo, ad esempio, di utilizzare **SHA1**, **UTF-8**, ed il segreto condiviso  **WEBUP91818$** ( modificato di comune accordo tra chi implementa il client chi implementa il server), avremmo il seguente algoritmo in pseudo codice : 

_String stringToHash= codcon + parametri facoltativi + timestamp +  "WEBUP91818$";_

_byte[] byteToHash= encode("UTF8",stringToHash);_

_byte[] calculatedHash = hashFunction("SHA1", byteToHash);_

_if(calculatedHash != recievedHash)_
_    return "INVALID REQUEST";_

## Gestione delle sessioni e dei timeout

Se la una connessione non viene utilizzata per 30 minuti viene invalidata.
Per tenerla attiva senza sprecare risorse macchina, è sufficiente chiamate la funzione PING

esempio
http(s)://indirizzo_provider:porta/XMLService?codcon=12345678&fun=**PING**&timestamp=0150203155433&hash=sgnfkcqcweafhjjhdfcjhsfdgjhugjh


## Come Debuggare
Questo servizio è richiamabile sempre (anche direttamente da un browser).
Nasce per fornire un feedback immediato sullo stato e sulla raggiungibilità dello Smeup Provider.
Si richiama tramite l'URL http(s)://indirizzo_provider:porta/debug, ad esempio:  https://providertest.smeup.com/debug.

Risponde una pagina html  con informazioni tecniche : 
- AS400 a cui è connesso
- informazioni sulla richiesta HTML
- le variabili dello smeup provider
- alcune funzioni tecniche




