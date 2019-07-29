# UMS - Unità di misura
 :  : DEC T(ST) K(UMS)
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la descrizione dell'unità di musura.
 :  : FLD T$UMRI __UM di riferimento__
È un elemento della tabella UMS. Se codificato, è l'unità di misura base collegata (ad esempio, metri per tutte le unità di misura di lunghezza).
 :  : FLD T$FATT __Fattore di conversione__
Se codificata l'unità di misura di riferimento, è il fattore di conversione tra le due unità di misura. Se non inserito, si assume 1.
 :  : FLD T$MUDI __Tipo Fattore__
_7_* :     Moltiplicatore
_7_/ :    Divisore
Se è codificata l'unità di misura di riferimento, definisce se per passare dall'u.m. all'u.m. di riferimento bisogna moltiplicare (*)  o dividere (/) per il fattore di conversione.
Se invece non è codificata l'unità di misura di riferimento, e questo elemento definisce una coppia di u.m. (u.m.1 e u.m.2), definisce se per passare dall'u.m.1 all'u.m.2 bisogna moltiplicare (*) o dividere (/) per il fattore di conversione.
In entrambi i casi, se assente, si assume (/).
_7_P :  Pezzi per unità di tempo
Indica che il valore indicato deve essere trattato come denominatore. Il fattore indica la corrispondenza con l'unità di riferimento. Ad esempio avremo 1 per pezzi ora e 60 per pezzi minuto. In questo caso è consigliato definire i fattori di arrotondamento, al fine di conservare dopo una doppia conversione lo stesso valore di partenza.
 :  : FLD T$NRAR __Fattore arrotondam.__
È il fattore a cui si arrotonda il risultato della conversione.
 :  : FLD T$ARRO __Tipo arrotondam.__
Definisce se l'arrotondamento va eseguito per difetto (-), per eccesso (+), oppure al valore più vicino (H).
 :  : FLD T$UMS1 __Descrizione ISO__
Stabilisce la descrizione dell'unità di misura da utilizzare nella documentazione prodotta. Tale descrizione corrisponderà agli standard in vigore.
 :  : FLD T$UMSC __Contenitore associato__
Definisce l'unità di movimentazione tipica dell'unità di misura.
 :  : FLD T$UMSD __Fatt.Alternativo decimali__
Permette di condizionare il modo in cui vengono trattati i numeri dopo la virgola, al fine di poter gestire valori diversi dai decimali.
I valori ammessi sono : 
1 = Sessagesimi. Per esprimere ore e minuti
2 = Ventiquattresimi. Per esprimere giorni e ore
 :  : FLD T$UMSA __Tipo Oggetto Smeup__
È un elemento *CN/TT che stabilisce il tipo di numero ammesso per l'unità di misura di questa tabella (numero intero, positivo, relativo..)
