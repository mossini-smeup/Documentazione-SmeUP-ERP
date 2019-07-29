
# La natura dei documenti

Per agevolare la consultazione di tutti i documenti che vengono normalmente gestiti in azienda, si è pensato di introdurre il concetto di NATURA DOCUMENTO, ovvero un'informazione aggiuntiva del tipo documento che permette di organizzare i documenti in macro categorie. Volendo riassumere i criteri secondo cui i documenti possono essere ordinati, si ha che, dopo la distinzione generale tra ciclo passivo e ciclo attivo, la natura è di fatto il concetto più generale di raggruppamento. A questa seguono poi il tipo documento (ovvero l'elemento di tabella V5D), il modello, il tipo modello, etc.

*********************************
In questo contesto, è bene fare una precisazione. Ricordiamo infatti che, con ciclo attivo si intende l'insieme di tutte le operazioni che l'azienda intrattiene verso terzi, generalmente clienti, e che le permettono di generare dei guadagni; rientrano quindi nel ciclo attivo tutte quelle attività e documenti che permetto all'azienda di vendere i suoi prodotti e servizi.
Con ciclo passivo si intende l'insieme delle attività che l'azienda intrattiene con i suoi fornitori e che generano tipicamente delle uscite finanziarie.
*********************************

A oggi le nature documento che sono state definite sono : 

A         Offerta/Preventivo Ciclo attivo
B         Ordine Aperto/Contratto Ciclo attivo
C         Ordine Ciclo attivo
D         Documento Sped/Ric/Fatt Ciclo attivo
E         Altri documenti Ciclo attivo

1         Richiesta di acquisto
2         Richiesta d'offerta (SV)
3         Ordine Aperto/Contratto Ciclo passivo
4         Ordine Ciclo passivo
5         Documento Sped/Ric/Fatt Ciclo passivo
6         Altri documenti Ciclo passivo

Come si potrà intuire già da questo elenco, l'utilizzo delle lettere e dei numeri non è casuale, ma dipende dal ciclo gestionale aziendale cui la natura fa riferimento :  le lettere per le nature dei documenti del ciclo attivo e i numeri per quelli del ciclo passivo.


# La natura dei documenti e i nuovi moduli V5

In corrispondenza di ogni natura è stato ideato un nuovo modulo all'interno dell'applicazione V5.
A ciascun modulo è stata associata un'icona identificativa che avrà uno sfondo rosso se la natura appartiene al ciclo passivo, verde se al ciclo attivo. Ecco un esempio : 

![V5_001](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_001.png)
I moduli che sono stati creati per agevolare le navigazioni sono stati denominati in modo da richiamare, all'interno del nome stesso, la natura che lo contraddistingue. La natura coincide con l'ultima lettera del modulo radice.

**Ciclo attivo : **
V5DOCUA per i documenti di natura A
V5DOCUB per i documenti di natura B
V5DOCUC per i documenti di natura C
V5SPRID per i documenti relativi a spedizioni e ricevimenti di natura D
V5DOCUE per i documenti di natura E

**Ciclo passivo : **
V5RIDA1 per i documenti relativi a richieste di acquisto di natura 1
V5DOCU2 per i documenti di natura 2
V5DOCU3 per i documenti di natura 3
V5DOCU4 per i documenti di natura 4
V5SPRI5 per i documenti relativi a spedizioni e ricevimenti di natura 5
V5DOCU6 per i documenti di natura 6

Come si diceva all'inizio, all'interno di ciascun modulo è possibile consultare tutti i documenti, anche di tipologie diverse, che hanno però la stessa natura. La natura del documento è quindi un'informazione obbligatoria che deve essere aggiunta in tabelle V5D.

![V5_002](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_002.png)
Una volta che si è scelto un modulo, il doppio click del mouse permette di accedere al suo dashboard, ovvero una scheda puramente statistica che permette di visualizzare, a parità di natura, il numero di documenti presenti nel sistema, suddivisi per tipologia. A seconda della forma di presentazione impostata nella sezione dei filtri, è possibile vedere queste stesse informazioni raggruppate per stato o per modello documento.
Può succedere che, al primo ingresso, l'utente si trovi davanti a una videata con il riepilogo di tutti i tipi documento della natura cui fa riferimento il modulo. Questa è la videata che permette di impostare il tipo documento che si intende consultare. In ogni momento della navigazione, questa videata è richiamabile dalla voce di menù CAMBIO DOCUMENTO presente nella sezione di sinistra.

![V5_003](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_003.png)
Il dashboard del modulo è strutturato in tre sezioni :  una verticale di sinistra che riporta l'elenco delle azioni e delle navigazioni importanti del modulo, e due orizzontali sulla destra. La prima in alto studiata per impostare i filtri per la consultazione dei dati e la seconda per la visualizzazione dei risultati.

![V5_004](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_004.png)
In ciascun modulo è possibile controllare la situazione complessiva dei documenti accedendo direttamente alla sezione 'Situazione parametri modulo' che permette di vedere, raggruppate per natura, quali tipologie di documento sono utilizzate nel sistema.

Presenteremo ora alcuni esempi di navigazione facendo riferimento a un modulo del ciclo attivo legato ai documenti generici e uno legato invece alle spedizione/ricevimenti, rispettivamente il modulo V5DOCUC e V5SPRID.

# V5DOCUC Ordini di vendita :  Natura C

![V5_005](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_005.png)
La natura C identifica tutti quei documenti che rientrano nel ciclo attivo e che normalmente generano un flusso finanziario positivo per l'azienda. All'interno di questo modulo trovano posto infatti tutti i documenti che possono essere classificati in 'Ordini di vendita'. La scheda del modulo, chiamata anche DASHBOARD, si presenta con l'ormai nota struttura a tre sezioni : 

1. La parte di sinistra, con le azioni di menù e le navigazioni che possono riguardare gli ordini del ciclo attivo.
2. La parte alta di destra, adibita all'inserimento dei filtri per le navigazioni.
3. La parte centrale, sempre a destra, in cui verranno caricati i risultati delle ricerche.

Data la struttura dei documenti V5, all'interno di questi moduli è possibile scegliere di navigare o a partire dalle testate dei documenti o dalle relative righe. A questo proposito sono stati ideati dei SURF specifici :  il primo per le testate (A DOCUMENTO) e il secondo per le righe (B RIGHE DOCUMENTO).

![V5_006](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_006.png)
Sia che si scelga un SURF del gruppo delle testate o un SURF del gruppo delle righe, le modalità per eseguire le ricerche sono fondamentalmente le stesse. L'unica cosa che cambia sarà la parte relativa ai filtri dal momento che, a seconda del SURF specifico, conterranno alcuni campi piuttosto che altri. Illustreremo come esempio un surf di testata e uno di riga.

## A) Il surf di testata per numero documento

Scegliendo di partire dal surf per numero documento delle testate, la sezione dei filtri offre la possibilità di impostare alcuni campi come per esempio : 
** __Posizionamento numero documento : __ inserendo in questo campo un numero di documento la scheda permette di visualizzare tutti i documenti antecedenti o successivi a questo, a seconda di quanto impostato nel campo A/D dell'ordinamento (ascendente o discendente). A differenza di tutti gli altri campi che fungono da filtri puntuali, questo campo serve solo a porre un limite alla ricerca.
** __Flag Righe : __ se impostato, questo flag permette di visualizzare per ciascuna testata, le relative righe, dove ovviamente presenti. La presenza di queste è manifestata da una piccola icona a forma di lente che viene caricata in corrispondenza delle testate, nella prima colonna della matrice. Solo cliccando su questa icona sarà possibile vedere il dettaglio nella parte inferiore della scheda.

![V5_007](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_007.png)
Se si sceglie di non visualizzare la sezione delle righe nella parte inferiore della scheda, è comunque possibile accedere alla loro consultazione grazie alla voce di menù 'Righe' presente nel popup caricabile cliccando sull'icona funzionale accanto a ogni numero di documento.

![V5_008](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_008.png)
## B) Il surf di riga per numero documento

È un surf che permette di visionare, dato un documento, tutte le sue righe.
La navigazione è stata studiata per consentire di visualizzare, attraverso l'impostazione del flag 'Limite' anche i documenti successivi o precedenti a quello inserito giocando con l'ordinamento A/D (ascendente o discendente). Nel caso in cui si decida una navigazione multi documento con questo flag, le righe verranno già presentate a video raggruppate per numero.
Ecco quindi la visualizzazione senza il flag limite : 
![V5_009](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_009.png)e il risultato dell'estrazione con il flag limite impostato :  in questo caso la consultazione dei dati è agevolata dal raggruppamento per numero documento.
![V5_010](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_010.png)
Per usare al meglio i filtri che sono stati predisposti e per capirne anche il funzionamento, è stato creato un aiuto contestuale attivabile con il tasto funzionale F1. Il suo funzionamento è semplice :  occorre semplicemente posizionare il cursore in corrispondenza del filtro di cui si vuole visualizzare la documentazione. A questo punto, è possibile premere F1 e attendere il caricamento della descrizione che illustra lo scopo, le finalità e le modalità di utilizzo dei campi filtro.

# Spedizione/ricevimenti vendita - Natura D

La natura D identifica tutti quei documenti relativi alla spedizione e ricevimento della merce del ciclo attivo. La scheda del modulo si presenta strutturata come già per il V5DOCUC nelle tre sezioni base : 
1. La parte di sinistra, con le azioni di menù e le navigazioni che possono riguardare gli ordini del ciclo attivo.
2. La parte alta di destra, adibita all'inserimento dei filtri per le navigazioni.
3. La parte centrale, sempre a destra, in cui verranno caricati i risultati delle ricerche.

Le impostazioni di questo modulo sono le stesse del modulo precedente. Anche qui infatti è possibile trovare delle navigazioni specifiche sia per le testate che per le righe.
Il primo SURF è per le testate (A  DOCUMENTO) e il secondo per le righe (B RIGHE DOCUMENTO).

![V5_011](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_011.png)
Sia che si scelga un SURF del gruppo delle testate o un SURF del gruppo delle righe, le modalità per eseguire le ricerche sono fondamentalmente le stesse. L'unica cosa che cambia sarà la parte relativa ai filtri dal momento che, a seconda del SURF specifico, conterranno alcuni campi piuttosto che altri. Illustreremo come esempio un surf di testata specifico per questo modulo.
Una precisazione :  quanto verrà detto in corrispondenza del SURF per DDT, varrà anche per il SURF per fattura.

## A) Il surf di testata per numero DDT
![V5_012](http://localhost:3000/immagini/MBDOC_OPE-V5DOCU_01/V5_012.png)Scegliendo di partire dal surf per numero DDT delle testate, la sezione dei filtri impone che venga impostato l'anno di emissione del DDT nell'apposito campo, e all'occorrenza anche il numero del DDT.
Impostati questi filtri, la scheda permette di visualizzare l'elenco dei documenti cui è associato quello specifico DDT.
Come per tutti i surf di testata, anche in questo caso è possibile impostare un tipo di navigazione che consente di vedere immediatamente le righe di un documento nella stessa schermata attraverso la lente di ingrandimento che è l'icona che permette di individuare la presenza di righe legate a una testata.

Come già detto in precedenza, ogni campo filtro è dotato di una documentazione accessibile attraverso il tasto funzionale F1. Questo comando farà aprire una scheda contenente, campo per campo, il significato di ogni campo.

