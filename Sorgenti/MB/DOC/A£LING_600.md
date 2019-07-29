# Obiettivo della tracciatura
Tracciare varie informazioni di utilizzo delle frasi utilizzate in un'installazione, per guidare la priorità delle traduzioni da effettuare.

# Descrizione funzionamento
La tracciatura salva varie informazioni relative a tutte le richieste di traduzione effettuate da Sme.UP.
Ogni volta che viene richiesta al sistema la traduzione di una frase, vengono aggiornate varie informazioni quali : 
* numero di volte totali di cui è stata richiesta tale traduzione
* numero di giorni in cui è stata richiesta la traduzione
* ultimo giorno in cui è stata richiesta la traduzione
Sulla base di queste informazioni sarà poi possibile andare ad effettuare le effettive traduzioni richieste in modo efficiente.

La tracciatura è attivabile solo ed esclusivamente su ambienti in lingua.
E attivabile/disattivabile mediante flag e può essere attivata per tutti gli utenti o per una lista di specifici utenti.

La lingua di tracciatura non deve essere necessariamente la lingua in cui dovrò poi tradurre.
Posso ad esempio raccogliere i dati da un ambiente inglese per capire le priorità di traduzione della lingua spagnola.

Quando si parla di frase, si intende sempre la frase "contestualizzata".

# Passi da eseguire per attivare il trace su ambienti in lingua
- Compilazione file A£TRTR0F e logici A£TRTR0L e A£TRTR1L
- Configurazione ambiente in lingua
- Definizione Exit A£A£BT_xx
- Impostazione exit in tabella A£1

## Compilazione file A£TRTR0F e logici A£TRTR0L e A£TRTR1L
Il file della tracciatura delle traduzioni A£TRTR0F e le sue viste logiche devono stare nella stessa libreria dei file delle traduzioni ver e proprie (A£TROR* e A£TRDE*).

Nel file SRCDB della libreria P_LINTR sono presenti i sorgenti da compilare.

Il file è creato in modo da avere gli stessi parametri identificativi degli altri file delle lingue (frase, tipo, parametro, codice, dettaglio 1, 2, 3 e 4, lingua) a cui si aggiungono i campi specifici relativi al numero utilizzi, numero giorni di utilizzo e data ultimo utilizzo.

## Configurazione ambiente in lingua
La tracciatura funziona su un ambiente in lingua, è quindi necessario configurare le exit e le tabelle opportune.

## Definizione Exit A£A£BT
E' necessario e creare una exit A£A£BT_xx che definisce gli utenti da tracciare su un determinato ambiente.
E' possibile utilizzare la exit predefinita 01 per tracciare tutti gli utenti che si collegano all'ambiente.

## Attivazione tramite tabella A£1
Per attivare il trace occorre compilare il campo T$A£1K con il suffisso xx della exit A£A£BT_xx.

# Consultazione traduzione
Nel modulo A£LING, è possibile consultare i risultati della tracciatura dalla scheda "Traduzioni" sotto la label "Per Tracciatura".
E' possibile filtrare le traduzioni da fare secondo vari criteri :  stato, fonte di traduzione, numero minimo di accessi (richieste di traduzione della singola frase), numero minimo di giorni di utilizzo e data minima ultimo accesso.
E' inoltre possibile selezionare la lingua di tracciatura (lingua di traduzione con cui è configurato l'ambiente usato appunto per tracciare). Se non viene indicata la lingua di tracciatura il risultato è la somma degli utilizzi nella varie lingue.
