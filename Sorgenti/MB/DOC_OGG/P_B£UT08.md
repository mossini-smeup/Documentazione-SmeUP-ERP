# Ricerca stringa
L'utility di scansione sorgenti permette la ricerca massiva di stringa all'interno di un gruppo di sorgenti.
Quando la stringa viene trovata questa informazione viene emessa su stampa e consolidata su database per poi essere inerrogata tramite UP GLM.

## Dove cercare
E' possibile indicare un elenco di file/libreria.
Per quanto riguarda il file, è possibile indicare *ALL per efefttuare la ricerca all'interno di tutti i file della libreria.

E' possibile filtrare per tipo membro e inoltre è possibile includere/escludere i membri "old" (tipo _O)

## Cosa cercare
E' possibile cercare : 
* testo in tutto il sorgente
* testo in modifiche
* testo sotto forma di espressioni

E' possibile indicare 3 stringhe di testo in
* AND (opzione A) :  in questo caso tutte le stringhe devono essere presenti sulla stessa riga
* OR (opzione O) :  in questo caso deve essere presente almeno una stringa
* AND di membro (opzione M) :  in questo caso devono essere presenti tutte le stringhe ma non necessariamente sulla stessa riga

E' inoltre possibile affinare la ricerca tramite altre opzioni : 
Case sensitive, includere le righe di commento.

### Exit
Per effettuare ricerche particolarmente complesse è possibile avvalersi dell'uso di una exit.
La exit viene richiamata solamente quando la condizione è risultata vera e può riconfermare/annullare la veridicità della stessa.                                                

Parametri della exit
 :  : PAR L(TAB)
Parametro|Descrizione
Stringa|Riga di attivazione della condizione
Condizione confermata|impostata a falso deve essere riconfermata
Libreria|Nome della libreria in esame
File|Nome del source file in esame
Membro|Nome del sorgente in esame
Posizione|Riga assoluta del sorgente in esame

