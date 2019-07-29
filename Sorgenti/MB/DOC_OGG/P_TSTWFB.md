# £WFB FUNZIONI SU ORDINI DI WORKFLOW

## OBIETTIVI

 * Fornire gli strumenti standard per l'inizializzazione, creazione, aggiornamento di ordini di workflow.
 * Eseguire azioni particolari a livello di utente sugli ordini, come l'annullamento, il congelamento...

## FUNZIONI E METODI

### AZI E AZI.NAU :  Azioni su ordini.
Forniscono una chiamata a funzioni di cambio stato di ordini di workflow.
La funzione AZI testa le autorizzazioni WFORTE, mentre la AZI.NAU no ed è riservata principalmente per uso interno.

### OGG.CLO
Chiude tutti i workflow intestati a un determinato oggetto.

### AGG.PRO
Tramite questa chiamata è possibile aggiornare un ordine di workflow di cui si sia cambiato il processo aggiungendo nuove transizioni.
È applicabile in un insieme limitato di casi ed è in generale un'operazione molto rischiosa da effettuare.

Cosa fa : 
 * Scandisce lo script del processo e per ogni transizione crea un equivalente impegno nell'ordine se non c'è già.
 * Allinea il processo.

Quando si può fare : 
 * Se l'ordine non è ancora stato avanzato oppure è "indietro" rispetto al punto in cui sono presenti le nuove transizioni.
Quando SICURAMENTE non si può fare : 
 * Se ho, ad esempio, inserito una nuova transizione T2 tra due vecchie transizioni T1 e T3, e l'ordine è già stato avanzato a T3.

