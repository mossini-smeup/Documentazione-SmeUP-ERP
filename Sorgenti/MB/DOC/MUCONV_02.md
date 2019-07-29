## Processo importazione

### Premessa
L'importazione in ambiente multipiattaforma si divide in due fasi : 
* importazione sorgenti;
* importazione dati;
Esistono una serie di comandi per eseguire queste importazioni.

### Importazione sorgenti
Per l'importazione di sorgenti intendiamo, la creazione in ambiente multipiattaforma di una struttura a folder contenente i file .xmi prodotti dalla fase di estrazione.

Il primo comando adibito all'importazione delle librerie in ambiente multipiattaforma è **RCVXMI** "XMI Data Receiver"
Es :  RCVXMI OBJ(SMEUP_DEV/*ALL)

Questo comando genera una cartella che ha come nome quello della libreria con le relative sottocartelle per i tipi oggetto

I parametri di questo comando sono i seguenti : 
* OBJ            (Datastruttura contenente il nome della libreria e dell'oggetto che si vuole importare. Il nome accetta *ALL come valore speciale)
* OBJTYPE   (Tipo oggetto di sistema operativo che si vuole importare :  *FILE, *PGM etc.)
* DATE         (Questo paramentro indica da quale data si intende fare l'importazione)
* REPLACE  (flag per indicare se si vuole rimpiazzare il vecchio sorgente)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualora si presentasse)
* RESTORE  (flag per indicare se si vuole eseguire il restore degli oggetti contestualmente all'importazione)
* DATA    (flag per indicare se si vuole effettuare l'importazione dei dati)

Il secondo comando che può essere usato dopo la ricezione è **RSTXMI** "XMI Data Restorer"
Es :  RSTXMI OBJ(SMEUP_DEV/*ALL) OBJTYPE(*PGM)

Questo comando genera nella cartella della libreria la zona relativa agli oggetti restorati.

I parametri di questo comando sono i seguenti : 
* OBJ            (Datastruttura contenente il nome della libreria e dell'oggetto che si vuole importare. Il nome accetta *ALL come valore speciale)
* OBJTYPE   (Tipo oggetto di sistema operativo che si vuole importare :  *FILE, *PGM etc.)
* REPLACE  (flag per indicare se si vuole rimpiazzare il vecchio sorgente)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualora si presentasse)
* DATA    (flag per indicare se si vuole effettuare l'importazione dei dati)

### Documentazione messaggi relativi al restore di file di database

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Desrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MUS0000   | Eccezione SQL non codificata :  &1                          | 30 |
| MUS0204   | Nome non definito :  &1                                     | 30 |
| MUS0205   | Definizione campo &1 non valida                           | 30 |
| MUS0208   | Oggetto non valido :  &1                                    | 30 |
| MUS0209   | Colonna ambigua :  &1o                                      | 30 |
| MUS0604   | Errore informazioni :  &1                                   | 30 |
| MUS0612   | Nome duplicato :  &1to                                      | 30 |
| MUS0614   | Definizione indice &1 non valida                          | 30 |
| MUS1011   | Correlazione specificata più volte :  &1                    | 30 |
| MUS1940   | Creazione indice non possibile :  &1                        | 30 |
| MUS1942   | Creazione indice non possibile :  &1                        | 30 |
| MUS1944   | Errore dimensione chiave :  &1                              | 30 |
| MUS2714   | Oggetto esistente :  &1                                     | 30 |
| MUS2750   | Precisione specificata non possibile :  &1                  | 30 |
| MUS2760   | Schema non valido :  &1                                     | 30 |
| 


### Documentazione messaggi relativi al restore di oggetti non dbf

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Desrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00310   | Errore in load risorsa                                    | 30 |
| MU00319   | File sorgente &1 non trovato                              | 30 |
| 


### Importazione Dati
L'importazione dati consiste nello scrivere il database multipiattaforma con i dati presenti sul database iSeries.

Il comando adibito all'importazione dei dati in ambiente multipiattaforma è **RCVDTB** "Database Receiver"
Es :  RCVDTB LIB(SMETAB) TBL(*ALL) REPLACE(*YES)

I parametri di questo comando sono i seguenti : 
* LIB (Indica la libreria di cui si vogliono importare i dati)
* TBL   (Indica la tabella da importare, può accettare il valore speciale *ALL)
* WHERE  (clausola where per importare soltanto una porzione di dati di una tabella)
* REPLACE (flag per indicare se si vuole eseguire una pulizia del file prima dell'importazione)
