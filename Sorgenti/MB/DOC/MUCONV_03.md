## Compilazione oggetti

### Premessa
Gli oggetti compilabili in ambiente multipiattaforma sono : 
* DSPF
* PRTF
* DBF
* MODULE
* PGM
Il processo di compilazione, implica la trasformazione del modello neutro (file .xmi) in un oggetto per il sistema di destinazione (file .java e .class)
Questo avviene per tutti gli oggetti sopra citati.
I Moduli ed i Programmi hanno un processo intermedio di ulteriore trasformazione ed ottimizzazione.

### DSPF - Display File
Il comando per compilare i display file è :  **CRTXMIDSPF** "Create XMI DisplayFile"
Es :  CRTXMIDSPF FILE(SMEUP_DEV/V5DO01DV)

Questo comando genera un file .java depositandolo nella cartella "src" della libreria di destinazione

I parametri di questo comando sono i seguenti : 
* FILE   (Datastruttura contenente il nome della libreria e del display file che si vuole compilare. Il nome accetta *ALL come valore speciale)
* TOLIB   (Specificare questo parametro per impostare una libreria di destinazione differente da quella del parametro FILE)


### PRTF - Printer File
Il comando per compilare i printer file è :  **CRTXMIPRTF** "Create XMI PrinterFile"
Es :  CRTXMIPRTF FILE(SMEUP_DEV/V5BO01SP)

Questo comando genera un file .java depositandolo nella cartella "src" della libreria di destinazione

I parametri di questo comando sono i seguenti : 
* FILE   (Datastruttura contenete il nome della libreria e del printer file che si vuole compilare. il nome accetta *ALL come valore speciale)
* TOLIB   (Specificare questo parametro per impostare una libreria di destinazione differente da quella del parametro FILE)

### DBF - Database File
Il comando per compilare i database file è :  **CRTXMIDBF** "Create XMI DatabaseFile"
Es :  CRTXMIDBF FILE(SMEUP_DAT/V5TDOC0F)

Questo comando genera un file .java depositandolo nella cartella "src" della libreria di destinazione

I parametri di questo comando sono i seguenti : 
* FILE   (Datastruttura contenete il nome della libreria e del file di database che si vuole compilare. Il nome accetta *ALL come valore speciale)
* TOLIB   (Specificare questo parametro per impostare una libreria di destinazione differente da quella del parametro FILE)

### MODULE - Moduli
I moduli prima della compilazione necessitano di una conversione, ovvero una ulteriore trasformazione del modello neutro originale, generando un modello intermedio.

Il comando per covertire i moduli è :   **CVTXMIMOD** "XMI Module Converter"
Es :  CVTXMIMOD MOD(SMEUP_DEV/£DEC)

I parametri di questo comando sono i seguenti : 
* MOD   (Datastruttura contenente il nome della libreria e del modulo che si vuole convertire. Il nome accetta *ALL come valore speciale)
* APP   (Filtro per applicazione)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualore si presentasse)

Il comando per compilare i moduli è :    **CRTXMIMOD** "XMI Module Compiler"
Es :  CRTXMIMOD MOD(SMEUP_DEV/£DEC)

I parametri di questo comando sono i seguenti : 
* MOD   (Datastruttura contenete il nome della libreria e del modulo che si vuole compilare. Il nome accetta *ALL come valore speciale)
* APP   (Filtro per applicazione)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualora si presentasse)
* CVT    (flag per indicare se eseguire il processo di conversione contestualmente alla creazione)

### PGM - Programmi
I programmi, cosi come i moduli, prima della compilazione necessitano di una conversione, ovvero una ulteriore trasformazione del modello neutro originale, generando un modello intermedio.

Il comando per covertire i programmi è :  **CVTXMIPGM** "XMI Program Converter"
Es :  CVTXMIPGM PGM(SMEUP_DEV/B£DEC0)

I parametri di questo comando sono i seguenti : 
* PGM   (Datastruttura contenente il nome della libreria e del programma che si vuole convertire. Il nome accetta *ALL come valore speciale)
* APP   (Filtro per applicazione)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualora si presentasse)

Il comando per compilare i programmi è :   **CRTXMIPGM** "XMI Program Compiler"
Es :  CRTXMIPGM PGM(SMEUP_DEV/B£DEC0)

Questo comando genera un file .java depositandolo nella cartella "src" della libreria di destinazione

I parametri di questo comando sono i seguenti : 
* PGM   (Datastruttura contenente il nome della libreria e del programma che si vuole compilare. Il nome accetta *ALL come valore speciale)
* APP   (Filtro per applicazione)
* LOG    (flag per indicare se si vuole scrivere un log di errore qualora si presentasse)
* CVT    (flag per indicare se eseguire il processo di conversione contestualmente alla creazione)
* REPLACE (flag per indicare se si vuole rimpiazzare il vecchio sorgente)
* TOLIB   (Specificare questo parametro per impostare una libreria di destinazione differente da quella del parametro PGM)
* SRCTYPE (CL/RPG - Specioficare questo parametro per filtrare la compilazione)
* FORMAT (flag per indicare se si vuole eseguire la formattazione del testo dopo la creqazione del file)
* DATE (Specificare questo parametro per compilare oggetti restorati alla data)
quella del parametro PGM)

### Documentazione messaggi relativi alla compilazione di programmi e moduli

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Desrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00319   | File sorgente &1 non trovato                              | 30 |
| MU00335   | Errore non codificato :  &1                                 | 30 |
| MU00341   | Errore di IO :  &1                                          | 30 |
| MU00342   | Statement non valido :  &1                                  | 30 |
| MU00343   | Loading non valido :  &1                                    | 30 |
| 

