 :  : HEA RESP(GR) STAT(15)
# OBIETTIVO
Questo servizio costruisce rappresentazioni sintetiche del risultato dell'MRP.
Per tutte le funzioni è prevista la possibilità di utilizzare una exit, da passare nei parametri; se non passata il programma controlla l'esistenza della exit standard M5SER_06U e la utilizza se presente.

# FUNZIONI
## Analisi raggruppata a una data (GRU)
Presenta una matrice con una riga per articolo (articolo/oggetto di rottura, se utilizzato) e una serie di colonne rappresentanti le quantità calcolate dall'MRP fino a una certa data, suddivise per fonte o raggruppamenti di fonti.

## Analisi su una periodicità (PER)
Presenta una matrice con una riga per articolo (articolo/oggetto di rottura, se utilizzato) e una serie di colonne rappresentanti l'evoluzione nel tempo della disponibilità calcolata dall'MRP lungo un certo periodo.

 :  : PRO.SER Cod="GRU.1" Tit="Analisi raggruppata a una data. " Fun="F(EXB;M5SER_06;GRU) 1(TA;M5B;-(O;;TAM5B;Scenario)) 2(TA;MAG;-(O;;TAMAG;Magazzino)) 3(D8;*YYMD;-(O;;D8*YYMD;Data massima di analisi)) P( TIP(-(F;;;Tipo raggruppamento)) AGG(-(F;;;Suff.pgm.aggiustamento)) PAR(-(F;;;Param.pgm.aggiustamento)) MOD(-(F;;;Modalità analisi)))"

 :  : PRO.SER Cod="PER.2" Tit="Analisi su un periodo. " Fun="F(EXB;M5SER_06;PER) 1(TA;M5B;-(O;;TAM5B;Scenario)) 2(TA;MAG;-(O;;TAMAG;Magazzino)) 3(TA;A£Q;-(O;;TAA£Q;Periodicità)) 4(D8;*YYMD;-(F;;D8*YYMD;Data di inizio analisi)) P( AGG(-(F;;;Suff.pgm.aggiustamento)) PAR(-(F;;;Param.pgm.aggiustamento)) MOD(-(F;;;Modalità analisi)))"

