## Modificare una Tabella
Per modificare la struttura di una tabella, ad esempio per aggiungere una nuova colonna, è necessario seguire i seguenti passi : 
 * UP DEF  per entrare nel programma relativo alla modifica di settori e subsettori;
 * inserire 06 "Def. campi" nel campo "Opzioni";
 * inserire il nome della tabella nel campo "Settore" e il nome del sottosettore, se presente, nel campo "Subsettore".
A questo punto compare la schermata di definizione della struttura del settore, in cui specificare per ciascun campo della tabella : 
 ** Seq.  :  numero di sequenza univoco da incrementare a livello di decine, non di unità
 ** Nome Campo  :  nome del campo, secondo la struttura
                              T$ + nome tabella + lettera dell'alfabeto in ordine crescente
 ** Intestazione Campo  :  descrizione del campo
 ** Tp  :  tipo del campo
 ** Param  :  parametro del campo, in base al tipo scelto
 ** Lun  :  lunghezza del campo
 ** Dec  :  numero di cifre decimali, se il campo è numerico
 ** Obl  :  obbligatorietà del campo
 ** Non Ctr  : 
 ** Ann  : 
 ** Pos Ini  :  Posizione inizale del campo

Se la tabella è vuota, i primi due campi (T$ELEM e T$DESC) sono inseriti di default.

Per aggiungere un nuovo campo, è necessario inserire il numero di sequenza (incrementando il valore precedente), il nome, la descrizione, il tipo e il parametro (se necessari) e la lunghezza.

Premere Invio per riempire automaticamente il campo Posizione Iniziale.

Premere F06 per il posizionamento automatico del video :  generalmente è opportuno utilizzare il posizionamento su singola colonna per mantenere la descrizione dei campi, che viene invece persa nel posizionamento a due colonne. Se gli automatismi del tasto funzionale non risultano adeguati, le posizioni dei singoli campi devono essere sistemati manualmente (inserendo una X nel campo "S c" a sinistra del campo da posizionare).

F09 permette di vedere un'anteprima del risultato a video.

Premere F01 per effettuare l'aggiornamento del campo inserito :  se non sono presenti errori, la struttura della tabella viene aggiornata.

Quando si aggiunge / modifica un campo, è necessario compilare l'help relativo : 
 * UP TAB
 * Inserire il nome della tabella nel campo "Settore"
 * Inserire l'opzione 02 "Modifica"
 * Posizionarsi nell'area modificabile del campo di cui si vuole inserire l'help e premere F01 per entrare nella schermata "Documentazione per oggetto", in cui vengono riassunte le proprietà del campo
 * Premere F20 per entrare nell'Editazione della documentazione, del seguente formato fisso :  FLD Nome_del_campo Descrizione_del_campo (FLD è preceduto da due  : ) Documentazione

Quando si effettua una modifica sulla struttura di una tabella, è necessario effettuare una news.

Per cancellare un campo inserito in una tabella, bisogna inserire la lettera 'A' nel campo 'Ann'.

### Superamento del 36° campo
L'attuale codifica standard dei nomi campo delle tabelle è : 
 >>>>>>>> T$XXXY, dove XXX è il nome della tabella e Y è un progressivo alfanumerico.
Se una tabella ha più di 36 campi, tale codifica non è più sufficiente in quanto vengono esauriti i 36 possibili caratteri alfanumerici per la posizione Y.

Dal 37° campo va quindi adottata una codifica diversa : 
 >>>>>>>> T1XXXY
In pratica si sostituisce il T$ con T1. XXX e Y mantengono lo stesso significato (tabella e progressivo).

Ovviamente dall'eventuale 73° campo il prefisso T1 andrebbe sostituito con T2.
