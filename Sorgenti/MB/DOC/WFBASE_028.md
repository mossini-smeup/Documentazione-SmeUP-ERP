# Problematica

Nei casi in cui un utente debba interagire con un numero non determinabile a priori di persone (ad esempio mettere a conoscenza dell'esecuzione di un lavoro un insieme di volta in volta variabile di utenti) le reti di Petri non riescono da sole a descrivere in maniera soddisfacente il processo.
Questo perchè ogni impegno (inteso come compito elementare svolto da un utente, quale la presa visione di un'informazione) deriva da una distinta transizione nella rete :  nel caso in esame sarebbe quindi necessario disporre di uno script con un numero variabile di transizioni.
Per questo motivo è necessario introdurre degli strumenti per permettere la creazione di più impegni a fronte di una stessa transizione, in un numero di volta in volta variabile :  le liste di distribuzione.

# Implementazione

Una lista di distribuzione è costituita da : 
 * Un impegno master, in cui un utente si fa carico di decidere a quanti e quali utenti inviare degli impegni slave
 * N impegni slave, a risposta facoltativa o obbligatoria

La dinamica dell'esecuzione di una lista di distribuzione è : 
 * L'utente sull'impegno master prende in carico l'impegno :  viene creata una pre-lista sulla base delle informazioni contenute nello script del workflow.
 * L'utente sull'impegno master può modificare tale lista, aggiungengo o rimuovendo elementi.
 * L'utente sull'impegno master distribuisce la lista :  gli impegni slave si attivano e finiscono nelle worklist dei rispettivi utenti.
 * Quando tutti gli impegni slave a risposta obbligatoria sono stati eseguiti l'impegno master viene dichiarato automaticamente e il workflow può avanzare.
L'utente master può continuare ad aggiungere elementi alla lista fino alla dichiarazione dell'impegno master, ovvero fino a quando l'ultimo impegno slave non viene eseguito.

## Liste di distribuzione automatiche

Se l'impegno master è automatico le liste di distribuzione vengono create automaticamente a partire dallo script, in tal caso non saranno ovviamente modificabili.

## Liste di distribuzione differite

Si può impostare sulla T master di creare la lista di distribuzione direttamente alla creazione dell'ordine. In questo modo è possibile all'interno di impegni non master (precedenti la distribuzione) modificare la lista, che verrà eseguita automaticamente in un secondo momento.

# Impegni slave

Vengono creati : 
 * Alla presa in carico del master
 * Se la transizione master è solo di distribuzione (no presa in carico) all'attivazione
 * Se la transizione master è automatica alla distribuzione
 * Se specificato nello script direttamente alla creazione dell'ordine

Vengono resi pronti alla distribuzione.
Le distribuzioni possono essere multiple, ovvero mentre la transizione master è attiva (non sono ancora stati chiusi gli slave a risposta obbligatoria) è sempre possibile aggiungere impegni e distribuirli.

Gli impegni slave possono trovarsi solo nello stato "non pronto" oppure "pronto"; il passaggio di stato a "pronto" avviene solo per impegni assegnati con la distribuzione.

# Sugli script

Operazioni necessarie per definire una lista di distribuzione : 
 * Compilare una transizione master :  è una transizione normale
 * Compilare una o più transizioni slave
 ** senza luoghi FROM/TO
 ** con la keyword Mas valorizzata sulla transizione master (es. Mas="T01")
 ** gli utenti di esecuzione (classe o utente singolo) servono a identificare il gruppo di utenti a cui verrà distribuita :  per ogni utente appartenente agli utenti che possono eseguire un impegno slave verrà creato (o proposto) un impegno.
 ** la keyword Rfa="1" indica che una transizione slave è a risposta facoltativa, quindi ininfluente ai fini dell'avanzamento del master.

Quindi : 
 * nelle transizioni normali viene creato un solo impegno eseguibile da uno e uno solo utente tra quelli assegnati alla transizione
 * nelle transizioni slave viene creato un impegno PER OGNI utente tra quelli assegnati alla transizione slave

# Programmi coinvolti

Sono : 
 * WFWFC0 : 
 ** crea gli impegni slave da script, alla presa in carico o all'attivazione se la transizione master è senza presa in carico.
 ** effettua le dichiarazioni automatiche della master quando sono finite le slave con risposta obbligatoria.
 * WFSUP_02 :  è utilizzato per la modifica di liste di distribuzione, ovvero per aggiungere o togliere impegni slave oltre a quelli da script.
 * WFWFA0_AS :  aggiorna la memoria per le azioni master-slave.
 * WFWFB0 :   crea gli slave alla creazione dell'ordine, se specificato sulla T master.

# Varianti

Da implementare : 
 * Gestione di risposte diversificate sugli impegni slave (non solo presa visione ma decisioni) : 
 ** G08 alla dichiarazione con scelta multipla
 ** Conseguenze di dichiarazione sugli impegni slave per eventuale chiusura altri impegni sulla prima risposta negativa.
 ** Sugli impegni successivi :  testing delle scelte effettuate negli impegni slave.
