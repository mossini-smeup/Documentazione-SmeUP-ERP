# £FOR APPLICAZIONE DI FORMULE MATEMATICHE A VARIABILI
 * _2_FUNZIONE
 ** _3_Calcolo, viene eseguito il calcolo delle formule visualizzate attraverso l'utilizzo delle variabili a video.
 * _2_METODO
 ** _3_On; l'elaboratore di formule è attivato. Le formule vengono analizzate per ogni richiesta di calcolo.
 ** _3_Off; l'elaboratore di formule è disattivato. Le formule caricate alla prima richiesta di calcolo vengono memorizzate.

Qualsiasi successiva modifica alle stesse formule viene ignorata.

 * _2_VARIABILI; nonostante a video compaiano 9 variabili (V01,..,V09), nel programma il range arriva a 99, da V01 a V99. Oltrepassare tale range porta inevitabilmente ad un CPF. Mentre a video la loro lunghezza arriva a 12 cifre intere e 3 decimali, a programma si arriva a 15 cifre intere e 5 decimali.
 * _2_FORMULE;  Devono essere inserite a partire dalla prima posizione a sinistra, utilizzando i nomi delle variabili intercalati dalle operazioni possibili.
 * _2_OPERAZIONI :  +,*,-,/,%,"(",")".

# ESEMPIO
(V01+V05)*V02 Il valore della variabile V01 sommato al valore della variabile V05, viene moltiplicato al valore della variabile V02.

Mentre a video le potenzialità di calcolo si limitano a 6 formule, ciascuna costruibile attraverso 38 caratteri, a programma si arriva a formule costruibili attraverso 256 caratteri.

