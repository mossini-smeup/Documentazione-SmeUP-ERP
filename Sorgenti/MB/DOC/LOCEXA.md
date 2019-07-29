# Componente grafico

## Abstract

E' utilizzato per disegnare un grafico, utilizzando dei dati in formato griglia.

## Funzionalità
- [Tipo di grafico](Sorgenti/MB/DOC/LOCEXA_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCEXA_F02)
- [Grafica](Sorgenti/MB/DOC/LOCEXA_F03)
- [Esportazione](Sorgenti/MB/DOC/LOCEXA_F04)
- [Visualizzazione dati](Sorgenti/MB/DOC/LOCEXA_F05)

Il componente grafico permette una rappresentazione simbolica dei dati, rendendoli facilmente consultabili.
Esistono vari tipi di grafici :  barre (orizzontali o verticali), torta, linee, etc... In futuro verranno elencati tutti i tipi di grafici che e' possibile utilizzare.

## Formato dei dati
Questo componente viene alimentato da un xml di tipo matrice.

Nella definizione delle colonne e' possibile specificare se una colonna appartiente all'asse o alla serie, aggiungento l'attributo Fill="ASSE" / Fill="SERIE".
In alternativa, questo comportamento e' possibile specificarlo nel setup del componente, tramite gli attributi di setup Series="COL1|COL2|..." e Axe="COL".

## Dinamismi
Quando si clicca su un elemento di un grafico, vengono lanciati i dinamismi 'Click' e 'DblClick'.
Al dinamismo vengono aggiunte tutte le variabili relative alla riga associata all'elemento cliccato.

## Schede di esempio
Gli esempi del componente exa sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;EXA) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;EXA) 2(MB;SCP_SCH;WETEST_EXA)) L(1)
