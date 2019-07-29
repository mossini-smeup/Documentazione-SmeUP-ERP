# Obiettivo
Interfacciare il programma in esecuzione con l'anagrafico conti contabili. Eseguire la ricerca alfabetica relativa se richiesto
# Funzioni e metodi
# Input
£ICOFU :  Funzione
£ICOME :  Metodo
£ICOAM :  Ambiente
£ICOCO :  Contesto
£ICOCD :  Codice conto contabile (se funzione = *Blanks)
£ICOLC :  Livello chiamata
£ICODS :  DS valorizzata

# Output
£ICOCD :  Conto contabile(se eseguita ricerca)
£ICODE :  Descrizione conto contabile
£ICOMS :  Codice messaggio ritorno
£ICOFI :  File   messaggio ritorno
£ICOCM :  Ultimo Comando
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
C5B$DS :  DS valorizzata
£ICODS :  DS valorizzata

# Prerequisiti
D/COPY QILEGEN,£TABC5BDS
D/COPY QILEGEN,£ICODS

# Esempio di chiamata

## Chiamata con singola lettura
> C*                  CLEAR                   C5B$DS
 C*                  CLEAR                   £ICODS
 C*                  MOVEL     *BLANKS       £ICOFU
 C*                  MOVEL     Con_cont      £ICOCD
 C*                  EXSR      £ICO
 C*                  MOVEL     £ICODE        Campo_descrizione
 C*                  MOVEL     £ICOCD        Campo_con_cont
 C*                  MOVEL     C5B$DS        Tutti_campi
 C*                  MOVEL     £ICODS        Campi_output


## Chiamata con scansione
>     C*                  CLEAR                   C5B$DS
     C*                  CLEAR                   £ICODS
     C*                  EVAL      £ICOFU='SL'
     C*                  EVAL      £ICOME='0L'
     C*                  EVAL      £ICOCD=Campo_con_cont
     C*                  EXSR      £ICO
     C*
     C*                  DO        *HIVAL
     C*
     C*                  EVAL      £ICOFU='RD'
     C*                  EVAL      £ICOME='0L'
     C*                  EVAL      £ICOCD=Campo_con_cont
     C*                  EXSR      £ICO
     C*                  IF        £ICO35=*ON
     C*                  LEAVE
     C*                  ENDIF
     C*
     C*                  ....
     C*                  ENDDO


# Oggetti collegati


# Note particolari
È preferibile eseguire un clear delle DS  C5B$DS e £ICODS prima di ogni richiamo
