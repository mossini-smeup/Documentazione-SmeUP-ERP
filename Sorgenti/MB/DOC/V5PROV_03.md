# Generalità
La liquidazione è la procedura tramite cui vengono consolidate le elaborazioni del calcolo provvigioni avvenute sui documenti in stato normale, mettendoli in condizione d'attesa fattura (P§FL10='b').

Se oltre a presentare un importo da liquidare il record risulta anche interamente pagato, verrà messo in stato chiuso e in stato di elaborazione 9 (da non elaborare).

La data dell'ultima elaborazione definitiva viene memorizzata nell'elemento della tabella B£4 ottenuto unendo la radice "*PC" + il codice di ogni periodicità.

Ad elaborazione eseguita in definitivo, è possibile ritornare alla situazione preelaborazione tramite un pgm di utility.
Quest'ultimo però permette di tornare indietro rispetto all'ultima elaborazione e non all'infinito in quanto i valori di preelaborazione sono memorizzati sul file stesso e riguardano solo la penultima elaborazione.

E' da considerare inoltre che, se dopo la liquidazione era stata eseguita la creazione del  piano / documento d'attesa in modo definitivo, dovrà prima essere riportata indietro anche tale elaborazione.

# Movimenti di liquidazione
Esiste l'archivio V5PROM0F destinato a contenere i movimenti di liquidazione provvigionali, che sono lo storico di tutte le liquidazioni fatte nel tempo sulla singola provvigione. Una provvigione, infatti, può essere liquidata in diversi periodi (se viene liquidata sull'incassato della fattura).
Alimentando questo archivio, abbiamo la possibilità di ristampare una liquidazione fatta in passato.
Il singolo movimento di liquidazione è a sua volta un oggetto (PM).

# Gestione anticipi
## Anticipi automatici
Se prevista una gestione anticipi, verranno anche generati dei record del V5PROV0F con il flag 12 <> '' (Anticipo) in stato chiuso e in attesa di fatturazione che, con la procedura di generazione dei documenti d'attesa, genereranno il documento relativo all'anticipo da corrispondere al soggetto in base all'elemento della V6Z (Piano Provvigioni) definito sulla tabella AGE o in risalita sulla tabella V58.

Questo tipo di elaborazione viene eseguita solo se la periodicità è mensile per i soggetti con una periodicità trimestrale e solo se non si sta trattando il mese di fine trimestre (nel quale viene corrisposta la fattura normale da cui dovranno essere detratti gli anticipi già corrisposti).
L'importo dell'anticipo a stardard può essere calcolato secondo 3 criteri : 
 * ad importo fisso
 * secondo una percentuale sul pagato
 * secondo una percentuale fatturato del periodo.

E' prevista però anche la possibilità di poter gestire la determinazione dell'importo tramite un pgm di exit, nel caso si utilizzino criteri differenti da quelli previsti.
Il nome di tale programma ha radice "V5PR04C_" + il suffisso indicato nella tabella V6Z.

Agli anticipi può essere attribuito un significato particolare in base all'utilizzo del tipo provvigione che attributo all'anticipo : 
* Se il tipo provvigione ha tipo "2" = Minimo garantito, come tale l'anticipo verrà conguagliato solo se le provvigioni superano l'importo del minimo garantito corrisposto.
* Se il tipo provvigione ha tipo "0" = Fisso, come tale l'anticipo non verrà mai conguagliato. sarà sempre un importo corrisposto all'agente in aggiunta a quello maturato tramite le provvigioni.
* Per gli altri tipi, gli importi anticipati verrà sempre conguagliati e in caso superino l'importo delle provvigioni, riportati al periodo successivo.

## Anticipi su fattura
Oltre agli anticipi automatici, è possibile gestire degli anticipi su fattura, che, utilizzabili anche con agenti a periodicità mensile, permettono di portare in detrazione l'anticipo solo quando viene liquidata una provvigione relativa alla fattura indicata nell'anticipo stesso, al di là di quando esso avvenga.
Questi anticipi vanno inseriti manualmente e contraddistinti dal valore 2, impostato nel flag 12.

# Oggetti
## Pgm del flusso
V5PR04G/V  :  Guida
V5PR04C    :  Esecuzione
V5PR04C_X  :  Eventuale pgm di exit per la determinazione degli importi d'anticipo da corrispondere
V5PR14A    :  Utility per il riallineamento del V5PROV dopo esecuzione definitiva della liquidazione

## Richiamo pgm Liquidazione
 :  : INI
 :  : CMD CALL V5PR04G
 :  : FIN
## Richiamo pgm Riallineamento liquidazione
 :  : INI
 :  : CMD CALL V5PR14A
 :  : FIN

## Tabelle
 :  : DEC T(ST) P() K(V58)
 :  : DEC T(ST) P() K(AGE)
 :  : DEC T(ST) P() K(V6Z)
 :  : DEC T(TA) P(B£4) K(*PCM)
 :  : DEC T(TA) P(B£4) K(*PCT)
