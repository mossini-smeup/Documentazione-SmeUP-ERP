# £G76 QUERY PER STRUTTURE DATI

## OBIETTIVO
 Gestire query per strutture dati (Oggetto RE) orientando le funzioni agli oggetti
 Il campo di input non e' posizionale, ma parametrico; vengono indicati i parametri
  con la sintassi NomeParametro(Valore)

 Al momento vengono supportate due inizializzazioni : 
  - Inizializzazione per file
 :  : INI SINTASSI DELLA CHIAMATA
      * Inizializzo per file
     C                   EVAL      £G76FU='INZ'
     C                   EVAL      £G76ME='F-'
     C                   EXSR      £G76
 :  : FIN
  - Inizializzazione per oggetto
 :  : INI SINTASSI DELLA CHIAMATA
      * Inizializzo per oggetto
     C                   EVAL      £G76FU='INZ'
     C                   EVAL      £G76ME='O-'
     C                   EXSR      £G76
 :  : FIN

### Inizializzazione per file
 Con questa inizializzazione si lavora sui campi del file indicato
 :  : INI SINTASSI DELLA CHIAMATA
      * Set del file
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='REC'
     C                   EVAL      £G76IN='REC(File)'
     C                   EXSR      £G76
 :  : FIN

### Inizializzazione per oggetto
 Con questa inizializzazione si lavora per OAV dell'oggetto indicato
 Il mapping fra OAV e campo del file viene specificato nel file
  di script SCP_G76/NomeOggetto
 :  : INI SINTASSI DELLA CHIAMATA
      * Set dell'oggetto
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='REC'
     C                   EVAL      £G76IN='REC(Oggetto)'
     C                   EXSR      £G76
 :  : FIN

### Set dei campi richiesti
 E' possibile selezionare campi del record, eventualmente indicando
  il titolo e l'oggetto della colonna
 L'impostazione e' multipla
 :  : INI SINTASSI DELLA CHIAMATA
      * Set del campo/attributo
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='FLD'
     C                   EVAL      £G76IN='FLD(NomeCampo/Attributo)
     C                                     OGG(OggettoDellaColonna)
     C                                     INT(IntestazioneColonna)
     C                                     HDD(Hidden)'
     C                   EXSR      £G76
 :  : FIN

### Set del filtro
 E' possibile selezionare campi del record in base a dei filtri
  sia statici(campi del file) che dinamici(OAV)
 L'impostazione e' multipla
 :  : INI SINTASSI DELLA CHIAMATA
      * Set del filtro
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='FLT'
     C                   EVAL      £G76IN='FLD(NomeCampo/Attributo)
     C                                     OPE(V2OPC03)
     C                                     VAL(Valore)'
     C                   EXSR      £G76
 :  : FIN

### Set dell'ordinamento
 E' possibile ordinare il recordset in base a campi del record
 L'impostazione e' multipla
 :  : INI SINTASSI DELLA CHIAMATA
      * Set dell'ordinamento
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='ORD'
     C                   EVAL      £G76IN='FLD(NomeCampo/Attributo)
     C                                     ORD(A/D)'
     C                   EXSR      £G76
 :  : FIN

### Set del raggruppamento
 E' possibile raggruppare i campi del recordset in base a dei campi selezionati
  nel SET/FLD
 L'impostazione e' multipla
 :  : INI SINTASSI DELLA CHIAMATA
      * Set del group by
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='GRP'
     C                   EVAL      £G76IN='FLD(NomeCampo/Attributo)
     C                   EXSR      £G76
 :  : FIN

### Set delle funzioni
 Alla funzione di SET per i metodi (FLD,FLT,ORD,GRP) e' possibile specificare
  una delle funzioni sottoelencate aggiungendo i parametri
  FUN(xxx) e PAR(V1,V2,Vn) al campo di input £G76IN

  Funzione  Descrizione   Parametri
  CNC       Concat        Vn= Campi da concatenare
  SUM       Somma         V1= Campo da sommare
  CNT       Count         V1= Campo da conteggiare
  MAX       Massimo       V1= Campo da cui selezionare il valore massimo
  MIN       Minimo        V1= Campo da cui selezionare il valore minimo
  AVG       Media         V1= Campo di cui calcolare la media
  FOR       Formula       V1= Sintassi della formula
  RRN       Nr. record    V1= Nome file da cui selezionare il nr. relativo record
  SST       Substring     V1= Nome campo, V2=Posizione, V3=Lunghezza
  DEC       £DEC          V1= Campo, V2=Oggetto(Opzionale, se assente da V1)
  OAV       £OAV          V1= Campo, V2=Attributo, V3=Oggetto(Opzionale, se assente da V1)
 :  : INI SINTASSI DELLA CHIAMATA
      * Set della funzione
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='FLD'
     C                   EVAL      £G76ME='FLT'
     C                   EVAL      £G76ME='ORD'
     C                   EVAL      £G76ME='GRP'
     C                   EVAL      £G76IN=%trim(£G76IN)
     C                                    FUN(xxx) PAR(xxxxx)
     C                   EXSR      £G76
 :  : FIN

### Caricamento da file di script
 E' possibile caricare tutti i comandi della /COPY attraverso
 un file di script. Degli esempi sono contenuti nel file SCP_G76
 :  : INI SINTASSI DELLA CHIAMATA
      * Caricamento dello script
     C                   EVAL      £G76FU='CAR'
     C                   EVAL      £G76ME='SCP'
     C                   EVAL      £G76IN='LIB(*LIBL)
     C                                     FIL(NomeFile)
     C                                     MBR(Membro)'
     C                   EXSR      £G76
 :  : FIN

### Selezione dei record
 Al termine delle procedure di set, occorre eseguire la selezione dei records
 La selezione puo' essere di 2 tipi : 
  - Tutti i record
 :  : INI SINTASSI DELLA CHIAMATA
      * Selezione di tutti i campi
     C                   EVAL      £G76FU='SLC'
     C                   EVAL      £G76ME=*BLANKS
     C                   EXSR      £G76
 :  : FIN
  - Solo un elemento per campo (distinct)
 :  : INI SINTASSI DELLA CHIAMATA
      * Distinct dei campi
     C                   EVAL      £G76FU='SLC'
     C                   EVAL      £G76ME='DST'
     C                   EXSR      £G76
 :  : FIN

### Scansione dei record
 Al termine delle procedure della selezione si puo' scorrere il resultset
 :  : INI SINTASSI DELLA CHIAMATA
      * Scorrimento resultset
     C                   EVAL      £G76FU='NXT'
     C                   EVAL      £G76ME=*BLANKS
     C                   EXSR      £G76
 :  : FIN

### Ripresa campi
 Una volta posizionati sul record selezionato occorre reprire il valore
 dei campi selezionati
 :  : INI SINTASSI DELLA CHIAMATA
      * Ripresa valore campo
     C                   EVAL      £G76FU='GET'
     C                   EVAL      £G76ME='FLD'
     C                   EVAL      £G76IN=NomeCampo
     C                   EXSR      £G76
     C                   EVAL      campo=£G76OU
 :  : FIN

### Impostazione di variabili
 E' possibile settare delle variabili che verranno utilizzate come
 valori per il set del filtro
 :  : INI SINTASSI DELLA CHIAMATA
      * Set di variabile
     C                   EVAL      £G76FU='SET'
     C                   EVAL      £G76ME='VAR'
     C                   EVAL      £G76IN='VAR(Nome)
     C                                     VAL(Valore)
     C                   EXSR      £G76
 :  : FIN
 E' possibile, a scopo informativo, scandire le varibili contenute
  nella selezione
 :  : INI SINTASSI DELLA CHIAMATA
      * Scansione variabili
     C                   EVAL      £G76FU='SCV'
     C                   EVAL      £G76ME='POS'
     C                   DO
     C                   EXSR      £G76
     C                   EVAL      £G76V=£G76OU
     C                   EVAL      £G76ME='LET'
     C                   ENDDO
 :  : FIN

### Scansione struttura resultset
 E' possibile scandire la struttura del resultset selezionato,
  questa funzionalita' viene utilizzata dal TSTG76 per la
  funzione VIS/REC e VIS/LST
      * Scansione struttura
     C                   EVAL      £G76FU='SCS'
     C                   EVAL      £G76ME='POS'
     C                   DO
     C                   EXSR      £G76
     C                   EVAL      £G76G=£G76OU
     C                   EVAL      £G76ME='LET'
     C                   ENDDO
 :  : FIN
