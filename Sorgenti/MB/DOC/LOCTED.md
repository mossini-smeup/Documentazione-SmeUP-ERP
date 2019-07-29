# Componente Ted

## Abstract

È un componente (non supportato da Looc.UP in quanto Looc.UP risolve solo la chiamata F(TED;;) ma non gestisce appunto G.SUB.TED come componente...) che permette all'utente di gestire contenuti in formato HTML. Il fatto che si tratti di contenuto HTML per l'utente è assolutamente trasparente, ma per lo sviluppatore è importante essere a conoscenza di questa caratteristica.

Allo stato dell'arte gestisce membri AS400 in cui appunto scrive e reperisce puro HTML.
Attualmente utilizza le medesime FUN (per lettura e salvataggio) del componente EDT.

Si tratta di un componente web di terze parte (Primefaces) integrato in Web.UP.

Dal punto di vista tecnico, in quanto componente (G.SUB.TED), può essere facilmente incluso in una sezione : 

  :  : G.SEZ Pos(1)
  :  : G.SUB.TED Tit="..."
  :  : D.FUN.STD F(TED;*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;*LIB;[libreria])

oppure richiamato dallo spotlight secondo la forma canonica : 

 F(TED;*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;*LIB;[libreria])


## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCTED_F01)
- [Menu e strumenti](Sorgenti/MB/DOC/LOCTED_F03)

## Formato dati
Tipo di XML utilizzato :  Xml con contenuto in CDATA. Il contenuto di CDATA è HTML

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.TED) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.TED))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;TED) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TED) 2(MB;SCP_SCH;WETEST_TED)) L(1)

# Documenti applicativi
 :  : DEC K(Esempi) D( Esempi con i Setup attualmente implementati) X(F(EXD;*SCO;) 2(MB;SCP_SCH;WETEST_TED)) L(1)
- [Struttura XML](Sorgenti/MB/DOC/LOCTED_XML)
 :  : DEC T(MB) P(DOC_OPE) K(LOCTED_SYX)
