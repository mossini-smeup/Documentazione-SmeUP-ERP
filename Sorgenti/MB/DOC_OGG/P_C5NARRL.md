## Obiettivo
Attraverso questa voce di menù è possibile eseguire l'estrazione delle rate scadute per procedere al successivo sollecito.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D010_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5NARRL/C5D010_007.png)
All'interno del formato guida è necessario selezionare la modalità di lancio dell'interrogazione :  le opzioni disponibili sono stampa, interrogazione ed estrazione. Attraverso le prime due modalià è possibile conoscere quali scadenze verrebbero estratte lanciando l'estrazione visualizzandole rispettivamente all'intenro dello spool oppure a video. La terza opzione consente, invece, di eseguire l'estrazione e popolare il file dei solleciti.
All'interno di questo formato è anche possibile definire per quale scadenzario eseguire l'estrazione (attivo o passivo), l'azienda su cui lavorare ed eventualmente una precisa data scadenza e/o un preciso ente per il quale si vogliono estrarre le rate scadute.

Dal formato guida è anche possibile accedere a parzializzazioni e impostazioni dell'interrogazione rispettivamente tramite il tasto F13 e F17 oppure digitando i relativi pulsanti.
Le parzializzazioni si presentano in questo modo : 

![C5D010_008](http://localhost:3000/immagini/MBDOC_OGG-P_C5NARRL/C5D010_008.png)
Attraverso di esse è quindi possibile parzializzare le rate estratte secondo diversi parametri (esercizio, tipo rata, tipo pagamento, data scadenza, ecc.). Partendo da questa schermata è possibile digitare nuovamente F13 (o premere il pulsante Altre parzializzazioni) per ottenere un filtro su altri campi (rapporto bancario, banca d'appoggio, utente di inserimento, ecc.).
Le impostazioni si presentano, invece, in questo modo : 

![C5D010_009](http://localhost:3000/immagini/MBDOC_OGG-P_C5NARRL/C5D010_009.png)
Al loro interno è possibile definire una specifica data di sollecito (che verrà riportata sulla lettera inviata al cliente), una data scadenza limite (quindi le rate con scadenza superiore alla data qui impostata non verranno considerate), uno specifico tipo di sollecito da emettere (ad esempio si potrebbe di richiedere di estrarre solamente le rate al primo sollecito), assegnare uno specifico tipo al primo sollecito che quindi sarà diverso dal primo sollecito standard. Il campo 'Tipo lista' permette di visualizzare solo una specifica tipologia di enti mentre nel campo 'Lista attributi' è possibile definire un elenco di attributi associati agli enti e un range di valori entro cui questi attributi devono stare affinchè l'ente venga preso in considerazione (ad esempio si potrebbe estrarre l'elenco delle rate da sollecitare di clienti francesi). Attraverso l'ultimo campo è, invece, possibile forzare il tipo di sollecito da applicare alle rate estratte :  se ad esempio si decide di forzare il primo sollecito anche le rate già sollecitate una volta prenderanno questa tipologia di sollecito.

Confermando il formato guida è possibile accedere al formato lista.

## Formato lista
All'interno del formato lista viene restituito l'elenco delle rate che verrebbero estratte lanciando la funzione in esecuzione : 

![C5D010_010](http://localhost:3000/immagini/MBDOC_OGG-P_C5NARRL/C5D010_010.png)
Le rate riportate nella lista vengono ordinate per data scadenza. Per ogni rata sono riportate le seguenti informazioni : 
 * tipologia di sollecito
 * data documento
 * ente intestatario e relativa ragione sociale
 * numero documento
 * data scadenza
 * tipo pagamento
 * codice valuta
 * importo scaduto in valuta
 * segno registrazione (dare/avere)
 * importo scaduto in euro

Per ogni data scadenza è poi riportato un riassunto che riporta l'ammontare scaduto a una certa data.
In fondo alla lista è poi riportato un totale scaduto generale per ogni valuta presente.


## Formato dettaglio
Per ogni rata da sollecitare sono disponibili le seguenti opzioni : 

![C5D010_011](http://localhost:3000/immagini/MBDOC_OGG-P_C5NARRL/C5D010_011.png)
Vediamo le principali opzioni :  attraverso l'opzione di pareggio è possibile pareggiare tra loro rate di segno opposto, l'opzione ES permette di estrarre una singola rata, le opzioni sottostanti consentono di gestire la registrazione e la rata. Dal formato lista è possibile stampare la lettera di insoluto o di estratto conto inserendo una singola rata attraverso le opzioni 17 e 20 rispettivamente, creare o modificare distinte e visualizzare la partita associata a una singola rata con l'opzione VP.
