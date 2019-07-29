# PARAMETRI GANTT IMPEGNI PER RISORSA
## OBIETTIVO
Vengono esposte le scelte che guidano la presentazione del Gantt degli impegni ordinati per risorsa.
## SCELTE
### Nascondi data al + presto
Se impostato, non verrà presentata la data al più presto.
Questa data, che è la fine dell'operazione precedente, eventualmente corretta dalla sovrapposizione, viene rappresentata da una freccia gialla verso destra.
In presentazione incolonnata questo campo non vienei presentato.
### Nascondi data fine richiesta
Se impostato, non verrà presentata la data fine richiesta dell'ordine.
Questa data viene rappresentata da una freccia blu verso sinistra.
In presentazione incolonnata questo campo non viene presentato.
### Nascondi data fine schedulata
Se impostato, non verrà presentata la data fine schedulata dell'ordine a cui appartiene la fase.
Se è anteriore alla fine richiesta, viene rappresentata con uno, due o tre triangoli verdi verso sinistra, a seconda che l'anticipo in giorni sia minore della prima soglia, sia compreso tra la prima e la seconda, o sia superiore alla seconda.
Se è superiore alla fine richiesta, viene rappresentata con uno, due o tre triangoli rossi verso destra, a seconda che il ritrardo in giorni sia minore della prima soglia, sia compreso tra la prima e la seconda, o sia superiore alla seconda.
Se coincide con la fine richiesta, viene rappresentata con un cerchio verde.
### GG anticipo livello 1
Definiscono la prima soglia per scegliere la rappresentazione della data fine schedulata, se anticipata (inferiore alla fine richiesta).
### GG anticipo livello 2
Definiscono la seconda soglia per scegliere la rappresentazione della data fine schedulata, se anticipata (inferiore alla fine richiesta).
Se impostati, devono essere maggiori dell'anticipo 1.
### GG ritardo livello 1
Definiscono la prima soglia per scegliere la rappresentazione della data fine schedulata, se ritardata (superiore alla fine richiesta).
### GG ritardo livello 2
Definiscono la seconda soglia per scegliere la rappresentazione della data fine schedulata, se ritardata (superiore alla fine richiesta).
Se impostati, devono essere maggiori del ritardo 1.
### Nascondi vincolo esterno
Se impostato, non verrà presentata la data di vincolo esterno
Questa data, che è impostata dall'esterno (con funzioni specifiche) viene rappresentata da una freccia grigia verso destra.
In presentazione incolonnata questo campo non viene presentato.
### Ingresso bloccato
Se impostato, non è possibile eseguire azioni di spostamento e di costruzione gruppi temporaneti sulle celle del Gantt.
La costruzione dei gruppi temporanei è impedita anche se non è stata attivata la loro gestione (nello script di parametri), indipendentemente dal valore del presente campo.
### Ingresso chiuso su dettaglio
Normalmente, l'ingresso è chiuso (si pesentano solo le risorse e non le celle) nella presentazone totale, mentre è aperto nella  presentazione di dettaglio (singola risorsa, generale o specifico).
Impostando questo campo, si forza l'ingresso chiuso anche sul dettaglio.
### Presentazione incolonnata
Se impostato, gli impegni vengono rappresentati in verticale, in modo da riservare più spazio alla parte a sinistra (e qunindi poter ritornare un maggior numero di informazioni).
Lo switch tra rappresentazione incolonnata e rappresentazione a Gantt è presente anche sul popup (della zona vuota di celle). La modifica via popup è equivalente alla modifica in questo configuratore.
### Evidenzia attrezzaggio
Se impostato, e se deciso di calcolare, nello script dei parametri, la fine dell'attrezzaggio, questo istante viene rappresentato da una barra verticale.
Nella rappresentazione a Gantt essa viene situata alla sua posizione temporale.
Nella rappresentazione incolonnata, essa viene posizionata in base alla percentuale dell'attrezzaggio rispetto al tempo totale della cella.
Ad esempio, se il tempo totale è di 80 minuti e l'attrezzaggio è di 20 minuti, la barra viene posizonata al 25 % della cella.
### Nascondi risorse vuote
Se  impostato, le risorse su cui non è stata schedulata nessuna fase non sono presentate.
Ciò rende la presentazione più sintetica.
Va tenuto presente che, in presenza di risorse specifiche, trascinare una cella su una risorsa vuota ha l'effetto di forzarvi la cella.
### Ingresso chiuso su OAV
In presenza di un OAV di riclassifica sulla risorsa specifica, l'ingresso, normalmente aperto, con questa impostazione sarà invece chiuso.
### Nascondi slave / gruppi temporanei
Se impostato, le celle slave di batch e gruppi temporanei non verranno presentate.
Lo switch tra visualizzazione e occultamento delle celle slave è presente anche sul popup (della zona vuota di celle). La modifica via popup è equivalente alla modifica in questo configuratore.
### Sfondo su batch / gruppi temporanei
Se impostato, gli impegni che formano un batch, o un gruppo temporaneo, avranno sullo sfondo una griglia dall'istante di inizio a quello di fine del tiro.
Il colore della griglia è blu se batch, arancio se gruppo temporaneo.
Se il batch o il gruppo temporaneo viene mosso in un'altra posizione, lo sfondo apparirà verde, fino alla successiva rischedulazione.
Per evidenziare la presenza del gruppo, utile specialmente nel caso di slave nascoste, l'altezza della cella master è ridotta, in modo da presentare sullo sfondo la griglia stessa.
In presentazione incolonnata questo campo non viene presentato.
### Sfondo su tiro
Se impostato, gli impegni che formano un tiro avranno sullo sfondo una griglia rossa dall'istante di inizio a quello di fine del tiro.
In presentazione incolonnata questo campo non viene presentato.
### Nascondi riga raggruppata
Se impostato, non verrà presentata la riga raggruppata per ogni gruppo, che contiene, uno accanto all'altro, tutti gli impegni del
gruppo stesso.
Questa riga non vienei presentata in presentazione incolonnata od in presenza di batch, in quanto in questi casi ci sono impegni che
si sovrappongono, e quindi essa perderebbe di rappresentatività.
### Cella master allargata
Questa impostazione è significativa se impostato lo sfondo (su batch e gruppi temporanei).
Se impostata, la cella master andrà dall'inizio alla fine del gruppo o del batch, in modo da poter essere più facilmente puntata.
Ciò è utile nel caso di gruppi temporanei, che possono contenere un gran numero di impegni, ciascuno di una durata molto breve rispetto a quella dell'intero gruppo.
In presentazione incolonnata questa opzione non è significativa.
### Ora in azioni di massa
Le azioni di massa premettono il congelamento e lo scongelamento contemporaneo di più celle presenti nel Gantt.
L'azione viene eseguita impostando un istante limite (data e ora), con la seguente regola : 
In caso si congelamento si congelano le celle con inizio schedulato minore o uguale all'istante limite.
In caso di scongelamento si scongelano le celle con inizio schedulato maggiore o uguale all'istante limite.
La data limite è individuata dalla posizione del Popup, e corrisponde al giorno in cui è situato il triangolo rosso che appare, in alto, sulla barra del tempo.
Per quanto riguarda l'ora limite, se non si imposta il presente campo, viene assunta in modo "conservativo", vale a dire le ore 24,00 per il congelamento, e le ore 0,00 per lo scongelamento.
Se invece si imposta il presente campo, si assume, anche per l'ora limite, la posizione del Popup, e quindi l'istante limite corrisponde esattamente alla posizione del triangolo rosso.
### Intervalli di chiusura
E' possibile presentare, come sfondo grigio, gli intervalli in cui la risorsa specifica è chiusa
Vengono evidenziati su tutte le righe, fino all'ultimo istante di carico della risorsa.
Con l'opzione '1' si presentano tutti gli intervalli di chiusura.
Con l'opzione '2' si presentano invece unicamente i giorni di chiusura totale. Ad esempio, se la risorsa è chiusa dal venerdì alle 18 fino al lunedì alle 7, viene presentato l'intervalo dalle 0 del sabato alle 24 della domenica.




