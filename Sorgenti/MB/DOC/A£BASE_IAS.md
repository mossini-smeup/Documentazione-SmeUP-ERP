# Alta affidabilità e IASP

L'alta affidabilità mediante IASP si basa sul meccanismo di "sincronizzazione" degli IASP.
Per semplicità possiamo definire uno IASP come un "insieme di dischi". A grandissime linee una libreria può stare sui dischi "IASP" o sui dischi "SYSBAS".

Sistema 1 -SYS1- (sistema source - di produzione) ha SYSBAS + IASP
Sistema 2 -SYS2- (sistema target - di backup) ha SYSBAS + IASP "replicato" da SYS1

Entrambi i sistemi sono attivi contemporaneamente, ma solo uno dei due ha lo IASP in linea.
I due sistemi possono essere partizioni diverse della stessa macchina o su macchine separate.

Normalmente SYS1 (il sistema di produzione) ha in linea SYSBAS e IASP.
Se si "rompe" SYS1, il cluster "passa il controllo" a SYS2. Quindi effettua tutte le operazioni per sostituire in modo trasparente SYS1. Di conseguenza SYS2 porta in linea IASP, prende l'IP di SYS1 ecc.

SYS2 deve ovviamente essere funzionante anche senza IASP in linea.

Lo IASP viene mantenuto sincronizzato sui due sistemi in automatico. (Sono possibili configurazioni in cui esistono due "copie" degli IASP e configurazioni in cui lo IASP è sempre lo stesso che viene scollegato e collegato ad uno dei due sistemi).
Tutto quello che c'è in SYSBAS invece non è sincronizzato in modo automatico.
Bisogna prestare attenzione al fatto che non tutti gli oggetti sono "IASP-izzabili". Es. USRPRF, lavori schedulati, librerie in QSYSLIBL...

Per allineare tutto ciò che non è IASP-izzabile (e quindi sta in SYSBAS) è possibile usare prodotti di PowerHA (come AdministrativeDomain). Però questo è difficile da usare e mantenere allineato al sistema (bisogna indicare esplicitamente gli oggetti).
Oppure è possibile usare prodotti appositi. Ad esempio QuickEDD. QuickEDD si occupa di trasferire anche le operazioni in sospeso (ad esempio lavori in coda che non sono ancora partiti, oppure gli spool).


# Convertire un'applicazione

## Linee guida generali
Questi sono i passi principali da eseguire in fase di migrazione di un'applicazione
- Effettuare uno studio iniziale di cosa voglia dire IASP-izzare i propri sistemi
- Informare e istruire l'eventuale EDP su specificità che riguardano lo IASP (Connettività ad database, trigger, DDM, Journal, ecc.)
- Capire se e quali modifiche vanno fatte all'applicazione e al sistema per renderla funzionante in ambiente IASP-izzato.
- Preparare un ambiente di test in cui testare la IASP-izzazione
- Decidere una strategia per sincronizzare il SYSBAS del sistema source con quello target.
- Testare le modifiche a processi e applicazioni.
- Pianificare e testare (possibilmente in ambiente controllato) la strategia di migrazione alla nuova struttura
- Istruire tutto il personale
- Eseguire la migrazione

## Considerazioni varie
Per capire se e quali modifiche vanno fatte all'applicazione e al sistema bisogna tenere conto di vari aspetti.

Questi aspetti riguardano in particolare l'abilitazione degli IASP, la loro configurazione (cosa spostare e cosa no, come farlo...), la gestione sistemistica e la struttura del database.

Per i dettagli relativi a queste considerazioni si rimanda al capitolo 5 del redbook "IBM i 6.1 Independent ASPs :  A Guide to Quick Implementation of Independent ASPs" (vedere l'ultimo capitolo per i riferimenti).


# Redbook
Per ulteriori dettagli consigliamo la lettura dei seguenti Redbook : 

IBM i 6.1 Independent ASPs :  A Guide to Quick Implementation of Independent ASPs
http://www.redbooks.ibm.com/redbooks/pdfs/sg247811.pdf
(In particolare i capitoli 1 e 5 e le appendici B, D ed F)
IBM Eserver iSeries Independent ASPs :  A Guide to Moving Applications to IASPs
http://www.redbooks.ibm.com/redbooks/pdfs/sg246802.pdf
(In particolare i capitoli 4 e 8)

# IASP e Sme.UP
- [IASP e Sme.UP](Sorgenti/MB/DOC/A£BASE_IA1)
