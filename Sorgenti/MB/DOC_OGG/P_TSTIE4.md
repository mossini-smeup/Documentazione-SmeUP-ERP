# Obiettivo
 Interfacciare il programma in esecuzione con le testate di  registraz.contabili delle diverse applicazioni previste nella tabella di personalizzazione applicazioni B£1.
 Eseguire la ricerca alfabetica relativa se richiesto

# Input
£IE4FU :  Funzione
£IE4ME :  Metodo
£IE4AM :  Ambiente
£IE4CO :  Contesto
£IE4PR :  Progressivo registrazione
£IE4RI :  N.ro Record di input
£IE4LC :  Livello di chiamata

# Output
£IE4PR :  Progress.registr.scelto (se eseguita ricerca)
£IE4DE :  Descrizione testata registrazione
£IE4MS :  Codice messaggio ritorno (7)
£IE4FI :  File   messaggio ritorno (10)
£IE4CM :  Ultimo Comando
£IE4RO :  N.ro record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5TREG :  DS valorizzata

# Prerequisiti
DC5TREG         E DS                  EXTNAME(C5TREG0F) INZ

# Esempio di chiamata
>                  Z-ADD     N_campi       £IE4NK
                  MOVEL     'Funzione'    £IE4FU
                  MOVEL     'Metodo'      £IE4ME
                  MOVEL     Ambiente      £IE4AM
                  MOVEL     Contesto      £IE4CO
                  MOVEL     Prog.Reg      £IE4PR
                  EXSR      £IE4
                  IF        NOT(*IN35)
                  MOVEL     £IE4PR        Campo_Prog
                  MOVEL     £IE4DE        Campo_Descr


# Note particolari
è preferibile eseguire un clear della DS C5TREG prima di ogni richiamo.
Parametro aggiuntivo :  £IE4NK :  Numero di campi che si vuole utilizzare nella ricerca (es. se si accede alla vista logica con chiavi AZIE,DIVI,TREGe si valorizza solo AIZE il programma esclude dalla chiave i campi BLANK e lavora con chiave parziale (nell'es. = AZIE).Se si volesse usare una chiave formata da AZIE e da LIVE=*BLANKS allora si ponga £IE4NK=2) Non valorizzare £IE4NK per lasciare al programma il compito di stabilire il numero di chiavi da usare £IE4NK viene inserito nell'ultimo char di £IE4ME al richiamo dell'interfaccia
