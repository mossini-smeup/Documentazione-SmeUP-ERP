 :  : HEA RESP(FD) STAT(80)
# OBIETTIVO
Fornire funzioni relative alle dichiarazioni d'intento.
# FUNZIONI/METODI
## DIC.DIN
La funzione ritorna una matrice contenente le informazioni presenti sul file BRDINT0F filtrate in base a : 
Ente(Azienda, cliente/fornitore, ente generico-TABRE-), Flag01(tipo registro), Periodo.
In Oggetto 1 viene passato l'oggetto che funge da filtro.
## DIN.DOC
La funzione ritorna una matrice contenente le informazioni relative all'applicazione dell'Iva su un documento, con specificata l'eventuale dichiarazione d'intento.

 :  : PRO.SER Cod="DIC.DIN.1" Tit=". " Fun="F(EXB;BRSER_04;DIC.DIN) 1(AZ;;-(O;;AZ;))"

 :  : PRO.SER Cod="DIN.DOC.2" Tit=". " Fun="F(EXB;BRSER_04;DIN.DOC) 1(DO;;-(O;;DO;))"

