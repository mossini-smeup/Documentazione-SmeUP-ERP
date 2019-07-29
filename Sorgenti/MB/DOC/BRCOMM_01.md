## Perché introdurre la gestione commesse
La gestione per commessa si può utilizzare per avere delle situazioni separate e distinte per : 

- costi di produzione
- logistica dei materiali
- attività e le registrazioni conseguenti

Una delle caratteristiche che normalmente si incontrano in una gestione per commessa è quella di avere degli ordini cliente di articoli, generalmente complessi, configurati o
realizzati specificatamente per quel cliente.

In questi casi è interessante controllare sia tutti i costi, a partire dalla progettazione fino alla produzione e, certe volte, anche dopo l'installazione in casa del cliente (assistenza, garanzia, ricambi, ...);
sia la gestione logistica, dall'acquisto delle materie prime e dei componenti significativi alla produzione, alla prenotazione componenti e loro segregazione in aree riservate,
fino alla definizione di ordini di produzione e montaggio specifici per commessa.

## Vantaggi
Con una gestione per commessa tutti gli ordini di vendita, di acquisto e di produzione, le giacenze, la disponibilità, sono per commessa; questo significa la possibilità di avere immediatamente il quadro completo della situazione logistica della commessa.

Deve essere anche  considerato che tutti i movimenti di magazzino e le attività di produzione sono per commessa quindi anche sul fronte dei costi consuntivi esiste la possibilità di
avere immediatamente il quadro completo della situazione.

## Limiti
Premesso che la gestione a commessa dei materiali puo' essere implementata anche solo per alcuni materiali, nel caso in cui fosse implementata per tutti si avrebbe come limite il seguente : 
il materiale giacente a magazzino risulta giacente su una propria commessa con codice "blank", in questo modo la pianificazione per commessa considera la giacenza di magazzino come
appartenente alla commessa blank e quindi non disponibile per le altre commesse.

Deve essere considerato che se si applica la gestione per commessa i materiali dovrebbero essere approvvigionati per commessa ed al loro ricevimento, invece di andare a magazzino
dovrebbero essere subito dirottati sulla commessa di appartenenza.

Quindi, a rigor di logica, non dovrebbe esistere materiale a magazzino. Questa però è un'assunzione un po' troppo forte :  se consideriamo infatti che in una gestione a commessa è facile
che esista una progettazione ad hoc è anche possibile che, per un cambio in sede di progettazione o per una richiesta di modifica del cliente, certi componenti inizialmente previsti vengano
sostituiti da altri, ci troviamo ad avere a magazzino dei resi da commessa che potrebbero benissimo essere utilizzati in altre commesse ma che non sono visti come disponibili da MRP.

Un altro problema che si incontra nella gestione per commessa è quello dei cambi di priorità e delle rischedulazione delle commesse :  infatti potremmo avere ordinato per una commessa, in un
primo tempo prioritaria, dei componenti necessari anche ad una seconda commessa che è diventata prioritaria successivamente; al ricevimento dei materiali ordinati sulla prima commessa
non è possibile, salvo interventi manuali, dirottare i materiali sulla seconda commessa. In una gestione per commessa la logistica classica non assiste nell'attribuzione dell'articolo più giusto
all'utilizzo più urgente, in base alla situazione attuale di ordini e produzione.

## Suggerimento - Gestione mista
Poiché nella stragrande maggioranza dei casi il cliente non ha esigenze spinte di separazione ed identificazione per commessa di tutte le attività e di tutti i materiali fino all'ultima vite,
il suggerimento è di adottare una gestione per commessa "mista" cioè gestire secondo le modalità standard sia l'acquisto di materia prima ed articoli di consumo comune che la produzione
di particolari comuni, mentre gestire a commessa solo le attività più significative : 

- _2_progettazione, perché responsabile di una parte significativa dei costi e condizionante nel raggiungimento dei tempi di consegna del prodotto
- _2_assemblaggio finale del prodotto, si possono segregare per commessa i componenti del montaggio, è possibile fare un'analisi disponibilità mirata, il montaggio è quello che sicuramente
determina la personalizzazione del prodotto al cliente e dove si possono registrare le differenze maggiori nei tempi di produzione tra prodotti formalmente simili
- _2_acquisto materiali specifici per la commessa, se i materiali sono specifici non esiste il problema di cambi di priorità, avere questi materiali ordinati a fronte della commessa permettedi controllare agevolmente la situazione degli acquisti specifici di una data commessa

## Moduli interessati
Per la gestione commesse si utilizzano parti di applicazioni appartenenti ad una serie ampia di moduli Sme.up, di seguito vediamo i principali.

### Anagrafico commesse
Questo modulo permette la gestione dell'anagrafico commesse.
Una commessa, in base al tipo, può essere attribuita a : 

- un ente
- un oggetto (Sme.up) intestatario
- un oggetto (Sme.up) responsabile
- un oggetto (Sme.up) per il controllo di gestione

Una commessa può anche essere riferita ad un'altra commessa (la commessa madre) in questo modo riusciamo a costruire una gerarchia di commesse e possiamo ad esempio
attribuire alla commessa iniziale (per la realizzazione e l'installazione della macchina richiesta dal cliente) anche tutte le eventuali commesse successive per riparazioni in garanzia,
fornitura di ricambi, trasformazioni ed evoluzioni.

### Distinta base
Spesso in una gestione per commesse capita anche di avere la necessità di fornire un prodotto configurato, in questi casi è normale che la configurazione sia riferita alla commessa.

Nella gestione della distinta base esiste un modalità che prevede una distinta configurata per commessa :  si utilizza uno dei campi sequenza per inserire il codice commessa, uno specifico
programma di aggiustamento nella scansione distinta permette di eseguire una distinta di produzione evidenziando solo i legami validi per la commessa in input.

La limitazione ad un simile metodo di configurazione sta nella lunghezza del campo commessa, che deve poter essere inserita nella sequenza.
In termini di calcolo preventivo del costo materiale per commessa è possibile usare la funzione di esplosione riepilogata di produzione configurata per commessa ed utilizzare il tipo/livello
costo voluto.

### Documenti
Nelle righe dei documenti deve essere compilato il campo commessa, questo permette di attribuire alla specifica commessa tutti i fatti di competenza del ciclo esterno (ciclo attivo / ciclo passivo), cioè righe ordini vendita, righe ordini acquisto, righe bolle / fatture di spedizione, righe bolle di ricevimento, ecc.

### Ordini produzione
Come per i documenti del ciclo esterno, nelle testate degli ordini di produzione deve essere compilato il campo commessa, questo permette di attribuire la produzione alla specifica
commessa :  versamenti, impegni / prelievi componenti, impegni risorse, attività di produzione,  ecc.

### Movimenti
In tutti i movimenti fatti a fronte di commessa è compilato lo specifico campo (nei movimenti manuali deve essere obbligatorio).

Esiste un'interrogazione specifica dei movimenti di una commessa.

### Giacenze
Dove richiesto, le giacenze devono essere differenziate per commessa, cioè devono avere la commessa come uno dei codici caratteristici definiti nel tipo giacenza.
Ovviamente, se nel tipo giacenza è presente anche la commessa, questa dovrà essere inserita in tutti i movimenti manuali, mentre nei movimenti eseguiti da sistema dovrà essere possibile recuperare la commessa di competenza, attraverso opportuni programmi di aggiustamento, durante la scrittura della transazione di movimentazione.

### MRP
Una delle varie modalità di esecuzione dell'MRP di Sme.up è quella dell'MRP per commessa, in questo caso il codice di separazione è la commessa e questo significa che l'MRP
elaborerà tutte le fonti ed i suggerimenti, come se fossero separati verticalmente, commessa per commessa.

Tutte le fonti che non hanno una separazione per commessa e gli articoli che non hanno delle politiche di riordino per commessa saranno trattati per definizione come appartenenti ad
una commessa blank e conseguentemente gestiti come appartenenti ad una commessa separata.

Non esiste la possibilità di bilanciamenti automatici tra una commessa e l'altra, cioè gli eccessidi una commessa non vengono automaticamente girati dall'MRP per coprire difetti di altre
commesse. Quindi giacenze di magazzino non possono bilanciare fabbisogni di commesse.

Tra le possibilità offerte dall'MRP che possono essere agevolmente sfruttate nel caso di gestione per commessa c'è quella di poter rieseguire l'MRP solo per una commessa senza dover
rieseguire tutto l'MRP per la totalità degli articoli :  vengono cancellati e ricalcolati solo i suggerimenti riferiti alla commessa in input.
