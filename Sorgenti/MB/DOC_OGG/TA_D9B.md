# D9B - Fonti
 :  : DEC T(ST) K(D9B)
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la descrizione delle fonti di estrazione per Cube_up.
 :  : FLD T$D9BA **Programma D9AP_xxy**
Contiene il suffisso dei 2 programmi specifici per l'estrazione dell'archivio trattato. I suffissi numerici (01,02,03,...) competono agli archivi propri di Smeup, quelli preceduti da una X (X1,X2,X3,...) sono personalizzazioni su archivi esterni a SMEUP.
Segue elenco completo estrattori presenti. Selezionare opzione "HE" per visualizzare l'help specifico.
 :  : DEC T(OJ) P(*PGM) K(D9AP_[V3.PFC]C) I( Estrattore >>)
 :  : FLD T$D9BB **Parametri origine**
Contiene i parametri origine specifici per il programma specificato nel campo del prefisso. Essi variano a seconda dell'estrazione, per visualizzarli inserire un '+' all'inizio del campo.
 :  : FLD T$D9B1 **Dimensioni (Gerarchia 1-10)**
Contiene le gerarchie da tabella D9C (sottosettore uguale al suffisso del programma utilizzato) per gli oggetti che il programma specifico con suffisso 'P' gli passa, in base ai parametri origine. Se presenti elementi per l'oggetto in questione li propone in lista, e propone anche la scelta di non includere nessuna gerarchia per quell'oggetto. In base alla gerarchia che si passa, l'oggetto verrà aggregato in Databeacon con la struttura qui specificata.
 :  : FLD T$D9B2.T$D9B1
 :  : FLD T$D9B3.T$D9B1
 :  : FLD T$D9B4.T$D9B1
 :  : FLD T$D9B5.T$D9B1
 :  : FLD T$D9B6.T$D9B1
 :  : FLD T$D9B7.T$D9B1
 :  : FLD T$D9B8.T$D9B1
 :  : FLD T$D9B9.T$D9B1
 :  : FLD T$D9B0.T$D9B1
 :  : FLD T$D9BI **Mod. Vis. Campi Aggiuntivi**
Dove gestito dal programma estrattore, permette di gestire una serie di campi piatti ai quali non si può associare una gerarchia da tabella D9C. Si possono tuttavia portare nel cubo singolarmente o utilizzarli per aggregare qualsiasi oggetto della gerarchia della D9C utilizzata.
 :  : FLD T$D9BF **Modello Valori**
Contiene la struttura dei valori che verranno portati nel Databeacon, da tabella D9D nel sottosettore specificato dal campo suffisso programma. Se lasciato bianco i valori e le intestazioni saranno presi direttamente dai programmi specifici.
 :  : FLD T$D9BG **Tipo generazione**
Selezionare se in fase di estrazione deve estrarre, relativamente a questa fonte, solamente i dati, senza rigenerare la struttura o lo script di esecuzione, utilizzando quelli che devono essere già presenti. Può essere usato per modificare i cubi dal programma PC, e successivamente alle modifiche rinfrescarlo solo con i dati, mantenendo la struttura già modificata. Utilizzando uno script costruito, lascia la libertà di fare delle operazioni sulla rete Pc prima, dopo o durante l'estrazione, come spostare l'estrazione in più cartelle oppure inviare via email il cubo.
 :  : FLD T$D9BH **Parametri dinamici**
È un valore SI/NO. Selezionando SI, se previsto dai programmi specifici prima del lancio dell'estrazione, propone un impostazione di altri parametri che possono influenzare l'estrazione. Selezionando NO, esegue l'estrazione in modo tradizionale.
 :  : FLD T$D9BL **Opzioni Excel**
Permette di gestire alcune opzioni che valida solo se la destinazione è l'esportazione su Excel. Opzioni : 
- A Applica la D9D, quindi permette di rinominare i campi dei valori o di non esportarli sul file di testo.
- B Come la funzione A e in più non lancia la macro di esecuzione del foglio Excel.
 :  : FLD T$D9BM **Formato Nr. in TXT**
Permette di impostare il numero di decimali da emettere nel record del file D9WKDT0F per i valori del cubo.
Di default, il numero possiede 6 decimali. Se impostato il campo, viene assunto un numero diverso di decimali.
Questa formattazione viene visualizzata nell'esplosione dei record di dettaglio, e non viene utilizzata per la visualizzazione del formato numerico all'interno del cubo, per la quale bisogna seguire la strada del modello valori (D9D)
 :  : FLD T$D9BJ **Eliminazione Workfile**
Se viene impostato questo campo, al termine delle operazioni di generazione del cubo verranno eliminati i membri dei file di lavoro creati per la fonte. I file di lavoro interessati sono : 
- D9WKBT0F   CUBE File Trasferimento Batch
- D9WKDS0F   CUBE File Trasferimento DS4
- D9WKDT0F   CUBE File Trasferimento TXT dati.

L'eliminazione dei membri riguarderà esclusivamente quelli creati per la specifica fonte.
È consigliabile tenere attivata questa funzionalità, per limitare l'occupazione di memoria disco
 :  : FLD T$D9BC **Tipo Output**
Questo campo indica che tipo di output è richiesto per l'elaborazione.
Se questo campo non viene impostato viene utilizzato il tipo output di default impostato nella tabella D91.
Se viene impostato il valore '1' l'output dell'elaborazione sarà nella cartella IFS \Smedoc\D9\.
Se viene impostato il valore '2' l'output dell'elaborazione sarà nella cartella IFS \Smecs\ e verranno creati i membri col nome della fonte nei files : 
- D9WKBT0F   CUBE File Trasferimento Batch;
- D9WKDS0F   CUBE File Trasferimento DS4;
- D9WKDT0F   CUBE File Trasferimento TXT dati.
