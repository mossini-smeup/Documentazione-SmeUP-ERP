# Componente Box

## Abstract
I dati che compongono il componente box sono strutturati esattamente come sono strutturati nel componente matrice, la differenza sta nel fatto che la visualizzazione dei dati non è vincolata ad un formato strettamente tabellare :  l'area del box può essere suddivisa in sezioni, il che rende questo componente molto flessibile.
Il comportamento di questo componente è simile a quello di una scheda, l'area in cui vengono esposti i dati può essere sezionata a seconda delle necessità.

## Funzionalità principali
- [Esporre i dati](Sorgenti/MB/DOC/LOCBOX_F01)
- [Ordinare](Sorgenti/MB/DOC/LOCBOX_F02)
- [Stile delle sezioni](Sorgenti/MB/DOC/LOCBOX_F03)
- [Lavorare con gli oggetti](Sorgenti/MB/DOC/LOCBOX_F04)
- [Dinamismi](Sorgenti/MB/DOC/LOCBOX_F05)
- [Filtrare](Sorgenti/MB/DOC/LOCBOX_F06)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Dinamismi
Il componente box gestisce i seguenti dinamismi : 
  - BtnClick :  quando viene premuto un bottone all'interno del box
  - Click :  quando viene cliccato un box
  - ChangeRow :  quando viene cliccato un box
  - Change :  quando viene cliccato un box

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.BOX))) L(1)

## Schede di esempio
Gli esempi del componente box sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;BOX) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;BOX) 2(MB;SCP_SCH;WETEST_BOX)) L(1)
