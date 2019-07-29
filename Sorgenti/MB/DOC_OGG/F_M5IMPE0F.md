## Contenuto
Impegni "provvisori". Questo archivio contiene gli impegni (di materiali ed, eventualmente, di risorse) che servono a prenotare le quantità degli articoli coinvolti in un ATP per gli ATP successivi.
Si dividono in
- "provvisori provvisori", costruiti durante una sessione di ATP di simulazione, il cui utilizzo è unicamente di non rubare disponibilità libera tra più istanze dello stesso componente, presente in  diversi rami della distinta dell'assieme che si sta elaborando.Questi impegni devono essere presenti nel gruppo fonti della disponibilità libera, ma vengono considerati unicamente quelli della sessione in cui si sta eseguendo la scansione della disponibilità.
Hanno il campo numero sessione valorizzato
- "provvisori confermati" che sono il consolidamento dei precedenti quando l'ATP viene calcolato per una riga documento. Questi impegni devono essere presenti nel gruppo fonti della disponibilità libera, per evitare che essa venga utilizzata, in sequenza, per più di una datazione. Rappresentano quindi la disponibilità libera allocata ad una riga di documento datata con ATP. Essi vengono cancellati prima di ogni MRP (se totale nella loro globalità, se parziale unicamente quelli degli articoli coinvolti nella pianificazione), in quanto verranno sostituiti da impegni pianificati della stessa quantità.
Hanno il campo numero sessione vuoto.

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
 :  : DEC T(VO) P(F.M5IMPE0F) K(I£NSES)
 :  : DEC T(VO) P(F.M5IMPE0F) K(I£PROG)
 :  : DEC T(VO) P(F.M5IMPE0F) K(I£TIP1)

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
 :  : DEC T(ST) P() K(M5H)

## Autorizzazioni
N.A.

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Sono presenti le seguenti exit per modificare alcune informazioni  : 
Modifica finestra utente : 
 :  : DEC T(MB) P(M5SRC) K(M5M5HF_Z)
Smagrimento configurazione sui componenti
 :  : DEC T(MB) P(M5SRC) K(M5M5HK_A)
Innesco assieme
 :  : DEC T(MB) P(M5SRC) K(M5M5H0_Z)
Avanzamento date per sovracapacità
 :  : DEC T(MB) P(M5SRC) K(M5M5HC_S)

## /COPY
Calcolo ATP
 :  : DEC T(MB) P(QILEGEN) K(£M5H)
Rimappatura campi quantità da file a schiere (/COPY interna)
 :  : DEC T(MB) P(QILEGEN) K(£M5M5H_C01)
Arrotondamento al lotto e calcolo disponibilità prodotta (/COPY interna)
 :  : DEC T(MB) P(QILEGEN) K(£M5M5H_C02)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.

## Contenuto campi

 :  : FLD I£NSES **N.Sessione**
In simulazione è il nome del lavoro in cui è lanciato l'ATP (£PDSJN).
All'inizio di ogni nuova simulazione, vengono eliminati tutti i record del lavoro attuale. Non è necessaria l'eliminazione in uscita, in quanto l'intero archivio verrà cancellato prrima del lancio del successivo MRP totale.
In memorizzazione viene pulito, contestualmente al consolidamento dell'oggetto ricevuto, che sostituisce quello della simulazione (tipicamente si passa da un articolo a una riga documento).

 :  : FLD I£TIP1 **Tipo record**
- A  :  Record di testata (uno per ATP) :  contiene, nella schiera delle quantità, una serie di 400 date consecutive (a partitre dalla data partenza ATP impostata in tabella M5H).
I seguenti record sono sempre presenti, uno per ogni elemento di distinta base, anche se con le quantità a zero (assenza di disponibilità libera o disponibilità riservata)
- I  :  Record di anagrafica e di ATP :  contiene i dati generali e la quantità da produrre alla data ATP (corrispondente a quella registrata nel record 'A'), sia per gli articoli, sia per le risorse (in questo caso le quantità sono le ore di carico).
- R  :  Record di disponibilità libera riservata, riportata negli elementi della schiera corrispondenti alle date del tipo record 'A'.
- T  :  Record di disponibilità libera totale, riportata negli elementi della schiera corrispondenti alle date del tipo record 'A'.

 :  : FLD I£CDMG **Codice magazzino**
Presente su tutti i record.
Se non è attivo l'ATP multiplant completo è sempre il primo plant del gruppo fonti.
In caso contrario, nei record 'I' di trasferimento, è il plant origine del trasferimento (plant di competenza dell'articolo). Questo valore viene ereditato dagli altri record (R/T/C) e dai componeneti. E' in sostanza un 'deviatore' dei plant su cui si esegue l'ATP.
Per tener traccia di questo passaggio, il plant viene registrato anche nel primo campo libero (I£CL01), che è il plant d'arrivo se ordine di trasferimento.

 :  : FLD I£TIOG **Tipo oggetto**
Presente su tutti i record :  tipizza, con il parametro oggetto, l'oggetto dell'ATP (vedi I£CODI).

 :  : FLD I£PAOG **Parametro oggetto**
Presente su tutti i record :  tipizza, con il tipo oggetto, l'oggetto dell'ATP (vedi I£CODI).

 :  : FLD I£CODI **Codice oggetto**
Presente su tutti i record :  è l'oggetto di cui si calcola l'ATP.
In simulazione piò essere un articolo o una riga documento. Quando si memorizza viene sostituito dall'oggetto ricevuto (usualmente una riga documento).
Alternativamente, se è un calcolo definitivo, è direttamente la riga documento.

 :  : FLD I£CONF **Configurazione**
Presente su tutti i record :  se impostato l'ATP per configurazione, viene riportata la configurazione ricevuta (sia in calcolo sia in memorizzazione).
In discesa la configurazione viene passata secondo quanto è definito del campo della tabella M5H (copiata, tralasciata, smagrita).

 :  : FLD I£TIAF **Tipo assieme di riferimento**
Presente su tutti i record a partire dal livello 1 :  è il tipo oggetto di riferimento dell'assieme.

 :  : FLD I£PAAF **Parametro assieme di riferimento**
Presente su tutti i record a partire dal livello 1 :  è il parametro oggetto di riferimento dell'assieme.

 :  : FLD I£OGAF **Codice assieme di riferimento**
Presente su tutti i record a partire dal livello 1 :  è l'oggetto di riferimento dell'assieme.

 :  : FLD I£TIRF **Tipo oggetto di riferimento**
Presente su tutti i record :  tipizza, con il parametro oggetto di riferimento, l'oggetto di riferimento (vedi I£OGRF)

 :  : FLD I£PARF **Parametro oggetto di riferimento**
Presente su tutti i record :  tipizza, con il tipo oggetto di riferimento, l'oggetto di riferimento (vedi I£OGRF)

 :  : FLD I£OGRF **Codice oggetto di riferimento**
E' valorizzato in modo diverso a seconda del record
Per i record 'I' di articolo è l'ente preferenziale. Viene valorizzato solo se ATP logistico o se parametri di pianificazione ATP per ente.
Per i record 'I' di carico è il piano in cui sono registrate le capacità e i carichi.

 :  : FLD I£TSES **Tipo sessione**
Presente su tutti i record :  è l'elemento della tabella M5H con cui è stato lanciato l'ATP in simulazione (routine £M5H con funzione 'CAL')

 :  : FLD I£PROG **N.progressivo**
Presente su tutti i record :  è l'ordine progressivo con sui sono elaborati gli articoli (ha lo stesso valore per tutti i tipi record dello stesso legame).
Ad esempio, una distinta di questo tipo :  A -> B, B -> C, B ->D e C -> E, ha questi campi : 
 :  : PAR L(TAB)
Assieme di Consumo|Oggetto di consumo|Livello distinta|N.Progressivo origine|N.Progressivo
|A|0|0|1
A|B|1|1|2
B|C|2|2|3
C|E|3|3|4
B|D|2|2|5


 :  : FLD I£NORI **N.progressivo origine**
Presente su tutti i record a partire dal livello 1 :  è il numero progressivio dell'assieme.

 :  : FLD I£TIAC **Tipo assieme di consumo**
Presente su tutti i record a partire dal livello 1 :  è il tipo oggetto di consumo dell'assieme.

 :  : FLD I£PAAC **Parametro assieme di consumo**
Presente su tutti i record a partire dal livello 1 :  è il parametro oggetto di consumo dell'assieme.

 :  : FLD I£OGAC **Codice assieme di consumo**
Presente su tutti i record a partire dal livello 1 :  è l'oggetto di consumo dell'assieme.

 :  : FLD I£TICO **Tipo oggetto di consumo**
Presente su tutti i record :  tipizza, con il parametro oggetto di consumo, l'oggetto di consumo (vedi I£OGCO)

 :  : FLD I£PACO **Parametro oggetto di consumo**
Presente su tutti i record :  tipizza, con il tipo oggetto di consumo, l'oggetto di consumo (vedi I£OGCO)

 :  : FLD I£OGCO **Codice oggetto di consumo**
Presente su tutti i record :  a livello 0 è l'oggetto di cui si calcola l'ATP di simulazione, oppure l'oggetto (articolo) se si sta eseguendo un ATP effettivo. Nei livelli successivi contiene il componente ritornato dalla distina base.
Il legame di distinta base viene quindi registrato, a partire dai record di livello 1, dalla coppia Assieme di consumo - Oggetto di consumo

 :  : FLD I£LIMI **Livello di distinta**
Presente su tutti i record :  è il livello di distinta base :  per il primo record (che contiene solo l'oggetto di consumo) vale zero, per gli altri viene recepito dalla scansione della distinta base.

 :  : FLD I£LOTR **Lotto di riferimento**
Presente sul record 'I'
E' il lotto standard dell'articolo contenuto nel campo oggetto di consumo.

 :  : FLD I£QMIN **Quantità minima**
Presente sul record 'I'
Calcolato dall'oggetto di consumo (e dall'oggetto di riferimento, se impostato in M5H) con la routine di acquisizione dati di pianificazione £M5H.
L'oggetto di riferimento può essere solo l'ente esecutore dell'ordine, e viene utilizzato se sono stati impostati in tabella M51 i paramentri di pianificazione per ente, e in tabella M5H di utilizzarli.

 :  : FLD I£QMUL **Quantità multipla**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£QMAX **Quantità massima**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£LDTS **Lead time fisso**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£LDTV **Lead time variabile**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£LDTR **Lead time rettifica**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£LDAD **Lead time adj**
Presente sul record 'I'
Vedi I£QMIN per i dati di input del calcolo.

 :  : FLD I£TIOR **Codice suggerimento**
Presente sul record 'I'
E' il tipo dell'ordine da emettere secondo questo ATP (produzione, acquisto, lavorazione, trasferimento).

 :  : FLD I£QTOR **Quantità originale**
Sul record 'I' è' la quantità richiesta, ad ogni livello, precedente alla nettificazione :  al livello zero è la quantià di cui si vuol calcolare l'ATP, ai livelli successivi è la quantità originale del livello superiore moltiplicata per il coeffciente di impiego.
Sul record 'T' è la disponilibità libera giacente.

 :  : FLD I£QTRI **Quantità richiesta**
Sul record 'I' al livello zero coincide con la quantità originale, ai livelli successivi è la quantità da produrre del livello superiore moltiplicata per il coefficiente di impiego.

 :  : FLD I£QTDP **Disponibilità prodotta**
Sul record 'I' è la disponibilità prodotta nel livello, generata dalla lottizzazione, e messa a disposizione di ulteriori impegni del componente, su successivi rami di distinta base, nel corso dello stesso ATP, o di ATP successivi, se consolidata (e impostata come fonte nel gruppo della disponibilità libera).

 :  : FLD I£QTPR **Quantità da produrre**
Sul record 'I' è la quantità richiesta del livello nettificata dalla disponibilità libera utilizzata. C
Sul record 'R' è il totale della quantità riservata (somma delle disponibilità libere usate per questa riga ATP).

 :  : FLD I£DTMI **Data materiali inizio**
Sul record di tipo 'A' è la data di inizio della finestra ATP (data minima di tabella M5H).
Sul record di tipo 'I' è la data di inizio dell'ordine da emettere.

 :  : FLD I£DTMF **Data materiali fine**
Sul record di tipo 'A' è la data di fine della finestra ATP (data massima di tabella M5H).
Sul record di tipo 'I' è la data di fine dell'ordine da emettere.

 :  : FLD I£DTAI **Data appiattimento inizio**
Sul record di tipo 'I' è la data di inizio dell'ordine da emettere, appiattita al più tardi. Coincide con la data materiali inizio se non è stato impostato l'appiattimento in tabella M5H, oppure se si è sun un ramo critico.

 :  : FLD I£DTAF **Data appiattimento fine**
Sul record di tipo 'I' è la data di fine dell'ordine da emettere, appiattita al più tardi. Coincide con la data materiali fine se non è stato impostato l'appiattimento in tabella M5H, oppure se si è sun un ramo critico.

 :  : FLD I£DTCI **Data capacità inizio**
Sui tipi riga 'I', è la data inizio corretta dal vincolo delle capacità;  in assenza di questo vincolo coincide con la data appiattimento inizio.

 :  : FLD I£DTCF **Data capacità fine**
Sui tipi riga 'I', è la data fine corretta dal vincolo delle capacità;  in assenza di questo vincolo coincide con la data appiattimento fine.

 :  : FLD I£COEF **Coefficiente d'impiego_n
Presente su tutti i record a partire dal livello 1 :  è la quantità ritornata dalla distinta base  nel campo £DIV(7).

 :  : FLD I£Q001 **Quantità fonte**
Questo campo, e gli altri 399 che costituiscono una schiera di 400 elementi, contengono quantità diverse in funzione del tipo record I£TIP1. Si rimanda quindi alla documentazione di quest'ultimo campo per un'esposizione dettagliata.

 :  : FLD I£LIVE Livello
Campo attualmente non utilizzato

 :  : FLD I£STAT Stato
Campo attualmente non utilizzato

 :  : FLD I£DL01 Data libera 1
Campo a disposizione utente

 :  : FLD I£DL02 Data libera 2
Campo a disposizione utente

 :  : FLD I£DL03 Data libera 3
Campo a disposizione utente

 :  : FLD I£DL04 Data libera 4
Campo a disposizione utente

 :  : FLD I£DL05 Data libera 5
Campo a disposizione utente

 :  : FLD I£QL01 Quantità libera 1
Campo a disposizione utente

 :  : FLD I£QL02 Quantità libera 2
Campo a disposizione utente

 :  : FLD I£QL03 Quantità libera 3
Campo a disposizione utente

 :  : FLD I£QL04 Quantità libera 4
Campo a disposizione utente

 :  : FLD I£QL05 Quantità libera 5
Campo a disposizione utente
Se impostato di calcorare i giorni di distanza dalla criticità, viene scritta sul record 'I'.

 :  : FLD I£CL01 Codice libero 1
Campo a disposizione utente
Se ordine di trasferimento vi viene scritto il plant d'arrivo

 :  : FLD I£CL02 Codice libero 2
Campo a disposizione utente

 :  : FLD I£CL03 Codice libero 3
Campo a disposizione utente

 :  : FLD I£CL04 Codice libero 4
Campo a disposizione utente

 :  : FLD I£CL05 Codice libero 5
Campo a disposizione utente

 :  : FLD I£DTIN Data inserimento
Impostato alla data di inserimento del record

 :  : FLD I£ORIN Ora insertimento
Impostato all'ora di inserimento der record

 :  : FLD I£DTAG Data aggiornamento
Impostato alla data di inserimento del record

 :  : FLD I£ORAG Ora aggiornamento
Impostato all'ora di inserimento del record

 :  : FLD I£USIN Utente inserimento
Impostato con l'utente che ha lanciato l'azione

 :  : FLD I£USAG Utente aggiornamento
Impostato con l'utente che ha lanciato l'azione


