

# Come si costruisce un Input panel da - in una funzione
## Definizione
Tramite l'attributo Showinput="Yes" su una sezione si abilita la richiesta parametri della funzione.
Se nella funzione non sono presenti caratteri -, viene richiesto il codice dell'oggetto 1.
Se una funzione contiene uno o più caratteri -, la richiesta parametri viene mostrata anche in assenza dell'attributo ShowInput nella definizione della sezione.

## Setup del -
Per ogni carattere - presente nella funzione è possibile specificare alcuni comportamenti che il campo relativo deve avere, indicando alcune informazioni dopo lo stesso tra parentesi tonde.

In particolare : 
 :  : PAR F(01) L(PUN)
- Carattere di controllo : 
-- F/b :  Facoltativo  e controllato
-- O/B :  Obbligatorio e controllato
-- c :  Facoltativo e non controllato
-- C :  Obbligatorio e non controllato
- Valore assunto :  Il valore iniziale contenuto nel campo
- Oggetto :  L'oggetto rappresentato dal campo
- Titolo :  L'intestazione del campo
- Nome campo :  Il nome da associare al campo (usato anche come nome di variabile)
- Lunghezza :  La lunghezza in caratteri del campo
- Attributo GRP :  Attributo che può contenere diverse informazioni grafiche (in fase di sviluppo).


## Esempio
F(EXB;*SCO;) 1(ST;;-(O;V5D;ST;Testo a piacere))
imposta il campo per : 
Chiedere obbligatoriamente e controllare un oggetto ST (Settore)
assumendo : 
V5D come valore e intestazione "Testo a piacere"

