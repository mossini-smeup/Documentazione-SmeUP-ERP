 :  : HEA RESP(LS) STAT(10)
# OBIETTIVO

# FUNZIONI E METODI

## LIS Lista
### ELE Elementi
Espone gli schemi presenti.
### FLD Campi
Espone la definizione dei campi di uno schema.

## FMT Formattazione
### SCH Schema
Espone lo schema in formato SQL.

## CAR Caricamento
Da un codice oggetto (K1) ed uno schema (K2) ne espone il risultato.

## OGGETTI COLLEGATI

 :  : RIN                              TpParametro         Lung.DOVAuD
## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato
LIS|PAG|*Yes|Si
LIS|PAG||No


 :  : PRO.SER Cod="LIS.1" Tit="Lista. " Fun="F(TRE;JASER_02L;LIS) 1(Q1;;-(F;;Q1;Oggetto)) 2(Q2;;-(F;;Q2;Schema)) 3(Q3;;-(F;;Q3;Filtro)) 4(Q4;;-(F;;Q4;Ordinamento)) 5(**;;-(F;;**;Contesto)) 6(**;;-(F;;**;Configurazione Filtro)) P( Q3_CFG(-(F;;**;Configurazione filtro)) FLT(-(F;;**;Filtro)) NRE(-(F;;**;N° Elementi per Pagina)) PAG(-(F;;**;Carica Pag. Successiva)))"

 :  : PRO.SER Cod="LIS.2" Tit="Lista. " Fun="F(EXB;JASER_02L;LIS)" Ref="LIS.1"

 :  : PRO.SER Cod="LIS.3" Tit="Lista. " Fun="F(EXC;JASER_02L;LIS)" Ref="LIS.1"

 :  : PRO.SER Cod="LIS.4" Tit="Lista. " Fun="F(FRM;JASER_02L;LIS)" Ref="LIS.1"

