# Componente Immagine

## Abstract

Componente utlizzato per visualizzare un'immagine, dato il suo tipo, parametro e codice.


## Funzionalità
- [Impostazioni grafiche](Sorgenti/MB/DOC/LOCIMG_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCIMG_F02)

## Introduzione
Il componente Immagine viene utilizzato per visualizzare immagini che possono risiedere sull'AS, utilizzando il componente J1PATHFILE, oppure reperibili su web utilizzando il componente J1URL.

## Formato dati
Tipo di XML utilizzato :  Xml ad albero (in questo caso di 1 solo nodo).

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.IMG))) L(1)

## Schede di esempio
Gli esempi del componente Immagine sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;IMG) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;IMG) 2(MB;SCP_SCH;WETEST_IMG)) L(1)
