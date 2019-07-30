 :  : HEA RESP(BS) STAT(80) USAG(RM) DTAG(20061204)

# OBIETTIVO
Gestire le funzioni di base per Lock/Autorizzazioni/Attributi/Tabelle

# FUNZIONI/METODI
## LIS Lista
### LCK Lock attivi
 :  : PRO.SER Cod="LISLCK" Tit="Lock Attivi" Txt="Matrice dei lock attivi." Fun="F(EXB;B£SER_01;LIS.LCK) 1(RE;K-;-(O;;REK-;Tipo lock))" Blo="1"

## AUA Autorizzazioni
### SIG significato di una classe
 :  : PRO.SER Cod="AUASIG" Tit="Significato" Txt="Albero dei significati data la classe e la funzione." Fun="F(TRE;B£SER_01;AUA.SIG) 1(TA;B£P;-(O;;TAB£P;Classe)) 2(**;;-(O;;**;Stringa))"

### ESI record esistenti per una classe
 :  : PRO.SER Cod="AUAESI" Tit="Autoriuzzazioni esistenti" Txt="Matrice dei record presenti data la classe,la funzione e l'utente." Fun="F(EXB;B£SER_01;AUA.ESI) 1(TA;B£P;-(O;;TAB£P;Classe)) 2(**;;-(F;;**;Stringa)) 3(UP;;-(F;&AM.UT;UP;Utente))"

## ATR Attributi
### LAB Label
 :  : PRO.SER Cod="ATRLAB" Tit="Label dei valori" Txt="Label del valore." Fun="F(TRE;B£SER_01;ATR.LAB) 1(;;-(O;;;Oggetto)) 2(OA;[T1][P1];-(O;;OA[T1][P1]))"

### TRE Albero
 :  : PRO.SER Cod="ATRTRE" Tit="Albero dei valori" Txt="Albero dei valori." Fun="F(TRE;B£SER_01;ATR.TRE)" Ref="ATRLAB"

## Tabelle
### COL Collegate
 :  : PRO.SER Cod="TABCOL" Tit="Albero tabelle collegate" Txt="Albero delle tabelle collegate ad un elemento." Fun="F(TRE;B£SER_01;TAB.COL)" Ref="ATRLAB"
