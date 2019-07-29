# CSB - Struttura imp. aliquote
 :  : DEC T(ST) K(CSB)
## OBIETTIVO
La tabella permette di scegliere la colonna nella quale verrà memorizzato il tempo dell'operazione che servirà, in seguito, per determinare il costo dell'operazione.
La tabella risulta formata da 6 flag per ogni aliquota.
## CARATTERISTICHE
Questa tabella deve essere compilata e legata a un tipo costo.
## SIGNIFICATO DEI CAMPI


## CONTENUTO DEI CAMPI

 :  : FLD T$H,01

I sei CAMPI provenienti dal ciclo sono così suddivisi : 
1  - Componente di tempo numero 1
2  - Componente di tempo numero 2
3  - Componente di tempo numero 3
4  - Componente di tempo numero 4
5  - Componente di tempo numero 5
6  - Componente di tempo numero 6
Per ulteriori informazioni si veda la documentazione allegata alla funzione £BRT.
Le 6 aliquote sono gestite dalla funzione £G16 e sono definite nella tabella *CNVS.
Dove il significato standard delle aliquote è : 
1  - Lavoro variabile
2  - Macchina variabile
3  - Diversi variabile
4  - Lavoro fisso
5  - Macchina fisso
6  - Diversi fisso
Il risultato dell'incrocio Tempo/Aliquota può essere assegnato ad uno degli 8 possibili valori memorizzati nell'archivio.
Nel caso in cui non esista la tabella viene assunta la seguente impostazione.
CAMPO     1    2    3    4    5    6
Aliq.01   1         5
 "   02        3         7
 "   03
 "   04   2         6
 "   05        4         8
 "   06
Il significato del singolo flag è il seguente : 
1  - Tempo lavorazione variabile (campo C$LAV1)
2  - Tempo lavorazione fisso (C$LAF1)
3  - Tempo macchina variabile (C$MCV1)
4  - Tempo macchina fisso (C$MCF1)
5  - Tempo attrezzaggio lavorazione variabile
6  - Tempo attrezzaggio lavorazione fisso
7  - Tempo attrezzaggio macchina variabile
8  - Tempo attrezzaggio macchina fisso

 :  : FLD T$H,02.T$H,01

 :  : FLD T$H,03.T$H,01

 :  : FLD T$H,04.T$H,01

 :  : FLD T$H,05.T$H,01

 :  : FLD T$H,06.T$H,01

 :  : FLD T$H,07.T$H,01

 :  : FLD T$H,08.T$H,01

 :  : FLD T$H,09.T$H,01

 :  : FLD T$H,10.T$H,01

 :  : FLD T$H,11.T$H,01

 :  : FLD T$H,12.T$H,01

 :  : FLD T$H,13.T$H,01

 :  : FLD T$H,14.T$H,01

 :  : FLD T$H,15.T$H,01

 :  : FLD T$H,16.T$H,01

 :  : FLD T$H,17.T$H,01

 :  : FLD T$H,18.T$H,01

 :  : FLD T$H,19.T$H,01

 :  : FLD T$H,20.T$H,01

 :  : FLD T$H,21.T$H,01

 :  : FLD T$H,22.T$H,01

 :  : FLD T$H,23.T$H,01

 :  : FLD T$H,24.T$H,01

 :  : FLD T$H,25.T$H,01

 :  : FLD T$H,26.T$H,01

 :  : FLD T$H,27.T$H,01

 :  : FLD T$H,28.T$H,01

 :  : FLD T$H,29.T$H,01

 :  : FLD T$H,30.T$H,01

 :  : FLD T$H,31.T$H,01

 :  : FLD T$H,32.T$H,01

 :  : FLD T$H,33.T$H,01

 :  : FLD T$H,34.T$H,01

 :  : FLD T$H,35.T$H,01

 :  : FLD T$H,36.T$H,01
