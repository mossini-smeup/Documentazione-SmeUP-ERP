 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Attraverso questo servizio è possibile lanciare le elaborazioni previste relative ai viaggi.

## PRE - ALL
Permette di ritornare in un unica chiamata le previsioni di tutti i raggruppamenti.
Questa funzione gestisce tre parametri : 
- LO :  E' necessario il logico che si vuole utilizzare per la lettura
- K1 :  E' possibile inidare in compatibilità del logico scelto il valore di filtro da applicare alla
1° chiave del logico
- K2 :  E' possibile inidare in compatibilità del logico scelto il valore di filtro da applicare alla
2° chiave del logico

## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato


 :  : PRO.SER Cod="PRE.ALL.1" Tit="Previsioni. Tutti i raggruppamenti" Fun="F(EXB;MMSER_01;PRE.ALL) P( LO(-(F;;**;Logico)) K1(-(F;;**;Chiave 1)) K2(-(F;;**;Chiave 2)))"

