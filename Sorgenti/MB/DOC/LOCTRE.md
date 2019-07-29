# Componente Albero

## Abstract

Il componente Albero è una componente utile per visualizzare informazioni in modo gerarchico. Ogni nodo dell'albero rappresenta un oggetto che può essere ramo (padre di altri nodi) oppure una foglia.
Per ogni nodo dell'albero è possibile anche dichiarare informazioni aggiuntive, che possono essere mostrate attraverso una griglia associata all'albero (vedi albero con griglia).
Nell'albero è anche possibile definire se e quali icone vedere per ogni nodo e se è possibile filtrarlo oppure no, così come se mostrarlo espanso o collassato.
L'albero possiede anche la proprietà (abilitabile attraverso un setup) di essere dinamico e non avere quindi i nodi precalcolati. I nodi figli vengono richiesti al sistema all'espansione del nodo padre.

Questo componente dovrebbe essere utilizzato principalmente per : 
- organizzare le informazioni gerarchicamente.
- mostrare grandi quantità di dati in modo facilmente consultabile.
- gestire menù di opzioni/selezioni.

Ogni menù presente del sistema è realizzato tramite l'uso del componente albero (o accordion e albero).


## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCTRE_F01)
- [Stile](Sorgenti/MB/DOC/LOCTRE_F02)
- [Espansione albero](Sorgenti/MB/DOC/LOCTRE_F03)
- [Dinamismi](Sorgenti/MB/DOC/LOCTRE_F04)

## Formato dati
Tipo di XML utilizzato :  Xml ad albero.

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Click :  scatta al click su un elemento dell'albero
- Doubleclick :  in Loocup scatta al doppio click su un ekemento dell'albero
- Change :  scatta alla selezione di un elemento
- Drop :  scatta al drop su una elemento dell'albero
- Expand :  scatta quando viene espanso un nodo dell'albero

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.TRE))) L(1)

## Schede di esempio
Gli esempi del componente accordion sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;TRE) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TRE) 2(MB;SCP_SCH;WETEST_TRE)) L(1)

## Altre risorse
- [Creazione XML di un albero](Sorgenti/MB/DOC/LOCTRE_01)
- [Variabili gestite da un albero](Sorgenti/MB/DOC/LOCTRE_02)
- [Funzioni Varie](Sorgenti/MB/DOC/LOCTRE_03)
- [Utilizzo dell&-x27;Albero su Device Mobile](Sorgenti/MB/DOC/LOCTRE_MO)
