 :  : HEA RESP(CM) STAT(10)
# OBIETTIVO
Questo servizio gestisce la manutenzione in scheda di membri.

# SCHEDA DI ESEMPIO
La scheda dove sono esplicitate le funzionalità del servizio è la scheda del modulo A£DEMO

# FUNZIONI/METODI
 :  : PRO.SER Cod="GES.NEW" Tit="Nuovo membro" Fun="F(EXD;B£SER_58;GES.NEWSCH) 1(MB;SCP_SCH;) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEW) 1(MB;SCP_SCH;) ))"
 :  : PRO.SER Cod="GES.NEW" Tit="Nuovo membro (propone lib)" Fun="F(EXD;B£SER_58;GES.NEWSCH) 1(MB;SCP_SCH;) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEW) 1(MB;SCP_SCH;) P(Lib(W_PARFR)) ))"
 :  : PRO.SER Cod="GES.NEW" Tit="Nuovo membro (propone lib, membro)" Fun="F(EXD;B£SER_58;GES.NEWSCH) 1(MB;SCP_SCH;TSTMB) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEW) 1(MB;SCP_SCH;TSTMB) P(Lib(W_PARFR)) ))"
 :  : PRO.SER Cod="GES.NEWLIB" Tit="Crea lib" Fun="F(INT;B£SER_58;GES.NEWLIB) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEWLIB)))"
 :  : PRO.SER Cod="GES.NEWLIB" Tit="Crea lib (propone)" Fun="F(INT;B£SER_58;GES.NEWLIB) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEWLIB) P(Lib(TSTLIB))))"
 :  : PRO.SER Cod="GES.CHGLIB" Tit="Modifica lib" Fun="F(INT;B£SER_58;GES.CHGLIB) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.CHGLIB)))"
 :  : PRO.SER Cod="GES.CHGLIB" Tit="Modifica lib (propone)" Fun="F(INT;B£SER_58;GES.CHGLIB) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.CHGLIB) P(Lib(TSTLIB))))"
 :  : PRO.SER Cod="GES.NEWOBJ" Tit="Crea obj" Fun="F(INT;B£SER_58;GES.NEWOBJ) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEWOBJ)))"
 :  : PRO.SER Cod="GES.NEWOBJ" Tit="Crea obj (propone lib)" Fun="F(INT;B£SER_58;GES.NEWOBJ) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEWOBJ))) P(Lib(TSTLIB))))"
 :  : PRO.SER Cod="GES.NEWOBJ" Tit="Crea obj (propone lib e obj)" Fun="F(INT;B£SER_58;GES.NEWOBJ) SP(Mod(F) Show(Yes) Edit(Yes) Fun(A(EMU;B£WSYS_SP;GES.NEWOBJ))) 1(OJ;TSTFILE) P(Lib(TSTLIB))))"

Metodi che il servizio espone : 
* LIS.LIB (Lista librerie)
* LIS.OBJ (Lista oggetti)
* LET.GRA (Lettura documentazione della grammatica)
* LET.SCP (Lettura contenuto dello script)
* EXB.SCP (Matrice dei tag dello script)
* TRE.SCP (Albero dei tag dello script)
* TRE.REL (Albero delle relazioni del tag)
* IMG.REL (Immagini delle relazioni del tag)
* GES.CON (Gestione consistenza)
* GES.TAG (Aggiunge tag)
* GES.AZI (Esegue azione)
* GES.NEWLIB (Nuova libreria)
* GES.NEWOBJ (Nuovo oggetto)
* GES.NEW (Nuovo script)
* CHG.LIB (Modifica libreria)
* CHG.OBJ (Modifica oggetto)
* CHG (Modifica script)
* DEL.LIB (Elimina libreria)
* DEL.OBJ (Elimina oggetto)
* DEL (Elimina script)
* TAG.VER (Sviluppo di un tag in verticale)
* TAG.NOTAG (Aggiorna nota)
* TAG.NOT (Nota)

# PROTOTIPI
