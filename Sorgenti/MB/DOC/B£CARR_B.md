# Navigazione Standard

## Gestione Carrelli

### Ricerca

A questa scheda si può accedere : 


- Dal modulo B£CARR :  MyLoocup > Applicazioni > B£ > TAB Moduli > B£CARR
- Dalla scheda Debug (tasto rapido CTRL+F9) :  TAB Carrelli
- Dal popup di un oggetto :  Carrello > Scheda gestione carrelli
- Dal formato di richiesta parametri che compare quando si aggiunge un elemento a una cartella (vedi sopra) :  tasto F7


 :  : PAR
Nella sezione Tipo Oggetto vengono elencate le tipologie di oggetto per le quali esistono istanze con carrello. Selezionandone una, nella sezione sottostante si visualizzano le istanze di quella tipologia che hanno un carrello agganciato. L'istanza identifica univocamente un carrello; per ogni istanza può essere attivato un unico carrello.


![B£CARR_004](http://localhost:3000/immagini/B£CARR_B/BXCARR_004.png)
 :  : PAR
Ogni carrello contiene cartelle. Selezionando l'istanza, e quindi il carrello corrispondente, nella sezione centrale in alto viene caricato l'elenco delle cartelle. Le cartelle possono essere di diverse tipologie e si distinguono per omogeneità del contenuto e per utilizzo.
Se è valorizzata la colonna tipo... la cartella è omogenea cioè potrà contenere solo elementi della tipologia specificata.
Se il tipo non è impostato la cartella conterrà oggetti di tipologie distinte.
La cartella *LAST viene creata in automatico con la creazione del carrello e contiene un solo oggetto per ogni tipologia.
La cartella *WORK è specifica per l'istanza di un utente ed è la cartella di lavoro di quell'utente. Viene creata solo per carrelli relativi a istanze utenti e utilizzata in diversi punti di LoocUp.
Per accedere al contenuto di una cartella, bisogna selezionarla dall'elenco e sfogliarne gli elementi nella sezione centrale.
In basso a destra compare un cestino... per eliminare un elemento è sufficiente trascinarcelo sopra con Drag & Drop.




### Azioni
 :  : PAR
In basso, di fianco alla toolbar di navigazione di LoocUp è attiva una sequenza di bottoni. Essi lanciano operazioni di creazione, cancellazione e svuotamento di carrello e di cartelle. Consentono anche l'aggiunta o la rimozione di elementi. Ciascuna di queste azioni passa attraversouna finestra di dialogo con richiesta di conferma.


![B£CARR_007](http://localhost:3000/immagini/B£CARR_B/BXCARR_007.png)
 :  : PAR
L'immagine sopra si riferisce al tasto Aggiungi Elemento.



## Merging
 :  : PAR
Le operazioni di Merging sono un utile strumento di confronto e di travaso di elementi tra cartelle di diversi carrelli. L'azione avviene attraverso operazioni di Drag and Drop.
Le modalità di merging previste sono di due tipologie : 
- merge tra Work e carrello
- merge tra carrelli


### Merge tra cartella di Work e Carrello
Sulla sinistra viene caricata la cartella di WORK specifica dell'utente di lavoro.
Attraverso operazioni di trascinamento (Drag & Drop) tra la cartella di work e il carrello a destra è possibile alimentare o svuotare la medesima su altre cartelle.
E' attivo su entrambi il cestino

![B£CARR_006](http://localhost:3000/immagini/B£CARR_B/BXCARR_006.png)
### Merge tra Carrelli
A destra e sinistra vengono aperti due carrelli.
E' possibile travasare il contenuto della cartella di un carrello in quello della cartella di un altro
E' attivo su entrambi il cestino

![B£CARR_005](http://localhost:3000/immagini/B£CARR_B/BXCARR_005.png)
## Carrello

## Cartella

# Inserimento di elementi tramite Menù di PopUp

## Carrello
La creazione di un carrello avviene implicitamente la prima volta che si inserisce un elemento in una sua cartella, ad esempio dal menu Popup di un oggetto (vedi sotto).
Nella scheda dei carrelli, associata al modulo applicativo B£CARR, si trovano poi tutte le funzioni di gestione degli stessi.

## La cartella di un carrello
### Inserire oggetti
Dal menu Popup di un oggetto è possibile memorizzare l'oggetto stesso in una cartella.

![B£CARR_008](http://localhost:3000/immagini/B£CARR_B/BXCARR_008.png)
Le cartelle disponibili possono essere di varie tipologie. Tra le principali proprietà che le caratterizzano citiamo : 
- il nome può essere prefissato o modificabile
- il proprietario del carrello può essere l'utente che sta eseguendo la funzione o un altro oggetto
- gli oggetti contenuti devono essere tutti dello stesso tiipo o possono essere di tipi diversi.

In particolare abbiamo le cartelle : 

- Appunti  (Alt + C)
Ha la particolarità di memorizzare sempre l'ultimo codice ricevuto di un certo tipo (e parametro),per cui conterrà ad esempio l'ultimo cliente, l'ultimo articolo, l'ultima bolla fornitore, ecc.,mentre tutte le altre cartelle memorizzano ogni nuovo codice che ricevono. Si trova nel carrellodell'utente ed inoltre il suo nome è prefissato e non modificabile. Pertanto non è richiesta l'immissione di parametri da parte dell'utente.
- Di lavoro  (Alt + W)
Contiene un insieme di elementi, anche di tipo eterogeneo. Si trova nel carrello dell'utente ed inoltre il suo nome è prefissato e non modificabile. Pertanto non è richiesta l'immissione di parametri da parte dell'utente.
- Standard per Tipo Oggetto  (Alt + O)
E' una cartella omogenea, ossia tutti gli elementi che contiene devono essere dello stesso tipo. Si trova nel carrello dell'utente ed inoltre il suo nome è prefissato e non modificabile. Pertantoo non è richiesta l'immissione di parametri da parte dell'utente.
- Per Tipo Oggetto ...
E' una cartella omogenea, ossia tutti gli elementi che contiene devono essere dello stesso tipo. Si trova nel carrello dell'utente ed il suo nome ha il formato ttppp.xxxx, dove tt e ppp sono tipoe parametro oggetto e non sono modificabili, mentre xxxx è un nome libero, scelto dall'utente.
- Generico per Tipo Oggetto ...
E' una cartella omogenea, ossia tutti gli elementi che contiene devono essere dello stesso tipo. Può trovarsi in un carrello collegato ad un oggetto qualsiasi, scelto dall'utente. Il suo nome ha il formato ttppp.xxxx, dove tt e ppp sono tipo e parametro oggetto e non sono modificabili, mentre xxxx è un nome libero, scelto dall'utente.
- Cartella libera ...
Contiene un insieme di elementi, anche di tipo eterogeneo. Si trova nel carrello dell'utente ed il suo nome è libero e scelto dall'utente.
- Generico cartella libera ...
Contiene un insieme di elementi, anche di tipo eterogeneo. Può trovarsi in un carrello collegato ad un oggetto qualsiasi, scelto dall'utente ed il suo nome è anch'esso libero e scelto dall'utente.

Se la cartella richiede l'immissione di parametri da parte dell'utente, appare il seguente formatodi richiesta : 

![B£CARR_002](http://localhost:3000/immagini/B£CARR_B/BXCARR_002.png)
Se la cartella è personale dell'utente (= si trova nel carrello dell'utente e non in un carrello Generico), i campi tipo e codice carrello sono preimpostati con il nome utente e non sono accessibili.

## Utilizzare oggetti presenti in una cartella
Le applicazioni possono utilizzare una cartella. Ad esempio nel modello dinamico posso prevedere una sezione in cui presentare tutte e sole le applicazioni che un utente vuole analizzare, oppure,nei flussi finanziari presentare un grafico con le sole fonti che l'utente ha portato in una cartella specifica. Chi scrive l'applicazione potrà decidere di fissare il nome della cartella utilizzata, oppure prevedere un momento di richiesta all'utente del nome della cartella da utilizzare. Ancora qualche esempio : 
- Voglio stampare come PDF un documento che raggruppa tutti i membri che trascino in una apposita cartella.
- Porto in una cartella del cliente tutte le partite che voglio segnalare nell'estratto conto.
- Invio una lettera di richiesta di offerta all'insieme dei fornitori memorizzati in una cartella.
In sintesi si tenga presente che il carrello è uno strumento a disposizione delle applicazioni capaci di utilizzarlo. Man mano sarà utilizzato da nuove applicazioni standard SME.up e comunque è a disposizione per implementazioni specifiche dell'azienda.

## Esercizi / Verifiche di comprensione

- Mediante il tasto rapido ALT+C portare un cliente e un articolo nella cartella appunti e verificarne la presenza.
- Portare nel carrello di lavoro almeno 10 oggetti diversi che si trovano in schede qualsiasi.
- Inserire le applicazioni "BR" e "V5" in una cartella contenente solo applicazioni, di nome "APP"nel carrello personale.
- Creare un carrello per un cliente
- Spostare la cartella "APP" sopra creata nel carrello del cliente appena creato.
- Aprire la scheda dei carrelli e spostare gli oggetti della cartella di lavoro in una cartella di nome "MIX" appartenente al carrello dell'applicazione "BR".



