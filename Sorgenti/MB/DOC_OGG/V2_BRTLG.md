# BRTLG     -  TIPO LEGAME DI DISTINTA BASE
Definisce se un componente (articolo, se non è già un fittizio, (tipo parte con radice '0') lo può diventare, in un
determinato legame di distinta base. In questo modo la distinta di produzione può scendere o meno.
Questa forzatura permette di trattare come fittizio un articolo che non lo è ma non il contrario :  non è possibile far
sì che un fittizio non lo sia per alcuni legami.
Se la distinta non tratta articoli, non esiste il concetto di fittizio :  con questa forzatura sul legame si possono
comunque rendere fittizi i componenti.

## VALORI POSSIBILI

### ' ' DA TIPO PARTE ARTICOLO
Per il legame non viene fatta nessuna sovrapposizione al tipo parte dell'articolo.

### '1' FITTIZIO
Per il legame il componente è sempre un fittizio.

### '2' FITTIZIO PER PRODUZIONE INTERNA
Per il legame il componente è un fittizio se si sta eseguendo una scansiome di produzione interna.

### '3' FITTIZIO PER LAVORAZIONE ESTERNA
Per il legame il componente è un fittizio se si sta eseguendo una scansiome di lavorazione esterna.
