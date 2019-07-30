 :  : HEA RESP(GR) STAT(80)
# OBIETTIVO
Fornire un adattatore per rendere dinamici i sotto-componenti (semaforo, label, gauge...) della scheda.
Le chiamate standard (es. D.LAB.STD), infatti, vengono interpretate dal JATRE_18C al momento della creazione della
scheda :  è così impossibile utilizzare in esse variabili dinamiche.

# FUNZIONI/METODI
## GAU
Costruisce un cruscotto.
## SEM
Costruisce un semaforo.
## LAB
Costruisce una label.
## OGG
Costruisce un oggetto. È equivalente alla funzione LAB (mantenuta per compatibilità), produce un XML
- label
- bottoni
- immagini
- alberi monoelemento

# SCHEDE CONTENENTI ESEMPI DI CHIAMATE
 :  : DEC T(**) I(Componenti grafici) O(I) X({F(EXD;*SCO;) 2(MB;SCP_SCH;ESE1B) 4(;;GRA)}) O(I)
 :  : DEC T(**) I(Testi formattati) X({F(EXD;*SCO;) 2(MB;SCP_SCH;ESE1B) 4(;;TXT)}) O(I)

 :  : PRO.SER Cod="GAU.1" Tit="Cruscotto. " Fun="F(EXB;LOSER_02;GAU) P( MIN(-(F;;NR;Minimo)) SG1(-(F;;NR;Soglia 1)) SG2(-(F;;NR;Soglia 2)) MAX(-(F;;NR;Massimo)) VAL(-(F;;NR;Valore)) INV(-(F;;V2SI/NO;Inversione)))"

 :  : PRO.SER Cod="SEM.2" Tit="Semaforo. " Fun="F(EXB;LOSER_02;SEM) P( SG1(-(F;;NR;Soglia 1)) SG2(-(F;;NR;Soglia 2)) VAL(-(F;;NR;Valore)))"

 :  : PRO.SER Cod="LAB.3" Tit="Label. " Fun="F(EXB;LOSER_02;LAB) 1(**;;-(F;;**;Oggetto label)) P( TXT(-(F;;**;Testo)) FUN(-(F;;J1FUN;Funzione)))"

 :  : PRO.SER Cod="OGG.4" Tit="Oggetto. " Fun="F(EXB;LOSER_02;OGG)" Ref="LAB.3"

