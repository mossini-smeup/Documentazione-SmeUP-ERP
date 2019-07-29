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

