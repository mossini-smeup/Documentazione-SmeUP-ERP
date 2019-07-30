 :  : HEA RESP(BS) STAT(10)
# OBIETTIVO
Gestire tutte le funzioni di servizio per la comprensione e l'analisi dei costruttori grafici.

# FUNZIONI/METODI
## LIS.COM
Restituisce l'elenco dei componenti grafici (V2AGRA) che sono dei costruttori
## LIS.COS
Restituisce l'elenco dei costruttori
## LIS.CAT
Restituisce secondo diversi criteri un elenco di codici di raggruppamento dei costruttori

# SCHEDE CONTENENTI ESEMPI DI CHIAMATE
 :  : DEC T(**) I(Gestione Costruttori) X({F(EXD;*SCO;) 1(;;) 2(MB;SCP_SCH;LOSER_15)}) O(I)

# UTILIZZO PARAMETRO "IND"
Il parametro IND serve per eseguire un filtro sulla scansione dei dati e va strutturato
nel seguente modo : 

Costruttore\Sezione\Subsezione

Dove i valori sono tutti opzionali ma in modo scalare (posso indicare il costruttore e
non sezione e subsezione oppure indico costruttore e sezione, non avrebbe invece senso
indicare solo la subsezione).

