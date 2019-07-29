 :  : TIT Qualità
# Concetti base
Sme.UP si occupa della qualità, copre i requisiti delle diverse normative che regolano la materia e lo fa raccogliendo informazioni in modo gratuito o semiautomatico dal sistema informativo che supporta l'azienda. Un esempio :  prendiamo una informazione che normalmente è trattata dall'ufficio contabile, prendiamo il ritardo di pagamento di un cliente ( o un insoluto). Questo evento trasporta una informazione che riguarda anche la qualità. Oppure, una nostra spedizione a cliente in ritardo rappresenta una informazione valida per la qualità. Infatti è nel manuale della qualità che ci si occupa di controllare la soddisfazione del cliente, ed uno dei misuratori della soddisfazione del cliente è dato dalla puntualità dei pagamenti o dalla puntualità delle nostre spedizioni.
Sme.UP, con l'applicazione Q9000 si occupa di "raccogliere" queste informazioni determinanti per lo sviluppo dei processi di qualità in modo facilitato, diciamo quasi automaticamente.

# Integrazione
L'integrazione tra i processi di qualità e quelli gestionali è l'architrave dell'applicazione Q9000. Il modello dei processi che sottende la qualità è concepito per sfruttare al massimo l'integrazione dei dati, ed il rispetto dei processi/archivi dove l'informazione viene creata e gestita (vedi fig. 1).

![AAP_QEM_01](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_01.png)
Questo rapporto di collaborazione tra il sistema qualità ed il sistema gestionale è mutuo :  così come l'analisi degli indici di performance (KPI) di un fornitore legge l'informazione relativa al ritardo di consegna dalla bolla di ricevimento materiale e dall'ordine di acquisto (la data della bolla confrontata con la data richiesta dall'ordine determinano la puntualità del fornitore), allo stesso tempo il pagamento delle fatture fornitore viene bloccato dall'esito di collaudo del lotto ricevuto.

I punti di collaborazione tra il sistema gestionale e l'applicazione della Qualità sono i seguenti : 
 * Integrazione di tutti gli oggetti applicativi :  articoli, fornitori, centri di lavoro, ecc...
 * Creazione dei lotti a partire dagli eventi del sistema gestionale che rappresentano l'aggregazione di materiale : 
 ** Ricevimento di materiale, sia da fornitore (acquisto, conto lavoro) che da cliente (reso Cliente)
 ** Creazione di ordini di produzione
 ** Versamento di ordini di produzione
 ** Dichiarazione di avanzamento di fase di ordine di produzione
 * Creazione di Non Conformità, con integrazione dei costi rilevati dall'archivio costi
 * Pagamento fattura fornitore bloccato dall'esito di collaudo del lotto ricevuto, e relativo solo a quantità effettivamente ricevuta
 * Workflow attivato a seguito di creazione non conformità :  può portare ad emissione nota di credito/debito
 * Movimenti di magazzino generati dall'esito del collaudo che permettono di spostare il materiale dall'area del collaudo alle aree interessate (vedi fig. 2), con criteri diversi per tipo lotto (la logistica del lotto di acquisto è diversa da quella del reso cliente, o da quella dell'ordine di produzione)
 * Una delle chiavi dei movimenti di magazzino (e quindi di giacenza) può essere il lotto :  questa è la base per poter ottenere una rintracciabilità informatica dei materiali.

![AAP_QEM_02](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_02.png)
# Funzioni native della qualità
Ovviamente ci sono funzioni native della qualità che creano e processano i dati in modo autonomo : 
 * la gestione dei cicli di collaudo
 * l'esecuzione dei collaudi
 * la gestione dei piani di campionamento (con già caricate circa 8000 griglie di campionamento)
 * la rilevazione dei valori misurati
 * la gestione degli strumenti di misura
 * la manutenzione degli impianti
 * la gestione delle non conformità
 * la gestione della FMEA (Failure Mode Effect Analysis)
 * la gestione degli audit
 * la gestione dell'addestramento del personale
 * le richieste di intervento

Tutti questi sono altamente parametrizzati :  significa che la loro applicabilità a gestire i processi per cui sono stati inizialmente pensati, si estende anche a processi non immaginati all'origine, semplicemente cambiando l'impostazione delle tabelle di parametrizzazione. Per esempio, il modulo "richieste di intervento" che inizialmente era pensato per gestire le azioni correttive relative alla risoluzione della non conformità, può essere utilizzato per descrivere la richiesta di identificazione di un nuovo fornitore o di un nuovo candidato per assunzione. Infatti questo modulo gestisce delle "cartoline" elettroniche che hanno un mittente (un oggetto qualsiasi, parametrizzabile) un destinatario (pure lui parametrizzabile), una griglia di 3 chiavi cui fa riferimento la cartolina, delle date di evasione richieste ed effettive, dei costi di budget ed effettivi, uno stato di esecuzione, note. Praticamente una richiesta generalizzabile per descrivere qualsiasi rapporto aziendale dove c'è uno che chiede qualcosa a qualcun altro che deve farla entro una certa data e con certi costi. Ovviamente descrive anche l'azione correttiva, ma si può utilizzare per molti altri scopi.

# Funzioni di sintesi della qualità
Come in tanti altri processi anche la qualità ha dei KPI (Key Performance Index) che cercano di misurare in modo oggettivo la performance del processo. Anche questi sono impostazioni personalizzabili con tabelle parametriche, che  possono assegnare a diversi oggetti i valori coerenti con le politiche di valutazione aziendali
Inoltre è possibile comporre questi KPI in indici finali che rappresentano con un solo voto tutto l'andamento di un processo.
Questo avviene tramite il modulo di composizione indici, chiamato "Vendor Rating" (fig. 3 ), che permette di comporre come in una distinta base, indici elementari a più livelli, determinando quindi un valore finale controllato tra 0 e 100 che  rappresenta il punteggio.

![AAP_QEM_03](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_03.png)
# Rapportistica
L'utilizzo delle schede grafiche permette la realizzazione di consultazioni facilmente filtrabili, ordinabili, esportabili in excel o in formati report.

![AAP_QEM_01](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_01.png)
![AAP_QEM_02](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_02.png)
![AAP_QEM_03](http://localhost:3000/immagini/MBDOC_VIS-AAQEM/AAP_QEM_03.png)