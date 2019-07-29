# Lotto in ordine produzione
 - All'atto dell'inserimento **CQP5L01**, PGM funizzato scatenato dal flusso inserimento/annullamento ordine (dipendente dal tipo ordine) :  crea il N. lotto uguale al N. Ordine e mette nel lotto il N. dell'ordine
 - All'atto del versamento **CQP5L02**, PGM chiamato dalla causale di versamento (metterlo in teblla GMC) che assegna, per ogni versamento, un lotto con radice uguale al N. ordine e mette questo N. nel lotto del movimento di magazzino che si sta eseguendo.
