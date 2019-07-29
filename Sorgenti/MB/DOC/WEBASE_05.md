# Configurazione menu Web.UP

Questa funzionalità di Web.UP consente, una volta effettuato il login, di avere un menu che comparirà sulla sinistra con il quale possiamo navigare più facilmente all' interno di Web.UP.
Questo menù è estremamente personabizzabile da parte dell'utente, con peculiartità specifiche per la parte web e per la parte mobile.

# Come aprire il modulo di configurazione?

Per raggiungere il modulo di cofigurazione del menù di Web.UP bisogna andare sulla pagina di avvio di Web.UP, ad esempio per noi "webuptest.smeup.com", poi attivare la modialità sviluppatore.
A questo punto cliccare sul modulo *main config, e selezionare la seconda voce ERP vs B2B settings.
Ora scendendo fino al punto dove troviamo external menù, qui possiamo andare a personalizzare il nostro menù di Web.UP.

# Personalizzazioni

Adesso andiamo a personalizzare a nostro piacimento il menù :  con le prime due voci fleggate (External Web menu enabled, External Mobile menu enabled), indichiamo a web.UP di mostrarci il menù, in caso contrario il menù di Web.UP sarà disattivo e quindi non utilizzabile.
Con la terza voce fleggata (Force external menu collapse on click), andiamo a indicare a Web.UP che quando premiamo un tasto del menù, questo subito dopo andrà in modalità nascosta. Sarà possibile aprire nuovamente il menù cliccando sul pulsante in altro a sinistra
con le tre linee parallele.
Subito dopo troviamo due campi di immissione (Fixed start menu (WEB), Fixed start menu (MOB)), nella prima andiamo a configurare soltanto la parte web, mentre nella seconda andremo a configurare soltanto la parte mobile, quindi se vogliamo avere lo stesso menu sia in web che in mobile dovremmo inserire la FUN in entrambe i campi.
  in questi due campi abbiamo 3 possibili soluzioni di immissione : 

      1 - true :  inserendo la parola true andiamo ad indicare a web.UP che il menù che aprirà sarà con una FUN cablata all'interno del codice di web.UP
           Le FUN che vengono generate quando abbiamo abilitato la modalità TRUE sono : 
WEB :        F(TRE;*MNU;) 1(IU;;) 6(;WU3_01;0010) SS(CONAP(X1))
MOBILE :   F(TRE;JATRE_06C;NEW)

      2 - false :  inserendo la parola false utilizziamo un menù che apre una FUN cablata all'interno dello script di configurazione della scheda
            Le FUN che vengono generate quando abbiamo abilitato la modalità FALSE sono : 
WEB :        F(TRE;LOA12_SE;MNU.TRE) 1(CN;COL;SANCOS) P(MN(WEDEMO_001)) SS(CONAP(X1))
MOBILE :   F(TRE;LOA12_SE;MNU.TRE) 1(CN;COL;SANCOS) P(MN(WEDEMO_001)) SS(CONAP(X1))

      3 - la terza possibilità e quella di inserire una FUN che decidiamo noi, per utilizzare un menù completamente personalizzato da parte dell'utente finale.
Il quarto campo che troviamo consente, se fleggato, che all'avvio di web.UP il menù partirà in modalità nascosta (molto utile nel caso si vogliano mostrare cruscotti all'avvio di web.UP). Per poter utilizzare il menù sarà sufficiente premere il tasto in alto a sinistra con le tre linee parallele.



