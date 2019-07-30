 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Attraverso questo servizio è possibile lanciare le elaborazioni previste relative alle fatture,
attive e passive. Esse si articolano nel seguente modo : 
## TRE Albero delle fatture per ente
I vari metodi previsti permettono di ritornare un albero con i periodi relativi alle fatture di
un ente
### . ATT - Ciclo Attivo
Tutti i periodi in cui sono presenti fatture attive dell'ente
### . PAS - Ciclo Passivo
Tutti i periodi in cui sono presenti fatture passive dell'ente
## MAT Matrice
Tramite questa funzione è possibile creare una matrice relative alle fatture dell'ente per il
periodo richiesto o se è richiesto una fattura il suo dettaglio
### . ATT - Ciclo Attivo
Gestione matrice per le fatture del ciclo attivo (vendite)
### . PAS - Ciclo Passivo
Gestione matrice per le fatture del ciclo passivo (acquisti)
 :  : PRO.SER Cod="TRE.ATT.1" Tit="Albero periodi fatture. Ciclo Attivo" Fun="F(TRE;V5SER_04;TRE.ATT) 1(CN;xxx;-(O;;CNxxx;Ente))"

 :  : PRO.SER Cod="TRE.PAS.2" Tit="Albero periodi fatture. Ciclo Passivo" Fun="F(TRE;V5SER_04;TRE.PAS)" Ref="TRE.ATT.1"

 :  : PRO.SER Cod="MAT.ATT.3" Tit="Matrice fatture. Ciclo Attivo" Fun="F(EXB;V5SER_04;MAT.ATT) 1(CN;xxx;-(O;;CNxxx;Periodo))"

 :  : PRO.SER Cod="MAT.ATT.4" Tit="Matrice fatture. Ciclo Attivo" Fun="F(EXA;V5SER_04;MAT.ATT)" Ref="MAT.ATT.3"

 :  : PRO.SER Cod="MAT.PAS.5" Tit="Matrice fatture. Ciclo Passivo" Fun="F(EXB;V5SER_04;MAT.PAS)" Ref="MAT.ATT.3"

 :  : PRO.SER Cod="MAT.PAS.6" Tit="Matrice fatture. Ciclo Passivo" Fun="F(EXA;V5SER_04;MAT.PAS)" Ref="MAT.ATT.3"

