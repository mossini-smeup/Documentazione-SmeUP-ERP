 :  : HEA RESP(LS) STAT(80)
# OBIETTIVO
Fornire funzioni relative al magazzino.

# FUNZIONI/METODI
## ARE
Restituisce una matrice con le giacenze per area/tipo giacenza

## ART
### GIA
Restituisce una matrice con le giacenze di un determinato articolo.
### MOV
Restituisce una matrice con i movimenti di un determinato articolo.
### GAM
Restituisce una matrice con gli articoli di un magazzino leggendoli dal GMQUAN, pertanto sono solo e tutti quelli con giacenza.

 :  : PRO.SER Cod="ARE.1" Tit="Giacenze per area/tipo. " Fun="F(EXB;GMSER_01;ARE) 1(TA;GMR;-(O;;TAGMR;Area)) 2(TA;GMQ;-(O;;TAGMQ;Tipo giacenza)) P( MAXEL(-(F;;NR;Massimo numero elementi)))"

 :  : PRO.SER Cod="ART.GIA.2" Tit="Articolo. Giacenze" Fun="F(EXB;GMSER_01;ART.GIA) 1(TA;MAG;-(O;;TAMAG;Magazzino)) 2(AR;;-(O;;AR;Articolo)) P( MAXEL(-(F;;NR;Massimo numero elementi)))"

 :  : PRO.SER Cod="ART.MOV.3" Tit="Articolo. Movimenti" Fun="F(EXB;GMSER_01;ART.MOV)" Ref="ART.GIA.2"

 :  : PRO.SER Cod="ART.GAM.4" Tit="Articolo. Articoli di un magazzino" Fun="F(EXB;GMSER_01;ART.GAM) 1(TA;MAG;-(O;;TAMAG;Magazzino)) 2(AR;;-(F;;AR;Articolo)) P()"

