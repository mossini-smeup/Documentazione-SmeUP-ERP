# Inventario fisico
## Generalità
La gestione dell'inventario ha lo scopo di allineare il magazzino Contabile (del Sistema Informatico) con quello Fisico.

I passi fondamentali sono : 
 - _2_preparare il sistema informatico, creare un codice inventario, decidere se eseguire le conte attraverso liste di conta (in questo caso si dovranno creare le lsite di conta, con uno dei vari metodi previsti), oppure attraverso cartellini inventariali (in questo caso si devono stabilire i lotti di conta da associare ai vari gruppi di cartellini ed eventualmente generare i cartellini da lista di conta);
 - _2_contare il magazzino fisico, eseguire fisicamente le conte e riportare sulle liste o sui cartellini le quantità contate;
 - _2_inserire la conta fisica nel sistema informatico se si sono utilizzate le liste di conta si tratta di inserire la qtà contata nella lista, se invece si sono utilizzati i cartellini si inseriscono i cartellini e poi si lancia un programma che totalizza, a parità di chiave giacenza, i cartellini nelle liste;
 - _2_eseguire le rettifiche inventariali, a seconda della modalità di inventario scelta si può lanciare un programma che riallinea le giacenze, le rattifiche previste possono essere valorizzate per valutare l'opportunità di una seconda conta, poi si lanciano i movimenti di aggiustamento inventariale.
## Formato iniziale

![GMINVE_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_02.png)
A supporto della gestione dell'inventario fisico l'applicazione fornisce : 

- funzioni generali
- funzioni di inventario
- funzioni di analisi


### Fuzioni Generali
È l'elenco delle funzioni di carattere generale applicabili a tutti gli inventari presenti : 

- Elenco inventari per data, presenta l'elenco in ordine di data dei codici inventario presenti nella tabella GMI.
- ..........


![GMINVE_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_03.png)
### Funzioni Inventario
Sono tutte le funzioni applicabili ad un dato inventario : 

![GMINVE_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_04.png)
_3_Funzioni Preparazione Inventario
Sono le funzioni che agiscono scrivendo o modificando le conte inventario : 

![GMINVE_05](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_05.png)
_1_Preparazione Inventario - Pulizia totale
Cancella tutte le righe relative all'inventario su cui si sta lavorando.

_1_Preparazione Inventario - Estrazione
Questa funzione si applica quando si vuole eseguire un inventario fisico partendo da una lista di conte inventariali, estraendo le conte da eseguire da una giacenza o da una selezione di articoli. Le conte inventario vengono costruite in base alla modalità di estrazione impostata nell'elemento della tabella GMI corrispondente all'inventario in gestione.
Se viene richiesta una delle estrazioni partendo dall'anagrafico articoli, il sistema propone una finestra di selezione delle giacenze secondo parametri di giacenza (tipologia e caratteristica aree, quantità in giacenza), date di esecuzione inventario e date di esecuzione movimenti.
Se viene richiesta una delle estrazioni partendo dalle giacenze, il sistema propone una finestra di selezione delle giacenze secondo parametri di quantità (se la giacenza è maggiore o minore o uguale ad un valore in input, numero massimo di conte da generare, ...)
L'opzione 6 permette di lanciare un programma specifico di estrazione con regole utente.

_1_Preparazione Inventario - Ripresa giacenza
Questa funzione si applica nel caso si voglia riallineare la giacenza teorica nell'archivio delle conte oppure quando l'archivio delle conte è stato generato per totalizzazione dei cartellini per inserire la giacenza teorica. La funzione aggiorna la quantità prevista nell'archivio righe inventario in base alla modalità di ripresa giacenze impostata nell'elemento della tabella GMI corrispondente all'inventario su cui si sta lavorando.

_3_Funzioni Cartellini di Conta
Sono le funzioni che agiscono sui cartellini di conta : 

![GMINVE_06](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_06.png)
_1_Funzioni Cartellini - Estrazione da liste inventario
Questa funzione genera un lotto di cartellini partendo dalle liste di conta. Il programma funziona come la stampa dei dati inventario, quindi permette di selezionare, utilizzando le parzializzazioni, all'interno dell'inventario le conte da trasformare in un lotto di cartellini di conta.
Possono essere creati quanti lotti si vuole, i lotti dei cartellini di conta devono essere inseriti nella tabella GML e devono essere congruenti con l'inventario in gestione.
Le conte inventario che generano lotti di cartellini vengono messe in stato 70 e restano bloccate fino alla totalizzazione dei cartellini che riporta sulle conte inventario la quantità effettivamente contata.
Le conte che hanno generato un lotto non possono generarne un secondo.

_1_Funzioni Cartellini - Gestione in Lista
Permette di gestire l'inserimento delle quantità contate direttamente nella lista dei cartellini di conta.
La gestione è basata sul lotto di conta, cioè sono presentati solo i cartellini appartenenti a quel determinato lotto di conta.
La presentazione dei cartellini può essere ordinata e parzializzata secondo esigenze utente, le modalità di ordinamento e parzializzazione possono essere memorizzate con un nome caratteristico e richiamate quando si apre la lista.
Dentro la lista dei cartellini il comando funzione F10 permette l'inserimento di un nuovo cartellino di conta con dati di giacenza e quantità contate.

_1_Funzioni Cartellini - Gestione per Lotto/Articolo
Questa funzione consente la gestione individuale dei cartellini, è possibile entrare in lista chiedendo l'ordinamento dei cartellini  per lotto o per articolo e passare da un ordinamento all'altro attraverso il comando funzione F15.
Dentro la lista dei cartellini il comando funzione F10 permette l'inserimento di un nuovo cartellino di conta con dati di giacenza e quantità contate.

_1_Funzioni Cartellini - Cancellazione
Permette di cancellare tutti i cartellini di un lotto di conta.

_1_Funzioni Cartellini - Stampa
Stampa i dati dei cartellini secondo uno schema informazioni, un ordinamento e delle parzializzazioni  scelte dall'utente, memorizzabili e richiamabili.
Oltre alla stampa è possibile la visualizzazione e/o il trasferimento a PC.

_1_Funzioni Cartellini - Controllo Numerazione
Il controllo numerazione verifica che siano stati inseriti tutti i cartellini appartenenti ad un lotto di conta, la verifica è possibile solo se nella tabella GML per il lotto di conta in esame sono stati inseriti il numero iniziale e il numero finale.

_1_Funzioni Cartellini - Totalizzazione
Questa funzione, per tutti i cartellini di tutti i lotti di un inventario che abbiano stato 30 (contato), a parità di caratteristiche di giacenza, totalizza le quantità contate e genera o aggiorna le liste di conta inserendo la quantità totale contata e portando lo stato della conta a 30 (conta eseguita).

_3_Funzioni Liste di Conta
Raggruppa le funzioni per l'inserimento della quantità contata e per l'esecuzione di altre funzioni sulle liste di conta : 

![GMINVE_07](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_07.png)
_1_Funzioni Liste - Gestione in Lista
Permette di gestire l'inserimento delle quantità contate direttamente nella lista di conta.
La presentazione delle liste può essere ordinata e parzializzata secondo esigenze utente, le modalità di ordinamento e parzializzazione possono essere memorizzate con un nome caratteristico e richiamate quando si apre la lista.
Dentro la lista dei cartellini il comando funzione F10 permette l'inserimento di una nuova conta con dati di giacenza e quantità contate

_1_Funzioni Liste - Gestione per Giacenza/Articolo
Questa funzione consente la gestione individuale delle conte, è possibile entrare in lista chiedendo l'ordinamento delle conte per area/tipo giacenza o per articolo e passare da un ordinamento all'altro attraverso il comando funzione F15.
Dentro la lista delle conte il comando funzione F10 permette l'inserimento di una nuova conta con dati di giacenza e quantità contate.

_1_Funzioni Liste - Stampa
Permette :  stampa, visualizzazione o trasferimento a PC delle conte di un inventario, oltre alle normali funzioni di una stampa standard (ordinamento, parzializzazioni, schema informazioni, condizione libera utente) è prevista anche la possibilità della sola stampa dei totali.

_1_Funzioni Liste - Cancellazione Scostamento Nullo
Dopo che sono state inserite le quantità contate questa funzione permette di eliminare tutte le conte con scostamento nullo, in modo da poter ottenere liste e stampe delle sole conte con differenza.

_1_Funzioni Liste - Gestione Stato
Questa funzione permette la modifica di massa degli stati delle conte di un inventario da uno stato origine ad uno di destinazione, è possibile anche la visualizzazione.
La selezione delle conte da modificare di massa può essere parzializzata secondo le modalità standard.

_1_Funzioni Liste - Statistiche
La funzione presenta una serie di informazioni statistiche sull'inventario in gestione.


_3_Ripresa giacenza
Se previsto nella tabella inventari (GMI) questa funzione, per tutti gli articoli presenti nell'inventario, rifasa la quantità prevista riprendendola da : 

- giacenza alla data
- foto
- giacenza corrente

in funzione di quanto specificato nella GMI.


_3_Funzioni Rettifiche
Dopo che le conte sono state eseguite (utilizzando le liste di conta o i cartellini) e i risultati di conta sono stati inseriti (via gestione liste di conta o gestione e totalizzazione cartellini); per tutte le conte con differenza è possibile lanciare le rettifiche inventariali.
Per ogni area giacenza / tipo giacenza il sistema reperisce la causale di rettifica predisposta nella tabella GMC (causali di magazzino) e lancia i movimenti di rettifica inventariale, la data di registrazione del movimento è la data di esecuzione inventario inserita nella tabella GMI corrispondente.
Se esiste una conta con differenza ma, per l'area di giacenza / tipo giacenza a cui la conta fa riferimento, manca la causale di rettifica, viene emesso un messaggio di avviso e viene stampato un file di log.

![GMINVE_08](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_08.png)
_3_Totalizzazione Inventario per Articolo
Le conte di un inventario possono essere totalizzate per articolo, le conte totalizzate così ottenute vengono inserite in un nuovo inventario che è quello inserito nel campo «Codice Inventario di Totalizzazione» riportato nella tabella GMI. L'inventario totalizzato può essere completato con dati di costo e di classificazione, tipo costo e livello e tabella di sintesi (classificazione) sono riportati nella tabella GMI
Sugli inventari totalizzati per articolo sono possibili le seguenti attività : 

- _2_Generazione da inventario principale, genera le liste totalizzate per articolo partendo dalle liste dell'inventario principale .
- _2_Completamento, in base alla richiesta, può completare le liste totalizzate per articolo con i costi e la classificazione secondo :  tipo costo / livello e tabella di sintesi riportati nella tabella GMI.
- _2_Interrogazione, permette di accedere alle liste di conta totalizzate per articolo, l'interrogazione può essere per articolo o per area / tipo giacenza.
- _2_Stampa, permette :  stampa, visualizzazione o trasferimento a PC delle conte di un inventario, oltre alle normali funzioni di una stampa standard (ordinamento, parzializzazioni, schema informazioni, condizione libera utente) è prevista anche la possibilità della sola stampa dei totali.
- _2_Cancellazione scostamento nullo, questa funzione permette di eliminare tutte le conte con scostamento nullo, in modo da poter ottenere liste e stampe delle sole conte con differenza.
- _2_Statistiche, presenta una serie di informazioni statistiche sull'inventario in gestione.


![GMINVE_09](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_09.png)
### Funzioni Analisi Inventari per Magazzino/Articolo
Queste funzioni, dato un magazzino / articolo, permettono di verificare i risultati di tutte le conte di tutti gli inventari eseguiti.

![GMINVE_10](http://localhost:3000/immagini/MBDOC_OGG-P_GMSI03/GMINVE_10.png)
_3_Tutte le righe di conta
Visualizza tutte le righe di conta di tutti gli inventari presenti.

Visualizza solo le righe di conta con differenza di tutti gli inventari presenti.

_3_Riepiloghi per Inventario
Presenta la situazione totalizzata per articolo, indipendentemente da area / tipo giacenza.

_3_Statistiche
