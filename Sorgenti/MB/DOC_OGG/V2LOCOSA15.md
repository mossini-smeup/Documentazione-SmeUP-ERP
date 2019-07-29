## Scheda Analisi delle fonti
La scheda è uno strumento di business intelligence integrato in Looc.Up che permette l'analisi multidimensionale di fenomeni diversi legati all'attività dell'azienda.

##  Terminologia e processo
* _2_Dimensioni, sono le colonne sulle quali si applica l'analisi multidimensionale. Una colonna può rappresentare ad esempio gli articoli venduti, i clienti, le provincie, gli agenti, ecc.... Le dimensioni  possono essere indipendenti (generalmente corrispondono agli oggetti Sme.Up) oppure derivate (generalmente attributi degli oggetti).
* _2_Misure, sono i valori associati alle dimensioni ad esempio la quantità venduta o acquistata, l'importo, il costo unitario, ecc....
* _2_Fonti, rappresentano le informazioni che vengono sottoposte ad analisi.
* _2_Gruppi fonte, raggruppano fonti della stessa natura che vengono preparate per l'analisi nello stesso processo.
* _2_Schemi, rappresentano i dati di una fonte con raggruppamenti e/o completamenti (dimensioni aggiuntive calcolate come attributi di dimensioni esistenti e misure aggiuntive come elaborazioni di misure esistenti) impostati nello script di configurazione.

Il processo prevede : 
* _2_Definizione dello script di impostazione, questo risiede nel file _3_SCP_SET, e comprende le parametrizzazioni che saranno utilizzate sia in fase di estrazione e completamento dei dati che in fase di analisi
* _2_Estrazione delle informazioni, eseguita da un programma che, con logiche utente, estrae le informazioni dal database e scrive un file di lavoro. Programma ed eventuali parametri di condizionamento sono definiti nello script.
* _2_Completamento, eseguito dal programma LOA15_GC che completa i dati estratti aggiungendo attributi di oggetti e creando nuove misure come risultato di operazioni matematiche su misure esistenti. Le informazioni vengono memorizzate in file creati in una apposita libreria, uno per ciascuna fonte più uno per ogni schema. I parametri di condizionamento del completamento sono definiti nello script.

La composizione del nome della libreria avviene nel seguente modo a seconda di quanto impostato nella tabella **LO1**
**SBI_yyyxxT**
dove _7_yyy è il valore presente nel campo T$LO1A, _7_xx è il codice azienda presente in B£2 (££B£2A) e il carattere T viene aggiunto qualora sia valorizzato il flag ambiente di test in B£2 (££B£2Z).

Quindi qualora T$LO1A sia valorizzato a G001 e l'azienda in B£2 a 01 avremmo come libreria dati del LOA15 **SBI_G00101** per l'ambiente di produzione e **SBI_G00101T** per l'ambiente di test.

Qualora >non sia valorizzato T$LO1Ala composizione del nome della libreria avviene nel modo : 
**SMEUPBIxxT**
dove  _7_xx è il codice azienda presente in B£2 (££B£2A) e il carattere T viene aggiunto qualora sia valorizzato il flag ambiente di test in B£2 (££B£2Z).

* _2_Analisi, utilizzando la scheda LOA15.

## La scheda
La scheda si presenta nel modo seguente : 

![LOA15_001](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_001.png)
 * Nella sotto-sezione di sinistra denominata _2_Fonti vengono elencati gruppi fonte, fonti e schemi presenti nello script di configurazione, per procedere è necessario selezionare uno schema (es. A2.F2.S3)
 * La sezione sottostante denominata in partenza _2_Azioni è sensibile allo schema selezionato e presenta : 
 ** _3_Azioni di report, queste sono le azioni da selezionare in modo che nella sezione di destra compaia una analisi
 ** _3_Azioni di fonte, sono le azioni legate alle fonti (costruzione, eliminazione, documentazione)
 * Nella sezione di destra viene presentato il tipo di report scelto
 * Il bottone _2_Aggiornamento permette di ricaricare gli script di configurazione (es. è stato definito una nuova fonte o un nuovo schema)
 * La sotto-sezione di sinistra denominata _2_Set'n play porta alle schede di impostazione, tra cui gli script di configurazione e quelli dei flussi

## Azioni di report
### Matrice
Quando viene selezionata questa azione nella sezione di destra viene presentata una matrice : 
![LOA15_002](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_002.png)
### Report
Quando viene selezionata questa azione parte il configuratore per la produzione di un report in formato pdf : 
![LOA15_003](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_003.png)
### Foglio di lavoro
Quando viene selezionata questa azione parte il configuratore per l'export su foglio di lavoro : 
![LOA15_004](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_004.png)LOA15)

### Analisi di Pareto
Questa azione lancia l'analisi di Pareto, selezionare la dimensione e la misura da analizzare, nella parte di destra viene presentata l'analisi in forma di matrice : 
![LOA15_005](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_005.png)la stessa analisi può essere vista in forma grafica : 
![LOA15_006](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_006.png)
### Drill down
Richiede di selezionare una dimensione, mostra tutti i codici presenti per la dimensione selezionata, quando si sceglie uno dei codici viene emessa una matrice con tutti record del codice selezionato, la matrice può essere raggruppata in funzione dello script di configurazione : 
![LOA15_007](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_007.png)
### Analisi tabellare standard
Questa azione lancia la scheda LOA03 : 
![LOA15_008](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_008.png)
### Costruzione report
Viene lanciato il programma LOA15_GF per la ricostruzione del report identificato dallo specifico schema : 
![LOA15_009](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_009.png)
### Eliminazione report
Viene lanciato il programma LOA15_GF per l'eliminazione del report identificato dallo specifico schema : 
![LOA15_010](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_010.png)
### Set'n play
Mostra una serie di sottoschede statistiche sulla elaborazione delle fonti : 

_1_Cruscotto
Mostra i dati raccolti l'ultima volta che la fonte è stata ricostruita (durata elaborazione, data/ora creazione, righe, anzianità del dato, ecc...) : 
![LOA15_011](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_011.png)
_1_Oggetti
Mostra gli oggetti di sistema (programmi, file, tabelle, ecc...) interessati : 
![LOA15_012](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_012.png)
_1_Parametri report
Mostra le impostazioni (default ed utente) presenti per la produzione dei report : 
![LOA15_013](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_013.png)
_1_Dati report
Mostra tutti i record presenti nel file relativi al report (lo schema) : 
![LOA15_014](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_014.png)
_1_Parametri fonte
Mostra le impostazioni (default ed utente) presenti per la produzione della fonte : 
![LOA15_015](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_015.png)
_1_Dati fonte
Mostra tutti i record presenti nel file relativi alla fonte : 
![LOA15_016](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_016.png)
_1_File BI azienda
Mostra tutti i file contenuti nella libreria SMEUPBIaa (aa = azienda) : 
![LOA15_017](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_017.png)
_1_Azioni gruppo
Elenca le azioni di gruppo : 
![LOA15_018](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_018.png)
_1_Azioni globali
Elenca le azioni globali : 
![LOA15_019](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_019.png)
_1_Dimensioni
Mostra le dimensioni (campi Cxx) di tutti i record presenti nel file : 
![LOA15_020](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_020.png)
_1_Misure
Mostra le misure (campi Vxx) di tutti i record presenti nel file : 
![LOA15_021](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_021.png)
_1_Funzioni
Mostra le funzioni presenti nello script : 
![LOA15_022](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_022.png)
### Documentazione report
Permette di leggere e/o creare-modificare la documentazione utente specifica del report : 
![LOA15_023](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_023.png)
## Azioni di fonte
### Costruzione fonte
Lancia il programma di ricostruzione della fonte : 
![LOA15_024](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_024.png)
### Eliminazione fonte
Lancia il programma di eliminazione della fonte : 
![LOA15_025](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_025.png)
### Documentazione fonte
Permette di leggere e/o creare-modificare la documentazione utente specifica della fonte : 
![LOA15_026](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA15/LOA15_026.png)
## Set'n Play
Questa sottoscheda rimanda a sua volta : 
 * _2_alla scheda LOA07, per la gestione dello script di configurazione del LOA15 (per l'utilizzo vedi Help specifico)
 * _2_alla scheda LOA11, per la gestione dei flussi (per l'utilizzo vedi Help specifico)
 * _2_alla scheda LOA17, per la gestione dell'invio e-mail (per l'utilizzo vedi Help specifico)
 * _2_alla presentazione in forma di matrice delle fonti dei cubi (Tabella D9B)
 * _2_alla presentazione in forma di albero delle fonti dei cubi (Tabella D9B)

## Schedulare la costruzione di un LOA15

Per schedulare la creazione del LOA15 BISOGNA passare dal programma LOA15_AM che serve ad impostare la £PDS con l'ambiente necessario al recupero dei  parametri (configurazioni *ENV) utilizzati nella costruzione delle fonti del LOA15 in modo che sia possibile la costruzione delle fonti schedulata tramite WRKJOBSCDE.
Al LOA15_AM bisogna passare come quarto parametro il codice dell'ingresso utente di UP UT5 corrispondente all'ambiente per l'utente con il quale verrà schedulato il lavoro.


 Esempi di chiamata : 
 - Costruzione di TUTTE le fonti del'ingresso utente 0006 (Derivato dalla UT5)
   CALL PGM(LOA15_AM) PARM('ALL' 'COS' '' '0006')
 - Costruzione di un gruppo fonti (dove X2 indica tutte le fonti dello script LOA15_X2)
   CALL PGM(LOA15_AM) PARM('GRU' 'COS' 'X2' '0006')
 - Costruzione di una singola fonte (dove X9.F3 indica l'identificativo della fonte)
   CALL PGM(LOA15_AM) PARM('FON' 'COS' 'X9.F3' '0006')

Si può forzale la lettura di una configurazione personale utilizzando il quinto parametro specificando il nome della stessa nell'attributo**NCfg()**oppure passare delle proprie impostazioni.
Naturalmente l'utilizzo di questo parametro disabilita la configurazione di tipo *ENV specificata nello script della fonte.

Esempio di chiamata
   CALL PGM(LOA15_AM) PARM('FON' 'COS' '' '0006' 'NCfg(Mia)')
   CALL PGM(LOA15_AM) PARM('FON' 'COS' '' '0006' 'Cod1(A01) Cod2(B01)')
