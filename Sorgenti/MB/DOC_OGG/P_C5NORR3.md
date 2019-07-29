 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OPE) Mem(C5D010_01) Tag(Intro scadenzario)

 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OPE) Mem(C5BASE_01) Tag(Parzializzazioni)

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle **Impostazioni** che riportano i seguenti campi : 

![C5D010_027](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORR3/C5D010_027.png)

- Impostazioni generali :  apre un'altra finestra di impostazioni dove andare a scegliere se forzare o meno la richiesta e se stampare la pagina delle impostazioni.
- Tipo :  permette di scegliere che tipo di scadenzario visualizzare. Le scelte disponibili sono :  rischio, scadenzario ed esposizione. Nel primo caso saranno visualizzate le sole scadenze in rischio (RiBa di cui si sia già registrato l'incasso ma di cui non si ha ancora la certezza dell'esito), nel secondo caso saranno invece visualizzate le sole partite aperte mentre nell'ultimo caso saranno esposte sia le scadenze in rischio che le partite aperte.
- Data situazione :  attraverso questo campo è possibile visualizzare lo scadenzario a una data indicata.
- Tutte le aziende :  è un campo utilizzato per la multiaziendalità. Se impostato a SI permette di vedere lo scadenzario relativo a tutte le aziende facenti parte del gruppo.
- Natura pagamento :  consente di visualizzare le sole scadenze con una certa natura pagamento.
- Segno :  se impostato permette di visualizzare le sole scadenze in dare o in avere.
- Categoria contabile :  consente di visualizzare solo gli enti aappartenenti a una determinata categoria contabile. La categoria contabile dell'ente è impostata all'interno dell'anagrafica.
- Filtro :  può essere utlizzato per costruire filtri personalizzati sulle scadenze incluse nell'interrogazione.
- Presentazione :  consente di visualizzare lo scadenzario in modalità 'Partite' oppure 'Scadenze'. Nel primo caso sarà possibile visualizzare l'intera evoluzione della partita aperta mentre nel secondo caso saranno visualizzati solo i dati relativi alla rata aperta.
- Esito :  impostando questo campo è possibile visualizzare le sole scadenze con un determinato esito (insolute, protestate, richiamate, ecc.).
- Schema :  può essere utilizzato qualora si voglia costruire uno schema utente per le colonne che si intendono visualizzare nello scadenzario.
- Schema totali :  funziona come il precedente ma è utilizzato per creare uno schema di visualizzazione personalizzato solo sui totali dello scadenzario.
- Ordinamento :  determina l'ordinamento con cui si vogliono visualizzare le scadenze. Le scelte a disposizione sono :  per attributo ente, per banca, per banca/attributo ente e infine come da default per ente.
   -- Attributo ente 1 permette di scegliere l'attributo su cui si voglia ordinare (es. provincia, nazione, ecc.).
   -- Rotture atr. 1 permette di impostare le rotture all'interno dello scadenzario sul tipo di attributo impostato precedentemente; può essere impostato SI, SOLO TOTALI oppure come default NO.
   -- Attributo ente 2 permette di fare un secondo ordinamento su un attributo ente.
   -- Rotture atr. 2
- Livello di dettaglio :  se impostato permette di visualizzare i soli totali.
- Totali mensili :  impostando questo campo è possibile visualizzare un totale mensile delle scadenze.
- Note :  permette di abilitare la visualizzazione delle note. Le opzioni disponibili sono : 
   **1.**   Note delle righe :  vengono visualizzate le note scritte sulle righe delle registrazioni contabili.
   **2.**   Note delle rate e delle righe :  permette di includere le note di rate e righeall'interno dello scadenzario.
   **3.**   Note delle testate :  vengono visualizzate le note scritte sulle testate delle registrazioni contabili.
   **4.**   Tutte le note :  vengono incluse tutte le note della registrazione contabile.
   **Blank.**  Note delle rate :  di default lasciando a blank questo campo vengono incluse solo le note inserite sulle rate.
 -- Visualizza :  imposta il tipo di visualizzazione della nota. Può essere visualizzata :  l'intera nota, un suo prologo oppure ne viene segnalata la sola presenza.
- Note anagrafica :  permette di includere anche le note presenti sull'anagrafica dell'ente.
- Importo netto ritenute :  se impostato a si, mostra  l'importo al netto e al lordo di ritenuta per i percipienti.
- Valuta di conto :  permette di visualizzare il controvalore in euro delle rate. Ha ovviamente senso solo in caso di scadenze in valuta.
- Salto pagina :  permette di impostare il salto pagina sulle stampe.
- Ometti data/utente :  permette di ommettere sull'intestazione della stampa la data e l'utente di lancio .
- Raggrup. cumulati :  se impostato a 1 nel caso in cui esistano rate cumulate invece di mostrare le differenti rate visualizza una sola rata. Se impostato a 2 permette di evidenziare quali rate sono state raggruppate e visualizza la rata di cumulo.
- Controlllo Esito : 
- Portafoglio :  consente di visualizzare distintamente la parte di portafoglio da presentare e quella presentata.
- Escludi effetti :  permette di ignorare le scadenze indicate come effetti (Riba, Tratte, ecc.).
- Data rischio :  è riferita al rischio alla data inserita. E' utile in caso di interrogazioni retroattive.


All'interno delle impostazioni sono anche disponibili le _memorizzazioni video_ attraverso le quali è possibile salvare una specifica configurazione delle impostazioni : 
![C5D010_029](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORR3/C5D010_029.png)Per accedervi è necessario interrogare con il punto esclamativo il  campo "memorizzazioni" posto in alto nella schermata.
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente link : 
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)


Da qui in avanti la documentazione farà riferimento al lancio della funzione sul singolo soggetto, tenendo conto però, che il lancio su una lista di soggetti, presenta le stesse funzionalità ed opzioni che si andranno a vedere per il singolo soggetto.


## Formato lista

All'interno del formato lista è riportato l'elenco delle scadenze associate all'ente ordinate per data registrazione e per scadenza : 

![C5D010_023](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORR3/C5D010_023.png)
I dati riportati variano a seconda delle impostazioni definite dall'utente e possono essere personalizzati in funzione delle esigenze. Il parametro che modifica maggiormente la visualizzazione dello scadenzario è la 'Presentazione'. Nell'immagine riportata sopra vediamo, infatti, uno scadenzario in modalità 'Scadenze' mentre qui in basso è riportato lo stesso scadenzario in modalità ' Partite' : 

![C5D010_032](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORR3/C5D010_032.png)
All'interno dello scadenzario per ogni rata sono riportati :  data registrazione, data scadenza, tipologia di pagamento con relativa descrizione, importo e segno della rata, ABI-CAB della banca dell'ente, banca di presentazione aziendale, data e numero documento che ha generato la scadenza, numero protocollo e numero di distinta in cui la rata è inclusa.

In fondo all'elenco delle scadenze è inoltre riportata una sintesi del valore scaduto, a scadere, in rischio e il totale per cui il soggetto risulta esposto.

### Opzioni

Per ogni scadenza sono disponibili le seguenti opzioni : 

![C5D010_024](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORR3/C5D010_024.png)
 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OGG) Mem(P_C5NO00G)


### Tasti funzionali

**F01** :  Permette di ricercare una stringa all'interno della videata.
**F05** :  Esegue l'aggiornamento della videata.
**F09** :  Permette di posizionarsi sulla prima pagina dello scadenzario.
**F10** :  Permette di posizionarsi sull'ultima pagina dello scadenzario.
**F13** :  Apre le parzializzazioni. Le parzializzazioni permettono di definire dei filtri per l'estrazione dei dati.
**F17** :  Apre le impostazioni, le quali permettono di accedere alla schermata in cui definire degli schemi e altre tipi di informazioni che modificano la visualizzazione dello scadenzario.


