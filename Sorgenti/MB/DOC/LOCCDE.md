# Componente Cde

## Abstract

È un componente utilizzato per visualizzare codice sorgente di diverse tipologie, come ad esempio javascript, json, sorgenti AS400.

La porzione di codice sottostante mostra il contenuto di un membro sorgente AS400 : 

  :  : G.SEZ Pos(1)
  :  : G.SUB.CDE Tit="*NONE"
  :  : G.SET.CDE Mode="html"
  :  : D.FUN.STD F(HTM;B£SER_22;DOC.CON) 1(MB;[file];[membro]) P(Typ(HTML) Met(RIT))


## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCCDE_F01)

## Formato dati
Tipo di XML utilizzato :  Xml con contenuto in CDATA

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.CDE))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;CDE) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;CDE) 2(MB;SCP_SCH;WETEST_CDE)) L(1)

# Documenti applicativi
 :  : DEC K(Esempi) D( Esempi con i Setup attualmente implementati) X(F(EXD;*SCO;) 2(MB;SCP_SCH;WETEST_CDE)) L(1)
- [Struttura XML](Sorgenti/MB/DOC/LOCCDE_XML)
 :  : DEC T(MB) P(DOC_OPE) K(LOCCDE_SYX)
