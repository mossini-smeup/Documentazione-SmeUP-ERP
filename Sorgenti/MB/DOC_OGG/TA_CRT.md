# CRT - Modalità di trattamento fase
 :  : DEC T(ST) K(CRT)
## OBIETTIVO
Specifica un eventuale programma di controllo che dovrà precisare : 
-se la fase di collaudo per quel fornitore/articolo deve essere esclusa o meno.
-se la fase di collaudo per una particolare fase di lavoro deve essere esclusa o meno.
-nei casi precedenti, per quanto tempo dal ciclo di collaudo.
## CONTENUTO DEI CAMPI
 :  : FLD T$PRGC **Programma di controllo**
È il programma che gestirà la fase in questione decidendone la sua validità.
 :  : FLD T$FLAG **Esclusione Fase**
Se vi è una 'X' allora la fase di collaudo è esclusa  a prescindere dalla presenza del programma di controllo.
 :  : FLD T$PAR1 **Parametro_1**
Eventuali parametri utilizzabili dal programma di controllo.
