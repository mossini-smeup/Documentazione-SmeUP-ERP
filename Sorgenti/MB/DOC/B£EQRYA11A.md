# Struttura delle Query

La struttura delle Query si appoggia alla /COPY £IQR.

Questa /COPY in sintesi permette di combinare insieme le dimensioni riportate a seguire al fine di ottenere una "matrice" di risultati : 
* **Una fonte** :  identificata dall'oggetto Q5, è l'oggetto che identifica una modalità di accesso alla scansione delle istanze dell'oggetto.
* **Una schema di colonne** :  identificata dall'oggetto Q2, è l'oggetto che permette di identificare le colonne della "matrice"

Le succitate dimensioni sono obbligatorie, mentre opzionamente vi si possono aggiungere
* **Un filtro** :  identificato dall'oggetto Q3, è l'oggetto che permette di applicare dei filtri specifici nella scansione delle istanze della classe
* **Un ordinamento** :  identificato dall'oggetto Q4, è l'oggetto che permette di applicare un particolare ordine alla scansione delle istanze dell'oggetto.

Una particolare combinazione di queste dimensioni è definita query ed è identicata dall'oggetto Q1.

 :  : DEC T(MB) P(QILEGEN) K(£IQR)
 :  : DEC T(OG)  K(Q1)
 :  : DEC T(OG)  K(Q2)
 :  : DEC T(OG)  K(Q3)
 :  : DEC T(OG)  K(Q4)
 :  : DEC T(OG)  K(Q5)

# Origine delle istanze degli oggetti delle query.

Le istanze degli oggetti Qx sopracitate vengono forniti da una serie di pgm aventi la seguente B£IQR_xx (ognuno dei quali rappresenta una particolare fonte). Ognuno di questi programmi si occupa di fornire istanze di uno o più oggetti Qx rispondendo principalmente alle funzioni della £IQR : 
* LIS.QRY :  elenco delle query. Cioè l'insieme delle istanza Q1 che il pgm è in grado di fornire.
* LIS.SCH :  elenco degli schemi. Cioè l'insieme delle istanza Q2 che il pgm è in grado di fornire.
* LIS.FLT :  elenco degli schemi. Cioè l'insieme delle istanza Q3 che il pgm è in grado di fornire.
* LIS.ORD :  elenco degli ordinamenti. Cioè l'insieme delle istanza Q4 che il pgm è in grado di fornire.

Ogni programma ha delle logiche molto specifiche di elaborazione e ognuno va analizzato nel dettaglio. Si portano qui di seguito a seguire i pgm più utilizzati : 
* B£IQR_00 :  fornisce le istanze di qualsiasi oggetto Qx costruito a partire dagli script SCP_QRY
* B£IQR_01 :  fornisce le istanze delle query *KEY e *DEC attraverso le corrispondenti interfacce
* B£IQR_02 :  risolve le query costruite dagli script qual'ora queste siano riconducibili ad accessi SQL
* B£IQR_07 :  risolve le query costruite a partire da definizione di liste (Classe LI)
* B£IQR_08 :  risolve le query costruite su oggetti del sistema operativo (Classe OJ)
* B£IQR_09 :  risolve le query costruite su tabelle (Classe TA)
* B£IQR_10 :  risolve le query costruite su membri sorgenti (Classe MB)
* B£IQR_17 :  risolve gli schemi definiti attraverso i membri SCP_NAV
* B£IQR_18 :  risolve gli schemi definiti attraverso i pgm B£IQ2_xx
* B£IQR_20 :  risolve le query di ricerca da Surf di Modulo

# L'utilizzo delle funzionalità delle funzioni delle query

Le funzionalità delle funzioni di query sono state utilizzate in modo combinato nelle struttura delle ricerche, ma possono essere parzialmente o totalmente impiegate per funzioni proprie. In particolare si rimanda ai documenti in cui viene descritto : 
- [Aggiungere&-x2f;Modificare gli Schemi della Finestra](Sorgenti/MB/DOC/B£EQRY_A03)
- [Utilizzare Uno Schema in un Servizio Generico](Sorgenti/MB/DOC/B£EQRY_A04)
- [Aggiungere Nuove Query di Ricerca](Sorgenti/MB/DOC/B£EQRY_A05)
- [Utilizzare Una Query in Scheda](Sorgenti/MB/DOC/B£EQRY_A06)
- [Utilizzare il Filtro di Job in un Servizio](Sorgenti/MB/DOC/B£EQRY_A07)

# Utilizzo di una query in un programma

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
























