## Impegno provvisorio
>Se l'origine è IR (impegno provvisorio)
Parametro 1 : 
-    Pos.1/1   Tipo impegno considerato
.              ' '  tutti gli impegni (sia '1' sia '2');
.              '1'  consumi su disponibilità esistente;
.              '2'  nuovi impegni;
.              '3'  disponibilità prodotta (per effetto della lottizzazione).
.              NB :  le scelte '1' e '2' sono impegni, la scelta '3' è una copertura.
.              Bisogna tenerne conto nell'impostazione di questa fonte.
-    Pos.2/2   Tipo provvisorio
.              ' '  Impegno provvisorio "confermato";
.              '1'  Impegno provvisorio "provvisorio".
.              NB :  Gli impegni provvisori del primo tipo sono quelli che vengono
.              confermati dopo l'esecuzione dell'ATP, mentre i secondi sono gli
.              impegni che vengono creati durante l'esecuzione dell'ATP.
.              Tecnicamente, i primi contengono nel campo I£NSES del file M5IMPE0F
.              il valore BLANK, mentre i secondi contengono il nome del terminale.
.              Gli impegni "provvisori" devono essere utilizzati per permettere al
.              calcolo ATP di considerare il consumo 'precedente', quando lo stesso
.              articolo compare più volte nella distinta. In questo caso, nel gruppo
.              fonti usato nell'ATP dovrà essere aggiunta una fonte di impegno con
.              questo flag impostato a '1'.

