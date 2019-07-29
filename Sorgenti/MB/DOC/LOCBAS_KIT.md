## INSTALLAZIONE
E' ospitato nel sistema operativo installato nella macchina virtuale che viene distribuita in uno dei formati previsti (VMWare, Hyper-V, Virtualbox), quindi, una volta installata ed avviata la macchina virtuale, anche il provider è attivo. Ovviamente senza una configurazione.

## CONFIGURAZIONE
Prima che il provider diventi operativo deve essere configurato.

Per accedere al file di configurazione bisogna collegarsi alla macchina virtuale tramite SSH con utente **smeup**

_ssh smeup@indirizzo-macchina-virtuale_
Al primo accesso verrà richiesto di impostare la password dell'utente **smeup**.

Una volta collegati in SSH ci si troverà nella home directory dell'utente, i percorsi citati in seguito fanno tutti riferimento a questa cartella di partenza.

### Il file di configurazione
La configurazione del provider avviene gestendo il file **container/smeup-provider-fe/config/smeup-provider-fe/configuration.properties**

Nel seguente esempio in grassetto i dati indispensabili per la configurazione sono in grassetto

--------- INIZIO ESEMPIO SCRIPT DI CONFIGURAZIONE ---------
 :  : PAR F(04)
user=**UTENTE**
password=**PASSWORD**
server=**INDIRIZZO**
serverQName=**CODICE-PROVIDER**
.-se metto env viene creata una connessione completa
.-senza env solo la coda server--> necessario specificare XML iniziale
env=**AMBIENTE** (commentare la riga nel caso di provider che si deve collegare ad un sistema non Sme.UP ERP)
.-env=

dblogtype=remote
logdblib=SMEUP_DAT

.-mapping path
.-queste variabili informano il provider sulla corrispondenza
.-tra il percorso Windows e quello dove viene montato in Linux
.-esempio
.-MAPPING_PATH_01=WIN(\\server01.xyz.com\azienda01\share1) LIN(/mnt/payara/server01-share1)
.-sono predisposte 9 copie,
.-se non bastassero se ne possono aggiungere quante ne servono : 
.-il provider leggerà tutte le chiavi che iniziano con MAPPING_PATH_
.-ogni chiave deve essere univoca
MAPPING_PATH_01=WIN() LIN()
MAPPING_PATH_02=WIN() LIN()
MAPPING_PATH_03=WIN() LIN()
MAPPING_PATH_04=WIN() LIN()
MAPPING_PATH_05=WIN() LIN()
MAPPING_PATH_06=WIN() LIN()
MAPPING_PATH_07=WIN() LIN()
MAPPING_PATH_08=WIN() LIN()
MAPPING_PATH_09=WIN() LIN()
.-utilizzo come XML iniziale quello di default si trova in LOOCUP_SET/SPR/XML/default.xml
.-xmlini=eventuale override del percorso xml di inizializzazione (per provider senza Sme.UP)
loocupEncCode=U8
logLevel=debug
logComunication=YES
.-di default è in appdata\Loocup log se in Windows - altrimenti è in home/
logPath=
.-numero di rolling mantenuti
logRollingFileNum=
.-Dimensione in megabyte del singolo file di rolling es 10MB
logRollingFileSize=
.-numero età max dei file di log
logMaxAgeDays=
debugMode=
.-rootFolder=Percorso alla cartella che il provider deve considerare root
rootFolder=
.-non va eseguito il ping :  non ho connessione verso SmeUp
pingPeriod=100
.-pingPeriod=-1
cleanDBPeriod=8h

---------- FINE ESEMPIO SCRIPT DI CONFIGURAZIONE ----------

### Scenari di configurazione
Per quanto riguarda i dati di configurazione obbligatori (quelli in grassetto nel file di configurazione sopra riportato), gli scenari possibili sono due : 

Configurazione per collegarsi ad un server **con** Sme.UP ERP
user= utente server applicativo
password= password utente
server= indirizzo server applicativo
serverQName= codice provider
env= codice ambiente
xmlini commentato

Configurazione per collegarsi ad un server **senza** Sme.UP ERP
user= utente server applicativo
password= password utente
server= indirizzo server applicativo
serverQName= codice provider
env commentato
xmlini= DEFAULT


### Ricaricare configurazione
Una volta modificato il file di configurazione va fermato ed avviato container per fargli prendere le modifiche della configurazione con i comandi

_docker stop smeup-provider-fe_

_docker start smeup-provider-fe_
## AGGIORNAMENTO
L'aggiornamento del provider avviene attraverso il comando

_update-provider_

Se questo comando viene eseguito senza parametri l'aggiornamento porterà il provider all'ultima versione rilasciata. Lo stesso script ammette un parametro indicante la versione, nel caso venga passata la versione il provider verrà portato alla versione indicata. Es :  eseguendo il comando

_update-provider 1.0.8_
provocherà l'aggiornamento del provider alla versione 1.0.8.

L'aggiornamento salverà nella cartella principale il file war della versione richiesta. Tali file resteranno finchè non verranno rimossi manualmente.

E' possibile procedere all'aggiornamento anche manualmente, basta prendere il file war del provider e copiarlo nella cartella**container/smeup-provider-fe/deployments/** dandogli nome smeup-provider-fe.war e riavviando il container tramite i comandi precedentemente riportati.

## MONITORAGGIO
Una volta avviato il provider la verifica del suo stato di salute avviene attraverso 3 strade (due immediate, la terza più drastica da intraprendere solo di fronte a problemi)

- La pagina di debug http://indirizzo-virtuale:8080/smeup-provider-fe/debug
- Le pagine di probe
-- http://indirizzo-virtuale:8080:8080/smeup-provider-fe/ProbesService/connectivity (test connettività)
-- http://indirizzo-virtuale:8080/smeup-provider-fe/ProbesService/appserver (test interazione con Sme.UP ERP, valido ovviamente solo per situazioni con SmeUP su as400)
-- http://indirizzo-virtuale:8080/smeup-provider-fe/ProbesService/folders (test raggiungibilità dei folder di rete configurati)
- Accedere alla cartella dei log presente nel seguente percorso **container/smeup-provider-fe/log/**
La struttura della cartella è identica a quella del provider classico :  i file specifici per funzione nella cartella **log**, i file globali nella cartella **GLOBAL**

## UPCOMING
Prossimamente metteremo a punto : 

- Funzionalità per agevolare il download dei log
- Esposizione di ulteriori informazioni nelle funzionalità di probe (es :  versione del provider)
