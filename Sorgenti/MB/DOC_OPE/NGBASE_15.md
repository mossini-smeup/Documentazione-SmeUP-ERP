# Note Gestione Configurazione Applicativa

## Note Gestione Configurazione Applicativa

La Configurazione di Negoziando è basata su due Parametri principali, che sono il Nodo e l'Utente.
Il Nodo rappresenta un'entità geografica all'interno della quale possono coesistere N. negozi. il Nodo è un codice alfanumerico di 8 caratteri
Nel caso in cui esista una sede che al proprio interno contenga anche un negozio, allora entrambi faranno parte dello stesso stesso nodo, non verranno configurate trasmissioni per lo scambio di dati tra sede e Pv.
Nei casi più comuni, invece, esisterà una sede (ad esempio con nodo 00000000) ed i vari Pv dislocati sul territorio, ognuno col proprio nodo differente (00000001, 00000002, etc..)

## Nota sulla Gestione Nodi/Utenti

Dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa_

All'attivazione della Configurazione Applicativa viene richiesto di indicare il Codice Nodo e l'Utente per il quale impostare la Configurazione. Il programma propone in automatico i valori con i quali è stato
effettuato l'accesso alla funzione (i valori sono naturalmente modificabili).
E' possibile definire la Configurazione per : 

 * Tutti i Nodi e tutti gli Utenti = Lasciare in bianco sia il Codice Nodo che il Codice Utente. Questa impostazione varrà per tutti i Nodi e tutti gli Utenti nell'ambito di qualsiasi utilizzo di Negoziando (salvo definizioni specifiche).
 * Singolo Nodo = Indicare il Codice Nodo e lasciare in bianco il Codice Utente. Questa impostazione varrà per tutti gli Utenti del Nodo (salvo definizioni specifiche). Se alcuni Valori di Configurazione vengono visualizzati con un simbolo rosso, questo significa che sono stati modificati a livello di Nodo e Utente lasciati in Bianco
 * Nodo/Utente = Indicare sia il Codice Nodo che il Codice Utente. Questa impostazione varrà solo per il singolo Utente nell'ambito del Nodo di utilizzo di Negoziando. Se alcuni Valori di Configurazione vengono visualizzati con un simbolo verde, questo significa che sono stati modificati a livello di Singolo Nodo
 * Singolo Utente = Indicare il Codice Utente e lasciare in bianco il Codice Nodo. Questa impostazione varrà solo per il singolo Utente nell'ambito di qualsiasi utilizzo di Negoziando (salvo definizioni specifiche).

**N.B.Se l'elaborazione viene effettuata in Negozio, non sarà possibile definire configurazioni per altri Nodi. Il campo del Codice Nodo verrà compilato automaticamente in grigio chiaro e non sarà possibile modificarlo.

In Configurazione, posizionando il cursore sul Valore di una determinata Richiesta, premendo F6 Visualizza Altri Valori è possibile vedere, a livello di Nodo/Utente, tutti i Valori impostati e, sotto le Annotazioni in basso, è possibile trovare un breve suggerimento relativo alla Richiesta selezionata.

## Regola di Determinazione dei Valori di Configurazione

Per determinare il Valore da attribuire a un parametro di Configurazione Negoziando opera delle interrogazioni sulla tabella che definisce la Configurazione (CONFI00F) per la variabile interessata
(CFVAR) utilizzando le seguenti priorità : 

1) **Ricerca per Codice Nodo e Utente**

Viene effettuata una ricerca per Codice Nodo (CFNOD) = Nodo con il quale è stata attivata l'applicazione e Utente (CFUSR) = Utente con il quale è stata attivata l'applicazione.
Se trovato imposta il valore e non effettua le ricerche successive.
N.B. L'interrogazione non viene effettuata se l'applicazione è stata attivata senza indicare il Codice Utente.

2) **Ricerca per Utente**

Viene effettuata una ricerca per Codice Nodo (CFNOD) in bianco e Utente (CFUSR) = Utente con il quale è stata attiva l'applicazione.
Se trovato imposta il valore e non effettua le ricerche successive.
N.B. L'interrogazione non viene effettuata se l'applicazione è stata attivata senza indicare il Codice Utente.

3) **Ricerca per Nodo**

Viene effettuata una ricerca per Codice Nodo (CFNOD) = Nodo con il quale è stata attivata l'applicazione e Utente (CFUSR) in bianco.
Se trovato imposta il valore e non effettua le ricerche successive.

4) **Ricerca senza Utente e senza Nodo**

Viene effettuata una ricerca per Codice Nodo (CFNOD) in bianco e Utente (CFUSR) in bianco.
Se trovato imposta il valore.
