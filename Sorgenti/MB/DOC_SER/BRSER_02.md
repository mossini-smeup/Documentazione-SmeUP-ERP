 :  : HEA RESP(GR) STAT(80)
# OBIETTIVO
Fornire funzioni relative alle distinte base.


# FUNZIONI/METODI
## DIB
Restituisce una distinta, effettuando una scansione con £DIB. Si possono opzionalmente indicare
fino a 5 OAV degli oggetti della distinta da restituire, se l'output è matrice.

 :  : PRO.SER Cod="DIB.1" Tit="Scansione distinta. " Fun="F(EXA;BRSER_02;DIB) P( FU(-(F;;**;Funzione)) ME(-(F;;**;Metodo)) IT(-(F;;TABRL;Tipo distinta)) IC(-(F;;**;Codice scansione)) LM(-(F;;NR;Livello massimo)) CG(-(F;;**;Configurazione)) O1(-(F;;**;Oav1)) O2(-(F;;**;Oav2)) O3(-(F;;**;Oav3)) O4(-(F;;**;Oav4)) O5(-(F;;**;Oav5)))"

 :  : PRO.SER Cod="DIB.2" Tit="Scansione distinta. " Fun="F(EXB;BRSER_02;DIB)" Ref="DIB.1"

 :  : PRO.SER Cod="DIB.3" Tit="Scansione distinta. " Fun="F(EXC;BRSER_02;DIB)" Ref="DIB.1"

 :  : PRO.SER Cod="DIB.4" Tit="Scansione distinta. " Fun="F(TRE;BRSER_02;DIB)" Ref="DIB.1"

