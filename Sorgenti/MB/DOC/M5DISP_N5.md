# Disponibilità libera
La disponibilità libera è un'informazione che viene ritornata dalla scansione disponibilità (£M5D) se impostato il flag £M5DDL (nel programma M5FUADI viene impostato sempre e la disponibilità libera è un campo sceglibile nello schema).
Per determinarla si considera l'andamento della disponibilità (nota; nello stesso giorno si assume la disponibilità finale di tutte le fonti quindi è indipendente dal loro ordinamento), la disponibilità libera è la parte crescente (se positiva) della curva della disponibilità, vale a dire è la qtà che in quella data è libera da impegni futuri (ascisse il tempo, ordinate la disponibilità).

![M5DISP_03](http://localhost:3000/immagini/M5DISP_N5/M5DISP_03.png)
Si può inoltre definire la disponibilità libera come fonte :  l'origine fonte è "DL" ed il parametro 1 contiene il gruppo fonti su cui si calcola la disponibilità libera :  la fonte è l'incremento giornaliero della disponibilità libera. Questa fonte può essere usata da sola nell'analisi evadibilità quando si imposta un articolo/quantità.

## Esempio
![M5DISP_04](http://localhost:3000/immagini/M5DISP_N5/M5DISP_04.png)
Se si sceglie solo la disponibilità libera come fonte, l'andamento della sua disponibilità conicide con la disponibilità libera de gruppo fonti su cui è stata calcolata.
