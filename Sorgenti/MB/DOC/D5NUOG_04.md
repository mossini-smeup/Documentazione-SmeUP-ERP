# Struttura

## Utilizzo
I numeri oggetti storicizzati potranno essere di due tipi : 
1) Definitivi
2) Provvisori
NB :  lo stato di provvisprio o definitivo è relativo alla totailità dei 100 numeri.

I numeri provvisori potranno essere utilizzati solo attraverso una richiesta esplicita dell'utente : 

- nella costruzione di valori della £G37 imppostando il flag "Numeri memorizzati" nel formato di
  richiesta numeri
- come attributo dell'oggetto, di tipo O/xxx, dove xxx è l'indice del numero

I numeri definitivi saranno sempre recuperati dallo storicizzato, indipendentemente dalla
richiesta di utilizzo o dal tipo OAV (O/xxx e V/xxx sono coincidenti)

Una volta attivata la gestione, ad ogni richiesta di numero (via G37)

- se defitivo viene letto dallo storico
- se provvisorio e non richiesto l'utilzzo del provvisorio, si ricalcolano sempre i numeri e li si riconsolidano.
- se provvisorio, e richiesto l'utilizzo del provvisorio, viene confrontato istante di ultimo aggiornamento dell'oggetto con l'istante di consolidamento :  se diversi viene ricalcolato e ricosolidato, se uguale viene utilizzato il numero consolidato.


## Stato di definitivo
Per rendere un numero definitivo, deve essere eseguita l'aposita funzione per avanzare gli oggetti richiesti in stato di definitivo.
Una volta trasformato l'oggetto in definitivo i propri numeri non saranno più storicizzati.
Per evidenziare eventuali anomalie fra i numeri storicizzati e i numeri attuali è stata predisposta l'aposita funzione di verifica.
Se dovesse nascere l'esigenza di ricalcolare un numero definitivo, bisogna eseguire la cancellazione dallo storico e rieseguire la stroricizzazione.
Tale funzione si esegue dalla scheda del modulo D5NUOG
