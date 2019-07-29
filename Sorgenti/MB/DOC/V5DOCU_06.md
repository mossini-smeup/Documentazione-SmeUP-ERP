# Emissione fatture d'acconto

## Prerequisiti
Per la gestione degli acconti è necessario avere una release a partire dalla V4R1, nella quale tutti i programmi e le tabelle sono standard, altrimenti è necessario qualora si parli di versioni precedenti, scaricarsi il savf con l'intero pacchetto di aggiornamenti necessari.

## Impostazioni per l'installazione
Di seguito vedremo tutte le impostazioni necessarie per gestire gli acconti in SmeUp.

### Documenti coinvolti
- Ordini di vendita
- Fattura di acconto
- Bolla consegna merce
- Fattura saldo

### Tabelle interessate
**Tabella V5B OA/DA**
 :  : DEC T(ST) K(V5BOA) I(Gestione Tabella)
 :  : DEC T(ST) K(V5BDA) I(Gestione Tabella)

**Tabella V5A OA/DA**
 :  : DEC T(ST) K(V5AOA) I(Gestione Tabella)
 :  : DEC T(ST) K(V5ADA) I(Gestione Tabella)

Tabella V5G CA
 :  : DEC T(ST) K(V5G) I(Gestione Tabella)

Tabella B£H
 :  : DEC T(ST) K(B£H) I(Gestione Tabella)

Tabella B£J
 :  : DEC T(ST) K(B£JCA) I(Gestione Tabella)
 :  : DEC T(ST) K(B£JDR) I(Gestione Tabella)

Tabella B£Y
 :  : DEC T(ST) K(B£Y) I(Gestione Tabella)

Tabella COA SP
 :  : DEC T(ST) K(COASP) I(Gestione Tabella)

Tabella V5S
 :  : DEC T(ST) K(V5S) I(Gestione Tabella)

Tabella PAG
 :  : DEC T(ST) K(PAG) I(Gestione Tabella)

Tabella V5H
E' stata creata la tabella V5H con l'intenzione di slegare dal programma qualsiasi impostazione sugli anticipi riferita al tipo e codice documento.
 :  : DEC T(ST) K(V5H) I(Gestione Tabella)

Tabella V59
E' stata creata appositamente questa tabella per gestire i parametri di configurazione degli anticipi.
 :  : DEC T(ST) K(V59) I(Parametri Anticipi)

### Programma V5FUANT

È stato creato il programma V5FUANT per gestire tutti quegli automatismi adibiti alla gestione delle fatture di anticipo.

Il programma ha le seguenti ROUTINE : 
1) **INSREA** :  richiamato il programma nel flusso di creazione della riga di anticipo, questa routine permette di aggiungere automaticamente la riga di storno documento nello stesso ordine di vendita.
2) **MODACC** :  richiamando la MODACC nel flusso di modifica delle righe, in caso di modifica di una riga d'anticipo permette di modificare allo stesso modo la riga automatica di storno creata precedentemente dallo stesso programma.
3) **CANACC** :  il programma deve essere aggiunto al flusso di cancellazione della riga, se questa è una riga di anticipo, allora la routine procede contestualmente alla cancellazione della riga di storno anticipo automatica.
4) **CALIMP** :  questa routine effettua il calcolo dell'importo da estrarre, ed è per questo che il programma deve essere aggiunto al flusso di transazione nella testata dell'ordine di vendita.
5) **IMPPAG** :  infine questa procedura riguarda il calcolo dell'importo dell'acconto da inserire automaticamente nei casi in cui l'inserimento non avvenga manualmente ma a seguito dell'impostazione di alcuni campi nelle condizioni di pagamento (tabella PAG).  Deve ovviamente essere inserito il V5FUANT con questo parametro nei flussi di transazione della testata ordine, in modo che alla conclusione dell'inserimento di testata e righe venga lanciata la creazione delle 2 righe di acconto e di storno.

## Procedura utilizzo gestione acconti
Dobbiamo fare una premessa, prima di entrare nel dettaglio della procedura possiamo avere 2 casistiche che coinvolgono le fatture d'acconto, una riguarda le fatture di acconto derivate da un ordine di vendita, l'altra invece riguarda quelle fatture che sono svincolate da un documento di vendita di partenza (ad esempio una fattura di acconto generica su un insieme di forniture).

**CASO I° - Fatture di anticipo relative ad un ordine**
Questa casistica risulta essere più frequente e prevede l'inserimento manuale della riga di anticipo nell'ordine.
L'utente procede ad aggiungere alle righe dell'ordine di vendita una riga con l'importo dell'anticipo.

La cosa importante ovviamente è aver codificato nella tabella V5B OA (relativi ai tipi riga degli ordini attivi) 2 tipologie di riga : 
- quella relativa all'acconto (es. 004)
- quella relativa allo storno dell'anticipo (005)
![V5_013](http://localhost:3000/immagini/V5DOCU_06/V5_013.png)
La prima riga relativa all'acconto viene inserita dall'utente, e grazie all'automatismo previsto dal programma V5FUANT, se correttamente richiamato nei flussi di inserimento (tabelle B£H e B£J) della riga stessa, viene creata una seconda riga di storno.
![V5_014](http://localhost:3000/immagini/V5DOCU_06/V5_014.png)Affinchè ciò avvenga però, deve essere inserito nella nuova tabella V5H creata appositamente per la gestione degli anticipi, un nuovo elemento con lo stesso codice della riga di anticipo manuale.
In questo elemento deve essere definita la tipologia di riga da utilizzare per lo storno dell'anticipo (il codice riga è assolutamente libero, non vi è nulla di forzato nel programma).
![V5_024](http://localhost:3000/immagini/V5DOCU_06/V5_024.png)
Quindi contestualmente all'aggiunta del tipo di riga dell'ordine è necessario creare nella tabella V5H questo elemento che contenga tutte le informazioni necessarie al V5FUANT per automatizzare i processi.

![V5_015](http://localhost:3000/immagini/V5DOCU_06/V5_015.png)Devono essere definiti : 
- il sottosettore della V5B e l'elemento che il programma deve usare per creare la riga.
- il "Codice oggetto Rec. Or." conterrà l'elemento della V5S che verrà utilizzato come oggetto della riga di recupero.
- qualora si vogliano adottare dei comportamenti particolari esiste la possibilità di indicare il suffisso del programma di aggiustamento V5FUANT_X.
- l'unità di misura che sarà utilizzata sulle righe di recupero acconto sia dell'ordine che della bolla deve esistere sulla tabella UMS.

Quindi in sostanza se nella tabella V5H esiste lo stesso tipo riga di quello appena inserito manualmente dall'utente nell'ordine, allora il pgm andrà a leggerne i campi per poter automaticamente creare la riga di storno nell'ordine.
Successivamente questa tabella sarà utilizzata anche necessari ai flussi per gestire i DDT.

Nella tabella V5S  devono essere creati 2 nuovi tipi di spese : 
- ANT per l'anticipo
- RAN per lo storno dell'anticipo.

Il prossimo passo è inserire i flussi nelle apposite tabelle (B£H) : 
1. In inserimento righe ordini
2. In modifica delle righe d'ordine
3. In pre-cancellazione righe d'ordine
4. In transazione sulle righe dell'ordine e sulle righe della bolla
![V5_016](http://localhost:3000/immagini/V5DOCU_06/V5_016.png)
La B£J invece : 
![V5_025](http://localhost:3000/immagini/V5DOCU_06/V5_025.png)
Il programma se agganciato quindi nei flussi di riga, qualora individui una riga presente come elemento nella V5H, provvederà a generare in automatico la relativa riga di recupero/storno dell'anticipo.
Queste righe saranno legate fra di loro, in quanto sulla riga automatica di storno anticipo nel campo R§NRRI (Riga master di riferimento) verrà indicata la riga origine dell'anticipo.
La particolarità della riga di storno sta nel gruppo flag riga, il qual'è avrà nel FLAG07 il valore "1", indicando così l'inversione, l'importo risulterà positivo ma verrà stornato dall'imponibile totale.

Qualora si decidesse di modificare la riga di anticipo, la routine di modifica permetterà di aggiornare coerentemente la riga automatica di storno con le modifiche appena effettuate sulla riga manuale di anticipo. Questo perché ovviamente la riga automatica non sarà manutenibile dall'utente.
Allo stesso tempo se dovessi eliminare la riga di anticipo, agganciando il programma al flusso di pre-cancellazione, la routine CANACC permetterà di eliminare automaticamente anche la riga automatica di storno.

Passiamo ora allo step successivo, una volta inserito l'ordine con le relative righe acconto e recupero dell'acconto, mi devo occupare della fatturazione dell'acconto stesso.
Per fatturare l'acconto però è necessario estrarre un documento  di tipo fattura con i flag impostati correttamente, gli importi presi dalla riga dell'ordine ecc.

A tal proposito è possibile, è un opzione facoltativa, di creare un tipo documento nella V5ADA apposito per la fattura d'acconto : 
![V5_017](http://localhost:3000/immagini/V5DOCU_06/V5_017.png)
Procediamo poi, alla creazione di un tipo riga apposito di modo che nella V5AOA della riga 004 di anticipo potrò indicare la riga di destinazione appena creata (in questo modo il pgm di estrazione prenderà solo le righe specifiche).
Il passo successivo sarà creare nella tabella V5G CA (per i flussi del ciclo attivo), un flusso di estrazione e stampa degli anticipi e aggiungerlo al menu.
![V5_026](http://localhost:3000/immagini/V5DOCU_06/V5_026.png)
Quando sarà spedita la merce al cliente, la routine CALIMP, richiamata come flusso di transazione delle bolle, calcola l'importo di recupero dell'acconto.
Quindi quando si procederà all'estrazione della bolla a partire dall'ordine, dopo aver compilato testata e selezionato le righe in uscita dal documento, A CONDIZIONE CHE LA RIGA DI ANTICIPO origine sull'ordine sia CHIUSA/FATTURATA (ovvero che abbia un livello = 8) si attiverà il pgm inserito nel flusso di transizione che calcolerà l'imponibile (se l'imponibile è 0 non farà nulla) leggerà tutte le righe dell'ordine. Per ogni riga della bolla che ha documento origine (ogni riga della bolla potrebbe aver origine da ordini di vendita diversi) verificherà che la tipologia delle righe sia presente sulla tabella V5H (quindi sia una riga di acconto) e che abbia livello 8.
A questo punto leggerà la riga di recupero acconto (grazie ai parametri impostati nella V5H), verificherà che sia o meno recuperabile (deve essere di LIV=2 aperto).
Grazie agli OAV troverà la quantità delle riga di recupero e il valore iniziale, leggerà la quantità residua e il valore residuo.
![V5_027](http://localhost:3000/immagini/V5DOCU_06/V5_027.png)
La quantità residua verrà scritta dopo la decurtazione dell'anticipo dalla bolla, e sarà calcolata in % a partire dalla quantità iniziale pari a 1, quindi per esempio se preleverò il 60% rimarrà un quantità pari a 0,40.
![V5_018](http://localhost:3000/immagini/V5DOCU_06/V5_018.png)
Dopo le varie considerazione viene creata la riga di recupero acconto sulla bolla. Questo grazie alla lettura della V5H nella quale è stato indicato il tipo riga e il sottosettore della V5B.
Nella tabella V5H come già anticipato deve essere compilata la spesa (tabella V5S) che voglio utilizzare per il recupero dell'anticipo.
Quando viene scritta la riga di recupero dell'anticipo sulla bolla, questa riga tramite i campi R§TDOR, R§NDOR, R§NRIR viene collegata alla riga di recupero sull'ordine di vendita.



**CASO II° - Fatture di anticipo su future forniture**
Il secondo caso riguarda tutti quegli anticipi che non sono legati a nessun ordine specifico ma che vengono incassati preventivamente a nome delle successive forniture.
A tal proposito infatti, abbiamo la tabella V59, creata appositamente per permettere al programma di reperire i dati necessari per individuare questi anticipi generici sul cliente.
Nella tabella V59 abbiamo i seguenti campi : 

![V5_019](http://localhost:3000/immagini/V5DOCU_06/V5_019.png)Tipo doc. Solo Ant. - Contiene il tipo documento da utilizzare per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione.
SS Modello Solo Ant.  - Contiene il sottosettore del modello per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione.
Modello solo Ant. - Contiene il modello per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione a cliente.

In questo caso infatti andremo ad indicare il tipo e il modello del documento "ordine" che sostanzialmente conterrà il solo anticipo e il suo storno.
Questo comporterà quindi l'inserimento di un nuovo tipo documento ordine che avrà importo a zero. Il tipo riga dovrà essere un elemento della V5S, perchè l'ordine non conterrà articoli bensì solo spese.

In fase di evasione ordine il programma controllerà se è stato indicato un modello documento nella tabella V59, se esiste allora recupera gli acconti per quel soggetto.

Azioni eseguite in fase di creazione bolla : 
- il primo controllo che verrà fatto è ovviamente legato agli acconti sull'ordine che sta generando questa bolla (quindi acconti del 1° tipo)
- successivamente controllerà se per quel cliente esiste un documento (ordine acconto del 2° tipo) aperto intestato a quel soggetto, come da indicazione della V59.
In sequenza sulla bolla appena generata stornerà prima uno e poi l'altro, se esiste ancora un residuo.

![V5_020](http://localhost:3000/immagini/V5DOCU_06/V5_020.png)

### Anticipi creati tramite codici pagamento - IN SVILUPPO
Sarà predisposto un automatismo che permetterà la creazione delle riga di anticipo completamente in modo automatico tramite la tabella PAG.
![V5_021](http://localhost:3000/immagini/V5DOCU_06/V5_021.png)A differenza del primo metodo che prevedeva un inserimento manuale della riga d'anticipo sull'ordine, per questa tipologia di acconto il tutto viene pilotato dalla tabella PAG nella quale vado a definire la % di anticipo per quel pagamento. Quindi la riga verrà riempita in base al valore del documento calcolando la %.

Sono stati aggiunti 3 campi sulla tabella : 
-  % anticipo :  ovviamente in questo caso posso gestire un unico anticipo precedente alla consegna.

Come verrà attivato questo automatismo?
Inserendo nel flusso di transazione in testata all'ordine, il programma V5FUANT che, grazie alle impostazioni contenute nella PAG, inserirà le 2 righe (quella di anticpo e quella di storno).
Il programma trovando il campo della PAG valorizzato, cercherà sulla tabella V5H i parametri di creazione delle righe (la % e il tipo riga) per poter creare le righe sull'ordine.

Prende gli imponibili totali, calcola la % e mette una quantità fissa.


### Gestione scenari
E' stata aggiunto nella tabella V59 un campo che permette la gestione degli scenari.
Se attivo questo flag la spedizione recupererà solo gli acconti a parità di scenario altrimenti se non valorizzato verrano recuperati tutti gli acconti inseriti indipendentemente dallo scenario.
Il programma recupera gli anticipi legati allo scenario da cui sto partendo.

![V5_022](http://localhost:3000/immagini/V5DOCU_06/V5_022.png)

### Exit
**ATTENZIONE : ** l'unico accorgimento che segnaliamo è quello di predisporre una semplicissima EXIT da agganciare al flusso standard di bolla, per evitare che in fase di estrazione bolla si vedano anche le righe di recupero dell'acconto.
![V5_023](http://localhost:3000/immagini/V5DOCU_06/V5_023.png)
### Prototipo
Sulla tabella V5H ho un pgm di controllo di cui è stato fatto il prototipo V5FUANT_X.
V5FUANT_X   Esempio Pgm aggiustamento funzioni Anticipi   [SMESRC/V5SRC].
