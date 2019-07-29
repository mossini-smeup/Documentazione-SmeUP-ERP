# Generalità
Le liste di distribuzione sono contenitori di oggetti a cui possono essere inviati messaggi riguardo temi caratteristici della lista. Esse sono create dall'utente, il quale, in qualsiasi momento, può aggiungere o eliminare un elemento.
Una lista di distribuzione identifica un insieme di oggetti, interessati da argomenti omogenei,  a cui l'utente può decidere di distribuire un oggetto (si costruirà, ad esempio, una lista per le azioni correttive, una per i fornitori, una per i clienti, ecc...).
Per la creazione di ogni nuova lista è necessario aggiungere un sottosettore alla tabella NSL, identificando il codice della lista con il codice del sottosettore (gli elementi del sottosettore della tabella NSL costituiscono gli oggetti della lista a cui possono essere inviati messaggi, domande, ecc...).

Per ogni elemento appartenente alla lista possono essere indicati alcuni valori di default e in particolare : 

- i destinatari fissi delle distribuzioni;
- un codice della domanda e renderlo non modificabile;
- un codice della risposta e renderlo non modificabile;
- automatizzare la data della risposta.

E' possibile, inoltre, disporre che tutti i messaggi inviati all'area commerciale elemento della lista azioni correttive debbano essere di tipo informativo, eludendo la necessità di accedere tutte le volte al dettaglio della gestione delle domanda.
Dopo essersi collegati alla distribuzione della documentazione, la manutenzione degli elementi della tabella è possibile dal programma di gestione delle tabelle e anche dagli applicativi, che danno la possibilità di aggiungere, modificare e cancellare elementi della lista (vedi diagramma di flusso per la costruzione della lista di distribuzione).

# Distribuzione Documentazione
La distribuzione di un messaggio avviene collegandosi da una qualsiasi applicazione, immettendo GL nel campo in basso a sinistra e specificando : 

- la lista di distribuzione (di default viene presentata la lista specificata nel contenitore associato all'oggetto);
- gli elementi della lista, per ognuno dei quali vengono gestiti la descrizione del messaggio e lo stato della domanda.

Lo stato viene codificato in tabella A£D dove è possibile combinare i seguenti elementi : 

- tipo invio (informativa, facoltativa o obbligatoria);
- tipo risposta (vincolante,  non vincolante);
- livello della domanda (una domanda viene inviata una volta gestite le domande dei livelli inferiori);
- la data richiesta della risposta.

Effettuando la distribuzione in questa modalità è possibile catalogare i tipi di domanda, condizionare le azioni in base alla risposta e classificare le domande in modo che non possano essere gestite se non è ancora stata data risposta a quelle del livello superiore.

![B£LISD_01](http://localhost:3000/immagini/B£LISD/BXLISD_01.png)Figura 1 - Costruzione Liste Distribuzione

# Risposta Documentazione
Il destinatario della documentazione si accorge della posta inviatagli nei seguenti modi : 

- se la documentazione è stata inviata utilizzando come elemento della lista il profilo utente, sul terminale all'operatore viene visualizzato un messaggio con i riferimenti opportuni con cui rintracciare i dettagli sulla problematica proposta;
- l'operatore si collega con il modulo di interrogazione delle liste di distribuzione, in cui immetterà il proprio codice di identificazione. Entrando con / dal codice elemento, si aprono in sequenza delle videate successive per sfogliare l'archivio dei documenti presenti, fino ad arrivare al livello del singolo documento distribuito ad un ente.

L'operatore risponde alla documentazione inviata, specificando il tipo di risposta (positiva o negativa) codificato in tabella A£R e la data della risposta.

# Gestione Liste di Distribuzione
È possibile, con una serie di parzializzazioni, interrogare gli oggetti a cui sono associate delle distribuzioni e vedere sinteticamente : 

- lo stato di tutte le risposte inviate;
- l'esito delle risposte;
- l'esito complessivo del documento in base agli esiti delle singole risposte (vedi diagramma di flusso).


![B£LISD_02](http://localhost:3000/immagini/B£LISD/BXLISD_02.png)Figura 2 - Gestione Liste di Distribuzione
