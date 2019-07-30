 :  : HEA RESP(FD) STAT(10)
# OBIETTIVO
Fornire i dati relativi al piano ammortamento per categoria o per azienda.
# FUNZIONI/METODI
##    AMMORTAMENTI
### AMM.CAT
Costruisce una matrice che riporta, per esercizio, il residuo da ammortizzare per l'azienda passata in Oggetto1 e per
la categoria passata in Oggetto2 a livello di totali.
Se la categoria non viene passata, il calcolo viene effettuato cliccando su tutte le categorie presenti per l'azienda passata.
Contestualmente la funzione può essere richiamata utilizzando il componente "Grafico" per visualizzare lo stato dei residui negli anni tramite barre verticali.
LA
### AMM.CAD
Costruisce una matrice che mostra lo spaccato dell'anno scelto :  vengono elencati i cespiti in causa a quella data e per quella categoria.

## ANAGRAFICA

### ANA.AZI
Ritorna una matrice con l'elenco dei cespiti relativi all'azienda passata in Oggetto 1.

### ANA.MAT
Ritorna una matrice con l'elenco dei cespiti filtrati per Lista, Cespite di Riferimento, per Azienda o per Azienda/Categoria. L'elemento con cui filtrare viene passato in Oggetto 1.

### ANA.CER
Ritorna un albero in cui vengono riportati tutti i cespiti di riferimento. In sostanza viene scansionato il file con la vista logica A5CESP2L e vengono trattenuti solo i cespiti con campo TACERI compilato.
Per la chiamata non è necessario passare alcun Oggetto.

### ANA.AZF
Ritorna un albero contente l'azienda per la quale si sta richiedendo l'analisi dei cespiti.
Il nodo viene scritto in base a quanto memorizzato tramite la _7_£MDV nelle inizializzazioni.
Per la chiamata non è necessario passare alcun Oggetto.

### ANA.CLA
Ritorna un albero che riporta tutte le classificazioni inidcate nella **TA A5A** (Categoria fiscale cespite) :  in sostanza vengono letti i campi >T$A5AC e >T$A5AF (Griglia classificazione) che sono elementi della **TA B£G** (Griglia controllo 3 Oggetti).
Per la chiamata non è necessario passare alcun Oggetto.
## IMPOSTAZIONI

### IMP.BAS
Questa chiamata costruisce una matrice contenente le impostazioni generali di base per tutto il modulo A5BASE.
In pratica vengono letti i valori settati nella _7_£MDV.
Per la chiamata non è necessario passare alcun Oggetto.

### IMP.PAM
Questa chiamata costruisce una matrice contenente le impostazioni relative alla sottoscheda "Piani Ammortamento" per la scheda _3_A5BASE_BAS.
In realtà utilizzo la stessa struttura della precedente fu/me, ma mostro solo alcune colonne...(da rivedere)!!!
Per la chiamata non è necessario passare alcun Oggetto.
### IMP.ATT
Questa chiamta restituisce l'albero delle attività possibili all'interno del modulo _3_A5BASE.
Per la chiamata non è necessario passare alcun Oggetto.

### IMP.SCH
Questa chiamata costruisce una matrice contenente le impostazioni generali di base per tutto il modulo A5BASE..(.da rivedere!!!)

## CAUSALI

### CAU.PRO
Prospetto azioni causali.
Questa chiamata costruisce una matrice contenente il prospetto azioni causali cespiti ricalcando quanto fatto dal programma A5NOWE0. Tale programma viene lanciato dal servizio stesso tramite chiamata con una variabile apposita valorizzata (U$AMBI='LO') e che restituisce la matrice necessaria al servizio.


##    TOTALIZZATORI

 :  : PRO.SER Cod="STA.SEM.1" Tit="STATO CESPITE. Semaforo" Fun="F(EXB;A5SER_02;STA.SEM) P()"

 :  : PRO.SER Cod="STA.LAB.2" Tit="STATO CESPITE. Label" Fun="F(EXB;A5SER_02;STA.LAB)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="STA.GAU.3" Tit="STATO CESPITE. Cruscotto" Fun="F(EXB;A5SER_02;STA.GAU)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="SCH.LIN.4" Tit="SCHEDA CESPITE. matrice/grafico della/delle linea/linee" Fun="F(EXB;A5SER_02;SCH.LIN) 1(CE;;-(O;;CE;Cespite)) 2(TA;A5C;-(F;;TAA5C;Linea)) P()"

 :  : PRO.SER Cod="SCH.LIN.5" Tit="SCHEDA CESPITE. matrice/grafico della/delle linea/linee" Fun="F(EXA;A5SER_02;SCH.LIN)" Ref="SCH.LIN.4"

 :  : PRO.SER Cod="SCH.GRA.6" Tit="SCHEDA CESPITE. grafico comparativo delle linee" Fun="F(EXB;A5SER_02;SCH.GRA) 1(CE;;-(O;;CE;Cespite)) P()"

 :  : PRO.SER Cod="SCH.GRA.7" Tit="SCHEDA CESPITE. grafico comparativo delle linee" Fun="F(EXA;A5SER_02;SCH.GRA)" Ref="SCH.GRA.6"

 :  : PRO.SER Cod="CAU.PRO.8" Tit=". Prospetto azioni causali" Fun="F(EXB;A5SER_02;CAU.PRO) P()"

