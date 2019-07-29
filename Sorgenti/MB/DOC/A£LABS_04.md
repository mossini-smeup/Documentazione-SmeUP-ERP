# Obiettivi

- Disaccoppiare la richiesta di una attività (ANALISI) dalla sua esecuzione (PROGRAMMAZIONE)
- Riconoscere le azioni, le schede, sezioni e subsezioni in fase di sviluppo


Non si pretende di risolvere tutti i casi ma quelli dove si vuole aprire una scheda (magari associandola ad una chiave di menù), una sezione o una subsezione.

Il programmatore vede i task del modulo (in prospettiva con un responsabile e uno stato) Legge cosa si chiede di fare, vede tutte le condizioni di richiamo : 

- Dove viene richiamato
- Che parametri ricevo
- Come sarà impostata la funzione


Se ricevo la funzione, ne vedo i dati e si abilita una scheda dinamica che mostra l'effetto provvisorio

# Luogo in cui scrivo le attività
Ad ogni modulo viene associato un membro con nome modulo_ATT nel file DOC_SVI
Per ogni modulo avremo più progetti e per ogni progetto avremo più attività.
Quando il documento viene aperto dalla scheda di gestione viene generato il progetto "Base" e sono aperte tre attività : 

- Cose da fare (già note e decise)
- Suggerimenti (segnalazioni degli operatori allo sviluppatore)
- Errori (già noti e in attesa di risoluzione)

Questi tre tipi di attività potranno ripetersi anche su ogni altro progetto.

# Come evidenziare le funzioni che sono sotto sviluppo
Quando voglio dire che l'attività è in fase di lavoro, invece di scrivere la funzione metterò il richiamo alla scheda : 
F(EXD;*SCO;) 1(TA;B£AMO;modulo in sviluppo) 2(MB;SCP_SCH;A£LABS_ATT) 4(;;DETATT)
Nel campo di input metterò : 

- PRO() Progetto
- ATT() Attività
- FUN() Funzione (che potrebbe anche non esistere ancora ma indica che al rilascio tale funzione sostituirà la scheda.


# Come accedere
Arriveremo alla gestione nei seguenti modi : 

- Come azione del modulo A£LABS. Vedremo tutti i moduli con attività presenti e potremo passare alla gestione delle attività del modulo.
- Da ogni singolo modulo attraverso la sua documentazione
- Mediante richiamo specifico della scheda (A£LABS_ATT) che potrà ricevere un progetto, nel qual caso presenterà tutte le attività del progetto oppure direttamente l'attività.

