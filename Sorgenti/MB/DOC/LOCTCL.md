# Componente Tag Cloud (TCL)
## Abstract

Il componente TagCloud permette di renderizzare una nuvola di etichette (tag cloud), una forma di visualizzazione di dati che mostra un gruppo di etichette di grandezza differente, la quale viene utilizzata spesso per rappresentare gli argomenti più trattati all'interno di un sito web. Le voci sono generalmente associate a link che portano alle pagine collegati a quell'argomento. Le tag cloud sono infatti spesso usate come strumenti di navigazione.

In Sme.UP il componente TagCloud recupera i dati da una matrice. Esso opera su due colonne definibili nel setup, la colonna da cui ricavare le label e la colonna di pesi di tipo numerico da cui ricavare la dimensione del tag. La dimensione del tag (denominata strenght) potrà essere un valore da 1 a 5 (su parametro di setup è ammessa anche la classe speciale 0). Per approfondimenti sulle modalità di trasformazione dei pesi in strenght vedere la sezione sugli algoritmi.

## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCTCL_F01)
- [Impostare l&-x27;algoritmo di calcolo](Sorgenti/MB/DOC/LOCTCL_F02)
- [Impostare limiti e soglie](Sorgenti/MB/DOC/LOCTCL_F03)
- [Dinamismi](Sorgenti/MB/DOC/LOCTCL_F04)
- [Dimensioni](Sorgenti/MB/DOC/LOCTCL_F05)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice (righe-colonne)

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.TCL))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili sulla sezione specifica per il web : 

 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TCL) 2(MB;SCP_SCH;WETEST_TCL)) L(1)
