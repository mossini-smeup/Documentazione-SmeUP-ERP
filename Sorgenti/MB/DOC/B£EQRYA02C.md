Di seguito un esempio di utilizzo in un programma RPG della /COPY £IQR.

>     H/COPY QILEGEN,£INIZH
     V*===============================================================
     V* MODIFICHE Ril.  T Au Descrizione
     V* gg/mm/aa  nn.mm i xx Breve descrizione
     V*===============================================================
     V* OBIETTIVO
     V*
      *===============================================================
      /COPY QILEGEN,£IQ2_PD1
      /COPY QILEGEN,£IQ3_PD1
      /COPY QILEGEN,£IQ2DS
      /COPY QILEGEN,£IQ3DS
      /COPY QILEGEN,£IQRDS
      /COPY QILEGEN,£TABB£1DS
      /COPY QILEGEN,£PDS
      *
     C                   EVAL      £IQROG='CNCLI'
     C                   CLEAR                   £IQR2I
     C                   CLEAR                   £IQR3I
      * imposto schema libero
     C                   EVAL      £IQRSC='**'
     C                   EVAL      £IQR2I(1)='I/01'
     C                   EVAL      £IQR2I(2)='I/03'
      * imposto filtro libero
     C                   EVAL      £IQRFL='**'
      * solo attivi U/G02
     C                   CLEAR                   £IQ3C
     C                   EVAL      £IQR3I(1)='U/G02'
     C                   EVAL      £IQ3CCD='U/G02'
     C                   EVAL      £IQ3COP='EQ'
     C                   EVAL      £IQ3CFU='OAV'
     C                   EVAL      £IQ3CPA='I/02,U/G02'
     C                   EVAL      £IQR3D(1)=£IQ3C
      * inizializzo
     C                   EVAL      £IQRFU='INZ'
     C                   EVAL      £IQRME=*BLANKS
     C                   EVAL      £IQRQR='*FIL'
     C                   EXSR      £IQR
      * valorizzo filtro
     C                   EVAL      £IQR3V(1)='1'
      * seleziono
     C                   EVAL      £IQRFU='SLC'
     C                   EXSR      £IQR
      * scandisco
1    C                   DO        *HIVAL
     C                   EVAL      £IQRFU='NXT'
     C                   EXSR      £IQR
2    C                   IF        £IQR35=*ON
     C                   LEAVE
2e   C                   ENDIF
      *
     C                   EVAL      $$CODI=£IQROK
     C                   EVAL      $$RAGS=P_£IQ2_EXT_VAL('I/01')
     C                   EVAL      $$INDI=P_£IQ2_EXT_VAL('I/03')
      *
1e   C                   ENDDO
      *
     C     G9MAIN        TAG
     C                   SETON                                        LR
      *---------------------------------------------------------------------
      /COPY QILEGEN,£INZSR
      *---------------------------------------------------------------------
    RD* Routine iniziale
      *---------------------------------------------------------------------
     C     £INIZI        BEGSR
      *
     C                   MOVEL     *BLANKS       $$CODI           15
     C                   MOVEL     *BLANKS       $$RAGS           35
     C                   MOVEL     *BLANKS       $$INDI           35
      *
     C                   ENDSR
      /COPY QILEGEN,£IQR
      /COPY QILEGEN,£IQ2_PC1
      /COPY QILEGEN,£IQ3_PC1

