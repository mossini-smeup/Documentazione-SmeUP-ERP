# Installazione documentale HyperDok
## Prerequisiti
 T(**Sistema operativo**)
- Windows XP, Windows 2000, Windows 2003
- Database SQL Server
- Porta USB per chiave di licenza
- Porta USB (non virtuale) per lettore smartcard in caso di necessità di firma digitale o conservazione sostitutiva dei documenti archiviati


## Installazione Database
E' necessaria la presenza di un database su cui HyperDok manterrà i dati. Non è necessario sia sulla stessa macchina su cui è installato il software della HyperDok, basta che sia raggiungibile via rete dalla stessa. Il database da noi utilizzato è Microsoft SQL Server 2005, si rimanda alla documentazione specifica del prodotto per le informazioni relative ad altri database compatibili.

## Installazione e configurazione di HyperDok (il software documentale)
Allo stesso modo si rimanda alla documentazione specifica del prodotto per informazioni più specifiche sulla procedura di installazione

# Installazione Loocup Server
## Prerequisiti
 T(**Sistema operativo**)
- Windows XP, Windows 2000, Windows 2003


## Installazione Loocup
L'installazione del software di Loocup Server è identica all'installazione di un Loocup in locale, quindi attraverso il setup.exe del CD.
L'utilizzo di Loocup come server è una questione di configurazione dell'applicazione e della registrazione della stessa come servizio.
## Configurazione di Loocup Server
La configurazione per l'avvio come server e come servizio di Loocup è basata sul file wrapper.conf contenuto nella cartella serviceNT\conf.
In tale file vanno definite alcune chiavi di configurazione : 
 T(I parametri di collegamento all'AS, vale a dire il sistema e l'utente con cui Loocup server opererà sull'AS400)
- wrapper.app.parameter.2=AS400
- wrapper.app.parameter.3=UTENTE
- wrapper.app.parameter.4=PASSWORD
- wrapper.app.parameter.5=--server

L'utente indicato al punto 2 deve essere monoambiente. Nel caso non lo sia va aggiunta la riga
**wrapper.app.parameter.6=CODICE AMBIENTE**
allo stesso modo in cui viene indicato quando si avvia un collegamento con Loocup client

 T(I parametri di avvio del servizio, vale a dire l'utente, eventualmente di dominio, con cui l'applicazione sarà eseguita sul server)
- wrapper.ntservice.account=DOMINIO\utente
- wrapper.ntservice.password=password

Tipicamente per l'utilizzo di Loocup per l'integrazione con HyperDok l'applicazione deve svolgere delle funzioni che prevedono : 

- accesso a cartelle condivise sull'AS
- accesso a cartelle condivise in rete
- collegamenti ad AS400 e SQL server

quindi l'utente che viene scelto per l'installazione del servizio deve avere le autorizzazioni necessarie e le Group Policies di macchina o dominio consone a permettergi di svolgerle

Una volta terminato di editare il file di configurazione si registra Loocup server come servizio eseguendo il file ServiceInstall.bat
Una volta registrato il servizio il file di configurazione nonv iene più letto quindi se si desidera modificare la configurazione di avvio del servizio è necessario disinstallarlo con ServiceUninstall.bat, modificare il file wrapper.conf, reinstallare il servizio con ServiceInstall.bat.
Allo stesso modo se non si desidera lasciare in chiaro le credenziali di avvio del servizio o di collegamento all'AS, una volta registrato il servizio, è possibile eliminarle dal file wrapper.conf
