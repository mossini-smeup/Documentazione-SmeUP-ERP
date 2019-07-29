## Relazioni fra referenti
### Obiettivo
Analizzare le relazioni di un referente con gli altri referenti sulle opportunità.
Rispondere a domande quali : 
- Questo architetto con quali agenti lavora?
- Un installatore opera con l'ingegnere X?

### Come creare relazioni causali per test iniziali
E' possibile richiamare il programma RE_RER_DEM con parametro ORA "CALL RE_RER_DEM PARM('ORA')"
Questo programma : 
- Cancella tutti e soli i parametri R01 della categoria ORA creati da lui stesso (Campo VER_R01)
- Seleziona un insieme di opportunità (Ora forza quelle che iniziano con R)
- Prepara tutti i ruoli della tabella RER
- Sceglie in modo causale fino a 20 referenti
- Genera i parametri in modo random

### Modalità operative
- Vengono presentati tutti i referenti che hanno generato opportunità
- Presento tutte le relazioni per un referente scelto
- Posso arrvare al dettaglio partendo dalla scheda di un referente

### Sviluppi
- Isolare solo le ripetizioni significative
