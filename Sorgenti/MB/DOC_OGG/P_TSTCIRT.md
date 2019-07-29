# Obiettivo
 Scansione sequenziale dei cicli di lavoro per determinare l'andamento nel tempo del consumo risorse (principali e  secondarie)

# Funzioni e metodi

FUNZIONI : 
'SVI'    :  sviluppo nel tempo (viene considerata la schiera quantità con le schiere date)
'DAT'  :  valori alla data (viene considerato il primo valore della schiera quantità con la prima data della schiera date iniziali) :           questa funzione ha senso se nel metodo si imposta che si desiderano risorse secondarie (una o tutte), perchè          altrimenti basta la scansione normale.

METODI : 
'PRI'  :  risorsa principale
'SEC'  :  risorse secondarie
'ALL'  :  risorsa principale e risorse secondarie
'SING' :  vengono ritornati i valori delle risorse secondarie relative ad una singola operazione e ad un elemento di carico o costo di cui si            specifica l'andamento nel tempo nella schiera quantità di input (se la funzione è 'DAT' è significativo solo il primo elemento).
          In questo caso si definisce la chiave della risorsa principale con i seguenti campi : 
          - £CIRIT   Tipo ciclo
          - £CIRIA   Codice assieme
          - £CIRIZ   Ciclo selez.
          - £CIRIQ   Sequenza ciclo
          - £CIRIV   Ciclo valid.iniziale

# Input
Dati di input della £CIR per esplosione di produzione ad eccezione della data di validità e della quantità, ed inoltre i seguenti campi : 
£CRI     Schiera quantità di input
£CRB     Schiera date inizio periodo
£CRF     Schiera date fine periodo
£CIRNC - N.ro del componente di costo o di carico da esplodere nel seguente formato COSxx / CARxx (xx = 01 - 10) :                 è significativo solo se il metodo non è 'SING'
£CIRBJ - Se inmpostata è la B£J che individua le risorse secondarie da scandire (è il metodo della £BRR con funzione POS),                se lasciato a blanks, si imposta *RPS. NB :  questo campo, come del resto i rimanenti campi di input, viene ripulito dopo ogni chiamata.

# Output
          Dati di ritorno della £CIR
          *IN35  :  ON per fine scansione
 £CRZ     Schiera quantità calcolata distribiuta nel tempo
 £CIRMS  'PRI'  :  se risorsa principale
   ,,    'NEW'  :  all'inizio di ogni nuovo tipo di risorsa sec
   ,,    'SEC'  :  per le restanti risorse secondarie
 £CIRT1   Tipo della risorsa principale o secondaria
 £CIRP1   Parametro     ,,          ,,
 £CIRK1   Codice        ,,          ,,


# Prerequisiti
D/COPY QILEGEN,£CIRTE

# Esempio di chiamata

     C                   CLEAR                   £CIRSP
     C                   DO        *HIVAL
     C
     C                   EVAL      £CIRFU=Funzione
     C                   EVAL      £CIRME=Metodo
     C                   EVAL      £CIRIT=Tipo ciclo
     C                   EVAL      £CIRIA=Codice
     C                   EVAL      £CIRCG=Configurazione
     C                   EVAL      £CIRUP=Um di Present.
     C                   EVAL      £CIRIZ=Cicl di Selezione
     C                   EVAL      £CIRIQ=Sequenz Ciclo
     C                   EVAL      £CIRIS=Stato
     C                   EVAL      £CIRIO=Tip Operazione
     C                   EVAL      £CIRI1=Par.condiz.1
     C                   EVAL      £CIRNC=N.Comp.costo/carico
     C                   EXSR      £CIRT
     C                   IF        £CIR35=*ON
     C                   LEAVE
     C                   ENDIF
     C
     C                   EVAL      Fonte ris.    =£CIRF1
     C                   EVAL      Tipo ris.     =£CIRT1
     C                   EVAL      Parametro ris.=£CIRP1
     C                   EXSR      Codice ris.   =£CIRK1
     C                                           =
     C                   EVAL      Ciclo Selez.  =£CIRCS
     C                   EVAL      Sequenza      =£CIRSE
     C                   EVAL      Risorsa       =£CIRRI
     C                   ENDDO

# Note particolari

