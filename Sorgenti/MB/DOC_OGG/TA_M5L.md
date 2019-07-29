# M5L - Completamento chiavi di giacenza
## OBIETTIVI
Descrivere le modalità di completamento virtuale di un record di giacenza nell'analisi disponibilità, il cui tipo giacenza è stato esteso con un tipo giacenza complementare impostato nella fonte.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$O,1 __Origine__
Si imposta quale oggetto origine del record di GMQUAN verrà utilizzato per determinare, tramite un suo OAV, l'oggetto nella posizione di questa riga del GMQUAN.
Può assumere i valori
- A     :  Articolo
- M     :  Plant
- 1/4   :  Chiave 1/4
- C     :  Collo
 :  : FLD T$V,1 __OAV__
Si imposta quale OAV dell'oggetto origine verrà utilizzato per ottenere l'oggetto risultante, nella posizione di questa riga di GMQUAN.
Attenzione :  in questo campo non può essere controllata l'esattezza dell'OAV, in quanto l'oggetto a cui è riferito dipende dal tipo giacenza GMQ, e l'accoppiamento tabelle GMQ - M5L avviene soltanto a livello della fonte esistente (M5E).
 :  : FLD T$O,2.T$O,1
 :  : FLD T$O,3.T$O,1
 :  : FLD T$O,4.T$O,1
 :  : FLD T$V,2.T$V,1
 :  : FLD T$V,3.T$V,1
 :  : FLD T$V,4.T$V,1
