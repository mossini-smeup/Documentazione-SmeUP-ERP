# £G81 GESTIONE VINCOLO SU UN OGGETTO APPLICATIVO

## OBIETTIVO
Gestire il vincolo logico (= allocazione) su un oggetto applicativo.
Sono possibili tre tipi di vincolo :  ottimistico, pessimistico, logico.

### Vincolo PESSIMISTICO (1)
Con questo metodo ad ogni richiesta viene scritto un vincolo sull'oggetto richiesto e ne viene impedita la lettura ad altri richiedenti fino all'eliminazione del vincolo stesso o alla conclusione del job che l'ha creato.
Se l'oggetto richiesto è il membro di un file, ne viene eseguita anche l'allocazione fisica, tramite comando del Sistema Operativo.

### Vincolo OTTIMISTICO (2)
Con questo metodo si memorizza sul vincolo l'immagine originale di un record che viene letto (senza essere allocato) e presentato all'utente per la modifica.
Quando si rilegge il record per aggiornarlo si confronta il suo contenuto con l'immagine salvata in precedenza, in modo da scrivere il nuovo record solo se non è cambiato nel frattempo.

### Vincolo LOGICO (3)
Con questo metodo viene scritto un vincolo sull'oggetto per impedire l'accesso ad altri programmi.
A differenza del vincolo pessimistico, l'oggetto non viene allocato fisicamente, per cui è compito dei programmi che accedono all'oggetto verificarne la disponibilità.
Inoltre è possibile fissare una scadenza del vincolo, inserendo la durata in minuti.

## FUNZIONI

### VER      Verifica esistenza vincolo

### CFR      Confronto immagine vincolo con immagine attuale

### WRI      Scrittura vincolo

### DEL      Rimozione vincolo

### SCA      Scansione vincoli

### GESLOCK  Gestione vincoli

Per ulteriori informazioni si veda la documentazione all'interno della routine.
