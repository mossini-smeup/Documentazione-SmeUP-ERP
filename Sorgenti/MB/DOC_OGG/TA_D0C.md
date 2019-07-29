# D0C - Struttura aliquote
 :  : DEC T(ST) K(D0C)
## OBIETTIVO
La tabella permette di impostare l'utilizzo di un'aliquota nel calcolo e la memorizzazione del costo di una fase interna.
## CONTENUTO DEI CAMPI
 :  : FLD DC1,01
Identifica l'indice dell'elemento della schiera dei valori ritornati dalla scansione del ciclo che si vuole utilizzare.
 :  : FLD DC1,02.DC1,01
 :  : FLD DC1,03.DC1,01
 :  : FLD DC1,04.DC1,01
 :  : FLD DC1,05.DC1,01
 :  : FLD DC1,06.DC1,01
 :  : FLD DC2,01
Definisce l'elemento della struttura del costo nel quale il risultato deve essere sommato, nel caso il cui questo sia memorizzato al livello.
 :  : FLD DC2,02.DC2,01
 :  : FLD DC2,03.DC2,01
 :  : FLD DC2,04.DC2,01
 :  : FLD DC2,05.DC2,01
 :  : FLD DC2,06.DC2,01
 :  : FLD DC3,01
Definisce l'elemento della struttura del costo nel quale il risultato deve essere sommato, nel caso il cui questo sia memorizzato al livello inferiore.
 :  : FLD DC3,02.DC3,01
 :  : FLD DC3,03.DC3,01
 :  : FLD DC3,04.DC3,01
 :  : FLD DC3,05.DC3,01
 :  : FLD DC3,06.DC3,01
 :  : FLD DC4,01
Definisce il metodo di applicazione speciale. I codici eccezioni previsti sono : 
- "A" --> Attrezzaggio :  Il risultato viene diviso per la quantità del lotto standard.
 :  : FLD DC4,02.DC4,01
 :  : FLD DC4,03.DC4,01
 :  : FLD DC4,04.DC4,01
 :  : FLD DC4,05.DC4,01
 :  : FLD DC4,06.DC4,01
