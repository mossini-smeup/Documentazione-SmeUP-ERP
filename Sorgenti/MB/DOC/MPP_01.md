# Generalità
## Introduzione
MPS è uno strumento di ampia versatilità, assimilabile a un foglio elettronico integrato con il sistema gestionale (Clienti, Articoli, Ordini, Giacenze, ecc...) e che permetta di gestire le informazioni riguardanti le previsioni di marketing e gli ordini in corso e di ottenerne un piano generale di produzione, basato su regole definibili in funzione delle esigenze aziendali.

# Oggetti di base
## Piano
### Definizione
Il "piano" è l'elemento fondamentale dell'applicazione e definisce quale orizzonte temporale considerare, inteso come data di partenza e frammentazione dell'orizzonte, ossia quanti giorni, settimane, mesi.
Il numero massimo di periodi definibili nell'orizzonte è 120 e il minimo è 1, per cui si può andare da un piano di 1 giorno a uno di 10 anni.
Il tipo di periodicità è tabellato nella tabella A£Q .
In sintesi, possiamo dire che definire il piano (elemento della tabella MPP) equivale a disegnare sulla linea dell'orizzonte una serie di tacche per delimitare l'inizio del primo periodo e di ogni successivo
periodo. A questo punto possiamo dire che le cose che ci interessano troveranno un riscontro all'interno dei periodi così definiti.
Di fatto non abbiamo ancora detto "cosa" ci interessa, quale dato vogliamo gestire nel "piano" e per farlo dobbiamo definire le "viste".

![MP_001_05](http://localhost:3000/immagini/MPP_01/MP_001_05.png)
## Vista
### Definizione
La "vista" è ciò che stiamo trattando, ossia il set di dati che ci interessa gestire.
Quindi, possiamo avere la vista delle previsioni per cliente, del venduto per cliente, del consegnato per fornitore, del prodotto per articolo, ecc...
Tutte le viste possono appartenere a qualsiasi piano e, in effetti, esse rappresentano una "visione" particolare dei dati del piano.
La vista si definisce nella tabella MPC, in cui è possibile definirne le chiavi.
Esse possono essere una o due e sono oggetti applicativi, ossia appartenenti alla tabella *CNTT.

![MP_001_04](http://localhost:3000/immagini/MPP_01/MP_001_04.png)
>N.B.** :  **la Vista di seguito riportata ha la gestione dei dati decimali impostata. Questo significa che in visualizzazione dei dati si vede un decimale. Tuttavia, anche le viste che non hanno la gestione dati decimali impostata hanno i dati registrati con la parte decimale (2 posizioni), ma non viene visualizzata.

![MP_001_01](http://localhost:3000/immagini/MPP_01/MP_001_01.png)
# Periodicità
## Frazionamento periodi
La periodicità è la possibilità di "mettere le tacche sulla linea del tempo", ossia di definire come devono essere intestate le colonne del nostro piano.
Naturalmente è un elemento di tabella (MPC) che mostriamo qui di seguito con un esempio.

![MP_001_02](http://localhost:3000/immagini/MPP_01/MP_001_02.png)
**In questo elemento di tabella MPC, si è deciso di costruire una periodicità di 20 giorni, 13 settimane e 9 mesi, quindi il piano avrà 20+13+9 = 42 colonne (periodi). È importante notare che, se la data di inizio piano è un lunedì e la settimana tipica della risorsa CDL ** è di 5 giorni (dal lunedì al venerdì), i primi venti giorni del piano saranno esattamente le prime 4 settimane, per cui la costruzione del 21° periodo sarà una settimana esatta. Se invece la giornata di inizio piano fosse un mercoledì, allora la costruzione del 21° periodo dipenderebbe dal contenuto del campo "Flag giorni".
Se in quest'ultimo è contenuto il valore "-", allora vengono cancellati gli ultimi periodi fino a saldarsi con un possibile inizio settimana (il primo giorno lavorativo della settimana della risorsa CDL **).
Quindi, nel caso in considerazione, sarebbero cancellati il martedì e il lunedì ultimi, proponendo un periodo settimanale che comicia di lunedì. Se invece il contenuto di "Flag giorni" è "+", allora verranno aggiunti periodi giornalieri fino a saldarsi con un inizio settimana :  sarebbero aggiunti il mercoledì, il giovedì e il venerdì. Se nel campo "Flag giorni" c'è un Blank, per default il programma di costruzione periodi si comporta come se ci fosse un "+". Analogamente, vengono trattati il "Flag settimane" e il "Flag mesi" (in questo caso si salda sull'anno), risolvendo il problema delle saldature tra periodi di diversa unità di misura.

# Raggruppamenti di periodi
È possibile, nell'analisi di un piano (sia in visualizzazione che in stampa), raggruppare i periodi di un piano per ottenerne una vista sintetica nel tempo, in cui le quantità raggruppate vengano sommate.
Questa funzione è richiamabile dalla gestione dei dati di un piano mediante il comando F18 = sintesi, che mostra la seguente finestra, in cui è possibile definire con "I" l'inizio raggruppamento, con "F" la fine e con "X" i periodi esclusi dal raggruppamento.

![MP_001_03](http://localhost:3000/immagini/MPP_01/MP_001_03.png)
# Altri oggetti utilizzati
## Periodi predefiniti
Naturalmente è possibile predefinire dei raggruppamenti e registrarli nella memorizzazione multipla.

## Calendari
Vedere il documento specifico per il calendario :  "Calendario"

- [Calendario](Sorgenti/MB/DOC/B£CALE)

# Flussi di pianificazione
## Creazione sequenze di funzioni
Il processo di pianificazione di ogni azienda è diverso e pertanto in MPS si trova la possibilità di costruire uno o più flussi di azioni.
Le azioni elementari, che possono essere utilizzate per creare sequenze in flussi (un flusso è un elemento della tabella B£H) sono contenute nella voce 13 del menu iniziale di plan-up (MP00).
Queste azioni sono ovviamente parametrizzabili una volta inserite nei flussi e sono essenzialmente di 4 tipi : 

### 1) Azioni di ingresso da altre funzioni
Queste azioni caricano nelle viste del piano informazioni provenienti da altri archivi :  per esempio la disponibilità delle risorse è ripresa dalla gestione del calendario, il residuo ordini di vendita è ripreso
dai documenti esterni, come il fatturato o gli ordini di produzione. Elenchiamo qui di seguito le azioni possibili e i loro dettagli di parametrizzazione : 

>RIPRESE
- Da calendario
- Da calendario partendo da vista
- Da carico risorse interne
- Da carico risorse esterne
- Da ordini rilasciati
- Da documenti ciclo esterno
- Da fatture ciclo esterno
- Da altro Piano/Vista
- Da analisi disponibilità
- Da movimenti di magazzino
- Da piani diversi in base a data *

### 2) Azioni di creazione /cancellazione piani
Queste azioni creano i piani, li cancellano o li stampano.
Elenchiamo qui di seguito le azioni possibili e i loro dettagli di parametrizzazione : 

>Cancellazione piano/vista piano
Definizione piano
Stampa piano/viste batch
Cancellazione piani precedenti
Cancellazione piano con limiti
Operazioni su due viste

### 3) Azioni di Riga di piano (singolo record)
Queste azioni trasformano le informazioni contenute nelle viste utilizzando le strutture del sistema informativo come le distinte, i cicli, i parametri, i costi, le sintesi, le giacenze, le fonti, ecc...
Elenchiamo qui di seguito le azioni possibili ed i loro dettagli di parametrizzazione : 

>Totalizzazione di una vista
Creazione sintesi
Valorizzazione di una vista
Adeguamento dettaglio al totale
Attribuz. parametri a una vista
Copert. in per. di vis. risp. or.
Esplosione distinta
Espl. distinta con nettificazione
Esplosione ciclo
Nettificazione giacenza
Nettificazione gruppo fonti
Emissione suggerimenti
Esplosione risorse
Carico risorse a capacità finita
Elaborazione MRP

### Azioni di trasformazione dati
Queste azioni hanno la caratteristica di poter essere applicate anche solo a un record del piano (singola riga). Elenchiamo qui di seguito le azioni possibili ed i loro dettagli di parametrizzazione : 

>Ricerca guidata
Confronto fra righe di un piano
Gestione
Manutenzione dei dati

### Funzioni su una riga del piano
 * Analisi grafica del contenuto
 * Trasferimento a foglio elettronico
 * Gestione
 * Analisi grafica
 * Confronto con altre righe
 * Selezione delle righe di piano secondo criteri di valore
 ** Compresi tra limiti
 * Selezione secondo criteri di sequenze di valori
 * Analisi grafica valori di una riga
 * Analisi statistica dei valori
 ** medie
 ** deviazioni
 ** massimi e minimi
 * Analisi di singole righe dei piani
 ** Con viste collegate
 ** Confrontate algebricamente con altre viste
 * Totalizzazione per riga/colonna
 * Verifica delle capacità aziendali
 * Risorse primarie
 ** carico macchine
 ** carico uomini
 ** Fabbisogni materiali
 * Risorse secondarie
 ** volumi
 ** contenitori
 ** mezzi di trasporto
 ** energia
 ** materiali di consumo
 ** attrezzi

# Stampa piani
La stampa del piano permette di stampare le viste piano singolarmente, oppure confrontate con una o diverse altre, applicando anche un operatore di confronto.
La stampa permette l'impostazione di diverse opzioni, che possono essere memorizzate singolarmente e anche come gruppo.

Queste opzioni sono : 

- **Tipo stampa** : 
-- Vista singola
-- Confronto con altra vista (nella finestra della vista da stampare compare anche la scelta del piano e della vista di riferimento, con l'operatore logico da utilizzare per il confronto. Inoltre c'è la possibilità di escludere dalla stampa una vista, mettendo la X nella colonna Esclude Stampa. I record stampati sono quelli della vista campione, a meno che si imposti la X in Tutti i record.)
-- Dettaglio viste collegate (esiste la possibilità di scegliere anche le viste da confrontare con quella scelta come vista campione. L'ordine di stampa è quello della lista, a meno che in ORDINAMENTO ne sia stato impostato un altro.)

- **Sintesi** :  se definita la vista, compaiono le sintesi selezionabili per le 2 chiavi. Esse saranno visibili nell'ordinamento.

- **Ordinamento** :  permette di scegliere ordinamenti dipendenti dai valori del tracciato della vista piano.
Essi possono essere ascendenti o discendenti ed è possibile scegliere come caratterizzare la rottura di codice (se infilandoci una riga bianca, stampando il codice e la decodifica, oppure inserendo trattini ===, casi che possono anche essere scelti con la stampa dei totali parziali).

- **Parzializzazioni** :  permette di scegliere le righe da stampare, parzializzando per valori dei codici chiave della vista, per valori delle sintesi dei codici, o addirittura per i valori dei periodi del piano. In questo caso si può scegliere anche la possibilità di stampare solo le righe del piano con un certo set di valori in un numero di periodi (contigui e non). Queste opzioni risultano particolarmente utili, as esempio, quando si vuole stampare il piano di produzione solo degli articoli con qualcosa da produrre entro la prima settimana o due.

- **Schema Informazioni** :  con questa opzione si scelgono le colonne da stampare, quanti caratteri e quali attributi dare ad ogni colonna, ecc...
Le scelte operate sono salvate in uno schema, che è un elemento (T1, T2, T3, T4, T5) della tabella INT, sottosettore Mx. Per ogni sottosettore possono essere definiti al massimo 5 schemi :  se ne servono di più, devono essere definiti.

- **Valori** :  con questa opzione si sceglie di stampare, cumulare valori periodici, oppure valorizzarne la vista mentre la si stampa, col tipo costo desiderato, al livello voluto ed eventualmente con un fattore di correzione.

- **Totali** :  permette di inserire delle colonne di totali (in orizzontale) a rottura di Mese, Trimestre, Anno, oppure come generale alla fine dei periodi.

- **Forma** :  permette di stampare solo i totali, i sottototali (2 chiave dell'ordinamento) o tutto del primo ordinamento.

- **Periodi** :  malgrado la periodicità definita del piano, possono essere scelte delle riaggregazioni dei periodi specificate in questa opzione, inserendo nella colonna di sinistra della finestra periodi aperta (mettere / su raggruppamento), >I e >F dove iniziano e finiscono i raggruppamenti. Sui periodi inalterati bisogna confermare una X.

- **Colonne** :  definisce il modo in cui si desiderano vedere intestate le colonne.

