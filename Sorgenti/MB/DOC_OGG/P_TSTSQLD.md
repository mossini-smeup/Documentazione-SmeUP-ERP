# OBIETTIVO
 Restituisce in formato alfanumerico i risultati di una istruzione SQL Select tramite un cursore
 con allocazione dinamica della SQLDA

# FUNZIONI E METODI

## CLOSE - Chiude il cursore
>    C                  EVAL      £SQLD_FUNFU='CLOSE'
    C                  EVAL      £SQLD_FUNME=*BLANKS
    C                  EXSR      £SQLD


## OPEN - Prepara lo statement, apre il cursore, dimensiona la SQLDA
**Prima di eseguire la funzione 'OPEN' è necessario impostare la variabile £SQLDString con l'istruzione SELECT.

### NAM  - recuperando i nomi di sistema dei campi in £SQLDCName
>    C                  EVAL      £SQLDString=SelectSQL
     * numero di righe per istruzione OPTIMIZE (se 0 assume 5000)
    C                  EVAL      £SQLDRows=n
    C                  EVAL      £SQLD_FUNFU='OPEN'
    C                  EVAL      £SQLD_FUNME='NAM'
    C                  EXSR      £SQLD

### NAMLAB - recuperando i nomi di sistema dei campi in £SQLDCName e le intestazioni in £SQLDCLabel
    **ATTENZIONE :  COMPORTA UN'ALLOCAZIONE DI MEMORIA TRIPLA**
>    C                  EVAL      £SQLDString=SelectSQL
    C                  EVAL      £SQLD_FUNFU='OPEN'
    C                  EVAL      £SQLD_FUNME='NAMLAB'
    C                  EXSR      £SQLD

### LAB - recuperando le intestazioni dei campi in £SQLDCName
>    C                  EVAL      £SQLDString=SelectSQL
    C                  EVAL      £SQLD_FUNFU='OPEN'
    C                  EVAL      £SQLD_FUNME='LAB'
    C                  EXSR      £SQLD


## POS  - Posizionamento cursore
### NEXT - al record successivo
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='NEXT'
    C                  EXSR      £SQLD

### PRIOR - al record precedente
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='PRIOR'
    C                  EXSR      £SQLD

### FIRST - al primo record
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='FIRST'
    C                  EXSR      £SQLD

### LAST - all'ultimo record
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='LAST'
    C                  EXSR      £SQLD

### BEFORE - a BOF
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='BEFORE'
    C                  EXSR      £SQLD

### AFTER - a EOF
>    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='AFTER'
    C                  EXSR      £SQLD

### RELATIVE - relativo al record corrente
**(posizionamento relativo al record corrente di +n o -n in base alla variabile £SQLDRows)**
>    C                  EVAL      £SQLRel=n
    C                  EVAL      £SQLD_FUNFU='POS'
    C                  EVAL      £SQLD_FUNME='RELATIVE'
    C                  EXSR      £SQLD


## READF - Recupera il Valore della colonna
>    C                  EVAL      £SQLD_FUNFU='READF'
    C                  EVAL      £SQLD_FUNME='   '
    C                  EXSR      £SQLD


## FINDC - Recupera la definizione della colonna
### NAM - Ricerca dal nome della colonna in £SQLDCName
>    C                  EVAL      £SQLDCName=NomeCampo
    C                  EVAL      £SQLD_FUNFU='FINDC'
    C                  EVAL      £SQLD_FUNME='NAM'
    C                  EXSR      £SQLD

### LET - Posizionamento
>    C                  EVAL      £SQLD_FUNFU='FINDC'
    C                  EVAL      £SQLD_FUNME='POS'
    C                  EXSR      £SQLD

### LET - Lettura
>     * ciclo sui campi
    C                  DO        *HIVAL
    C                  EVAL      £SQLD_FUNFU='FINDC'
    C                  EVAL      £SQLD_FUNME='LET'
    C                  EXSR      £SQLD
    C                  IF        £SQLD35=*ON
    C                  LEAVE
    C                  ENDIF
    C                  ENDDO


## RETREC - Restituisce in £SQLDString l'intero record
### G18 - con i campi separati da ' '
>    C                  EVAL      £SQLD_FUNFU='RETREC'
    C                  EVAL      £SQLD_FUNME='G18'
    C                  EXSR      £SQLD

### MAT - con i campi separati da '|'
>    C                  EVAL      £SQLD_FUNFU='RETREC'
    C                  EVAL      £SQLD_FUNME='MAT'
    C                  EXSR      £SQLD

### CSV - con i campi separati da ';'
>    C                  EVAL      £SQLD_FUNFU='RETREC'
    C                  EVAL      £SQLD_FUNME='CSV'
    C                  EXSR      £SQLD


## RETINT - Restituisce in £SQLDString le intestazioni
### G18 - con i campi separati da ' '
>    C                  EVAL      £SQLD_FUNFU='RETINT'
    C                  EVAL      £SQLD_FUNME='G18'
    C                  EXSR      £SQLD

### CSV - con i campi separati da ';'
>    C                  EVAL      £SQLD_FUNFU='RETINT'
    C                  EVAL      £SQLD_FUNME='CSV'
    C                  EXSR      £SQLD


# TIPI DI DATI SUPPORTATI
 :  : PAR L(TAB)
- **Tipo dato RPG** | **Tipo dato SQL** | **Tipo dato £IR1**
-  A              |  CHAR           |  A
-  A (VARYING)    |  VARCHAR        |  A
-  05I 0          |  SMALLINT       |  B
-  10I 0          |  INTEGER        |  B
-  20I 0          |  BIGINT         |  B
-  F              |  FLOAT          |  F
-  D              |  DATE           |  L
-  P              |  DECIMAL        |  P
-  S              |  NUMERIC        |  S
-  T              |  TIME           |  T
-  Z              |  TIMESTAMP      |  Z


# VARIABILI
>      * Stringa istruzione SQL (in INPUT)
      * Record restituito (in OUTPUT con funzione 'RETREC')
      * Valore del campo restituito (in OUTPUT con funzione 'READF')
     D £SQLDString     S          32766    VARYING
      *-------------------------------------------------------------------
      * DS INPUT/OUTPUT
     D £SQLD_DS1       DS
      * INPUT
     D* numero in base al quale eseguire il fetch relative (con funzione 'RELATIVE')
     D* numero di righe per l'optimize su apertura cursore
     D  £SQLDRows                    30P 0
      * OUTPUT con info campi (con funzione 'READF')
     D* nome colonna (con metodo 'NAM' o 'NAMLAB') o intestazione (con metodo 'LAB')
     D  £SQLDCName                   30
     D* label (intestazione) colonna (con metodo 'NAMLAB')
     D  £SQLDCLabel                  30
     D* tipo di dato del campo
     D  £SQLDCDType                   5I 0
     D* lunghezza campo stringa
     D  £SQLDCLen                     5I 0
     D* scala campo numerico (numero posizioni decimali)
     D  £SQLDCScale                  10I 0
     D* precisione campo numerico
     D  £SQLDCPrec                   10I 0
     D* indice della colonna corrente del record
     D  £SQLDCurCol                   7  0
     D* numero totale delle colonne del record
     D  £SQLDTotCol                   7  0
     D* tipo di dato del campo nel formato della £IR1AC
     D  £SQLDCDTpIR                   1
      *---------------------------------------------------------------
      * DS OUTPUT Info ERRORE
     D £SQLD_ERROR     DS
      * Indicatore di errore
     D  £SQLD35                        N
      * SQLCOD
     D  £SQLDCOD                      5I 0
      * SQLERM
     D  £SQLDERM                     80
      * %Status (per errori di allocazione di memoria)
     D  £SQLDSTATUS                   5S 0
      * Variabili per errore non SQL
     D  £SQLDVA                      45

# ESEMPIO
>     ESEGUIRE UNA LETTURA DEL BRARTI0F QUERY  :  SELECT * FROM BRARTI0F
     C*APRO
     C                   EVAL      £SQLDString='SELECT * FROM BRARTI0F'
     C                   EVAL      £SQLD_FUNFU='OPEN'
     C                   EVAL      £SQLD_FUNME='NAM'
     C                   EXSR      £SQLD
1    C                   IF        £SQLD35=*ON
     C                   LEAVESR
1e   C                   ENDIF
     C*posizionamento
     C                   EVAL      £SQLD_FUNFU='POS'
     C                   EVAL      £SQLD_FUNME='NEXT'
     C                   EXSR      £SQLD
1    C                   IF        £SQLD35=*ON
     C                   LEAVESR
1e   C                   ENDIF
     C*lettura
     C                   DO        *HIVAL
     C                   EVAL      £SQLD_FUNFU='RETREC'
     C                   EVAL      £SQLD_FUNME='MAT'
     C                   EXSR      £SQLD
1    C                   IF        £SQLD35=*ON
     C                   LEAVE
1e   C                   ENDIF
     C* £SQLDString  CONTIENE IL RISULTATO DELLA FETCH
1e   C                   ENDDO
     C*CHIUDO
     C                   EVAL      £SQLD_FUNFU='CLOSE'
     C                   EVAL      £SQLD_FUNME=*BLANKS
     C                   EXSR      £SQLD
     C* LA FUNZIONE CLOSE CHIUDE IL CURSORE E PULISCE £SQLDString
