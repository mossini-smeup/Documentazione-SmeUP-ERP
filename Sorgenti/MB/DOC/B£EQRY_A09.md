# Introduzione

A fianco degli oggetti standard smeup può nascere l'esigenza di definire degli oggetti custom (es. basati su archivi di altre applicazioni). Questi oggetti possono essere implementati attraverso la classe "*D", di cui si riporta a seguire la relativa documentazione.

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

- [B§O - Relazione oggetto-database](Sorgenti/ST//B§O)
- [CQ3 - Definizione calcolo costo](Sorgenti/OG//Q3)
- [](Sorgenti/MB/QILEGEN/£IQ3)
 :  : DEC T(MB) P(QILEGEN) K(£K04) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£EQRY_AOX) L(1)

# Altre estensioni dell'oggetto Ufo
Un oggetto ufo può inoltre essere esteso, con tutte le caratteristiche degli altri oggetti smeup (es. attributi, utilizzo nello combo, ricerca per descrizione ecc.), ma per questo si rimanda alla documentazione delle classi standard, qui riportata a seguire.

# Azioni sull'oggetto Ufo
Implementare nel programma B£GES0_x (T$B£7E in B£7) eventuali modalità di risoluzione delle azioni di gestione (immissione/modifica/copia/cancellazione/interrogazione)
- inserire nello script B£GES0_U in SCP_SET le eventuali funzioni di risoluzione delle azioni di gestione di cui sopra (immissione/modifica/copia/cancellazione/interrogazione)
- inserire nello script B£OGGE_OG/B£OGGE in SCP_MNUPER l'eventuale gestione del "nuovo" per l'oggetto

 :  : I.INC.MBR Fil(DOC_OGG) Mem(OG_OG_N)




