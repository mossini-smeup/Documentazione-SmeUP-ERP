## Struttura tecnica MRP
L'MRP, per ogni articolo, riempie i'archivio dei suggerimenti
 :  : DEC T(OJ) P(*FILE) K(M5CONS0F)
con le informazioni ottenute dalla scansioni disponibilità (fonti rilasciate) e le completa con la scrittura di nuove informazioni (fonti pianificate di ordini e impegni) e l'aggiornamento delle fonti precedenti (suggerimenti di modifica alle fonti rilasciate).

##  Introduzione
La "colonna vertebrale" dell'MRP, che guida l'esecuzione della pianificazione di ogni singolo codice, con la corretta sequenza, è il programma
 :  : DEC T(OJ) P(*PGM) K(M5MRP0A)
che riceve le impostazioni dal programma di guida
 :  : DEC T(OJ) P(*PGM) K(M5MRP0G)

## Impostazioni generali
L'MRP può essere eseguito totalmente o per un singolo articolo, una lista di articoli o una commessa.
La singola pianificazione non differisce, ma varia la modalità di reperimento degli articoli da pianificare.

Come prima cosa, se lo scenario è autopulente (impostato nello scenario), vengono cancellati tutti gli elementi dello scenario, indipendentemente dal fatto che la pianificazione sia parziale o completa.
 :  : DEC T(VO) P(T.M5B) K(T$M5BV) O(D)

## Parziale :  un articolo o una lista di articoli
Il caso del singolo articolo può essere considerato come una lista composta da un solo articolo, quindi tratteremo solo questo secondo caso.
Viene utilizzato un file di lavoro in cui, all'inizio, si inseriscono gli articoli della lista.
Dopo di ciò, si legge questo archivio, e, per ogni articolo incontrato, si esegue la pianificazione, con la previa cancellazione di tutti i record dei consigli relativi all'articolo in esame (ad eccezione degli impegni pianificati) , e di tutti gli impegni pianificati appartenenti ai suoi ordini pianificati. Vengono poi inseriti in coda al file di lavoro, se non già presenti (e non pianificati) i codici degli articoli degli impegni pianificati che sono stati appena cancellati. Così facendo, questi articoli verranno ritrovati in seguito, scorrendo l'archivio di lavoro e, a loro volta, pianificatI.
Questo procedimento termina quando il puntatore al record che si sta leggendo raggiunge quello che si sta scrivendo, vale a dire quando non c'è più nessun articolo da trattare.
Questo modo di operare è conservativo, in quanto riesegue la pianificazione anche se non differisce dalla precedente, arrestandosi al punto in cui non trova più nuovi ordini di produzione (o di conto lavoro) da pianificare.
Esso è inoltre indipendelte dal livello minimo, in quanto un articolo può essere trovato (e quindi pianificato) più di una volta nel corso dell'elaborazione, ogni volta con informazioni più complete. Ad esempio, se A -> C e A -> B -> C, C la prima volta considera i suoi impegni che dipendono da A, la seconda volta anche quelli che dipendono da B. In questo modo non è necessario avere l'archivio dei livelli minimi corretto (cosa che si ottiene ricostruendolo prima di un MRP totale, mentre non è proponibile la ricostruzione in un MRP parziale).
E' possibile attivare un log di stampa (collegato al programma M5MRP0A) che presenta la sequenza di tutti gli articoli trattati, nell'ordine in cui vengono pianificati.
Va ricordato che la pianificazione di un set di articoli può differire da quella totale, in quanto essa opera unicamente in discesa. Se, ad esempio, sono presenti i seguenti legami di distinta :  D -> F e E -> F, se si vuol pianificare unicamente l'articolo D, che trascina come effetto la pianificazione di F, tra gli impegni pianificati di quest'ultimo non sono considerati quelli che potrebbero derivare da una maggior domanda di E successiva all'ultima pianificazione, che sarebbero invece presenti in una pianificazione totale.


##  Completa
La pianificazione completa si svolge nei seguenti passi : 
Si fissa l'istante di inizio.
Si pulisce l'archivio (tutto o selettivamente, in base al fatto che la pianificazione sia mono o multiscenario, e monoplant o monocommessa)
Se impostato in M51 si ricalcola il livello minimo di distinta
Si lanciano i flussi PRE.
Si scandisce l'archivio contenente i livelli minimi
 :  : DEC T(OJ) P(*FILE) K(BRARDT0F)
e si pianificano, in sequenza, tutti i record trovati (con eventuale inclusione / esclusione di fittizi e codici a punto di riordino, in base a quanto impostato nel lancio).
Se non è stato calcolato il livello minimo di distinta, successivcamnente si scandisce l'anagrafica articoli, e si pianificano i codici non presenti nell'archivio del livello minimo. Questo si rende necessario in quanto la mancata ricostruzione del livello minimo sta a significare che si mantengono i valori determinatri durante la manutenzione della distinta base. Eventuali codici non presenti in distinta, di pura commercializzazione (acquistati e venduti) non sono quindi presenti nemmeno nell'archivio del livello minimo, e quindi non verrebbero trattati dalla pianificazione. Il ricalcolo di massa del livello minimo registra invece nell'archivio tutti i codici, eventualmente con livello minimo pari a zero (che è il caso degli articoli di commercializzazione), e qundi rende superfluo il secondo giro di scansione degli articoli.
Si eseguono i flussi POST.
Si fissa l'istante di fine e si registra il record di log della pianificazione.


## Parziale per commessa
La pianificazione ner singola commessa viene eseguita lanciando la pianificazione completa con il filtro, nella scansione dell'analisi disponibilità, della commessa impostata.
Questa pianificazione ha una zona "grigia" corrispondente agli articoli (non gestiti a commessa) che sono componenti di un articolo gestito a commessa. Quando si pianifica quest'ultimo vengono scritti, se è il caso, impegni pianificati per i primi, con la commessa ereditata. Ma, quando si tratta di pianificare questi articoli, anche se gli impegni pianificati vengono ritornati dall'analisi disponibilità (la commessa è presente), non vengono trattati, perchè essa non viene copiata nell'oggetto di rottura.
Questi articoli quindi, fino ad una successiva pianificazione totale ( o comunque non monocommessa), possono risultare sbilanciati, avendo impegni pianificati in eccesso.


## Pianificazione singolo articolo
Indipendentemente da come viene selezionato, si arriva alla pianificazione di ogni singolo articolo.
Essa differisce in base alla modalità multiplant.
Se monoplant o multiplant cumulata la si lancia solo una volta per il primo plant del gruppo fonti (eventualmente compattandovi gli altri, nella modalità cumulata).
Se invece è mulriplant completa, si determina il plant di competenza, e la si lancia per ogni plant del gruppo fonti, lasciandno come ultimo il plant di competenza che, in tal modo, soddisfa gli impegni di trasferimento pianificati in precedenza verso gli altri plant.
Questa modalità di pianificazione di un plant alla volta potrà permettere, in futuro, di implementare strategie più raffinate, di trasferimenti da plant a plant (ad esempio un legame plant -> plant di competenza a livello di articolo o di famiglia). Ciò si tradurrebbe in un ordinamento specifico dell'ordine dei plant da elaborare, e nell'impostazione del plant di partenza negli ordini di trasferimento in funzione del plant d'arrivo.

## Struttura tecnica esecuzione MRP
Viene prima lanciato il programma
 :  : DEC T(OJ) P(*PGM) K(M5M5R0I)
che esegue la scansione disponibilità, scrive i record rilasciati e prepara le schiere per il calcolo
Viene poi eseguita la routine di calcolo
 :  : DEC T(MB) P(QILEGEN) K(£M5R)
che esegue il vero e proprio MRP, e che, a sua volta, lancia la routine
 :  : DEC T(MB) P(QILEGEN) K(£M5S)
per completare il suggerimento di nuovi ordini (lottizzazione, applicazione lead time, assegnazione ente)
e la routine
 :  : DEC T(MB) P(QILEGEN) K(£M5W)
che scrive gli impegni pianificati scandendo la distinta base.
Sono presenti inoltre i programmi di servizio (lanciati anch'essi dall'interno dell'MRP)
 :  : DEC T(OJ) P(*PGM) K(M5M5R0C)
che esegue la modifica agli ordini in corso e calcola i ragguppamenti dei fabbisogni (sia in termine di quantità sia di data massima)
 :  : DEC T(OJ) P(*PGM) K(M5M5R0K)
che calcola la classe di copertura

## Schiere dell'MRP
Tecnicamente l'MRP opera su una serie di schiere, e solo opzionalmente si "fissa" sull'archivio dei consigli (lanciando sia la scansione della disponibilità sia la pianificazione con metodo "WRI").
 :  : DEC T(MB) P(QILEGEN) K(£M5RE)
La documentazione di queste schiere è contenuta nel sorgente di questa copy.






