# Collegamento documenti
Questa funzione serve per collegare un documento derivato al suo documento origine, in contemporanea se il documento prevede la movimentazione di magazzino la funzione lancia i movimenti associati alle righe.

## Formato di lancio
![V5DOCU_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5GM01/V5DOCU_01.png)
Se il tipo documento non è già impostato nella funzione di menù lo si deve inserire, il funzione del tipo documento in input il sistema orienta il comportamento del programma e determina a cosa riferire il numero documento.

Fatte le opportune selezioni, con F6 si può lanciare la funzione.


## Scollegamento documento
Lo stesso programma può essere utilizzato per lo scollegamamento di un singolo documento, dal formato guida utilizzare il comando funzione **F15 = Scollegamento**, nel formato che si presenta inserire il numero documento ed eventualmente il numero riga e lanciare lo scollgamento con F6 : 
![V5DOCU_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5GM01/V5DOCU_02.png)
Da questo formato, dopo lo scollegamento, il comando funzione **F15 = Ricollegamento** ritorna al formato guida compilando il campo numero documento con il documento appena scollegato.
