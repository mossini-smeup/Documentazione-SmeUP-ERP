# Modalità di movimentazione con codice lotto
Si imposta in GM1 se gli articoli senza classe funzionale sono gestiti a lotti (default = SI).
Sulla classe funzionale si imposta poi se gli articoli di quella classe sono gestiti a lotti (default = SI).
Esiste una /copy (£GNA) che può ricevere l'articolo o la classe funzionale e ritorna l'informazione che l'oggetto di input è movimentato o meno a lotti. Questa informaizone è usata in : 
 * impostazione lotto(CQP5L01) :  se articolo non a lotti __non__ viene creato il lotto
 * prelievo di produzione (P5FUIML) :  se impostata la gestione lotto secondo la classe funzionale, viene richiesto il lotto se l'articolo lo richiede, in caso contrario __non__ viene visualizzato il campo lotto.

Questo per mantenere la compatibilità con l'esistente.
