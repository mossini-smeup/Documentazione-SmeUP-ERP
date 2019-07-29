# Scopo

Questo documento ha lo scopo di riepilogare gli elementi di tabella rilasciati per la gestione dei TODO standard, oggetto applicativo H3 £TDO.

# Definizione

## TODO
Sono richieste di intervento relative ad attività da fare, non collegate a workflow, con una eventuale gestione di comunicazioni via email, in tal caso oltre agli elementi di tabella sottoindicati è necessario associare gli indirizzi email per una risalita tramite G85.

# Tabelle utilizzate : 

### CRR - Richieste Intervento - Elemento £TDO
L'elemento £TDO standard identifica l'oggetto TODO

### B£G - Griglia Controllo 3 Oggetti - Elemento £TD
L'elemento £TD standard identifica il tipo griglia specifico per il TODO

### C£E - Categorie Parametri - Elemento £TD
L'elemento £TD identifica i parametri espliciti standard per il TODO

### B£NH3 -  Parametri Variabili - Sottosettore H3 - Elementi £T1-7
I seguenti elementi indicano i parametri standard per il TODO
* £T1               Descrizione
* £T2               Commenti
* £T3               Attività
* £T4               Url
* £T5               Tag
* £T6               Partecipanti via mail
* £T7               Todo list

### CRNH3 - £TDO  Numeratori Sottosettore H3 -Elemento £TDO
L'elemento £TDO standard identifica il numeratore per l'oggetto TODO

### WFA - Processo workflow
E' necessario specificare i singoli elementi di questa tabella per tutti i processi relativi agli oggetti H3, disabilitando il workflow in quelli relativi al TODO impostando il flag T$WFAS Spegni inserimento=1. Disattivando i prodessi relativi al TODO è necessario attivare tutti i processi relativi agli altri oggetti H3.

### CPG - Progetto
Definire qui gli elementi relativi agli ambiti dei TODO, sono raggruppamenti, definiti "scrum".

