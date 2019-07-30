 :  : HEA RESP(LS) STAT(10)
# OBIETTIVO
Raccogliere tutti i servizi relativi alle frasi, alle parole, alle loro traduzioni e utilizzi.
I servizi si fondano sull'analisi dei dati contenuti negli archivi del modulo A£LING.

# FUNZIONI E METODI
Le funzioni sono dipendenti dalla partenza. Alcune accettano sia la chiave che il testo (utilizzato per ottenere
la chiave).
Si possono vedere gli utilizzi nella scheda del modulo A£LING

## OGGETTI COLLEGATI
 :  : DEC T(TA) P(B£AMO) K(A£LING)

 :  : PRO.SER Cod="LIS.RIE.1" Tit="Lista. Risultato" Fun="F(EXB;V5SER_11;LIS.RIE) 1(VD;;-(O;;VD;)) P( VA(-(F;;**;Mde)) VA(-(F;;**;Std)) VA(-(F;;**;Azi)) VA(-(F;;**;Dim)) VA(-(F;;**;Mis)) VA(-(F;;**;Whe)))"

 :  : PRO.SER Cod="LIS.RIE.2" Tit="Lista. Risultato" Fun="F(REP;V5SER_11;LIS.RIE)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.RIE.3" Tit="Lista. Risultato" Fun="F(EXC;V5SER_11;LIS.RIE)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.RIS.4" Tit="Lista. Risultato" Fun="F(EXB;V5SER_11;LIS.RIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.RIS.5" Tit="Lista. Risultato" Fun="F(REP;V5SER_11;LIS.RIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.RIS.6" Tit="Lista. Risultato" Fun="F(EXC;V5SER_11;LIS.RIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.REP.7" Tit="Lista. Report" Fun="F(EXB;V5SER_11;LIS.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.REP.8" Tit="Lista. Report" Fun="F(REP;V5SER_11;LIS.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.REP.9" Tit="Lista. Report" Fun="F(EXC;V5SER_11;LIS.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.STD.10" Tit="Lista. Standard" Fun="F(EXB;V5SER_11;LIS.STD)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.STD.11" Tit="Lista. Standard" Fun="F(REP;V5SER_11;LIS.STD)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.STD.12" Tit="Lista. Standard" Fun="F(EXC;V5SER_11;LIS.STD)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.DIM.13" Tit="Lista. Dimensioni" Fun="F(EXB;V5SER_11;LIS.DIM)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.DIM.14" Tit="Lista. Dimensioni" Fun="F(REP;V5SER_11;LIS.DIM)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.DIM.15" Tit="Lista. Dimensioni" Fun="F(EXC;V5SER_11;LIS.DIM)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MIS.16" Tit="Lista. Misure" Fun="F(EXB;V5SER_11;LIS.MIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MIS.17" Tit="Lista. Misure" Fun="F(REP;V5SER_11;LIS.MIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MIS.18" Tit="Lista. Misure" Fun="F(EXC;V5SER_11;LIS.MIS)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.AZI.19" Tit="Lista. Azioni" Fun="F(EXB;V5SER_11;LIS.AZI)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.AZI.20" Tit="Lista. Azioni" Fun="F(REP;V5SER_11;LIS.AZI)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.AZI.21" Tit="Lista. Azioni" Fun="F(EXC;V5SER_11;LIS.AZI)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MDE.22" Tit="Lista. Memorizzazioni Video" Fun="F(EXB;V5SER_11;LIS.MDE)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MDE.23" Tit="Lista. Memorizzazioni Video" Fun="F(REP;V5SER_11;LIS.MDE)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="LIS.MDE.24" Tit="Lista. Memorizzazioni Video" Fun="F(EXC;V5SER_11;LIS.MDE)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="DBG.001.25" Tit="Matrice di debug. Matrice di debug" Fun="F(EXB;V5SER_11;DBG.001)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="DBG.001.26" Tit="Matrice di debug. Matrice di debug" Fun="F(REP;V5SER_11;DBG.001)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="DBG.001.27" Tit="Matrice di debug. Matrice di debug" Fun="F(EXC;V5SER_11;DBG.001)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="FLU.REP.28" Tit="Flusso. Di Report" Fun="F(EXB;V5SER_11;FLU.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="FLU.REP.29" Tit="Flusso. Di Report" Fun="F(REP;V5SER_11;FLU.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="FLU.REP.30" Tit="Flusso. Di Report" Fun="F(EXC;V5SER_11;FLU.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="VOL.REP.31" Tit="Volume. Di Report" Fun="F(EXB;V5SER_11;VOL.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="VOL.REP.32" Tit="Volume. Di Report" Fun="F(REP;V5SER_11;VOL.REP)" Ref="LIS.RIE.1"

 :  : PRO.SER Cod="VOL.REP.33" Tit="Volume. Di Report" Fun="F(EXC;V5SER_11;VOL.REP)" Ref="LIS.RIE.1"

