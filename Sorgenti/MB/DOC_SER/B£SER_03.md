 :  : HEA RESP(BS) STAT(80) USAG(RM) DTAG(20061204)

# OBIETTIVO
Gestire le funzioni di base per i periodi.

# FUNZIONI/METODI
## MAT Matrice
### PER Periodi

Matrice dei periodi dato un elemento della tabella periodi.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.PER) 1(TA;PER-;-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi" Cod="00001"
E' possibile anche sfruttare il servizio con questa chiamata passando, anzichè le due date limite, due parametri (NPE REL) che definiscono numero periodi e relazione desiderata. In questo modo il servizio è in gradi di calcolare i periodi desiderati sfruttando la £PE8.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.PER) 1(TA;PER;-(O)) P(NPE(-(O;;NR;Numero periodi)) REL(-(O;;NR;Relazione tra periodi)))" Tit="Matrice dei periodi" Cod="00002"

Matrice dei periodi data una data.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.PER) 1(D8;-(O);-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi" Cod="00003"
Matrice dei periodi dato un elemento della tabella periodicità.
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.PER) 1(TA;A£Q;-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi" Cod="00004"

L'oggetto 2 è data limite iniziale.
L'oggetto 3 è data limite finale.


### ESE Periodi
Uguale al metodo precedente, ma include solo il tipo periodo "A".
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.ESE) 1(TA;PER-;-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi Annuali" Cod="00005"
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.ESE) 1(D8;-(O);-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi Annuali" Cod="00006"
 :  : PRO.SER Fun="F(EXB;B£SER_03;MAT.ESE) 1(TA;A£Q;-(O)) 2(D8;*YYMD;-) 3(D8;*YYMD;-)" Tit="Matrice dei periodi Annuali" Cod="00007"
## CON Contabilità
### TES Periodi
Albero dei periodi contabili di un contatto.
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.TES) 1(CN;-(O);-(O))" Tit="Matrice dei periodi Contabili di un contatto" Cod="00008"
Albero dei periodi contabili di un conto contabile.
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.TES) 1(TA;C5B;-(O))" Tit="Matrice dei periodi Contabili di un conto" Cod="00009"
Albero dei periodi contabili di un conto contabile.
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.TES) 1(CO;;-(O))" Tit="Matrice dei periodi Contabili di un conto" Cod="00010"
### PES Periodi/Mesi
Uguale al metodo precedente, ma esplode anche i mesi.
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.PES) 1(CN;-(O);-(O))" Tit="Matrice dei periodi Contabili di un contatto mensile" Cod="00011"
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.PES) 1(TA;C5B;-(O))" Tit="Matrice dei periodi Contabili di un conto mensile" Cod="00012"
 :  : PRO.SER Fun="F(EXB;B£SER_03;CON.PES) 1(CO;;-(O))" Tit="Matrice dei periodi Contabili di un conto mensile" Cod="00013"
