# Installazione
Per quanto riguarda l'installazione del modulo delle statistiche, le operazioni da effettuare sono le seguenti : 
 * riportare la nuova SMEDEV contenente tutti gli aggiornamenti;
 * lanciare l'estrazione dei dati per alimentare il file delle statistiche;
 * aggiungere l'elemento V5STAT (Statistiche sul fatturato) nella tabella B£A sottosettore MO per poter accedere alla scheda V5STAT tramite il modulo.


Inoltre, bisogna verificare che sia attivata la gestione delle "viste di database". Bisogna verificare l'esistenza del pgm B£IVD0, ed inoltre (IMPORTANTE) deve esiste l'ggetto VD nella tabella *CNTT (oggetti del sistema)

AUTORIZZAZIONI PER PARTIRE :  immetere le autorizzazioni sulla classe LO.FLD e LO.EXD !!!

Sul programma B£IVD0 sono definite le viste relative al file V5STAT0F.
Una vista è un oggetto di tipo VD, il quale definisce già delle condizioni implicite di selezione dei records di un file.

