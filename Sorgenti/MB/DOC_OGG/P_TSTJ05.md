## Obiettivi
## Simulazione
## Note di sviluppo
### Lancini

- E' Possibile far partire la JVM alla partenza di LOOC.up
- Verificare errore di richiamo J1PATHDIR nella scheda di simulazione
- Gestire in COPY
-- Tipo di file FLR / FILE
-- Forse il suffisso
-- Si possono avere gli attributi del file (**FATTO in funzione PRO.FIL, POS e LET. Formato NOME=VALORE)
-- Messaggi
- Gestire in Simulatore
-- Messaggi
-- Tempi
-- Matrice deli attributi dei files
- Testare letture su : 
-- AS/400

### Maestrelli

- caratteri Jolly nei percorsi (**IMPOSTATO IN JAVA**)
- gestione dei concetti di DOMINIO, SERVER, CONDIVISIONI e PERCORSI (**FATTO**)
- ricorsione
-- gestire flag per richiederla. (**IMPOSTATO IN JAVA**)
- attributi dei files (**FATTO**)
- gestione delle / finali (**FATTO :  VENGONO TOLTE**)
- gestione delle sostituzioni / con \ ? (**FORSE E MEGLIO BASARSI SU UNC PATH**)
- messaggi di errore ed eccezioni

### Rocchi

- render più fruibile i log (sopratutto della parte java in /TMP)
- ricorsione
-- gestire flag per richiederla
- gestione dei concetti di DOMINIO, SERVER, CONDIVISIONI e PERCORSI (**FATTO**)
- messaggi di errore ed eccezioni
- richiesta parametri non espressi

