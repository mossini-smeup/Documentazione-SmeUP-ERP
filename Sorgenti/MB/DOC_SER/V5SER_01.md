 :  : HEA RESP(BP) STAT(10)
# OBIETTIVO
Questo servizio fornisce funzionalità di interrogazione degli oggetti DO.

# FUNZIONI/METODI

## DOC Documento
Tutte i metodi di questa funzione restituiscono una griglia con i valori relativi a un aspetto del d
### IMP - Importi
### PRO - Provvigioni
### TAX - Tasse
### SPE - Spese
### CON - Conti contabili
### SCA - Scadenze
### GRA - Grafico valori

 :  : PRO.SER Cod="DOC.IMP.1" Tit=". Importi" Fun="F(EXA;V5SER_01;DOC.IMP) 1(DO;;-(O;;DO;Documento))"

 :  : PRO.SER Cod="DOC.IMP.2" Tit=". Importi" Fun="F(EXB;V5SER_01;DOC.IMP)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.IMP.3" Tit=". Importi" Fun="F(EXC;V5SER_01;DOC.IMP)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.PRO.4" Tit=". Provvigioni" Fun="F(EXA;V5SER_01;DOC.PRO)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.PRO.5" Tit=". Provvigioni" Fun="F(EXB;V5SER_01;DOC.PRO)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.PRO.6" Tit=". Provvigioni" Fun="F(EXC;V5SER_01;DOC.PRO)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.TAX.7" Tit=". Tasse" Fun="F(EXA;V5SER_01;DOC.TAX)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.TAX.8" Tit=". Tasse" Fun="F(EXB;V5SER_01;DOC.TAX)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.TAX.9" Tit=". Tasse" Fun="F(EXC;V5SER_01;DOC.TAX)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SPE.10" Tit=". Spese" Fun="F(EXA;V5SER_01;DOC.SPE)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SPE.11" Tit=". Spese" Fun="F(EXB;V5SER_01;DOC.SPE)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SPE.12" Tit=". Spese" Fun="F(EXC;V5SER_01;DOC.SPE)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.CON.13" Tit=". Conti contabili" Fun="F(EXA;V5SER_01;DOC.CON)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.CON.14" Tit=". Conti contabili" Fun="F(EXB;V5SER_01;DOC.CON)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.CON.15" Tit=". Conti contabili" Fun="F(EXC;V5SER_01;DOC.CON)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SCA.16" Tit=". Scadenze" Fun="F(EXA;V5SER_01;DOC.SCA)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SCA.17" Tit=". Scadenze" Fun="F(EXB;V5SER_01;DOC.SCA)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.SCA.18" Tit=". Scadenze" Fun="F(EXC;V5SER_01;DOC.SCA)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.GRA.19" Tit=". Grafico valori" Fun="F(EXA;V5SER_01;DOC.GRA)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.GRA.20" Tit=". Grafico valori" Fun="F(EXB;V5SER_01;DOC.GRA)" Ref="DOC.IMP.1"

 :  : PRO.SER Cod="DOC.GRA.21" Tit=". Grafico valori" Fun="F(EXC;V5SER_01;DOC.GRA)" Ref="DOC.IMP.1"

