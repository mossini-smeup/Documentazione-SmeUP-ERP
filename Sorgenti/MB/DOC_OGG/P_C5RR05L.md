## Obiettivo
Attraverso questa voce di menù è possibile registrare l'esito di effetti attivi così come il richiamo di assegni di cui si sia già registrato l'incasso.
E' da ricordare che nel caso in cui la registrazione dell'esito effetti avvenga tramite servizio di remote banking a questa fase dovrà necessariamente precedere la fase di salvataggio del flusso trasmesso dalla banca e dell'acquisizione dello stesso da parte del gestionale. Questa fase si realizza scaricando dal sito di remote banking il flusso dell'esito degli effetti aziendali e salvando questo file all'interno della cartella Sme.UP appositamente creata. Terminato il salvataggio si dovrà procedere all'acquisizione del file attraverso la voce 'Ricezione esiti da remote' dal menù della tesoreria. A questo punto attraverso l'Attribuzione Automatica è possibile spuntare i movimenti corripondenti; quella manuale è consigliata nel caso in cui durante l'automatica ci siano messaggi di errore, come può essere nel caso di assegni protestati.

## Attribuzione Automatica
Cliccando su Esito Effetti e successivamente su Reg. Esito Effetti da Remote, in modo da spuntare automaticamente i movimenti che presentano corrispondenza perfetta; come da figura sottostante impostare i campi, facendo particolare attenzione alla data rispetto alla quale si vuole effettuare la registrazione e l'esercizio.

![C5D010_043](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_043.png)
## Attribuzione Manuale

### Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D010_012](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_012.png)
Al suo interno è necessario impostare i seguenti campi : 
 * Istituto di credito :  indicare in questo campo la banca su cui si deve effettuare la registrazione
 * Metodo :  il metodo definisce il tipo di registrazione da effettuare; le scelte disponibili sono : 
 ** Insoluti :  registrazione di effetti insoluti.
 ** Protesti :  registrazione di effetti protestati.
 ** Richiami :  registrazione di assegni richiamati.
 ** Incassati :  questo metodo non effettua una vera e propria registrazione contabile ma consente di annotare per ogni effetto la data di effettivo incasso comunicata dalla banca (qualora il relativo servizio sia stato attivato presso la banca) indicando anche che l'effetto è stato incassato e quindi non concorre più alla composizione del rischio.
 * Modalità :  è disponibile solo la modalità Interrogazione.

Confermando il formato guida viene presentata una prima schermata di parzializzazione : 

![C5D010_013](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_013.png)
I campi impostabili all'interno della schermata sono i seguenti : 
 * Natura pagamento rata originaria :  in questo campo deve essere impostata la natura del pagamento della rata insoluta (nel caso in cui si stia registrando l'esito di una riba il campo andrà compilato con E mentre nel caso in cui si stia registrando un assegno richiamato il campo andrà compilato con D)
 * Codice pagamento :  è il pagamento che verrà riportato sulla rata di insoluto
 * Data registrazione (obbligatorio) :  indica la data di registrazione dell'insoluto
 * Esercizio (obbligatorio)
 * Conto contabile :  è il conto contabile associato alla banca indicata nel formato guida
 * Carico spese :  è possibile indicare se le spese sono a carico dell'azienda (opzione A) oppure del cliente (opzione S). Questo campo ed i tre successivi diventano ininfluenti qualora venga attivata la tesoreria, poichè le considerazioni saranno determinate dalla parametrizzazione della stessa.
 * Tipo spesa :  indica se le spese inserite sono spese totali (opzione 1) oppure sono spese per singola rata insoluta (campo blank)
 * Importo spese :  in questo campo va indicato l'importo unitario delle spese bancarie
 * Separa spese :  in questo campo è impossibile indicare se all'interno della registrazione contabile le spese bancarie devono essere registrate in un'apposita riga separata da quella che identifica la rata dell'ente oppure no.
 * Stampa lettere :  la registrazione di un insoluto su un cliente genera una lettera che riporta le rate insolute e che è possibile inviare al cliente. Attraverso questo campo è possibile evitare la generazione di questa lettera.
 * Ricerca su base esterna :  questo campo deve essere impostato a 1 nel caso in cui la registrazione degli insoluti venga effettuata tramite remote (se richiamo il programma partendo dalla banca, mentre è automatica se richiamo la funzione dall'azienda). In questo caso verranno registrati gli insoluti indicati nell'apposito file smeup predisposto per contenere gli insoluti comunicati dalla banca tramite il servizio di remote banking e acquisito trmaite la procedura indicata sopra.
 * Estrazione solleciti :  attraverso questo campo è possibile forzare l'estrazione dei solleciti al termine dell'immissione degli insoluti
 * Dettaglio per rata :  attraverso questo campo è possibile ottenere una registrazione dettagliata per rata
 * Contabilizza per pratica :  attraverso questo campo è possibile forzare che venga effettuata una registrazione differente di insoluto a parità di n° distinta di presentazione.

Confermando questa prima schermata viene presentata un'ulteriore schermata di parzializzazione : 

![C5D010_014](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_014.png)
Al suo interno è possibile impostare i seguenti campi : 
 * Ricerca :  determina come effettuare la ricerca delle rate; le scelte disponibili sono :  per codice cliente, per scadenza/codice cliente, per scadenza/ragione sociale cliente.
 * Filtro rischio :  se attivato permette di visualizzare nella lista solo gli effetti che risultano ancora a rischio.
 * Filtro banca (obbligatorio) :  in questo campo è possibile impostare la ricerca delle sole rate di pagato che riportino come banca di presentazione la banca indicata nel formato guida (opzione S) oppure la ricerca di rate di pagato che non abbiano valorizzata la banca di presentazione (opzione N)
 * Banca d'appoggio :  è possibile specificare l'ABI/CAB della banca di appoggio dell'incasso
 * Soggetto :  in questo campo è possibile indicare la tipologia (per clienti è CLI) e il codice dell'ente di cui si vuole registrare l'insoluto
 * Numero titolo :  è possibile specificare il numero del titolo nel caso in cui l'incasso sia stato registrato come incasso di titoli
 * Scadenza :  in questi campi è possibile impostare un range di date scadenza entro cui ricercare le rate di pagato
 * Debitore :  è possibile indicare il riferimento del debitore riportato sul titolo
 * Piazza debitore :  è possibile indicare il riferimento del debitore riportato sul titolo

Confermando anche questa seconda schermata di parzializzazioni si passa alla lista di rate di pagato.

### Formato lista
All'interno del formato lista sono riportate tutte le rate di pagato che soddisfano le condizioni indicate all'interno delle parzializzazioni : 

![C5D010_015](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_015.png)
Per ognuna delle rate sono riportati la data scadenza, la data documento, la valuta, l'importo, il cliente, il numero di pratica, il numero di titolo, il debitore e la piazza (se presenti).
Le rate che presentano all'inizio un asterisco sono rate cumulate :  per esse è riportato l'importo totale delle rate che compongono la rata cumulata. Immediatamente sotto la rata cumulata è visualizzato il dettaglio delle rate che la compongono.
Per selezionare le rate di cui si vuole registrare l'esito è sufficiente mettere una X sul campo a sinistra e confermare con F6 : 

![C5D010_016](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_016.png)
Nella schermata che compare confermando con F6 è riportata una sintesi della registrazione che verrà effettuata; in particolare sono riportati : 
 * Natura del pagamento
 * Tipo, data registrazione e esercizio
 * Importo totale della registrazione
 * Tipo pagamento
 * Conto di contropartita
Inoltre per ogni rata sono riportati : 
 * Tipologia di spesa (a carico azienda o cliente)
 * Indicazioni sull'eventuale cumulo
 * Cambio
 * Importo spese associate alla rata
 * Ente
 * Numero e data documento
 * Data scadenza
 * Importo singola rata
 * Importo spese amministrative. E' possibile impostare un valore fisso relativo a queste spese che viene automaticamente imputato all'interno di questa schermata.
Nel caso in cui nella prima schermata delle parzializzazioni sia stato indicato che le spese sono totali il sistema imputa in automatico le spese alla prima rata di ogni ente selezionato.
Le informazioni riportate all'interno di questa finestra sono modificabili.
Nel caso in cui si vogliano inserire insoluti di un altro soggetto è sufficiente digitare F8. In questo modo verrà nuovamente presentata la schermata di impostazione del codice ente già vista sopra e si procederà esattamente come appena visto.

Confermando con F6 la schermata riassuntiva delle spese della registrazione si passerà alla registrazione contabile vera e propria che andrà confermata sempre con F6 : 

![C5D010_017](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR05L/C5D010_017.png)