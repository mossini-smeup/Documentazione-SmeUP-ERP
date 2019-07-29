# Generalità

Il componente matrice è utilizzabile in ambiente device.

La sintassi di definizione è la medesima prevista per l'utilizzo del componente sul client loocup. Rispetto a quello che si può fare sul client, vigono però varie limitazioni ed alcune peculiarità, che vengono a seguire descritte.

# Attributi

A seguire, verranno evidenziate i principali attributi che possono essere sfruttati anche per il device mobile. Per gli attributi assenti si può assumere che questi non siano supportati e vengano quindi ignorati.

* RowHeight (Altezza righe) :  in ambiente mobile, risulta di particolare importanza, in quanto permette di aumentare/diminuire in modo sensibile, il numero di righe presenti contemporaneamente su una schermata.
* CellStyle (Stile Celle) :  attraverso questo attributo è possibile condizionare il relativo layout. Per un maggior dettaglio si rimanda al documento riportato a seguire, qui ci si limita a dire che attraverso è possibile presentare da una fino ad un massimo di 4 colonne con la possibilità di poter inoltre visualizzare un'icona.
* Columns :  se presente, questo attributo condiziona l'ordine con cui vengono presentate le celle, ma non solo, sempre se presente, questo attributo definisce quali sono le colonne che anche oltre quelle visualizzate in lista vengono presentate quando si applica la gesture di "passa a dettaglio".
* ShowHeader :  è possibile omettere la sezione relativa alle intestazioni, in matrici in cui le informazioni riportate nelle celle sono palesemente chiare, è possibile omettere la sezione relativa alle intestazioni, guadagnando un spazio che per il device mobile può essere rilevante.
* ShowTotal :  è possibile attivare anche per il device mobile, la sezione di presentazione dei totali

- [Utilizzo Attributo CellStyle su Device Mobile](Sorgenti/MB/DOC/LOCEXB_MOC)

# Paginazione

Non è gestita, ma nel caso il servizio, mandi l'xml previsto per l'indicazione della presenza di ulteriori pagine, nella videata verrà apposta l'indicazione che il risultato della funzione non è completo.

# Variabili e Dinamismi

Sono disponibili tutte le variabili comunemente utilizzabili sul client loocup che possono poi essere implementate per l'applicazione di dinamismi.

Come tutte le sezioni, il dinanismo applicazione ad un evento può essere unico, e gli eventi sono limitati When="Change" e When="Click".

# Passa a dettaglio

Sulle matrici, in mobile, è prevista una particolare gesture, che permette di passare ad una  schermata di dettaglio fissa, in cui sono riportate tutte le colonne della matrice, visibili in base agli attributi della griglia o alternativamente elencate nell'attributo Columns.

Questa particolare gesture si effettua in questo modo : 
* si poggia un dito sull'estremità destra di una riga di matrice
* tenendo premuto si trascina il dito verso sinistra
* nella riga apparirà a questo punto un icona, affiancata dalla dicitura "Passa a dettaglio", premendola, si accederà alla specifica schermata di dettaglio.

# Considerazioni su Performance

In base alla quantità di dati inviati al device, le performance di presentazione della matrice possono variare di molto. Si consiglia quindi (considerando anche le celle nascoste) di cercare di non superare il numero di duecento/trecento celle.

