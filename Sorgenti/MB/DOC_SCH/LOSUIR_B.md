### UTILIZZO SETUP E DINAMISMI

In queste schede viene evidenziata, per tutte le modalità grafiche previste (attributo UirMGr), la possibilità settare anche setup e dinamismi.

### NOTE OPERATIVE

Per avere questa possibilità è sufficiente indicare semplicemente ad di sotto della subsezione interessata le normali istruzioni G.DIN e G.SET.xxx.

Va in particolar modo considerato che se viene indicata una variabile di loocup questa verrà presa in considerazione solo dopo che la funzione di esecuzione si sarà conclusa (in modo da poter sfruttare le variabili contestuali della funzione).

 :  : PAR F(04) L(MON)
- Definizione della sezione e della subsezione
G.SEZ Pos(1)
G.SUB.UCF Tit="*NONE"
G.SET.UCF UirTRe="LOA08/E" UirCtx="M_LOSUIR" UirMGr="&PA.MGr" UirTiF="Elenco Moduli" UirTit="Interrogazione Moduli"
- Setup aggiuntivi
G.SET.MAT DftGroup="OG_J_T02_I_OG_J_T02_C_D" Parent="A01"  Name="Per Applicazione"  AutoFit="No" Formulas=";Descrizione MODULI APPLICAZIONI;ATT(Cos\OG\**;DEC;);;;|CALC0;CALC0;ATT(Cos\OG\OA;TAB£AMO;J/T02);15;0;O|CALC0;CALC0;ATT(Cos\OG_J_T02\**;C_D);35;0;O" Columns="$OP|OG|OG_"
G.SET.MAT DftSort="OG" Parent="A01"  Desc="Per Codice" Columns="$OP|ID_LI|OG_" Formulas=";Descrizione MODULI APPLICAZIONI;ATT(Cos\OG\**;DEC;);;;"
G.SET.MAT DftSort="OG_" Parent="A01"  Desc="Per Descrizione" Columns="$OP|ID_LI|OG_" Formulas=";Descrizione MODULI APPLICAZIONI;ATT(Cos\OG\**;DEC;);;;"
- Dinamismi aggiuntivi
G.DIN When="Change"
G.DIN When="Click" Exec="F(EXD;*SCO;) 1(TA;B£AMO;[ID_LI])" Enabled="{'[Column]' EQ '$OP'}"
- Funzione
D.FUN.UCF F(EXB;LOA10_SE;ELE) 1(LI;TAB£AMO;$IN.K1) P(RPa(2000) SchFx(T/OGG) Opz(000101) NTit(1))


### NOTE SU ESEMPI

Per tutti gli esempi proposti viene sempre eseguita la medesima funzione :  una lista di moduli a cui vengono applicate dei setup di matrice specifici ed il dinamismo che permette al click del bottone riportato sull'estrema sinistra di lanciare la scheda del modulo interessato.


