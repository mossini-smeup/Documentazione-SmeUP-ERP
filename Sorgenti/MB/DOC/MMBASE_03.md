# Esecuzione
Attraverso la funzione di dichiarazione interventi si può dichiarare l'esecuzione sia degli interventi pianificati che degli interventi straordinari.

Lanciando la funzione si presenta la lista degli interventi già dichiarati : 


![MMAM20L](http://localhost:3000/immagini/MMBASE_03/MMAM20L.png)
L'opzione 01 permette l'inserimento di un nuovo intervento, l'intervento può essere programmato o straordinario.

## Interventi programmati
Se selezionata l'opzione interventi programmati viene chiesto il raggruppamento quindi viene mostrata al lista : 


![MMAM23L](http://localhost:3000/immagini/MMBASE_03/MMAM23L.png)
La dichiarazione dell'intervento assegna all'intervento un progressivo ed un tipo intervento eseguito che può assumere i seguenti valori : 

- Il valore 1 nel caso di intervento pianificato regolarmente eseguito (dichiarato con opzione DI)
- Il valore 2 nel caso di intervento pianificato non eseguito (dichiarato con opzione ND)
- Il valore 3 nel caso di intervento straordinario (pompieristico o predittivo)


Per distinguere gli interventi predittivi da quelli pompieristici si consiglia di codificare adeguatamente la tabella "causali intervento" (tab. MMA sottosettore 3).

![MMAM21D](http://localhost:3000/immagini/MMBASE_03/MMAM21D.png)
## Scheda interventi eseguiti
Come per gli interventi pianificati, anche per quelli eseguiti è possibile una reappresentazione grafica, attraverso la scheda : 


![MMBASE_006](http://localhost:3000/immagini/MMBASE_03/MMBASE_006.png)
Sono anche possibili visualizzazioni in formato Gantt, nell'esempio il Gantt degli interventi di un operatore relativi ad un impianto : 


![MMBASE_005](http://localhost:3000/immagini/MMBASE_03/MMBASE_005.png)
## Registrazione materiali
Il comando funzione F8 permette la dichiarazione dei materiali impiegati che possono essere richiamati dalla distinta di manutenzione dell'impianto (opzione RI) oppure inseriti manualmente (opzione 01) : 


![MMAM21I](http://localhost:3000/immagini/MMBASE_03/MMAM21I.png)
Per ciascun materiale inserito è possibile passare alla mappa di gestione : 


![MMAM21D](http://localhost:3000/immagini/MMBASE_03/MMAM21D.png)
Da notare la possibilità di definire fornitori codificati, nel qual caso nel campo descrizione appare la decodifica automatica, o di definire fornitori non codificati scrivendo liberamente la descrizione.


## Interventi straordinari
Scegliendo questa categoria di interventi si presenta direttamente la mappa di inserimento dati consuntivi.
