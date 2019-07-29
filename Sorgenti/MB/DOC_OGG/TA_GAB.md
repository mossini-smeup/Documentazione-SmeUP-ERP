# GAB - Buyer - richieste di acquisto
## OBIETTIVO
Creare un archivio in cui verrano indicati i Buyer.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
Codice del Buyer .
 :  : FLD T$DESC Descrizione
Descrizione del Buyer .
 :  : FLD T$GABC __Capo Buyer__
Elemento della tabella GAB che indica se il Buyer che si sta definedo ha un capo Buyer ed in tal caso chi è.
Esempio  : 
Capo Buyer A -------->  A1    N.B. Capo XX
!                   Subordinati XXnnnn
+----->  A2
Quando definisco A  il capo Buyer è A
Quando definisco A1 il capo Buyer è A
Quando definisco A2 il capo Buyer è A
