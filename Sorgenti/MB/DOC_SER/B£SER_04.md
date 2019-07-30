 :  : HEA RESP(BS) STAT(10) USAG(RM) DTAG(20061204)

# OBIETTIVO
Gestire le funzioni di base per le tabelle.

# FUNZIONI/METODI

## MOD Modello
### MAT Matrice
??? Matrice degli elementi di una tabella di un modello.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MOD.MAT) 1(OG;TA;-(O))" Cod="00001"
 :  : PRO.SER Fun="F(EXB;B£SER_03;MOD.MAT) 1(ST;;-(O))" Cod="00002"
### ELE Elementi
??? Matrice degli elementi di una tabella di un modello.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MOD.ELE) 1(OG;TA;-(O))" Cod="00003"
 :  : PRO.SER Fun="F(EXB;B£SER_03;MOD.ELE) 1(ST;;-(O))" Cod="00004"
### LIV Livello
??? Albero degli elementi.
### IMP Impostazioni
??? Salvataggio impostazioni.
 :  : PRO.SER Fun="F(FBK;B£SER_03;MOD.IMP) 1(OG;TA;-(O))" Cod="00005"
 :  : PRO.SER Fun="F(FBK;B£SER_03;MOD.IMP) 1(ST;;-(O))" Cod="00006"

## *CN Tabella *CN
### AAP Azioni
???Matrice dei programmi.
 :  : PRO.SER Fun="F(EXB;B£SER_03;*CN.AAP) 1(TA;*CNAA;-(O))" Cod="00007"
