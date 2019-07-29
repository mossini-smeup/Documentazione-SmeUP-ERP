## Passo 1 :  Impostazione Tabelle
Per il funzionamento del modulo bisogna impostare le seguenti tabelle : 

_3_Tabella OD1 :  Configurazione Documentale
Definisce i parametri generali relativi al modulo documentale
 :  : DEC T(TA) P(OD1) K(*)

_3_Tabella ODB :  Nome Documentale
Definisce i parametri generali relativi al documentale COMPED
 :  : DEC T(ST) K(ODB)

_3_Tabella ODC :  Tipo Documento
Definisce i parametri generali relativi al tipo documento nel documentale
 :  : DEC T(ST) K(ODC)

_3_Tabella ODD :  Volume Documentale
Definisce i volumi di archiviazione/conservazione contenuti nel documentale
 :  : DEC T(ST) K(ODD)

Devono esistere i seguenti elementi della Griglia di controllo 3 oggetti

_3_ Elemento £D1 della Tabella B£G
E' utilizzato per salvare nei file dei parametri i riferimenti di archiviazione e conservazione della fattura nel documentale.
 :  : DEC T(TA) P(B£G) K(£D1)

_3_ Elemento £D2 della Tabella B£G
E' utilizzato per memorizzare nei parametri  l'ultimo documento conservato nel documentale
 :  : DEC T(TA) P(B£G) K(£D2)



## Passo 2 :  Impostazione parametri
Devono essere presenti le seguenti categorie parametri : 

 :  : INI Gestione parametri Categoria £D1
 :  : CMD CALL C£CR01G PARM('£D1')
 :  : FIN
###
La categora parametri £D1 contiene le informazioni relative a idoj di archiviazione e conservazione legati alla fattura archiviata e conservata. Gli idoj costituiscono il legame tra la fattura in Smeup
e la fattura nel documentale.

Idoj di archiviazione
 :  : DEC T(TA) P(B£N£D) K(£01)

Idoj di conservazione
 :  : DEC T(TA) P(B£N£D) K(£02)


 :  : INI Gestione parametri Categoria £D2
 :  : CMD CALL C£CR01G PARM('£D2')
 :  : FIN
###
La categoria parametri £D2 contiene le informazioni relative all'ultima fattura conservata. Viene utilizzato per controllare che la numerazione delle fatture sia consecutiva tra una conservazione e un'altra.

Ultimo documento conservato
 :  : DEC T(TA) P(B£N£D) K(£11)



## OAV

Devono esistere i seguenti OAV

Oggetto FT attributi
J/G12  Volume documentale
J/G13  Idoj documentale
J/G14 Stato conservazione
J/G15 Nome file archiviazione

Oggetto DO attributi
J/G00 Parametro REG.AN.NAZ
J/G02 Oggetto fattura REG.AN.AZ
J/O01 Nome file fattura

## Utility per l'archiviazione dei documenti
### £ODA
Gestisce le funzioni di servizio con il documentale (archiviazione documento, pulizia volumi, controllo conservazione documento ecc)

### V5OD01E
Gestisce la chiamata all'archiviazione del documento. E' un programma funizzato che gestisce sia l'oggetto DO che l'oggetto FT. Il programma controlla che il documento non sia già conservato; in caso sia già conservato il documento non viene archiviato e viene emesso un messaggio nel log di stampa (se attivato).
Con oggetto DO il funizzato può essere chiamato nel programma di stampa fattura (la fattura non è ancora contabilizzata). Segue un esempio di richiamo da mettere nel programma di stampa fattura.


Nella routine TL1

C*----------------------------------------------------------------
D* Archivia
C*----------------------------------------------------------------
C     ARCHIVI            BEGSR
 *
C                              IF        U$ARCH<>*BLANKS
C                              EVAL      £FUNPG='V5OD01E'
C                              EVAL      £FUNFU='ARC'
C                              EVAL      £FUNME='FA '
C                              EVAL      £FUNT1='DO'
C                              EVAL      £FUNP1=T§TDOC
C                              EVAL      £FUNK1=T§NDOC
C                              EXSR      £FUN02
C                             ENDIF
 *
C                             ENDSR

Con oggetto FT puoi essere messo direttamente in un passo di flusso post contabilizzazione.

### V5OD01X
Deviatore che gestisce oggetti DO, E4, E5 e apre la scheda della relativa fattura. Essendo funizzato può essere utilizzato nelle interrogazioni di contabilità (partitario, scadenzario mastrino) mettendo il richiamo  nella relativa B£J.
