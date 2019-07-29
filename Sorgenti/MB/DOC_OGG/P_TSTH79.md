
# Funzioni su timestamp
## CTR - controllo 
 Controlla la validità di un timestamp
## CNV - conversione e controllo 
 Controlla la validità di un timestamp e lo converte da un tipo timestamp a un altro

### Campi di input  
**Timestamp numerico  £H79IN**
 Timestamp da controllare o convertire in formato numerico.
 Se presente utilizza il valore numerico.
_3_ N.B. :  per l'oggetto I31 (tempo unix) se viene passato in input £H79IN=0 e £H79IA=''
 vengono considerati 0 millisecondi dal 1 gennaio 1970, quindi una data corrispondente al
 1970-01-01-00.00.00.000000 .
 Se invece viene passato £H79IN=0 e £H79IA<>'' considera £H79IA.

**Timestamp alfa      £H79IA**
 Timestamp da controllare o convertire in formato alfa.
 Se assente il valore numerico utilizza il valore alfa.

**Formato input       £H79F1**
 Formato del timestamp da controllare o formato di partenza del timestamp da convertire.
- [Tipo timestamp](Sorgenti/MB/DOC_OGG/V2_TI_I3)

**Formato output      £H79F2**
 Formato di arrivo del timestamp da convertire.
- [Tipo timestamp](Sorgenti/MB/DOC_OGG/V2_TI_I3)

### Campi di output  
**Timestamp numerico £H79ON**
 Timestamp controllato o convertito in formato numerico.

**Timestamp alfa £H79OA**
 Timestamp controllato o convertito in formato alfa.

**Descrizione £H79DE**
 Descrizione (espressa come YYYY-MM-DD-HH.MM.SS.µµµµµµ).

**Data £H79OD**
 Data numerica formato YYYYMMDD.

**Ora  £H79OH**
 Ora numerica formato HHMMSS.
