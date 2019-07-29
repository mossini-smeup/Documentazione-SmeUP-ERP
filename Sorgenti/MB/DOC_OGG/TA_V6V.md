# V6V - Piano I.S.C.
 :  : DEC T(ST) K(V6V)
## OBIETTIVO
Definisce i parametri di calcolo dell'_Indennità Suppletiva di Clientela_, che dovrà essere accantonata per l'agente, in rapporto alle provvigioni liquidate e agli anni di durata del rapporto. Dovrà essere inoltre versata all'agente al termine del rapporto con l'azienda.
## CONTENUTO DEI CAMPI
 :  : FLD T$V6VA **% Fissa**
Indica la % fissa da accantonare sulle provvigioni.
 :  : FLD T$V6VB **Anno 1° incremento**
Indica il numero di anni a partire dal quale dovrà essere applicato il 1° incremento nella % di calcolo dell'accantonamento.
 :  : FLD T$V6VC **% 1° incremento**
Indica la % di incremento nel calcolo dell'accantonamento; essa dovrà essere applicata una volta che gli anni di durata del rapporto avranno superato il limite indicato dal campo precedente.
 :  : FLD T$V6VD **Importo massimo 1° incremento**
Indica l'importo limite raggiunto il quale non dovrà più essere applicata la % aggiunta in seguito al 1° incremento.
 :  : FLD T$V6VE **Anno 2° incremento**
Indica il numero di anni a partire dal quale dovrà essere applicato il 2° incremento nella % di calcolo dell'accantonamento.
 :  : FLD T$V6VF **% 2° incremento**
Indica la % di incremento nel calcolo dell'accantonamento che dovrà essere applicata, una volta che gli anni di durata del rapporto avranno superato il limite indicato dal campo precedente.
 :  : FLD T$V6VG **Importo massimo 2° incremento**
Indica l'importo limite raggiunto il quale non dovrà più essere applicata la % aggiunta in seguito al 2° incremento.
