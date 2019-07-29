# Measurement System Analisys
## Definizione
Il Measurement System Analisys (MSA) è un insieme di procedure utilizzate in ambito qualità e finalizzate a individuare e isolare i componenti di variabilità insiti in un processo di misurazione che possono influenzare o inficiare i risultati stessi delle misure.
L'MSA valuta quindi l'intero processo con cui si ottengono le misure, prendendo in considerazione sia le modalità con cui vengono condotte le misurazioni che gli strumenti stessi, al fine di ottenere dei dati attendibili, accurati, stabili e precisi in modo da poterli usare poi nelle analisi di processo o di prodotto.

Per poter svolgere un'analisi di questo tipo occorre
1. Determinare il numero di operatori che saranno coinvolti nei test, il numero di campioni e il numero di ripetute. Più il numero di campioni e di ripetute è elevato, più avremo dei risultati attendibili.
2. Coinvolgere gli operatori che normalmente si occupano di fare misure e che hanno familiarità con gli strumenti e che conoscono già le procedure.
3. Selezionare dei campioni che siano rappresentativi della variabilità del processo per poter ottenere una stima corretta del grado di errore di misura.
4. Definire i valori target dei campioni, effettuando più misurazioni sugli stessi, per un certo periodo di tempo. La media di queste misure costituirà il valore di riferimento.

In queste condizioni, l'MSA consente di individuare in modo preciso la componente della variabilità della misura dovuta allo strumento (EV Equipment Variation indice della ripetibilità), la componente dovuta all'operatore (AV Appraiser Variation indice della riproducibilità) e la variabilità totale ottenuta dalla combinazione delle due precedenti (GRR indice di ripetibilità e riproducibilità). La regola generale per l'accettazione di un sistema di misura è che la percentuale dell'indice combinato non sia superiore al 30% della variazione totale. Valori più alti potrebbero segnalare la presenza di un errore della definizione del target, la presenza di un errore della definizione delle procedure di misura o, peggio ancora, una certa instabilità del sistema di misura.
Se infatti a questo si accompagna la presenza di trend o run nei grafici SPC delle misure, allora ci può essere la necessità di ricalibrare gli strumenti oggetto di analisi.

MSA strumento di misura sono l'oggetto Sme.UP
 :  : DEC T(OG) P() K(H5)

![CQACMC_H501](http://localhost:3000/immagini/CQACMC_04/CQACMC_H501.png)
## Inserimento e gestione di un nuovo documento di MSA
Entrare nel modulo degli strumenti di misura all'interno dell'applicazione CQ. Nel menu di sinistra, cliccare sulla voce "Gestione MSA" presente tra le Actions delle matricole.
Tramite questa voce sarà possibile creare un nuovo documento, modificarlo, copiarlo, cancellarlo o semplicemente visualizzarlo. Le opzioni autorizzate sono visibili a video nella finestra seguente


![CQACMC_H502](http://localhost:3000/immagini/CQACMC_04/CQACMC_H502.png)
**INSERIMENTO :  OPZIONE 1**
Inserire l'opzione "1" o "01" nella casella bianca e premere invio. Questo farà aprire una finestra in cui compare l'elenco degli strumenti di misura. L'elenco viene caricato con la paginazione e quindi per poter consultare tutta l'anagrafica delle matricole occorre paginare con l'apposito tasto della tastiera oppure tramite il bottone "Segue" presente nella parte alta sinistra del video. Se si conosce già il codice dello strumento, è possibile velocizzare la ricerca inserendo questo codice nel campo in alto a destro (campo Pos.01).
Una volta inserita qui la matricola, premere invio. Questo farà caricare l'elenco a partire dal codice inserito.

![CQACMC_H503](http://localhost:3000/immagini/CQACMC_04/CQACMC_H503.png)
Scegliere quindi lo strumento che si deve testare mettendo una "X" sulla riga. La scelta dello strumento comporta l'apertura di una nuova videata in cui alcuni campi vengono già compilati in automatico (a partire dall'anagrafica dello strumento di misura scelto) e altri devono essere compilati in modo opportuno rispetto all'analisi che stiamo facendo.

Per la compilazione di dettaglio, si rimanda ai paragrafi successivi. La compilazione della videata infatti si differenzia in base al tipo di studio che si vuole fare.


### Campi comuni a tutte le tipologie di studio
Compilare la videata immettendo : 
1. ARTICOLO DA VERIFICARE :  inserire un codice articolo dell'anagrafica che corrisponda al codice articolo che verrà utilizzato per la taratura dello strumento
2. CARATTERISTICA :  è la grandezza del ciclo di collaudo del codice articolo che deve essere controllata. Dei due campi richiesti è possibile indicarne anche solo uno (quello della descrizione), scrivendo quindi la caratteristica controllata.
3. NUMERO CAMPIONI :  è il numero di ripetute da eseguire su ogni pezzo
4. NUMERO MISURE :  è il numero di elementi sui quali vengono svolte le misure
5. RISOLUZIONE MATSER :  è il valore che esprime la capacità di rilevare piccole variazioni della grandezza misurata (dovrebbe essere coerente alla sensibilità dello strumento che è il più piccolo valore che lo strumento può misurare).
6. NOMINALE :  è il valore nominale atteso che ci si aspetta di rilevare
7. LIMITE INFERIORE :  indica il valore minimo considerato valido per la caratteristica
8. LIMITE SUPERIORE :  indica il valore massimo considerato valido
9. OPERATORE A/B/C :  immettere "DI" (che indica DIPENDENTE) O "UP" (*USERPROFILE) nel primo campo e la matricola /Uutente dell'operatore nel campo adiacente. La ricerca delle matricole può essere fatta mettendo il "!" nel campo e premendo poi invio.

### MSA per variabili :  Studio di tipo 1
Per questo tipo di studio occorre poi compilare
* TIPO STUDIO :  inserire il valore 1 dall'elenco precaricato
* TIPO CONTROLLO :  "VA" che indica il controllo per variabili
Per questo tipo di studio gli operatori previsti devono essere almeno 2.
Affinché poi questa tipologia di studio offra risultati attendibili, è importante che il numero totale di valori raccolti (numero di campioni * ripetute) sia almeno pari a 50.

### MSA per variabili :  Studio di tipo 2
Per questo tipo di studio occorre poi compilare
* TIPO STUDIO :  inserire il valore 2 dall'elenco precaricato
* TIPO CONTROLLO :  "VA" che indica il controllo per variabili
Per questo tipo di studio gli operatori previsti devono essere almeno 2.
Affinché poi questa tipologia di studio offra risultati attendibili, è importante che vengano svolte almeno 2 ripetute su 5 campioni.

### MSA per attributi

Per questo tipo di studio occorre poi compilare
* TIPO STUDIO :  inserire il valore 1
* TIPO CONTROLLO :  "AT" che indica il controllo per attributi
Le risposte, sia negative che positive, devono rifarsi ai due elementi della tabella CQE sotto settore H5. Questi due elementi sono infatti quelli che vengono presi come riferimento nella compilazione delle misure.

Una volta inseriti tutti i dati richiesti, premendo INVIO i campi obbligatori retroilluminati di rosso si spengono. Questo è importante perché significa che tutti i campi sono stati compilati correttamente.
Premendo poi F6 si procede alla conferma definitiva dei dati. Alla conferma, viene aperta in automatico una nuova scheda che servirà all'operatore per registrare i valori inseriti.


![CQACMC_H504](http://localhost:3000/immagini/CQACMC_04/CQACMC_H504.png)
Impostare quindi la data in cui si è svolta la misurazione e il codice dell'operatore che ha svolto le misure (si veda il paragrafo relativo alla compilazione dei campi comuni) e premere nuovamente INVIO.

![CQACMC_H505](http://localhost:3000/immagini/CQACMC_04/CQACMC_H505.png)
Inserire nella matrice tutti i valori riscontrati durante le misurazioni in modo ordinato. In questa fase occorre fare molta attenzione al numero di decimali che viene gestito dalle celle della matrice. Se il numero di decimali che viene accettato durante la fase di inserimento non è conforme alle aspettative, occorre andare in modifica della CATEGORIA dello strumento che stiamo analizzando e impostare in modo opportuno il campo intitolato "Numero decimali gestiti".
Inseriti tutti i valori richiesti, confermare il lavoro premendo il bottone "Conferma e salva le misure". Questo permetterà di caricare nuovamente la stessa scheda predisposta all'inserimento della nuova serie di misure rilevate da un nuovo operatore. Cambiare quindi l'operatore in alto e procedere all'inserimento della nuova serie di dati. Ripetere l'operazione anche per il terzo operatore (se previsto).
Per chiudere la scheda e uscire, premere semplicemente il bottone "Chiudi scheda" .

 NB :  in fase di inserimento di un MSA per attributi, oltre a riportare le misure di tutti gli operatori interessati, occorre inserire anche le misure di riferimento e cioè quelle che verranno prese come linee guida per verificare la correttezza o meno delle risposte fornite dagli operatori coinvolti nei test. Il campione di riferimento dovrà essere inserito nel sistema dal responsabile dell'analisi scegliendo nella scheda delle misure, l'operatore "Z  campione di riferimento".

**MODIFICA :  OPZIONE 2**
Inserire l'opzione "2" o "02" nella casella bianca. Digitare un "!" nel campo "Nr.Taratuta" e premere poi INVIO per  vedere l'elenco di tutti i documenti di MSA presenti in archivio.
Scegliere a questo punto il documento che si intende modificare cliccando sulla riga corrispondente. Questo riporterà il numero selezionato nella finestra precedente alla quale risponderemo ancora con INVIO.
Per entrare nel dettaglio delle misure, premere INVIO o F7. Questi ci faranno accedere nuovamente alla scheda delle misurazioni. A questo punto è possibile modificare i campi che devono essere corretti : 
per uscire basterà confermare prima con INVIO e poi con F6. Se si intende modificare un dato della testata del documento, con il primo INVIO il programma farà accedere comunque alla scheda delle misure.
Occorrerà quindi chiudere prima questa e poi confermare la modifica con F6.

**COPIA :  OPZIONE 3**
Inserire l'opzione "3" o "03" nella casella bianca. Digitare un "!" nel campo "Nr.Taratuta" e premere poi INVIO per  vedere l'elenco di tutti i documenti di MSA presenti in archivio.
Scegliere a questo punto il documento che si intende copiare cliccando sulla riga corrispondente. Questo riporterà il numero selezionato nella finestra iniziale alla quale risponderemo ancora con INVIO.
NB :  questo è il documento che vogliamo copiare. Premendo INVIO il programma aprirà un nuovo documento uguale a questo ma con un numero diverso. Si veda infatti la figura seguente : 

![CQACMC_H506](http://localhost:3000/immagini/CQACMC_04/CQACMC_H506.png)A questo punto è possibile modificare i dati del nuovo documento per poi procedere all'inserimento delle misure. Si precisa a questo proposito che la copia del documento di MSA non agisce sulle serie di misure inserite, ma solo sulla testata del documento.

**CANCELLAZIONE :  OPZIONE 4**
Inserire l'opzione "4" O "04" nella casella bianca. Digitare un "!" nel campo "Nr.Taratuta" e premere poi INVIO per  vedere l'elenco di tutti i documenti di MSA presenti in archivio.
Scegliere a questo punto il documento che si intende cancellare cliccando sulla riga corrispondente. Questo riporterà il numero selezionato nella finestra precedente alla quale risponderemo ancora con INVIO.
Confermare la cancellazione con F16.

**VISUALIZZAZIONE :  OPZIONE 5**
Entrare sempre in gestione MSA  inserire l'opzione "5" o "05".
Premendo INVIO si accede al documento in modalità protetta (senza avere la possibilità di modificare alcun dato). Per consultare le misure inserite, premere sempre F7 o semplicemente INVIO.
Consultato il documento, uscire con F12 fino a che non si sono chiuse tutte le videate.

## Visualizzazione dei risultati
Entrare nell'applicazione CQ e scegliere sempre il modulo "Strumenti di misura". Una volta entrati nel modulo, scegliere il surf per strumenti intitolato "Strumenti di misura" per poter consultare i documenti MSA dato un certo strumento e impostare il flag "Cicli e rilievi" per abilitare la navigazione delle informazioni collegate agli strumenti stessi. A questo punto, accanto agli strumenti che hanno almeno un MSA, comparirà nella colonna MSA una lente di ingrandimento che consente di accedere direttamente ai documenti stessi.


![CQACMC_23](http://localhost:3000/immagini/CQACMC_04/CQACMC_23.png)
Facendo doppio click sul numero di MSA, ovvero sul contenuto della colonna intitolata "Identificativo", si può accedere alla scheda del documento.
Di seguito i layout specifici per le tre tipologie di MSA che vengono gestite in Sme.UP.

**MSA per VARIABILI - studio tipo 1**

![CQACMC_24](http://localhost:3000/immagini/CQACMC_04/CQACMC_24.png)
**MSA per VARIABILI - studio tipo 2**

![CQACMC_25](http://localhost:3000/immagini/CQACMC_04/CQACMC_25.png)
**MSA per ATTRIBUTI**

![CQACMC_26](http://localhost:3000/immagini/CQACMC_04/CQACMC_26.png)
## Stampa del certificato
Per eseguire la stampa di un documento di MSA sarà sufficiente andare nella voce di menu "Specifiche MSA Strumenti" e scegliere poi tra le voci : 
* Stampa MSA verticale"
* "Stampa MSA orizzontale"
La differenza tra le due stampe è solo il layout della pagina (orizzontale o verticale). È possibile scegliere indistintamente tra le due tipologie di stampa.
È ovvio che a seconda della numerosità dei dati che si devono stampare (numero di campioni e di ripetute) sarà consigliata la stampa in orizzontale rispetto a quella in verticale.
Le stampe si adattano al contenuto del documento di MSA; a seconda infatti del tipo di studio di MSA, verrà cambiato sia il titolo del certificato che la parte di dettaglio delle misure.

![CQACMC_27](http://localhost:3000/immagini/CQACMC_04/CQACMC_27.png)![CQACMC_28](http://localhost:3000/immagini/CQACMC_04/CQACMC_28.png)
