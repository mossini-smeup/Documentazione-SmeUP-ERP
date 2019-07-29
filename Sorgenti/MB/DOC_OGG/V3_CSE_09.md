# Server 09

## Cos'è
Il server 09 mette in grado Loocup di interfacciarsi alle funzioni esposte dal documentale Archibox.

### Sommaria descrizione di Archibox
Il documentale Archibox presenta quattro elementi di base : 

- **Archivio** :  è l'"ambiente" che contiene i documenti
- **Raccoglitore** :  è il contenitore di una tipologia di documento
- **Documento** :  è il record che contiene le informazioni del documento
- **Allegati** :  sono file elettronici relativi al documento archiviato


### Servizi
Il server 09 mette a disposizione alcuni servizi per l'accesso alle entità del documentale.
L'indirizzo del server documentale va passato nella definizione del server (parametro "url")

- **JA_09_01** :  utility varie
-- Metodo STR.A64 per la conversione della stringa in Base 64 :  nel campo P va passata la stringa da convertire nel parametro Val()
- **JA_09_02** :  accesso ai raccoglitori.
-- Metodo LST.RAC per ottenere la lista dei raccoglitori in formato matrice.
--- il parametro ARCH permette di passare l'archivio
--- il parametro LOGIN permette di passare l'utente di collegamento
--- il parametro PWD permette di passare la password
- **JA_09_03** :  funzioni sui documenti
-- Metodo LST.RAC per ottenere la lista dei raccoglitori in formato matrice.
--- il parametro ARCH permette di passare l'archivio
--- il parametro LOGIN permette di passare l'utente di collegamento
--- il parametro PWD permette di passare la password
--- il parametro RACC permette di passare il raccoglitore
--- il parametro TIP permette di passare il tipo-parametro del documento richiesto


### Installazione e configurazione del plugin
(in via di definzione)
I prerequisiti per l'attivazione del server 09 consistono nella presenza delle librerie di interfaccia scaricabili dall'apposita sezione del sito di download
Le librerie sono contenute in uno zip che va scompattato ed il contenuto copiato nella cartella libs di Loocup

## Prerequisiti Archibox
(in via di definzione)
Archibox è un sistema/prodotto fornito da Archivist sotto forma di appliance. Tale appliance può essere fornito in forma virtuale (macchina virtuale da deployare su un sistema di vrtualizzazione) oppure in forma fisica come un box-server.

Tale sistema necessita di due indirizzi IP.
I due indirizzi sono necessari, uno per l'accesso applicativo su cui vengono esposti web interface, web service, servizi per i client Archibox, l'altro, pubblico sulla porta 3389, per funzioni amministrative espletate dal produttore :  monitoraggio, diagnostica, manutenzione, backup, etc.


## Vedi anche
- [Archiviazione](Sorgenti/MB/DOC_OGG/V2LOCOSA26)
- [Interfaccia Archiviazione Archibox](Sorgenti/MB/DOC/ODIAAB)

