# Obiettivo
 Interfacciare il programma in esecuzione con le rate da  registraz.contabili delle diverse applicazioni previste nella  tabella di personalizzazione applicazioni B£1.
 Eseguire la ricerca alfabetica relativa se richiesto

# Input
£IRRFU :  Funzione
£IRRME :  Metodo
£IRRAM :  Ambiente
£IRRCO :  Contesto
£IRRID :  Identificativo rata
£IRRRI :  N.ro Record di input

# Output
£IRRID :  Identificativo rata (se eseguita ricerca)
£IRRDE :  Descrizione rata
£IRRMS :  Codice messaggio ritorno (7)
£IRRFI :  File   messaggio ritorno (10)
£IRRCM :  Ultimo Comando
£IRRRO :  N.ro Record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5RATA :  DS valorizzata


# Prerequisiti
DC5RATE         E DS                  EXTNAME(C5RATE0F) INZ

# Esempio di chiamata
>C*                  Z-ADD     N_campi       £IRRNK
C*                  MOVEL     'Funzione'    £IRRFU
C*                  MOVEL     'Metodo'      £IRRME
C*                  MOVEL     Ambiente      £IRRAM
C*                  MOVEL     Contesto      £IRRCO
C*                  MOVEL     ID_Rata       £IRRID
 *
C*                  EXSR      £IRR
 *
C*                  IF        NOT(*IN35)
C*  36              MOVEL     £IRRID        Campo_Id_Rata
C*                  MOVEL     £IRRDE        Campo_descr
C*                  ENDIF


# Note particolari
£IRRNK :  Numero di campi che si vuole utilizzare nella ricerca (es. se si accede alla vista logica con chiavi AZIE,DIVI,TREG  e si valorizza solo AIZE il programma esclude dalla chiave i campi BLANK e lavora con chiave parziale (nell'es. = AZIE).Se si volesse usare una chiave formata da AZIE e da LIVE=*BLANKS allora si ponga £IRRNK=2).
Non valorizzare £IRRNK per lasciare al programma il compito di stabilire il numero di chiavi da usare £IRRNK viene inserito nell'ultimo char di £IRRME al richiamo dell'interfaccia
