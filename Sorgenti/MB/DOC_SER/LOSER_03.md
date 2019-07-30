 :  : HEA RESP(GR) STAT(80) USAG(GR) DTAG(20050909) ORAG(113200)
# OBIETTIVO
Fornire un'analisi complessiva sullo stato di compilazione ed assegnazione di schede standard/servizi.

# FUNZIONI/METODI
## SCH
Restituisce una matrice contenente informazioni sulle schede compilate (solo in SMEDEV per ora).

## RES.OG
Restituisce una matrice contenente i responsabili dell'oggetto passato come oggetto 1.

## RES.LIS
Restituisce una matrice contenente i responsabili degli oggetti derivanti dalla lista passata come oggetto 1.

## SER
Restituisce una matrice contenente informazioni sulla documentazione dei servizi.

 :  : PRO.SER Cod="SCH.1" Tit="Schede compilate. " Fun="F(EXB;LOSER_03;SCH)"

 :  : PRO.SER Cod="SCH.P.2" Tit="Pianificazione schede. " Fun="F(EXB;LOSER_03;SCH.P)"

 :  : PRO.SER Cod="SER.3" Tit="Servizi. " Fun="F(EXB;LOSER_03;SER)"

