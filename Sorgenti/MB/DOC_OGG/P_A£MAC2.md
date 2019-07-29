### Destinazione  E' la destinazione desiderata per i due
# SIMULAZIONE E CREAZIONE SPECIFICHE MACRO
## Obiettivo
Permettere di ottenere la creazione della stringa di macro a partire da una richiesta di parametri presentati a video in funzione del contenuto delle specifiche della macro stessa.
Permettere di sviluppare le specifiche di una macro per cui sono stati definiti i parametri.
Gli utilizzi possono essere i seguenti : 
-    Testare una nuova macro sia nella parte di definizione dei parametri che in quella di creazione delle specifiche finali.
-    Sviluppare le specifiche da includere poi nel programma in fase di sviluppo. A seconda dei casi potranno essere incluse la stringa MACRO o le specifiche finali generate.
## Prerequisiti
Per una maggiore comprensione delle modalità di definizione e di utilizzo delle macro si veda il documento A£MAC0.PGM.
## FORMATO DI RICHIESTA
### Origine
Il formato richiede membro, file e libreria di origine nel quale è scritta la macro che si vuole eseguire.
### Destinazione
E' la destinazione desiderata per i due membri generati dalla simulazione : 
-    Membro contenente la specifica M* con la macro scritta per esteso
Se non immesso, assume A_M
-    Membro contenente le specifiche generate dal precompilatore
Se non immesso assume A_C
Il file e la libreria sono le stesse
### Azione sul membro
Sono possibili le seguenti azioni : 
-    C = Creazione
Il membro non deve essere già presente. Sarà creato dall'applicazione assumendo le caratteristiche del membro RPG di CPYSRC nella libreria degli standard
-    S = Sostituzione
Il membro deve essere presente e il suo contenuto viene eliminato
-    A = Aggiunta
Il membro deve essere presente e il suo contenuto non viene eliminato.
Le specifiche generate sono aggiunte in coda.
Ciò può essere utilizzato per creare un gruppo di macro da testare eventualmente in gruppo.
