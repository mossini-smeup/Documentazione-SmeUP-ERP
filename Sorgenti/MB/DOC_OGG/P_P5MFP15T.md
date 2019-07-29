# Storico avanzamento contenitore MFP
Questo programma permette la visualizzazione di tutti gli avanzamenti relativi ad un contenitore.
Generalmente quando la quantità di un contenitore viene avanzata tra due ubicazioni/fasi del ciclo di lavorazione vengono eseguiti : 
 * un movimento di scarico della giacenza origine
 * un movimento di carico della giacenza di destinazione
 * tutte le dichiarazioni di produzione relative alla fasi di lavorazione comprese tra quella origine e quella destinazione
Quando invece la quantità viene trasferita da un contenitore in una ubicazione/fase ad un altro contenitore nella stessa ubicazione/fase vengono eseguiti solo : 
 * un movimento di scarico della giacenza origine
 * un movimento di carico della giacenza di destinazione
Un avanzamento è l'insieme degli eventuali movimenti di giacenza e delle attività di produzione relativi ad uno spostamento di quantità di un contenitore.

### Formato di lancio
![P5PMFP_06](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP15T/P5PMFP_06.png)Dato il contenitore con F6 si ottiene la lista dei suoi avanzamenti

### Formato lista
![P5PMFP_07](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP15T/P5PMFP_07.png)Il tipo oggetto indica se si tratta di movimenti di magazzino o attività di produzione. Da notare che eventuali spostamenti da o verso contenitori esterni vengono segnalati.

Nella riga corrispondente all'avanzamento si può attivare l'opzione di cancellazione che esegue un roll-back cancellando sia i movimenti che le attività relative all'avanzamento : 
![P5PMFP_08](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP15T/P5PMFP_08.png)