# Configurazione Esito Fatture

## Premessa
Il cruscotto esito fatture è una funzionalità che può prendere senso solo se viene implementata l'interfaccia, per il reperimento degli esiti dell'invio, verso l'intermediario o direttamente verso l'SDI.

Solo se questa funzionalità viene implementata, la voce di menù corrispondente può produrre un risultato significativo.

A standard in questo senso è stata predisposta l'interfaccia verso Abletech ed alcune indicazioni (esplicitamente indicate) verteranno su questa specifica interfaccia.

## Prerequisiti
Se come nel caso Abletech la comunicazione si basa su un webservice, per il corretto funzionamento delle funzionalità di invio delle fatture elettroniche presuppone la disponibilità di uno Smart Kit.
Lo stato e la bontà della configurazione della connessione può sempre essere monitorato all'interno della scheda _Cruscotto esito fatture_  all'interno del tab _Controlli di sistema
Per un maggiore dettaglio sull'impostazione dello Smart Kit si rimanda al documento "Impostazione invio fatture"

## Configurazione
Se non l'interfaccia non è abletech è necessario predisporre i seguenti sorgenti : 
* il servizio V5_082A_xx atto ad elaborare l'aggiornamento degli esiti per tramite dell'intermediario specifico. Se non si ha Abletech si può guardare il V5_082A_01 come esempio.
* il programma V5_082B_xx atto ad controllare l'avanzamento degli esiti dell'intermediario specifico. Se non si ha Abletech si può guardare il V5_082B_01 come esempio.
* il programma e la scheda V5_082C_xx atte a mostrare il dettaglio delle informazioni di esito ritornate dall'intermediario specifico. Se non si ha Abletech si possono guardare i sorgenti V5_082C_xx.

A seguire vengono riportate considerazioni che valgono solo quando l'intermediario è Abletech.

* Ad eccezione del webservice corrispondente all'invio, vanno attivate tutte le funzionalità descritte nel documento "Impostazione invio fatture".
* Oltre ai succitati webservice vanno implementati quelli corrispondenti agli elementi **£AB04_n_ (notifiche trasmissione) e **£AB05** (notifiche fatture) della tabella **EDC** .
La PTF V580508A imposta gli SE.SUB.A38 che puntano ai webservice di produzione
* **82.S03.B00** per l'elemento **£AB04** (notifiche trasmissione)
* **82.S01.B00** per l'elemento **£AB05** (notifiche fatture)

Esistono due webservice di notifiche in quanto abletech, prevede una prima fase, in la fattura ricevuta viene validata. In questa fase solo il webservice notifiche fatture è in grado di rispondere. Solo in una seconda fase quando la fattura è stata validata, allora gli avanzamenti di stato della fattura iniziano ad essere restituiti dal webservice notifiche fatture.

E' inoltre da considerare che entrambi i webservice funzionano ritornando l'elenco degli stati attraverso cui la fattura è passata nel tempo.

NOTA BENE :  se viene settato l'ambiente per l'invio di test, non sarà possibile in quell'ambiente verificare l'esito delle fatture inviate nel reale. Si sottolinea che d'altra parte non si pongono particolari problemi ad eseguire più volte la richiesta di esito, sulla medesima fattura (cosa che per altro è sintomatica del fatto che l'esito cambia varie volte nel tempo).

