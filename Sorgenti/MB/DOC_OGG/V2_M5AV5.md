# M5AV5     -  MODALITÀ ACCODAMENTO A V5
Definisce le varie modalità con cui un consiglio di pianificazione, all'atto del suo rilascio verso una riga di ciclo
esterno (V5), viene accodato ad un documento esistente, oppure viene creata una nuova testata.

## VALORI POSSIBILI

### '  ' RICHIESTA ESPLICITA
Viene presentato un formato di richiesta, con la possibilità di inserire il documento a cui accodare la riga, oppure
di forzare l'inserimento di una nuova testata.

### 'NA' NESSUN ACCODAMENTO
Ad ogni riga viene inserita una nuova testata.

### 'AP' AL PRIMO ORDINE ATTIVO (TEST.ESPL.)
La riga viene accodata alla prima testata attiva che soddisfa tutte le condizioni di parzializzazione (ente, modello
documento, stato).
Se non trovata, la testata viene richiesta come nella modalità ESPLICITA

### 'AA' AL PRIMO ORDINE ATTIVO (TEST.AUTO.)
La riga viene accodata alla prima testata attiva che soddisfa tutte le condizioni di parzializzazione (ente, modello
documento, stato). Se non trovata, la testata viene creata automaticamente (come la modalità NA).

### 'UP' ALL'ULTIMO ORDINE ATTIVO (TEST.ESPL.)
La riga viene accodata all'ultima testata attiva che soddisfa tutte le condizioni di parzializzazione (ente, modello, documento, stato, data inserimento, ora inserimento).
Se non trovata, la testata viene richiesta come nella modalità ESPLICITA

### 'UA' ALL'ULTIMO ORDINE ATTIVO (TEST.AUTO.)
La riga viene accodata all'ultima testata attiva che soddisfa tutte le condizioni di parzializzazione (ente, modello, documento, stato, data inserimento, ora inserimento).
Se non trovata, la testata viene creata automaticamente (come la modalità NA).

### 'GI' NEL GIORNO (TEST.ESPL.)
E' come l'opzione precedente con l'ulteriore limitazione che la testata deve avere come data documento la data odierna.
Con questa opzione è possibile, in una sessione di rilascio, raggruppare in modo implicito, per ciascun ente, tutte le
righe sotto un'unica testata. Se la testata non viene trovata verrà richiesta come nella modalità ESPLICITA.

### 'GA' NEL GIORNO (TEST.AUTO.)
E' come l'opzione precedente con il default che se la testata non viene trovata verrà richiesta come nella modalità NA.

### 'CT' CONTRATTO IMPOSTATO (TEST.ESPL.)
Viene assunta la testata impostata, in pianificazione, nel campo oggetto di rilascio (tipo e numero documento).
Se la testata non viene trovata verrà richiesta come nella modalità ESPLICITA.

### 'CD' DERIVATO DA CONTRATTO (TEST.ESPL.)
Viene ricercata una testata valida le cui righe hanno come documento origine il contratto, se non ci sono testate
valide viene creata una testata derivandola dalla testata del contratto e presentata come nella modalità ESPLICITA.
Anche la riga viene derivata dal contratto.
Il contratto viene impostato in pianificazione nel campo oggetto di rilascio (tipo, numero documento e numero riga).

### 'CA' NEL GIORNO (TEST.AUTO.)
E' come l'opzione precedente con il default che se la testata non viene trovata verrà richiesta come nella modalità NA.

### 'IS' RICHIESTA A INIZIO SESSIONE
All'inizio di ogni sessione viene presentato un formato con la richiesta se inserire una nuova testata oppure se
accodare la riga ad un documento esistente, e se per i successivi collegamenti della stessa sessione, dovrà essere
riemesso questo formato di richiesta oppure se essi si accoderanno al documento definito ad inizio sessione.
Per inizio sessione si intende ogni prima volta che, a partire dal lancio del programma da menù, si rilascia un
suggerimento su un nuovo ente.

### 'DT' CONTRATTO IMPOSTATO (TEST.ESPL.)
Viene assunta la testata di un documento aperto che ha come origine il contratto impostato, in pianificazione,
nel campo oggetto di rilascio (tipo, numero documento e riga).
Se la testata non viene trovata verrà richiesta come nella modalità ESPLICITA.
### 'DA' CONTTRATTO IMPOSTATO (TEST.AUTO.)
E' come l'opzione precedente con il default che se la testata non viene trovata verrà creata una nuova testata
derivata dal contratto, in pianificazione, nel campo oggetto di rilascio (Tipo e numero documento). Questo avviene
solo se il contratto è un documento esistente. In caso contrario non è possibile rilasciare la riga, e viene emessa una
segalazione di errore.

