# Descrizione

## Prerequisiti

* Download del prodotto (http://www.smeup.com/Download')
* Installazione del database, consigliato DB2Luw seguendo la procedura
- [IBM DB2 Luw](Sorgenti/MB/DOC/MUDBMS_12)

## Procedura

Estrarre il contenuto del file zip in una cartella a piacere.
Verificare che il contenuto del file 'Application.xmi' sia presente nella cartella di root, se mancante seguire le indicazioni di  :  : DEC T(MB) P(DOC) K(MUBASE_xx) I(configurazione) L(1)
Editare il file 'Application.xmi' se si desidera cambiare i parametri di default
Lanciare l'applicazione tramite eseguibile (TODO)
Collegarsi tramite interfaccia grafica Loo.cup; è possibile cambiare i parametri di configurazione editando il file 'Application.xmi'

## Funzioni preliminari

### Restore librerie
Se non si possiede una cartella contenente la preinstallazione del sistema, occorre ricevere ed eseguire il restore da un sistema origine  tramite i comandi
 :  : DEC T(OJ) P(*CMD) K(RCVXMI)
 :  : DEC T(OJ) P(*CMD) K(RSTXMI)

### Configurazione utenti
Il sistema viene fornito con il profilo di default QASUP, una volta eseguita la  :  : (DEC) T(MB) P(DOC) K(MUOPER_xx) I(login) L(1) è possibile creare nuovi utenti tramite il comando  :  : DEC T(OJ) P(*CMD) K(CRTUSRPRF)
Per i dettagli circa la gestione utenti si rimanda a  :  : DEC T(MB) P(DOC) K(MUOPER_xx)

### Verifica installazione
Per verificare la corretta installazione è possibile accedere tramite telnel alla shell del sistema
Normalmente occorre digitare il comando 'telnet localhost 8023', se si desidera modificare la configurazione di base occorre editare il file 'Application.xmi'

