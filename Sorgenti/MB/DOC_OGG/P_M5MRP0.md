L'elaborazione MRP può essere schedulata automaticamente con una frequenza stabilita oppure lanciata manualmente.

I parametri di lancio si impostano nella videata seguente : 

![M5_001_07](http://localhost:3000/immagini/MBDOC_OGG-P_M5MRP0/M5_001_07.png)
Significato dei campi : 
 * __gruppo fonti__ :  usato dall'MRP durante l'elaborazione (esclusi gli articoli con una politica di riordino riferita a un gruppo fonti speciale);
 * __scenario__ :  si possono definire diversi scenari per elaborazioni MRP parallele di simulazione o effettive (normalmente lo scenario effettivo è denominato **);
 * __metodo__ :  elaborazione totale (standard), elaborazione parziale (in questo caso scegliere l'articolo o la commessa e il sistema cancella e ricalcola tutti i suggerimenti relativi all'articolo / commessa dell'elaborazione parziale);
 * __selezione__ :  definisce la tipologia di codici da considerare nell'elaborazione;
 * __flussi precedente / successivo__ :  contemporaneamente all'azione di lancio dell'MRP, è possibile lanciare delle elaborazioni precedenti e successive l'MRP stesso (es. :  per rifasare gli impegni o ricalcolare il livello minimo di distinta prima dell'MRP e lanciare il calcolo risorse derivate dalle proposte ordini di produzione dopo l'MRP). I gruppi di azioni pre e post sono tabellati nella tabella B£H con prefisso MRP - e con suffisso il valore del campo (es. MRP-A = flusso precedente).

>N.B. :  Segnaliamo che con il comando funzione F15 si possono vedere le statistiche dell'ultima elaborazione completa : 

![M5_001_08](http://localhost:3000/immagini/MBDOC_OGG-P_M5MRP0/M5_001_08.png)