
## LO SCHEMA

Per effettuare la creazione degli schemi di lettura e di intestazione si usa la funzione /COPY  **G25**

La **G25** si occupa di impostare i titoli delle colonne e delle righe di dettaglio variabili per la presentazione degli attributi di un particolare oggetto; lancia il pgm "<nome_file>_I" che a sua volta richiama il programma B£GI25 (Costruzione stringhe per interrogazione generalizzata).

### PREREQUISITI DELLA G25

La **G25** deve essere definita come una Data Structure (DS) esterna con il tracciato record uguale a quello del file da gestire.

>Esempio :       I       £G25DS              E         I         DS                PROVA0F

### PARAMETRI DI INPUT E DI OUTPUT
>**Input : **
	             £G25FU :  Funzione (10)
   	                           COSTES = Costruzione testata
 	                           COSRIG = Costruzione riga
 	            £G25ME :  Modello (10)
                              £G25FI :  File da gestire (8)
                 	            £G25SC :  Schema interrogazione (1)
                                             Valori :  da 1 a 5 (si veda tab. INT)
                              £G25LN :  Lunghezza delle righe (3 0)

**Output** : 
	           £G25R1 :  Riga 1 colonne o riga dettaglio (198)
                             £G25R2 :  Riga 2 colonne (198)
                             £G25RC :  Codice ritorno (7)


### SPECIFICITA' NEL RICHIAMO DI B£GI25E

 Questa routine richiama il programma <nomefile>_I (o _U), quindi quest'ultimo chiama il programma B£GI25E, passandogli una funzione in base al metodo ricevuto dalla £G25, secondo  la seguente tabella : 

>Funzione/Metodo G25	-------------------->  Funzione B£GI25

COSTES -----> COSTRUZIONE TESTATA
------------>	ST/M------>	Stampa Manuale------->TM
------------>	VI/M------>	Visual. Manuale--------->TM
------------>	TR/M----->	Trasf. Manuale--------->	tM
------------>	ST/A------>	Stampa Automatica-->	TV
------------>	VI/A------>	Visual. Automatica---->	TV
------------>	TR/A----->	Trasf. Automatico---->	tV
			
COSRIG -----> COSTRUZIONE RIGA
------------>	ST--------->	Stampa ----------------->RS
------------>	VI--------->	Visualizzazione---------->RV
------------>	TR-------->	Trasferimento---------->RT



### ESEMPIO DI CHIAMATA
>Input : 
 EVAL £G25FU='Funzione'
 EVAL £G25FI=NomeFile
 EVAL £G25SC=Schema
 Z-ADD Lung_Riga £G25LN C* EXSR £G25

 Output : 
 EVAL Titoli1=£G25R1
 EVAL Titoli2=£G25R2

## DEFINIZIONE DEGLI ATTRIBUTI E DEI VALORI DELL'OGGETTO
Per gestire i vari attributi ed i valori associati ad un oggetto, si deve utilizzare la /COPY **OAV**, che consente di eseguire molteplici funzioni, tra le quali la visualizzazione del dettaglio attributi relativi ad un oggetto (Gestione dizionario attributi); l'immissione, copia, modifica, cancellazione (Gestione singolo valore attributo); creazione gruppi di attributi o scelta tra diversi attributi (Scelta), ed altre operazioni quali costruzione di un modello e la scansione singola, per gruppo o per radice di categoria.

## CODIFICA DEGLI SCHEMI E  PARAMETRI PER INTERROGAZIONE
Per la definizione della sequenza dei campi dello schema nella simulazione della /COPY **G25**, nel campo "Schema Interrogazione" digitare !, quindi digitare D sullo schema da definire (si può scegliere tra uno dei 5 schemi predefiniti).
- [INT - Parametri interrogazione standard](Sorgenti/MB/DOC_OGG/TA_INT)

Gli schemi di interrogazione usati sono definiti nella tabella delle interrogazioni :  per accedere alla tabella nella riga di comando digitare **UP TAB**, nel settore indicare INT (interrogazioni) e nel campo subsettore l'oggetto a cui si riferisce l'interrogazione.
- [Gestione schemi interrogazione (INT](Sorgenti/MB/DOC_OGG/P_TSTG25)
