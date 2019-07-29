# WFS - Stati di avanzamento di un ordine
 :  : DEC T(ST) K(WFS)
## OBIETTIVI
Caratterizzare gli stati di avanzamento (stati "logici") di un ordine di workflow di un certo tipo.
Lo stato di avanzamento di un ordine è il valore del suo campo F2STAV; a differenza dello stato
tradizionale (F2STAT) non porta informazioni utili al motore di workflow ma può essere utilizzato
dall'implementatore di workflow per sintetizzare la progressione dell'ordine rispetto al suo
processo.
Questo può venire utile, ad esempio, nel colloquio tra workflow innestati (un workflow master vede
se un suo sottoworkflow è arrivato a un certo punto).

## SOTTOSETTORI
Gestiti

## CONTENUTO DEI CAMPI
