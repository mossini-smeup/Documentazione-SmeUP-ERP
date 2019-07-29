## Setup Archibox
### Prerequisiti generali
Per i prerequisiti per avere le funzioni di archiviazione sono descritte nel documento : 
- [A26-Interfaccia arch. generica](Sorgenti/MB/DOC/ODBASE_02)
### Prerequisiti specifici integrazione
Per connettere SmeUp al documentale Archibox sono necessari i seguenti strumenti : 
* l'installazione presso un server aziendale di una versione server Archibox raggiungibile dall'AS400.
* la presenza di un'istanza client di Archibox che abbia installato il client Archibox oltre che il prodotto Archivist chiamato **MultiPlugin**
* la configurazione del prodotto Multiplugin in cui vengano specificati i path in cui leggere il file XML (utilizzato per il setup dell'archiviazione) e i documenti da archiviare (il file si chiama **Config-Raccoglitori-Xml.xml**e si trova nell'installazione del client Archibox.)
* Nel caso in cui si voglia interrogare in SmeUp i documenti archiviati è necessario un plugin specifico di LoocUp  (per la documentazione ci si riferisca a **DOC_OGG/V3_CSE_09**)
* Per avere le segnalazioni della corretta archiviazione dei documenti deve essere installato e funzionante il Web service V2_WEBSE_01 (**DOC_OGG/V3_CSE_09**) che configurato correttamente permette la segnalazione in SmeUp della corretta archiviazione dei documenti

### Configurazione script Multiplugin Archibox
![ODIAAB_002](http://localhost:3000/immagini/ODIAAB_02/ODIAAB_002.png)

