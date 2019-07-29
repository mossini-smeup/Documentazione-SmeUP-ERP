# Formato guida
![Fig_001](http://localhost:3000/immagini/MBDOC_OGG-P_BRIN01/Fig_001.png)
Da questo formato è possibile gestire le dichiarazioni ricevute o emesse :  il **registro** definisce appunto il "verso" della dichiarazione, ovvero appunto se si vuol gestire le dichiarazioni ricevute dai clienti o quelle mandate ai fornitori.
Volendo è possibile anche scegliere direttamente una dichiarazione tramite l'indicazione del suo **Identificativo**(che non coincide nè con il numero riferimento, nè con il numero protocollo).
Selezionando  con un' opzione una dichiarazione si accede al relativo dettaglio.

![Fig_002](http://localhost:3000/immagini/MBDOC_OGG-P_BRIN01/Fig_002.png)
Oltre alle informazioni relative al registro ed al soggetto intestatario, viene mostrato il **Riferimento** (con la relativa data) ovvero il numero con cui la dichirazione è stata registrata dall'ente che la emette, e che verrà poi riportato sui documenti di tipo fattura.
Il numero **Protocollo** è invece il progressivo con cui la dichiarazione viene registrata dall'azienda che riceve la dichiarazione.

Il **Tipo dichiarazione** indica, in linea con quanto richiesto dal Ministero, se la dichiarazione si riferisce ad una singola operazione(1), oppure a più operazioni fino a concorrenza di un determinato importo(2), oppure a più operazioni in un determinato periodo di tempo(3). Ad esso è collegato il campo **Importo**, che indica la misura dell'importo, nel caso in cui si tratti di una dichiarazione di tipo 2.
Nel caso in cui invece si tratti di una dichiarazione di tipo (2), è necesario indicare il **Periodo** di riferimento, periodo entro il quale verrà considerato valido (e pertanto applicato) l'assoggettamento Iva inserito ovvero il **Cod. Iva**.
E' stata prevista poi anche una **Data Sospensione**, ovvero una data che se compilata inibisce l'applicazione del codice Iva sopraindicato.

## Note di gestione
E' importante sapere che il programma di gestione delle dichiarazioni, oltre ad alimentare appunto l'archivio delle dichiarazioni, esegue in automatico anche un'altra operazione, ossia quella di riportare alcune informazioni sulla dichiarazione nell'archivio degli enti.
Ciò significa che per ogni soggetto per il quale è presente una dichiarazione, nella sezione "Dati fiscali" della sua anagrafica vedrò compilati i campi : 
 * Data Valid.Esenzione
 * Dichiarazione Intento
 * Data Dichiarazione Intento

N.B. :  tali campi verranno aggiornati SOLO in caso di ricezione/invio di una nuova dichiarazione.
