# OBIETTIVO
Il servizio si occupa di estrarre i riferimenti telefonici, skype e mail di uno o più contatti.

# FUNZIONI/METODI
La sintassi per richiamare la funzione/metodo che interessa è la seguente **funzione.metodo**

## Metodi

 T(Metodi di esportazione di una matrice in un databse esterno)
- LET
-- ALL :  Leggi tutti i riferimenti di tutti i contatti
-- FLT :  Leggi i riferimenti filtrati



Per i dettagli vedi la sezione dei parametri.




 :  : PRO.SER Cod="LET.ALL.1" Tit=". Leggi tutti i riferimenti di tutti i con" Fun="F(EXB;X1SER_26;LET.ALL)"

 :  : PRO.SER Cod="LET.FLT.2" Tit=". Leggi i riferimenti filtrati" Fun="F(EXB;X1SER_26;LET.FLT) P( USR(-(F;;TAB£U;Utente)) CNAZI(-(F;;CNAZI;Azienda/contesto)) CLEXC(-(F;;CNCLI;Clienti da includere)) CLINC(-(F;;CNCLI;Clienti da escludere)) CMINC(-(F;;CM;Commesse da includere)) CMEXC(-(F;;CM;Commesse da escludere)))"

