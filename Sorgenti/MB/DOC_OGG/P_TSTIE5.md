# Obiettivo
Interfacciare il programma in esecuzione con le testate di registraz.contabili delle diverse applicazioni previste nella tabella di personalizzazione applicazioni B£1.
Eseguire la ricerca alfabetica relativa se richiesto

# Input
£IE5FU :  Funzione
£IE5ME :  Metodo
£IE5AM :  Ambiente
£IE5CO :  Contesto
£IE5PR :  Progressivo registrazione
£IE5NR :  Numero riga
£IE5RI :  N.ro Record di input

# Output
£IE5PR :  Progress.registr.scelto (se eseguita ricerca)
£IE5NR :  Riga registr.scelta (se eseguita ricerca)
£IE5DE :  Descrizione riga registrazione
£IE5MS :  Codice messaggio ritorno (7)
£IE5FI :  File messaggio ritorno (10)
£IE5CM :  Ultimo Comando
£IE5RO :  N.ro Record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5RREG :  DA Valorizzata

# Prerequisiti
DC5RREG E DS  EXTNAME(C5RREG0F) INZ

# Esempio di chiamata
>C*                  Z-ADD     N_campi       £IE5NK
C*                  MOVEL     'Funzione'    £IE5FU
C*                  MOVEL     'Metodo'      £IE5ME
C*                  MOVEL     Ambiente      £IE5AM
C*                  MOVEL     contesto      £IE5CO
C*                  MOVEL     Prog_Reg      £IE5PR
C*                  MOVEL     Riga          £IE5NR
C*                  EXSR      £IE5
C*                  IF        NOT(*IN35)
C*                  MOVEL     £IE5PR        Campo_Prog_Reg
C*                  MOVEL     £IE5NR        Campo_Riga
C*                  MOVEL     £IE5DE        Campo_descr
C*                  ENDIF


# Note particolari
è preferibile eseguire un clear della DS C5RREG prima di ogni richiamo.
Parametro aggiuntivo :  £IE5NK :  Numero di campi che si vuole utilizzare nella ricerca (es. se si accede alla vista logica con chiavi AZIE,DIVI,TREG  e si valorizza solo AIZE il programma esclude dalla chiave i campi BLANK e lavora con chiave parziale (nell'es. = AZIE).Se si volesse usare una chiave formata da AZIE e da LIVE=*BLANKS allora si ponga £IE5NK=2). Non valorizzare £IE5NK per lasciare al programma il compito di stabilire il numero di chiavi da usare £IE5NK viene inserito nell'ultimo char di £IE5ME al richiamo dell'interfaccia
