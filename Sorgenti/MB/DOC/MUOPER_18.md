# Ambiente condivisione sorgenti

In un ambito di sviluppo condiviso, è necessario individuare un ambiente che consenta la gestione centralizzata dei sorgenti
e consenta a più sviluppatori di condividere e lavorare sulla stessa base di codice.

In un ambiente server centrico come il sistema iSeries, la gestione dello sviluppo condiviso è insita nelle caratteristiche del
sistema stesso che portano ad una globale condivione di oggetti e risorse del sistema.

In un ambito multipiattaforma caratterizzato da una architettura scalabile in orizzontale, la condivisione di risorse può avvenire
solo attraverso la condivisione di servizi.

## Eclipse Cloud Development

Il framework Eclipse Cloud Development (d'ora in avanti identificato come ECD) è un modello proposto dall'infrastruttura
Eclipse per la condivisione degli oggetti di tipo sorgente (identificati oggetti di tipo OJ*SRCF). Questo framework fornisce le
le seguenti funzionalità : 


- Gestione centralizzata dei sorgenti
- Funzioni di sincronizzazione tra repository centralizzato e client di sviluppo
- Strumenti Web-based per l'accesso e l'editing condiviso dei sorgenti




## Implmentazione del servizio CDO

Tra le varie implementazioni disponibili per il servizio ECD, all'interno dell'architettura As.UP è stata scelto di utilizzare
**Flux**.
Flux viene dichiarato come il punto di congiunzione tra lo sviluppo in un ambiente IDE tradizionale e lo sviluppo in un
IDE condiviso. Fornisce un servizio cloud di storage e di sincronizzanione a cui ci si può connettere in vari modalità.
Fornisce inoltre vari strumenti per la connessione al repository condiviso :  un plugin per Eclipse, un servizio JDT per
l'accesso alle funzioni del repository e l'integrazione con Orion (editor web) per la parte di editing condivisa.
Inoltre, l'architettura di Flux consente la separazione tra i servizi grafici di editing (Orion o Eclipse) e il servizio JDT
di sincronizzazione delle risorse, consentendo l'accesso alle risorse condivise da più ambienti operativi.


La seguente figura mostra un tipica installazione Flux attestata su server dedicato.

![MUOPER_18A](http://localhost:3000/immagini/MUOPER_18/MUOPER_18A.png)
Analizziamo brevemente i componenti : 


- **Flux server** :  è il server su cui è attivo il servizio di condivisione Flux. In seguito verranno mostrati i dettagli di
installazione di questo servizio. Sulla stessa macchina è installato un server Orion che consente l'accesso ai file
sorgente condivisi da un editor web based e i connettori SMProvider che consentono l'accesso alle GUI di Sme.Up
(Looc.UP e Web.UP).
- **Flux client** :  con questa dicitura generica si intendono tutti i fruitori del servizio di condivisione file offerto da
Flux. In particolare, l'accesso condiviso ai file può avvenire da ambiente grafico di sviluppo (Eclipse IDE) oppure da
tutte le altre entità che necessitano di un accesso ai sorgenti (ad esempio, l'As.UP Server)
- **Workspace** :  è il file system di riferimento per il server Flux e rappresenta il target del servizio di sincronizzazione.
Tutte le modifiche ai sorgenti vengono riportate a questo file system di riferimento e da qui replicate su tutte le entità
da sincronizzare.








