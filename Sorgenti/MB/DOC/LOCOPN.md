# Componente Opn

## Abstract

È un componente che permette di accedere ad una risorsa.

Le risorse possono essere ad esempio : 
 - numeri di telefono
 - indirizzi su una mappa
 - file
 - url

La risorsa è aperta con l'applicazione relativa, delegata cioè a gestire quella risorsa sul proprio dispositivo.
Ad esempio un OPN di un numero di telefono su un dispositivo mobile lancia l'applicazione delegata a gestire i numeri di telefono (il modulo telefono), impostando direttamente il numero da chiamare sulla
tastiera in maniera che sia pronto per la chiamata (o per l'invio di un messaggio).

Analogamente, se la funzione è eseguita su un oggetto riconosciuto come mail, verrà eseguita l'applicazione designata a gestire le mail (ad esempio il client di posta elettronica predefinito sul PC).

Verosimilente se la funzione è eseguita su un file remoto, verrà eseguita l'applicazione relativa e appositamente configurata e associata (browser per scaricare il file, lettore documenti pdf, lettore multimediale, ecc..).

## Funzionalità
- [Accedere ad una risorsa](Sorgenti/MB/DOC/LOCOPN_F01)

## Formato dati
Tipo di XML utilizzato :  Xml ad albero.

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.OPN))) L(1)

## Schede di esempio
Gli esempi del componente opn sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;OPN) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;OPN) 2(MB;SCP_SCH;WETEST_OPN)) L(1)

