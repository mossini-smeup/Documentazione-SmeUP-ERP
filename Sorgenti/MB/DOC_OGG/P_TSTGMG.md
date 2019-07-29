# £GMG FILTRO MOVIMENTI DI MAGAZZINO

## OBIETTIVI

Fornire funzioni di dialogo tra movimenti di magazzino e chiavi variabili da tipo giacenza.

## FUNZIONI E METODI

### INZ e CTR

Inizializza e controlla un record specifico (di GMMOVI o GMMOAR, definito dal metodo) confrontandolo con dei filtri sul tipo giacenza passati in £GMDDS.
Esegue automaticamente il mapping tra oggetti variabili in £GMDDS e campi dei file (es. per UB controlla il campo S§LOCN).

### RIT/FLD

Restituisce i nomi dei campi di GMMOVI da controllare dati dei tipi oggetti passati esplicitamente in £GMDDS.
Ad esempio, dando in input : 
- £GMDT1='RI', £GMDP1='CDL'
vengono tornati : 
- £GMDP1='S§TRIS', £GMDK1='S§LINE'
In questo modo è possibile impostare degli SQL variabili sui movimenti di un determinato tipo giacenza.

## Oggetti collegati
Le chiavi variabili sono definite nella tabella dei tipi giacenza : 
 :  : DEC T(ST) K(GMQ)

