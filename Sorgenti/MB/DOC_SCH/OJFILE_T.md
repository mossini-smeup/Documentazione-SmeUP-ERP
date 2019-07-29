# T- Tracciato di un file
Questa scheda permette l'esplorazione del tracciato di un file con la possibilità del drill-down per vedere i valori presenti nei vari campi, una delle possibilità premesse dal drill-down è quella del controllo di congruenza attraverso la quale è possibile identificare i record del file che hanno nel contenuto dei valori non validi.

## Formato scheda
![B£BASE_065](http://localhost:3000/immagini/MBDOC_SCH-OJFILE_T/BXBASE_065.png)
La scheda si suddivide i 3 sottoschede : 
 * _2_campi, è la sottoscheda che si presenta di default, presenta il tracciato dell'archivio con il riferimento agli oggetti Sme.Up. Il doppio click su una riga sposta alla sottoscheda valori di un campo riempita con i valori presenti del campo selezionato.
 * _2_tutti gli errori presenti
 * _2_valori di un campo

## Tutti gli errori presenti
Il programma scorre tutti i record dell'archivio e per ciascuno controlla la validità del contenuto, vengono presentati i campi e relativi valori errati ed il numero di occorrenze dell'errore.
![B£BASE_066](http://localhost:3000/immagini/MBDOC_SCH-OJFILE_T/BXBASE_066.png)Il doppio click sulla colonna "_3_Campo" di una riga sposta alla sottoscheda valori di un campo riempita con i valori presenti del campo selezionato.

## Valori di un campo
A questa sottoscheda si arriva selezionando una riga dalla sottoscheda campi, oppure dalla sottoscheda tutti gli errori presenti.
Per il campo selezionato mostra i valori presenti in tutti i record dell'archivio, vengono evidenziati in rosso i valori errati. Il doppio click manda alla sezione _3_Righe dove vengono listati i record che hanno come contenuto il valore selezionato.
![B£BASE_067](http://localhost:3000/immagini/MBDOC_SCH-OJFILE_T/BXBASE_067.png)###
### Valori di un campo - Righe
Quindi se nella sezione _3_Valori abbiamo selezionato un valore in errore (rosso) nella sezione righe vediamo i record con il contenuto errato.
![B£BASE_068](http://localhost:3000/immagini/MBDOC_SCH-OJFILE_T/BXBASE_068.png)