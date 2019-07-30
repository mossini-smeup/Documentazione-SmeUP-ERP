 :  : HEA RESP(LS) STAT(00)

# OBIETTIVO
Raccogliere tutte le funzioni che trattano le funzioni.

# FUNZIONI/METODI
Matrice dei periodi dato un elemento della tabella periodi.
 :  : PRO.SER Cod="00001" Fun="F(EXB;B£SER_49;OAV.FUN.01) 1(TA;PER;-(O;;;Periodo;A01;10))"
 :  : PRO.SER Cod="00002" Fun="F(EXB;B£SER_49;OAV.FUN.02) 1(TA;PER;-(O;;;Periodo)) 2(TA;BRE;-(O;;;Tipo Ente))"
 :  : PRO.SER Cod="00003" Tit="Caso 003" Fun="F(EXB;B£SER_49;OAV.FUN.03) P(Var001(-(O;;TAPER;Periodo)) Var002(-(F;;TAV5D;Tipo documento;DOC;10;A)) Var003(-(F;;TABRE;Tipo ente)))"
 :  : PRO.SER Fun="F(EXB;B£SER_49;OAV.FUN.04) 1(TA;PER;-(O;;;Periodo)) P(Var001(-(O;;TAPER;Per)) Var002(-(F;;TAV5D;Tipo)))" Cod="00004"
