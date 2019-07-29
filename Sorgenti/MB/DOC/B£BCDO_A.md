# Introduzione
Lo script BCD è un motore di esecuzione di programmi, che condividono le stesse aree di memoria, con possibilità di ripetizione di azioni, esecuzioni condizionate, ecc...
Per motivi tecnici, in questo documento le tag di BCD sono precedute dai caratteri '..' In realtà esse vanno precedute da una coppia di due punti.

# Variabili dello script
Sono presenti 20 variabili alfanumeriche (_&_01, _&_02, ... _&_20) e le variabili numeriche di puntamento alle 20 aree dello script : 
>£T01 - £T20  :  riempimento dell'area
£A01 - £A20  :  puntatore   dell'area
£I01 - £I20  :  numero iniziale  area ** definiscono una sezione o una
£E01 - £E20  :  numero finale    area ** scelta

Sono presenti anche 10 flag (gestiti nei programmi come elementi di schiera) ed accessibili dallo script come (/01, /02, .. /10)

# Istruzioni dello script
## Blocco di azioni ripetute fino ad una uscita esplicita
>..DO
   azione
   azione
..ENDDO

## Salto incondizionato
>..ITER   riparte dal ciclo DO in corso
..LEAVE  esce dal ciclo DO in corso
..START  va a inizio programma
..EXIT   va a fine programma

## Blocco condizionato
>..IF <condizione>
   azione
..ELSE
   azione
..ENDIF

## Salto condizionato
>..IF <condizione> CM(xx)
dove xx = ITER, LEAVE, START, EXIT
          con gli stessi effetti del salto incondizionato

## Condizione
>F1(xx) OP(yy) F2(xx)
dove xx = campo costante (max 15 caratteri) oppure variabile _&_x o £x
          oppure variabile d'ambiente : 
          - %01      = £INZJT
          - %02      = Nome dell'elemento BCD
          - %03      = Classe dell'elemento BCD
          - %04      = Ultimo messaggio di ritorno (fornito da un programma BCD o funizzato)
          - %05zzzww = Porzione della stringa parametri dello script : 
                       zzz  :  partenza (da 001 a 200)
                       ww  :  lunghezza (da 01 a 15)
          - %06        = Modalità di esecuzione (NB :  Viene assunta la prima condizione soddisfatta)
                             "L" - Loocup (se £INZJT='B' e Forza emulazione di tabella B§G=' ')
                             "B" - Batch (se £INZJT='B')
                             "I" - Interattiva (in tutti gli altri casi)

       yy   :   LE, LT, GE, GT, EQ, NE

## Pulizia variabili
>..CLEAR
 .*  VR(*ALL) pulisce tutte le variabili (alfan. numeriche e flag)
 .*  VR(*ALF) pulisce le variabili alfanumeriche
 .*  VR(*FLG) pulisce i flag
 .*  VR(*NUM) pulisce le variabili numeriche
 .*  VR(_&_xx)  pulisce la variabile alfanumerica xx
 .*  VR(£yxx) pulisce la variabile numerca xx di tipo y (esempio £T03 :  pulisce il puntatore al riempimento della DS n.3)


## Azioni su variabili numeriche
>..INCR  VR(£yxx) incrementa di 1 la variabile numerica xx di tipo y
..DECR  VR(£yxx) decrementa di 1 la variabile numerica xx di tipo y


## Esecuzione programma con struttura BCD
>..BCD PG(Nome) FU(Funzione) ME(Metodo) PA(Parametri 50 bytes)
Nome, funzione e metodo possono essere variabili _&_x di script
Es PG(_&_01) FU(_&_03)


## Esecuzione programma funizzato
>..FUN PG(Nome) FU(Funzione) ME(Metodo)
Nome, funzione e metodo possono essere variabili _&_x di script
Es PG(_&_01) FU(_&_03)
Viene lanciato il programma senza impostazioni di oggetti (la £FUND1 è inizializzata prima del lancio)

## Esecuzione programma senza parametri
>..PGM PG(Nome)

Il nome può essere una variabile di script

## Commento interno
Qualsiasi riga senza un codice operativo valido viene considerata un commento, e viene esclusa dalla presentazione dello script.
Se si vuole escludere temporaneamente una riga valida, si deve impostare in prima posizione un asterisco : 
Es : 
 ..BCD PG(Nome)

## Commento presentato
Se si vuole riportare un commento nella presentazione dello script, esso va codificato nel seguente modo : 
>..REM Testo libero del commento
..TIT Testo libero del commento con riga bianca precedente


## Esecuzione script con struttura BCD (sv)
-----------------------------------
..SCP(Nome)
Il nome può essere una variabile di script.
Gli script condividono tutte le variabili

# Struttura programma BCD
>Funzione     (10   byte)
Metodo       (10   byte)
Parametro    (50   byte)
DS comune    (2000 byte)
DS specifica (2000 byte)
A01 Campi di 1 byte di passaggio indirizzi schiere, ds, ecc...
...  ,,         ,,       ,,
A20  ,,         ,,       ,,
Messaggio    (7    byte)
File         (10   byte)

### Struttura DS comune
-------------------
>   1 -  100  :  DS della tabella B§G
 101 -  400  :  20 variabili dello script
 401 -  500  :  puntatori £Txx
 501 -  600  :  puntatori £Axx
 601 -  700  :  puntatori £Ixx
 701 -  800  :  puntatori £Exx
 801 -  805  :  numero progressivo di schedulazione
 806 -  815  :  flag della sessione
 816 - 1015  :  parametri dello script

Parametri dello script
----------------------
La variabile 'parametri dello script' contiene 200 caratteri formattati in funzione di quanto impostato nello script per parametri, che si definisce (in modo facoltativo) nell'elemento B§G.

Lo script deve avere la seguente struttura : 
>  Par Lun Valore_____________* Nota----------------------------------------*
V 001 003 ABC                  AAAAAAAAAAAAAAA
N                              BBBBBBBBBBBBBBBBBBBBB
V 004 010 1234567890           AAAAAAAAAAAAAAA

In posizione 1 si imposta 'V' se la riga contiene un valore, 'N' se contiene una nota che verrà visualizzata nella presentazione dei parametri (attivabile via F15 dalla presentazione dello script)

Se la riga è 'V', contiene le seguenti informazioni : 
Posizioni  3 -  5  :  partenza del valore nella stringa parametri (allineato a destra)
Posizioni  7 -  9  :  lunghezza della stringa parametri (max 20)   (allineato a destra)
Posizioni 11 - 30  :  valore
Posizioni 33 - 92  :  nota

Se la riga è 'N', contiene le seguenti informazioni : 
Posizioni 33 - 92  :  nota

All'inizio dell'esecuzione del motore BCD, la stringa parametri viene riempita con il contenuto dello script, e sarà disponibile ai successivi programmi che ne potranno utilizzare alcune parti, sottostringandola.

Nell'esempio dello script precedente, la variabile parametri sarà composta nel seguente modo : 
>'ABC1234567890......
 1---5----0----5 .....

Questa modalità  permette di definire un settaggio del motore BCD a livello più basso di quello definibile tramite il settore dei dati di input, presente sempre nella tabella B§G.
Quest'ultimo contiene i parametri richiesti all'atto del lancio della BCD, la stringa parametri è invece riservata alle impostazioni definite 'una tantum' all'atto dell'implementazione del motore, che possono comunque essere facilmente variate senza modificare nè i programmi nè lo script che contiene i passi da eseguire.

Tabelle
-------
B§G :  Elemento BCD : 
     - pgm innesco
     - script :  nome / src / libreria
     - settore che descrive l'input (futuro :  anche pgm specifico)


Programmi generali
------------------
B£BCD01 :  Richiesta parametri
B£BCD02 :  Esecuzione motore
B£BCD03 :  Debug :  si può inserire come passo BCD dello script (solo in modalità 5250). Presenta un formato video da cui è possibile passare alla presentazione delle variabili del motore
(alfanumeriche, puntatori, flag), del contenuto dell'LDA, della stringa di impostazioni, dell'elemento B§G.
Da questo formato è possibile inoltre eseguire un programma BCD, impostando funzione, metodo e parametri.
Un utilizzo di tale funzione risulta utile condizionato da una variabile d'ambiente, l'elemento BCD o la sua classe.

Oggetti specifici (proposta di standardizzazione)
-------------------------------------------------
>xxyySC     :  Script
xxyyDS     :  /COPY di descrizione delle 20 aree di memoria utilizzate e del loro contenuto
xxyyPLI    :  /COPY dell'ENTRY PLIST dei pgm di esecuzione (con le 20 aree)
xxyyPLO    :  /COPY della PLIST dei pgm di esecuzione in richiamo
xxyyIN     :  Pgm di Innesco
xxyyIN_LO  :  Pgm di Innesco (x LOOCUP) :  è obbligatorio che si chiami come il pgm innesco + '_LO'
xxyyES_01  :  Pgm di Esecuzione 1
xxyyES_02  :     ,,      ,,     2
 ...
dove : 
xx = sigla applicazione
yy = sigla dello script


Quando si aggiunge una DS di lavoro, si devono eseguire le seguenti attività : 
- Definirla nella /COPY xxyyDS
- Inserirla nella PLIST della /COPY xxyyPLI e xxyyPLO
- Ricompilare tutti i programmi xxyyES_zz e l'innnesco xxyyIN

Impostazioni iniziali
---------------------
Si fissano in LDA con la funzione £G67 (eseguita nel lancio BCD se presente nell'elemento B§G il settore per dati di input), con la seguente struttura : 
Posizioni
> 1 -  15   U$NOME Nome della tabella BCD il suo contenuto è zzz
16 -  18   U$LUNG Lunghezza della DS di memorizzaz.impostata dalla £G67

Per acquisire in un programma BCD i campi di input, si deve includere la seguente copy : 
     D/COPY QILEGEN,£xxxxPLI

si definisce l'LDA in questo modo
>     D/COPY QILEGEN,£PDS
     D  U$NOME                 1     15
     D  U$LUNG                16     18  0

