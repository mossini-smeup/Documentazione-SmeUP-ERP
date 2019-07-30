# OBIETTIVO
Fornire informazioni relative alla Disponibilità Finanziaria.

# FUNZIONI/METODI

## GRUPPI FONTI
Con la Funzione **GFO** il servizio ritorna gli elementi delle tabelle  **C6E** (fonti presenti) e **C6F**(fonti future) contenuti nelle memorizzazioni multiple create e a disposizione dell'utente.

### GFO.FPR
Costruisce un'albero che riporta gli elementi della tabella **C6E FONTI ESISTENTI DISP.FINANZ.** contenuti nella memorizzazione passata in K1 dell' _3_Oggetto 1.

### GFO.FFU
Costruisce un'albero che riporta gli elementi della tabella **C6F FONTI FUTURE DISP.FINANZ.** contenuti nella memorizzazione passata in K1 dell' _3_Oggetto 1.

## AGGIUNGI/TOGLI ELEMENTI
Con le funzioni ADD e DEL è possibile aggiungere o togliere elementi dell'albero delle fonti scelte manualmente.

### ADD
Costrusce un albero aggiungendo il nodo (fonte) su cui si è cliccato leggendolo da una schiera memorizzata.

### DEL
Costrusce un albero togliendo il nodo (fonte) su cui si è cliccato cancellandolo da una schiera memorizzata.

## ANALISI DISPONIBILITA' FINANZIARIA
Con la funzione **ESE** il servizio ritorna i dati relativi alla disponibilità finanziaria di un cliente, dando la possibilità di utilizzare gruppi fonti memorizzati o di scegliere alcuni manualmente. Vengono coinvolte due /COPY :  la **£C6F** e la **£C6D**

### ADF
Questa funzione/metodo svolge la funzione di costruire una matrice contenente i dati realtivi alla disponibilità finanziaria del cliente, ricalcando lo schema utilizzato dal punto "Analisi dispon. finanziaria" del menù "Disponibilità finanziaria ".
In questa funzione/metodo sono utilizzati 2 oggetti : 
l'_3_Oggetto 1 è necessario per il funzionamento di questa funzione ed è quello in cui vengono forniti alla funzione i dati realtivi al cliente di cui si richiede l'elaborazione; nel caso in cui si stiano elaborando delle scelte fonti manuali, l'oggetto 1 è sufficiente.
l'_3_Oggetto 2 è invece facoltativo, e serve nel caso in cui si stiano elaborando dei gruppi fonti memorizzati.




 :  : PRO.SER Cod="GFO.FPR.1" Tit="Gruppi Fonti. Fonti presenti" Fun="F(TRE;C5SER_13;GFO.FPR) 1(MD;C5C6F0G;-(O;;MDC5C6F0G;Memorizzazione C5))"

 :  : PRO.SER Cod="GFO.FFU.2" Tit="Gruppi Fonti. Fonti future" Fun="F(TRE;C5SER_13;GFO.FFU)" Ref="GFO.FPR.1"

 :  : PRO.SER Cod="ADD.3" Tit="Aggiungi fonte. " Fun="F(TRE;C5SER_13;ADD) 2(TA;C6E;-(O;;TAC6E;Tabella C6E))"

 :  : PRO.SER Cod="DEL.4" Tit="Togli fonte. " Fun="F(TRE;C5SER_13;DEL)" Ref="ADD.3"

 :  : PRO.SER Cod="ADF.5" Tit="Disponibilità finanziaria. " Fun="F(EXB;C5SER_13;ADF) 3(CN;CLI;-(O;;CNCLI;Cliente))"

 :  : PRO.SER Cod="ADF.6" Tit="Disponibilità finanziaria. " Fun="F(EXA;C5SER_13;ADF)" Ref="ADF.5"

