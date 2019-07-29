# Introduzione
Le principali peculiarità della versione 2 del nuovo data entry anagrafico consistono : 
 * nella gestione dei dati in lista.
 * nella possibilità di poter accedere secondo differenti prospettive ai dati, in modo da poter focalizzare l'attenzione sui soli dati interessati al momento (es. Dati fiscali, Dati commerciali ecc.). NOTA BENE :  se non si è in una situazione in cui differenti utenti operano su differenti dati, è consigliabile lasciare autorizzata solo la prospettiva CN_P£01, viceversa la funzionalità delle prospettive può portare a confusione.
 * nella possibilità di poter gestire in unica sessione dati di differente natura (sia dall'anagrafico di base, che dalle estensioni).
 * nella possibilità di gestire in unica schermata dati con rilevanza comune e specifica (se attivato lo scenario in un'unica schermata si possono gestire più scenari, imputando un'unica volta i dati comuni a tutti gli scenari e potendo specificare i valori peculiari di ogni scenario).
 * nella possibilità di poter indicare le date di validità e le differenti valorizzazioni temporali per i dati per i quali è prevista tale possibilità.
 * nella configurabilità tramite script di ogni funzionalità.

# Attivazione
La Versione 2 del data entry viene attivata in modo esplicito quando sulla tabella BR2 viene impostato il relativo flag, o implicitamente quando vengono attivate le funzioni di : 
 * scenario
 * data-effective
 * nominativo

 :  : DEC T(ST) K(BR2)

# Exit
**Controllo campi**
Dalla tabella BRZ è attivabile un programma di exit che permette di applicare dei controlli di congruenza aggiuntivi rispetto a quelli previsti a standard. La prima cosa da prendere in considerazione passando al data entry V2 è il fatto che l'exit prevista dalla versione precedente rimane attiva, ma viene deviata su un programma che supporta una radice ed un'entry differente. Per tale motivo per mantenere l'exit i programmi dovranno essere ridenominati e riadeguati.
 :  : DEC T(ST)  K(BRZ)
 :  : DEC T(MB) P(BRSRC) K(BRBR23_X)

**Aggiustamento pre/post modifica del singolo record**
Con le nuove funzioni a livello di tipo contatto/codice sarà possibile intestare più record anagrafici con differenti caratteristiche (scenario, date validità). Non essendo tale record intestato ad alcun oggetto, eventuali flussi di pre/post-modifica di aggiustamento del singolo record possono essere implementati solo tramite questa exit. I flussi dell'oggetto CN rimarranno attivi ma verranno sempre considerati a livello di contatto e non di singolo record.
L'exit ha radice BRBR24_x ed è attivabile dalla tabella BRE.
 :  : DEC T(ST) P() K(BRE)
 :  : DEC T(MB) P(BRSRC) K(BRBR24_X)

# Parametri
Il data entry V2 gestisce anche la possibilità di poter imputare i parametri in inserimento; per fare questo è però necessario indicare sull'elemento della tabella B£G nella griglia di controllo della C£E, il fatto che per il codice cliente venga accettato anche il valore **.
 :  : DEC T(ST) P() K(C£E)

# Autorizzazioni
Vengono qui descritti i vari livelli di autorizzazione presi in considerazione dal data entry.

- Tipo Contatto :  definisce il livello di autorizzazione delle azioni eseguibili a livello di tipo contatto. Tipo significato GD, funzione TABRE.

 :  : DEC T(TA) P(B£P) K(BREN01)

- Estensione :  definisce il livello di autorizzazione delle azioni eseguibili a livello di estensione. Tipo significato CD, funzione TABRI.

 :  : DEC T(TA) P(B£P) K(BRES01)

- Prospettive :  definisce il livello di autorizzazione delle prospettive (cioè dei metodi di visualizzazione dei dati). Tipo significato AZ, funzione MBSCP_SET.

 :  : DEC T(TA) P(B£P) K(BRENPRO)

- Campi :  definisce il livello di autorizzazione per la gestione e/o visualizzazione dei singoli campi all'interno di un tipo contatto/scenario.
Questa autorizzazione si riconduce al fatto di aver indicato nello script dei campi un livello di autorizzazione minimo, in caso contrario il campo è sempre gestibile e manutenibile. Tipo significato AZ, funzione TSBRG.
- L'autorizzazione su campo è attivabile dallo script di configurazione del tipo contatto, indicando tramite due apposite colonne la classe necessaria a poter visualizzare e la classe necessaria a poter modificare il relativo campo. Tale autorizzazione è indiscriminatamente attivabile sia sui campi anagrafici che sulle estensioni.


E' consigliabile impostare le autorizzazioni nel seguente modo : 
 * Raggruppando i campi sotto max dieci categorie (una per ogni riga della classe stati).
 * Attribuendo, quando la si vuole impostare, i primi 5 valori della riga per la non visualizzazione ed i successivi 5 per la protezione (Cfr. "Configurazione dello script").
 :  : DEC T(TA) P(B£P) K(CN_F)
 :  : DEC T(MB) P(SCP_SET) K(CN_F[TA.BRE]) I(**Script Campi >>)

- Scenari :  se previsti, definisce il livello di autorizzazione necessario alla gestione dello scenario. Va prevista una classe per ogni sottosettore della tabella BRG implementato. Tipo significato GD, funzione TABRG.

 :  : DEC T(TA) P(B£P) K(TABRG[SS.BRG])

A queste si affiancano le autorizzazioni relative ai dati esterni quali parametri e note, per i quali si rimanda a specifica documentazione.
- [Parametri](Sorgenti/MB/DOC/C£PARA)
- [Note](Sorgenti/MB/DOC/B£NOTE)

# Prospettive
Le prospettive definiscono i metodi di visualizzazione dei dati anagrafici. Possono essere estendibili e modificabili a piacimento (anche se è consigliabile non apportare modifiche alle prospettive previste a standard). Per una maggior comprensione si rimanda alla documentazione degli script del modulo BRENTI ("Configurazione dello script").

NOTA BENE :  se non si è in una situazione in cui differenti utenti perano su differenti dati, è consigliabile lasciare autorizzata solo la prospettiva CN_P£01, iceversa la funzionalità delle prospettive può portare a confusione.

# Dati del nominativo
I dati gestiti a livello di nominativo, sia nella gestione del nominativo stesso che di un suo soggetto subordinato, sono riconoscibili dall'indicazione di una "N" al limite esterno della riga del campo, e tali campi potranno essere gestiti solo entrando in modifica del nominativo e non a livello di soggetto subordinato, salvo attivare lo specifico flag previsto dalla tabella BR2.
 :  : DEC T(ST) K(BR2)

# Gestione file di transito
Il data entry anagrafico gestisce tutte le transazioni su un file di lavoro. Tali transazioni sono visualizzabili tramite il programma riportato di seguito. Tramite programma è anche possibile eventualmente eliminare le transazioni relative a job ormai disattivi legati a cause quali la caduta della sessione.

 :  : INI Pgm gestione file di transito
 :  : CMD CALL BRTR01R
 :  : FIN
