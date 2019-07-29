# B§B - Corrispondenze * conversione
 :  : DEC T(ST) K(B§B)
## Sottosettore
Il sottosettore contiene il tipo oggetto da convertire (es AR nel caso si tratti di conversione di articoli). Il sottosettore può essere bianco nel caso la conversione avvenga da u n file ad una o piu tabelle.
## CONTENUTO DEI CAMPI
 :  : FLD T$B§B1 **Elemento**
L'elemento contiene il nome dell'oggetto da convertire nel vecchio archivio.
_Elementi 1-->5._
Questi cinque campi contengono gli oggetti di destinazione del nostra conversione.
In caso questi siano una tabella verranno dedicate le prime 5 posizioni a contenere settore e sottosettore della tabella di destinazione, dalla posizione 6 in poi ci sarà l'elemento.
 :  : FLD T$B§B2.T$B§B1 Elemento
 :  : FLD T$B§B3.T$B§B1 Elemento
 :  : FLD T$B§B4.T$B§B1 Elemento
 :  : FLD T$B§B5.T$B§B1 Elemento
