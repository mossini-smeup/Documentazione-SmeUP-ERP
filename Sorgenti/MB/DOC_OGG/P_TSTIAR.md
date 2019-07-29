# Obiettivo
 Interfacciare il programma in esecuzione con l'anagrafico articoli.
Eseguire la ricerca alfabetica relativa degli articoli se richiesto.

# Funzioni e metodi
FUNZIONI
01           Ricerca / decodifica / lettura
02 REFRESH   Elimina ottimizzazione su articolo letto precedentemente
03 SL        SETLL
04 SLRE      SETLL + READE
05 SG        SETGT
06 RE        READE
07 RPE       REDPE
08 RD        READ
09 RP        READP
10 CHA       CHAIN

METODI (PER FUNZIONI DA 2 A 10)
   0L         ARTI
   1L         DEAR/ARTI
   2L         TIAR/ARTI
   3L         GRDI/ARTI
   4L         CALT/ARTI
   5L         RCDV/ARTI
   6L         BARC/ARTI
   7L         CSVA/NOMC
   8L         DISE/ARTI
   9L         CLPR/ARTI
   AL         CLMA/ARTI


# Input
£IARFU :  Funzione
£IARME :  Metodo
£IARAM :  Ambiente
£IARCO :  Contesto
£IARCD :  Codice articolo (se funzione = *Blanks)
£IARTA :  Tipo   articolo (se funzione = *Blanks)
£IARRI :  N.ro Record di input
£IARLC :  Livello chiamata

# Output

BRARTI :  DS valorizzata

 £IARCD :  Articolo (se eseguita ricerca)
£IARDE :  Descrizione articolo
£IARMS :  Codice messaggio ritorno
£IARFI :  File   messaggio ritorno
£IARCM :  Ultimo Comando
£IARRO :  N.ro record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
BRARTI :  DS valorizzata

# Prerequisiti

     D/COPY QILEGEN,£IARDS

# Esempio di chiamata

Esempio 1 :  chiamata secca per reperire i campi della DS BRARTI di uno specifico articolo
     C*                  EVAL      £IARFU=*BLANKS
     C*                  EVAL      £IARCD='codice articolo'
     C*                  EXSR      £IAR
     C*                  IF        £IAR35=*OFF
     C*                  BRARTI VALORIZZATO
     C*                  ENDIF
     C*
Esempio 2 :  scansione di tutti gli articoli che hanno un dato tipo articolo
     C*                  CLEAR                   BRARTI
     C*                  EVAL      £IARFU='SL'
     C*                  EVAL      £IARME='2L'
     C*                  EVAL      £IARTA='TIPO ARTICOLO'
     C*                  EXSR      £IAR
     C*
     C*                  DO        *HIVAL
     C*
     C*                  EVAL      £IARFU='RE'
     C*                  EVAL      £IARME='2L'
     C*                  EVAL      £IARTA='TIPO ARTICOLO'
     C*                  EXSR      £IAR
     C*                  IF        £IAR35=*ON
     C*                  LEAVE
     C*                  ENDIF
     C*
     C*                  ....
     C*                  ENDDO

# Oggetti collegati

# Note particolari

È consigiato eseguire un clear della DS BRARTI prima di richiamare la copy

Parametro aggiuntivo : 
£IARNK :  Numero di campi che si vuole utilizzare nella ricerca.
Non valorizzare £IARNK per lasciare al programma il compito di stabilire il numero di chiavi da usare.
£IARNK viene inserito nell'ultimo carattere di £IARME al richiamo dell'interfaccia.

