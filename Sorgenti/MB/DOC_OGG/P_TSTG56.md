# FUNZIONI NUMERICHE
## Introduzione
Scopo della /COPY G56 è l'esecuzione di operazioni matematiche su numeri, serie e coppie di serie. Una serie è una sequenza di numeri, la si può rappresentare geometricamente come un insieme di punti su una retta su cui è stata definita l'origine. Una coppia di serie è formata da due sequenze di numeri, la si può rappresentare come un insieme di punti nel piano cartesiano, ciascuno con l'ascissa costituita dalla seconda serie e l'ordinata dalla prima; il numero di elementi delle due serie è lo stesso, in quanto costituisce il numero di punti. Un modo particolare di definizione delle due serie è quello in cui la seconda è il "passo unitario" della prima. In tal caso essa viene riempita automaticamente nel seguente modo :  se la prima serie è composta da questi 5 elementi :  23, 12, 34, 45, 0; viene riempita la seconda con le posizioni della prima; 1, 2, 3, 4, 5.
NB :  questo è unicamente un modo di inserire automaticamente la seconda serie, che potrebbe essere inserita manualmente, senza che nulla cambi nei risultati.

E' possibile calcolare : 
 * __funzioni scalari__ :  viene ritornato un numero, o un insieme di numeri di significato diverso. Un esempio del primo caso è la media di una serie. Un esempio del secondo caso è la regressione lineare di due serie, il cui risultato è costituito da due numeri :  il coefficiente angolare e l'ordinata all'origine della retta interpolatrice.
 * __funzioni vettoriali__ :  viene ritornata una serie di numeri con significato omogeneo. E' possibile calcolare funzioni vettoriali anche sui numeri :  un esempio è la scomposizione in numeri primi. Nel caso di funzioni vettoriali su serie, la serie di output può avere lo stesso numero di elementi dell'ingresso, o un numero diverso.
Un esempio del primo caso è l'interpolazione lineare :  viene ritornata una serie che contiene le ordinate della retta interpolatrice in corrispondenza ai valori della prima serie.
Un esempio del secondo caso è la previsione con il metodo Holt Wilters :  viene ritornato un numero di elementi pari a quello della serie di input sommato al numero di periodi di previsione.
In taluni casi, le funzioni vettoriali ritornano, come "effetto collaterale", anche degli scalari. Un esempio è ancora la previsione Holt Winters, in cui vengono ritornati gli indici di bontà della previsione stessa.

## Funzioni implementate
### Funzioni scalari di un numero
Fattoriale (viene calcolato se il numero di input è inferiore a 20, per motivi di overflow)
Attualizzazione di un valore :  dato un montante (valore finale), la data iniziale e finale, e un valore di interesse, viene ritornato il valore attualizzato, che porta al montante, in caso di interesse composto su base annuale.
### Funzioni vettoriali di un numero
Scomposizione in numeri primi (viene calcolato se il numero di input è inferiore a 10000, per motivi implementativi)
### Funzioni scalari di una serie
Numero elementi (1)
Somma
Media
Varianza
Deviazione standard
MAD
MSD
Numero elementi non a zero
Somma elementi non a zero
Media elementi non a zero
Varianza elementi non a zero
Dev. Std elementi non a zero
MAD elementi non a zero
MSD elementi non a zero
Numero elementi senza max e min
Somma elementi senza max e min
Media elementi senza max e min
Varianza elementi senza max e min
Dev. Std elementi senza max e min
MAD elementi senza max e min
MSD elementi senza max e min
Valore massimo
Valore minimo
Numero elementi tra estremi non zero
Somma elementi tra estremi non zero
Media elementi tra estremi non zero
Varianza elementi tra estremi non zero
Dev. Std elementi tra estremi non zero
MAD elementi tra estremi non zero
MSD elementi tra estremi non zero
Posizione primo elemento non a zero
Posizione ultimo elemento non a zero
Mediana
Indicatori di process capability : 
* CP
* CPL
* CPU
* CPK
* CPM
* CPKM

### Funzioni vettoriali di una serie
Ritorno. (1)
Inversione
Ordinamento crescente
Ordinamento decrescente
Cambio segno
Valore assoluto
Statistica Hotelling - In questo caso si passano le N serie di seguito. Il numero di variabili corrisponde al numero delle serie. Si deve passare inoltre, nel valore numerico 1, il numero di elementi di ogni serie e, nel valore numerico 2, il numero di variabili (attualmente è gestito solo il caso di 3 variabili). Il numero di elementi da passare è dato dal prodotto di questi due numeri.
Ad esempio, con le tre serie :  1,3,4,6; 4,2,5,8; 7,8,6,3, si passano i seguenti valori : 
 * Serie di input :  1,3,4,6,4,2,5,6,7,8,6,3
 * N.elementi serie :  12
 * Numeri di input :  4,3
Ritorna una serie di N elementi pari alla lunghezza di ogni serie, (nel caso dell'esempio 4) che costituisce la statistica Hotelling della previsione.
Ritorna anche i seguenti numeri : 
 * n. elementi fuori limite
 * limite della serie

### Funzioni scalari di due serie
Numero elementi (1)
**Regressione lineare**. Viene ritornata una coppia di numeri :  l'ordinata all'origine e il coefficiente angolare della retta interpolatrice la spezzata costituita dalle due serie di input.
**Media ponderata**. Viene ritornata la media della prima serie pesata con i valori della seconda.
**Media ponderata senza nulli**. Vengono esclusi, dalla media ponderata, i valori nulli della prima serie
**Deviazione tra due serie**. Ritorna la radice quadrata del rapporto tra la somma dei quadrati delle differenze tra le due serie e il numero di elementi. E' utilizzata internamente, dal metodo Holt Winter, per stabilire la bontà della previsione, ed è stata quindi resa disponibile per un utilizzo pubblico. C'è da osservare che questa funzione rappresenta un'eccezione alla rappresentazione "geometrica" delle due serie, in quanto prevede che esse siano della stessa natura. Esse devono comunque avere lo stesso numero di elementi.

### Funzioni vettoriali di due serie
Ritorna la prima serie (1)
Ritorna la seconda serie (2)
**Residuo della regressione**. Calcola l'interpolazione e ritorna, per ogni elemento della serie, la differenza tra la prima serie e l'ordinata della retta interpolatrice (2)
**Interpolazione multipla**. Calcola l'interpolazione e ritorna, per ogni elemento della serie, il valore dell'ordinata della retta che interpola la prima serie (2)
**Regressione multipla**. Si deve impostare il numero di elementi della regressione, che è anche il numero degli elementi della serie di output.
**Previsione con metodo Holt Winter (HW)**
Implementa il metodo di previsione della domanda di Holt Winter, E' obbligatorio che le serie di input siano, esplicitamente o implicitamente, a passo unitario.
Devono essere impostati i seguenti dati di input : 

- _2_Periodicità;  se non impostato si assume 12. Non può essere passato il valore 1 (viene ritornato errore)
- _2_Alfa factor (fattore di smorzamento del livello);  si imposta un valore tra 0 e 1.
- _2_Beta factor (fattore di smorzamento del trend);  si imposta un valore tra 0 e 1.
- _2_Gamma factor (fattore di smorzamento della stagionalità);  si imposta un valore tra 0 e 1.

Se si imposta per uno o più di questi fattori un valore maggiore di 1, si attiva l'autofit :  la routine determina i valori ottimi dei fattori, che minimizzano l'indice impostato nel seguito.
Si può decidere di eseguire l'autofit solo su uno dei tre fattori; ad esempio, la seguente impostazione :  Alfa=2; Beta=0,4; Gamma=0,9 indica che si desidera calcolare solo il valore migliore di Alfa.
Attenzione :  è ammesso il valore 0, che fa sì che venga considerato solo il perido iniziale.
Un valore comunemente utilizzato è 0,2 per tutti e tre i coefficienti.
I valori degli indici calcolati, vengono ritornati nei numeri di output della routine.

- _2_N. Periodi futuri di previsione; se non impostato viene assunta la periodicità
- _2_Frontiera, ultimo periodo della serie di input che viene assunto come "passato". La previsione inizia dal periodo successivo. Se non impostato si assume il numero di periodi caricati. Se si imposta un valore superiore, viene ritornato errore.
- _2_N.periodi di storia; numero di elementi della serie di input su cui eseguire la previsione, a partire dalla frontiera a ritroso :  se non impostato si assume il numero periodi della frontiera. Se è maggiore di quest'ultima, e quindi sfonderebbe all'indietro, vengono assunti pari alla frontiera.
Per il metodo HW moltiplicativo devono essere, al minimo, pari a due periodicità, mentre per quello additivo devono essere superiori ad una peridicità. Se questo non accade, viene segnalato errore.
- _2_Mantiene negativi; se impostato, nella serie ricevuta e nella previsione calcolata, vengono mantenuti i valori negativi. Il default è NO :  nella serie di input, prima del calcolo, vengono azzerati i valori negativi, e che, se durante il calcolo della previsione dei periodi futuri, si ottiene un valore negativo, verrà anch'esso azzerato. La previsione che si calcola nel "passato", il cui scopo è di determinare i valori per arrivare alla frontiera, non viene invece mai azzerata.
- _2_N.decimali di arrotondamento; se impostato un valore 0,1,2 o 3, la previsione viene arrotondata a questo valore. Se si imposta un valore diverso, non viene eseguito nessun arrotondamento.
- _2_Autofit senza arretramento; normalmente, per eseguire l'autofit, è necessario disporre di una serie di almeno tre periodicità :  impostando questo valore a 1, diventa sufficiente una serie di sole due periodicità.
- _2_HW moltiplicativo; normalmente è utilizzato il metodo additivo, se si imposta a 1 questo valore, viene utilizzato il metodo moltiplicativo.
- _2_Indice autofit; per determinare i migliori valori dei fattori di smorzamento, si deve scegliere, in questo campo, l'indice da minimizzare : 
-- 0 oppure ' ' (default)  :  Errore %
-- 1  :  Mape
-- 2  :  Errore di interpolazione
- _2_N.periodi iniziali. Il metodo HW additivo, per determinare i valori iniziali di livello e trend, esegue un'interpolazione lineare sui primi elementi della serie. In questo campo si imposta il numero di periodi da trattare. Se non impostato, o impostato un valore maggiore della storia, si assume uguale a una periodicità. Se impostato un valore minore di due, si forza il valore due.

**Risultati**
Viene ritornata una serie con un numero di elementi pari a quello delle serie di input sommato al numero di periodi di previsioni, riempita nei periodi di storia e in quelli di previsione con il valore della previsione calcolata.
Nei periodi di storia viene calcolata una previsione "passata" e viene confrontata con la serie storica, per ottenere indici di scostamento tra le due, che sono una stima dell'attendibilità della previsione "futura".
**Coefficienti Holt Winters (HW)**
Ritorna una serie di N elementi (dove N è tre volte la storia) contenente i coefficienti di livello, trend e stagionalità della sere HW predcedentemente calcolata, per ogni periodo della storia.
Ad esempio, con una storia di 24 periodi, la serie di output contiene : 
* Posizioni 1 - 24  :  livello degli elementi 1 - 24
* Posizioni 25 - 48  :  trend degli elementi 1 - 24
* Posizioni 49 - 72  :  stagionalità degli elementi 1 - 24
NB :  le posizioni partono dall'inizio, e quindi possono non avere esatta corrispondenza con la serie HW. Ad esempio, con una frontiera al periodo 36, ed una storia di 24 periodi, il primo periodo della storia, nella serie HW è il 13, mentre nella presente serie dei coefficienti è il 1.
Vengono ritornati inoltre i seguenti numeri, che sono gli estremi delle tre sottoserie.
* Numero 1 - 1
* Numero 2 - 24
* Numero 3 - 25
* Numero 4 - 48
* Numero 5 - 49
* Numero 6 - 72
**Statistica Hotelling da Holt Winter (HW)**
Questa funzione/metodo va lanciata dopo il calcolo Holt Winters.
Ritorna una serie di N elementi pari alla storia, che costituisce la statistica Hotelling della previsione. Ritorra anche i seguenti numeri : 
 * n. elementi fuori limite
 * limite della serie
**Previsione con metodo interpolazione lineare (IL)**
Implementa il metodo di previsione della domanda determinando la retta che interpola linearmente (con il metodo dei minimi quadrati) l'input, e calcolandone i valori per i punti di previsione. E' obbligatorio che le serie di input siano, esplicitamente o implicitamente, a passo unitario. Devono essere impostati i seguenti dati di input : 
 - Vedi HW. In questo metodo la periodicità non è utilizzatat direttamente. La si inserisce per omogeneità  e per matenere gli stessi defalut di HW. Non viene dato errore se si passa il valore 1.
 - N.S.
 - N.S.
 - N.S.
 - Vedi HW
 - Vedi HW.
 - Vedi HW, con la differerenza che il numero minimo di periodi di storia è due.
 - Vedi HW.
 - Vedi HW
 - N.S.
 - N.S.
 - N.S.
 - N.S.
**Risultati**
Vedi HW
**Differenza tra serie 1 e serie 2**
Ritorna una serie, in cui, in ogni elemento, viene calcolata la differenza tra il valore dello stesso elemento della serie 1 e della serie 2
**Diferenza % tra serie 1 e serie 2**
Ritorna una serie, in cui, in ogni elemento, viene calcolata la differenza tra il valore dello stesso elemento della serie 1 e della serie 2, divisa per il valore della serie 2, il tutto moltiplicato per 100. Se il valore della serie 2 è zero, viene ritornato zero.

**Note** : 
(1) Oltre ad uno scopo didattico, questa funzione può essere utile in caso di caricamento progressivo. Si rimanda alla parte di documentazione tecnica per un'esposizione dettagliata
(2) Vengono ritornati anche, come scalari, l'ordinata all'origine e il coefficiente angolare della retta interpolarice

## Utilizzo della /COPY
### Funzione INZ (inizializzazione)
La si lancia una volta per comunicare che si sta per elaborare una nuova serie, ed il tipo di serie (singolo numero, semplice, doppia, ecc ...); in questa funzione si inizializzano : 
* le schiere interne del programma
* tutti i campi di input
* tutti i campi di output

### Funzione CAR (caricamento)
La si lancia per caricare le serie di input; si passa il numero di elementi :  se non impostato, si assume l'ultimo elemento non vuoto, si può richiamare più volte :  i nuovi dati si accodano ai precedenti; in questa funzione si inizializzano (al ritorno del richiamo) i campi di input passati. La caratterizzazione alfanumerica di ogni elemento della serie è comune alle due serie :  il valore viene messo nella posizione del numero corrispondente, e ricopre il precedente. Nel caricamento alternato si deve impostare, come numero di elementi, il numero di coppie. Ad esempio, se la prima serie è 1,2,3 e la seconda 8,7,6, per passarle con metodo A_12, si passa la serie 1,8,2,7,3,6, ed il numero di elementi 3.

Deve esserci congruenza tra i metodi delle funzioni INZ e CAR

| 
| .COL Cod="A01" Txt="Metodo INZ" LunAut="1" A="L" |
| ---|----|
| 
| .COL Cod="A02" Txt="Metodo CAR" LunAut="1" A="L" |
| - NUM|A_N |
| - SIN|A_1 |
| - DOP|A_1 |
| - DOP|A_2 |
| - DOP|A_12 |
| - DOPUNI|A_1 |
| 

Negli altri casi viene acceso l'indicatore 35 e ritornato il messaggio di incongruenza tra inizializzazione e caricamento.

### Funzione Fxx (esecuzione funzione)
Al primo richiamo si deve SEMPRE pulire il messaggio £G56MS. Anche in questo caso si controlla la congruenza tra la funzione di inizializzazione e di esecuzione.

Deve esserci congruenza tra il metodo della funzione INZ e la funzione di calcolo Fxx

| 
| .COL Cod="A01" Txt="Metodo INZ" LunAut="1" A="L" |
| ---|----|
| 
| .COL Cod="A02" Txt="Funzione Fxx" LunAut="1" A="L" |
| - NUM|F01     F02 |
| - SIN|F03     F04 |
| - DOP|F03 (*) F04 (*) F05  F06 |
| - DOPUNI|F03 (*) F04 (*) F05  F06 |
| 

 (*) :  funzioni eseguite sulla prima serie delle due

Negli altri casi viene acceso l'indicatore 35 e ritornato il messaggio di incongruenza tra inizializzazione ed esecuzione.

Si passano i dati di input specifici della funzione (numeri e e stringa, che vengono puliti dopo il richiamo). Questa impostazione ha l'effetto di inizializzare tutti i campi di output. Se la serie di output non è finita (ha un numero di elementi maggiore di quello della schirea di passaggio) viene tornato il messaggio CONT :  occorre richiamare la routine (con la stessa funzione), lasciando il messaggio CONT. Negli altri casi ritorna il messaggio vuoto. La schiera dei numeri e dei significati (come effetto collaterale di un ritorno di un vettore) viene ritornata tutte le volte. Idem per la stringa di output.

## Descrizione formule utilizzate
 :  : I.INC.MBR Fil(DOC_VOC) Mem(B£MATE_GLO)
