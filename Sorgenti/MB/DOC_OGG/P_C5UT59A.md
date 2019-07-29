## Obiettivo

Il programma permette di eseguire una registrazione contabile di giroconto tra due enti.
In particolare verranno chiuse le scadenze aperte dell'ente origine e ri-aperte sull'ente  destinazione

## Formato guida

All'interno del formato guida è possibile compilare i seguenti campi : 
 ** Azienda :  Inserire il codice azienda per il quale si vuole effettuare il giroconto
 * ORIGINE
 ** Tipo Ente :  Tipologia ente delle scadenze aperte da chiudere (tabella BRE)
 ** Codice Ente :  Codice ente (relativo al tipo contatto inserito nel campo precedente) delle scadenze aperte da chiudere
 * DESTINAZIONE
 ** Tipo Ente :  Tipologia ente su cui verranno ri-aperte le scadenze chiuse dell'ente origine (tabella BRE)
 ** Codice Ente :  Codice ente (relativo al tipo contatto inserito nel campo precedente) su cui verranno ri-aperte le scadenze chiuse dell'ente origine.
 * REGISTRAZIONE
 ** Tipo Registrazione :  Indicare  il tipo registrazione con cui verrà effettuato il giroconto (tabella C5D). Il tipo registrazione impostato in questo campo dovrà essere di incasso/pagamento (verificare che nell'elemento della C5D il campo Modello sia impostato con 05).
 ** Causale :  Indicare la causale contabile con cui verrà effettuato il giroconto (tabella C5V). La causale impostata in questo campo dovrà essere una causale di incasso/pagamento (verificare che nell'elemento della C5V il campo Tipologia movimento sia impostato con 05 e il Segno Rate sia impostato con - ).
 ** Data Registrazione :  Indicare la data registrazione  con cui verrà effettuato il giroconto
 ** Valuta :  Indicare la valuta con cui verrà effettuato il giroconto. Se valorizzato questo campo, verrà reperito il cambio a seconda della data registrazione inserita precedentemente ed eseguita l'eventuale rilevazione di differenza cambio. Se sono presenti partite aperte in più valute sarà necessario girare  (tabella VAL)

### Parzializzazioni

Digitando il tasto F13 o selezionando il relativo pulsante è possibile accedere alla schermata delle parzializzazioni che consentono di filtrare le scadenze da girocontare.

All'interno delle parzializzazioni è sempre disponibile il campo delle memorizzazioni che consente di salvare una particolare parzializzazione.
