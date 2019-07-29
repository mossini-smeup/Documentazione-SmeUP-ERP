## Scorta minima
>Se l'origine è SC (scorta minima)  : 
>**Parametro 1**.
-   Pos.1/3 :   Tipo ente per scorta (opzionale)
-   Pos.4     Modalità calcolo scorta per ente (opzionale :  è significativo se
.             impostato il tipo ente).Può assumere i seguenti valori : 
.              ' '  Scorta specifica. Viene ritornata la scorta a quantità inserita
.                   per ogni ente, nell'archivio articolo/ente
.              '1'  Scorta generale distribuita. La scorta definita a livello di
.                   articolo/magazzino, viene suddivisa tra i vari enti  in base alla
.                   % di distribuzione della scorta impostata a livello di
.                   articolo/ente, nel campo scorta gg o distribuita.
.              '2'  Le due scorte precedenti vengono ritornate in due righe separate.
.              '3'  Le due scorte precedenti vengono ritornate in un'unica riga.
.
.                   Esempio : 
.                                             Codice Ente
.                         Dati di ingresso    F01       F02       F03       F04
.                         Scorta art :  200
.                         Scorta %            20         30                  50
.                         Scorta Quantità               200       150       300
.
.                         Scorta calcolata
.                         Modo ' '                      200       150       300
.                         Modo '1'            40         60                 100
.                         Modo '2'            40        200 60    150       300 100
.                         Modo '3'            40        260       150       400
.                   Se non è stato impostato l'ente viene semplicemente ritornata
.                   la scorta definita per l'articolo/magazzino.
-   Pos.5     Risalita scorta.
.             E' significativa se NON è stata impostata la scorta per Ente.
.             Si inserisce un elemento V2/GM_SM, che guida il modo in cui viene
.             reperita la scorta minima, nei dati magazzino/articolo.

