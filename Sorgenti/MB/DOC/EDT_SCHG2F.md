# Componente Lista Immagini

## Introduzione
Il componente Lista Immagini permette di definire all'interno di una sezione, una sottosezione che può contenere una serie di immagini.
Per questo tipo di subsezione è previsto un setup specifico G.SET.IML
Esse possono risiedere sull'AS oppure essere anche immagini prese dal web; per fare questo viene utilizzato il componente J1URL che si occupa di andare a reperirle attraverso il loro URL.
La disposizione viene gestita sia per riga che per colonna ed è possibile associare ad ognuna di esse un dinamismo.

## Formato dati
Tipo di XML utilizzato :  Xml ad albero.

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.IML))) L(1)

## Schede di esempio
Gli esempi del componente Lista Immagini sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;IML) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;IML) 2(MB;SCP_SCH;WETEST_IML)) L(1)
