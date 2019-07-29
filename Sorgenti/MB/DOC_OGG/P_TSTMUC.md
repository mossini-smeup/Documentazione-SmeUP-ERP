# Obiettivo
Vengono registrati nel file MUCONV0F tutti gli eventi riguardanti la conversione di un oggetto
Oltre al record di avvenuta esportazione, vengono registrati tutti i possibili errori o warning
che vengono determinati nel momento della conversione dell'oggetto

# Input
£MUCFU :  Funzione
£MUCME :  Metodo
£MUCD1 :  Ds 1
£MUCD2 :  Tracciato file MUCONV

* **Funzione 'LOG' - Scrittura Log**
** __Metodo 'INI' - Inizializzazione log__; viene scritto il record con messaggio MU00100
** __Metodo 'WRI' - Scrittura log__; viene scritto il log con il codice messaggio relativo
** __Metodo 'DEL' - Cancellazione log__; viene cancellato il contenuto relativo all'oggetto
** __Metodo 'CHK' - Check errori__; presenza di errori per oggetto, test su gravità='30'
** __Metodo 'CHA' - Chain su messaggio MUXXXXX__; viene effettuata una chain sul file per verificare la presenza di quello specifico messaggio
* **Funzione 'SCA' - Scansione**; Data una libreria, ritorna i record relativi
** __Metodo 'POS' - Posizionamento log__;
** __Metodo 'LET' - Lettura log__;
* **Funzione 'SCAXMI' - Scansione**; Data una libreria, ritorna i record relativi controllando la presenza del file su IFS
** __Metodo 'POS' - Posizionamento log__;
** __Metodo 'LET' - Lettura log__;


# Output
£MUC35 :  On=Errore
£MUCD2 :  Tracciato del file (solo se LOG CHA)

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£MUCDS

# Esempio di chiamata
 * Scrive log
C                   EVAL      £MUCFU='LOG'
C                   EVAL      £MUCME='WRI'
C                   CLEAR                   MUCONV
C                   EVAL      MULIBR=Libreria oggetto
C                   EVAL      MUOGGE=Oggetto
C                   EVAL      MUSTAT='00'
C                   EVAL      MUMEMB=Nome sorgente oggetto
C                   EVAL      MUTIPO='*PGM'
C                   EVAL      MUMESS=Codice messaggio MSGMU
C                   EVAL      MUINFO=%TRIM(£DMSTE)

# Note particolari

