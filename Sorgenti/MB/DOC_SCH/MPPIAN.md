# Help Operativo
La scheda è studiata per interrogare, modificare, confrontare i valori contenuti nelle viste piano appartenenti ai piani presenti.

![MPPIAN_071](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN/MPPIAN_071.png)
La sezione di sinistra della scheda permette di analizzare i dati presenti seguendo percorsi diversi a seconda che si entri per : 
 * _2_piani, vengono presentati tutti i piani esistenti, eventualmente filtrati se già è stata fatta una selezione precedente
 * _2_viste, vengono presentate tutte le viste esistenti, eventualmente filtrate se già è stata fatta una selezione precedente (es. se è stato in precedenza selezionato un piano, in questa sezione vediamo solo le viste del piano selezionato)
 * _2_famiglie, vengono presentate tutte le famiglie esistenti, eventualmente filtrate se già è stata fatta una selezione precedente
 * _2_tipi oggetto, vengono presentati tutti i tipi oggetto esistenti, eventualmente filtrati se già è stata fatta una selezione precedente

_1_Nota Bene;  il meccanismo del filtro si applica a tutte le selezioni successive che possono essere fatte, es. se ho selezionato un piano e passando alle viste seleziono una vista se passo ai tipi oggetto vedo solo i tipi oggetto della vista del piano.

Per eliminare la selezione eseguita utilizzare il bottone in basso.

![MPPIAN_072](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN/MPPIAN_072.png)
Impostando i vari criteri di ricerca si aggiorna la matrice centrale (contenente i dati relativi ai piani e alle viste che corrispondono ai criteri di ricerca impostati) e le varie sezioni sulla sinistra usate per la ricerca (ad esempio se clicco su una vista, nella sezione piani verrano visualizzati solo quelli a cui corrisponde la vista selezionata).

Se clicco su una riga di questa matrice e sul titolo della sezione in basso vedo nelle due sub-sezioni in basso gli oggetti gestiti nella vista del piano a cui fa riferimento la riga della matrice su cui ho cliccato, se gli oggetti della vista sono 2 si apriranno 2 sub-sezioni, altrimenti si aprirà solo una sub-sezione.
Se sono presenti due sezioni, cliccando su un oggetto in chiave1 e poi sul corrispondente pulsante : 

![MPPIAN_073](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN/MPPIAN_073.png)
nella sezione relativa alla chiave2 vedrò solo gli oggetti che si riferiscono a quella particolare chiave1, analogamente se clicco su un oggetto in chiave2 e poi sul pulsante : 

![MPPIAN_074](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN/MPPIAN_074.png)
Se faccio doppio click su una riga della matrice oppure su uno degli oggetti delle sezioni in basso passo alla scheda di visualizzazione della scheda MPPIAN_GRA relativa a quel piano-vista.

- [Scheda MPS Visualizzazione Vista Piano](Sorgenti/MB/DOC_SCH/MPPIAN_VDP)
- [Scheda MPS Riga di una vista piano](Sorgenti/MB/DOC_SCH/MPPIAN_RVP)
- [Grafici MPS](Sorgenti/MB/DOC_SCH/MPPIAN_GRA)
