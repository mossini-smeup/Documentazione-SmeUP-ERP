# Componente Treemap

## Abstract

Il treemap e' un componente che permette di rappresentare, sotto forma di grafico, i dati contenuti in una struttura ad albero.
Ciascun nodo dell'albero viene rappresenzato da un rettango, la cui grandezza e colore sono definiti dal valore associato a quel nodo. La grandezza ed il colore sono calcolati in base ai valori degli altri nodi del grafico.


## Funzionalità
- [Personalizzazioni grafiche](Sorgenti/MB/DOC/LOCTMP_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCTMP_F02)
- [Rappresentazione dati](Sorgenti/MB/DOC/LOCTMP_F03)

Il treemap e' un componente che permette di rappresentare, sotto forma di grafico, i dati contenuti in una struttura ad albero.
Ciascun nodo dell'albero viene rappresenzato da un rettango, la cui grandezza e colore sono definiti dal valore associato a quel nodo. La grandezza ed il colore sono calcolati in base ai valori degli altri nodi del grafico.
I nodi dell'albero possono avere 0 o piu' figli.

## Formato dei dati
Questo componente viene alimentato da un xml di tipo albero.
Nella griglia e' necessario specificare due colonne numeriche :  una rappresenta il valore, mentre l'altra il colore.

## Esempio di XML dei dati
<Griglia>
  <Colonna Cod="VAL" Txt="Valore" Tip="" Lun="50" IO="B" Ogg="NR" />
  <Colonna Cod="COL" Txt="Colore" Tip="" Lun="50" IO="B" Ogg="NR" />
</Griglia>
<Oggetto Nome="" Tipo="" Parametro="" Codice="Globale" Testo="" Fld="0|0" Leaf="">
  <Oggetto Nome="" Tipo="" Parametro="" Codice="America" Testo="" Fld="0|0" Leaf="">
    <Oggetto Nome="" Tipo="" Parametro="" Codice="Brazil" Testo="" Fld="11|10" Leaf="" />
    <Oggetto Nome="" Tipo="" Parametro="" Codice="USA" Testo="" Fld="52|31" Leaf="" />
    <Oggetto Nome="" Tipo="" Parametro="" Codice="Mexico" Testo="" Fld="24|12" Leaf="" />
    <Oggetto Nome="" Tipo="" Parametro="" Codice="Canada" Testo="" Fld="16|-23" Leaf="" />
  </Oggetto>

  [...]
</Oggetto>

## Dinamismi
Quando si preme su un elemento del grafico, vengono lanciati i seguenti dinamismi :  Click, DblClick e Change.
A ciascun dinamismo vengono associate le variabili dell'elemento cliccato, piu' quelle della riga ad esso associata.

## Schede di esempio
Scheda d'esempio, esclusiva per WebUP

 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TMP) 2(MB;SCP_SCH;WETEST_TMP)) L(1)
