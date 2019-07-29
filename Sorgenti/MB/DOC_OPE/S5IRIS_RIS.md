# Scheda della schedulazione
Il risultato della schedulazione viene rappresentato in una scheda.
Nella sezione principale vengono riportate tutte le risorse schedulate a capacità finita, eventualmente suddivise per gruppo.
Il gruppo è l'insieme delle risorse che possono essere utilizzate, in alternativa, per eseguire la stessa operazione.

Le sezioni secondarie riportano : 

* le risorse su cui sono state eseguite operazioni manuali (congelamento, forzatura) e non ancora schedulate. Qualora la schedulazione risulti particolarmente gravosa, è possibile infatti operare manualmente sulle singole risorse, ed in un secondo tempo eseguire la schedulazione globale da questa scheda. Dopo aver schedulato, questa sezione ritorna vuota
* l'ambito su cui è stata eseguita la schedulazione
* un bottone che evidenzia la presenza di errori
* l'indice primario della schedulazione (scelto tra quelli calcolati, ed impostato nei parametri).
Per default viene presentata la percentuale di saturazione.

Da questa scheda si può, tramite i bottoni sul bordo inferiore : 
* finire :  tutte le azioni eseguite manualmente (ordinamenti, congelamenti e forzature) andranno perdute :  viene emesso un messaggio di avvertimento con richiedsta conferma.
* memorizzare :  ammessa solo se la sezione risorse modificate è vuota, vale a dire che l'ultima operazione eseguita è stata una schedulazione, e quindi la situazione della memoria è congruente, avendo recepito le azioni manuali impostate. Se così non è, e quindi ci sono delle azioni manuali in sospeso, viene data segnalazione ed impedita la memorizzazione.
I risultati della schedulazione (istanti di inizio e fine, risorse specifiche selezionate, azioni di congelamento e di forzatura) sono riportati sugli impegni risorse dello scenario di output.
Se essi vi sono già presenti, vengono aggiornati, in caso contrario verranno copiati in corrispondenti record dallo scenario di input.
* visualizzare gli indici globali della schedulazioe
* passare all'analisi della memoria :  funzione riservata a personale tencico, per esaminare in dettaglio il contenuto della schedulazione

Il seguente formato riporta un esempio della scheda della schedulazione. E' possibile selezionare i campi riportati nella matrice (in una exit specifica).
Lo standard propone, tra l'altro
* i giorni di makespan (GG Mks) :  per ogni risorsa l'intervallo (in giorni solari) tra l'inizio della schedulazione e l'ultima data in cui essa è schedulata, e la loro rappresentazione grafica, rapportata al valore massimo.
* il numero di impegni in esecuzione (Imp.Ese.)
* il numero di impegni non iniziati, da schedulare (Imp.Sch.)
* la % di carico di ogni risorsa rispetto alla totalità delle risorse del gruppo, rappresentata sia numericamente sia graficamente
* la % di saturazione di ogni risorsa, rappresentata sia numericamente sia graficamente, con colori diversi se la percentuale si abbassa (verde / giallo / rosso)

![FIG_060](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_060.png)
# Rappresentazione di dettaglio (Gantt / Incolonnata)
Cliccando su una risorsa specifica, nella sezione principale della scheda della schedulazione, si presenta il seguente popup
![FIG_063](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_063.png)
da cui si può passare alla rappresentazione di dettaglio
* su tutte le risorse schedulate  (Gantt totale)
* su tutte le risorse appartenenti al gruppo della risorsa selezionata (Gantt della risorsa generale), questo bottone è presente solo se è stata attivata nello scenario la distinzione tra risorse generali e specifiche
* sulla risorsa stessa (Gantt della risorsa specifica)

E' possibile inoltre impostare, nello script dei parametri BCD, due codici OAV che, se definiti, aggiungono due bottoni, la cui pressione fa passare al dettaglio di tutte le risorse (generali o specifiche, in base a quanto impostato, sempre nello script dei parametri) che hanno lo stesso valore dell'OAV della risorsa puntata.

Nel seguente esempio si è scelto di poter filtrare per il responsablie del centro di lavoro a cui appartiene la macchina selezionata, o per il codice di appartenenza della macchina stessa.
![FIG_076](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_076.png)
Le righe presentate si dividono in due tipi : 
* riga riassuntiva - una per ogni risorsa specifica
* riga di dettaglio - un per ogni fase schedulata

A sua volta la riga si divide in due parti : 
* parte informativa, in cui è riportato il codice della risorsa e, se la riga è di dettaglio, ulteriori informazioni sulla fase
* parte grafica, in cui per ogni fase viene riportata una cella
** rappresentazione Gantt :  la cella ha la lunghezza proporzionale alla durata della fase, ed è collocata in sequenza temporale
** rappresentazione Incolonnata, in cui tutte le celle hanno la stessa dimensione e sono collocate nella stessa colonna. In questa forma, la perdita dellla collocazione temporale è bilanciata dall'omogeneità delle celle e dal maggior numero di informazioni riportabili nella parte informativa.

## Impostazioni dei campi della riga
Si può scegliere quali campi riportare nella parte informativa della riga con la modlità standard del componente Gantt.
La specificità della schedulazione è che è possibile, con exit utente, modificare la lista dei campi (aggiungerne e toglierne) da cui si scelgono quelli da riportare nella riga.
L'impostazione della riga può essere salvata, in modo da essere riproposta all'ingresso successivo, nella gestione viste del componente Gantt.
Il nome della vista salvata deve essere  :  XXY dove XX è ripreso da quanto impostato nello script dei parametri e Y vale ' ' per la forma a Gantt e 'I' per la forma incolonnata. In questo modo si possono avere parti informative diverse per le due forme.
Questa memorizzazione vale per tutti gli utenti.

## Impostazioni generali
E' possibile settare la presentazione del dettaglio, operando nella finestra di impostazioni,
richiamata dal menu di popup ottenuto premendo il tasto destro in una zona vuota del Gantt.

![FIG_064](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_064.png)
Tali impostazioni permettono : 
* di non visualizzare i segnali delle date
** al più presto
** vincolo esterno
** fine richiesta
** fine schedulata
* di entare in modo bloccato (lo spostamento delle celle deve essere attivato esplicitamente :  riferirsi alla documentazione generale del componente Gantt)
* di entare in modo chiuso, visualizzando solo la riga riassuntiva. Questa impostazione non ha effetto in visualizzazione totale, che è sempre eseguita in tale modalità.
* di entare in presentazione incolonnata
* di inserire due soglie di giorni di ritardo, per visualizzare in modo diverso il ritardo stesso.
* di evidenziare l'attrezzaggio.
* di non presentare le risorse vuote (non caricate) :  significativa solo se si è in visualizzazione delle risorse specifiche di una risorsa generale
* di entrare in modo chiuso se si è in visualiizzazione filtrata da un OAV.

## Visualizzazione di tutte le risorse
In modalità Gantt viene riportata una riga riassuntiva per ogni risorsa caricata, con le fasi schedulate una accanto all'altra in sequenza temporale. E' possibile aprire ogni risorsa per  visualiizzare le righe in dettaglio.
La figura seguente riporta un esempio di questa presentazione.
![FIG_065](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_065.png)In modalità Incolonnata viene riportata una riga riassuntiva per ogni risorsa caricata, ma essa appare vuota in quanto le celle si sovrapporrebbero.In questo caso, l'apertura delle singole risorse è obbligatoria.
La figura seguente è un esempio di questa presentazione, dopo aver aperto manualmente la risorsa MOA.02
![FIG_066](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_066.png)
## Visualizzazione di una risorsa generale e delle sue risorse specifiche.
Vengono presentate le risorse specifiche della risorsa generale, ciascuna con la riga riassuntiva ed il dettaglio.
In questa forma si può sceglere se vislauzziare o meno le risorse vuote, e se entare in modalità aperta o chiusa
Nelll'esempio seguente viene riportato un caso di presentazione a Gantt, in modalità aperta e con le risorse vuote visualizzate (ad esempio le macchine ASA.02, ASA.03, ecc--)
![FIG_067](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_067.png)L'esempio seguente è la stessa visualizzazione in modalità incolonnata.
![FIG_068](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_068.png)
### Filtro solo preferenziali
In questa rappresentazione, se è attivo il filtro delle risorse specifiche è possibile utilizzarlo per visulizzare un sottoinsieme delle risorse specifiche.
Se si attiva il poup da una cella la cui fase ha un filtro di risorse specifiche, si presenta il bottone "visualizza solo preferenziali" la cui pressione fa sì che appaiano solo le risorse del filtro (oltre alla risordsa attuale della cella, se non appartiene al filtro).

Nel seguente esempio, la pressione del bottone "Visualizza solo preferenziali" farà sì che vengano mostrate le risorse MOA.02 e MoA.03 (che costituiscono il filtro) e la rlsorsa MOA.01 (attuale). Si rimanda al documento "Azioni manuali" per la descrizione completa del bottone "Sposta nel gruppo" che mostra il flitro.
![FIG_026](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_026.png)
Dalla presentazione filtrata, si ritorna alla visualizzazione completa tramite il pulsante "Visualizza tutti" che, in questo caso,appare nei popup di tutte le celle.

## Visualizzazione di una singola risorsa specifica.
La rappresentazione è simile alla precedente, con la differenza che viene presentata una sola risorsa specifica (obbligatoriamente caricata).

## Azioni eseguibili
Le azioni generali eseguibili, dall'inteno di un dettaglio, si richiamano cliccando in una zona libera della parte grafica.
Appare il seguente popup : 
![FIG_069](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_069.png)
In esso è possibile
* Alternare la presentazione Gantt e Incolonnata (nell'esempio precedente si è in Incolonnata e quindi viene proposto di passare alla visualizzazione Gantt
* Passare alla definizione delle Impostazioni. Al ritorno, il dettaglio verrà riaggiornato con le nuove impostazioni.
* Eseguire la schedulazione globale, al termine della quale verrà ripresentato lo stesso dettaglio, con i valori eventualmente aggornati, Questa funzione è utile dopo aver eseguito azioni manuali, per verificarne l'effetto.

## Formato celle
Nel dettaglio le celle rappresentano le operazioni schedulate. La loro forma permette di individuare facilmente il loro stato.

Esse possono infatti essere : 
**iniziate** :  è stata eseguita almeno una dichiarazione di attività
![FIG_003](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_003.png)**libere** :  non son state iniziate e non vi è nessuna azione manuale
![FIG_002](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_002.png)**congelate** :  vedi documentazione sulle azioni manuali
![FIG_001](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_001.png)**forzate** :  vedi documentazione sulle azioni manuali
![FIG_004](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_004.png)
Se è stato impostato di evidenziare l'attrezzaggio e se esso è effettivamente presente, all'interno della cella viene riportata una barra verticale.
* nella rappresentazione GANTT, in cul la lunghezza della cella è proporzionale al tempo della fase, la barra è posizionala all'instante di fine attrezzaggio.
* nella rappresentazione incolonnata, in cui tutte le celle hanno la medesima lunghezza, la barra è posizionata alla fine della percentuale di attrezzaggio rispetto al tempo totale. Ad esempio, se l'attrezzaggio è il 20 % del tempo totale, la barra è sempre nella stessa posizione (ad un quinto dall'inizio della cella) indipendentemente dal tempo della fase.

## Segnali
Vengono riportati inoltre dei segnali e che rappresentano gli istanti significativi per l'operazione della riga a cui appartengono.

Ad esempio, se si impostano 5 giorni per l'anticipo di livello 1 e 15 giorni per l'anticipo di livello 2, si individueranno tre fasce, in cui la data fine schedulata verrà rappresentata in modo diverso : 
* gli ordini con anticipo inferiore a 5 giorni (sotto la soglia 1)
* gli ordini con anticipo tra 5 e 15 giorni (tra la soglia 1 e la soglia 2)
* gli ordini con anticipo superiore a 15 giorni (sopra la soglia 2)

Alcuni segnali sono riportati in entrambe le forme di presentazione (Gantt e incolonnata), alcuni invece soltanto in una sola di esse :  in tal caso nel seguito di questa documentazione ne verrà data indicazione esplicita.

I segnali nella rappresentazione Gantt son collocati all'istante in cui si verificano, in quella incolonnata invece sono riportati sempre nella stessa posizione (che non  è quindi temporalmente significativa).

Vengono riportati i seguenti segnali : 

__Solo in Gantt__ :  data al più presto (vincolo dalla fine dell'operazione precedente)
![FIG_005](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_005.png)__Solo in Gantt__ :  vincolo esterno al più presto
![FIG_020](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_020.png)__Solo in Gantt__ :  data fine richiesta (dell'ordine a cui l'operazione appartiene)
![FIG_006](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_006.png)__Solo in incolonnata__ :  data fine richiesta (dell'ordine a cui l'operazione appartiene) se scaduta
![FIG_021](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_021.png)__Solo in incolonnata__ :   c'è una hole subito prima dell'operazione visualizzata
![FIG_022](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_022.png)**data fine schedulata**(dell'ordine a cui l'operazione appartiene)
se inferiore alla data fine richiesta (anticipo)
sotto la soglia 1 (anticipo basso)
![FIG_007](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_007.png)tra la soglia 1 e la soglia 2 (anticipo medio)
![FIG_008](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_008.png)sopra la soglia 2 (anticipo alto)
![FIG_009](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_009.png)se superiore alla data fine richiesta (ritardo)
sotto la soglia 1 (ritardo basso)
![FIG_010](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_010.png)tra la soglia 1 e la soglia 2 (ritardo medio)
![FIG_011](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_011.png)sopra la soglia 2 (ritardo alto)
![FIG_012](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_012.png)se uguale alla data fine richiesta (ordine puntuale)
![FIG_013](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_RIS/FIG_013.png)