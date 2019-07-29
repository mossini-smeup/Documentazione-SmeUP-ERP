# Componente Pgb

## Abstract

È un componente Web.UP (non supportato da Looc.UP) utilizzato per rappresentare graficamente un valore incluso in un intervallo di due valori.
Dati due valori di riferimento (min e max) ed un terzo che rappresenta il valore da visualizzare, la progressbar mostra un effetto grafico di "riempimento" fino al valore in questione,
mostrando immediatamente a colpo d'occhio quanto dista dal valore minimo e dal valore massimo il valore da prendere in considerazione.
Si usa spesso per rappresentare valori percentuali e per dare un effetto immediato della relazione tra un valore ed i relativi minimi/massimi stabiliti.
È possibile variarne la colorazione (da zero fino al valore raggiunto), e indicare l'unità di misura a piacimento (lt, %, ecc.).


## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCPGB_F01)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice (righe-colonne)

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.PGB))) L(1)

## Schede di esempio
Gli esempi del componente pgb sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;PGB) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;PGB) 2(MB;SCP_SCH;WETEST_PGB)) L(1)

