## Obiettivo
Costruire una richiesta parametri comandata da uno script di configurazione

## Attenzione
Il costruttore è in sviluppo, potrebbe subire revisioni pesanti e non ne viene grantito il funzionamento.

## Script di configurazione
Lo script di configurazione risiede nel source denominato SCP_A42 e possiede i seguenti tag : 

 :  : PAR L(TAB)
**DEF.INI** |Indica il primo passo da eseguire
**DEF.PAS** |Definisce la struttura del passo
**DEF.END** |indica la funzione da lanciare dopo l'ultimo passo


Uno script avrà quindi un tag DEF.INI per indicare da quale passo partire, uno o più tag DEF.PAS che definiscono i passi (Layout, Exit, Prossimo passo, autorizzazioni) e se necessario un tag DEF.END che indica la funzione da lanciare dopo l'ultimo passo. L'ultimo passo è quello per il quale non sia indicato il prossimo passo, oppure il cui prossimo passo sia sbiancato dalla exit.

## EXIT
L'exit (per cui è disponibile il prototipo LOA42_ES01) viene richiamata se indicata nel passo con le seguenti funzioni : 

 :  : PAR L(TAB)
***LAY**|definisce la struttura di XML iniziale e di SETUP
***CTR**|permette di eseguire controlli
***EXE**|permette di eseguire passi finali


### Routine disponibili
Durante la progettazione della Exit abbiamo a disposizione le seguenti routine : 

 :  : PAR L(TAB)
**£A42_INIIZ**|Inserisce la entry plist, definisce la comunicazione con il costruttore. Richiamarla nella £INIZI
**£A42_IMP**|Richiamarla all'inizio della exiT, rende disponibili le variabili del costruttore
**£A42_FIN**|Richiamarla alla fine della exit, informa il costruttore della variazioni apportate
**£A42_FLD**|Utilizzarla per recuperare il contenuto di una variabile, riceve il campo £A42E_CD e ritorna la struttura £A42FLD
**£A42_VAR**|Utilizzarla per cambiare il valore di una variabile esistente
**£A42_ADD**|Utilizzarla per creare e/o modificare la struttura di un campo, comprende la variazione di valore


### Funzione *LAY
Tramite questa funzione è possibile apportare variazioni al layout prima che venga emesso l'input panel
**Esempio di lettura variabile**
 :  : PAR F(04) L(N03)
C                   EVAL      £A42E_CD='LP'
C                   EXSR      £A42_FLD
C                   EVAL      R£NRDM=£A42F_OV


**Esempio di scrittura variabile**
 :  : PAR F(04) L(N03)
C                   EVAL      £A42E_CD='MG'
C                   EXSR      £A42_FLD
C                   EVAL      £A42F_OV=££MAGD
C                   EXSR      £A42_ADD


**Esempio di aggiunta nuovo campo dopo il campo di riferimento già presente**
 :  : PAR F(04) L(N03)
C                   EVAL      £A42F_CD='MGNEW'
C                   EVAL      £A42F_CR='MG'
C                   EXSR      £A42_ADD


**Esempio di aggiunta nuovo campo dopo dopo ultimo campo del layout**
 :  : PAR F(04) L(N03)
C                   EVAL      £A42F_CD='MGNEW'
C                   EXSR      £A42_ADD


### Funzione *CTR
Tramite questa funzione è possibile inserire controlli specifici sui campi del layout
**Esempio di Gestione dell'errore**
 :  : PAR F(04) L(N03)
C                   EVAL      £A42E_CD='MG'
C                   EXSR      £A42_FLD
C                   EVAL      £A42F_ET=TXT(01)
C                   EXSR      £A42_ADD


### Funzione *EXE
Viene eseguita in assenza di errori e prima di procedere al passo sucessivo.
E' possibile cambiare il prossimo passo ed eseguire le procedure di fine passo più opportune

### Esempio
E' presente l'esempio LOA42_ES01 nel file sorgenti QSRCGEN.
