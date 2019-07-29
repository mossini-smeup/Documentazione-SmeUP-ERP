# Componenti (Molto ridotta)
 :  : I.INC.SER Fun="F(EXB;B£SER_02;COM.MAT)" Col="COMCOD|COMDES" Rig="2"
# Componenti (Meno ridotta)
 :  : I.INC.SER Fun="F(EXB;B£SER_02;COM.MAT)" Col="COMCOD|COMDES|COMA04|COMA02|COMA11|COMA03" Rig="99"
# Prime 20 righe della tabella CLS
 :  : I.INC.SER Fun="F(EXB;*TBL;) 1(TA;CLS;)" Rig="20"
# Parametri di connessione
 :  : I.INC.SER Fun="F(EXB;B£SER_01;CON.PRO)"
# Moduli dell'applicazione BR
 :  : I.INC.SER Fun="F(EXB;*APP;MOD.MAT) 1(TA;B£A;BR)"
# Oggetto V2SI/NO
 :  : I.INC.SER Fun="F(EXB;*TBL;) 1(V2;SI/NO;1)"
