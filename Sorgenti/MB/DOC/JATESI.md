 :  : INI Verifica esistenza questionario
 :  : CMD CALL B£FUN3
 :  : FIN

 :  : INI Verifica esistenza subsettore domande
 :  : CMD CALL B£AR16
 :  : FIN
 :  : DEC T(MB) P(DOC) K(JATS2) I(Verifica esistenza tabelle)

 :  : DEC T(TA) P(CFQ) K() I(Visualizza questionario)

 :  : INI Questionario Bilanciai
 :  : CMA  :  : FUN PG(CFQUE0) T1(RE) P1(Q-) K1(COOP_BIL)
 :  : FIN
 :  : INI Questionario Italpresse
 :  : CMA  :  : FUN PG(CFQUE0) T1(RE) P1(Q-) K1(IP)
 :  : FIN
