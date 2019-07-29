## Introduzione

Il modulo si occupa di acquisire documenti (ad esempio documenti del ciclo esterno) al fine di supportare eventuali registrazioni contabili e programmi o procedure di archiviazione degli stessi.

## Servizio di presentazione
Il servizio principale che considera i documenti letti e importati è ODSER_01.
Tale servizio al momento tra le sue funzionalità ha quella di lanciare l'esecuzione del programma di acquisizione ODUT05.
In futuro i due passi di lettura e di acquisizione potrebbero essere separati

## Acquisizione
Prevede l'esecuzione di un programma (ODUT05) che legge il documento txt acquisito e considera i valori in esso contenuti.


## Stati acquisizione

* 01 Ho letto e riconosciuto il numero e la data
* 02 Ho individuato il fornitore
* 10 Ho individuato l'importo della fattura
* 15 Ho individuato la presenza di una registrazione contabile associabile al documento scannerizzato (è possibile che gli importi non coincidano)
* 20 Ho individuato la registrazione e gli importi coincidono

