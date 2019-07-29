# Obiettivo
Verificare se una copy è presente in un assieme, creare l'oggetto *MODULE relativo

# Input
£MUDFU :  Funzione
£MUDME :  Metodo
£MUDCP :  Copy

* **Funzione 'LET_MAS' - Lista /copy master (con TST)
* **Funzione 'LET_SLA' - Lista /copy slave di un master
* **Funzione 'CHK_CPY' - Controllo tipo copy master/slave
* **Funzione 'CRT_SRC' - Creazione modulo in QTEMP

# Output
£MUD35 :  On=Errore

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£MUDDS

# Esempio di chiamata
 * Lettura copy master
C                   EVAL      £MUDFU='LET_MAS'
C                   EVAL      £MUDME=*BLANK
C                   EVAL      £MUDCP=*BLANK
C                   EVAL      £MUDLD=*BLANK
C                   EVAL      £MUDFD=*BLANK
C                   EVAL      £MUDMD=*BLANK
C                   EXSR      £MUD

# Note particolari
E' collegata alla distinta base £MU (TABRL) e fornisce gli assiemi di una copy
Es :  £DEC ha come componente £DECDS.

