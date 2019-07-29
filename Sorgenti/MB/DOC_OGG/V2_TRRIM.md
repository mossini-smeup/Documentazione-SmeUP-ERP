# TRRIM     -  TIPO RIGA RICHIESTA DI MOVIMENTAZIONE
Definisce la natura della riga di richiesta di movimentazione in modo noto all'applicazione, che in tal modo può
assumenre comportamenti specifici in funzione di esso.

## VALORI POSSIBILI

### 'P' PRELIEVO (NESSUNA DESTINAZIONE)
Definisce una richiesta di prelievo :  l'assegnazione determinerà unicamente l'origine di queste richieste.

### 'V' VERSAMENTO (NESSUNA ORIGINE)
Definisce una richiesta di versamneoto :  l'assegnazione determinerà unicamente la destinazione  di queste richieste.

### 'D' FISSO DESTINAZIONE CALCOLO ORIGINE
Definisce una richiesta di trasferimento in cui si fissa la destinazione :  l'assegnazione determinerà unicamente
l'origine di queste richieste.

### 'O' FISSO ORIGINE CALCOLO DESTINAZIONE
Definisce una richiesta di trasferimento in cui si fissa l'origine :  l'assegnazione determinerà unicamente la
destinazione di queste richieste.

### 'T' TRASFERIMENTO
Definisce una richiesta di trasferimento in cui non si fissa niente :  l'assegnazione determinerà sia l'origine sia la
destinazione  di queste richieste.
