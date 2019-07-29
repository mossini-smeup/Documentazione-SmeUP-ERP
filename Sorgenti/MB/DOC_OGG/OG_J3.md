# OGGETTO J3 - DOCUMENTAZIONE GENERALE

## SCHEDA J3
I J3 sono gli oggetti di setup per i vari componenti di LoocUp. Un oggetto J3 e' una serie di informazioni relative ad ogni componente. Sostanzialmente a livello di script, gli oggetti J3 corrispondono ai vari G.SET.MAT, G.SET.TRE, G.FRM.REP, ecc.
![OGJ301](http://localhost:3000/immagini/MBDOC_OGG-OG_J3/OGJ301.png)La definizione dei diversi J3 e' fattibile tramite un membro di script, il J3_SET_STD (Script di definizione dei modelli) presente nel file SCP_SCH. I setup servono per definire dei default (sulla base dei quali vengono poi eseguiti degli override). Per ogni componente infatti sono stati (dovrebbero essere) definiti dei modelli (A01, A02, ecc).

## Completamento da parte del server dei parametri (esempio report)
E' stato fatto in modo che (al momento solo per 2 componenti REP e EXC) qualunque funzione abbia alle spalle un setup e sia identificata da un 'Contesto'. Cio' significa contestualizzare la richiesta di un setup, quindi a seconda di dove sia usato un certo componente si avranno potenzialmente diversi valori di setup. La parte Java fornisce dei parametri (letti direttamente dall'XML), al servizio LOSER_07, il quale li restituisce a sua volta integrandoli e quindi costruendo il nuovo setup. Sostanzialmente il LOSER_07 riceve la parte di XML riguardante il setup, lo completa a seconda del contesto e lo restituisce nel formato finale.

## Setup da Programma
### a. Dati Standard

- Context
- Title
- Show/Edit

### b. Specifici per componente

- TRE, EXB, FRM ecc

Nell'XML il setup e' così strutturato : 
![OGJ302](http://localhost:3000/immagini/MBDOC_OGG-OG_J3/OGJ302.png)dall'esempio possiamo vedere che vi e' un tag PROGRAM nel quale sono definiti : 

- Show (Yes/No) che permette di decidere se mostrare il Wizard del setup o meno, in fase di elaborazione ad esempio del report;
- Edit dice, nel caso in cui venga emesso, se questo setup può essere modificato;
- Context contiene l'informazione per contestualizzare il componente (presa poi come indicazione dal LOSER_07);
- Title e' il titolo della finestra di setup (qualora questa venga emessa).

Vi e' poi un tag relativo al componente, nell'esempio EXB, il quale ha un Name, un Type e degli attributi specifici. Al momento, soprattutto per compatibilita' col passato, il solo componente EXB supporta un formato leggermente diverso che permette di esprimere per esso differenti configurazioni con un ulteriore livello di tag : 
_NomeComponente
Setup...
Setup...
/NomeComponente 
Il quale contiene gli attributi che altrimenti si dovrebbero trovare direttamente in EXB (NomeComponente).

