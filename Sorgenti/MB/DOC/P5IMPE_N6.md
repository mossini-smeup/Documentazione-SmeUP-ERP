# Codifica tipo origine in impegni

|  Nam="Tipo origine in impegni" R="90" |
| 
| .COL Txt="." |
| ---|----|
| 
| .COL Txt="Impegni materiali" |
| 
| .COL Txt="Impegni risorse" |
|  **Produzione** | PP | VP |
|  **Documenti esterni** | PE | DO |
| 

 In questo modo, gli impegni di risorse sono agganciati al documento di testata (ordine produzione / documento V5) e si può usare la routine di controllo chiavi generalizzata £GMK (anche per le parzializzazioni). - è la stessa che si usa per la gestione del documento nel dettaglio del GMRRIM.
Nel caso di impegni risorse, __dopo__, c'è la gestione della fase (fatta con routines specifiche).

![P5IMPE_03](http://localhost:3000/immagini/P5IMPE_N6/P5IMPE_03.png)
Questo serve per unificare il controllo / trattamento parzializzazione dell'identificativo (anche parziale nel caso degli impegni risorse perchè manca la fase).
