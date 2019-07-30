 :  : HEA RESP(RM) STAT(00)

# OBIETTIVO
Gestire le funzioni di lista per oggetto.
Interfaccia api £H40 per LOOC.up.

# FUNZIONI/METODI

## Lista (LIS)
### delle liste (LIS)
Costruisce una matrice delle liste presenti per l'oggetto.
 :  : PRO.SER Fun="F(EXB;B£SER_40;LIS.LIS) 1(LI;-(O);-)" Cod="00001"

### degli elementi (ELE)
Costruisce una matrice degli elementi contenuti nella lista.
 :  : PRO.SER Fun="F(EXB;B£SER_40;LIS.ELE) 1(LI;-(O);-(O))" Cod="00002"

## Aggiunta (ADD)
### Elemento in lista (ELE)
Aggiunge un elemento alla lista e presenta la scheda della lista posizionata sull'elemento.
 :  : PRO.SER Fun="F(EXD;B£SER_40;ADD.ELE) 1(LI;-(O);-(O)) 2(-(O);-;-(O))" Cod="00003"

## Pulizia (CLR)
Svuota la lista.
 :  : PRO.SER Fun="F(FBK;B£SER_40;CLR) 1(LI;-(O);-(O))" Cod="00004"

## Importazione elementi (IMP)
### Elementi da £G40 (G40)
Importa la lista o gli elementi di una lista da £G40.
 :  : PRO.SER Fun="F(FBK;B£SER_40;IMP.G40) 1(LI;-(O);-(O))" Cod="00005"

 :  : SEZ
LIS            Lista          N
.LIS.LIS        Liste         N
.LIS.ELE        Elementi      N

 :  : RIG
LIS.LIS
.DIN     Includi dinamiche              V2SI/NO                 001
LIS.ELE
.SCH     Schema                         Q2                      015
IMP.G40
.G40     Codice £G40                    **                      015
.TIM     Tipo importazione              .VTIM                   001

 :  : LIS
TIM
.               Pulisci lista
.1              Accoda elementi
