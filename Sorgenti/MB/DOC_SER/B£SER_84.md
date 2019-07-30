 :  : HEA RESP(LS) STAT(10)
# OBIETTIVO

# FUNZIONI E METODI

## VAL Valori

- FLD Torna la distinct dei valori trovati in un campo di un file
- TRE pome FLD ma l'xml viene tornato in forma ad albero
- OGG Torna tutte le istanze di un oggetto

## GET

- MEM Dati in memoria

## OGGETTI COLLEGATI

## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato
VAL.FLD|Pag|*YES|Si
VAL.FLD|Com|Yes|Si
VAL.FLD|Ord|Des|Discendente
VAL.FLD|Ord||Ascendente
VAL.TRE|Pag|*YES|Si
VAL.TRE|Com|Yes|Si
VAL.TRE|Ord|Des|Discendente
VAL.TRE|Ord||Ascendente
VAL.OGG|Pag|*YES|Si
VAL.OGG|Com|Yes|Si
VAL.OGG|Ord|Des|Discendente
VAL.OGG|Ord||Ascendente


 :  : PRO.SER Cod="VAL.FLD.1" Tit="Valori. Di un campo di file" Fun="F(EXB;B£SER_84;VAL.FLD) 1(OJ;*FILE;-(O;;OJ*FILE;)) 2(Q3;;-( ;;Q3;)) P( Pag(-(F;;**;Carica Pag. Successiva)) NoPop(-(F;;V2SI/NO;No Popup Servizio)) Fld(-(F;;;Nome Campo)) Flt(-(F;;;Where aggiuntiva di filtro)) Com(-(F;;**;Emissione (???))) Ord(-(F;;**;Ordine)))"

 :  : PRO.SER Cod="VAL.FLD.2" Tit="Valori. Di un campo di file" Fun="F(REP;B£SER_84;VAL.FLD)" Ref="VAL.FLD.1"

 :  : PRO.SER Cod="VAL.FLD.3" Tit="Valori. Di un campo di file" Fun="F(EXC;B£SER_84;VAL.FLD)" Ref="VAL.FLD.1"

 :  : PRO.SER Cod="VAL.TRE.4" Tit="Valori. Di un campo di file (albero)" Fun="F(EXB;B£SER_84;VAL.TRE)" Ref="VAL.FLD.1"

 :  : PRO.SER Cod="VAL.TRE.5" Tit="Valori. Di un campo di file (albero)" Fun="F(REP;B£SER_84;VAL.TRE)" Ref="VAL.FLD.1"

 :  : PRO.SER Cod="VAL.TRE.6" Tit="Valori. Di un campo di file (albero)" Fun="F(EXC;B£SER_84;VAL.TRE)" Ref="VAL.FLD.1"

 :  : PRO.SER Cod="VAL.OGG.7" Tit="Valori. Di un oggetto" Fun="F(EXB;B£SER_84;VAL.OGG) 1(;;-(O;;;)) P( Pag(-(F;;**;Carica Pag. Successiva)) NoPop(-(F;;V2SI/NO;No Popup Servizio)) Fld(-(F;;;Nome Campo)) Flt(-(F;;;Where aggiuntiva di filtro)) Com(-(F;;**;Emissione (???))) Ord(-(F;;**;Ordine)))"

 :  : PRO.SER Cod="VAL.OGG.8" Tit="Valori. Di un oggetto" Fun="F(REP;B£SER_84;VAL.OGG)" Ref="VAL.OGG.7"

 :  : PRO.SER Cod="VAL.OGG.9" Tit="Valori. Di un oggetto" Fun="F(EXC;B£SER_84;VAL.OGG)" Ref="VAL.OGG.7"

 :  : PRO.SER Cod="GET.MEM.10" Tit="Ripresa. Dati in Memoria" Fun="F(EXB;B£SER_84;GET.MEM)"

