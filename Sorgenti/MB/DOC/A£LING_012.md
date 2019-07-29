# Come scrivere un programma Sme.UP affinché possa essere tradotto
Tutte le parole e frasi presenti in un programma Sme.UP che devono poter essere tradotte, devono essere messe in schiere a tempo di compilazione.
La schiera inoltre deve essere "tipizzata" nel modo corretto.

Questo è un esempio di frase NON traducibile : 
 :  : PAR F(04)
C                   EVAL      PIPPO='Descrizione Articolo'


La "tipizzazione" delle schiere va scritta nel campo commento della prima specifica D di definizione della schiera.
La tipizzazione corretta è formata dal carattere "_" seguito da un oggetto di tipo V2A£TSK.
Sono quindi definizioni di schiera valide le seguenti : 
 :  : PAR F(04)
D SCH1             S            100    DIM(5) CTDATA PERRCD(1)              _TXT
D SCH2             S             80    DIM(50) CTDATA PERRCD(1)             _£FEM
D SCH3             S             50    DIM(5) CTDATA PERRCD(1)              _TXT_S05,10


Chiaramente la tipizzazione deve essere concorde con il testo presente nella schiera.
Alcuni esempi : 
Se una schiera contiene solo testo, bisogna indicare _TXT
Se una schiera contiene testo dalla posizione 11 per 30 caratteri, bisogna indicare _TXT_S11,30
Se una schiera contiene la definizione di una matrice, bisogna indicare _£JAXSWK
Se una schiera non contiene testo, bisogna indicare _NOTXT
Per la lista di tutte le possibili tipizzazione, fare riferimento agli oggetti di tipo V2A£TSK.

La tipizzazione, oltre a far riferimento ad un oggetto V2A£TSK deve essere "formalmente" in accordo con la schiera stessa.
Non è possibile, ad esempio, tipizzare una schiera _TXT_S11,30 (30 caratteri dall'undicesima posizione) su una schiera più corta di 40 caratteri.

Per le schiere definite come "alternate", la tipizzazione vale come se fossero schiere separate.
Quindi una schiera definita come : 
 :  : PAR F(04)
D SCH1            S             10    DIM(6) CTDATA PERRCD(1)              _TXT
D SCH2            S             80    DIM(6) ALT(SCH1)                     _TXTS02,20

Avrà testo in tutti e 10 i caratteri della schiera SCH1 e testo nei 20 caratteri a partire dalla posizione 2 per la schiera SCH2

# Supporto del compilatore Sme.UP alla traduzione
Per aiutare il programmatore, il compilatore Sme.UP fornisce un supporto alla gestione delle lingue.
E' possibile abilitare in tabella B£5 due flag di supporto.

"Compil pgm in lingua" (T$B£5I) e "Ctr.costanti pgm" (T$B£5J).

## Compil pgm in lingua (T$B£5I)
Questo campo attiva il supporto vero e proprio per le lingue, ossia il controllo della tipizzazione delle schiere e l'inserimento automatico delle istruzioni per la traduzione delle schiere.
Il controllo della tipizzazione impedisce la compilazione del programma se la tipizzazione indicata per ogni schiera a tempo di compilazione : 
* non è presente
* non è scritta correttamente (non è un oggetto V2A£TSK)
* non concorda formalmente con la schiera (schiera troppo corta)
L'inserimento automatico delle istruzioni per la traduzione determina appunto l'inserimento nel programma di tutte le istruzioni necessarie alla traduzione automatica delle schiere.
Le schiere vengono tradotte secondo quanto indicato nella tipizzazione.
Le istruzioni sono introdotte automaticamente solo nel sorgente temporaneo creato dal precompilatore (£UI_SRC) e non nel sorgente originario.

Questi sono i possibili valori del campo T$B£5I : 
* blank :  supporto attivo solo per librerie standard
* P :  supporto attivo solo per librerie standard e PER
* A :  supporto attivo per tutte le librerie
* N :  supporto non attivo
Il fatto che una libreria sia considerata standard o PER viene valutato sulla base delle variabili V§N.

## Ctr.costanti pgm (T$B£5J)
Questo campo attiva il controllo della costanti non in schiera nei programmi.
Se vengono incontrate istruzioni (nelle specifiche C) che il compilatore interpreta come contenenti testo, viene eseguita l'apposita azione.

E' possibile segnalare al compilatore di saltare il controllo per alcune righe (per evitare false segnalazioni).
Ad esempio l'istruzione
 :  : PAR F(04)
C                   EVAL      PIPPO='ABCDEFGHIJKLMNOPQRSTUVZ'

non contiene testo ma il compilatore la segnalerebbe come tale.
E' possibile indicare nel campo commento di quella riga la keyword COSTANTE per indicare al compilatore di non effettuare il controllo per questa riga.

Questi sono i possibili valori del campo T$B£5J : 
* 1 :  Compilazione arrestata se costanti testuali presenti nel programma
* 2 :  Segnalazione (spool) ma compilazione consentita se costanti testuali presenti nel programma
* blank :  nessuna azione intrapresa se costanti testuali presenti nel programma

## Opzioni di compilazione
Esistono due opzioni di compilazione (COP*) utilizzabili all'interno dei singoli sorgenti :  *NOA£B e *NOLI.
Tali opzioni sono utilizzabile anche per andare in override delle opzioni viste precedentemente.

### COP* *NOA£B
Assume il significato di "gestisco manualmente la traduzione di questo pgm"
* Non viene inserita la £INIZTR (routine di traduzione automatica)
* Viene fatta l'eventuale estrazione delle frasi in schiera
* Controlla la presenza delle costanti in specifiche C (se abilitato in tabella)
* Viene controllata la tipizzazione delle schiere (se abilitato in tabella)
Se non voglio che una schiera venga tradotta bisogna, come nel caso standard, mettere _NOTXT nella tipizzazione della schiera.
### COP *NOLI
Assume il significato di "programma che non ha nulla a che fare con le traduzioni"
* Non viene inserita in automatico la £INIZL
* Non viene controllata la tipizzazione delle schiere (nemmeno se indicato in tabella)
* Non controlla la presenza di costanti nelle specifiche C (nemmeno se indicato in tabella)
* Non vengono estratte le frasi

