 :  : TIT Pianificazione materiali
# Importanza della pianificazione materiali
In un contesto in cui il mercato richiede forniture sempre più puntuali con tempi di risposta sempre più veloci e contemporaneamente l'azienda ha la necessità di ridurre costantemente le scorte di magazzino assicurando comunque l'alimentazione alle linee produttive e il servizio al cliente, la pianificazione materiali acquista un'importanza crescente ed è un fattore strategico per la sopravvivenza e la crescita dell'impresa.
## Impostazione concettuale
La pianificazione dei materiali si inserisce in un circolo virtuoso che interessa diverse funzioni aziendali : 
 * la funzione commerciale che negli ordini di vendita inserisce date di consegna congruenti con la disponibilità materiali, a tutti i livelli e compatibili con la capacità produttiva installata (ATP)
 * la programmazione materiali che utilizza tecniche previsionali, scorte strategiche opportuni parametri e politiche di pianificazione, differenziate per tipologia di materiali per assicurare la disponibilità quando serve senza pianificare eccedenze di scorta non giustificate (MRP)
 * la produzione che assicura l'esecuzione nei tempi e quantità stabilite ed opera una schedulazione a capacità finita degli ordini di produzione rilasciati in modo da avere una alta affidabilità delle data schedulate di produzione e al contempo mantiene adeguatamente il calendario delle risorse e la definizione della capacità produttiva giornaliera onde permettere della adeguate verifiche di capacità sia a capacità finita che infinita (FCS - CRP)
 * la logistica che garantisce l'affidabilità delle giacenze e la costanza dei tempi previsti per la movimentazione
 * se giacenze, coperture e pianificazione sono corrette e la data di consegna negli ordini di vendita può essere più accurata
 * l'accuratezza delle date degli ordini, delle coperture e delle quantità in giacenza permette una migliore pianificazione
 * la pianificazione adeguata, solleva la produzione dalle situazioni di emergenza
 * la movimentazione diventa più fluida
 * e si ricomincia ....

## Punti qualificanti Fonti / Gruppo fonti
Il fabbisogno o la copertura, come anche la scorta minima sono tutte condizioni che variano la situazione di disponibilità di un articolo nel tempo. In Marp.UP queste condizioni sono state codificate come "fonti" :  una fonte può essere costituita dalle righe ordini di vendita, un'altra può essere la previsione, un'altra ancora i fabbisogni dei componenti di produzione, altre fonti possono essere la giacenza o la scorta minima, In generale tutte le informazioni presenti in AS/400 possono concorrere alla costruzione di una fonte di disponibilità.
Esiste una libreria di fonti codificate :  giacenza, scorta minima, fabbisogno rilasciato di produzione, fabbisogno pianificato, previsione di vendita, ordine di acquisto, ecc...; ciascuna controllata da una tabella di impostazione, nella tabella possono essere anche chiamati programmi di exit che intervengono sui valori ritornati dalla fonte. Oltre alle fonti codificate è possibile anche creare delle fonti utente che implementano regole specifiche e possono anche leggere informazioni esterne al sistema.
Una menzione particolare meritano : 
 * scorta datata, che permette di spostare la data di fabbisogno associata alla scorta minima alla data run + lead time, in questo modo non abbiamo fabbisogni dipendenti scaduti per effetto della scorta minima
 * eccedenze pianificate, in fase di elaborazione MRP il sistema è in grado di identificare due tipologie di eccedenze :  quelle esistenti di materiale già presente e non richiesto; quelle pianificate, che al momento non sono presenti ma che potrebbero costituirsi per effetto delle lottizzazioni. Conoscere le eccedenze pianificate e valorizzarle permette una più consapevole gestione e approvazione dei suggerimenti di pianificazione
 * fabbisogni trascurati,che permette di impostare una soglia minima al di sotto della quale il suggerimento di copertura assume una fonte diversa. Questo permette di evitare suggerimenti pianificati a copertura di fabbisogni trascurabili
 * scorta trascurata, simile alla precedente, in questo caso la soglia è riferita alla copertura della scorta :  si trascura un fabbisogno di quantità minima che serve unicamente alla ricostituzione della scorta.
 * fonte bilanciata, che permette la fusione di gruppi di altre fonti e di una fonte guida, in questo modo si possono ottenere, con regole diverse, le risultanze della fusione tra previsioni e ordini acquisiti. La particolarità della fonte bilanciata è che questa fusione tra previsione e fabbisogno consolidato può essere fatta anche ai livelli inferiori di distinta, utile in particolare ad esempio per la pianificazione della materia prima di processo (alluminio, plastica, componenti chimici)

Le varie fonti impostate possono essere raggruppate in gruppi fonte, gruppi fonte diversi possono dar luogo a figure diverse di disponibilità (es. un gruppo fonte può includere anche le scorte minime, mentre un altro può non considerarle, oppure si possono comprendere o escludere le previsioni, ecc...). L'elaborazione MRP parte con un gruppo fonte generale, specificato nei parametri di lancio, ma può cambiare gruppo fonte dinamicamente durante l'elaborazione utilizzando quello previsto dalla politica associata all'articolo in esame.

![M5_06](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_06.png)
## Politiche e parametri di pianificazione
Attraverso le politiche si determinano le tipologie di raggruppamento da apportare ai fabbisogni netti, quale fonte utilizzare per la pianificazione delle coperture, se attivare un concetto di fonte trascurata, che regole utilizzare per la determinazione del fornitore preferenziale nel caso di coperture di acquisto o di conto lavoro. La politica determina anche se, durante la pianificazione MRP, si debba considerare il gruppo fonte di lancio MRP oppure se utilizzare un gruppo fonte particolare per questa politica (es. generalmente le giacenze dei non conformi non entrano in MRP ma potrei voler considerare le SK elettroniche non conformi da rilavorare). I parametri di pianificazione che l'elaborazione MRP utilizza, possono essere gestiti a livello di dettaglio articolo (articolo/codice di rottura) oppure a livelli di classe articolo o generici per plant (questi livelli sono fino a sei e possono essere qualsiasi attributo dell'articolo), con risalite anche composte ("a pettine"), questa impostazione permette una gestione dei parametri su tanti articoli attraverso la manutenzione di pochi record.

![M5_004_01](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_004_01.png)
## Controllo capacità (CRP)
Il controllo della capacità produttiva si ottiene, innanzitutto impostando le fonti degli ordini di produzione rilasciati in modo da considerare come data di disponibilità la data di fine dell'ultima fase schedulata a capacità finita. Per quanto riguarda invece i suggerimenti di produzione pianificati si possono generare gli "impegni risorse pianificati". Gli impegni risorse pianificati possono essere schedulati a capacità infinita al più presto o al più tardi o in entrambi i modi. Il piano dei fabbisogni di capacità può essere importato in MPS per eseguire il confronto con la disponibilità risorse.

## Scenari
L'MRP prevede l'utilizzo di "scenari" questa caratteristica rende possibile eseguire delle elaborazioni di simulazione utilizzando politiche e gruppi fonte diverse, per ogni scenario è possibile analizzare i suggerimenti proposti e verificarne gli indici.

## Pianificazione per oggetto di rottura
Nella elaborazione MRP si possono introdurre degli "oggetti di rottura" in modo da eseguire delle pianificazioni indipendenti, in cui viene eseguito un bilancio si fabbisogni e coperture all'interno dell'oggetto di rottura. Anche i parametri di pianificazione possono essere differenziati per oggetto di rottura, sempre mantenendo il concetto di risalita a pettine. Gli oggetti di rottura previsti sono :  la commessa, l'ente (tipicamente il fornitore o il cliente), la configurazione, l'esponente di modifica. Un accenno specifico va fatto per la "pianificazione per destino" in cui l'oggetto di rottura è il terzista e la pianificazione considera parametri specifici tra cui anche le scorte per ciascun terzista.

## Scheda MRP
I suggerimenti possono essere considerati come una matrice di fonti positive e negative con un legame verticale che è rappresentato dalla distinta tra un ordine e i suoi impegni ed un legame orizzontale rappresentato dai fabbisogni e dalle coperture datate.

![M5_08](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_08.png)
Per l'analisi dei suggerimenti è stata realizzata una funzione di navigazione grafica che permette di eseguire le analisi in orizzontale tra fabbisogni e coperture e l'analisi in verticale tra i vari livelli della distinta realizzando un pegging dinamico in discesa dalla domanda indipendente fino alle coperture dei materiali base ed al contempo il pegging in salita dai materiali base fino alla domanda che da questi viene soddisfatta, sfruttando le analogie con la distinta base sono state realizzate anche delle funzioni di esplosione ed implosione a "scalare". In implosione è possibile simulare l'effetto sugli assiemi superiori, ed in particolare sui fabbisogni indipendenti, provocato da un "peggioramento" (riduzione di quantità e/o ritardo della data di consegna) di una copertura :  vengono evidenziati i fabbisogni che diverrebbero non più evadibili alle date previste, con la relative quantità non fattibili.

## Pianificazione multiplant
Si può anche attivare una pianificazione multiplant in cui i vari plant sono "in serie" :  un articolo viene prodotto da un solo plant (il plant responsabile) e viene poi distribuito agli altri plant con un meccanismo di ordini di trasferimento tra plant.
La pianificazione può essere eseguita in tre modi, ciascuno corrispondente a una diversa necessità applicativa : 
 * **Cumulata**; vene eseguita una pianificazione unica per tutti i plant impostati nel gruppo fonti di lancio. Il primo plant di questo gruppo assume il significato di plant master :  viene utilizzato per reperire i dati di pianificazione e per pianificare i nuovi ordini.
 * **Lanciata singolarmente**; si esegue una pianificazione separata per plant (il gruppo fonti deve contenere un solo plant). Ogni pianificazione sostituisce soltanto la precedente dello stesso plant.
 * **Completa**; si esegue una pianificazione completa per tutti i plant presenti nel gruppo fonti. Ogni plant viene pianificato singolarmente, con suggerimenti di trasferimento dal plant di competenza (avendo impostato opportunamente i parametri di pianificazione

![M5_09](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_09.png)
## Indici per Kernel
Il Kernel che rappresenta l'oggetto di pianificazione è l'unità alla quale si applica l'elaborazione MRP il kernel è composto da Scenario - Plant Articolo - Codice di rottura. Alla fine dell'MRP vengono elaborati degli indici che rappresentano a quantità e valore dei macrofenomeni legati alla pianificazione. Ad esempio il numero di suggerimenti scaduti, i giorni medi di ritardo, il valore dei suggerimenti di eliminazione, di produzione, acquisto o conto lavoro, il valore delle quantità eccedenti, esistenti o future, il valore delle scorte minime, ecc... Tutti gli indici vengono calcolati considerando il kernel. Ci sono 26 indici calcolati, che permettono di analizzare l'andamento della pianificazione nel tempo, focalizzandosi sugli indici più rappresentativi della performance ricercata. È possibile anche aggiungere altri indici specifici dell'implementazione. Sempre all'interno della scheda MRP è possibile vedere il dettaglio, per articolo, delle quantità superflue, per identificare i maggiori contributori di obsolescenza ed inefficienza

## Impostazione "client" dell'MRP
L'applicazione di MRP è concepita con una impostazione "client" infatti i confini con le applicazioni esterne sono limitati e ben definiti (fonti, suggerimenti, interfacce articolo e enti) questo permette anche una facile introduzione del nostro MRP anche all'interno di altri sistemi ERP.

## Utilizzo come indicatore della bontà gestione
Gli strumenti di pianificazione forniti possono essere anche utilizzati per una visione a 360° di quale sarà l'andamento dell'azienda nell'immediato futuro, infatti oltre ai materiali e alle risorse si possono controllare : 
 * l'evoluzione pianificata della valorizzazione del magazzino
 * il fabbisogno di materiali e risorse per la movimentazione e lo stoccaggio (contenitori, spazi, ripiani, ...)
 * il fabbisogno di risorse produttive secondarie (attrezzature, impianti, energia, .....)
 * e qualsiasi altra risorsa o strumento possa essere messa in relazione ad una quantità di un articolo

## Esempi di output
![M5CMRP_020](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_020.png)![M5CMRP_037](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_037.png)![M5CMRP_034](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_034.png)![M5CMRP_03](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_03.png)![M5CMRP_033](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_033.png)![M5CMRP_029](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_029.png)![M5CMRP_030](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5CMRP_030.png)
# ATP multilivello
Permette di determinare con precisione la data di disponibilità di un nuovo ordine di vendita. Il calcolo si sviluppa su tutti i livelli della distinta considerando sia la disponibilità dei prodotti finiti che dei componenti. Per gli articoli di produzione si può anche attivare la verifica della capacità produttiva.

![M5_10](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_10.png)
L'ATP cioè si basa sul concetto di "disponibilità libera" cioè al netto della quota di impegni passati e futuri già consolidati e coperti.

# MPS
Ogni qualvolta i tempi di consegna consentiti dal mercato sono più stretti rispetto al lead time cumulato è necessario ricorrere alle previsioni per costituire delle scorte, agli opportuni livelli, per premettere tempi di consegna più veloci al ricevimento degli ordini.

![M5_05](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/M5_05.png)
Lo strumento utilizzato per la gestione delle previsioni è l'MPS, che si basa su : 
 * viste piano
 * piano
 * azioni (processi di gestione di piani e viste)

## Viste piano
Rappresentano le quantità sviluppate lungo i periodi, i periodi possono essere fino a 120 e possono avere ampiezza variabile in funzione della definizione del piano.

![MP_001_04](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/MP_001_04.png)
La vista può rappresentare la figura del fatturato consuntivo per cliente / articolo, un'altra vista può raffigurare la previsione di vendita per zona / famiglia, un'altra può rappresentare il budget di ore previste per risorsa.

## Piano
Il piano è il contenitore delle viste collegate tra di loro che hanno tutte lo stesso sviluppo temporale ed appartengono allo stesso contesto applicativo. Il piano è caratterizzato da una data iniziale e da 120 periodi che possono essere giorni, settimane o mesi. Periodi diversi possono anche essere presenti contemporaneamente nel piano (es. 60 giorni + 40 settimane + 20 mesi).

![MP_001_05](http://localhost:3000/immagini/MBDOC_VIS-AAPIA/MP_001_05.png)
## Azioni
Eseguono tutte le funzioni di creazione delle viste da fonti esterne, o di calcolo di una vista a partire da altre appartenenti allo stesso o ad altri piani. Le azioni sono raggruppate in processi che eseguono in sequenza un flusso costituito da più azioni.

## Versatilità
Grazie al fatto che le viste possono essere intestate ad una coppia qualsiasi di oggetti e che i periodi del piano possono avere un'ampiezza variabile, anche mista, con l'MPS possiamo rappresentare fenomeni aziendali dei più vari : 
 * lo storico ordinato o fatturato, in valore o quantità, per cliente articolo o sintetizzato per un attributo qualsiasi (es. classe materiale / zona)
 * la previsione di vendita (eventualmente ottenuta a partire dallo storico applicando regole di estrapolazione dipendenti dal trend e della stagionalità
 * il fabbisogno tempificato delle risorse legato ad un piano di produzione
 * il fabbisogno tempificato dei contenitori per l'imballo dei prodotti finiti
 * i flussi di cassa attivi e passivi
 * ecc.....

# Applicazioni utilizzate
Le applicazioni Sme.UP a supporto della gestione della produzione interna sono : 
 * __Plan.UP__, per la gestione dei piani
 * __Marp.UP__ per la pianificazione dei materiali
