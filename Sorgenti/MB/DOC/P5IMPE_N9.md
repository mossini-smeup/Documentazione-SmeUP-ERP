# Datazione impegni
 * **In pianificazione**; l'MRP determina, per ogni ordine pianificato, le seguenti date : 
 ** data fonte = data del fabbisogno
 ** data fine pianificata = data fabbisogno meno lead time rettifica
 ** data suggerimento = data fine ordine meno lead time calcolato
Gli impegni vengono datati alla data inizio ordine. Se c'è lead time di rettifica sul legame, e l'ordine è di produzione, l'impegno è datato alla data fine pianificata meno lead time di rettifica.
 * **In costruzione impegni** : 
 ** __impegni di produzione__ : 
 *** se non c'è lead time di rettifica sul legame, gli impegni sono datati alla data inizio ordine
 *** se c'è lead time di rettifica, sono datati alla data fine meno lead time di rettifica
 ** __impegni esterni__ : 
 *** se impostata in tabella V5L la "data impegno fissa", vengono datati alla data consegna confermata della riga. **Attenzione** :  se viene dall'MRP, se si fissa la data gli impengi pianificati sono arretrati e di conseguenza sono arretrati gli ordini pianificati sotto (di copertura). Quando tutto è stato rilasciato gli ordini sono comunque arretrati :  se gli impegni non lo sono, il successivo MRP emetterà un suggerimento di posticipo
 *** se in V5L il flag è lasciato blank, si parte dalla data consegna confermata e si arretra del lead time di lavorazione. **Nota** :  per la parte variabile del lead time si usa sempre la qtà originale e non la residua, infatti una consegna parziale non deve spostare la data degli impegni.
