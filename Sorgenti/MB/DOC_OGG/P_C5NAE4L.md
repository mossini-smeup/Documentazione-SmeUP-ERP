## Obiettivo
Attraverso questa voce di menù è possibile interrogare e gestire le registrazioni di prima nota.

## Formato guida
Al lancio della funzione viene presentata la seguente schermata : 

![C5C010_034](http://localhost:3000/immagini/MBDOC_OGG-P_C5NAE4L/C5C010_034.png)
All'interno del formato guida è prima di tutto necessario compilare il campo 'Funzione' che determina l'ordinamento e le informazioni che verranno poi visualizzate all'interno del formato lista. La funzione determina anche i campi che verranno poi visualizzati all'intenro del formato guida. Le funzioni disponibili sono : 
 * Per progressivo :  permette di visualizzare le registrazioni contabili ordinate per progressivo indicando eventualmente uno specifico numero di registrazione che si voglia gestire
 * Per utente/data/azienda/esercizio :  permette di visualizzare le registrazioni contabili ordinate per utente/data/azienda/esercizio. In questo caso è necessario definire almeno l'utente di inserimento delle registrazioni contabili mentre sono opzionali i campi che specificano la data registrazione, l'azienda e l'esercizio.
 * Per data registrazione/azienda/esercizio/tipo :  permette di visualizzare le registrazioni contabili ordinate per data registrazione/azienda/esercizio/tipo. Nei campi visualizzati in basso è possibile specificare data registrazione, azienda e numero registrazione.
 * Per azienda/esercizio/ente-conto :  permette di visualizzare le registrazioni contabili ordinate per azienda/esercizio/oggetto intestatario della registrazione. Nei campi visualizzati in basso è possibile specificare azienda, esercizio contabile, oggetto intestario, tipo registrazione e data registrazione.
 * Per ente/documento :  permette di visualizzare le registrazioni contabili ordinate per ente intestatario/data documento. In questo caso è necessario definire almeno l'intestatario delle registrazioni contabili mentre sono opzionali i campi che specificano la data documento, il numero protocollo e il tipo protocollo.
 * Per azienda/registro IVA :  permette di visualizzare le registrazioni contabili ordinate per azienda/registro IVA. Nei campi visualizzati in basso è possibile specificare azienda, tipo IVA (acquisti o vendite) e codice registro IVA.
 * Per pratica/protocollo :  permette di visualizzare le registrazioni contabili ordinate per tipo/numero protocollo. Nei campi visualizzati in basso è possibile specificare tipo e numero protocollo.
Le modalità disponibili per questa funzione sono 'Stampa' e 'Visualizzazione' che consentono di ottenere il risultato dell'interrogazione all'interno di un file di spool oppure visualiuzato a video.
I campi 'Pertinenza' e 'Condizione' devono essere compilati in funzione della tipologia di registrazioni che si vogliono considerare per il calcolo della situazione dei rapporti. In particolare nel campo Pertinenza è necessario indicare se considerare solo registrazioni gestionali, solo contabili o entrambe mentre nel campo Condizione è possibile indicare se considerare solo registrazioni attive, solo simulate o entrambe.

### Impostazioni
Digitando da tastiera il tasto F17 o selezionando il relativo bottone è possibile accedere alle impostazioni che riportano i seguenti campi : 
 * Impostazioni generali :  permette di forzare la presentazione della schermata delle impostazioni al lancio della funzione e di includere nella stampa una pagina riassuntiva delle impostazioni definite.
 * Presento testate? Permette di visualizzare o meno il dettaglio della testata delle registrazioni.
 * Presento righe? Permette di visualizzare o meno il dettaglio delle righe delle registrazioni.
 * Presento analitica? Permette di visualizzare o meno il dettaglio dell'analitica delle registrazioni.
 * Presento scadenze? Permette di visualizzare o meno il dettaglio delle rate delle registrazioni.
 * Presento ritenute? Permette di visualizzare o meno il dettaglio delle ritenute delle registrazioni.
 * Controllo errori? Permette di evidenziare i record contenenti errori
 ** Livello controllo :  permette di definire a che livello effettuare il controllo errori (testate, righe, scadenze o analitica)
 * Note testata? Permette di visualizzare o meno le note presenti in testata delle registrazioni.
 * Note righe? Permette di visualizzare o meno le note presenti sulle righe delle registrazioni.
 * Note analitica? Permette di visualizzare o meno le note presenti sulle righe di analitica delle registrazioni.
 * Note scadenze? Permette di visualizzare o meno le note presenti sulle rate delle registrazioni.
 * Stampati Giornale? Permette di visualizzare o meno le registrazioni già stampate sul giornale.
 * Stampati Registro IVA? Permette di visualizzare o meno le registrazioni il cui registro IVA sia stampato in definitivo.
 * Stampati Prima nota?  Permette di visualizzare o meno quelle registrazioni per cui sia già stata effettuata una stampa di prima nota.
 * Intercompany. Permette di visualizzare o meno le registrazioni intercompany.
 * Solo Totale? Permette di visualizzare solo le righe di totale. Il livello di totalizzazione è definito in base alla funzione scelta.
 * Ometti Data/Utente? Permette di escludere dalla stampa l'utente e la data di lancio.


### Tasti funzionali
 * F06 Conferma. Permette di confermare l'esecuzione della funzione.
 * F11 Parametri. Se indicata coma modalità di lancio la stampa permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 Parzializzazioni. Permette di accedere alla finestra delle prazializzazioni.
 * F17 Impostazioni. Permette di accedere alle impostazioni.

## Formato lista
All'interno del formato lista vengono restituite tutte le registrazioni che rispettano i parametri impostati nel formato guida : 

![C5C010_026](http://localhost:3000/immagini/MBDOC_OGG-P_C5NAE4L/C5C010_026.png)
Nell'esempio in figura è stata scelta la funzione 'Per utente/data/azienda/esercizio' e indicato l'utente 'BSI', pertanto i record insseriti dall'utente BSI sono ordinati per data registrazione e azienda. Le informazioni visualizzabili per ogni registrazione variano al variare della funzione scelta e delle impostazioni assegnate. In generale sono, comunque, riportate le principali informazioni di testata (numero e data registrazione, numero e data documento, intestatario della registrazione e informazioni sul protocollo), di riga (conti, importi, segni), di analitica (centri di costo e voci di spesa con i relativi importi) e di rata (scadenza, pagamento, segno rata, importo).
Vediamo un esempio completo : 

![C5C010_036](http://localhost:3000/immagini/MBDOC_OGG-P_C5NAE4L/C5C010_036.png)
In questo caso le informazioni riportate sono : 
 * Testata : 
 ** Numero e data registrazione
 ** Utente di inserimento
 ** Esercizio di riferimento
 ** Nimero e data documento
 ** Codice pagamento
 ** Importo della registrazione
 ** Note presenti in testata
 * Righe : 
 ** Numero riga
 ** Soggetto/conto presente sulla riga
 ** Causale contabile di riga
 ** Importo e segno registrazione
 ** Note righe
 * Rate : 
 ** Progressivo rata
 ** Data scadenza
 ** Tipo pagamento
 ** Numero e data documento
 ** Codice pagamento
 ** Importo e segno rata
 ** Note rata
 * Analitica
 ** Centro di costo
 ** Voce di spesa
 ** Importo
 ** Note analitica

### Opzioni
Sulle testate sono disponibili le seguenti opzioni : 

Sulle righe sono disponibili le seguenti opzioni : 

Sulle rate sono disponibili le seguenti opzioni : 

Sulle righe di analitica sono disponibili le seguenti opzioni : 

## Formato dettaglio
All'interno della lista delle registrazioni di prima nota è possibile disporre di diverse opzioni a livello di riga che consentono di modificare, copiare, cancellare, ecc. le registrazioni. Accedendo con una di queste opzioni è possibile visualizzare il dettaglio della registrazione contabile : 
