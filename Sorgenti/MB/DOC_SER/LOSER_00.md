 :  : HEA RESP(GR) STAT(80)
# OBIETTIVO
Dimostrare alcune delle tematiche connesse alla realizzazione di un servizio.

# FUNZIONI/METODI
## ESETRE
Costruisce un albero di esempio. Se specificato il metodo LIV aggiunge ad ogni elemento dell'albero
 costituito da un elemento, con un esempio di azione associata.
## ESEMAT
Costruisce una matrice di esempio. Se specificato il metodo MET aggiunge un paio di righe.
## ESEGAU
Costruisce un cruscotto di esempio. Nel parametro VAL indica il valore da indicare, altrimenti ne fi
## ESESEM
Costruisce un semaforo di esempio. Nel parametro VAL indica il valore da indicare, altrimenti ne fis
## ESELAB
Costruisce una label di esempio, con un'azione associata.


NB :  gli oggetti passati nei parametri non servono, servono per esemplificare le modalità di passaggi

## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato
ESETR.LIV||Param 1|MDC5C6F0G           00010 O
ESETR.LIV||Param 2|MDM5FO01G           00010


 :  : PRO.SER Cod="ESETR.LIV.1" Tit="Esempio di albero. A 2 livelli con esempi di azioni" Fun="F(TRE;LOSER_00;ESETR.LIV) 1(OG;TS;-(O;;OGTS;)) P()"

 :  : PRO.SER Cod="ESEMA.2" Tit="Esempio di matrice. " Fun="F(EXB;LOSER_00;ESEMA) P( TDO(-(F;;TAV5D;Param 1)) CMA(-(F;;MG;Param 2)) TOG(-(F;;TAB£G;Param 3)) VAL(-(F;;**;Param 4)))"

 :  : PRO.SER Cod="ESEGA.3" Tit="Esempio di cruscotto. " Fun="F(EXB;LOSER_00;ESEGA) P( VAL(-(F;;NR;Valore)))"

 :  : PRO.SER Cod="ESESE.4" Tit="Esempio di semaforo. " Fun="F(EXB;LOSER_00;ESESE)" Ref="ESEGA.3"

 :  : PRO.SER Cod="ESELA.MET.5" Tit="Esempio di label. Metodo - aggiunge 2 righe" Fun="F(EXB;LOSER_00;ESELA.MET)"

