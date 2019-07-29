# Generalità

L'attivazione o meno delle combo all'interno di un input è nativamente collegata alla classe :  senza che si debba specificare informazioni aggiuntive se la classe prevede che per essa vengano utilizzate le combo, quando la classe viene impiegata in un input panel verrà già presentata con la relativa combo.

Questa informazione è fissata attraverso la /COPY £K04, dove sono fissate le classi che a standard prevedono le combo e che modalità di combo (elenco completo o con ricerca).

 :  : DEC T(MB) P(QILEGEN) K(£K04) L(1)

# Personalizzazione delle combo a livello di classe

Come anticipato le combo sono normalmente fissate dallo standard attraverso la /COPY £K04. Queste informazioni possono però essere sovrascritte a livello di classe a partire dall'exit della /COPY £K04, B£K04G_U. Attraverso è possibile indicare che oggetti dello standard che non prevedono la combo, la prevedano o viceversa che oggetti dello standard che la prevedono, non al prevedano o la prevedano in modalità differente rispetto a quella standard (es. se ho pochi articoli potrei fissare che per gli articoli mi venga presentata la combo in modalità elenco completo).

# Personalizzazione delle combo a livello di servizio

Oltre che alla sovrascrittura a livello di classe è inoltre possibile personalizzare l'utilizzo delle combo a livello di singolo servizio. Queste personalizzazione può avvenire a vari livelli qui di seguito elencati : 
* Forzare che un oggetto che normalmente prevede la combo non la preveda :  per ottenere questo risultato è necessario forzare nella griglia e nel setup di aggiornamento che l'attributo di input/output del campo non è "B", com'è normalmente, ma "b".
* Forzare che un oggetto che normalmente non prevee la combo la prevede :  per ottenere questo risultato è necessario forzare nella griglia e nel setup di aggiornamento che l'attributo di input/output del campo non è "B", com'è normalmente, ma "C" o "E" a seconda che si voglia attivare una combo in modalità elenco completo o ricerca.
* Che la combo sia prevista nativamente o per effetto della sopracitata forzature è possibile inoltre forzare la funzione di risoluzione della combo (quella standard si può verificare, attraverso la /COPY £K04 alla risposta della funzione COM). Per ottenere questo vanno valorizzate le schiere £JayComLst, a loro volta rimappate con la DS £JayDSCom. Per sovrascrivere la funzione dovrà essere indica come riferimento nel campo £JayCNM della DS di ogni elemento il nome del campo della griglia. Qualunque sia la funzione che verrà lanciata, questa avrà comunque il vincolo di risponde con un XML di matrice composto da due sole colonne, codice e descrizione. Per la costruzione delle funzione si hanno a disposizione, purchè vengano gestiti di dinamismi  opportuni (When Change e LostFocus) si hanno tutte le variabili corrispondenti alla riga della matrice, nonchè le variabili T1/P1/K1 che contengono il tipo, il parametro ed il contenuto della cella da cui viene lanciata la funzione della combo.
* Va infine rilevanto che in alternativa all'indicazione della funzione esplicita, la funzione di combo può inoltre essere sovrascritta attraverso l'indicazione dell'elenco completo dei valori selezionabili nella combo, riempiendo sempre le schiere le schiere £JayDSCom.

Quanto sopra riportato vale anche per forzare l'utilizzo delle combo su una matrice, che nativamente non ne prevede l'impiego.

Per i nomi di Schiere/Variabili si veda nello specifico del documentazione del componente EXU.

 :  : DEC T(TA) P(B£AMO) K(LOCEXU) L(1)

