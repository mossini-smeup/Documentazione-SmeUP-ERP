## Obiettivo
Validare le informazioni di qualsiasi oggetto applicativo sia in maniera massiva sia per singolo oggetto.
## Validazione massiva
La validazione massiva è eseguibile dalle liste attraverso la voce  "Controllo errori"
## Validazione singolo oggetto
La validazione dell'oggetto in uso è eseguibile attraverso la voce  "Controllo errori"

## Struttura
La struttura del controller è suddivisa in 3 livelli : 
### Livello1
A questo livello sono controllate le informazioni di base dell'oggetto selezionato. Attraverso la tipizzazione dei campi, descritta sul database, viene verificata la consistenza del dato segnalando l'incosistenza qualora la stessa non fosse più valida.
### Livello 2
A questo livello vengono estesi i controlli di obbligatorietà dei campi. Per abilitare questa proprietà bisogna costruire l'exit di validazione con il seguente costrutto : 
* nome del database seguito dalla costante '_N'
### Livello 3
A questo livello vengono estesi i controlli anche alle specificità del cliente. Per abilitare questa proprietà bisogna aver abilitato il livello 2, il richiamo alla specificità deve risiedere nella stessa exit del livello 2.
Si fa notare che nella exit non deve essere presente l'apertura di un video, pena il malfunzionamento del controllore.

## Consultazione
La scheda di consultazione elenca l'oggetto contenente l'incosistenza e il motivo della stessa.

## Simulazione
E' possibile arrivare alla simulazione del controller attraverso la scheda LOSER_89.


