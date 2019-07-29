# Generalità

Il componente albero è utilizzabile in ambiente device, sia come sezione "TRE" che come sezione "ACC".

La sintassi di definizione è la medesima prevista per l'utilizzo del componente sul client loocup. Rispetto a quello che si può fare sul client, vigono però varie limitazioni ed alcune peculiarità, che vengono a seguire descritte.

# Attributi

A seguire, verranno evidenziate i principali attributi che possono essere sfruttati anche per il device mobile. Per gli attributi assenti si può assumere che questi non siano supportati e vengano quindi ignorati.

* RowHeight (Altezza righe) :  in ambiente mobile, risulta di particolare importanza, in quanto permette di aumentare/diminuire in modo sensibile, il numero di elementi presenti contemporaneamente su una schermata.
* NodeText (Testo del Nodo) :  è possibile sfruttare tutti valori previsti per l'attributo (al fine di visualizzare solo il codice, solo il testo o entrambi).
* CellStyle (Stile Celle) :  è un attributo tipico del device mobile. Tale attributo è principalmente utile sul componente matrice, dove permette di vedere visualizzare in vario modo le celle della matrice, mentre può risultare utile sull'albero per attivare o meno la visualizzazione delle icone. In questo senso risultano quindi di particolare rilevanza i cellstyle "LS03|PS03" (senza icona) e "LS05|PS05" (con icona).

 :  : DEC T(VO) P(L_EDT_SCH) K(CellStyle) L(1)

# Icone

L'attivazione delle icone, come anticipato al punto precedente, a differenza di quanto avviene sul client loocup è pilotata attraverso l'utilizzo dell'attributo cellstyle.
Viceversa come per il client loocup, l'immagine dell'icona viene reperita controllando l'attributo specifico "i" o a partire dall'oggetto 1 del singolo nodo.

# Alberi multilivello

Gli alberi multilivello sono gestiti, ma a differenza di quello che avviene sul client loocup ogni livello corrisponde ad una differente videata. Es. prendendo questa struttura : 
* titolo 1
** azione 1
** azione 2
** azione 3
* titolo 2
** azione 4
** azione 5
Sul client loocup, l'intera struttura sarà interamente visibile all'interno della sezione, viceversa in ambiente mobile in verrà presentata una sezione in cui saranno presenti solo i titoli, e solo al click su uno dei due titoli verranno presentate le corrispondenti azioni : 
Vedrò quindi una situazione del genere : 
* titolo 1 >
* titolo 2 >
Al click su titolo 1 verrà presentata la videata (che copre la precedente) con i livelli successivi : 
* < titolo 1
** azione 1 >
** azione 2 >
** azione 3 >

# Paginazione

Non è gestita, ma nel caso il servizio, mandi l'xml previsto per l'indicazione della presenza di ulteriori pagine, nella videata verrà apposta l'indicazione che il risultato della funzione non è completo.

# Variabili e Dinamismi

Sono disponibili tutte le variabili comunemente utilizzabili sul client loocup (es. T1, P1, K1, Tx, Fu) che possono poi essere implementate per l'applicazione di dinamismi.

Come tutte le sezioni, il dinanismo applicazione ad un evento può essere unico, e gli eventi sono limitati When="Change" e When="Click".

