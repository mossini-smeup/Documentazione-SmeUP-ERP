# Come trovare la documentazione di Sme.Up
Tutta la documentazione di Sme.up è presente in file di testo, distribuiti insieme al software, integrati con immagini (schemi, disegni, screenshot) che devono risedere su una cartella di windows denominata TAB£A, la cartella in questione e tutte le varie sottocartelle possono risiedere nell'IFS dell'AS/400 oppure in un server in rete a cui il client su cui gira Looc.Up (il PC dell'utente) deve avere accesso in lettura.
La parte iniziale del percorso che Looc.Up segue per reperire le immagini deve essere quella risolta dalla variabile _2_|SME.IMG|, codificata nel file di impostazione di Looc.Up, normalmente in _2_SCP_CLO\Default. Per la descrizione dettagliata delle modalità di impostazione dei percorsi rifarsi al documento **LOBASE_033 - Configurazione - Aspetti base** di Looc.Up - documenti applicativi : 
- [Configurazione - Aspetti base](Sorgenti/MB/DOC/LOBASE_033)

Esistono documenti di oggetto (tabella, file, API, servizio, .....) che sono poi raggruppati per tipologia, aggregati a livello di modulo di applicazione e prodotti in _2_Book per applicazione.

I book possono essere classificati in : 
 * **Documento Visione**, illustra i principi a cui ci si è ispirati nella costruzione dell'applicazione. Il manuale è rivolto ai key user e ai responsabili EDP.
 * **Manuale Applicativo**, spiega le particolarità dell'applicazione, fornisce suggerimenti sull'avviamento e approfondisce alcune funzioni particolari. Il manuale è rivolto ai responsabili EDP, ai customizzatori ed agli sviluppatori.
 * **Manuale Operativo**, spiega come utilizzare le funzioni fornite dall'applicazione, i documenti sono organizzati per modulo. Il manuale è rivolto agli utenti finali.
 * **Manuale tecnico**, raccoglie i documenti tecnici di archivi, tabelle e API che appartengono all'applicazione. Il manuale è rivolto ai responsabili EDP, ai customizzatori ed agli sviluppatori.
 * **Note di sviluppo**, raccoglie idee, prospettive, direzioni di sviluppo dell'applicazione o di parti di essa. Il manuale è rivolto esclusivamente agli sviluppatori del gruppo Sme.Up.

## Documentazione di un oggetto
Per una spegazione dettagliata della decumentazione di un oggetto rifarsi al doc. **B£DOCU_09 - Documentazione degli oggetti di Base.Up - documenti applicativi : 
- [Documentazione degli oggetti](Sorgenti/MB/DOC/B£DOCU_09)

Di seguito alcuni esempi su come trovare la documentazione di un oggetto

### Documentazione di un file
Nella scheda oggetto del file si trova la sezione dedicata alla documentazione : 
![B£DOCU_01](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_01.png)nell'esempio si tratta del file BRARTI0F.

### Documentazione di una tabella
Nella scheda oggetto della tabella si trova la sezione dedicata alla documentazione : 
![B£DOCU_02](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_02.png)nell'esempio si tratta della tabella GMC.

### Documentazione di un PGM emulazione video
Nelle icone in alto a destra del formato di emulazione il click tasto destro sull'icona centrale manda alla scheda del programma, nella scheda del programma si trova la sezione la sezione dedicata alla documentazione : 
![B£DOCU_03](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_03.png)nell'esempio si tratta del programma GMUB01G
![B£DOCU_04](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_04.png)
### Documentazione di una scheda
Non tutte le schede hanno la documentazione, in basso a destra c'è il bottone punto interrogativo, il click sul bottone apre un formato che manda alla documentazione della scheda, se esiste : 
![B£DOCU_05](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_05.png)nell'esempio vedete la scheda del modulo statistiche V5STAT
![B£DOCU_06](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_06.png)![B£DOCU_07](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_07.png)
## Documentazione di un'applicazione
Dalla scheda di un'applicazione si possono utilizzare varie funzioni che servono ad acquisire la conoscenza sull'applicazione stessa : 

- archivi
- servizi
- azioni
- oggetti
- api
- oggetti
- book


### Archivi
Dalla scheda di un'applicazione si apre la sottoscheda _2_Dati che presenta tutti gli archivi dell'applicazione, selezionando un file si apre la sua scheda da cui si può passare alla relativa  documentazione : 
![B£DOCU_08](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_08.png)
### Servizi
Dalla scheda di un'applicazione si apre la sottoscheda _2_Servizi e azioni che presenta una sottosezione in cui sono elencati i servizi dell'applicazione da cui si può passsare alla scheda relativa : 
![B£DOCU_09](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_09.png)
### Azioni (B£J)
Dalla scheda di un'applicazione si apre la sottoscheda _2_Servizi e azioni che presenta una sottosezione in cui sono elencati i servizi dell'applicazione da cui si può passsare alla scheda relativa : 
![B£DOCU_10](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_10.png)
### Oggetti
Dalla scheda di un'applicazione si apre la sottoscheda _2_Set'n play che presenta una sottosezione dove si trovano gli oggetti dell'applicazione raggruppati per tipo : 
![B£DOCU_11](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_11.png)Il click sull'oggetto manda alla sua scheda.

### API
Dalla scheda di un'applicazione si apre la sottoscheda _2_Set'n play che presenta una sottosezione dove si trovano le API dell'applicazione raggruppati per tipo : 
![B£DOCU_12](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_12.png)Il click sull'API manda alla sua scheda.

### Manuali
Dalla scheda di un'applicazione si apre la sottoscheda _2_Documentazione che presenta tutti i manuali esistenti per l'applicazione : 
![B£DOCU_13](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_13.png)
## Documentazione di un modulo
Dalla scheda di un modulo si apre la sottoscheda _2_Documentazione che presenta tutti i documenti esistenti per il modulo : 
![B£DOCU_14](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_14.png)
## Le News e le Note Tecniche
Questa scheda permette di accedere al link internet contenente le News di Sme.up, la scheda si raggiunge dalla scheda del modulo B£DOCU, sezione _2_Le news : 
![B£DOCU_15](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_15.png)
## Internet
I documenti possono anche essere raggiunti via Internet dal sito www.smeup.com, sul sito si trovano :  i book, i filmati, le news.
Tutti i documenti seguenti pretendono che l'utente Internet si sia autenticato inserendo utente e password ed accedendo all'area ri servata.

### I manuali
Si trovano nella sezione _2_Documentazione, per gli utenti autenticati si rende visibile il bottone _3_Manuali : 
![B£DOCU_16](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_16.png)click sul link per accedere alla lista
![B£DOCU_17](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_17.png)vengono presentati tutti i manuali a cui l'utente è autorizzato : 
![B£DOCU_18](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_18.png)
### I filmati
Si trovano nella sezione _2_Documentazione premendo il bottone _3_Videostreaming si apre la lista dei filmati che sono a disposizione degli utenti autenticati : 
![B£DOCU_19](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_19.png)
### Le news
Si trovano nella sezione _2_Eventi & news, premendo il bottone _3_News tecniche di Sme.up : 
![B£DOCU_20](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_20.png)click sul link per accedere alla lista : 
![B£DOCU_21](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU_80/BXDOCU_21.png)