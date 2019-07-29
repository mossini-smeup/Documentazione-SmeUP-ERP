# Contenuti principali della versione V3R2
Per tutti i moduli citati nei capitoli seguenti sono state create delle nuove schede che seguono una impostazione di tipo standard basata sui seguenti criteri : 
* entrata su scheda cruscotto, che generalmente mostra una matrice delle sottoclassi presenti nel modulo
* scegliendo una sottoclasse si attiva il filtro dati che mostra il cruscotto di quella sottoclasse, generalmente la matrice con le istanze attive (es. lotti da collaudare)
* sezione di scheda a sinistra, che mostra le azioni del modulo
* passaggio alla scheda delle singole istanze
Le schede delle singole istanze (es. Lotto, Non conformità, richieste di intervento), mostrano le seguenti caratteristiche standard : 
* sezione di sinistra con le azioni eseguibili sulla singola istanza
* piede di scheda con due sezioni : 
** una per note con evidenziazione di presenza
** una per la cartella dell'istanza, con eventuale creazione della cartella e possibilità di trascinamento/aggancio di file eterogenei
* sezioni centrali ( 2, 3 o 4) con i dati principali dell'istanza ben evidenziati
* sezione di destra con diversi bottoni funzionali per le azioni più frequenti

Qui di seguito citiamo invece i contenuti applicativi innovativi dei moduli toccati dalla versione V3R2

## Modulo CQLOTT :  gestione lotti
La scheda del lotto permette di navigare su tutte le registrazioni che hanno come origine il lotto : 
* ciclo di collaudo
* non conformità
* rilievi di collaudo
![CQBASE_023](http://localhost:3000/immagini/CQBASE_11/CQBASE_023.png)
- workflow :  questa analisi raggruppa tutti i workflow generati direttamente o indirettamente da questo lotto, permettendo di vedere tutte le attività / problemi legati al lotto. In questo modo si evidenziano subito i problemi che il lotto ha avuto e le soluzioni adottate

![CQBASE_029](http://localhost:3000/immagini/CQBASE_11/CQBASE_029.png)
## Modulo CQNCOG :  gestione non conformità per oggetto
Nel modulo delle non conformità spicca il cruscotto che si apre con una analisi di pareto per codice difetto e per ente rilevatore delle non conformità.

![CQBASE_024](http://localhost:3000/immagini/CQBASE_11/CQBASE_024.png)
La scheda della singola Non conformità permette di ottenere immediatamente la stampa PDF in modalità 8D del "problema" :  questa stampa infatti elenca i passi di analisi/soluzione prescritti dalla disciplina 8D (riferirsi a wikipedia per comprensione dell'approccio 8D).

![CQBASE_027](http://localhost:3000/immagini/CQBASE_11/CQBASE_027.png)
Altra importante novità è la definizione di un workflow di gestione delle non conformità, che prevede il collegamento automatico alle azioni correttive. In altre parole il "problema" viene descritto da un inserimento della non conformità, seguito dalla generazione delle richieste di intervento in modalità 8D (azioni di contenimento, individuazione delle cause, prevenire il ripetersi, ecc...).
La chiusura della non conformità avviene automaticamente allorchè l'ultima richiesta di intervento collegata alla non conformità viene chiusa.

![CQBASE_028](http://localhost:3000/immagini/CQBASE_11/CQBASE_028.png)
## Modulo CQRDI2 :  gestione richieste di intervento
Il modulo delle richieste di intervento è arricchito dalla definizione del workflow di gestione della richieste. L'attivazione del workflow permette naturalmente di tracciare le attività eseguite a seguito del workflow, in modo da sapere chi ha fatto cosa, in che tempi e con quali ritardi.

## Modulo CQCC02 :  cicli di collaudo per oggetto
La nuova scheda dei cicli di collaudo permette di analizzare immediatamente il contenuto dell'operazione di collaudo.

![CQBASE_018](http://localhost:3000/immagini/CQBASE_11/CQBASE_018.png)
Come si vede, oltre alla rappresentazione del documento collegato alla fase di ciclo, vengono evidenziati i risultati dell'ultima misurazione eseguita.
Inoltre è possibile rappresentare, sia sotto forma di Gaussiana che di carta X-R, le ultime rilevazioni ottenute su questa fase di ciclo.

_Distribuzione gaussiana delle misurazioni_
![CQBASE_022](http://localhost:3000/immagini/CQBASE_11/CQBASE_022.png)

_Rappresentazione X-R delle stesse_
![CQBASE_030](http://localhost:3000/immagini/CQBASE_11/CQBASE_030.png)
## Modulo CQRICO :  gestione dei rilievi dei collaudi
I controlli per variabili (che producono quindi dei numeri) generano delle serie numeriche che sono analizzate dalla nuova routine statistica B£G56. La G56 è in grado di produrre degli indicatori delle serie numeriche in accordo alle indicazioni di controllo di processo (SPC) generalmente richieste. Infatti otteniamo i seguenti indicatori : 

* Media
* Deviazione Std
* Valore MAX
* Valore MIN
* Num campioni
* CP, CPL, CPU, CPK, CPM, CPKM

Il cui significato è descritto in wikipedia

![CQBASE_019](http://localhost:3000/immagini/CQBASE_11/CQBASE_019.png)
## Modulo CQACMC :  gestione strumenti di misura
Creata la scheda che permette di analizzare velocemente il parco strumenti, per categoria, evidenziando gli strumenti in scadenza di taratura
![CQBASE_017](http://localhost:3000/immagini/CQBASE_11/CQBASE_017.png)
## Modulo CQDOCU :  gestione documenti
Oltre alla scheda di consultazione dei documenti, che mostra in prima battuta quelli rilasciati e poi lascia indagare sul portafoglio totale dei documenti, bisogna segnalare che la modalità di reperimento dell'ultimo livello di modifica del documento è stata completamente cambiata. Adesso è possibile legare un documento a un oggetto tramite il suo identificativo (numero documento). Al momento di consultare / visualizzare quel documento, il programma ricerca a parità di chiavi (fino a 3 chiavi, ossia tutta la griglia) se esiste un altro documento dello stesso tipo con livello di modifica più alto e rilasciato. Se lo trova, visualizza quello. Questo permette di avere sempre aggiornata la consultazione dei documenti senza dover modificare i record che li agganciano (ciclo di collaudo, FMEA, RDIN, ecc...).
Nella precedente versione il comportamento era analogo, ma aveva due limitazioni : 
* l'aggancio ai record avveniva registrando la chiave del documento, quindi due tipi documenti diversi con la stessa chiave non erano distinguibili
* la ricerca dell'ultimo livello di modifica rilasciato avveniva solo con una chiave, rendendo inutili i documenti con più chiavi.

## Modulo CQVEND :  vendor rating
La nuova scheda del vendor rating permette una consultazione efficace dei trend di comportamento, evidenziando gli indici sintetici per diversi enti, oltre al trend nei periodi dell'ente focalizzato e al dettaglio del periodo prescelto.

![CQBASE_020](http://localhost:3000/immagini/CQBASE_11/CQBASE_020.png)
Inoltre è possibile ottenere una stampa PDF del rating di un ente prescelto, che compone l'andamento sintetico degli ultimi 4 periodi e il dettaglio dell'ultimo periodo.

![CQBASE_026](http://localhost:3000/immagini/CQBASE_11/CQBASE_026.png)
Nell'ambiente modello (i template di smeup) sono stati preparati sia gli indici sintetici per il fornitore che quello dei clienti, dove indici contabili e di servizio si compongono.

## Modulo CQFMEA :  Failure Mode Effect Analysis
La nuova scheda permette una immediata evidenziazione delle FMEA aperte e delle criticità di ogni FMEA, come da immagine sottostante

![CQBASE_021](http://localhost:3000/immagini/CQBASE_11/CQBASE_021.png)
## Modulo CQPDCA :  gestione piani di campionamento
La scheda dei piani di campionamento, tramite l'esposizione in matrice delle varie condizioni statistiche, permette una rapida comprensione delle condizioni di campionamento

![CQBASE_025](http://localhost:3000/immagini/CQBASE_11/CQBASE_025.png)
