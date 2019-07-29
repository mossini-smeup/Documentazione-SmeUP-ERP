# Introduzione
La schedulazione BCD ha come risultato la datazione dei dettagli.
In presenza di sole risorse principali ciò si traduce nel produrre code di impegni su ciascuna di esse.
In presenza anche di risprse specifiche, le code prodotte su di esse implicitamente esprimono la scelta sul luogo dove vengono eseguiti gli impegni. Infatti, quando si schedula un dettaglio, vengono annullati i suoi collegati (relativi allo stesso impegno) in modo da essere esclusi nelle scelte successive.
Riassumendo : 
Se presenti solo le risorse principali la schedulazione risponde alla domanda :  quando si eseguono gli impegni?
Se presenti anche le risorse specifiche la schedulazione risponde invece alle domande :  quando e dove si eseguono gli impegni?

Questo risultato si ottiene con l'esecuzione di uno script, costituito da una serie di passi che riempiono la memoria dagli archivi dell'applicazione, la modificano e riportano i risultati sugli archivi.

![FIG_014](http://localhost:3000/immagini/S5IRIS_T12/FIG_014.png)
# Descrizione script BCD
Nel seguito viene descritto a grandi linee lo script proposto come base per la schedulazione, contenuto nel membro INT del file BCDSRC.
 :  : DEC T(MB) P(BCDSRC) K(INT) L(1)

Vengono innanzitutto caricate le DS delle risorse, all'esterno del loop generale di schedulazione, in quanto si assume che il loro contenuto non venga modificato dall'interno della schedulazione.

Viene poi eseguito il loop generale in cui, per prima cosa, vengono riempite le DS degli impegni  (se, dall'interno del Gantt si modifica un ordine di produzione, disattivando e attivando alcune fasi, gli impegni di risorse dell'ordine in esame si modificano, e quindi è necessario rigenerare
le loro DS), quindi vengono ricostruite le alternative e i dettagli.

Si controlla quindi la presenza di errori bloccanti, nel qual caso non si può proseguire :  viene emessa la matrice di presentazione errori e si termina l'esecuzione.

Si eseguono qundi le azioni generali di input, eseguite sulle memorie complete e corrette.

A questo punto si può iniziare la schedulazione, essendo l'input completato.

Come prima cosa vengono schedulate, al più presto, le operazioni iniziate. Se ce n'è più di una per una risorsa, si schedulano lifo (in ordine di data ultima attività decrescente).

A questo punto si entra nel loop di schedulazione.
Si sceglie l'operazione più urgente, la si schedula, e si ripete il processo fino a quando sono stati esaminati tutti gli impegni.

Al termine, si calcolano gli indici globali, si determina, se è il caso, lo stato dei materiali, e si passa alla presentazione dei risultati.

Dopo la prima schedulazione viene presentata la matrice delle risorse, le volte successive si ritorna invece al punto da cui si era scelto di rischedulare (matrice delle risorse o Gantt specifico).
La scelta di rischedulare si traduce nel rimanere nel loop, dopo aver reinizializzazto le DS.

Dalla matrice delle risorse si può invece uscire, decidendo qundi di non salvare la schedulazione appena eseguita, oppure di memorizzarla (in questo caso non si devono aver eseguito congelamenti o forzature dopo l'ultima schedulazione), aggiornando gli impegni risorse dello scenario di output, e fissando gli indici in un record di D5COSO.

# Forzature e congelamenti
Le forzature e i congelamenti sono riportati sulla DS di S5IRIS, in due versioni : 
 * i dati originali
 * i dati di sessione
Nella costruzione iniziale di DSIRIS vengono entrambi riempiti con i valori di S5IRIS.
I dati di sessione vengono poi aggiornati con le azioni nel Gantt.
All'atto della rischedulazione vengono salvati sulla DSFORZ (programma S5SMES_03), all'interno della fase di reinizializzazione delle DS, e quindi, dopo la ricostruzione dell'IRIS, vengono riempiti, sempre nell'IRIS, a partire da questa DS (nel programma S5SMES_01F).
In tal modo si hanno sempre i dati originali (per eventuali futuri rollback), ed i dati delle ultime scelte eseguita.
![FIG_014](http://localhost:3000/immagini/S5IRIS_T12/FIG_014.png)