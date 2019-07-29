# Obiettivo
Interfacciare il programma in esecuzione con le rate da registraz.contabili delle diverse applicazioni  previste nella tabella di personalizzazione applicazioni B£1. Eseguire la ricerca alfabetica relativa se richiesto
# Funzioni e metodi
# Input
 £IC3FU :  Funzione
£IC3ME :  Metodo
£IC3AM :  Ambiente
£IC3CO :  Contesto
£IC3ID :  Identificativo rata
£IC3RI :  N.ro Record di input

# Output
£IC3ID :  Identificativo rata (se eseguita ricerca)
£IC3DE :  Descrizione rata
£IC3MS :  Codice messaggio ritorno (7)
£IC3FI :  File   messaggio ritorno (10)
£IC3CM :  Ultimo Comando
£IC3RO :  N.ro Record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5RATA :  DS valorizzata

# Prerequisiti
  C5SOLL         E DS                  EXTNAME(C5SOLL0F) INZ

# Esempio di chiamata
## Chiamata con singola lettura
>C*                  Z-ADD     N_campi       £IC3NK
C*                  EVAL      £IC3FU='CHA'
C*                  EVAL      £IC3ME='Metodo'
C*                  EVAL      £IC3AM= Ambiente
C*                  EVAL      £IC3CO= contesto
C*                  EVAL      £IC3ID= ID.Rata
C*                  EXSR      £IC3
C*                  IF        NOT(*IN35)
C*                  EVAL      Campo_descrizione= £IC3DE
C*                  ENDIF


## Chiamata con scansione
>     C*                  CLEAR                   C5RATA
     C*                  EVAL      £IC3FU='SL'
     C*                  EVAL      £IC3ME='0L'
     C*                  EVAL      L5IDOJ=Identificativo'
     C*                  EXSR      £IC3
     C*
     C*                  DO        *HIVAL
     C*
     C*                  EVAL      £IC3FU='RE'
     C*                  EVAL      £IC3ME='0L'
     C*                  EVAL      L5IDOJ=Identificativo'
     C*                  EXSR      £IC3
     C*                  IF        £IC335=*ON
     C*                  LEAVE
     C*                  ENDIF
     C*
     C*                  ....
     C*                  ENDDO

# Oggetti collegati

# Note particolari
È preferibile eseguire un clear della DS  C5RATA prima di ogni richiamo

Parametro aggiuntivo :  £IE3NK :  Numero di campi che si vuole utilizzare nella ricerca (es. se si accede alla vista logica con chiavi AZIE,DIVI,TREG  e si valorizza solo AZIE il programma esclude dalla chiave i campi BLANK e lavora con chiave parziale (nell'es. = AZIE). Se si volesse usare una chiave formata da AZIE e da LIVE=*BLANKS allora si ponga £IE3NK=2). Non valorizzare £IE3NK per lasciare al programma il compito di stabilire il numero di chiavi da usare £IE5NK viene inserito nell'ultimo char di £IE3ME al richiamo dell'interfaccia
