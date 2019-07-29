## Obiettivo
La funzione serve per l'immissione delle liste di riferimento

## Formato di lancio

![CQ_AUDT_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM10/CQ_AUDT_03.png)
La lista viene generata in questo modo : 
 - si seleziona il numero progressivo di griglia
 - si seleziona un tipo griglia :  il tipo griglia determina il tipo di audit che può essere creato utilizzando quella lista di riferimento, dal tipo griglia dipendono infatti i tre campi dove si riportano le caratteristiche da verificare;
 - si immette il livello di modifica del documento che si sta generando

Mappa di selezione progressivo e tipo griglia.
![CQ_AUDT_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM10/CQ_AUDT_04.png)
Il gruppo di lavoro che si occupa di definire le liste di riferimento si crea dunque dei tipi griglia personalizzati che gli permettono di definire gli audits nel modo che ritiene più opportuno per la sua realtà.
Ad esempio nel caso di un audit interno delle procedure si sarebbe potuto  selezionare dal campo tabellato "tipo griglia" (vedi tabella CQY) una griglia a cui corrisponde la generazione di tre campi in cui può essere specificato : 
 * procedura,
 * sezione manuale,
 * settore.

Griglia Audit
![CQ_AUDT_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM10/CQ_AUDT_05.png)
Di utilizzo generale per ogni tipo di audit sono invece i campi : 
 * Descrizione ridotta, è un campo descrittivo in cui l'utente da una descrizione sintetica dell'audit;
 * Importanza caratteristica, è un campo tabellato CQJ che permette di valutare le caratteristiche in fase di Audit assegnando loro un peso che è dato dalla classe d'importanza.
 * valutazione minima, è un campo tabellato CQW che identifica con un codice il livello qualitativo minimo della caratteristica in esame
 * valutazione attesa, è un campo tabellato CQW che identifica con un codice il livello qualitativo atteso della caratteristica in esame;
 * tempo di controllo preventivato, è un campo richiedente caratteri numerici che identifica il tempo di controllo a preventivo espresso in ore;
 * procedura di riferimento, è un campo tabellato CQM che identifica con un codice la procedura di riferimento dell'attività di Audit in esame.

Dal punto di vista operativo è possibile ad esempio nel caso delle procedure collegarsi con la procedura e copiarne il paragrafo di interesse nel campo gestione commenti.

Si noti come anche il campo gestione commenti sia legato al progressivo griglia ed al livello di modifica di quest'ultimo. Con la compilazione di questi campi termina la fase di immissione dei dati che poi vengono utilizzati per costruire la griglia dell'audit. Con il modo di procedere visto si inseriscono ad esempio per gli audit interni tanti documenti identificati dal numero di progressivo griglia assegnato dall'operatore e dal tipo griglia "PRO" che poi vanno a costituire la lista di riferimento per gli audit-interni. È da notare che in fase di immissione il Q9000 controlla che non vengano inseriti documenti con numero di progressivo griglia già esistente obbligando in questo modo l'operatore ad inserire un livello di modifica superiore. Il Q9000 realizza dunque una catalogazione dando la possibilità tramite il modulo di interrogazione di consultare facendo passare tutti i livelli di modifica, la storia delle liste di riferimento utilizzate dall'azienda.

Gestione note
![CQ_AUDT_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM10/CQ_AUDT_06.png)