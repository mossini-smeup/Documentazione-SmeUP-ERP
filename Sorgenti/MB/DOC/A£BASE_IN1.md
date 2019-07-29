# Introduzione
I nastri magnetici/DVD-Rom di installazione di Sme.up vengono forniti con supporto di installazione mediante programma eseguibile direttamente da NASTRO/DVD-Rom.
I DVD-Rom contengono le librerie di Sme.up memorizzate in formato *SAVF, e possono essere caricate sul sistema di destinazione direttamente dal lettore DVD dell'AS/400, senza dover trasferire i dati tramite un personal computer.

## Nota sui supporti DVD-Rom
Il rilascio completo di Sme.up supera i limiti di capacità di un DVD single-layer. Di conseguenza tale rilascio si compone di due DVD (Base e Aggiornamento).
Il DVD 'Aggiornamento' contiene tutte le librerie aggiornate giornalmente, mentre il DVD 'Base' contiene le librerie che restano costanti nel periodo di distribuzione di un rilascio.

# Installazione guidata
## Caricamento programma di installazione
Procedere secondo i passi seguenti : 
 - inserire il supporto DVD-Rom 'Base' nel lettore DVD dell'AS/400, oppure, nel caso si sia in possesso del nastro magnetico, inserire quest'ultimo nell'unità nastro dell'AS/400;
 - collegarsi con utente QSECOFR o utente alternativo con autorizzazioni speciali *SECADM;
 - dalla linea comandi immettere il comando >LODRUN DEV(*OPT) se si è in possesso di un supporto DVD-Rom, oppure >LODRUN DEV(*TAP) se si è in possesso di un supporto NASTRO magnetico oppure >LODRUN DEV(xxxxx) dove xxxxx è il nome dell'unità di lettura;

A questo punto viene caricato automaticamente il programma di installazione, fase durante la quale viene visualizzato un messaggio di avvertimento del lavoro in corso.
A caricamento ultimato, il programma di installazione viene eseguito automaticamente e viene visualizzata la videata mostrata in Figura.

![A£BASE_01](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_01.png)
_Nota Bene : _ Nel caso l'installazione venga fatta da supporto magnetico, non compariranno le indicazioni 'DVD BASE' e 'DVD AGGIORNAMENTO', in quanto tutte le librerie (a differenza di quanto accade per i DVD-Rom) risiedono su un unico supporto.

## Step 1 - Caricamento librerie
Procedere seguendo i passi seguenti : 
 * Selezionare con 'X' l'opzione 'Impostazione sigla installazione', mediante la quale verrà visualizzata la videata mostrata in Figura.

![A£BASE_02](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_02.png)
 * Impostare correttamente la sigla dell'azienda e confermare con F06
>N.B. :  Prima di proseguire con il caricamento delle librerie, si consiglia di verificare lo stato di occupazione dei dischi del server I-series (comando >WRKSYSSTS). Si consideri che l'intera procedura di installazione può richiedere fino a 10 Gbyte.

 * Selezionare con 'X' l'opzione 'Sottomissione ripristino librerie base', mediante la quale verrà visualizzata la videata mostrata in Figura.

![A£BASE_03](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_03.png)
 * Impostare correttamente i nomi libreria nella colonna 'Ripristinare come', impostare l'eventuale IASP in cui effettuare il ripristino, quindi lanciare il lavoro di ripristino, mediante il tasto funzionale di conferma F06. Verrà richiesta la conferma di sottomissione di un lavoro batch per ogni libreria indicata, con la possibilità di specificare una coda lavori specifica (in assenza viene assunta QBATCH)
>N.B. :  Nel caso l'installazione venga fatta da supporto magnetico, non comparirà l'indicazione 'Attenzione utilizzare DVD BASE'.

 * Attendere il completamento dei lavori sottomessi e verificare il buon esito del caricamento, mediante la stampa generata dall'esecuzione del ripristino
 * Nel caso l'installazione venga fatta da DVD-Rom è necessario sostituire il DVD Base con il DVD Aggiornamento.
 * Selezionare con 'X' l'opzione 'Sottomissione ripristino librerie aggiornamento', mediante la quale verrà visualizzata la videata mostrata in Figura.

![A£BASE_04](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_04.png) * Impostare correttamente i nomi libreria nella colonna 'Ripristinare come', impostare l'eventuale IASP in cui effettuare il ripristino, quindi lanciare il lavoro di ripristino, mediante il tasto di conferma F06. Verrà richiesta la conferma di sottomissione di un lavoro batch per ogni libreria indicata, con la possibilità di indicare una coda lavori specifica (in assenza, verrà assunta QBATCH)
>N.B. :  Nel caso l'installazione venga fatta da supporto magnetico, non comparirà l'indicazione 'Attenzione utilizzare DVD AGGIORNAMENTO'

 * Attendere il completamento dei lavori sottomessi e verificare il buon esito del caricamento mediante la stampa generata dall'esecuzione del ripristino
In caso si stia effettuando una prima installazione Sme.UP (e non un upgrade) allora sarà necessario restore alcune librerie aggiuntive (libreria dati di partenza ecc.)
 * Selezionare in questo caso con 'X' l'opzione 'Sottomissione ripristino librerie 1° Installaz.', mediante la quale verrà visualizzata la videata mostrata in Figura.
![A£BASE_08](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_08.png) * Impostare correttamente i nomi libreria nella colonna 'Ripristinare come', impostare l'eventuale IASP in cui effettuare il ripristino, quindi lanciare il lavoro di ripristino, mediante il tasto di conferma F06. Verrà richiesta la conferma di sottomissione di un lavoro batch per ogni libreria indicata, con la possibilità di indicare una coda lavori specifica (in assenza, verrà assunta QBATCH)
>N.B. :  Nel caso l'installazione venga fatta da supporto magnetico, non comparirà l'indicazione 'Attenzione utilizzare DVD AGGIORNAMENTO'

## Step 2 - Definizione ambiente
Procedere seguendo i passi seguenti : 
 * Selezionare con 'X' l'opzione 'Valori di sistema', mediante la quale verrà visualizzata la videata mostrata.
![A£BASE_05](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_05.png)
Mediante il tasto funzione F06 è possibile accedere alla gestione "normale" dei valori di sistema.
Mediante il tasto funzione f07 è possibile accedere ad una gestione "particolare" dei valori di sistema. Questa modalità è da usare solo incasi specifici.
Mediante le istruzioni che appariranno nelle videate, aggiungere la libreria SMESYS (o l'alias definito al caricamento) all'elenco proposto
 * Premere F12 per tornare al menù iniziale e selezionare l'opzione 'Creazione JOBD e Completamento Ambiente SME.up'.
![A£BASE_06](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_06.png)
 * Inserire il nome della libreria in cui creare la JOBD (si consiglia di utilizzare la libreria di sistema precedentemente creata).
 * Confermare con il tasto funzionale F06, mediante il quale verrà visualizzata la seguente videata.
![A£BASE_09](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_09.png)
 * Impostare correttamente la lista di librerie da abbinare alla descrizione lavoro, l'eventuale IASP da associare alla JOBD, quindi premere F06 per confermare.

 * Selezionare l'opzione 'Creazione profilo utente di servizio', mediante la quale apparirà la videata.
![A£BASE_07](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_07.png)
 * Impostare il nome dell'utente amministratore di Sme.up, utilizzando il nome proposto (consigliato) o indicandone uno diverso. Indicare nel parametro pportuno la JOBD precedenteemnte creata.
L'utente creato sarà "amministratore" per quanto riguarda Sme.UP, ma "sistemisticamente" sarà di classe *PGMR.

## Step 2 - Fasi finali
Selezionare con 'X' l'opzione 'Completamento Installazione' mediante la quale verrà visualizzata la seguente videata.
![A£BASE_10](http://localhost:3000/immagini/A£BASE_IN1/AXBASE_10.png)Questo è solo un promemoria, per ricordare di ricollegarsi con l'utente appena creato e di eseguire il comando UP INS per eseguire le ultime operazioni di configurazione.

# Consigli per l'installazione di Sme.UP su sistemi iaspizzati
- [IASP e Sme.UP](Sorgenti/MB/DOC/A£BASE_IA1)
