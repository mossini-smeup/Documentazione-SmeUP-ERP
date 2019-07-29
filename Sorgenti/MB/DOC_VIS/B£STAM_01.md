# Documenti e stampe in Sme.UP ERP
La situazione relativa all'argomento stampe di Sme.UP attualmente, a fronte della ampiezza e libertà nelle soluzioni disponibili, necessita di semplificazione e razionalizzazione.
Il processo di rivisitazione è iniziato con una cernita delle soluzioni esistenti per i due ambiti coinvolti :  la generazione dei documenti e la produzione cartacea della stampa.
## Il presente
I motori per la generazione, e le peculiarità dei documenti per cui vengono utilizzati, sono : 

- G53 (AS400 standalone)
- REP (Stampa matrice, Report con subreport, etc. tramite Looc.UP)
- H53 (Stampe grafiche con script AS400 e motore Looc.UP)
- AOP (Stampe tramite applicazione server AOP, prodotta da Medusa Informatica e con script e XML)

I motori di stampa invece sono : 

- SmePD (stampa PDF esistenti su remote printer specifiche)
- AOP (stampa PDF contestualmente generati tramite il suddetto)

La situazione, abbastanza variegata, è stata sottoposta ad un lavoro di riorganizzazione, fino a definire la situazione a cui si vuole giungere.
## Il futuro prossimo
A regime la situazione sarà così formata per quanto riguarda la funzioni di generazione dei documenti : 

- H53
- AOP

Le funzioni di produzione cartacea invece resterà identica, almeno finchè AOP non riuscirà a gestire la stampa anche per documenti già esistenti : 

- SmePD
- AOP


## Generazione documenti
### H53
H53 è un componente di  Loocup che è in grado di generare documenti grafici PDF.
Nella H53 confluiranno le modalità di stampa Report ora coperte dal componente REP di Looc.UP. Ciò vuol dire che la funzione "PDF matrice" e "PDF scheda" utilizzabile tramite tasto destro su una matrice confluiranno in una "Stampa matrice" che sfrutterà la H53 per produrre un PDF che riproporrà la situazione di visualizzazione della matrice (raggruppamenti, ordinamenti, filtri, colonne aggiuntive, etc.)
Il componente H53 potrà anche farsi carico delle generazioni G53, ove richiamate tramite Loocup, periferizzando la generazione del PDF e scaricando la CPU AS400 delle funzioni di generazione PDF tramite G53.
H53 potrà anche generare documenti sulla base di script preventivamente definiti nel file SCP_G53 alla stregua di come una scheda Loocup viene generata sulla base di script definiti
Le tipologie di stampa che sarà prodotta da questo componente saranno : 

- Stampa matrice
- Stampe grafiche (es :  Report Q9000 già a standard)
- Stampe grafiche che sfruttano funzionalità di Looc.UP (grafici, immagini oggetti, ecc.)
- Stampe G53 che necessitano di risorse non su IFS (immagini, pdf da includere, etc.)
- Tutte le vecchie stampe tramite H53, con generazione periferizzata su Looc.UP

La progettazione delle stampe H53 passa attraverso la definizione di uno script all'interno del quale definire le tipologie di "righe" la cui sequenza definirà la struttura del documento.
![B£STAM_09](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_09.png)
La generazione dei documenti potrà avvenire nello stesso modo in cui viene "eseguita" una scheda :  lancio funzione che interpreta lo script e dati attinti da variabili o attraverso funzioni F.
**Esempi di documenti H53**
__Stampa matrice__
![B£STAM_10](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_10.png)
__G8D__
![B£STAM_11](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_11.png)
__Rapporto di analisi processo__
![B£STAM_12](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_12.png)
**Requisiti**
Questo motore prevede come prerequisito :  gli script della famiglia Looc.UP (nello specifico script nel file SCP_G53) su AS400, della /copy £H53 e di un Looc.UP attivo.
Così come per i report del Q9000 c'è intenzione di definire degli script ready to use per altri tipi di stampe grafiche H53.
### AOP
AOP (Advanced Output Production) è un prodotto di Medusa Informatica che viene distribuito gratuitamente da Sme.UP e permette di generare documenti in formato PDF, inviare tali documenti per e-mail e stamparli su carta utilizzando stampanti Windows.
Tramite AOP verranno realizzate le stampe gestionali canoniche : 

- Fattura
- Bolla
- Ordine d'acquisto
- Ordine di vendita
- Offerta
- Lettera (documento neutro con carta intestata)

E' in via di completamento un lavoro di definizione di modelli di documento base, per le tipologie di documenti suddetti, in maniera che Sme.UP venga fornito con dei documenti sufficientemente completi per poter essere pronti all'uso in situazioni con poche specificità.
Lo strumento di progettazione dei documenti messo a disposizione da AOP è un editor grafico di disegno dei documenti.
Attraverso tale editor è possibile, una volta prototipati i dati in un XML prodotto dalla /copy AOP, disegnare il documento ed agganciare graficamente i dati del documento.

__Editor WYSIWYG di AOP__
![B£STAM_13](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_13.png)**Esempi di documenti AOP**

__Fattura__
![B£STAM_14](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_14.png)
__Bolla__
![B£STAM_15](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_15.png)
__Offerta__
![B£STAM_16](http://localhost:3000/immagini/MBDOC_VIS-B£STAM_01/BXSTAM_16.png)
**Requisiti**
Questo motore prevede la /copy £AOP ed un server Windows su cui installare e configurare il server AOP, gli script di definizione del modulo utilizzati dal server AOP.
## Generazione stampe
### G87 - SmePD
SmePD è un server LPD, realizzato dal laboratorio Sme.UP, in grado di stampare file PDF su stampanti Windows attraverso delle code LPR standard.
Tramite questo motore di stampa è possibile stampare qualunque PDF, generato al momento, storicizzato o generato da altre fonti, tramite normali code remote di stampa AS400 su stampanti Windows debitamente configurate nell'applicazione.
**Requisiti**
Questa soluzione prevede un server Windows su cui installare il server SmePD sviluppato da noi, i software Ghostscript e Ghostview (entrambi gratuiti) e la sua configurazione relativamente alle stampanti Windows da utilizzare. Inoltre è necessaria la configurazione di code di stampa remote su AS400 e della /copy £G87
### AOP
Tramite lo stesso server AOP che genera i documenti, e contestualmente a questo processo di creazione,  è possibile stampare i documenti generati sulle stampanti Windows debitamente configurate nell'applicazione.
**Requisiti**
Gli stessi della parte di generazione dei documenti
## Il processo formativo
A fronte dei cambiamenti descritti sono allo studio perscorsi di formazione messi in atto avvalendosi degli strumenti a disposizione : 

- Documentazione attiva
-- Applicativa
-- Tecnica
-- Operativa
-- FAQ
- Video formativi
- Esempi ed esercizi
- Sessioni di corso per colleghi ed esterni

