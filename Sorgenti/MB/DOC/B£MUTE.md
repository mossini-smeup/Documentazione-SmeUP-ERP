# Generalità
Questo modulo tratta le funzioni che permettono di gestire la memorizzazione dei campi/configurazioni utente.

Le due principali applicazioni di questa funzionalità sono : 
* Nella memorizzazione delle schermate di richiesta dati utente (es. i campi per il lancio di una particolare funzione)
* Nella memorizzazione dei setup dei componenti grafici (es. modo in cui vedo le matrici modo in cui stampo e/o estraggo gli excel ecc.)

Tali memorizzazioni si scindono in due macro categorie : 
* memorizzazione utente :  viene salvata l'ultima "configurazione" utilizzata dall'utente, in modo tale che quando l'utente riapre la funzione veda la "configurazione" che aveva utilizzato la volta precedente
* memorizzazione multipla :  tramite questa gestione è possibile attribuire un "nome" ad una particolare configurazione utente, in modo da poter salvare differenti "configurazioni", che possono poi essere riprese all'uopo. Per queste configurazioni è inoltre possibile indicare delle note in modo da poter documentare in modo preciso lo scopo della "configurazione"

# Tipi di Memorizzazione
Tecnicamente in smeup sono presenti due funzioni per la gestione delle memorizzazioni video : 
* La £MDV - Memorizzazioni Video
* La £MDE - Memorizzazioni Video Estese

La prima sussiste essenzialmente per compatibilità storica, e le sue funzionalità sono inglobate nella successiva £MDE che non è altro che un'evoluzione della £MDV.

Tramite la £MDV posso salvare, memorizzazioni utente/multiple con contenuto di massimo 900 caratteri e senza la possibilità di poter identificare il contenuto della memorizzazione.

Viceversa tramite la £MDE è possibile salvare memorizzazioni utente/multiple per un contenuto massimo di 30000 caratteri, con la possibilità di identificare il contenuto della memorizzazione.

Chiavi della £MDV (salvate sul file MEDAV00F) sono : 
* __Utente__, che può essere valorizzato con il profilo utente oppure, quando sia tratta di una memorizzazione multipla dove può essere necessario utilizzare più dei 300 bytes disponibili in un record del MEDAV00F, allora si utilizzano 3 record identificati ciascuno da "**nome", "++nome", "--nome" (dove nome è il nome assegnato in fase di salvataggio della memorizzazione multipla);
* __Programma__, che normalmente corrisponde al nome del pgm che utilizza la memorizzazione, ma può in realtà contenere anche una stringa qualsiasi che permetta di identificarne l'utilizzo.

![B£MUTE_003](http://localhost:3000/immagini/B£MUTE/BXMUTE_003.png)
Chiavi della £MDE (salvate sul file B£MEDE0F con il campo METIPO='A20') sono : 
* __Utente (MECOD5)__, che può essere valorizzato : 
** con un codice utente (TAB£U)
** con **gruppo, dove gruppo è il gruppo utente (TAB£*GU)
** con ** (per identificare una memorizzazione comune a tutti gli utenti)
** con qualisiasi altra stringa qual'ora lo si ritenga opportuno
* __Struttura (METIPA)__, che esplicita il contenuto della memorizzazione, cioè il significato (tracciato, campi e contenuto) dei valori presenti nel campo MEDATI. Rispetto a questo è importante notare che : 
** questo campo, unitamente al contesto, identifica la configurazione
** il campo struttura viene normalmente valorizzato con un configuratore (vedi oggetto RES-), fra questi di particolare importanza sono quelli del configuratore di scheda (EDT_SCH es. EDT_SCH/G.SET.MAT).
** Nel campo struttura sono inoltre previsti i seguenti casi particolari : 
*** STR.MDV :  indica che nella memorizzazione è salvato un gruppo di dati che non è riconducibile ad una configurazione
*** OJ/*PGM/B£MDV5 :  indica che le memorizzazioni verranno cercate nella £MDV (quindi sul MEDAV00F)
* __Contesto (MECODI)__, che è una stringa qualsiasi che serve per distinguere configurazioni diverse all'interno degli stessi utente/struttura
* __Nome (MECOD6)__, che serve infine per identificare il nome della memorizzazione : 
** quando si tratta di una memorizzazione utente contiene *LAST
** quando si tratta di una memorizzazione multipla contiene il nome della memorizzazione (in pratica rispetto alla MDV dove avevo nel campo utente, o l'utente o **nome, qui ho un campo per l'utente ed un campo per i nomi)

![B£MUTE_002](http://localhost:3000/immagini/B£MUTE/BXMUTE_002.png)
Per ulteriodi dettagli si rimanda alla documentazione delle corrispondenti API (£MDV e £MDE).

# Descrizioni e note delle memorizzazioni
Nelle memorizzazioni estese è opportuno sfruttare la possibilità di inserire una descrizione in modo da comunicare agli utilizzatori lo scopo per cui la configurazione è stata preparata ed il suo utilizzo. In aggiunta alla descrizione è possibile inserire una spiegazione più approfondita nelle note associate.
Il contenitore note corrispondente è denominato "£ME" ed ha come tipo nota "NOT". La chiave (C$KYC1) con cui viene scritta la nota è il campo "MEIDOJ", ovvero la chiave univoca del file B£MEDE0F.

Anche nelle memorizzazioni video è possibile inserire delle note, in questo caso il contenitore corrispondente è denominato "£MD" ed ha come tipo nota "NOT". Le chiavi con cui sono scritte tali note sono l'utente (MD£UTE nel campo C$KYC1) e il programma (MD£PGM nel campo C$KYC2), ovvero le chiavi del file MEDAV00F.

# Nota su *CNV
A causa della coesistenza tra nuovi e vecchi setup, esiste un programma di conversione (B£MDE1) che si occupa, al lancio di una funzione, di tentare la conversione delle vecchie memorizzazioni nelle nuove.
Questo tentativo comporta la scrittura di nuovi record nel B£MEDE0F partendo da record del MEDAV00F o dello stesso B£MEDE0F con chiavi differenti.
I record scritti dal tentativo di conversione sono indentificati con l'Utente *CNV, e almeno uno viene sempre scritto per evitare che all'accesso successivo si attivi nuovamente il programma di conversione.
Fintanto che verranno manutenuti sia i nuovi che i vecchi setup non è possibile eliminare questa conversione, nel momento in cui verranno gestiti solo i nuovi setup sarà possibile eliminare tutti i record con *CNV.
