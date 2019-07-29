## Introduzione alla gestione utenti in Web.UP

Essendo una delle interfacce di Sme.UP ERP, Web.UP utilizza le stesse modalità di accesso al sistema di Looc.UP
* Indirizzo server
* Utente
* Password
* Ingresso utente
Questo significa che un utente, per accedere a Web.UP, deve possedere un profilo as400 e un B£U e un ambiente compatibile a Looc.UP

Tuttavia in ambito web possono nascere esigenze differenti, ad esempio può essere necessario far accedere utenti che non hanno un profilo as400.
Per questo motivo sono state create diverse modalità di Login che supportando le esigenze più varie.

ATTENZIONE :  per ogni modalità di login è importante chiedersi quale sarà l'utente as400 del job.

WebUP gestisce quattro tipologie di login : 
* USRPRF
* FUN
* ROLES
* DIRECT

Per accedere alla configurazione dei moduli di login (aggiunta, cancellazione, modifica) occorre premere la combinazione di tasti CTRL+SHIFT+F8, inserire
la password richiesta ed aggiornare la pagina.

![WEBASE_031](http://localhost:3000/immagini/WEBASE_011/WEBASE_031.png)
compariranno tre nuove voci : 
-Main config (configurazione generale)
-Login module config (modifica login già esistenti)
-Create new login module (crea nuovi moduli di login)

![WEBASE_032](http://localhost:3000/immagini/WEBASE_011/WEBASE_032.png)

Nella sezione "Create new login module" si possono creare i moduli di login necessari, impostando tipologia (una delle quattro accennate in precedenza e descritte a seguire) e
le credenziali di accesso per la connessione.
![WEBASE_033](http://localhost:3000/immagini/WEBASE_011/WEBASE_033.png)
Occorre poi andare nella sezione "Main config" per abilitare il modulo all'utilizzo, diversamente non sarebbe utilizzabile.
Per fare ciò occorre spostarlo tramite drag&drop nella colonna di destra come in figura : 
![WEBASE_034](http://localhost:3000/immagini/WEBASE_011/WEBASE_034.png)
Una volta effettuato il salvataggio delle impostazioni, in maniera automatica si aggiornerà la pagina, disabilitando le tre voci di configurazione e facendo comparire il nuovo modulo
di login creato : 
![WEBASE_035](http://localhost:3000/immagini/WEBASE_011/WEBASE_035.png)



# User Profile (USRPRF)

Utilizzata per accedere lasciando all'utente la possibilità di cambiare i parametri d'accesso (solo quelli che non sono già impostati).
Questa modalità usa l'utente di sistema operativo.
Connessione :  n utenti b£u -> n job (LO_Exxxxxx)

![WEBASE_018](http://localhost:3000/immagini/WEBASE_011/WEBASE_018.png)
![WEBASE_011](http://localhost:3000/immagini/WEBASE_011/WEBASE_011.png)
# Login External

Web.UP supporta la modalità di login che abbiamo definito definito  "External", che permette di autenticare l'utente attraverso i normali moduli di login, ma senza presentare la form di login.
Questa modalità supportata da tutti i moduli di login, **è pensata soprattutto per l'integrazione con altre applicazioni web.

La pagina da chiamare è

_/views/webupExtLogin.jsf_

a cui, a seconda del tipo di modulo di login utilizzato, dovvranno essere passati  dei parametri.

### Esempio di chiamata

http://mauer.smeup.com/AreaRiservata/views/webupExtLogin.jsf?
**mod**=areaRiservata
&**p**=mauro.sanfilippo@smeup.com
&**t**=20150429075751
&**hash**=828895f2ee6139d5b8ddaaca05510a6f8b3aceb7
&**callBack**=http://areariservata.smeup.com/area-demo/web-up-3.html
&**sfuncion**=CLI
&**var**=A(B)C(DD)E(FFFF)


### Parametri delle chiamata
I parametri sono definiti nelle seguenti tabelle, per ogni tipologia di login


### Moduli di tipo FUN

Utilizzata per contesti in cui si vuole gestire l'accesso di "n" utenze senza dover creare i relativi utenti di sistema operativo.
Nella modalità standard, occorre creare le "n" utenze necessarie nella tabella JAU.
Al momento del submit della form, verrà chiamato il servizio (fun) WEJAU_01 che riceverà utente/password digitati e, una volta verificate le credenziali nella tabella JAU,
restituirà un xml di matrice monoriga contenente tutti i campi della tabella JAU e permetterà quindi l'accesso al sistema.
Il valore di ogni campo della matrice sarà inoltre disponibile all'interno delle schede SmeUP (nel contesto WebUP) nella forma *WebUser.<nomeCampo> (es :  *WebUser.T$JAUF).
Il servizio è estendibile a piacimento e può quindi restituire una matrice arricchita di tutti i dati necessari.
Ad esempio, aggiungendo alla matrice il campo XXABCD, lo stesso sarà poi disponibile nelle schede come [*WebUser.XXABCD].
Serve comunque un utente di sistema operativo per la connessione "master", diversamente non sarebbe possibile effettuata la chiamata al servizio WEJAU_01.
Per ulteriori dettagli implementativi si veda di seguito.
Connessioni :  n utenti jau -> n job (LO_Exxxxxx) N.B. in questo caso ogni job sarà comunque intestato al medesimo utente master!

![WEBASE_019](http://localhost:3000/immagini/WEBASE_011/WEBASE_019.png)![WEBASE_012](http://localhost:3000/immagini/WEBASE_011/WEBASE_012.png)

|  Nam="Modulo di tipo FUN" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| **mod**|modulo di login|definisce quale modulo di login utilizzare|Obbigatorio |
| **t**|timestamp|definsce data e ora UTC in formato yyyyMMddhhmmss|Obbligatorio |
| **hash**|hash dei parametri|calcolata come descritto nel paragrafo sotto|Obbligatorio |
| **p**|parametro|contiene il parametro specifico per l'autenticazione, che verra passato alla fun di autenticazione ad esempio il nome utente|Obbligatorio |
| **callBack**|Url di callback|url di chiamare nel per ritornare all'applicazione chiamante|Facoltativo |
| **sfunction**|Funzione d'avvio|contiente il nome della variabile SCP_CLO da usare come funzione d'avvio in sovrascrittura dell *SFUNCTION|Facoltativo |
| **var**|Variabili|variabili da passare che verranno messe nel contesto LOO.VAR e impostate subito. La forma è variabile(valore)variabile2(valore2)|Facoltativo |
| 


### Moduli di tipo ROLES

Utilizzata per contesti in cui si vuole gestire l'accesso di "n" utenze senza dover creare i relativi utenti di sistema operativo, ma a differenza di Fun,
possono essere utilizzate le autorizzazioni di gruppo.
Occorre per prima cosa creare utenti di gruppo in b£u, ad esempio SMECLI, SMEAGE, SMECAP qualora si voglia creare tre tipologie di utenti :  Cliente, Agente, Capo area.
Nella modalità standard, occorre creare poi le "n" utenze necessarie nella tabella JAU ed associare ad esse il relativo utente di gruppo, specificandolo
nei campi di JAU : 

Ad esempio gli utenti JAU CLI001, CLI002, CLI00n dovranno essere associati a SMECLI
Tipo ogg.associato=TA
Par. ogg.associato=B£U
Cod. ogg.associato=SMECLI

analogamente gli utenti JAU AGE001, AGE002, AGE00n dovranno essere associati a SMEAGE : 
Tipo ogg.associato=TA
Par. ogg.associato=B£U
Cod. ogg.associato=SMEAGE

Al momento del submit della form, verrà chiamato il servizio (fun) WEROL_01 che riceverà utente/password digitati e, una volta verificate le credenziali nella tabella JAU,
reperirà anche le informazioni B£U legate all'utente associato.
In questo modo, verrà restituito un xml di matrice monoriga contenente tutti i campi della tabella JAU e tutti i campi della tabella B£U.
WebUP a questo punto cercherà l'utente di gruppo (SMECLI, SMEAGE, SMECAP...) restituito all'interno di una mappa (utente : password : ambiente) precompilata e
residente su server Windows/Linux, terminerà la connessione master per ritentarne una con le nuove credenziali.
Di fatto quindi il job su as400 sarà intestato all'utente di gruppo e come tale godrà delle relative caratteristiche.

Relativamente al servizio, analogamente alla modalità fun, esso può essere esteso e modificato a piacimento.
Serve comunque un utente di sistema operativo per la connessione "master", diversamente non sarebbe possibile effettuata la chiamata al servizio WEJAU_01.
Per ulteriori dettagli implementativi si veda di seguito.
Connessioni :  n utenti jau -> n job (LO_Exxxxxx) N.B. ogni job sarà comunque intestato all'utente B£U associato all'utente JAU

![WEBASE_016](http://localhost:3000/immagini/WEBASE_011/WEBASE_016.png)![WEBASE_009](http://localhost:3000/immagini/WEBASE_011/WEBASE_009.png)

|  Nam="Modulo di tipo ROLES" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| **mod**|modulo di login|definisce quale modulo di login utilizzare|Obbigatorio |
| **t**|timestamp|definsce data e ora UTC in formato yyyyMMddhhmmss|Obbligatorio |
| **hash**|hash dei parametri|calcolata come descritto nel paragrafo sotto|Obbligatorio |
| **p**|parametro|contiene il parametro specifico per l'autenticazione, che verra passato alla fun di autenticazione ad esempio il nome utente|Obbligatorio |
| **callBack**|Url di callback|url di chiamare nel per ritornare all'applicazione chiamante|Facoltativo |
| **sfunction**|Funzione d'avvio|contiente il nome della variabile SCP_CLO da usare come funzione d'avvio in sovrascrittura dell *SFUNCTION|Facoltativo |
| **var**|Variabili|variabili da passare che verranno messe nel contesto LOO.VAR e impostate subito. La forma è variabile(valore)variabile2(valore2)|Facoltativo |
| 


### Moduli di tipo DIRECT

Utilizzata per accedere senza lasciare all'utente la possibilità di cambiare alcun parametro d'accesso (provider, indirizzo as400, ambiente, utente, password...)
Questa modalità usa l'utente di sistema operativo.
Connessione :  n utenti b£u -> n job (LO_Exxxxxx)

![WEBASE_017](http://localhost:3000/immagini/WEBASE_011/WEBASE_017.png)![WEBASE_010](http://localhost:3000/immagini/WEBASE_011/WEBASE_010.png)

|  Nam="Modulo di tipo DIRECT" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Nome" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbiligatorietà" |
| **mod**|modulo di login|definisce quale modulo di login utilizzare|Obbigatorio |
| **sfunction**|Funzione d'avvio|contiente il nome della variabile SCP_CLO da usare come funzione d'avvio in sovrascrittura dell *SFUNCTION|Facoltativo |
| **callBack**|Url di callback|url di chiamare nel per ritornare all'applicazione chiamante|Facoltativo |
| **var**|Variabili|variabili da passare che verranno messe nel contesto LOO.VAR e impostate subito. La forma è variabile(valore)variabile2(valore2)|Facoltativo |
| 


### Validazione della richiesta
La richiesta viene validata
- calcolando l'hash dei parametri, secondo le modalità definite sotto, e confrontandola con quella passata nella request.
- calcolando il timestamp e confrontandolo con quella passata nella request, con una tolleranza definita nella configurazione del modulo di login

Successivamente, viene eseguito il login sul sistema nelle modalità definite nel modulo utilizzato.
Ad esempio, nel caso di direct, viene eseguita la connessione, nel caso di fun o roles, viene chiamata la fun, passando come parametro quello definito nel parametro
"p" della request.

### Calcolo dell'hash

Il calcolo dell'hash è eseguito usando
* **l'algoritmo di hashing**, secondo quanto definito nel file di configurazione.
* **il character encoding** da utilizzare per la conversione in byte delle, secondo quanto definito nel file di configurazione
* i parametri obbigatori **p** e **t**
* **un segreto condiviso** tra le due applicazioni, secondo quanto definito nel file di configurazione
* i parametri facoltativi

Suppondendo, ad esempio, di utilizzare **SHA1**, **UTF-8**, ed il segreto condiviso **WEBUP91818$**, avremmo il seguente algoritmo in pseudo codice : 

_String stringToHash= param + timestamp + "WEBUP91818$" + callback + sfunction + var ;_

_byte[] byteToHash= encode("UTF8",stringToHash);_

_byte[] calculatedHash = hashFunction("SHA1", byteToHash);_

_if(calculatedHash != recievedHash)_
_    return "INVALID REQUEST";_

### Uso del callback

La url di callback è una url che viene automaticamente chiamata da WebUP nei seguenti casi : 

- errore di login
- logout da webup

Nel caso di errore, per permettere al chiamate di identificare la situazione, viene passato il parametro **error**

Ad esempio : 
http://www.caller.com/callbackFromWebup.php?error=hashError

Gli errori vengono segnalati come segue : 

|  Nam="Codifica errori di login" |
| 
| .COL Txt="Parametro" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| **configCheckError**|Errore nel reperimento della configurazione del modulo |
| **timeError**|Richiesta scaduta |
| **hashError**|Hash non valido |
| **userError**|Utente non autorizzato o sconoscuito |
| 

