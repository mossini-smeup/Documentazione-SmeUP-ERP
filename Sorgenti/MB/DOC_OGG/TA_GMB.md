# GMB - Unità di movimentazione
## OBIETTIVO
Codifica e descrive le entità che hanno il compito contenere e movimentare i prodotti dell'azienda (materie prime, prodotti finiti, ecc.).
## CONTENUTO DEI CAMPI
 :  : FLD T$GMB1 __Lunghezza__
Dimensioni standard per l'unità.
 :  : FLD T$GMB2 __Larghezza__
Dimensioni standard per l'unità.
 :  : FLD T$GMB3 __Altezza/Volume__
Dimensioni standard per l'unità.
 :  : FLD T$GMBT __Tara__
Tara
 :  : FLD T$GMBN __Max. peso netto (KG)__
Max. peso netto (KG)
 :  : FLD T$GMBI __Identificativo vuoto__
Identificativo dell'unità di movimentazione a vuoto.
 :  : FLD T$GMBS __Fam.Un.Mov.superiore__
Unità di movimentazione superiore in cui è inclusa questa unità.
 :  : FLD T$GMBU __N° colli x Pallet__
Numero di elementi di questa unità, contenuti nell'unità superiore.
 :  : FLD T$GMBC __Tipo Identif. Collo__
Tipo identificativo collo (unità movimentazione piena).
 :  : FLD T$GMBA __Articolo associato__
Se l'unità è anche codificata come articolo (es. per gestire movimenti e giacenza di magazzino di contenitori), è possibile crearne l'associazione indicando l'articolo in questo campo (vedere anche relazioni con l'UNITÀ di MISURA attraverso esame della funzione £G32)
 :  : FLD T$GMBE __Tipo stampa-etichet__
Contiene il collegamento alla tabella gmp, indispensabile per la stampa di etichette
