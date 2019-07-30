## Obiettivo

Attraverso questa funzione è possibile confrontare le coordinate bancarie presenti sull'anagrafica di un ente con quelle riportate su rate aperte e/o su documenti in essere intestati all'ente stesso ed eventualmente allineare i dati.

## Formato guida

All'interno del formato guida sono disponibili i seguenti campi : 

![C5C010_076](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOCN5/C5C010_076.png)

 - Codice dell'ente o della lista di enti di cui si voglia analizzare l'allineamento delle coordinate bancarie. La compilazione di questo campo è facilitata dalla presenza dei classici caratteri di ricerca. Per maggiori informazioni su questi caratteri si veda il seguente : 

- [Ricerche](Sorgenti/MB/DOC_OPE/B£_RIC)
Per dettagli sull'utilizzo delle liste oggetti si veda invece : 
- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Funzione. Per la verifica delle coordinate bancarie il campo deve essere compilato con V.
 - Metodo. Per la verifica delle coordinate bancarie il campo deve essere compilato con B.
 - Modalità. In questo campo è necessario indicare il tipo di output desiderato. Le modalità disponibili per l'esecuzione di questa funzione sono : 
 -- 1 - Stampa :  permette di ottenere una stampa in cui sono visualizzati gli enti o l'ente per i quali vengono rilevate delle discordanze tra coordinate bancarie anagrafiche e coordinate bancarie presenti su documenti e/o sulle rate.
 -- 2 - Interrogazione :  permette di visualizzare e successivamente allineare le discordanze tra dati bancari anagrafici e dati bancari presenti su documenti aperti e/o rate.
 -- 3 - Esecuzione :  permette di lanciare l'allineamento automatico di tutti i record che verifichino le condizioni impostate tramite le parzializzazioni e impostazioni.


### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 

![C5C010_077](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOCN5/C5C010_077.png)
- Ometti Riferimenti Nulli. Se compilato con 1 verranno esclusi i record all'interno dei quali non è riportato alcun riferimento bancario.
- Ometti Banche Aggiuntive. Nel caso in cui all'ente siano associate a livello anagrafico più banche queste verranno visualizzate all'interno della funzione ad eccezione del caso in cui questo campo venga compilato con 1.
- Banca Fissa. All'interno di questo campo è possibile inserire il codice ABICAB di una banca :  in questo modo tutti i record che riportano la banca impostata verranno esclusi dall'interrogazione.
- Conto corrente fisso
- Solo se Ente Cessione. Visualizza le sole rate per le quali sia compilato l'Ente di Cessione.
- Dati da controllare. Il campo può essere compilato con : 
-- Blank - Tutti :  lasciando il campo vuoto verranno analizzate sia le scadenze che i documenti aperti
-- 1 - Solo Scadenze :  verranno analizzate solo le rate aperte
-- 2 - Solo Documenti :  verranno analizzati solo i documenti aperti.
- Documenti. Nel caso in cui nel campo precedente si sia scelto di analizzare anche i documenti è possibile definire quali documenti analizzare. Le scelte disponibili sono : 
-- Blank - Tutti :  lasciando il campo vuoto verranno analizzati tutti i documenti aperti
-- 1 - Solo da contabilizzare :  verranno analizzate solo le bolle in attesa di contabilizzazione
-- 2 - Solo ordini aperti :  verranno analizzati solo gli ordini non ancora evasi
- Controllo codice pagamento su documenti. Compilando questo campo con 1è possibile fare in modo che venga analizzato anche il codice pagamento riportato sui documenti :  verrranno quindi mostrati anche i documetni che presentano un codice pagamento diverso rispetto a quello riportato sull'anagrafica dell'ente.


All'interno delle impostazioni sono disponibili le memorizzazioni video attraverso cui e' possibile salvare una specifica configurazione delle impostazioni : 

![C5C010_072](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_072.png)
Le memorizzazioni salvate saranno poi richiamabili direttamente dal formato guida attraverso l'utilizzo dei caratteri di ricerca all'interno dello specifico campo : 

![C5C010_073](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_073.png)
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

### Parzializzazioni

Digitando il tasto F13 o il relativo pulsante è possibile accedere alle parzializzazioni : 

![C5C010_078](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOCN5/C5C010_078.png)
Sono disponibili due videate di parzializzazioni; per accedere alla seconda videata è sufficiente digitare il tasto F13 dalla prima videata.

### Tasti funzionali

 * F06 :  Conferma. Permette di confermare ed eseguire la funzione
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

### Memorizzazioni

Le memorizzazioni consentono di salvare le parametrizzazioni definite all'interno della videata. Per maggiori dettagli sulla loro creazione e gestione si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

## Formato lista

All'interno del formato lista è riportato l'elenco dei record per i quali è stato rilevato un disallineamente tra dati bancari anagrafici e dati riportati su documenti e/o rate.

![C5C010_079](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOCN5/C5C010_079.png)
Per ogni ente per il quale vengono trovati dati disallineati sono riportati : 
- Un riquadro relativo a rate per le quali i dati bancari non corrispondono a quelli anagrafici
- Un riquadro relativo a documenti per i quali i dati bancari non corrispondono a quelli anagrafici
Nel primo riquadro troviamo i seguenti record : 
 * Codice e ragione sociale dell'ente
 * Banca anagrafica principale
 * Eventuali banche anagrafiche aggiuntive
 * Dettaglio rate disallineate. In particolare per ogni rata sono riportati : 
 ** Data scadenza
 ** Tipologia di pagamento
 ** Importo
 ** Ente cessionario
 ** Banca aziendale (tabella C5F)
 ** Banca cliente (ABICAB)
 ** Conto corrente
 ** IBAN
 ** Codice SWIFT
Nel secondo riquadro troviamo i seguenti record : 
 * Codice e ragione sociale dell'ente
 * Banca anagrafica principale
 * Eventuali banche anagrafiche aggiuntive
 * Dettaglio documenti disallineati. In particolare per ogni documento sono riportati : 
 ** Data scadenza
 ** Tipologia di pagamento
 ** Importo
 ** Ente cessionario
 ** Banca aziendale (tabella C5F)
 ** Banca cliente (ABICAB)
 ** Conto corrente
 ** IBAN
 ** Codice SWIFT
 ** Codice Pagamento

### Opzioni

Per ogni record relativo a rate disallineate sono disponibili le seguenti opzioni : 
 * _2_AL - Allineamento rata.Permette di allineare i dati bancari della rata a quelli riportati sulla banca anagrafica principale.
 :  : I.INC.MBR Fil(DOC_OGG) Mem(P_C5NOCN5O)

Per ogni record relativo a documenti disallineati sono disponibili le seguenti opzioni : 
 * _2_AL - Allineamento rata.Permette di allineare i dati bancari del documento a quelli riportati sulla banca anagrafica principale.
 * _2_02 - Modifica Documento.Permette di entrare in modifica del documento.
 * _2_05 - Visualizza Documento.Permette di entrare in visualizzazione del documento.
