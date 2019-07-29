# Definizioni

## Sezione / subsezione
Una scheda è divisa in una o più finestre (dette sezioni), ognuna delle quali ospita una o più visualizzazioni di dati (ad esempio un albero e una matrice), dette subsezioni.

## Etichetta (Tag)
È il "titolo" di una subsezione.
Il suo colore indica lo stato di caricamento della subsezione :  nera caricata, blu da caricare oppure ricaricabile (ad esempio perchè sono variati alcuni dei suoi parametri).
![LOCEXD_046](http://localhost:3000/immagini/LOCEXD_C/LOCEXD_046.png)## Barra degli strumenti (Tool bar)
È la barra presente nella parte inferiore della scheda, contiene bottoni che eseguono le azioni associate ai tasti funzionali.
![LOCEXD_031](http://localhost:3000/immagini/LOCEXD_C/LOCEXD_031.png)
# Navigazione
## Uso del mouse
Tutta la navigazione della scheda viene effettuata tramite il mouse.

### Tasto sinistro

- Click sulle etichette delle subsezioni :  carica le subsezioni non ancora caricate o sceglie quale subsezione visualizzare se una sezione ospita più subsezioni.
- Doppio click su un oggetto(spesso associato a un'icona, ma non necessariamente) :  effetto è variabile a seconda del contesto, in genere parte la scheda associata all'oggetto, però questo può essere ridefinito dal componente o dal servizio associati alla subsezione.
- In alcuni casi è possibile selezionare (sempre cliccando con il mouse) un elemento di una subsezione per condizionare la rappresentazione di un'altra subsezione. Ad esempio posso avere una subsezione che mostra un albero di periodi e cliccando su un periodo indico a una subsezione che mostra una matrice di costi su quale periodo effettuare l'analisi.


### Tasto destro

- Click sulle etichette delle subsezioni :  apre un menù a tendina contenente una serie di azioni associate alla subsezione (documentate di seguito).
- Click su un oggetto :  apre un menù a tendina contenente le azioni associate all'oggetto. Molte di queste azioni sono standard e appaiono in qualunque punto di Looc.up si clicchi su un oggetto di quel tipo, altre sono specifiche di un determinato contesto.

![LOCEXD_030](http://localhost:3000/immagini/LOCEXD_C/LOCEXD_030.png)Ricordo che in Web.UP non è possibile utilizzare il tasto destro del mouse!

## Funzioni sulle etichette di una subsezione
Cliccando su un'etichetta con il pulsante destro del mouse si accede ad una serie di funzionalità relative alla subsezione, documentate di seguito.
Queste funzioni hanno effetto solamente sulla subsezione a cui sono associati!
Marchiamo con (T) le funzioni che hanno una valenza esclusivamente tecnica e che interessano solo gli sviluppatori, non i semplici utenti di una scheda.

### Aggiorna
Ricarica la subsezione in esame, ad esempio richiamando la funzione ad essa associata.

### Impostazioni
Permette di effettuare una scelta tra i vari setup definiti per il componente in questa subsezione :  ad esempio, per una matrice è possibile selezionare una visualizzazione raggruppata per un campo piuttosto che una in cui vengono mostrati i totali di una determinata colonna, ecc...

### Visualizza come...
Apre, nella stessa finestra, una nuova visualizzazione dei dati contenuti nella subsezione, permettendo di selezionare il componente che deve effettuare la presentazione tra quelli che possono gestire l'XML dei dati della subsezione.
Ad esempio, se la subsezione contiene una matrice si potrà selezionare matrice, grafico, excel o databeacon, in quanto l'XML che trattano è lo stesso.
Tecnicamente questa azione effettua una nuova chiamata, aprendo un nuovo componente :  per tornare alla scheda si prema F12.
Questa voce è abilitata solo per subsezioni in cui il caricamento dei dati venga affidato alla chiamata a un servizio.

### Help della scheda
Apre una nuova finestra in cui viene visualizzato l'help della scheda (documentazione attiva presente in coda al membro contenente lo script della scheda).

### Stampa della sezione
In Web.UP è possibile abilitare da setup di scheda la possibilità di stampare la singola sezione. basta abilitare il paramentro Printable="YES", in alternativa è possibile stampare anche tutta la scheda dalla bottoniera in alto di Web.UP.
E' possibile in oltre abilitare l'esportazione del componente in formato EXCEL o PDF, presenti nella bottoniera di sezione. Anche in questo caso possiamo abilitare o disabilitare questa funzione da script di scheda, di default sono abiliate le esprtazioni e le stampe.

### Ingrandisci/Ripristina
Massimizza/ripristina a dimensione normale la subsezione.
Tecnicamente questa azione non effettua una nuova chiamata, quindi anche quando la sezione è ingrandita siamo ancora nella scheda di partenza e premendo F12 si esce dalla scheda!
Queste azioni sono eseguibili anche effettuando doppio click con il pulsante sinistro sull'etichetta.
In Web.UP è è possibile mettere a full screen l'intera scheda, una sorta di modalità KIOSK. Oppure abbiamo la possibilità di zoomare sul singolo componente.

### Editor della scheda (T)
Apre una nuova finestra in cui è possibile modificare lo script della scheda in cui è contenuta la subsezione.
Si noti come sia possibile, salvando le modifiche nello script e ricaricando la scheda, aggiornare in tempo reale la visualizzazione.
Una recente novità è la possibilità di editare una scheda anche da Web.UP.

### Visualizza scheda servizio (T)
Apre una nuova finestra in cui viene mostrata la documentazione attiva del servizio che fornisce i dati per la subsezione.
Questa voce è naturalmente solo abilitata per subsezioni in cui il caricamento dei dati venga affidato alla chiamata a un servizio.

### Visualizza XML (T)
Apre il file XML associato alla sezione. La visualizzazione dell'XML viene effettuata con il programma associato in Windows alla visualizzazione di XML (di default Internet Explorer, a meno che non sia installato un programma specifico come XMLSpy, ...).
Se si vuole vedere l'XML da Web basterà entrare in debug (Switch in alto a destra) e premere il bottone debug in alto alla scheda. a questo punto scegliere il TAB XML che ci verrà presentato.

### Visualizza variabili (T)
Apre una finestrella in cui vengono mostrate le variabili "viste" dalla subsezione, suddivise per scope.
## Comandi
## Stampe

## Caricamento differito di una sezione
Nel wizard del G.SUB.SCH e' stato introdotto il campo 'Caricamento' per definire se la scheda deve essere caricata in modo differito o immediato : 
![03COMEXD01](http://localhost:3000/immagini/LOCEXD_C/03COMEXD01.png)Nel caso in cui si scelga il caricamento differito all'apertura della sezione apparirà la scritta 'Sezione a caricamento differito. Per caricare cliccare sulla linguetta del titolo'.

## Menù della sezione in caso di mancanza etichetta
Nel caso in cui su una sezione non sia visualizzata la label che la identifica e' possibile aprire il suo popup selezionando il nuovo pulsante posto in pulsantiera : 
![03COMEXD02](http://localhost:3000/immagini/LOCEXD_C/03COMEXD02.png)