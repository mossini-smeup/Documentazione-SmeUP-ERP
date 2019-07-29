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

