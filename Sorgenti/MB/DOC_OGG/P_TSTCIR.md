# Obiettivo
Interrogazione CICLI di LAVORO prevista nella tabella di personalizzazione applicazioni B£1

# Input/Output
   Se il parametro FUNZIONE : 
   1) EC (Esplosione ciclo) chiama il pgm B£ICIR_xx che esegue la
         scansione normale.
   1) IC (Implosione ciclo) chiama il pgm B£ICIR_xx che esegue la
         esplosione
   3) CT (Tempi ciclo) chiama il pgm B£ICIT che gestisce la
         scansione schedulata.
   4) GD (Interrog. dettaglio operazione) chiama il pgm B£ICIR_xx
      che ritorna/visualizza i campi di BRRICI0F
   5) CD (Esplosione ciclo del documento)
   5) CC (Costruzione ciclo del documento)


Input : 
£CIRPG   :  se non blanks lancia il programma con questo suffisso :  serve nel caso in cui ci siano due scansioni di ciclo attive contemporaneamente nella stessa applicazione (lanciate da programmi diversi).

Output :  *IN35  :  se On = fine scansione

# Prerequisiti
     /COPY QILEGEN,£BRTE
     /COPY QILEGEN,£CIRE

# Esempio di chiamata

*scansione cicli di un dato articolo

     C                   CLEAR                   £CIRSP        (START)
     C                   DO        *HIVAL
     C
     C                   EVAL      £CIRFU='EC'
     C                   EVAL      £CIRME='1'
     C                   EVAL      £CIRIA=ARTICOLO
     C                   EVAL      £CIRCG=CONFIGURAZIONE
     C                   EVAL      £CIRQT=QUANTITà
     C                   EXSR      £CIR
     C                   IF        £CIR35=*ON                   INDICATORE ERRORE
     C                   LEAVE
     C                   ENDIF

     C                   EVAL      N.Record      =£CIRNR
     C                   EVAL      Tipo Ciclo    =£CIRTC
     C                   EVAL      Codice        =£CIRCO
     C                   EVAL      Ciclo Selez.  =£CIRCS
     C                   EVAL      Sequenza Ciclo=£CIRSE
     C                   EVAL      Risorsa       =£CIRRI
     C                   EVAL      Stato         =£CIRST
     C                   EVAL      Tipo Operaz.  =£CIRTO
     C                   EVAL      Ciclo Iniziale=£CIRCI
     C                   EVAL      Ciclo Finale  =£CIRCF
     C                   EVAL      Descr. Ciclo  =£CIRDE
     C                   EVAL      Gruppo Altern.=£CIRGA
     C                   EVAL      Codice Colleg.=£CIRAC
     C                   EVAL      Ciclo  Colleg.=£CIRCC
     C                   EVAL      Seq.Cic.Coll. =£CIRSC
     C                   EVAL      Criterio Sel. =£CIRSZ
     C                   EVAL      Par. Selez. 1 =£CIRS1
     C                   EVAL      Par. Selez. 2 =£CIRS2
     C                   EVAL      Unità Tempo   =£CIRUT
     C                   ENDDO

# Note particolari
