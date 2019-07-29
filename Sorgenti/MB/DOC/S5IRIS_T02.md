
#  Prerequisiti
La schedulazione,  dato che si propone come obiettivo il miglior utilizzo delle risorse della fabbrica sulla base degli ordini produzione (Job) rilasciati dalla programmazione,  richiede che i Job siano completamente descritti a livello del ciclo produttivo( risorse, tempi lavorazione, setup, etc..).
Nel seguito descriviamo i dati di base necessari(risorse, cicli lavorazione ed ordini di produzione) per trattare dal punto di vista pratico la schedulazione o programmazione operativa.


##  Risorse
       Le risorse principali sono i centri di lavoro in cui risiede la capacità di fare una lavorazione.
       La macchina è il centro su cui fisicamente viene eseguita la lavorazione , il centro di lavoro è un insieme di macchine "indistinguibili"  per le quali a parità di operazione i tempi di esecuzione sono i
      medesimi.  Se la macchina coincide con il centro di lavoro stesso possiamo schedulare i centri di lavoro  oppure codificare una macchina per ogni centro di lavoro.
       Definiti i centri di lavorazione dobbiamo capire quali sono da schedulare a capacità finita,  quali schedulare a capacità infinita e quelli da escludere dalla schedulazione.
       Generalmente sono schedulati a capacità finita solamente i centri di lavoro che sono  "critici" per l'attraversamento del ciclo produttivo. Definiamo come critico il centro di
       lavoro la cui disponibilità è determinante per la definizione della data di fine dell'ordine  di produzione. Un centro di lavoro schedulato a capacità infinita è un centro in cui
       l'operazione non rimane in attesa di essere processato e pertanto la durata della fase è data dalle ore di carico. Un centro di lavoro non schedulato è un centro in cui la coda ed
       tempi di esecuzione sono insignificanti in questo caso definiamo i tempi di lavorazione solo per la costificazione del prodotto a standard o per analisi di efficienza del centro di lavoro .
       Il tipo di schedulazione viene impostato nella tabella BRM che definisce il gruppo risorsa a cui appartiene il centro di lavoro.
       Dato un centro di lavoro  è possibile descrivere  una coda di attesa o attraversamento  materiale. In tabella BRM possiamo  descriverere se la coda è in giorni oppure ore, se considerata come tempo         di attesa o tempo di attraversamento.
       Normalmente i centri di lavoro esterni sono trattati a capacità infinita e la coda è definita come tempo di attraversamento.
## Calendario
       Il calendario è il luogo in cui descriviamo la capacità oraria della risorsa di eseguire un task. Come minimo dobbiamo definire il calendari annuale ed iul calendario settimanale della risorsa. E 'possibile        gestire risalite ad entità di aggregazione a livello superiore come eccezioni specifiche fino a livello della singola macchina.
##  Operazione di Base
       L'operazione di base è il tipo di lavorazione che viene eseguito su una macchina, ad esempio tornitura, barenatura, tempra, sbavatura, etc... .L'operazione o Task non è istanziata sull'oggetto (articolo, ordine produzione,etc..) ma definisce le caratteristiche principali che poi verranno ereditate dalla fase di lavorazione.
##  Cicli lavorazione
       Il Ciclo di lavorazione definisce i task che devono essere processati in una sequenza logica  per fare in modo che un Job sia completato. Il ciclo di lavorazione contiene le informazioni fondamentali all'attuazione della schedulazione che possiamo riepilogare nel seguente elenco : 
  *Centro Lavoro
 *Tempo di lavorazione
 *Tempo Attrezzaggio
 *Tempo attesa precedente o successivo
 *Coda
 *Risorse Secondarie
## Ordini di produzione
La schedulazione schedula gli impegni degli ordini di produzione che devono come minimo contenere l'indicazione di un articolo, la data di fine richiesta e la priorità.


