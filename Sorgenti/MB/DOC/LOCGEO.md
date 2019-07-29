# Componente Geo

## Abstract

Questo componente (GEO) rappresenta una mappa geografica, utilizza quella di google, sulla quale possiamo posizionare dei punti di interesse tramite SmeUP.
Il componente è utilizzabile solo da WebUP, da LoocUP vedremo solo una matrice.
Il componente GEO è molto utile nel caso si voglia inserire in una scheda di WebUP una posizione geografica, posizionato su una cartina.


## Funzionalità principali
- [Esporre i dati](Sorgenti/MB/DOC/LOCGEO_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCGEO_F05)

## Eventi gestiti
- Click :  il click su un punto qualsiasi della mappa riporta le coordinate corrispondenti al target
- markerselect :  il click su un marker riporta di dati del marker al target


## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.GEO))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;GEO) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;GEO) 2(MB;SCP_SCH;WETEST_GEO)) L(1)





