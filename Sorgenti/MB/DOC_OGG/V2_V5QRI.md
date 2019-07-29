# V5QRI     -  QUANTITÀ RIFERIMENTO PER IMPEGNI
Definisce la quantità del documento che viene assunta nella scansione della distinta per la costruzione degli impegni
del documento.

## VALORI POSSIBILI

### ' ' QUANTITÀ MODIFICABILE
E'il caso in cui si tengono gli impegni solo su un documento (normalmente il documento origine), che vengono scaricati
all'atto del collegamento a magazzino.

### 'A' QUANTITÀ RESIDUA
E'il caso in cui si tengono gli impegni sia sul documento origine (ordine) sia sulla documento derivato (bolla). I
primo vengono scaricati dai secondi all'atto dell'estrazione (con un apposito passo di flusso di inserimento della
riga), i secondi vengono scaricati all'atto del collegamento a magazzino.
