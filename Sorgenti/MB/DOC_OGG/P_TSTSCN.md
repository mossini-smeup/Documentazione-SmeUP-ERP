# OBIETTIVO
Ricerca di una stringa (£SCN01) all'interno di un'altra stringa(£SCN02). E' possibile effettuare la ricerca in una sottostringa di £SCN02 specificando posizione iniziale e lunghezza della sottostringa.
# PREREQUISITI
-
# PARAMETRI
## PARAMETRI DI INPUT
- Stringa da ricercare :  _campo £SCN01_

- £SCN01=XX* :  controlla se la stringa/sottostringa da esaminare inizia con XX. Se la ricerca da esito positivo viene restituita la posizione di XX all'interno della stringa £SCN02.
- £SCN01=*XX* :  controlla se la stringa/sottostringa da esaminare contiene XX. Se la ricerca da esito positivo viene restituita la posizione di XX all'interno della sottostringa.
- £SCN01=*XX :  controlla se la stringa/sottostringa da esaminare termina con XX. Se la ricerca da esito positivo viene restituita la posizione di XX all'interno della stringa £SCN02.

- Stringa da esaminare :  _campo £SCN02_

- Posizione iniziale :  _campo £SCN03_
Valore di default uguale a 1

- Lunghezza della sottostringa :  _campo £SCN04_
Valore di default uguale alla lunghezza della stringa £SCN02. Posizione iniziale più lunghezza non deve superare 257.

- Condizione :  _campo £SCN98_
Condizione permette di definire l'opzione di ricerca : 

- 1 :  Case sensitive (valore di default)
- 2 :  Case insensitive

## PARAMETRI DI OUTPUT
- Posizione :  _campo £SCN97_
Posizione iniziale in cui e stata trovata la stringa

- Codice di ritorno :  _campo £SCN99_

- 0 :  Stringa trovata
- 1 :  Stringa non trovata

# ESEMPI DI CHIAMATA
>EVAL      £SCN01='A*'
EVAL      £SCN02='BAAAAAFDGG'
EXSR      £SCN
Valore di £SCN97=*BLANKS
Valore di £SCN99=1

EVAL      £SCN01='A*'
EVAL      £SCN02='BAAAAAFDGG'
EVAL      £SCN03=2
EVAL      £SCN04=5
EXSR      £SCN

Valore di £SCN97=2
Valore di £SCN99=0

# NOTE
-
