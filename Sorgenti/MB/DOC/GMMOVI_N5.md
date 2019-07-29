# Programmi collegamento GM - P5
Normalmente la movimentazione di magazzino viene eseguita con il PGM P5VE00G (carico assieme) e P5FUIML (scarico componenti).
Entrambi questi PGM aggiornano, al loro interno, le testate o gli impegni, rispettivamente.
Nel caso in cui la transazione NON sia da questi ma automatica (il caso più importante è l'applicazione di una richiesta di movimentazione) l'aggiornamento dei portafogli è demandato ai PGM associati alla causale : 
 * P5GMVE (Tipo movimento VP o VS) , aggiorna la testata con eventuale saldo se impostato nel movimento o se la qtà è >= alla richiesta (il tutto gestito con £P5I)
 * P5GMIM (Tipo movimento PP o PE) , aggancia l'impegno, lo riduce o lo elimina (se movimento a saldo)
