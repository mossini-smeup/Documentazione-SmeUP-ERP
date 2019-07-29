# Obiettivo
Lettura normalizzata sorgente.
Per lettura normalizzata si intende dire che si tiene conto delle cosiddette "continuation line" ovvero le specifiche che pur andando a capo nel codice RPG possono essere normalizzate in una stringa unica.

# Input
£MUSFU :  Funzione
£MUSME :  Metodo
£MUSLI :  Libreria
£MUSFI :  File
£MUSMM :  Membro
£MUSLC :  Livello chiamat G75
£MUSIN :  Indicatore generico
£MUSCA :  Continuation line

* **Funzione 'LET' - Lettura sorgente**
** __Metodo 'SETLL' - Lettura prima riga__;
** __Metodo 'READ'  - Lettura avanti__;
** __Metodo 'READP' - Lettura indietro__;

# Output
£MUS35 :  On=Errore
£MUSD2 :  Riga sorgente normalizzata

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£MUSDS
Possono essere usate anche le procedure
£MUS_PD1
£MUS_PC1

# Esempio di chiamata
     C                   EVAL      £MUSFU=Funzione
     C                   EVAL      £MUSME=Metodo
     C                   CLEAR                   £MUSD1
     C                   CLEAR                   £MUSD2
     C                   EVAL      £MUSLI=Libreria sorgente
     C                   EVAL      £MUSFI=File sorgente
     C                   EVAL      £MUSMM=Membro sorgente
     C                   EVAL      £MUSLC=Livello chiamata
     C                   EVAL      £MUSIN=Indicatore generico (*OFF)
     C                   EVAL      £MUSCA=Continuation line *ON/*OFF
     C                   EXSR      £MUS

# Note particolari

