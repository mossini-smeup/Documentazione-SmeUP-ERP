## Obiettivo
Obiettivo di questa scheda è analizzare gli affidamenti bancari concessi all'azienda

![C5D030_049](http://localhost:3000/immagini/MBDOC_SCH-C5D030_AFF/C5D030_049.png)
## Parametri di lancio

 * Data Riferimento :  permette di impostare la data a cui analizzare i fidi concessi. Se lasciata vuota viene considerato "Oggi"

## Dettaglio informazioni
Per ogni banca è possibile visualizzare : 
 * Gruppo affidamento :  è visualizzarto se è stata attivata la gestione del fido promiscuo
 * Affidamento di gruppo :  è visualizzato se è stata attivata la gestione del fido promiscuo e riporta il fido totale del gruppo
 * Condizioni di affidamento di ogni rapporto bancario alla data selezionata. In particolare per ogni rapporto bancario sono riportati : 
 ** Codice, descrizione e tipologia di rapporto
 ** Tasso attivo totale :  riporta la somma del primo livello di tasso attivo (spread + interbancario)
 ** Tasso passivo totale :  riporta la somma del primo livello di tasso passivo (spread + interbancario)
 ** Data inizio e fine validità delle condizioni
 ** Fido
 ** Limite Fido Gruppo se attivata la gestione del fido promiscuo
 ** Conto unico :  nel caso in cui un rapporto bancario utilizzi il fido associato a un altro rapporto sarà visualizzato il raporto su cui è impostato il fido
 ** Tassi attivi e passivi

## Opzioni
 * Gestione condizioni affidamento :  sulle linee di affidamento di gruppo permette di impostare il fido di gruppo mentre sui rapporti bancari permette di impostare le condizioni di rapporto
 * Gestione gruppo di affidamento :  è un'opzione attiva solo sui rapporti bancari e permette di associare un rapporto bancario a un gruppo di affidamento
 * Gestione rapporto in conto unico :  è un'opzione attiva solo sui rapporti bancari di conto corrente e permette di associare un rapporto bancario con cui si condivide il fido
 * Gestione rapporti in c/unico multiplo :  è un'opzione attiva solo sui rapporti bancari di conto corrente e permette di associare più rapporti bancari con cui si condivide il fido




