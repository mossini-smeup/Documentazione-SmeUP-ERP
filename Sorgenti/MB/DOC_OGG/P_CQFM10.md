# Obiettivo
Attraverso questa funzione, è possibile attribuire ad un oggetto tutte le informazioni relative alle eventualità di malfunzionamento. Nel caso in cui l'oggetto in questione sia un articolo, il programma automaticamente si preoccupa di reperire ed esplodere la distinta di 1° Livello. Tutte le fasi successive di inserimento, sono supportate dai vari programmi di gestione delle funzioni che compongono la F.M.E.A.

## Formato guida
![CQ_FMEA_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_02.png)
_2_Gestione della griglia di riferimento estendibile oltre che agli articoli anche agli enti
I campi evidenziati sono tabellati (CQ0) perché la FMEA può essere fatta su di un prodotto, un processo un cliente, un ente, etc.., e quindi offre la possibilità di creare un qualsiasi tipo di documento che permette di gestire quelle informazioni di base che sono collegate all'oggetto dell'analisi.

## Formato inserimento dati
![CQ_FMEA_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_03.png) * _2_identificazione leader e partecipanti
 * _2_identificazione responsabile
 * _2_identificazione prodotto, famiglia, parametro :  Il tipo e l'obbligarietà di questi 3 campi evidenziati dipende dal tipo griglia impostato osssia dal tipo documento scelto.

Con -INVIO- si passa alle funzioni che consentono all'operatore di legare l'analisi dei componenti al loro gruppo di appartenenza. Supponiamo che il prodotto su cui vogliamo fare la FMEA sia una presa di forza (PTO) , un gruppo potrebbe essere un componente al primo livello mentre il componente potrebbe essere uno degli articoli che entrano in questo ( esplosione scalare ), un gruppo potrebbe essere il servizio sviluppo prodotto  ed il componente un dipendente di esso, etc...

### Attribuzione gruppo e componenti
![CQ_FMEA_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_04.png)
Questo formato, come i successivi, è strutturato in modo da riportare automaticamente in alto il codice della documentazione, la data, il prodotto su cui si sta facendo l'analisi ed il livello di modifica.

_2_Selezione Gruppo/Componente (opzione 1)
Il gruppo ed il componente possono essere selezionati in questi modi : 
 * '!'  Collegamento con anagrafica articoli o enti ordinati per  codice
 * '?'  Collegamento con anagrafica articoli o enti ordinati per descrizione
 * '/' Collegamento con distinta base dell'articolo su cui si sta facendo la FMEA

La fase di immissione del componente si completa con la definizione della funzione e della criticità del componente riempiendo i due campi tabellati evidenziati nel formato successivo

### Attribuzione funzione e criticità
![CQ_FMEA_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_05.png)Il Q9000 permette, una volta effettuata l'immissione dei singoli componenti, di definire per ciascun componente i suoi difetti e, per ogni difetto, gli effetti e le cause con relativo indice di priorità di rischio. La filosofia che sta alla base del Q9000 per il calcolo dell'indice di priorità (dato dal prodotto della probabilità, per la rilevabilità, per la gravità) è che la rilevabilità  dipende dal difetto, la gravità dipende dagli effetti e la probabilità dalla causa.

Il Q9000  per la scelta dei difetti da attribuire al singolo componente prevede le seguenti modalità : 
 * '!' Collegamento con tabella CQD in cui sono inseriti i difetti i riscontrati finora in azienda
 * '/'  Collegamento con l'archivio che gestisce le non conformità' :  mi viene fornito l'elenco delle non conformità rilevate sull'articolo di cui si sta facendo la FMEA

### Dichiarazione difetti
Con l'opzione 6 si possono inserire i difetti, i difetti sono codificati nella tabella CQD da cui possono essere selezionati.
![CQ_FMEA_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_06.png)
Una volta inserito il difetto è necessario associare un indice di rilevabilità e un indice di gravità : 

### Definizione rilevabilità e gravità del difetto
![CQ_FMEA_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_07.png)
Il prossimo passo consiste nella dichiarazione degli effetti, non obbligatoria come detto al fine della valutazione dell'indice di priorità di rischio ma formalmente più corretta dal punto di vista della norma. L'opzione 6 "Azioni aggiuntive" permettere di scegliere l'azione da eseguire : 

### Scelta dell'azione per dichiarazione dell'effetto
![CQ_FMEA_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_08.png)
### Dichiarazione dell'effetto
![CQ_FMEA_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_09.png)
Il modo in cui il Q9000 gestisce gli effetti è formalmente identico a quello delle cause e pertanto per una spiegazione più dettagliata si rimanda a queste ultime.

Le successive figure illustrano i passaggi per l'immissione di un effetto : 

_1_Scelta dell'effetto
![CQ_FMEA_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_09.png)
_1_Definizione gravità dell'effetto_1_
![CQ_FMEA_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_10.png)Quando viene immesso l'effetto il peogramma prende come valore dell'indice di gravità quello associato all'effetto, è da notare inoltre che dato che l'operatore può immettere più effetti riferiti ad un determinato difetto, in automatico il programma considera come indice di gravità quello dell'effetto più gravoso.

### Attribuzione cause all' effetto
Si utilizza l'opzione 6 "Dichiarazioni cause"

_1_Formato inserimento cause_1_
![CQ_FMEA_11](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_11.png)
Per la scelta delle cause ci si collega o con una tabella delle cause storiche riscontrate nell'intero processo produttivo o con una lista di cause già riscontrate sul prodotto di cui si fa la FMEA, legate al difetto che si sta analizzando, in questa funzione le cause legate al difetto saranno evidenziate in funzione dell'accertamento delle cause gestite nel campo "ACCERTAMENTO" dell'archivio di gestione delle non conformità.

Scelta la causa o cause è necessario compilare un documento in cui si deve specificare la probabilità di un difetto dovuto a questa causa : 

_1_Formato inserimento probabilità del difetto_1_
![CQ_FMEA_12](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_12.png)
Il risultato di questa operazione è la priorità di rischio.
In questa prima fase di immissione, in genere non vengono inserite le misure previste od eventuali azioni correttive.
Supponendo di immettere più cause per un difetto il documento che produce il programma è del tipo in figura in cui vengono riportati tutti i suoi legami ossia : 
 * documento su cui è registrata la FMEA,
 * prodotto,
 * gruppo,
 * componente,
 * difetto a cui si riferiscono queste cause.

_1_Riassunto dati FMEA_1_
![CQ_FMEA_13](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM10/CQ_FMEA_13.png)
Il Q9000 permette di inserire quanti si voglia componenti del prodotto, per ogni componente quanti si voglia difetti, per ogni difetto quante si voglia cause, etc.., secondo le modalità viste fino ad ora, il documento finale a cui si giunge riporta tutti i legami tra le scelte effettuate in modo chiaro e sintetico.
