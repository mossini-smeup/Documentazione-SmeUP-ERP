# Esempi di lavoro
- Che_Telefono Lancini
- Mostra_Ferie Lombardi
- Modifica_Registrazione 301232
- Modulo distinte
- Vendite
- Estratto Saleri
- Che_Pagamento cliente.saleri
- programma.brar01g
- documenti applicativi che contengono MRP
- Sito Ferriere Nord
- agenda persona
- telefono cliente - fornitore
- mastrino conto
- mastrino cliente - fornitore
- visualizza pdf fattura emessa
- fatture acquisto da inserire
- ore residue cliente da pacchetto ore
- totale ore mese singola commessa
- visualizza OVE del cliente

- Visualizzazione prospetto ferie e rol dipendenti
- Apertura agenda del giorno di un collaboratore
- Mastrino del cliente/fornitore
- Anagrafica cespiti di una determinata categoria
- Visualizzazione di un determinato conto contabile nell'esercizio o in un periodo
- Scheda invio fatture a clienti
- Dati relazionali (telefoni/fax/mail) di clienti e fornitori
- Visualizzazione foto del magazzino a una determinata data
- Visualizzazione cruscotto di una determinata commessa (per Softia), per risalire ai documenti origine e a quelli derivati


# Note di sviluppo provvisorie( SILVIO )
- Dubbi
  - Potrebbe essere una cosa nativa della F( es. se voglio metterlo su un bottone adesso devo mettere la funzione in chiaro, non ho la semplificazione del wizard di scheda e di menù ...
  - Questione del setup G.SET.MAT => potrei aggiungerlo come variabile.
    => sulle schede di navigazione l'unica eccezione è il GMMOVI_OGN che richiama con vari IF in modi diversi il GMSER_21
  - Poco comprensibile essendo un misto di diverse tecniche/chiamate su schede ...


- Fatto
  - Gestione parole multiple sia su codice che su funzione loa12
  - Corretta presentazione menù filtrato
  - Revisione della funzione di test con evidenza del log di elaborazione

- Da Fare
  - Non c'è l'esempio per cui ad una parola mi corrispondono + codici ...
    => in linea generale pensare che fra le simulazioni non dovrebbero esserci casi per i quali sono invece costretto ad inserire una stringa libera
  - Raggruppare gli esempi una gruppi in base al tipo di test che permettono di effettuare

- Da pensare
  - Implementazione dei comandi degli alias (quelli dell'F21)
  - Implementazione del richiamo dei preferiti (oggetti/funzioni)
  => Guardando anche l'esempio degli alias, se non insistiamo sulla questione del punto io mi rifarei proprio alla struttura degli alias, dove è l'ordine quello che conta per altro li era già presente pura una funzione con "O" per la scheda oggetto.
  Quindi in questo caso se voglio mettere prima la funzione e poi l'oggetto potrei prevedere un comando diverso da quello del menù oggetto in cui prima viene la funzione ...

- Nella ricerca per oggetto dovrei considerare anche in caso in cui abbia Alias Multipli ... in questo caso dovrebbe propormi una matrice di scelta ...
- Soffermarsi un attimo sul tema di far sentire o meno, o in che momento le parzializzazioni dalla ricerca dell'oggetto ...
  - LOSER_47 ora non filtra
  - Il LOA10_SE si ...

---------------------------------------------------------------------------------------------
- Da far fare
 * Fare in modo che non si apra il LOA10, verificando già nel LOSER_47 se ho un solo codice
 * Fare in modo che nella scheda di test da ridenominare in loser_47 (al posto di esegui_tst)  mi venga evidenziata la singola stringa risolta, il livello di elaborazione che ha subito (era già in partenza il codice esatto ho dovuto fare una dec?)
 * Fare in modo che non venga emesso il loa10 se in ricerca la corrispondenza è unica
    => devo far fare la ricerca anche nel LOSER_47? Duplico?
    => la stessa cosa devo farla anche quando tenta di partire la ricerca del parametro

 * Risolvere i problema dei nodi del LOA12
 * Perchè se faccio consultazioni non mi esce nulla?
 * E' possibile fare in modo che per il caso ad esempio dei clienti, con stringa dati mi costruisca l'albero senza il nodo "non definito"?


* Guardare utilizzo £SQLS per il controllo della stringa complessa

- Mettere nella scheda LOA12??
- In fondo al pgm fare casi di test, da esemplificare in una scheda
  -> nella scheda di test evidenziare cosa è oggetto, cosa è il tipo cosa è la funzione, in tre campi separati
  -> fare in modo che veda anche i tentativi che vengono fatti per identificare il tipo
- Evidenziare nella funzione di test se ho risolto : 
  - Tipo Oggetto -> l'ho risolto da dec o da ricerca alias?
  - Codice Oggetto -> l'ho risolto da dec?
  - Funzione -> l'ho risolta?

- Analisi di confronto con l'F21 in modo da non avere più solo una funzione di "esegui scheda oggetto", ma anche di generalizzare al concetto di "esegui funzione"
- in questo senso si porrà la questione della risoluzione/passaggio dei parametri

++ .H - ToThink --------------------------------- +- Potrebbe essere (ma è da vedere la complessità, che effetto delle scelte, vedo anche cambiare la stringa?)
- fare poi ricerche simili per le applicazioni/moduli?

++ .E - Error ----------------------------------- +- vedere perchè se faccio cncli,brembo incassi funziona, cncol,lancini incassi non funziona
  la differenza dovrebbe essere dovuta al caso in cui devo scegliere fra più codici
  corrispondenti
- perchè non funziona più la ricerca per parametro? es. TApagamenti?

++ .Z - ToEnd ----------------------------------- +
++ .R - Request (Richieste) --------------------- +
++ .U - ToUP (Miglioramenti) -------------------- +- gestire le parole multiple fra apici, guardando/riprendendo/richiamando quello che fa il cerca?

++ .F - ToFuture -------------------------------- +
++ .D - Da Documentare -------------------------- +- Posso scrivere tipooggetto.codiceoggetto ed opzionalmente la funzione del loa12 da eseguire
- Anche il codice oggetto come si vedrà di seguito potrebbe essere opzionale, ma nel qual  caso la stringa del tipo oggetto dovrà differenziarsi per la presenza del punto
- Ognuno di questi codici può essere indicato tramite codice preciso oppure tramite stringa.
- Come stringa si può utilizzare un unica parola a meno che non si utilizzi il carattere apice per indicare l'insieme di parole che si vuole utilizzare di parole che si vuole utilizzare
- Se a partire dalla stringa non è possibile identificare in modo univoco un codice corrispondente mi viene proposto l'elenco dei codici corrispondenti trovati  ed al click di scelta viene lanciata la funzione completa
- Il metodo di risoluzione di ogni stringa varia a seconda del dato di input : 
- tipo oggetto :  vengono cercati degli alias, in assenza va scelto un tipo oggetto e a partire da quello verrà richiesto il parametro (se obbligatorio e poi il codice)
- parametro oggetto :  cerca fra il codice e la descrizione delle istanze del parametro
- codice oggetto :  cerca fra il codice e la descrizione delle istanze dell'oggetto
- funzione :  cerca fra il codice e la descrizione della voce di menù

++ .N - Note ------------------------------------ +
++ .X - Note Extra ------------------------------ +
* Fare in modo che l'O mi funzioni di nuovo correttamente, perchè la scansione fa casino?
* Fare in modo che pur mantenendo la struttura della lettera iniziale, al momento venga assunta come lettera la O

- Fare in modo che inizino ad essere applicati gli alias su tipooggetto e codice oggetto, lasciando perdere la questione della funzione
- Fare in modo che se non mi viene identificato qualcosa vada in ricerca
  - Ricerca con scelta parametro
  - Ricerca sul codice oggetto
    - impostata ricerca automatica con filtro like su codice/descrizione
    - scelta la "," come separatore avendo in mente il caso delle ragioni sociali con i "."
      in dubbio con " : ". Rispetto alla "," bisogna premere anche lo shitft, però " : " dovrebbe essere ancora più improbabile della "," ci potrebbero essere altre alternative
  => vogliamo provare a pensare anche al caso delle parole multiple (vedi per esempio caso della scelta delle commesse)
  => UTILIZZARE IL . E POI .. PER SOSTITURE
  => questo implementando gli apici  potrebbe non essere necessario?
  => Dare la possibilità di mescolare funzione e oggetto, la stringa oggetto lo riconosco perchè contiene il "."
  => mettere la scheda nel LOA12
  - in fondo al pgm fare casi di test, da esemplificare in una scheda
  -> nella scheda di test evidenziare cosa è oggetto, cosa è il tipo cosa è la funzione, in tre campi separati
  -> fare in modo che veda anche i tentativi che vengono fatti per identificare il tipo
  **=> vedere perchè se faccio cncli,brembo incassi funziona, cncol,lancini incassi non funziona la differenza dovrebbe essere dovuta al caso in cui devo scegliere fra più codici corrispondenti
  **=> perchè non funziona più la ricerca per parametro? es. TApagamenti?
  - Impostata selezione automatica se viene trovato un solo codice corrispondente => per come è adesso ha lo svantaggio che per un attimo si vede la matrice di ricerca ... => però così la ricerca viene effettuata solo una volta, viceversa dovrei ripeterla (con due sql ...)
  - Idee aggiuntive : 
  - Prevedere a livello di oggetto di poter specificare i campi in cui voglio effettuare la ricerca implicita
  - Poter associare ad un oggetto un o più LOA08 di ricerca? (questo fra parentesi rappresenterebbe quello che mattia definitiva come Q3 ... non tanto le risposte quando le domande ... vabbe ...)
  - Andrebbero gestiti i caratteri di ricerca nelle stringhe (es. CNCLI,001 ? => cerca la funzione, CNCLI,? cerca il cliente)
    => qui si pone una domanda ... solo in questo caso dovrei effettuare veramente la ricerca? Altrimenti  dovrei ad esempio lanciare la scheda con showinput?
  - per tipo oggetto è l'unica a gestire gli alias al momento
- Proposta di chiamare la scheda browser/browsing ..
- Potrebbe essere (ma è da vedere la complessità, che effetto delle scelte, vedo anche cambiare la stringa?)
- Nella ricerca per oggetto dovrei considerare anche in caso in cui abbia Alias Multipli ... in questo
  caso dovrebbe propormi una matrice di scelta ...
- fare poi ricerche simili per le applicazioni/moduli?

- Provare a capire cosa significherebbe inserire questa gestione nella sezione albero con showinput del LOA12

- Ricerca
  - Al click cosa deve succedere? Deve ricaricare la scheda, come?
  - Scheda di ricerca, che ha una funzione, al click
