## INTRODUZIONE
La tracciabilità lotti è la fuzione che, partendo dai movimenti di magazzino (con i loro campi di articolo, lotto e numeri ordini/documenti) permette di rispondere alle seguenti domande : 
 * _2_Dato un lotto (o altre informazioni che permettono di risalire ad esso)
 ** _3_quali lotti di articoli componenti sono entrati nella sua realizzazione
 ** _3_in quali lotti di articoli assiemi è entrato a far parte

## ESEMPIO DI UTILIZZO
Un utilizzo possibile è il seguente : 
 * Un cliente rende un articolo difettoso (facendo riferimento al numero di DDT o al lotto)
 * Si esegue un'analisi tecnica per risalire al componente che ha provocato il difetto
 * Si trova (con la funzione a) il lotto di questo componente
 * Si trovano (con la funzione b) tutti i lotti in cui è entrato questo lotto. Essi possono essere
 ** Ancora giacenti in azienda. In questo caso ne viene presentata la rimanenza.
 ** Già spediti. In questo caso vengono presentati i movimenti di spedizione con gli estremi del Cliente, della DDT, ecc...

## PREREQUISITI
Sui movimenti devono essere presenti il lotto, e l'ordine/documento a cui appartiene (informazione che viene riportata automaticamente nei prelievi e versamenti pianificati).

Sulle causali di magazzino va inoltre impostato il campo 'natura movimento', che indica se esso è
 * un'entrata
 * un'uscita
 * un prelievo
 * un versamento
 * un trasferimento
Nel motore di tracciabilità questa informazione viene utilizzata leggendo il valore di tabella, non è infatti riportata nei movimenti di magazzino.

Con riferimento alla rimanenza, precisiamo invece che per la tracciabilità non è necessaria (anche se molto consigliata) la tenuta della giacenza per lotto, in quanto la tracciabilità non è una
funzione logistica ma consuntiva.
La rimanenza del lotto viene calcolata come bilancio tra entrate e uscite :  informa su quanto c'è in azienda.
La giacenza per lotto (eventualmente divisa per area, ubicazione, ente, ecc...) informa invece su dove risiede quanto c'è in azienda.

## MOTORE DI SCANSIONE
Si basa sulla /COPY £GNE che esegue la tracciabilità del lotto sia in salita sia in discesa.

Essa può venire richiamata sia in scansione, sia in visualizzazione. In questo secondo caso, essa è sensibile all'ambiente :  se chiamata in  modalità 5250 (interattivo) presenta una lista £G18, se in modailtà Loocup (batch) presenta una matrice.

## FUNZIONI REALIZZATE
 * _2_movimenti del livello
 * _2_salita (analitica :  tutti i movimenti)
 * _2_salita sintetica (vedi oltre per la spiegazione di questa modalità)
 * _2_discesa (analitica :  tutti i movimenti)
 * _2_discesa sintetica (vedi oltre per la spiegazione di questa modalità)

## OGGETTO DI PARTENZA
 * _2_un articolo, si parte da tutti i suoi movimenti con un lotto valorizzato
 * _2_un articolo e un lotto, si parte dai movimenti della coppia articolo/lotto
 * _2_un ordine di produzione o_2_ una riga di documento di ciclo esterno, si parte dai movimenti dell'articolo intestatario e si considerano tutti i movimenti con un lotto valorizzato che hanno : 
 ** nel caso di ordine di produzione, l'ordine selezionato nel campo N.Ordine 1 oppure N.Ordine 2
 ** nel caso di riga di documento, il documento selezionato (tipo, numero e riga) nel campo N.Ordine 1, N.Ordine 2 oppure N.documento interno.
 * _2_un oggetto (tipo e codice) verosimilmente il tipo è CL o FO
 * _2_un flag che specifica se si passa un lotto di fornitura o di derivazione
 * _2_il codice del lotto (di fornitura o di derivazione), si parte dai lotti individuati dalla tripletta tipo ogg/ogg/lotto e per ciascuno di essi si estraggono i movimenti.

L'analisi tracciabilità _2_ non chiede mai il plant, in quanto essa è trasversale su tutti plant nei quali il lotto transita.

## DESCRIZIONE PROCESSO
A questo punto è stato ottenuto l'innesco della tracciabilità, che è costituita da tutti i movimenti di una o più coppie di articolo/lotto. Nel caso del 'livello' non si deve fare altro :  si ritornano in sequenza i movimenti di innesco. Negli altri casi si deve eseguire una salita o una discesa. Dato che la salita e discesa sintetica sono ottenute da un'elaborazione sui risultati delle corrispondenti funzioni analitiche, iniziamo con l'esposizione di queste ultime.

### Salita
Si esamina ogni movimento :  se la natura della causale è 4 (prelievo) si cercano i movimenti corrispondenti di versamento, con il seguente  criterio, per stabilire l'aggancio

>.  Ordine 1      Ordine 2      Doc.Interno     Oggetto Aggancio
.  --------      ---------     -----------     ----------------
.  Presente      ...           ...             Ordine 1
.  ...           Presente      ...             CASO NON CONTEMPLATO IN SMEUP
.  ...           ...           Presente        Doc.Interno
.  Presente      Presente      ...             Ordine 2
.  Presente      ...           Presente        Ordine 1
.  ...           Presente      Presente        CASO NON CONTEMPLATO IN SMEUP
.  Presente      Presente      Presente        Ordine 2


Nella realizzazione di visualizzatori per l'inserimento manuale di movimenti, va mantenuta la congruenza con questa tabella.

### Analisi sintetica (discesa e salita)
Se la natura della causale è 3 (versamento) si analizzano i corrispondenti movimenti di prelievo, (con lo stesso criterio per stabilire l'aggancio).
In entrambi i casi, i movimenti trovati costituiscono l'oggetto di partenza per un'ulteriore scansione, in modo ricorsivo.
Le funzioni di salita e di discesa, per ogni movimento, selezionano i movimento individuati che presentano il lotto valorizzato.
Ricordo che la rintracciabilità è puramente qualitativa :  se in un ordine di produzione è stato prelevato più di un lotto dello stesso articolo, ed esso è a sua volta stato versato con più di un lotto, non si è in grado di stabilire in quale lotto di versamento entrano i lotti di prelievo :  in ciascuno di essi si assume che entrino tutti i lotti di prelievo. Questo fatto si amplifica risalendo nei livelli.

**ATTENZIONE :  quando si parla di entrata ed uscita si fa riferimento SEMPRE alla natura del movimento presente nella sua causale.

La _2_discesa sintetica presenta, dato un lotto di partenza
 * i movimenti di uscita del lotto di partenza
 * i movimenti degli altri lotti collegati al lotto di partenza (ottenuti come risultato dalla discesa analitica), posto che siano di entrata
 * la rimanenza in azienda del lotto di partenza (ottenuta come differenza tra entrate e uscita)

La _2_salita sintetica presenta, dato un lotto di partenza
 * i movimenti di entrata del lotto di partenza
 * i movimenti degli altri lotti collegati al lotto di partenza (ottenuti come risultato dalla discesa analitica), posto che siano di uscita
 * la rimanenza in azienda di ogni lotto, in modo da evidenziare ciò che, del lotto di partenza, è ancora in azienda (al suo livello, e ai livelli superiori).

In sostanza, le funzioni sintetiche considerano l'azienda (compresi i suoi terzisti) come una 'scatola nera', e ne riportano l'interazione con il mondo esterno.

Nella discesa e salita sintetica, i movimenti vengono riportati una sola volta, anche se appaiono in più rami della scansione (vale a dire nelle corrispondenti funzioni analitiche).

## LANCIO TRACCIABILITA'
E' presente inoltre il programma di lancio della navigazione tracciabilità (GMRN02G), inserito a menu, predisposto per eseguire la presentazione sia in ambito 5250, sia in ambito Loocup, in base all'ambiente di esecuzione. In modalità Loocup si presenta il bottone di lancio, che reperisce le informazioni all'ultimo Enter. Loocup infatti non comunica direttamente con il formato video ma con il programma, che conosce quanto digitato a video al momento  dell'Enter.

Da ogni elemento della lista della tracciabilità si può proseguire in navigazione : 
 * in ambiente 5250 scegliendo l'opzione di lista
 * in ambiente Loocup, dal menu popup dell'oggetto lotto, scegliendo l'opzione tracciabilità (questa modalità è quindi attiva in qualsiasi punto dell'applicazione viene riconosciuto l'oggetto lotto).
