# Formato guida
![CQ_RDIN_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQRI10/CQ_RDIN_02.png)
 La gestione delle richieste di intervento è composta da otto opzioni principali : 
 * _2_01 :  consente di immettere una richiesta di intervento. Questa operazione può essere effettuata da tutte le direzioni presenti in azienda. In questa fase è necessario specificare l'ente richiedente (che dovrebbe coincidere con l'utente che sta inserendo la richiesta di intervento), l'oggetto su cui si esegue la richiesta, la soluzione del problema, l'obiettivo che si vuole raggiungere e l'ente designato alla risoluzione del problema.
 * _2_02 :  consente di gestire i dati che sono stati registrati durante l'immissione
 * _2_03 :  consente di copiare una qualsiasi richiesta di intervento in qualunque stato essa si trovi, in quanto si copiano solamente i dati che si gestiscono con le prime due opzioni, tralasciando quindi le informazioni relative alla GESTIONE o alla EVASIONE di una richiesta. La copia delle note è opzionale, infatti durante  l'esecuzione appare una finestra in cui se si preme F06 si conforma la copia, altrimenti con F12 si tralascia tale operazione
 * _2_04 :  consente la cancellazione della richiesta se questa non è ancora stata gestita o evasa
 * _2_05 :  consente la visualizzazione dei campi gestiti nell'immissione di una richiesta, in qualunque stato essa si trovi
 * _2_GE :  la gestione di una richiesta di intervento deve essere effettuata dall'utente associato alla direzione inserita nel campo Ente Designato. In questa fase è obbligatoria l'immissione dei seguenti campi : 
 ** Responsabile Evasione
 ** Priorità di evasione
L'operazione  fondamentale da fare in questa fase è di portare a GE (gestione esito intervento) lo stato della richiesta presente in seconda videata
 * _2_EV :  L'evasione consente di evadere la richiesta, quindi l'ente responsabile dell'evasione e l'ente a cui è stata addebitata, dovranno gestire i vari stati della richiesta finché non raggiungerà lo stato EV (evasa). A questo punto l'Ente Richiedente potrà compilare i campi relativi all'Esito Soluzione Adottata e Effetto soluzione adottata. Una volta compilati tutti i campi la richiesta è considerata chiusa e quindi è possibile solo visualizzarla in modo completo o parziale
 * _2_IN :  Consente di vedere tutta la richiesta di intervento e può essere richiesta in qualsiasi momento, è poi l'unico modo di visionare una richiesta quando è stata definitivamente chiusa

## Campi del formato
 * _2_Tipo Richiesta, è un campo tabellato CQZ identifica con un codice il tipo di richiesta d'intervento (azioni correttive, richieste di progetto, sperimentazione, deroga , assistenza, ecc..)
 * _2_Tipo Griglia, è un campo tabellato CQY identifica con un codice una tripletta di campi in cui l'utente può specificare i dati di riferimento dell'oggetto su cui si fa la richiesta di intervento. Esempi di triplette sono articolo/materia prima/famiglia, articolo/famiglia/centro di lavoro, articolo/fase di lavorazione/fase di collaudo
 * _2_Numero Documento, è il numero progressivo della richiesta di intervento che viene fornito in automatico con l'immissione della richiesta

# Formato lista
![CQ_RDIN_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQRI10/CQ_RDIN_03.png)
# Formato dettaglio
![CQ_RDIN_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQRI10/CQ_RDIN_04.png)
 * _2_Articolo/Fase lavorazione/Fase collaudo, sono i tre campi che dipendono dal tipo griglia impostato e che permettono di documentere l'oggetto della richiesta di intervento. L'archivio o la tabella a cui si collegano dipende dal tipo di codice che è stato impostato in tabella CQY.
 * _2_Ente Richiedente, è un campo tabellato * CNTT che  identifica con un codice l'ente/area operativa, l'ente/dipendente, ecc.. che effettua la richiesta di intervento.
 * _2_Obbiettivo e Soluzione Proposta, sono campi descrittivi controllati in tabella CQ*QZ che permettono di documentare i dati di base della richiesta in esame. La definizione di questi  due campi dipende dal campo "tipo di richiesta"  e quindi dalle impostazioni fatte in tabella CQZ.
 * _2_Procedura Riferimento, è un campo che identifica con un codice la procedura di riferimento dell'azienda a cui riferirsi per la gestione della richiesta in esame
 * _2_Ente Designato,  è un campo tabellato * CNTT che  identifica con un codice l'ente/area operativa, l'ente/dipendente, ecc.. che gestisce la richiesta di intervento.
 * _2_Quantità lotto/Unità di misura, sono campi di immissione facoltativa per specificare altre informazioni relative alla richiesta di intervento
 * _2_Data evasione programmata, è la data prevista di evasione della richiesta, in automatico è proposta quella odierna

## Gestione (GE)
L'opzione GE, presenta il formato di dettaglio in cui devono essere gestiti i seguenti campi : 
 * _2_Priorità di evasione, è un campo tabellato CQ*PR  che  identifica con un codice la priorità di evasione dell'intervento, ad esempio priorità massima, media, minima, elevata, bassa, ecc..
 * _2_Responsabile evasione, è un campo tabellato * CNTT che  identifica con un codice l'ente/area operativa, l'ente/dipendente, ecc.. a cui è affidato il compito di evadere la richiesta di intervento.
 * _2_Ore a preventivo, è un campo che richiede caratteri numerici in cui l'ente designato sulla base del tipo di richiesta immesso valuta il numero di ore in cui probabilmente verrà evasa l'attività di intervento
 * _2_Costi a preventivo, è un campo che richiede caratteri numerici in cui l'ente designato sulla base del tipo di richiesta immesso valuta il costo dell'attività di intervento
 * _2_ENTER, consente di passare al formato successivo : 

![CQ_RDIN_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQRI10/CQ_RDIN_05.png)
 * _2_Richiesta collegata, è un campo da cui si possono collegare alla richiesta in esame 'n' altre attività di intervento in serie : 

![CQ_RDIN_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQRI10/CQ_RDIN_06.png)
 * _2_Rapporti di prova/Soluzione adotta/Esito Sol. Adott/Effetto sol. adottata, controllati in tabella CQ*QZ con cui vengono descritte le informazioni fondamentali circa l'attività che è stata evasa. La definizione di questi  due campi dipende dal campo "tipo di richiesta"  e quindi dalle impostazioni fatte in tabella CQZ.
 * _2_Altri costi a con/Ore a consuntivo/Costo tot a cons, sono tre campi numerici con cui l'ente di addebito imputa i costi e le ore consuntivate per la risoluzione della richiesta
 * _2_Centro di lavoro, è un campo facoltativo in cui si specifica a quale centro di lavoro si vogliono addebitare i costi consuntivati
 * _2_Stato dell'intervento, è il campo in cui si specificano i vari stati della richiesta di intervento DE, GE, EV, ecc...
 * _2_Data effettiva evasione, si specifica la data in cui effettivamente si evade la richiesta
 * _2_Appr. Rilascio Doc, è un campo che si collega con il modulo della Documentazione (cfr modulo DOCU) per la emissione, approvazione, rilascio e distribuzione di un nuovo documento. In automatico il programma crea un documento legato all'oggetto della richiesta di intervento in esame,  nel caso del nostro esempio l'articolo A01.
 ** È da notare che nel caso in cui il tipo di documento sia un disegno tecnico il programma attua una gestione controllata del livello di modifica per cui se su quell'articolo su cui stiamo gestendo la richiesta di intervento esiste già un disegno, quello nuovo può essere emesso solo ad un livello di modifica superiore.
** Terminata la gestione del documento in automatico il programma prima di ritornare alla richiesta di intervento si collega con il modulo della  gestione dei collaudi per la modifica al corrispondente livello documento della/e fase/i del ciclo di collaudo. Se ad esempio la richiesta di intervento mi ha portato alla modifica di un particolare  del disegno progetto può essere richiesta la modifica di una o più fasi del ciclo di collaudo. Fino a che non è stato evaso questo punto il documento non deve essere rilasciato per impedire che vengano effettuati collaudi non in linea con il livello di modifica del documento.


