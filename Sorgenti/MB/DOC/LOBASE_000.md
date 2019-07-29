# Porte comunicazione
Loocup / Sme.Up Provider, per comunicare con l'AS400 utilizzano il range di porte 8470-8476.

Per ogni istanza di Loocup / Sme.Up Provider, vengono aperte 3 porte dalla 6000 in poi, es 6000, 6001, 6002.
Quando Loocup / Sme.Up Provider si avvia cerca tre porte libere a partire dalla 6000. Se le trova occupate, salta alla 6003 e così via, di 3 in 3.
Queste porte servono  per la comunicazione intra processo, avremo pertanto che SmeBase si metterà in ascolto sulla 6000, SmeTray sulla 6001 e Smeuiclt sulla 6002.

Per lo SmeUp Provider esistono altre porte: la porta http, la porta server e la porta con cui comunica con il gestore dei database dei log.
La porta http(s) e la porta server vengono definite nel file wrapper.conf.
La porta http(s) di default è la 9090, quella server, di default è la 9990.

Se sono presenti più istanze di provider sulla stessa macchina ogni istanza dovrà avere la propria porta http(s) e la propria porta server.
La porta del gestore del databse dei log è dinamica e cercata a partire dalla porta 7000. Se ad esempio ho 3 istanze di provider attive, la prima occuperà la porta 7000, la seconda la 7001 e la terza la 7002.
Se il gestore dei log su database non è attivo, non verranno utilizzate le porte da 7000 in sù.

