# S5_CM     -  COPERTURA MATWERIALI FINE UP
Se impostato, nella schedulazione Fine.Up, di calcolare la coperetura materiali, viene  calcolato un flag che esprime il livello di copertura, sia del singolo impegno materiale sia dell'intero ordine.

## VALORI POSSIBILI

### '1' COPERTURA TOTALE PRESENTE
Vi è coperetura totale con fonti presenti

### '2' COPERTURA TOTALE FUTURA
Vi è coperetura totale con fonti presenti e future

### '3' COPERTURA PARZIALE
Vi è coperetura parziale (con fonti presenti e/o future)

### '4' COPERTURA NULLA
Non vi è alcuna coperetura

### '5' MATERIALI NON RICHIESTI
I materiali non sono richiesti :  è una situazione anomala, in quanto vuol dire che non sono presenti gli impegni materiali.
Potrebbe verificarsi nel caso di schedulazione di servizi, ma allora non avrebbe senso attivare l'analisi dei materiali.
L'unico caso in cui questo flag potrebbe essere significativo è la schedulazione contemporanea di ordini di produzione (con materiali) e di servizi (senza materiali) che cometono nell'utilizzo delle stesse risorse.

### '8' ORDINE NON SCHEDULATO
Si presenta se l'ordine, per anomalie (deadlock, legami tra livelli non costruiti in modo corretto,
ecc..) non viene interamente schedulato.

### '9' ERRORE NEL GRUPPO FONTI
Si presenta quando il gruppo fonti impostato non presenta gli impegni dei materiali degli ordini da schedulare (o li presenta raggruppati per data), nel qual caso non si riesce a stabilire la loro posizione all'interno dell'andamento della disponinbilità.

