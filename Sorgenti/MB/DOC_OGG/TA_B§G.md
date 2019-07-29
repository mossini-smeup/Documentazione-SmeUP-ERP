# B§G - Elemento di BCD
 :  : DEC T(ST) K(B§G)
## OBIETTIVO
Contiene le informazioni per eseguire una procedura BCD
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Il codice contiene il nome della procedura BCD da eseguire ecc.
 :  : FLD T$B§GA **Programma innesco**
È il nome del programma di partenza della procedura BCD, in cui si definiscono le aree di lavoro utilizzate dall'applicazione.
 :  : FLD T$B§GB **Nome script**
È il nome dello script che contiene il flusso di azioni eseguite dal BCD
In caso di lancio in ambiente LOOCUP senza forzatura di emulazione, deve essere presente, oltre a questo script XXXX, anche lo script XXXX_LO (nello stesso file/libreria) che guida le operazioni di lancio del motore in ambiente grafico.
 :  : FLD T$B§GC **File SRC script**
È il file SRC in cui è presente lo script, se a blanks si assume 'SCP_BCD'
 :  : FLD T$B§GD **Libreria script**
È la libreria in cui è presente il file SRC dello script, se a blanks si assume '*LIBL'
 :  : FLD T$B§GE **Settore di dati input**
Se impostato, i dati di input di questo script verranno richiesti in un configuratore £G30 e descritti in questo settore di tabella (preferibilmente un settore di sola definizione tracciato :  nel campo tabella a elemento fisso si imposta 'L').
 :  : FLD T$B§GF **Forza interattivo**
È obbligatorio impostarlo a "1" per tutti i lavori che prevedono un'interazione con il video, sia in forma grafica, sia in modalità emulazione.
Se lasciato a blank, il successivo campo "Forza emulazione" deve essere impostato.
 :  : FLD T$B§GG **Forza emulazione**
Se impostato, lo script BCD viene eseguito in modalità di emulazione anche se lanciato da ambiente LoocUp.
Se lasciato a blank, il precedente campo "Forza interattivo" deve essere impostato, ed in tal caso lo script verrà eseguito in modalità grafica se in ambiente LoocUp, altrimenti in modalità carattere.
_7_Nota Tecnica
La coppia dei campi 'Forza interattivo' e 'Forza emulazione' permette di stabilire, all'interno dei programmi richiamati in uno script BCD, il modo in cui vengono eseguiti, come esposto nella seguente tabella.
>.                           ! Lancio da ! Lancio da !
.                           !   5250    ! Loocup    !
.----*-----------*----------*---*---*---*---*---*---*------------------------------
.    ! Forza     ! Forza    ! I ! B ! L ! I ! B ! L ! <-- Tipo del lavoro (£INZJT)
.    !Interattivo!Emulazione! I ! B ! L ! I ! B ! L ! <-- Tipo del lavoro (£INZJT)
.----*-----------*----------*---*---*---*---*---*---*------------------------------
. 1) !   ' '     !  ' '     !   !   !   !   !   !   ! Non ammesso :  un lavoro non può
.    !           !          !   !   !   !   !   !   ! essere potenzialmente un
.    !           !          !   !   !   !   !   !   ! servizio e non essere
.    !           !          !   !   !   !   !   !   ! obbligatoriamente interattivo
.----+-----------+----------+---+---+---+---+---+---+------------------------------
. 2) !   ' '     !  '1'     ! * ! * !   !   ! * ! * ! Se 'B' è un lavoro 'realmente' batch
.    !           !          !   !   !   !   !   !   ! Se 'I' o 'L' è un lavoro interattivo
.----+-----------+----------+---+---+---+---+---+---+------------------------------
. 3) !   '1'     !  ' '     ! * !   !   !   ! * !   ! Se 'B' è un servizio grafico
.    !           !          !   !   !   !   !   !   ! Se 'I' è un lavoro interattivo
.----+-----------+----------+---+---+---+---+---+---+------------------------------
. 4) !   '1'     !  '1'     ! * !   !   !   !   ! * ! È sempre un lavoro interattivo
.    !           !          !   !   !   !   !   !   !
.----*-----------*----------*---*---*---*---*---*---*------------------------------



Si consiglia di utlizzare le seguenti impostazioni : 
2) Per un lavoro batch
3) Per un lavoro che si setta automaticamnete come interattivo se lanciato in 5250, o Loocup, se lanciato da Loocup.

 :  : FLD T$B§GH **Gruppo appartenenza**
Se impostato, può essere attivo solo un motore BCD dello stesso gruppo.
Viene utilizzato il tipo log BK_BCD (elemento di tabella B§L)
 :  : FLD T$B§GI **Classe di esecuzione**
Questo valore viene utilizzato come variabile d'ambiente dello script. In questo modo è possibile far condividere lo stesso script ad elementi diversi e condizionarne l'esecuzione. Ad esempio, si può impostare nello script che alcuni passi di presentazione tecnica siano eseguiti solo se questa classe vale 'D' (iniziale di DEBUG).
Alcune classi sono riservate.
Ad esempio, per la schedulazione fine, la classe MI fa sì che venga presentata la memoria iniziale
 :  : FLD T$B§GJ **Script per parametri**
Se presente (come elemento del File Src e Libreria impostati nei campi successivi) contiene unset di parametri caratteristici della BCD, che sono disponibili (come sottostringhe diun campo generico di impostazioni), per i programmi della BCD.
In questo modo si può eseguire uno script con parametri diversi, semplicemente codificando più elementi della presente tabella, ciascuno con un diverso script di parametri.
 :  : FLD T$B§GK **File SRC script dei parametri**
È il file SRC in cui è presente lo script dei parametri, se a blanks si assume 'SCP_BCD'
 :  : FLD T$B§GL **Libreria script dei parametri**
È la libreria in cui è presente il file SRC con lo script dei parametri, se a blanks si assume '*LIBL'
 :  : FLD T$B§GM **Suffisso Richeste utente**
Normalmente le informazioni necessarie per l'esecuzione del motore vengono reperite tramite la funzione standard £G67,
che presenta un formato di richiesta con i campi del "settore dei dati di input" definito in questo elemento.
Se si imposta il presente campo, le richieste vengono fatte invece lanciando il programma XXXXX_Y (se presente), dove
XXXX è il programma di innesco (sempre definito in questo elemento), e Y è questo campo.
Per convenzione, sono da usare i prefissi alfabetici per exit utente, mentre quelli numerici sono riservati ad exit
standard. Ad esempio, l'exit 1 (S5SMIN_1) è riservato per la modalità di Fine.Up in consultazione.
Tale programma, di cui è fornito il prototipo S5SMIN_I, deve riempire le posizioni di LDA a partire dalla 19 con
i campi del "settore dei dati di input".
Il modo in cui lo fa è totalmente libero :  può richiedere i dati, può reperirli in modo cieco, può derivarne alcuni
da quelli richiesti, ecc...
 :  : FLD T$B§GN **Presenta statistiche**
Se impostato, viene abilitato il lancio il programma di presentazione statistiche, che dà informazioni sulle esecuzioni
precedenti di questo motore.
Il programma di presentazione si deve chiamare XXXX_ST, dove XXXX è il programma di innesco (definito in questo script).
Questo campo può assumere i seguenti valori : 
- 1  Viene abilitato il tasto funzionale F16 nel formato di lancio del motore (dove è richiesto il nome dell'elemento
     BCD da eseguire)
- 2  Viene presentato un bottone nel pannello di lancio di Loocup. In tal caso viene presentato anche il bottone dl
     lancio della schedulazione, in quanto questa nuova possibilità fa sì che a questo punto ci sia più di una scelta.
- 3  Sonmo attive entrambe le precedenti impostazioni.
 :  : FLD T$B§GO **Suffisso exit tasto**
Se impostato, nella presentazione dello script BCD (richiamato dal formato di richiesta elemento BCD), viene lanciato il programma B£BCD02_x (dove x è il presente suffisso).
La presenza di questo programma attiva il tasto F18 nella lista di presentazione dello script BCD :  in esso è possibile sia impostarne il significato, sia eseguire l'azione conseguente.
Per la schedulazione Fine.Up, è stato realizzata l'exit B£BCD02_1 (il suffisso numerico indica una exit standard) che permette di impostare i suffissi delle exit della schdulazione.
E' quindi opportuno, per gli elementi BCD relativi alla schedulazione, impostare questo campo a '1'.
 :  : FLD T$B§GP **Ambiente di memorizzazione BCD**
Definisce l'ambiente di memorizzazione di un'esecuzione di BCD per individuarlo in caso di interrogazione.
 :  : FLD T$B§GQ **Memorizza sessione**
Se impostato, all'atto del consolidamento dei risultati di una sessione BCD, vengono fotografate tutte le memorie, in modo da poter interrogare, in seguito, questa situazione.
 :  : FLD T$B§GR **Data inizio memor.**
Se impostato, vengono mantenute le sessioni di interrogazione eseguite con data maggiore o uguale a questa. Naturalmente si deve impostare una data implicita.
Se non impostato, si assume la data odierna.
