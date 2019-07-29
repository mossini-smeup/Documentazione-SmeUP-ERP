
# Generalità

Il Processo di schedulazione si compone delle seguenti fasi : 

- Preparazione dati di input (riempimento memorie)
- Loop di selezione e schedulazione
- Operazioni finali
- Presentazione risultati e interazione con l'utente
- Memorizzazione risultati su disco

Nel seguito esponiamo, per ognuna di queste fasi, le exit che vengono richiamate. Alcune di esse sono richiamate in più punti, naturalmente con funzioni/metodi diversi. Può inoltre verificarsi in caso di "ricongiunzione" di più exit in una mongolfiera, ma questa modalità è di totale responsabilità di chi le implementa.

#  Preparazione dati di input

## Istante Partenza Disponibilità Risorsa
 :  : DEC T(OJ) P(*PGM) K(S5SMES_T1) L(1)
Per ogni risorsa viene eseguito (all'atto del caricamento iniziale delle risorse, S5SMES_01R) S5SMES_T1 di calcolo istante di partenza di disponibilità risorsa. Questo programma viene lanciato anche da S5SMES_03 (di reinizializzazione campi risorse).
L'istante di partenza di disponibilità risorsa può essere variato (ritardato) per ogni singola risorsa tramite la exit S5SMX_16x, che riceve la risorsa in £A02 e può modificare direttamente il relativo elemento di DSRISO nei campi data e ora inizio disponibilità risorsa.


##  Costruzione DSIRIS e DSSINT
 :  : DEC T(OJ) P(*PGM) K(S5SMES_01I) L(1)

Il programma S5SMES_01I lancia : 


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_02X) L(1)
nel loop di caricamento dell'S5IRIS in memoria (S5IRIS), in due punti :  prima e dopo i controlli di appartenenza del record ai filtri impostati. Può modificare la DS del record o imporre di non   caricarlo. Questi richiami sono precedenti alla scrittura dell'elemento di DSIRIS :  questa memoria è riempita fino all'elemento precedente. Se si volesse scrivere un'estensione orizzontale a DSIRIS, essa va posta nell'elemento £T01+1.Viene inoltre lanciato all'inizio e alla fine del caricamento, rispettivamente per inizializzare memorie private e per poter seguire azioni globali (che possono essere eseguite solo a caricamento completo).

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_15X) L(1)
all'atto della scrittura della DSSINT (una per ogni ordine), ad ogni rottura di ordine negli impegni che si stanno scandendo (l'elemento di DSIRIS che provoca la rottura è già stato scritto). Permette di modificare la data obiettivo sull'elemento di DSSINT (che è stato già scritto, ad eccezione della data obiettivo), sostituendo il default (data fine richiesta) con il valore eventualmente ritornato in S5FILE. Riceve la DS di S5SIRIS (la data fine richiesta dell'ordine è riportata su tutti i suoi impegni).Dato il punto in cui viene richiamato, potrebbe essere utilizzato come exit di DSSINT (con le dovute accortezze), ad esempio modificando la commessa dell'ordine.La presenza di questa exit viene controllata nei programmi di presentazione (matrici e Gantt), per mostrare la colonna "Data obiettivo", in quanto, se assente, sarebbe una colonna identica alla "Data fine richiesta".

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_09X) L(1)
Al termine del loop di caricamento lancia S5SMES_07 (di gestione appuntamenti tra livelli) in inizializzazione, che a sua volta lancia S5SMX_09x, di acquisizione legami tra ordini (a meno che sia impostato un tipo distinta standard, nel qual caso lancia il programma di acquisizione standard S5SMES_09.

## Alternative

 :  : DEC T(OJ) P(*PGM) K(S5SMES_01K) L(1)

lancia : 

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_07X) L(1)
 dopo avere scritto ogni DSALTE, passando il puntatore della DSIRIS (£A01) e di DSALTE (£A03), passando la DS di S5IRSE (che contiene la risorsa secondaria di tipo RISP :  risorsa specifica), e a totale, dopo aver scritto tutte le DSALTE di un DSIRIS, passando il puntatore della DSIRIS (£A01) ma lasciando a 0 quello di DSALTE (£A03) e non passando la DS di S5IRSE.

## Completamento Inizializzazione

 :  : DEC T(OJ) P(*PGM) K(S5SMES_06) L(1)
 lancia  in sequenza  le exit : 

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_05X) L(1)
 in inizializzazione, per preparare un'eventuale memoria privata da sfruttare in questa attività nei richiami successivi, nel loop di selezione S5SMESS_11E (riferirsi alla documentazione delle exit di questo programma per il dettaglio di questi richiami).

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_14X) L(1)
in inizializzazione, per preparare un'eventuale memoria privata da sfruttare in questa attività nei richiami successivi, nel loop di selezione

 :  : DEC T(MB) P(BCDSRC) K(S5SMES_11E) L(1)
 (riferirsi alla documentazione delle exit di questo programma per il dettaglio di questi richiami).

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_26X) L(1)
 in inizializzazione, per preparare un'eventuale memoria privata da sfruttare in questa attività nei richiami successivi, nella gestione dei legami statici,

 :  : DEC T(MB) P(BCDSRC) K(S5SMES_07) L(1)
 nel loop di selezione (riferirsi alla documentazione delle exit di questo programma per il dettaglio di questi richiami).

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_11X) L(1)
 di inizializzazione generale, dopo aver costruito tutte le memorie.


# Loop di selezione e di schedulazione

Questa fase, a sua volta, si divide in due parti.
La prima è la selezione dei dettagli degli impegni in corso, e dei dettagli degli impegni pronti a capacità infinita :  ogni dettaglio viene passato alla funzione di schedulazione (S5SMES_16 e dipendenti), che verrà esposta nel seguito.
La seconda è il vero e proprio motore di schedulazione

## Selezione dettagli
 :  : DEC T(OJ) P(*PGM) K(S5SMES_11E) L(1)
viene richiamato per N volte per quanti sono gli impegni non schedulati nel passo precedente, e ad ogni richiamo sceglie il miglior dettaglio da schedulare, lancia le seguenti exit : 

Prima del loop sugli impegni pronti (all'inizio di ogni richiamo) lancia : 


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_14X) L(1)
 scelta iniziale di un dettaglio, con funzione RIT. Questo programma può : 
selezionare un dettaglio (valorizzando £A05) nel qual caso il programma termina e questo dettaglio viene schedulato (dall'esterno è come se fosse stato scelto dalla strategia. Attenzione a questo implemento in quanto non viene eseguire il controllo che il dettaglio appartenga a un impegno pronto, né che alteri una coda congelata).Tornare £A05 a zero, nel qual caso il programma prosegue normalmente, tornare £A05 a zero e impostando END nel messaggio, nel qual caso, oltre a far proseguire il programma normalmente, impone di non essere più richiamato, in quanto ha completato la parte di schedulazione di sua competenza (ad esempio se si esternalizza in questo programma la schedulazione della prima fase, quando tutti i suoi impegni sono stati trattati, il motore prosegue normalmente con le fasi successive, senza perdere tempo a richiamare questa exit).


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_05X) L(1)
spinta in partenza, con funzione PAR, per eseguire impostazioni e inizializzazioni da eseguire ad ogni lancio di selezione dettaglio (che integrano quelle eventualmente eseguite all'inizializzazione generale), che potranno essere utilizzate in seguito, dato che questa exit verrà eseguita in altri punti di questo programma

## Loop Selezione Miglior dettaglio
Come prima cosa viene controllata la presenza di un gruppo con tutti gli impegni schedulabili (pronti o già schedulati).
Se è così viene scandito solo quel gruppo, altrimenti vengono scanditi tutti i gruppi.
Si rimanda alla documentazione specifica dell'ottimizzazione gruppi e della sua disattivazione per un'analisi dettagliata di questo argomento.
Per ogni gruppo che abbia almeno un impegno pronto si scandiscono i suoi dettagli (che sono in ordine di CROR e di impegno).
Si saltano i dettagli già elaborati (XGSTAT non vuoto :  o schedulato (S) o eliminato (E), in quanto selezionato un altro dettaglio dello stesso impegno) o esclusi (XGTFAS uguale a 'E' :  controllo dipendente da exit utente in quanto il sistema non valorizza questo campo a 'E', utile per restringere in modo personale i dettagli, e quindi le risorse specifiche, in base a considerazioni che possono essere anche essere fatte durante la schedulazione, quando si rende pronto un impegno di cui si vogliono escludere alcuni dettagli).
Si aggancia l'impegno e, se pronto, si lancia (a rottura di impegno DSIRIS) il controllo di sospensione S5SMX_12x, passandogli in £A01 il puntatore di DSIRIS. Se questo controllo ha esito negativo, i dettagli dipendenti da questo impegno vengono saltati.
NB :  se gli impegni costituiscono un batch, viene eseguito automaticamente il controllo che siano tutti pronti. Se questo controllo ha esito positivo, l'eventuale controllo personale di sospensione viene eseguito, immediatamente dopo, sull'impegno master del batch.
Il controllo di sospensione può essere utile quando si implementa una strategia di schedulazione globale di un gruppo G (con l'exit S5SMX_14x). Se non tutti gli impegni di G sono pronti, questa exit, eseguita all'inizio del programma, non torna nessun dettaglio schedulabile, quindi il programma segue la sua strada, e nel seguito potrebbe scegliere un dettaglio di G, scardinando la strategia. È quindi necessaria una exit che sospende tutti gli impegni di G. Infatti, quando saranno tutti pronti, sarà la exit iniziale a tornare in sequenza (uno ad ogni richiamo) i dettagli di questo gruppo, e quindi la sospensione lanciata successivamente sarà ininfluente.
Si può dare una rappresentazione scacchistica del controllo di sospensione. Sta al bianco muovere (la mossa corrisponde alla scelta del dettaglio da schedulare). Su una riga, all'estrema destra c'è il re bianco, e nella casella immediatamente a sinistra, un pedone bianco, mentre, più a sinistra, sulla stessa colonna, c'è una torre nera che lo minaccia. Il pedone bianco non può avanzare, in quanto metterebbe sotto scacco il re :  è una mossa "sospesa". Se in seguito, o perché la torre o il re si spostano di colonna, o perché tra la torre e il pedone si intromette un altro pezzo (che non sia l'altra torre o la regina nera!), questa mossa non è più sospesa, e può quindi essere presa in considerazione.
A questo punto, si controlla se l'impegno (pronto) del dettaglio in esame è congelato ed è il primo della coda :  se è così si schedula direttamente questo dettaglio (si lancia S5SMES_16, senza andare a fine programma) e si prosegue nell'analisi della coda congelata, arrestandosi quando si trova un impegno congelato non pronto, nel qual casi si salta ad un altro gruppo.
Ricordo che in questo caso il controllo iniziale di un gruppo totalmente schedulabile non avrebbe avuto esito positivo, e quindi si stanno trattando tutti i gruppi.
Arrivati a questo punto, si sta trattando un dettaglio di un impegno pronto e non congelato. Si deve determinare l'istante al più presto in cui esso può essere eseguito (IPP) per metterlo in competizione con tutti gli altri e scegliere il più basso.
A rottura di impegno si sceglie il miglior dettaglio dell'impegno, che è quello che può essere eseguito per primo (IPP più basso).
Normalmente lo si fa con il programma standard S5SMES_12E (che torna il dettaglio £A05 con l'IPP, più basso, dove l'IPP è il maggiore tra l'IRS e il VPP :  se vi sono più dettagli con lo stesso IPP, si sceglie quello con IRS più basso, vale a dire la risorsa ferma da più tempo); se è presente, lo si fa con la exit di spinta S5SMX_05x con funzione DET. A questo programma si passa l'impegno £A01 e vengono ritornati il dettaglio £A05 e l'IPP. Attenzione :  la exit sostituisce integralmente il programma standard, e quindi è cura di chi lo realizza di far tornare comunque un dettaglio £A05 (ad esempio, se la spinta è solo finale, basta richiamare, all'interno di esso, il programma standard £S5SMES_12E). Se non lo si facesse, sarebbe un modo subdolo (e rischioso) di sospendere l'impegno, posto che il mancato ritorno del miglior dettaglio sia provvisorio (avvenga solo in determinate condizioni) e, in richiami successivi, questa condizione venga superata.
Va precisato che, mentre la spinta finale (che verrà esposta in seguito) sceglie esplicitamente il dettaglio da schedulare, la spinta a dettaglio sceglie (con un criterio diverso dalla semplice saturazione, che farebbe scegliere il dettaglio con IPP più basso) il miglior dettaglio di ogni impegno da mettere in competizione con gli altri dettagli. La competizione tra i 'migliori' dettagli (uno per impegno) avviene comunque in base alla saturazione (ovvero all'IPP più basso).
Se invece si vuol implementare una strategia ad hoc, lo si deve fare nella exit di spinta a dettaglio.
Ad esempio, se c'è una risorsa preferenziale, essa può essere scelta con considerazioni specifiche :  ad esempio se la sua scelta produce una hole inferiore di un valore stabilito.
Si rimanda al documento specifico di esempio di risorsa preferenziale per un'esposizione dettagliata dei casi possibili.

Se il dettaglio ha un IPP minore a quello attualmente più basso (oppure uguale ma con CROR minore o uguale, diventa il dettaglio potenzialmente da schedulare. A questo punto, si può lanciare (lo si fa solo sul dettaglio attualmente scelto) la exit S5SMX_21x, che permette di modificare (avanzandolo) l'IPP, a cui si passa il dettaglio £A05 e da cui si riceve un istante, che sostituisce, se maggiore, il suo IPP.
Questa sostituzione non altera la classifica dei migliori dettagli, in quanto lo spirito di questa exit è di introdurre un vincolo ulteriore, non di sostituire quello della risorsa. Un dettaglio scartato perché superiore a quello che si considera non avrebbe potuto superarlo. Infatti, o è il primo dettaglio, o è un dettaglio "di suo" minore del precedente, e allora sarebbe stato considerato, o è un dettaglio "di suo" maggiore del precedente, e quindi sarebbe stato scartato. Riferirsi al documento specifico per un'esposizione dettagliata di questo concetto. Va ricordato che, dato che viene passato solo il miglior dettaglio dell'impegno, il vincolo che si può aggiungere in questa exit può dipendere solo dall'impegno e non dal dettaglio (ad esempio dall'articolo ma non dalla risorsa specifica).

Al termine del loop, dopo aver scelto un dettaglio, lancia S5SMX_05x di spinta, con funzione FIN, passando il dettaglio selezionato in £A05. In questa fase si può "brutalmente" selezionare un altro dettaglio (sempre in £A05), che verrà schedulato senza nessuna verifica che esso appartenga a un impegno pronto, né che alteri una coda congelata.
Questa spinta finale può essere utilizzata in una scelta "minimale" della risorsa preferenziale :  si scandiscono i dettagli dello stesso impegno. Se, tra di essi, quello sulla risorsa preferenziale produce un ritardo accettabile, sostituisce quello selezionato. Con questa scelta non si è comunque protetti dal fatto che sulla risorsa preferenziale si sarebbe potuto eseguire un dettaglio più urgente.


## Schedulazione dettaglio
 :  : DEC T(OJ) P(*PGM) K(S5SMES_16) L(1)

La funzione di schedulazione del dettaglio scelto si compone di vari programmi, per comprendere il loop di schedulazione in tiro (sia manuale sia batch) :  il programma di partenza di questa funzione è S5SMES_16.

Il programma vero e proprio di schedulazione (datazione del dettaglio, resa pronta della fase successiva, avanzamento dell'istante di inizio della disponibilità della risorsa, ecc...) S5SMES_13 lancia le seguenti exit (passando a tutte il dettaglio £A05 che si sta schedulando.

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_04X) L(1)
prima di datare il dettaglio, se presente il tempo di attrezzaggio, per ricalcolarlo o, se è il caso, azzerarlo.

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_01X) L(1)
subito dopo aver datato il dettaglio ricevuto, senza aver fatto altre operazioni.

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_19X) L(1)
per rettificare (avanzandolo) l'istante di inizio di disponibilità della risorsa del dettaglio appena schedulato, passando l'istante di fine di questo dettaglio. Questa exit può avanzare questo istante (ad esempio per non far iniziare un nuovo dettaglio a fine giornata), lasciando inalterato quello di fine schedulazione del dettaglio. Questa correzione viene eseguita prima del calcolo delle hole, quindi, nel caso di avanzamento, verrà creata una hole tra la fine del dettaglio e l'inizio della disponibilità della risorsa.

 :  : DEC T(MB) P(BCDSRC) K(S5SMX_27X) L(1)
con funzione FIN, prima di aggiornare, sulla DSRISP se RSV, l'istante di fine disponibilità. Questa exit permette di avanzare l'impegno delle RSV in modo personale. La funzione FIN è eseguita dalla parte standard della exit, quindi è sufficiente implementare il richiamo di calcolo avanzamento istante. Tecnicamente entrambi i richiami vengono eseguiti (direttamente o indirettamente) in questo programma (S5SMES_13) che aggiorna l'occupazione della RSV, lanciando S5SMES_76 e S5SMES_77 (che possiede le memorie specifiche RSV e lancia la exit di eventuale avanzamento). In seguito S5SMES_13 aggiorna l'istante di fine occupazione per tutte le risorse secondarie (anche di quelle di segnalazione) che normalmente è l'istante di fine della schedulazione del dettaglio. Per la RSV viene lanciata, se presente, la exit che ritorna l'istante appena calcolato (viene controllato che il dettaglio sia lo stesso). La exit di avanzamento viene richiamata nel S5SMES_77 per il calcolato e la registrazione nella memoria privata, nel S5SMES_13 per la registrazione in quella pubblica.

 :  : DEC T(MB) P(BCDSRC) K(S5SMES_07) L(1)
viene lanciato (con funzione APP) in questa fase per rendere pronte le prime fasi dei livelli superiori quando tutti i livelli inferiori sono conclusi, che vengono rese pronte all'istante più alto della fine dei livelli inferiori. È possibile, in questo programma, al posto della sovrapposizione tra livelli standard, una sovrapposizione utente, tramite la exit S5SMX_26x, lanciata con funzione SOV, per ogni impegno di livello superiore che è stato reso pronto dal dettaglio schedulato, ricevendo l'impegno stesso in £A01 e una schiera (con il relativo riempimento) di tutte le sintesi (completate) di livello inferiore di cui era in attesa.

## Tiro
 :  : DEC T(OJ) P(*PGM) K(S5SMES_15) L(1)
Il programma che esegue il tiro è S5SMES_15, lancia la exit : 


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_03X) L(1)
quando il dettaglio appena schedulato è dalla frontiera in poi. In assenza di batch la frontiera è l'ultimo dettaglio della zona iniziata e congelata. In presenza di batch è l'ultimo impegno slave dell'ultimo batch di questa zona.
Alla exit di tiro viene passato, la priva volta, il dettaglio tirante £A05 con funzione INZ, le volte successive il dettaglio tirato dalla volta precedente (sempre in £A05) con funzione CONT. Ad ogni richiamo si ritorna, sempre in £A05, il dettaglio da tirare, valorizzato a zero per terminare il tiro.
In presenza di batch, il tiro viene comunque lanciato dal dettaglio (£A05) dell'ultimo impegno slave del batch stesso. Se si vuole tirare un altro batch, bisogna prestare attenzione che sia il dettaglio dell'impegno master. I dettagli slave verranno tirati, in seguito, nella parte standard dell'applicazione.


# Operazioni finali
 :  : DEC T(OJ) P(*PGM) K(S5SMES_19) L(1)
Il programma di azioni finali (S5SMES_19), lancia all'inizio l'exit S5SMX_13x, che può eseguire qualsiasi azione sulla memoria, e quindi la restante parte del programma può tenerne conto.
In cascata viene eseguito il programma di calcolo indici (S5SMES_20) che può lanciare l'exit S5SMX_22x, di calcolo degli indici utente (dal 61 al 90) e di eventuale esclusione di tutti gli indici dalla presentazione. Riferirsi al commento interno di questa exit per i dettagli implementativi.


# Presentazione del risultati e interazione con l'utente
I programmi di presentazione matrici e Gantt lanciano la exit S5SMX_06x, che permette di aggiungere/modificare/eliminare colonne dalla presentazione. Nei Gantt è possibile aggiungere segni grafici in una posizione qualsiasi della riga, oltre a linee, sempre in una posizione qualsiasi.
Riferirsi all'help interno a questa exit per l'elenco dei programmi di presentazione interessati e alle modalità di colloquio.

# Gantt di dettaglio
 :  : DEC T(OJ) P(*PGM) K(S5SMES_D4) L(1)
Nel Gantt di dettaglio (S5SMES_D4) in cui l'utente può modificare i risultati della schedulazione (modifica della risorsa specifica, variazione all'ordine di schedulazione) si possono richiamare le seguenti exit : 


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_10X) L(1)
Questa exit è attiva solo se in assenza di risorse specifiche. Riceve, in £A02 la risorsa su principale su cui si vuol spostare e in £A05 il dettaglio che si vuole spostare. Riempiendo una stringa verrà prodotto un messaggio di avvertimento con quella stringa, che dovrà essere confermato per eseguire lo spostamento. Ritornando inoltre nel messaggio "OK" si ha l'effetto che lo spostamento verrà solo segnalato (sempre dandone segnalazione nel messaggio). Questa exit va comunque attivata in concomitanza di una funzione di impostazione da parte dell'utente della nuova risorsa generale.


 :  : DEC T(MB) P(BCDSRC) K(S5SMX_25X) L(1)
Riceve, in £A02 la risorsa su cui si vuol spostare e in £A05 il dettaglio che si vuole spostare (da cui si ricava immediatamente la risorsa in cui è attualmente schedulato). Riempiendo una stringa verrà prodotto un messaggio di avvertimento con quella stringa, che dovrà essere confermato per eseguire lo spostamento. Ritornando inoltre nel messaggio "NO" si ha l'effetto che lo spostamento verrà impedito (sempre dandone segnalazione nel messaggio).

# Visualizzazione andamento RSV
 :  : DEC T(OJ) P(*PGM) K(S5SMES_DO) L(1)
Il programma S5SMES_DO che presenta, in vari modi, le RSV, tra le sue possibilità ha quella di elencare, per ogni RSV, l'andamento della disponibilità residua nel tempo. Per far questo, chiama il programma che ritorna questa informazione (S5SMES_74). Se il calcolo RSV non è standard, a sua volta questo programma esegue la exit S5SMX_24x, che ritorna questo valore calcolato in modo personale- Presumibilmente questa exit sarà un passaggio alla mongolfiera che sovrintende al calcolo delle RSV non standard, in analogia a quanto accade per il caso standard, in cui viene chiamato S5SMES_76 che a sua volta chiama la mongolfiera standard delle RSV S5SMES_77. Si passa alla exit la risorsa secondaria £A16, e si ricevono, in sequenza, nella DS £S5DS01 gli istanti di inizio e fine in cui la disponibilità non varia, e, ovviamente, il suo valore.


# Memorizzazione risultati su disco
 :  : DEC T(OJ) P(*PGM) K(S5SMES_25) L(1)
Nel programma S5SMES_25, di aggiornamento degli impegni risorse con i della schedulazione (istanti di inizio, fine e di vincolo, durata attrezzaggio, ecc..) è possibile richiamare la exit S5SMX_08x in vari punti, con le seguenti funzioni : 
INZ - all'inizio della memorizzazione
PRE - prima dell'aggiornamento di S5IRIS con in £A05 il dettaglio e la DSIRIS già modificata ma non ancora scritta. Se si vuol ottenere la before image basta agganciare il record di S5IRS con l'IDOJ ricevuto (salvando la DSIRIS perché non venga sovrascritta).
POST - dopo l'aggiornamento di S5IRIS (e degli eventuali impegni secondari), con gli stessi parametri della "PRE"
FIN - dopo aver aggiornato tutti i record.








