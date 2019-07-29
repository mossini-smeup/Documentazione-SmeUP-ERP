# OBIETTIVO E FUNZIONALITÀ
L'obiettivo è unificare le modalità con cui gli utenti agiscono su tutti gli oggetti di Sme.up.
Per ogni oggetto viene fornito l'insieme di azioni eseguibili su di esso da un particolare utente in un particolare momento, fondendo azioni provenienti da punti diversi (gestione, B£H, B£FUN0, ...) in un'unica lista accessibile da tutto Sme.up.

### Servizio B£BASE_05
Il servizio B£BASE_05 si occupa di eseguire le azioni di menù o di gestione dell'oggetto (modifica, cancellazione ...), pertanto può essere chiamato con la funzione/metodo ESE.MNU con nel parametro Azi() in nome della voce di menù da eseguire, oppure con la funzione/metodo ESE.GES con nel parametro Azi() l'azione da eseguire (01=inserimento, 02=modifica, 03=copia, 04=cancellazione ...).

Le funzioni di richiamo delle azioni da eseguire devono essere scritte nel seguente modo : 
F(ACT;B£BASE_05;ESE.GES) .. P(Azi(xx)) ..

Per passare parametri aggiuntivi alla funzione da eseguire è possibile utilizzare il parametro AziInp() per le variabili che devono essere passate come INPUT() e AziPar() per le variabili da passare nel parametro P() nel seguente modo : 
F(ACT;B£BASE_05;ESE.GES) 1(tipo;parametro;oggetto) P(Azi(xx) AziPar(p1(a) p2(b))) INPUT(AziInp(in1(c) in2(d)))

Per le necessità relative a funzioni di test è previsto il parametro Test(1) che restituisce la funzione senza eseguirla : 
F(ACT;B£BASE_05;ESE.GES) 1(tipo;parametro;oggetto) P(Azi(xx) Test(1))

Negli script di definizione della funzione da eseguire è possibile gestire il contesto applicativo, questo viene risolto automaticamente, come l'eventuale oggetto master tipicamente nelle funzioni di inserimento. Per eventuali forzature è comunque possibile passare variabili nel il parametro EsePar(), che verranno a tal scopo passate alla £G99 nel parametro £G99DSOG.

Queste azioni vengono presentate : 
 * in Looc.up nei pop.up di oggetto.
 * in 5250, se attivate, come sostituzione/fusione delle vecchie azioni di oggetto (UP FUN) e azioni di gestione (inserimento, modifica...).
 ** lanciate con % su un oggetto, oppure da UP FUN.
 ** selezionabili da un programma di guida unificato, che sostituisce i singoli programmi di guida specifici.

Questo modulo si occupa di : 
 * (Solo in Looc.up) Costruire i pop.up di oggetto, accessibili da qualunque punto di Looc.up.
 * Fornire liste eseguibili di azioni 5250 per un oggetto (quindi non solo in Looc.up). Questa lista sostituisce la gestione e il vecchio 'UP FUN' degli oggetti.
 * Fornire un'interfaccia per il lancio diretto di alcune classi di queste azioni (ad esempio fornisce un'interfaccia standard funizzata per la gestione di tutti gli oggetti di Sme.up :  B£G99D).


# CARATTERISTICHE DELLE LISTE DI AZIONI
Le azioni di un oggetto sono : 
 * MULTILIVELLO. Ad esempio per un determinato oggetto il livello 1 è costituito dalle voci : 
 ** Scheda oggetto
 ** Gestione (apre un sottolivello)
 ** Specifiche azienda (azioni da B£H - apre un sottolivello)
 ** Navigazione (su oggetti con proprietà simili - apre un sottolivello)
 ** ...e così via
 * SENSIBILI ALL'ISTANZA dell'oggetto :  per un particolare articolo potrebbe essere attiva la modifica mentre per un altro no.
 * RIDEFINIBILI DA SCRIPT :  è suggerito un pop.up standard valido per tutti i tipi, poi per particolari oggetti questo può essere specializzato mediante script la cui sintassi è analoga a quella delle schede di oggetto.

## Ridefinizione da script
Il programma JATRE_06C costruisce la lista di azioni di un oggetto a partire da uno script.
Normalmente utilizza uno script interno definito come default per tutti gli oggetti; se trova uno script appropriato nel file SCP_SCHPOP utilizza quello :  la risalita è quella classica Tipo Parametro / Tipo / Default.

La sintassi di questi script ricalca quella di definizione delle schede, in particolare : 
 * G.SUB.SCH dichiara un elemento di pop.up (nuova voce e sua descrizione).
 * D.FUN.STD definisce la chiamata da effettuare sulla voce in questione di pop.up : 
 ** se il programma è JATRE_06C si tratta dell'apertura di un sottolivello (ramo).
 ** negli altri casi viene fatta partire una funzione (foglia).
 ** NB :  nella visualizzazione da 5250 (G18 di azioni) tutti i rami vengono esplosi al caricamento, nei pop.up invece solo al click dell'utente sulla voce.
 * Vengono gestite condizioni di IF su questi script, quindi è possibile utilizzare delle variabili per condizionare la presentazione o no di alcune voci di pop.up
 ** ad esempio "I.IF.OPE F1(&OG.K1) OP(<>) F2()" serve a caricare una parte di lista solo se è stato istanziato il codice dell'oggetto.
 ** le variabili sono gestite tramite la £G91, fare riferimento ad essa per le possibilità.

### Opzioni per la personalizzazione
 * Totale :  nello script si mettono tutte e sole le opzioni che si vogliono vedere nel pop.up.
 ** Vantaggio :  è utile per semplificare di molto le opzioni di pop.up.
 ** Svantaggio :  si perdono eventuali nuove funzionalità introdotte nei pop.up standard in seguito alla ridefinizione.
 * Integrazione :  si include il membro 'OG' nello script ridefinito ( con l'istruzione ..I.INC.MBR Fil(SCP_SCHPOP) Mem(OG) ) e a questo si aggiungono le righe di pop.up personali. In questo modo qualunque nuovo sviluppo nel pop.up verrà riportato nel pop.up personalizzato.


# CODICI PER CHIAMATE DIRETTE
Sono riconosciuti i seguenti codici per le chiamate dirette in 5250 delle azioni sotto G99 : 
 * 01..09, CT, RI :  azioni di gestione.
 * 31..  :  azioni da B£H (A-oggetto).
 * C* :  azioni di carrello.

# STRUTTURA DEI RICHIAMI
esempio
![B£BASE_056](http://localhost:3000/immagini/B£BASE_05/BXBASE_056.png)
In sintesi : 
 * JATRE_06C costruisce le liste di azioni : 
 ** viene chiamato per costruire il primo livello o sottolivelli da script, gestendo le autorizzazioni.
 ** viene chiamato per costruire sottolivelli particolari (es. gestione, funzioni comuni, ...) :  per fare questo chiede a programmi specifici.

Help JATRE_06C : 
 :  : DEC T(V3) P(ASE) K(JATRE_06C)

 * £G99 (e relativo deviatore B£G99D) : 
 ** chiama JATRE_06C per avere la lista di azioni su un oggetto e la presenta filtrando solo per le azioni A(), eseguibili in 5250. Da tale presentazione è possibile lanciare le funzioni. Questa lista sostituisce il guida e la % sugli oggetti.
 ** può essere chiamato per lanciare direttamente azioni "importanti" (es. chiamata funizzata sulla modifica di un oggetto). Questa sostituisce le chiamate ai deviatori specifici di gestione oggetto, ad esempio nelle G18.

Help £G99 : 
- [Azioni su oggetti](Sorgenti/MB/DOC_OGG/P_TSTG99)

## Attivazione in 5250 delle nuove azioni
La nuova gestione azioni in emulazione si attiva dalla tabella B£2, nel campo "Nuova gest.azioni". Scelte possibili : 
 * ' ' - non attivare la nuova gestione azioni. Pop.up sotto Looc.up e le azioni viste su 5250 non sono fasate.
 * '1' - attiva la nuova gestione azioni per TUTTI gli oggetti di Sme.up.
 * '2' - attiva la nuova gestione azioni solo per i tipi di oggetto gestiti tramite workflow (da impostazioni tabella WFA).

La nuova gestione azioni su un oggetto comporta : 
 * L'utilizzo di un guida standard (G99) diverso da quello speciale di oggetto (es. BRAR01G), capace di listare TUTTE le azioni eseguibili.
 * Che i programmi di lista supportino la nuova modalità, presentando ed eseguendo le azioni tramite G99.
 * Che le eventuali chiamate dirette alla gestione dell'oggetto (es. modifica come azione da G18) in altri programmi di Sme.up passino per il deviatore B£G99D.
In questo modo il controllo sulle azioni è affidato interamente alla G99, che può ad esempio integrarsi con il workflow e presentare come eseguibili solo le azioni che soddisfino determinati criteri (autorizzazioni, eseguibilità da workflow, ...).


## Programmi specifici
Questi programmi servono a costruire sottoinsiemi importanti delle azioni degli oggetti.

### B£GES0
Il programma B£GES0 si occupa delle azioni di gestione (modifica, cancellazione...), restituendo la lista delle chiamate da fare per gestire un oggetto e gestendo al suo interno l'integrazione con il workflow.
La gestione delle azioni di gestione abilitata nella schiera a tempo di compilazione GAZ dove per ogni classe è possibile indicare le autorizzazioni specifiche (classe/funzione), il programma deviatore della classe, i relativi funzione/metodo, i filtri sulle azioni di gestione abilitate, il parametro e le abilitazioni specifiche per i singoli device.
La azioni di gestione negli ambienti client hanno una ulteriore definizione specifica nello script B£GES0 in SCP_SET. Ogni oggetto Sme.UP per cui vengono rilasciate le azioni di gestione per gli ambienti client viene inserito nello script. Se si desidera che un oggetto continui ad avere le azioni di gestione nella modalità precedente ci sono 2 possibilità : 
- ridefinire nello script B£GES0_U in SCP_SET le singole azioni omettendo la funzione (Fun="");
- disabilitare la gestione client nel programma B£K04G_U, exit della K04.
Nel medesimo script è possibile personalizzare le azioni di gestione nel "AZI.FUN", inoltre solo per l'azione di inserimento (Ese="01") è possibile indicare nel "AZI.NEW" gli eventuali parametri aggiuntivi provenienti da un oggetto master. Per quest'ultima opzione consultare il documento relativo al "Nuovo" : 
- [Nuovo](Sorgenti/MB/DOC/B£BASE_01)
Le azioni di gestione sono anche collegate allo swipe nell'ambiente Web, Tablet e Mobile. Sono ad oggi limitate alle azioni di variazione e interrogazione. Sono comunque gestibili nello swipe come personalizzazione le azioni di menù. A tal proposito consultare il documento relativo allo "Swipe" : 
- [Swipe](Sorgenti/MB/DOC/B£BASE_02)

### WFPOP_01
Il programma WFPOP_01 restituisce le azioni di workflow su un oggetto, che vanno dalla creazione di ordini di workflow su un oggetto all'esecuzione di impegni di ordini già aperti.
Queste azioni vengono tornate sempre nel sottolivello "Gestione", ridenominato in "Workflow" qualora la gestione "classica" (ad es.BRAR01D per gli articoli) fosse sostituita da workflow (impostato dalla tabella WFA).

### JAPOP_xxx
I JAPOP_xxx sono programmi che trattano diversi aspetti delle azioni su un oggetto : 
 * JAPOP_NAV :  navigazione su oggetti con proprietà simili (tramite barratori).
 * JAPOP_ALT :  funzioni di Sme.up specifiche per tipo oggetto.
 * JAPOP_COM :  funzioni comuni per tutti i tipi oggetto (ad es. gestione in lista).
 * JAPOP_CAR :  azioni sui carrelli.

# Note varie
## Programmi B£IFxx_£A
Sono chiamati da B£FUN0_B£ per "Proprietà oggetto" (visualizzazione dettaglio da UP FUN).
Servono a evitare la ricorsione nel caso in cui siano chiamati da un F10 del dettaglio.
Potrebbero essere sostituiti da B£G99D;GES;05, che apre un nuovo gruppo di attivazione.
Problema :  oggetti per cui non c'è il dettaglio, dovrebbero chiamare la "lista campi".

## Note varie

Guida e memorizzazioni :  se chiamo il nuovo guida passando il tipo non vengono utilizzate le memorizzazioni su tipo/parametro/codice.
