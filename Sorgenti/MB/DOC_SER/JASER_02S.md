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
 :  : PRO.SER Cod="LIS.ELE.1" Tit="Lista. Elementi" Fun="F(TRE;JASER_02S;LIS.ELE) 1(**;;-( ;;**;Oggetto))"

 :  : PRO.SER Cod="LIS.FLD.2" Tit="Lista. Campi" Fun="F(TRE;JASER_02S;LIS.FLD) 1(Q2;;-(O;;Q2;Schema))"

 :  : PRO.SER Cod="LIS.FLD.3" Tit="Lista. Campi" Fun="F(EXB;JASER_02S;LIS.FLD)" Ref="LIS.FLD.2"

 :  : PRO.SER Cod="FMT.SCH.4" Tit="Formattazione. Schema" Fun="F(TXT;JASER_02S;FMT.SCH)" Ref="LIS.FLD.2"

 :  : PRO.SER Cod="CAR.SCH.5" Tit="Caricamento. Schema" Fun="F(TXT;JASER_02S;CAR.SCH) 1(**;;-(O;;**;ID Oggetto)) 2(Q2;;-(O;;Q2;Schema))"

