# Scheda Controllo contenuto tabelle
Una tabella può essere assimilata ad un file di database, pertanto può assumere delle proprietà tipiche di un file : 
 * tracciato record
 * riferimento ad oggetti applicativi
 * congruenza contenuto

La sezione del controllo contenuto di una tabella ha l'obiettivo di aiutare l'utente nell'esplorazione di queste proprietà, in particolare una funzione importante è quella del controllo di congruenza attraverso la quale è possibile identificare gli elementi di tabella che hanno nel contenuto dei valori non validi.

## Formato scheda
![B£TABE_011](http://localhost:3000/immagini/MBDOC_SCH-ST_CC/BXTABE_011.png)
La scheda si suddivide i 3 sottoschede : 
 * _2_campi, è la sottoscheda che si presenta di default, presenta il tracciato della tabella con il riferimento agli oggetti Sme.Up. Il doppio click su una riga sposta alla sottoscheda valori di un campo riempita con i valori presenti del campo selezionato.
 * _2_tutti gli errori presenti
 * _2_valori di un campo

## Tutti gli errori presenti
Il programma scorre tutti gli elementi di tabella e per ciascun elemento controlla la validità del contenuto, vengono presentati i campi e relativi valori errati ed il numero di occorrenze dell'errore. Il doppio click su una riga sposta alla sottoscheda valori di un campo riempita con i valori presenti del campo selezionato.
![B£TABE_012](http://localhost:3000/immagini/MBDOC_SCH-ST_CC/BXTABE_012.png)
## Valori di un campo
A questa sottoscheda si arriva selezionando una riga dalla sottoscheda campi, oppure dalla sottoscheda tutti gli errori presenti.
Per il campo selezionato mostra i valori presenti in tutti gli elementi della tabella, vengono evidenziati in rosso i valori errati. Il doppio click manda alla sezione _3_Righe dove vengono listati gli elementi che hanno come contenuto il valore selezionato.
![B£TABE_013](http://localhost:3000/immagini/MBDOC_SCH-ST_CC/BXTABE_013.png)###
### Valori di un campo - Righe
Quindi se nella sezione _3_Valori abbiamo selezionato un valore in errore (rosso) nella sezione righe vediamo gli elementi di tabella con il contenuto errato.
![B£TABE_014](http://localhost:3000/immagini/MBDOC_SCH-ST_CC/BXTABE_014.png)