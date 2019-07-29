# D5X - Gestione WIP
 :  : DEC T(ST) K(D5X)
## CONTENUTO_DEIcCAMPIne

 :  : FLD T$ELEM **Elemento**
Codice di 15 carattere diventa il codice in gestione D5COSO. E' lo scenario della gestione WIP

 :  : FLD T$DESC **Descrizione**
E' la descrizione dello scenario WIP

 :  : FLD T$D5X1 **Contesto costo**
E' il contesto per il recupero dei costi per fase.  Normalmente può assumere i valori 'OR' o 'AR' in funzione del fatto
che i costi "ALLA FASE" siano gestiti sull'ordine di produzione o sull'articolo.

 :  : FLD T$D5X2 **Tipo Costo**
E' il tipo costo da utilizzare per il calcolo del costo alla fase. Può essere un costo D5 (in questo caso deve essere
presente anche il tema per la gestione del costo alla fase), oppure un costo CS (in questo caso dovrà essere gestito
il costo della fase nel file COSARO0F)

 :  : FLD T$D5X3 **Livello Costo totale**
E' il livello del costo totale da utilizzare (necessario solo per i costi D5)

 :  : FLD T$D5X4 **Livello Costo Materiale**
E' il livello del costo Materiale da utilizzare (necessario solo per i costi D5)
