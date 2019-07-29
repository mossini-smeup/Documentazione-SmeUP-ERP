# CQW - Valutazione controllo
 :  : DEC T(ST) K(CQW)
## OBIETTIVO
Definire le classi di valutazione per i punti controllati della GRIGLIA di RIFERIMENTO dell'AUDIT. Le classi di valutazione sono di tipo descrittivo, ad esse saranno poi associati dei valori numerici di riferimento.
## CONTENUTO DEI CAMPI
 :  : FLD T$VALP **Coeff. Valutazione**
Campo numerico. Associa ad una valutazione generica un peso, che entrerà nell'algoritmo di calcolo dell'indice dell'Audit.
 :  : FLD T$CANC **Caratteristica N.C.**
Questo campo può assumere il valore : 
' '  La descrizione della valutazione non corrisponde ad una caratteristica NON CONFORME.
'X'  La descrizione immessa corrisponde ad una caratteristica NON CONFORME.
 :  : FLD T$NEFF **Controllo non effettuato**
Questo campo può assumere il valore : 
' '  La descrizione della valutazione indica che tale punto della griglia di riferimento è stato valutato.
'X'  La descrizione immessa indica che il punto della griglia di riferimento NON è STATO VALUTATO, e quindi l'algoritmo di calcolo dell'indice di AUDIT non deve tener conto di tale punto.
