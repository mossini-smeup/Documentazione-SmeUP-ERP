## COSTRUZIONE DEL VIAGGIO
Il viaggio è costituito in sostanza dall'archivio dei viaggi propriamente detti che definiscono i "dati di testata" del viaggio e dalle richieste di movimentazione con le relative righe che definiscono da cosa è costituita la spedizione.
Queste due tipologie di dati vengono create separatamente :  generalmente vengono create le richieste a partire dagli ordini di vendita e poi queste vengono, manualmente o automaticamente, secondo determinate logiche attribuite ai viaggi.
Questa attribuzione può avvenire contemporaneamente all'estrazione delle richieste (e questo presuppone che il viaggio sia già stato definito) oppure in seguito tramite estrazione interna prevista nelle attività su viaggi.

### PGM  Estrazione richieste movimentazione
 :  : INI
 :  : CMD CALL V5RM01A
 :  : FIN
### PGM  Gestione Viaggi
 :  : INI
 :  : CMD CALL V5TR01G
 :  : FIN
### PGM  Gestione Lista Viaggi
 :  : INI
 :  : CMD CALL V5TR02G
 :  : FIN
### PGM  Attività Viaggi
 :  : INI
 :  : CMD CALL V5SI04
 :  : FIN

## COMPLETAMENTO DEL VIAGGIO
Una volta definito il viaggio questo dovrà passare attraverso una serie di elaborazioni che permettano di fare in modo che il viaggio parta in modo corretto alla data e all'ora prevista di partenza.

Queste fasi si possono così sintetizzare : 
 * Invio dei dati relativi al viaggio allo spedizioniere
 * Esecuzione delle richieste di movimentazione (prelievi)
 * Gestione della packing list (confenzionamento)
 * Creazione del documento di trasporto

Tutte queste fasi sono monitorate e gestite dal programma relativo alle attività sui viaggi
### PGM  Attività Viaggi
 :  : INI
 :  : CMD CALL V5SI04
 :  : FIN
