# Obiettivo
Obiettivo di questo docuemnto è descrivere il metodo consigliato  di approcio alla costruzione di exit previste dai parametri della BCD per la risoluzione di casi applicativi non gestiti nello standard o nelle exit proposte.

# Struttura Programma
Per realizzare una estensione articolata della schedulazione, normalmente si realizza un programma X a struttura BCD di tipo "mongolfiera" che possiede delle memorie specifiche, ed è richiamato dalle varie exit con diverse funzioni e metodi, che, in questo caso, hanno il compito unicamente di "passacarte".


## Preparazione delle memorie

### Caso A No informazioni Aggiuntive S5IRIS
Se non ci sono informazioni da memorizzare contenute in S5IRIS, è conveniente richiamare X dalla exit S5SMX_11x a sua volta richiamata dall'inizializzatore generale S5SMES_06. Infatti a questo punto tutte le memorie standard sono state riempite e quindi ci sono tutti i dati a disposizione.

###  Caso B Informazioni aggiuntive in S5IRIS                                                   
Se invece ci sono informazioni contenute in S5IRIS, si deve richiamare X dalla exit S5SMX_02x a sua volta richiamata da S5SMES_01, di costruzione della DSIRIS, passandogli anche la DS di S5IRIS.
La exit S5SMX_02x, quando viene chiamata con funzione "INZ" deve chiamare X a sua volta con "INZ" per pulire la memoria; quando viene chiamata con funzione "  " deve chiamarlo con "WRI" e passando la DS di S5IRIS. A questo punto tutti i controlli sono stati superati (a meno che la exit S5SMX_02x l scarti rispondendo "NO" nel messaggio, nel qual caso, ovviamente, X non deve essere lanciato).
L'elemento di DSIRIS non è stato ancora scritto :  la sua posizione sarà £T01+1.
Se si devono eseguire azioni finali dipendenti solo dal S5IRIS, si richiama X dal S5SMX_02x quando è stato richiamato con funzione "FIN". Se invece si devono fare considerazioni che coinvolgono altre memorie, ci si riconduce (solo per la funzione "FIN") al caso precedente, di completamento dell'inizializzazione (S5SMX_11x).
Un esempio di costruzione mongolfiera di DSIRIS è presente nei sorgenti : 
XXESE_01 (programma di lancio, lanciato da vari punti)
XXESE_02 (programma di mongolfiera)
La divisione in due programmi è stata fatta per distinguere i compiti :  XXESE_02 è una pura mongolfiera, XXESE_01 (richiamato dalle varie exit) deve essere completato per utilizzare in modo appropriato le
 informazioni ritornate dall'altro programma.

## Considerazioni sul disegno delle memorie.

Se le memorie sono pure estensioni di quelle standard, è preferibile farle corrispondere nella stessa posizione :  ad esempio, l'estensione dell'elemento N di DSIRIS, occuperà la posizione N della DSXXXX. In prima posizione mettere comunque la posizione dell'occorrenza (per debug).
Se invece le memorie contengono informazioni che legano più DS, un modo di implementarle è il seguente :  in prima posizione mettere il numero di occorrenza  nelle altre posizioni, oltre alle informazioni specifiche, mettere le posizioni delle DS coinvolte,  per accedere a queste memorie si suggerisce di realizzare schiere di puntamento numeriche il cui contenuto è la posizione di questa memoria.
Ad esempio, se si realizza una DSYYYY che lega due impegni (uno di input e uno di output) si realizza una schiera (di tanti elementi pari a DSIRIS) in cui, nell'elemento N c'è il numero M corrispondenza all'occorrenza della DSYYYY che contiene il puntatore N.



# Esempi di utilizzo

Negli esempi seguenti, quando si imposta di lanciare una exit S5SMX_nnx, è implicito che essa deve, a sua volta, lanciare la mongolfiera con appropriate funzioni e metodi, come esposto in precedenza.


## Variazione dell'inizio e dei tempi di schedulazione in base a regole esterne

Ad esempio, se un impegno non può iniziare dopo una certa ora, all'interno del giorno, si può operare nel seguente modo.
La exit va lanciata in acquisizione nel completamento dell'inizializzazione, per leggere (una sola volta, presumibilmente da una tabella) e memorizzare le regole di spostamento.
Va inoltre lanciata la exit S5SMX_01x, di completamento della schedulazione di un dettaglio (S5SMES_13) per modificare gli estremi di schedulazione del dettaglio ricevuto, in base alle informazioni memorizzane nel lancio iniziale.


## Macchina preferenziale

Nel completamento dell'inizializzazione va lanciata la exit che memorizza il dettaglio preferenziale con la condizione di validità.
Si lancia la exit di spinta S5SMX_05x con funzione "DET" (eseguita dalla scelta dettaglio S5SMES_11E) per tornare il miglior dettaglio, in base alle regole impostate, all'istante di disponibilità di ogni risorsa, al vincolo al più presto.
Si suggerisce di memorizzare, per velocità, nella DS di estensione dell'impegno, in cui sono contenute le informazioni di macchina preferenziale e massimo ritardo ammesso, l'istante di partenza della macchina preferenziale originale e quello avanzato del massimo ritardo ammesso, in modo che quest'ultimo venga ricalcolato solo al variare del primo.


## Impegno sospeso

Si impostano le informazioni di sospensione nel completamento dell'inizializzazione.
Nella exit di sospensione impegno S5SMX_12x, lanciata nella scelta dettaglio S5SMES_11, si controlla se l'impegno è sospeso.
Nella exit di completamento schedulazione S5SMX_01X, di completamento della schedulazione di un dettaglio S5SMES_13, si aggiorna la memoria se il dettaglio che si sta schedulando rende liberi impegni precedentemente sospesi.
Va ricordato che lo sblocco di un impegno è indipendente dal suo stato di pronto :  i due eventi possono avvenire in entrambe le sequenze temporali :  per mettere in competizione l'impegno, devono essere verificati entrambi.




