 :  : HEA RESP(LS) STAT(00)

# OBIETTIVO
Il servizio si propone come strumento di analisi delle proprietà dei campi di un file al fine di arrivare ad una maggiore correttezza e completezza delle informazioni associate ad un campo.
L'analisi effettuata permette di individuare :  i campi non oggettizzati od oggettizzati in modo errato; le dipendenze dei tipi oggetto dinamici; eventuali incompatibilità fra tipo oggetto e valore assegnato al campo; proprietà aggiuntive associate al campo.

# FUNZIONI/METODI

## Lista (LIS)
### dei campi di una applicazione (FLD)
Costruisce la matrice dei campi dei file di una applicazione o dei campi di un file evidenziando per ogni campo il tipo oggetto e la descrizione dell'oggetto, gli errori di assegnazione del tipo oggetto, proprietà aggiuntive del campo.
 :  : PRO.SER Fun="F(EXB;B£SER_44;LIS.FLD) 1(TA;B£A;APP)" Cod="00001"
APP = Applicazione da analizzare
 :  : PRO.SER Fun="F(EXB;B£SER_44;LIS.FLD) 1(OJ;*FILE;FILE)" Cod="00002"
FILE = file da analizzare


## Valori (VAL)
### di un campo (FLD)
Costruisce la matrice dei valori di un campo di un file evidenziando eventuali incompatibilità fra valore assegnato e tipo oggetto e il numero di occorrenze di ogni valore. Nel caso di tipi oggetto dinamici, il servizio risolve la dinamicità in base al tipo oggetto e ai valori dei campi condizione individuati. (vedi B£EQRY_OD)
 :  : PRO.SER Fun="F(EXB;B£SER_44;VAL.FLD) 1(CS;F-FILE;FIELD)" Cod="00003"
FILE = file da analizzare
FIELD = campo del file

## Errori (ERR)
### dei campi (FLD)
Analizza i campi di un file e crea la matrice delle incompatibilità fra i valori assegnati al campo e il suo tipo oggetto. Nel caso di tipi oggetto dinamici, il servizio risolve la dinamicità in base al tipo oggetto e ai valori dei campi condizione individuati. (vedi B£EQRY_OD)
 :  : PRO.SER Fun="F(FBK;B£SER_44;ERR.FLD) 1(OJ;*FILE;FILE)" Cod="00004"
FILE = file da analizzare

## Elenco dei record (OGG)
### per valori (VAL)
Il servizio estrae da un file i record individuati dalle quattro coppie FIELD-VAL. La coppia 2(;FIELD;VAL) contine il nome e il valore del campo di riferimento mentre le coppie 3(;FIELD;VAL), 4(;FIELD;VAL), 5(;FIELD;VAL) contengono i nomi e i valori di eventuali campi condizione, se il tipo oggetto del campo di riferimento è dinamico, in caso contrario duplicano i valori della coppia 2(;FIELD;VAL).
 :  : PRO.SER Fun="F(FBK;B£SER_44;OGG.VAL) 1(CS;F-FILE;FIELD) 2(;FIELD;VAL) 3(;FIELD;VAL) 4(;FIELD;VAL) 5(;FIELD;VAL)" Cod="00005"
FILE = file da analizzare
FIELD = campo di riferimento del file
FIELD-VAL = Coppie campo-valore usate per filtrare i record del file

## Dettaglio (DET)
### di un record (REC)
Costruisce la matrice di dettaglio dei valori di un record di un file.
 :  : PRO.SER Fun="F(OJ;*FILE;FILE) 2(ID;FILE;NREC)" Cod="00006"
FILE = File da analizzare
NREC = Numero del record
