 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Questo servizio permette di lanciare l'esecuzione di funzioni che non sono contenute in
pgm di servizio specifico, ma il cui svolgimento è invece contenuto in pgm o in una funzione
richiamabile in una chiamata funizzata. Tipicamente si tratta di programmi funzionanti in nero-verde
in cui è stato introdotto l'output su coda (in pratica al passaggio di determinate condizioni
invece di scrivere un subfile scrive l'xml di una matrice nella coda del servizio).
Per un esempio si veda il pgm GMGMJ0

Questo servizio essendo di carattere generale non gestisce alcuna funzione/metodo specifica.

I parametri assumono i seguenti significati.

T1/P1/K1 ---> £FUNT1/P1/K1
T2/P2/K2 ---> £FUNT2/P2/K2
T3/P3/K3 ---> £FUNT3/P3/K3
K4       ---> £FUNPG
K5       ---> £FUNFU
K6       ---> £FUNME
Parametri --> £FUND2


