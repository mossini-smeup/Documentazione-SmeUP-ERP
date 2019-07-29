# OBIETTIVI
Questa /COPY permette di contollare l'esistenza di un membro, di fare la scansione dei membri presenti all'interno
di un file, leggere i membri riga per riga (record), modificare, aggiungere e cancellare recrord di/da un membro.
Se durante il ciclo di lettura, si dovesse eseguire un'interruzione forzata, bisogna **OBBLIGATORIAMENTE** eseguire la chiusura esplicita tramite il metodo FINE. Se questa azione non viene intrapresa il sorgente rimarrà allocato e nessuno potra modificarlo fino alla fine del job che ha generato il vincolo.

# PREREQUISITI
Per utilizzare la /COPY è nesessario importare : 
D/COPY QILEGEN,£G75DS
e
C/COPY QILEGEN,£G75

# FUNZIONI/METODI
## DEC - Ricerca/Controllo/Decodifica

La funzione 'DEC' non necessita metodo alcuno, ma richiede l'immissione
del File, della Libreria e del Membro del quale si vuole verificare
l'esistenza oppure semplicemente, se già certi dell'esistenza del
membro, consente di decodificare la descrizione di questo, il tipo, la
data di creazione/modifica.

Se il Membro indicato non dovesse esistere si accenderà l'indicatore 35
mentre, se il Membro fosse presente verrà restituita la decodifica  e
tutti gli indicatori resteranno spenti.

## RIT - Ritorno elenco membri

La funzione 'RIT' consente la lettura di un File e la restituzione, uno
ad uno, dei membri contenuti in esso. Non richiede l'immissione del
Membro, bensì necessita di una Libreria e di un File nel quale verrà
effettuata la Ricerca.
L'indicatore 35 si accenderà quando verrà raggiunta la fine del file,
quindi tutti i membri saranno stati restituiti con la stessa
modalità di Output della funzione 'DEC' (descrizione, tipo, data).
La funzione 'RIT' ha due metodi, poichè richiede il posizionamento
(SETLL) sul primo membro del File prima di effettuarne la lettura(READ)

### INI - Posizionamento lettura primo membro
Va selezionato come Metodo per la prima esecuzione della funzione 'RIT'
ed ogni qualvolta venga cambiato il File all'interno del quale effettua
re la ricerca.

### ALL - Lettura Membro successivo
Dopo aver eseguito il posizionamento, utilizzare questo Metodo per legg
ere i Membri successivi. Al raggiungimento dell'ultimo Membro contenuto
nel File verrà acceso l'indicatore 35.


## LET - Lettura

La funzione 'LET' consente la lettura del contenuto di un membro riga
per riga. Richiede l'immissione della Libreria, del File e opzionalment
e anche il Membro di cui leggere le righe.

L'indicatore 35 si accenderà quando verrà raggiunta la fine del membro,
quindi tutte le righe saranno state lette. Oltre al contenuto delle
righe, verranno riempite anche una variabile indicante la Sequenza e
una indicante la Data.
La funzione 'LET' ha due metodi, poichè richiede il posizionamento
(SETLL) sulla prima riga del Membro prima di effettuare la lettura del
le righe successive (READ).
Se non verrà indicato alcun mebro verranno lette le righe di tutti i
Membri di tutto il File.

### SETLL - Posizionamento lettura primo record
Va selezionato come Metodo per la prima esecuzione della funzione 'LET'
ed ogni qualvolta venga cambiato il membro del quale leggere le righe.

### READ - Lettura record successivo
Dopo aver eseguito il posizionamento, utilizzare questo Metodo per legg
ere le righe successive. Al raggiungimento dell'ultima riga del Membro
verrà acceso l'indicatore 35.

### READP - Lettura record precedente
Eseguendo questo metodo si posso leggere a ritroso le righe del Membro.

### FINE - Fine immediata
Consente di raggiungere immediatamente la fine del Membro. Non accende
nessun indicatore.


## UPD - Lettura
Consente di leggere, modificare, aggiornare, cancellare i record.

### SETLL - Posizionamento e lettura primo record
### READ - Lettura record successivo
### READP - Lettura record precedente

### UPDATE - Aggiorna record
Una volta raggiunto il record interessato, utilizzare questo metodo per
modificarne il contenuto, la sequenza e la data.

### WRITE - Scrittura record
Una volta raggiunto il record interessato, utilizzare questo metodo per
aggiungere un record nella sequenza (riga) successiva.

### DELETE - Cancellazione record
Serve per eliminare il record sul quale si è posizionati.

### SL_UP - Posiz. e Aggiorna Record
Si posiziona su un record e permette la modifica del contenuto, della
seuqenza e della data.

### SL_DE - Posiz. e Cancella Record
Si posizione su un record e ne permette la cancellazione.

### FINE - Fine immediata
Consente di raggiungere immediatamente la fine del Membro. Non accende
nessun indicatore.


## GES - Gestione sorgente
Questa funzione richiede l'immissione di Libreria/File/Membro e consent
e, attraverso i suoi due metodi, di modificare o semplicemente visualiz
zare il sorgente del membro indicato.

### 02 - Modifica tramite SEU
Apre l'editor del sorgente del Membro indicato e ne consente le modific
he e il salvataggio.

### 05 - Visualizza tramite SEU
Apre il sorgente del Membro indicato in modalità di Esame e ne permette
la consultazione.

# ESEMPIO DI CHIAMATA
 :  : PAR
                     EVAL      £G75FU=W$FUNZ
                     EVAL      £G75ME=W$METO
                     EVAL      £G75NM=W$NOMM
                     EVAL      £G75NF=W$NOMF
                     EVAL      £G75NL=W$NOML
                     EVAL      £G75LC=' '
                     EXSR    £G75



