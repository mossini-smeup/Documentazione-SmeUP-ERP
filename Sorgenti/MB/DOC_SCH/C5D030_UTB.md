## Obiettivo
Obiettivo di questa scheda è aggiornare i tassi bancari utilizzati all'interno delle condizioni di tesoreria

![C5D030_051](http://localhost:3000/immagini/MBDOC_SCH-C5D030_UTB/C5D030_051.png)
## Parametri di lancio

 * Tipo Tasso :  è un campo obbligatorio e riporta il tipo di tasso interbancario (Euribor 1M, Euribor 3M, ecc.). I tipi tassi sono definiti nella tabella C5*TT
 * Data Tasso :  è necessario inserire la data di cui si vuole inserire o aggiornare il tasso interbancario
 * Nuovo Tasso :  è il valore del tasso da inserire all'interno delle condizioni bancarie per la tipologia di tasso e la data indicate prima
 * Visualizza già aggiornati :  permette di visualizzare o meno le condizioni bancarie che già sono allineate al nuovo tasso

## Dettaglio informazioni

All'interno della matrice di dettaglio vengono mostrate tutte le casistiche in cui il tipo di tasso indicato nei parametri è utilizzato. Potrebbero essere, quindi, esposte condizioni di rapporto e condizioni impostate su finanziamenti.
Per ogni casistica sono esposti : 
 * Rapporto bancario
 * Tipo di condizioni
 * Numero di finanziamento (per le condizioni relative a finanziamenti)
 * Importo residuo finanziamento (per le condizioni relative a finanziamenti)
 * Vecchia data validità :  è l'ultima data a cui è stato definito il tasso selezionato
 * Vecchio tasso :  è il tasso impostato alla vecchia data validità
 * Nuova data validità :  è la data impostata nei parametri di lancio
 * Nuovo tasso :  è il tasso impostato nei parametri di lancio
 * Aggiornato :  è compilato se il tasso del rapporto bancario è stato già aggiornato

Per confermare l'aggiornamento dei tassi sarà necessario digitare il tasto _F06=Esegui aggiornamento

## Opzioni

Tramite le opzioni richiamabili su ogni singola riga sarà possibile accedere : 
 * alla gestione delle condizioni di finanziamento per i rapporti di finanziamento
 * alle condizioni di rapporto per gli altri rapporti




