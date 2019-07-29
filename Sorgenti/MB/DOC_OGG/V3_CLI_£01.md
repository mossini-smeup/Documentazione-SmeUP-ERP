## £01, listener di coda con chiave
### Cos'è
Si tratta di un ascoltatore che, in maniera asincrona, all'arrivo di un XML sulla coda con chiave indicatagli, con le chiavi costituite da utente e ambiente di collegamento, lo esegue.
### A cosa serve
A poter lanciare una funzione su un client Looc.UP collegato a fronte di un evento gestito da RPG
## Parametri
I parametri che identificano il comportamento del listener sono : 

- Parametro QNAM, nome della coda da ascoltare
- Parametro QLIB, libreria dove è presente la coda da ascoltare
- Parametro WTO, timeout, espresso in numero di secondi, da attendere prima di effettuare la prossima lettura

Questi parametri, come per tutti i listener sono passati nella definizione.
## Comportamento
Il listener £01, ogni WTO secondi legge la coda QNAM nella libreria QLIB. Si aspetta un XML Sme.UP. Una volta letto lo esegue come se l'avesse ottenuto da una richiesta classica.

## Attivazione listener
L'attivazione del listener avviene tramite SCP_CLO aggiungendo le righe : 
Ogni lettura recupera un solo messaggio e poi si mette in attesa per il timeout specificato prima di leggere il messaggio successivo.

## Esempio di definizione
Utilizzando NOMECODA come valore esemplificativo del parametro QNAM, NOMELIBRERIA come valore esemplificativo del parametro QLIB e SECONDI come valore esemplificativo del parametro WTO di seguito è riportato un esempio di quanto dev'essere inserito nel SCP_CLO identificato per poter attivare il listener

 :  : C.LST Cod="£01" Txt="Listener coda con chiave" Add="localhost" Protocol="JAVA" Wiz="LST_DIR" Param="class=Smeup.smeui.uimainmodule.externallistener.java.keyedqueues.UIKeyedQueueListenerManager;QNAM=NOMECODA;QLIB=NOMELIBRERIA;WTO=SECONDI" LoadOnStartup="1" MaxDelay="60000" SendEvt="1" TypeLog="C1S0" MaxLog="1" NumDayLog="1"
