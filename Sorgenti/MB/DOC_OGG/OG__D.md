# Generalità

Tramite la classe *D è possibile definire dei propri oggetti custom, non previsti dallo standard. Questi oggetti sono comunemente chiamati UFO.

# Struttura

La definizione di un oggetto si completa attraverso il parametro della classe. Per questi oggetti nel parametro va indicato il nome del programma che si occupa di risolvere le istanze della classe. Opzionalmente separato da un "." è inoltre previsto di poter passare un parametro che arriverà nel campo "metodo" al pgm di ufo.

Di seguito viene riportato un pgm di esempio.
 :  : DEC T(MB) P(SMESRC) K(B£DEC_XX1) L(1)

# Estensione degli Oggetti Ufo attraverso gli elementi della B£O** (PROCEDURA CONSIGLIATA)

Di particolare interessi è poi l'utilizzo degli oggetti ufo in combinazione ad un elemento della tabella B£O**. Tramite gli elementi di questa tabella è infatti possibile "mappare" oggetti X su oggetti ufo. Questo, rispetto all'utilizzo diretto degli oggetti ufo comporta alcuni vantaggi : 
* permette di catalogare più tipologie di oggetto separate (es. posso poi applicare la stessa metodologia a diversi tipi oggetto, es. X1, X2 ecc. che non si incrociamo fra loro, invece di avere a disposizione la sola classe *D)
* permette di indirizzare in modo più mirato la parametrizzazione del tipo oggetto specifico. Mentre la classe *D punta direttamente alla ricerca di un pgm, tramite la configurazione della B£O** è possibile indicare parametrizzazioni apposite.
* non ci si scontra con i potenziali problemi che può comportare un codice che contiene/inizia per "*".

Per implementare questa struttura i passi sono i seguenti : 
* Predisporre il pgm di elaborazione dell'ufo (non secondo l'esempio riportato in precedenza, ma secondo quello che è riportato a seguire)
* Inserire nelle istanze della tabella *CNTT, il codice, con carattere iniziale "X" (carattere riservato alle classi custom), con la relativa descrizione, tramite il quale si vorrà identificare il nuovo oggetto (es. codice XA, descrizione oggetto classe XA).
* Inserire nelle istanze della tabella B£O** un elemento con lo stesso codice precedentemente inserito. In questo elemento dovranno essere indicati : 
** come Deviazione Tipo Oggetto :  *D
** come Deviazione Parametro :  il nome del pgm di risoluzione dell'ufo
** come Gest. parametro UFO :  1
** come Tipo Parametro :  l'eventuale tipo oggetto che si vuole utilizzare come parametro (es. TAxxx)
** come Obbligatorietà Parametro :  se il parametro per l'oggetto previsto è obbligatorio "1"

Quando viene implementata questa struttura, l'entry ed i metodi di chiamata per il pgm di ufo sono differenti rispetto a quelle previste quando la struttura della B£O** è assente. Per questa casistica è previsto un ulteriore sorgente di esempio.
 :  : DEC T(MB) P(SMESRC) K(B£DEC_XX2) L(1)

 :  : DEC T(ST) P() K(*CNTT) L(1)
 :  : DEC T(ST) P() K(B£O**) L(1)

# Estensione degli Oggetti Ufo attraverso gli elementi della B§O

Se l'oggetto Ufo appartiene ad un archivio è inoltre possibile esternare tale relazione tramite un elemento della tabella B§O. Questa tabella permette di indicare come l'oggetto può essere identificato sul database. Questa ulteriore parametrizzazione presenta alcuni vantaggi : 
* Possibilità di sfruttare le potenzialità dell'SQL
* Possibilità di avere a disposizione la funzione standard di filtro (si veda documentazione classe Q3, e /COPY £IQ3)

Varie caratteristiche della classe possono poi essere indicate attraverso l'exit della £K04.

Se l'archivio a cui punta l'oggetto è un archivio che non è un archivio standard smeup, può risultare inoltre interessante poter indicare l'oggettizzazione di ogni campo di tale file. Questo può avvenire attraverso il pgm di exit B£EQRY_AOX.

 :  : DEC T(ST) P() K(B§O) L(1)
 :  : DEC T(OG) P() K(Q3) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£IQ3) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£K04) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£EQRY_AOX) L(1)

# Altre estensioni dell'oggetto Ufo
Un oggetto ufo può inoltre essere esteso, con tutte le caratteristiche degli altri oggetti smeup (es. attributi, utilizzo nello combo, ricerca per descrizione ecc.), ma per questo si rimanda alla documentazione delle classi standard, qui riportata a seguire.

# Azioni sull'oggetto Ufo
Implementare nel programma B£GES0_x (T$B£7E in B£7) eventuali modalità di risoluzione delle azioni di gestione (immissione/modifica/copia/cancellazione/interrogazione)
- inserire nello script B£GES0_U in SCP_SET le eventuali funzioni di risoluzione delle azioni di gestione di cui sopra (immissione/modifica/copia/cancellazione/interrogazione)
- inserire nello script B£OGGE_OG/B£OGGE in SCP_MNUPER l'eventuale gestione del "nuovo" per l'oggetto

# Creare un nuovo Oggetto

* inserire l'oggetto come elemento nella tabella *CNTT :  dato che la *CNTT è una tabella cablata, se il nuovo oggetto è standard va aggiunto nel pgm B£AR14, se invece è un oggetto personale forzare l'inserimento in tabella con codice Xn (a questo punto verrà scritto nel TABEL relativo)
* se l'oggetto è standard definire il modulo proprietario dell'oggetto inserendolo nel programma B£K01G.
* creare il programma B£FUN0_XX, dove XX è il tipo oggetto per attaccare le funzioni specifiche dell'oggetto presentate nel popup, nonchè per tornare classe parametri e contenitore note
* nel pgm B£OAV9 la logica per la determinazione del contenitore note del punto precedente, va qui replicata
* modificare il programma B£G60T, implementando come per gli altri oggetti il reperimento delle informazioni di accesso al database (se l'oggetto appartiene ad un archivio). Casomai sorgesse la necessità di implementare logiche che esulano le possibilità previste dalla struttura del B£G60T, possono essere inserite particolare logiche nella £IVD (cioè il pgm B£IVD0, per il quale si veda ad esempio nel B£IVD0 le considerazioni sull'oggetto CN)
* creare il programma B£OA_XX, dove XX è il tipo oggetto, per gestire gli attributi dell'oggetto
* creare l'interfaccia dell'oggetto, tendenzialmente £IXX, dove XX è il tipo oggetto, sempre che il nome non sia già usato. creare anche il relativo TST.
* inserire l'oggetto nella £DEC andando a modificare il B£DEC0 (è da notare che è attraverso tale implementazione che viene anche riconosciuta l'API che gestisce l'interfaccia dell'oggetto).
* inserire l'oggetto nel B£DEC3 per definirne il parametro
* inserire l'oggetto nel B£DEC4 (se l'oggetto non è un campo di file) o (se l'oggetto è un campo di file) nel B£G60T (se standard) o nella tabella B§O (se personale) per la £G60 e le ricerche in Loocup
* inserire ulteriori caratterizzazioni dell'oggetto nella /COPY £K04 (es. presenza della descrizione, utilizzo del campo negli input panel ecc.)
* se l'oggetto corrisponde ad un archivio mantuenzionabile in Smeup implementarne la relativa struttura : 
** attivare il campo £K04O_GE nella £K04
** implementare nelle schiere in fondo al pgm B£GES0/B£GES0_x (T$B£7E in B£7) l'eventuale modalità di risoluzione delle azioni di gestione (immissione/modifica/copia/cancellazione/interrogazione). Sarà necessario prevedere una combinazione di classe/funzione d'autorizzazioni (tabella B£P da mettere a modello) e probabilmente prevedere il pgm deviatore per la gestione 5250.
** implementare il programma di controllo B£K89_XX, riprendendo il sorgente di esempio in SMESRC B£K89_XX.
** implementare il sorgente del file SCP_A36 avente come codice il tipo oggetto. Si consiglia di partire con la copia del sorgente dell'oggetto AR. In tale script si vedranno presi in considerazione gli script SCP_LAY per i quali nello standard si prevede la codifica tipooggetto_nnn, dove nnn è un progressivo numerico di 3 caratteri. Guardando l'SCP_A36 si evincerà la possibilità di prevedere un SCP_LAY diverso per device. E' inoltre importante che tutti gli scp_lay standard (salvo quello dedicato alla pre-immissione) prevedano l'impiego delle istruzioni I.Fld Tip="NOT" e I.Fld Tip="PAR".
** inserire nello script B£GES0/B£GES0_U in SCP_SET il richiamo della scheda di gestione dell'oggetto che corrisponderà direttamente alla scheda A36, o consisterà in una scheda più complessa che per la manutenzione dati richiamerà la scheda A36.
** Per un maggior dettaglio si rimanda anche al documento applicativo relativo alle azioni di gestione di un oggetto, previsto dal modulo B£BASE
* inserire nello script B£OGGE_OG/B£OGGE in SCP_MNU l'eventuale gestione del "nuovo" per l'oggetto
* se opportuno implementare : 
** lo schema di default da applicare nelle matrici dove sono elencate le istanze dell'oggetto (es. nelle ricerche) attraverso l'oggetto Q2. Si veda la documentazione della relativa classe.
** lo schema T/Q3 da applicare nella funzione di filtro generale in modo nell'F13 vengano presentati nell'ordine ed eventualmente solo i campi ritenuti opportuni.
* documentare l'oggetto in DOC_OGG
* se il nuovo oggetto comporta la creazione di nuove tabelle standard, aggiungerle nel pgm B£OA_ST3 in modo la definizione della tabella venga distribuita nel modello.





