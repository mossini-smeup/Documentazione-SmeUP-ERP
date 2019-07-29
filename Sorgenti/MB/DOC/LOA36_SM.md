## Obiettivo
Gestire una serie di oggetti con una matrice di aggiornamento
In numero massimo di oggetti gestibili è 999
E possibile gestire
. immissione
. modifica
. cancellazione
se modifica è possibile aggiungere la riga per l'immissione (default si)
se modifica è possibile aggiungere la colonna per la cancellazione (default si)
L'immissione è gestita con una riga che si autoaggiuge ad ogni riga completata

Se presente l'immissione la grigia viene costruita con il setup dell'immissione.

Le chiamata alla K89 sono
Setup "SET"
Costruzione griglia "CAR" senza oggetto
Tante "CAR" quanti sono gli oggetti in modifica
Una   "CAR" per l'immissione senza oggetto

La funzione "CAR" delal costruzione grigia e le funzioni "CAR" degli oggetti devono essere fra loro congruenti. Devono avere lo stesso numero di campi e nella stessa posizione.
