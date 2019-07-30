 :  : HEA RESP() STAT(00)
# OBIETTIVO

# FUNZIONI/METODI

## Funzione XXX
### Metodo YYY (XXX.YYY)


 :  : RIN                              TpParametro         Lung.DOVAuD
 :  : PRZ
## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato
SRA.DEN|TP|SCA|Scadenzario
SRA.DEN|TP|RIS|Rischio
SRA.DEN|TP||Esposizione
SRP.DEN|TP|SCA|Scadenzario
SRP.DEN|TP|RIS|Rischio
SRP.DEN|TP||Esposizione


 :  : PRO.SER Cod="SRA.DEN.1" Tit="Scadenze Attive. Dettaglio per ente" Fun="F(EXB;C5SER_04;SRA.DEN) 1(LI;CNCLI;-(F;;LICNCLI;Tipo)) 2(;;-(F;;;Codice)) 3(D8;*YYMD;-(F;;D8*YYMD;Data)) P( TP(-(F;;**;Tipo scadenze)) SC(-(F;;Q2RR;Schema)) PE(-(F;;V3C5SPE;Pertinenza)) CO(-(F;;V3C5SCO;Condizione)) NR(-(F;;V2SI/NO;Netto Ritenuta)) CU(-(F;;V2SI/NO;Cumulazione effetti)) PO(-(F;;V2SI/NO;Escludi effetti presentati)) DT(-(F;;D8*YYMD;Data situazione)))"

 :  : PRO.SER Cod="SRA.DEN.2" Tit="Scadenze Attive. Dettaglio per ente" Fun="F(EXC;C5SER_04;SRA.DEN)" Ref="SRA.DEN.1"

 :  : PRO.SER Cod="SRA.DEN.3" Tit="Scadenze Attive. Dettaglio per ente" Fun="F(FRM;C5SER_04;SRA.DEN)" Ref="SRA.DEN.1"

 :  : PRO.SER Cod="SRP.DEN.4" Tit="Scadenze Passive. Dettaglio per ente" Fun="F(EXB;C5SER_04;SRP.DEN)" Ref="SRA.DEN.1"

 :  : PRO.SER Cod="SRP.DEN.5" Tit="Scadenze Passive. Dettaglio per ente" Fun="F(EXC;C5SER_04;SRP.DEN)" Ref="SRA.DEN.1"

 :  : PRO.SER Cod="SRP.DEN.6" Tit="Scadenze Passive. Dettaglio per ente" Fun="F(FRM;C5SER_04;SRP.DEN)" Ref="SRA.DEN.1"

 :  : PRO.SER Cod="PAR.MAT.7" Tit="Partite. Dettaglio" Fun="F(EXB;C5SER_04;PAR.MAT) 1(CN;;-(O;;CN;Soggetto)) P( PER(-(F;;TAPER&AM.AZ;Esercizio)))"

 :  : PRO.SER Cod="PAR.MAT.8" Tit="Partite. Dettaglio" Fun="F(EXC;C5SER_04;PAR.MAT)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.MAT.9" Tit="Partite. Dettaglio" Fun="F(FRM;C5SER_04;PAR.MAT)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.MAA.10" Tit="Partite. Dettaglio aperte" Fun="F(EXB;C5SER_04;PAR.MAA)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.MAA.11" Tit="Partite. Dettaglio aperte" Fun="F(EXC;C5SER_04;PAR.MAA)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.MAA.12" Tit="Partite. Dettaglio aperte" Fun="F(FRM;C5SER_04;PAR.MAA)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.DOC.13" Tit="Partite. Solo Movimenti di Documento" Fun="F(EXB;C5SER_04;PAR.DOC)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.DOC.14" Tit="Partite. Solo Movimenti di Documento" Fun="F(EXC;C5SER_04;PAR.DOC)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.DOC.15" Tit="Partite. Solo Movimenti di Documento" Fun="F(FRM;C5SER_04;PAR.DOC)" Ref="PAR.MAT.7"

 :  : PRO.SER Cod="PAR.SIN.16" Tit="Partite. Sintesi" Fun="F(EXB;C5SER_04;PAR.SIN) 1(CN;;-(O;;CN;Soggetto))"

 :  : PRO.SER Cod="PAR.SIN.17" Tit="Partite. Sintesi" Fun="F(EXC;C5SER_04;PAR.SIN)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAR.SIN.18" Tit="Partite. Sintesi" Fun="F(FRM;C5SER_04;PAR.SIN)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAR.SIA.19" Tit="Partite. Sintesi aperte" Fun="F(EXB;C5SER_04;PAR.SIA)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAR.SIA.20" Tit="Partite. Sintesi aperte" Fun="F(EXC;C5SER_04;PAR.SIA)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAR.SIA.21" Tit="Partite. Sintesi aperte" Fun="F(FRM;C5SER_04;PAR.SIA)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAR.DET.22" Tit="Partite. Dettaglio" Fun="F(EXB;C5SER_04;PAR.DET) 1(CN;;-(O;;CN;Soggetto)) 2(D8;*YYMD;-(O;;D8*YYMD;Data Documento)) 3(**;;-(O;;**;N° Documento))"

 :  : PRO.SER Cod="PAR.DET.23" Tit="Partite. Dettaglio" Fun="F(EXC;C5SER_04;PAR.DET)" Ref="PAR.DET.22"

 :  : PRO.SER Cod="PAR.DET.24" Tit="Partite. Dettaglio" Fun="F(FRM;C5SER_04;PAR.DET)" Ref="PAR.DET.22"

 :  : PRO.SER Cod="PAG.RIT.25" Tit="Incassi/Pagamenti. Ritardi" Fun="F(EXB;C5SER_04;PAG.RIT) 1(CN;;-(O;;CN;Soggetto)) 2(TA;PER&AM.AZ;-(O;;TAPER&AM.AZ;Esercizio))"

 :  : PRO.SER Cod="PAG.RIT.26" Tit="Incassi/Pagamenti. Ritardi" Fun="F(EXC;C5SER_04;PAG.RIT)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.RIT.27" Tit="Incassi/Pagamenti. Ritardi" Fun="F(FRM;C5SER_04;PAG.RIT)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.INS.28" Tit="Incassi/Pagamenti. Insoluti" Fun="F(EXB;C5SER_04;PAG.INS)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.INS.29" Tit="Incassi/Pagamenti. Insoluti" Fun="F(EXC;C5SER_04;PAG.INS)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.INS.30" Tit="Incassi/Pagamenti. Insoluti" Fun="F(FRM;C5SER_04;PAG.INS)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.SOL.31" Tit="Incassi/Pagamenti. Solleciti" Fun="F(EXB;C5SER_04;PAG.SOL)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.SOL.32" Tit="Incassi/Pagamenti. Solleciti" Fun="F(EXC;C5SER_04;PAG.SOL)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.SOL.33" Tit="Incassi/Pagamenti. Solleciti" Fun="F(FRM;C5SER_04;PAG.SOL)" Ref="PAG.RIT.25"

 :  : PRO.SER Cod="PAG.SIN.34" Tit="Incassi/Pagamenti. Sintesi" Fun="F(EXB;C5SER_04;PAG.SIN)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAG.SIN.35" Tit="Incassi/Pagamenti. Sintesi" Fun="F(EXC;C5SER_04;PAG.SIN)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAG.SIN.36" Tit="Incassi/Pagamenti. Sintesi" Fun="F(FRM;C5SER_04;PAG.SIN)" Ref="PAR.SIN.16"

 :  : PRO.SER Cod="PAG.IDX.37" Tit="Incassi/Pagamenti. Indici" Fun="F(EXB;C5SER_04;PAG.IDX)"

