# Obiettivo
Interfacciare il programma in esecuzione con registrazioni di contabilità analitica delle diverse applicazioni previste nella tabella di personalizzazione applicazioni B£1.
Eseguire la ricerca alfabetica relativa se richiesto

# Input
£IMHFU :  Funzione
£IMHME :  Metodo
£IMHAM :  Ambiente
£IMHCO :  Contesto
£IMHID :  Identificativo rata
£IMHRI :  N.ro Record di input

# Output

£IMHID :  Identificativo rata (se eseguita ricerca)
£IMHDE :  Descrizione rata
£IMHMS :  Codice messaggio ritorno (7)
£IMHFI :  File messaggio ritorno (10)
£IMHCM :  Ultimo Comando
£IMHRO :  N.ro Record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5MOAN :  DS valorizzata

# Prerequisiti
DC5MOAN         E DS                  EXTNAME(C5MOAN0F) INZ


# Esempio di chiamata
> C*                  Z-ADD     N_campi       £IMHNK
 C*                  MOVEL     'Funzione'    £IMHFU
 C*                  MOVEL     'Metodo'      £IMHME
 C*                  MOVEL     Ambiente      £IMHAM
 C*                  MOVEL     contesto      £IMHCO
 C*                  MOVEL     ID_Anal       £IMHID
 C*                  EXSR      £IMH
 C*                  IF        NOT(*IN35)
 C*  36              MOVEL     £IMHID        Campo_Id_Anal
 C*                  MOVEL     £IMHDE        Campo_descr
 C*                  ENDIF


# Note particolari
è preferibile eseguire un clear della DS C5MOAN prima di ogni richiamo

£IMHNK :  Numero di campi che si vuole utilizzare nella ricerca (es. se si accede alla vista logica con chiavi AZIE,DIVI,TREG  e si valorizza solo AIZE il programma esclude dalla chiave i campi BLANK e lavora con chiave parziale (nell'es. = AZIE).Se si voless usare una chiave formata da AZIE e da LIVE=*BLANKS allora si ponga £IMHNK=2 . Non valorizzare £IMHNK per lasciare al programma il compito di stabilire il numero di chiavi da usare £IMHNK viene inserito nell'ultimo char di £IMHME al richiamo dell'interfaccia
