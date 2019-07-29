# Componente Edt

## Abstract

È un componente (non supportato da Looc.UP in quanto Looc.UP risolve solo la chiamata F(EDT;;) ma non gestisce appunto G.SUB.EDT come componente...) che permette all'utente di gestire il contenuto di membri (script) su AS400 tramite interfaccia Web.UP.
Di fatto è l'alternativa Web.UP al wizard (editor) di Looc.UP.

Si tratta di un componente web di terze parte (codemirror.net) esteso ed integrato in Web.UP per implementare le funzionalità richieste da Sme.UP, al fine di sostituire gradualmente l'editor (Wizard) di Looc.UP fornendo anche nuove funzionalità all'utilizzatore.
Ad oggi copre parzialmente le funzionalità dell'editor client di Looc.UP, ma gli sviluppi e gli sforzi hanno l'obiettivo di renderlo l'editor principale da utilizzare con Sme.UP.

Dal punto di vista tecnico, in quanto componente (G.SUB.EDT), può essere facilmente incluso in una sezione : 

  :  : G.SEZ Pos(1)
  :  : G.SUB.EDT Tit="..."
  :  : D.FUN.STD F(EDT;*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;*LIB;[libreria])

oppure richiamato dallo spotlight secondo la forma canonica : 

 F(EDT;*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;*LIB;[libreria])


## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCEDT_F01)
- [Autocompletamento e suggerimenti](Sorgenti/MB/DOC/LOCEDT_F02)
- [Menu e strumenti](Sorgenti/MB/DOC/LOCEDT_F03)

## Formato dati
Tipo di XML utilizzato :  Xml con contenuto in CDATA

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.EDT))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;EDT) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;EDT) 2(MB;SCP_SCH;WETEST_EDT)) L(1)

# Documenti applicativi
 :  : DEC K(Esempi) D( Esempi con i Setup attualmente implementati) X(F(EXD;*SCO;) 2(MB;SCP_SCH;WETEST_EDT)) L(1)
- [Struttura XML](Sorgenti/MB/DOC/LOCEDT_XML)
 :  : DEC T(MB) P(DOC_OPE) K(LOCEDT_SYX)
