# RIENTRO MFP DA C/LAVORO
Distribuisce i contenitori di riento del C/Lavoro di un fornitore sui suoi ordini aperti e sulla sua giacenza di C/Lavoro.

### Bolle rientro
Sono le righe della bolla di rientro del C/Lavoro

### Ordini C/Lavoro
Ordini aperti di C/lavoro del fornitore su articolo/fase bolle rientro

### Giacenze
Giacenza del fornitore su articolo/fase-precende bolla rientro

### Disponibilità
Legge gli ordini di C/Lavoro aperti, distribuisce ciascun ordine di C/Lavoro sulla giacenza disponibile con stesso articolo/fase/ordine di produzione. Fino ad esaurimento della giacenza.

Se rimane del residuo sull'ordine di C/Lavoro è disponibile ma senza giacenza.

Dopo aver distribuito tutti gli ordini di C/Lavoro se rimane della giacenza residua è disponibile ma senza ordine di c/lavoro

### Srittura righe
Legge tutte le righe di bolla rientro, distribuisce ciascuna riga di bolla sulla disponilità con stesso articolo/fase e se sulla riga di bolla sono presenti l'ordine di C/Lavoro e/o l'ordine di produzione con lo stesso ordine di C/Lavoro e/o produzione.
