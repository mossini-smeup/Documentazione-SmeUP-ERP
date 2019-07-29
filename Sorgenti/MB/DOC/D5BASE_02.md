## Concetti generali
 I programmi di ripresa da sistemi conferenti sono dei programmi tendenzialmente semplici il cui
 unico scopo è di chiamare la /COPY **£D5A** passandogli come parametri i seguenti dati : 
 - 10 tipi/parametri/oggetti che dipendono dal sistema conferente (per esempio la ripresa da
   documenti scriverà il numero documento, il codice cliente, il codice oggetto della riga, la
   commessa, etc. cioè la maggior parte degli oggetti presenti in un record di riga documento)
 - 10 valori che dipendono dal sistema conferente (nei documenti valori quali l'imponibile,
   l'imposta, il peso, il prezzo netto, etc.)
 - Una quantità
 - Che passi di ripresa (sottosettore ed elemento della **D5R**) eseguire con i parametri passati
 senza sapere che cosa e come si andrà a scrivere nel D5COSO0F.
 Il **concetto base** è quindi che il programma di ripresa deve semplicemente filtrare dei dati
 di un archivio e, per ogni record, riempire i parametri sopra specificati con tutti gli oggetti
 e valori che hanno un significato per quell'archivio, senza considerare se saranno o meno
 utilizzati nella scrittura del D5COSO0F.
 Un esempio di programma di ripresa generico è il D5APXX.
 Per determinare l'elemento della D5R da passare alla £D5A, nel caso in cui questo non sia stato
 specificato esplicitamente dall'utente nei parametri di lancio, ogni programma di ripresa
 usa delle logiche diverse, cioè controlla nella tabella D5R se esistono degli elementi
 codificati in un certo modo : 
 Esempi
 - Ripresa documenti
   1. modello documento + tipo riga
   2. tipo riga
   3. modello documento
   4. tipo documento
- Ripresa movimenti di magazzino
   1. causale del movimento di magazzino
   2. tipo movimento
 - Ripresa contabilità generale
   1. primi 12 caratteri del conto
   2. primi 06 caratteri del conto
   3. primi 04 caratteri del conto
   4. primi 02 caratteri del conto
 In questo modo è possibile ottenere comportamenti diversi a seconda dell'oggetto elaborato : 
 - escludere alcuni oggetti (basta mettere un elemento della D5R che non punta ad alcun elemento
   della D5E)
 - avere logiche di distribuzione del valore diverse (per esempio un conto contabile che
   utilizza un indice di distribuzione particolare diverso dagli altri)
 - scrivere contesti e temi diversi

## Lancio dei passi di ripresa
 Per eseguire dei flussi di ripresa dati da un sistema conferente occorre entrare nel menù
 del D5 "Elaborazioni per periodo" ed eseguire **"Esecuzione flusso azioni"**.
 Viene richiesto il periodo di lancio e il gruppo azioni che si desidera considerare.
 Il gruppo azioni è un elemento della tabella B£H (vedi help relativo per ulteriori informazioni)
 che permette di visualizzare le azioni appartenenti a quel gruppo.
 Le singole azioni sono elementi della tabella B£J.
 Una volta specificati il periodo ed il gruppo azioni verranno visualizzate le azioni che
 è possibile eseguire.
 Per eseguire un azione basta mettere una 'X' nel campo opzione e premere F06 o F11.
 E' possibile scegliere più azioni contemporaneamente e queste verranno elaborate sequenzialmente.
 Inserendo una P nel campo opzioni si accede alla finestra dei parametri di lancio dell'azione
 nella quale si può caratterizzare il passo di ripresa.
 Inserendo un 1/2/4/5 nel campo opzioni si possono inserire/modificare/cancellare/visualizzare
 i singoli passi di ripresa.
 Se si inserisce un '1' nel primo campo degli Indicatori esterni dell'elemento della B£J il
 programma di ripresa stamperà un log dei record elaborati e la £D5A un log dei passi eseguiti.
 Se si inserisce un '1' nel secondo campo degli Indicatori esterni viene attivata la modalità
 Set and play con visualizzazione a video dei risultati dei passi di ripresa.

## Parametri di lancio
 I parametri di lancio contestuali al programma di ripresa (parametri che
 permettono per esempio di filtrare i dati del proprio archivio e/o di specificare alcune modalità
 di calcolo) sono contenuti in schiere in formato £G30 nei programmi D5_G30 per quanto riguarda
 le riprese standard e nel D5_G30PER per quelle utente.
 Il periodo di lancio viene sempre passato in LDA nella posizione 1-10, le date di inizio
 e fine periodo in posizione 211-218 e 219-226.
 I parametri specifici del programma se passati in LDA sono presenti dalla posizione 151-190
 mentre se sono stati salvati nella MDV occorre reperirli eseguendo una chiamata alla £G70
 e vengono riportati nella DS £G07PA della /COPY.

### Logiche consigliate
 Per mantenere uniformità nei programmi di ripresa e completezza di funzionalità si consiglia
 di aggiungere ai parametri di lancio i seguenti campi : 
 - Sottosettore della tabella D5R
 - Elemento della D5R
 - Elemento della D5Z (per il suo significato leggere le FAQ)
 - Suffisso programma aggiustamento
 Inoltre conviene scrivere un help nel sorgente del programma (mettere H prima del carattere
 del tipo specifica) che illustri quali oggetti e quali valori vengono riportati dal programma
 (nel caso dei valori occorre specificare anche in quale dei 10 valori vengono scritti) e che
 logiche, se presenti, vengono utilizzate per la determinazione dell'elemento della D5R.


## Logiche di ripresa
 I passi di ripresa vengono elaborati dalla /COPY £D5A che riceve in ingresso la DS del file
 D5MOVI0F che contiene 10 oggetti, 1 qta, 10 valori e il sottosettore ed elemento della tabella
 D5R. Oltre a quest'ultimo vengono anche elaborati tutti gli elementi codificati con xxxxxx.n
 dove xxxxxx è l'elemento scelto dal programma di ripresa e n è un progressivo (ex. BOF.1, BOF.2).
 Nella tabella D5R (vedi help per maggiori delucidazioni) è scritto il sottosettore della
 tabella D5E e il prefisso degli elementi della D5E da eseguire (ex. AAA01 esegue tutti gli
 elementi che iniziano per AAA01).N.B. NON BISOGNA METTERE L'* DOPO IL PREFISSO.
 Nei singoli passi di ripresa (elementi della D5E) è scritto : 
 - il contesto (tabella D5S) che si vuole scrivere
 - il tema (tabella D5O) che si vuole scrivere
 - quale valore riportato dal programma di ripresa si vuole scrivere (ogni passo scrive un solo
   valore alla volta), quindi se la quantità o quale dei 10 valori
 - che logiche utilizzare per capire in quale dei 99 valori del D5COSO0F si vuole scrivere il
   valore precedentemente scelto (per le varie possibilità leggere l'help della tabella D5E).
   E' possibile per esempio derivare l'indice della IGI da scrivere da un OAV di un oggetto
   passato dal sistema conferente o addirittura da un parametro di un oggetto restituito da un OAV
   di un oggetto passato dal sistema conferente (per esempio si supponga di avere un parametro
   legato al dipendente (oggetto DI) che specifichi la sua tipologia (diretto, indiretto, part-time,
   etc.). Si può creare un parametro legato alla tipologia che contenga l'indice da andare ad
   aggiornare (ogni tipologia scrive in un valore diverso) e fare in modo che automaticamente
   se il programma di ripresa passa un oggetto DI, la £D5A legga la sua categoria e dalla categoria
   legga il suo indice associato).
 - se scrivere o meno il file di dettaglio D5RECO0F
 Dato che vengono elaborati tutti gli elementi con un dato prefisso è possibile scrivere
 con una sola ripresa più contesti e temi diversi, ognuno con logiche separate.

### Determinazione degli oggetti
 Avendo trovato il contesto e il tema che si vogliono scrivere (derivandoli dalla D5E) la £D5A
 conosce quali sono gli oggetti che gli servono per completare il record di D5COSO0F.
 Per ogni oggetto che gli serve controlla se nella tabella **D5M**, stesso sottosettore
 della D5E che si sta elaborando, è presente un elemento codificato come xxxxxx_ttpppppppppp dove
   - xxxxxx è il codice dell'elemento della D5E che sta elaborando
   - tt è il tipo oggetto che sta cercando
   - pppppppppp è il parametro dell'oggetto che sta cercando
 Per esempio se il passo di ripresa BOF010 scrive il contesto CC, la £D5A capisce che deve trovare
 un oggetto di tipo CC e cerca se esiste nella D5M un elemento codificato come BOF010_CC.
 Nel caso in cui non esista un tale elemento nella D5M, la £D5A cerca nei 10 oggetti passati
 dal programma di ripresa se esiste un oggetto di tipo CC. Se lo trova utilizza quell'oggetto
 per scrivere la chiave del D5COSO0F, altrimenti, per quel record, non scrive niente.
 Se invece viene trovato l'elemento nella D5M,  per derivare l'oggetto viene utilizzato l'algoritmo
 di ricerca specificato nell'elemento stesso della D5M (leggere l'help della tabella D5M per
 la lista degli algoritmi possibili).
 Tramite questi algoritmi è possibile : 
 - derivare nuovi oggetti, cioè oggetti non passati dal sistema conferente, da OAV e parametri
   applicati agli oggetti passati (per esempio derivare la classe materiale da un codice articolo).
 - distribuire un valore su più oggetti con percentuali di assegnazione
 - utilizzare indici e logiche di ricerca utente
 Questo tipo di ricerca/derivazione di oggetti viene effettuata per ogni oggetto necessario
 alla scrittura del D5COSO0F, cioè per l'oggetto del contesto e per gli eventuali altri 3 oggetti
 specificati nel tema.
 Se nel tema è stato specificato il periodo/data, viene scritto quello passato
 dal programma di ripresa che tipicamente è quello che l'utente ha impostato nell'esecuzione
 flusso azioni.

### Indici di distribuzione
 Per distribuire un valore su più oggetti si deve utilizzare la tabella D5M e la tabella **D5I**
 degli indici di distribuzione (vedi help delle 2 tabelle per il loro utilizzo).
 Per esempio è possibile distribuire il valore di una registazione contabile su più centri di costo
 con suddivisione percentuale del valore basandosi su un indice legato al conto contabile della
 registrazione.
