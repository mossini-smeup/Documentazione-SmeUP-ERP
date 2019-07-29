# Introduzione
È sempre stata sentita l'esigenza di analizzare nell'ambito di un MRP perché si produce qualcosa, oppure di che cosa abbiamo bisogno per produrre qualcosa.
Per rispondere a queste domande dobbiamo rifarci alla rappresentazione dell'MRP che è riporatata in fig. 1.
In questa rappresentazione l'MRP appare come una matrice di fonti positive e negative (coperture e fabbisogni), con una data e collegate da un legame verticale che è la struttura della distinta base.
Quindi, per soddisfare la nostra esigenza, si è sviluppata una funzione, chiamata navigazione, che permette di scandagliare questa matrice individuando le relazioni tra coperture e fabbisogni.

![M5_002_01](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_01.png)
La figura precedente è una rappresentazione MRP come insieme datato di fabbisogni e coperture a diversi livelli di distinta; le barre scure rappresentano i fabbisogni, quelle chiare le coperture e l'estensione indica la quantità dell'evento.

# Legami verticali ed orizzontali
I legami che implicitamente si creano all'interno della matrice MRP (che poi è l' archivio dei suggerimenti) sono di due tipi :  verticali (ossia tra livelli di distinta diversi) e orizzontali (ossia allo stesso livello di distinta).
I **legami verticali** sono i consueti legami tra ordine e impegno :  da un ordine è possibile derivare tutti i suoi impegni e da un impegno è possibile determinare l'ordine di appartenenza.
I **legami orizzontali** sono invece gli appuntamenti tipici delle situazioni in cui si deve eseguire un bilanciamento tra coperture (datate o meno) e fabbisogni (sempre datati).
L'assunto di base (che è il fondamento dell' MRP) è che il bilanciamento avviene per data. A pari data, la priorità viene stabilita dall'ordinamento (campo presente nella fonte :  tabella 'M5E' o 'M5F').
Per la modalità in cui la pianificazione si sviluppa (presenza di giacenza, lottizzazioni, raggruppamenti di ordini pianificati), il legame tra coperture e fabbisogni può essere eterogeneo :  un fabbisogno è soddisfatto da più coperture e, analogamente, una copertura è soddisfatta da più fabbisogni.
Bisogna quindi individuare i legami elementari, che contengono la quantità comune al fabbisogno e alla copertura.
Il legame può essere tra fabbisogno e copertura oppure tra copertura e fabbisogno.
Di seguito si farà riferimento al primo termine per identificare l'intero legame.
Esso contiene, oltre ai codici che individuano il fabbisogno e la copertura (nel caso di Sme.up il numero di record origine), tre quantità : 
 * la quantità sua, che è la quantità effettiva del legame, comune a fabbisogno e copertura;
 * la quantità precedente, che nel caso del fabbisogno corrisponde alla quantità che esso ha riservato per coperture precedenti, mentre, nel caso della copertura è la quantità soddisfatta da fabbisogni precedenti. Essa indica, in pratica, il modo in cui si posiziona temporalmente, all'interno della quantità complessiva del fabbisogno o della copertura;
 * la quantità totale del fabbisogno o della copertura.

![M5_002_02](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_02.png)
![M5_002_03](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_03.png)
![M5_002_04](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_04.png)
Come si vede, la quantità precedente è la somma di tutte le quantità precedenti, rispettivamente dello stesso fabbisogno o della stessa copertura.
Si noti inoltre che la colonna della quantità sua è uguale nelle figure 2B e 2C, in quanto esse sono due rappresentazioni diverse dello stesso fenomeno, ossia del legame elementare tra copertura e fabbisogno in figura 2B e tra fabbisogno e copertura in figura 2C.
Il legame è, per sua natura, dinamico :  introducendo un fabbisogno con data inferiore ad uno esistente, la copertura che soddisfaceva il fabbisogno originale, va a coprire il nuovo fabbisogno.
Per evitare questo fenomeno, è necessaria una disciplina nell'inserimento dei fabbisogni indipendenti. Essa può essere, ad esempio, introdotta con la loro datazione tramite strumenti ATP.

![M5_002_05](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_05.png)
## Esplosione
Lo scopo primario dell'esplosione è la presentazione, a tutti i livelli, delle coperture necessarie a soddisfare un fabbisogno.
Selezionando un fabbisogno, vengono come prima cosa determinate le coperture che lo soddisfano allo stesso livello (nel modo illustrato in precedenza). Si scandiscono quindi gli impegni della copertura, per ciascuno dei quali si ripete la procedura di determinazione delle coperture al livello e si procede fino a quando si incontrano coperture senza impegni collegati (presumibilmente giacenze
oppure ordini di acquisto).
Iniziando invece l'esplosione con una copertura, si parte con la scansione dei suoi impegni e ci si riconduce al caso precedente. Si può così eseguire una sorta di analisi mancanti :  ad esempio, al rilascio
di un ordine, si verifica la presenza dei suoi materiali, con una stima della loro criticità (se un componente, ad esempio, non ha ancora copertura 'certa', cioè né con giacenza né con ordini rilasciati, ma
solo pianificati).

![M5_002_06](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_002_06.png)
# Implosione
Lo scopo primario dell'implosione è invece la presentazione dei fabbisogni (ragionevolmente indipendenti) che sono soddisfatti da una copertura.
Selezionando una copertura, vengono come prima cosa determinati i fabbisogni che essa soddisfa, allo stesso livello (nel modo illustrato in precedenza), per ciascuno dei quali si risale alla copertura da
cui dipende.
Per ogni copertura si ripete la procedura di determinazione dei fabbisogni del livello e si procede fino a quando si incontrano fabbisogni senza coperture superiori (fabbisogni indipendenti).
È possibile iniziare l'implosione anche con un fabbisogno :  si parte con la risalita alla copertura da cui dipende e ci si riconduce al caso precedente, anche se non paiono esservi utilizzi applicativi specifici
per questa funzione.
In implosione, nei livelli superiori, viene presentata la quantità anche in termini del componente da cui si è partiti.

# Scansione riepilogata
È stata implementata anche, in conformità con la distinta base, una scansione riepilogata.

Si deve innanzitutto precisare il concetto di riepilogo, che non si applica alla totalità di un articolo come in distinta base, ma a tutti i legami dello stesso consiglio di pianificazione.
Ad esempio, se un componente d'acquisto è presente in più rami di distinta e, per motivi di raggruppamento è approvvigionato con un unico ordine, nell'esplosione scalare l'ordine appare più volte, ciascuna con la 'sua' quantità specifica. Nell'esplosione riepilogata, invece, tutte queste coperture vengono raggruppate in un'unica riga, con la quantità che è la somma delle 'sue' singole quantità.

Analogamente, nell'implosione riepilogata vengono sommati tutti i fabbisogni dello stesso consiglio di pianificazione.
La scansione riepilogata è stata differenziata tra esplosione e implosione, in quanto esse soddisfano esigenze diverse.

L'esplosione riepilogata riporta le coperture di tutti i livelli, ordinata per data, in modo che per prime vengano le giacenze e successivamente gli ordini (sia in corso sia pianificati).

L'implosione riepilogata viene invece eseguita ai prodotti finiti :  riporta, sempre ordinati per data, i fabbisogni indipendenti soddisfatti dalla copertura selezionata.

# Eccedenza
Un utilizzo interessante di queste scansioni è l'individuazione dei disturbi introdotti dall'eccedenza.
Ricordo che l'eccedenza è un suggerimento emesso dall'MRP in presenza di una disponibilità finale positiva. Un'eccedenza presente è dovuta ad una giacenza superflua, un'eccedenza futura è invece
dovuta alla presenza di lotti minimi e multipli, che impedisce di emettere suggerimenti di riduzione su ordini in corso oppure di pianificare nuovi ordini per quantità minori.
Si può interpretare l'eccedenza come un fabbisogno indipendente che porta a zero la disponibilità finale. Come fabbisogno può essere esploso :  si individuano le coperture che (parzialmente o totalmente) servono per coprirlo. In realtà esse non sono coperture superflue perché sono dovute ai vincoli della lottizzazione, ma in questo modo se ne possono valutare gli effetti negativi.
In implosione, si vede invece in che misura una copertura contribuisce a soddisfare l'eccedenza e quindi a trarne le opportune conseguenze.

# Simulazione
È possibile, in implosione, simulare l'effetto sugli assiemi superiori e in particolare sui fabbisogni indipendenti, provocato da un 'peggioramento' di una copertura :  riduzione di quantità e/o ritardo della
data di consegna :  vengono evidenziati i fabbisogni che diverrebbero non più evadibili alle date previste, con la relative quantità non fattibili.

# Nota tecnica
Le applicazioni che abbiamo descritto trovano il loro utilizzo nei seguenti punti di Sme.up : 
 * all'interno della funzione di interrogazione dell'MRP;
 * come funzione collegabile a un ordine di acquisto, di vendita o di produzione, in modo da poter valutare la sua situazione di materiali, sia come fabbisogni, sia come coperture;
 * come funzione di scansione, simile alla distinta base, che può essere inserita in applicazioni specifiche.

# Conclusioni
La capacità di individuare il legame orizzontale (detto di copertura o di appuntamento) tra fabbisogni e disponibilità permette di "vedere" l'MRP con una matrice x-y dove l'asse verticale rappresenta la
struttura del prodotto, ossia il passaggio dal finito ai componenti e quello orizzontale rappresenta il soddisfacimento dei fabbisogni.
A questo punto è stato possibile realizzare la scansione nel piano x-y di ciò che necessita a tutti i livelli per produrre un finito (esplosione) e di ciò che la disponibilità di un componente soddisfa a tutti i livelli (implosione).

# Analisi dei risultati e applicazione dei suggerimenti
Possiamo avere suggerimenti di : 
 * spostamento delle date di ordini (acquisto, produzione) già rilasciati quando il fabbisogno ha date diverse rispetto agli ordini;
 * cancellazione di ordini (acquisto, produzione) già rilasciati, quando il fabbisogno è minore della disponibilità;
 * creazione di nuovi ordini produzione, quando il fabbisogno è superiore alla disponibilità e la politica è di produzione;
 * creazione di nuovi ordini di acquisto, quando il fabbisogno è superiore alla disponibilità e la politica è di acquisto.
I suggerimenti possono essere interrogati per articolo, commessa, tipo suggerimento e fonte di disponibilità.

Si utilizza il formato seguente : 

![M5_001_09](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_001_09.png)
Il sistema presenta una lista dei suggerimenti in base al metodo di selezione scelto.

Ad esempio : 

![M5_001_10](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_001_10.png)
da notare : 
 * __tipo suggerimento__  -->  può essere AE = agire sull'esistente, PN = pianificare un nuovo ordine;
 * __codice suggerimento__  -->  può essere PR - AQ - LV (quando il tipo è PN e definisce se l'ordine pianificato è di produzione, acquisto, conto lavoro), MO - EL (quando il tipo è AE e definisce se il suggerimento è di modifica o cancellazione. inserendo l'opzione "ES" in corrispondenza del suggerimento, il sistema emette una finestra con l'esposizione del suggerimento : 

![M5_001_11](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_001_11.png)
Per i suggerimenti di modifica, di fianco alla data suggerita ci possono essere il segno -> oppure <-, che significano rispettivamente anticipa o posticipa.
L'opzione sulla sinistra del suggerimento può attivare delle funzioni che dipendono dal tipo / codice suggerimento e dal suo stato : 

![M5_001_12](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUC1/M5_001_12.png)
L'applicazione dei suggerimenti può essere : 
 * modifica;
 * creazione di un ordine (fatta direttamente come applicazione del suggerimento nella videata di gestione suggerimenti)  -->  in base alla politica di riordino associata all'articolo vengono generati ordini di produzione o montaggio oppure ordini di acquisto (in questo caso viene chiesto se creare un nuovo ordine o aggiungere una riga ad un ordine già esistente).
È possibile sia l'applicazione del suggerimento proposto dall'MRP, sia l'applicazione con variazione del suggerimento (possono essere modificati quantità, data, fornitore).
