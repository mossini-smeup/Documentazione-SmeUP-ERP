## INTRODUZIONE

La routine £M5S riceve il record di un consiglio di pianificazione
 :  : DEC T(OJ) P(*FILE) K(M5CONS0F)
ed eventualmente i parametri di pianificazione (se metodo=PAS) inel campo specifico (£M5RPA) della /copy
 :  : DEC T(MB) P(QILEGEN) K(£M5RDS)
in caso contrario li calcola con la /copy
 :  : DEC T(MB) P(QILEGEN) K(£M5A)

Il suo compito è di calcolare quantità, date, fornitori e contratti del suggerimento ricevuto, che può essere suddiviso a causa di assegnazione multipla (ad esempio sia produzione sia conto lavoro, in diverse %), oppure suddivisa per più di un fornitore.
L'assegnazione a fornitori/contratti è guidata dalla /copy
 :  : DEC T(MB) P(QILEGEN) K(£V5U)

Le strategie implementate sono : 
- [Assegna fornitore-contratto a suggerimenti](Sorgenti/MB/DOC/M5_018)




