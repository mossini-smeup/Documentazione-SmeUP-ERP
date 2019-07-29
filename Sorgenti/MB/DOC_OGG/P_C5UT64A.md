# Prerequisiti e Controlli preliminari
Si raccomanda controllare, prima del lancio, di aver creato il nuovo codice riclassifica         (tabella C5M) ed il relativo parametro della nuova riclassifica legato al conto contabile (tabella B£NC5). Il parametro dovrà essere denominato con i primi 2 caratteri ad HR.           Si consiglia di copiarlo dall'elemento HR1, impostando come parametro oggetto C5N + sottosettore della nuova linea riclassifica.


# Obiettivo
Tramite questa funzione sarà possibile creare riclassifiche di bilancio partendo da una
riclassifica già esistente.
Qualora la copia non andasse a buon fine verrà creato uno spool con il dettaglio dell'errore.


# Richiesta Parametri
I dati richiesti sono i seguenti : 
* Riclassifica origine :  riclassifica di bilancio da cui partire per la copia
* Riclassifica destinazione :  nuova riclassifica di bilancio che verrà scritta copiandola dalla   riclassifica origine.   La riclassifica destinazione non potrà essere BAS o CEE.
* Collegamento Conti :  se lasciato in bianco verranno copiati anche i collegamenti tra linee di   riclassifica e conti contabili. Se impostato a "N" non verranno creati i legami tra conti e    nuove linee di riclassifica.
* Sovrascrivi Esistente :  qualora esistano già elementi della riclassifica destinazione, e questo   campo viene lasciato in bianco, non verrà effettuata nessuna copia.     Mentre se impostato a "1" verranno cancellati eventuali dati relativi alla riclassifica   destinazione e ricreati.

