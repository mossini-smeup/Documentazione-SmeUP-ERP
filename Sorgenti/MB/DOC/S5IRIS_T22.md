
# Generalità

Con il termine multipostazione (nel seguito MP) si possono descrivere le situazioni in cui la risorsa destinata a eseguire il dettaglio (principale o specifica, in base a quanto impostato nello scenario) ha N postazioni indipendenti, ciascuna delle quali esegue un dettaglio indipendentemente dalle altre.
Alcuni esempi sono una macchina a pressofusione con vari ugelli, un centro di montaggio con più postazioni, ciascuna adibita ad un operatore, il forno "aperto" di una pizzeria con tante mensole separate.
La caratteristica fondamentale è che le postazioni sono indistinguibili :  nella schedulazione vengono numerate da 1 a N, senza corrispondenza con la loro realtà fisica.
Ne derivano, tra gli altri, i seguenti comportamenti :  non si dichiara su quale postazione si esegue un'attività; il congelamento avviene sulla risorsa, non sulla postazione :  può quindi verificarsi il caso che, in due schedulazioni successive, il congelamento venga assegnato a due postazioni diverse.
Il sistema cerca comunque di eseguire un "compattamento logico", caricando, a pari priorità, la postazione più bassa. Questa strategia non risolve lo slittamento di postazione, che potrebbe essere fastidioso in caso di più impegni iniziati :  se ce ne sono due, caricati in una schedulazione nelle prime due postazioni, e se nel frattempo il primo finisce, il secondo viene caricato sulla prima postazione.
Per risolvere questa casistica, le postazioni devono diventare risorse specifiche. Dato che la gerarchia è a due livelli, la risorsa che ha N postazioni, in questo caso deve diventare una risorsa generale :  non è possibile descrivere una situazione in cui un centro di lavoro ha tre macchine, ciascuna suddivisa in N sotto-macchine corrispondenti alle N postazioni. Un modo di aggirare questo problema è di 'saltare' il livello intermedio della macchina, definendola come attributo della postazione.


# Impostazioni
## Impostazione Multipostazione
Il MP si descrive impostando il numero risorse (NR) >1 nell'anagrafica della risorsa, eventualmente specifica (campo dell'archivio BRRISO0F).
Per definire che è attivo il MP, si deve valorizzare il campo "multipostazione" della tabella Gruppo Risorse (BRM).
Si deve quindi definire un gruppo risorse a cui appartengono tutte le risorse generali che hanno la proprietà di essere MP.

## Impostazione Parallelismo Rigido
Un estensione del MP è il parallelismo rigido (nel seguito PR), che descrive la situazione in cui un dettaglio viene eseguito parallelamente in modo accoppiato su più postazioni. Un esempio è il montaggio che viene eseguito da più operatori. Va precisato che, data la natura puramente logica del Mp, non può venire controllata la contiguità delle postazioni occupate da uno stesso dettaglio eseguito con il PR.
La possibilità di codificare le postazioni come risorse specifiche, in caso di PR non basta per risolvere questo problema. Bisogna infatti far conoscere al sistema la mappa delle postazioni, in modo che ne possa derivare la contiguità. Bisogna inoltre realizzare una strategia specifica di scelta della risorsa migliore, che tenga conto della contiguità, e che, all'atto della schedulazione, carichi tutte le macchine contigue necessarie.
Per descrivere il PR, bisogna impostare nella fase di ciclo il numero split (nel seguito NS), o comunque far sì che sia valorizzato il componente di carico N.6.
Per definire che è attivo il PR, si deve valorizzare il campo "parallelismo rigido" della tabella Gruppo Risorse (BRM). Naturalmente viene controllato, nella manutenzione di questa tabella, che il campo PR sia valorizzato solo se è valorizzato il campo MP.
Va tenuto presente che il NS, nella schedulazione, ha effetto di suddividere il dettaglio in più "sottodettagli" solo in presenza del PR. In caso di MP attivo senza PR, la presenza di un NS>1 non ha alcun effetto :  non si producono "sottoimpegni" ciascuno dei quali occupa in modo indipendente dagli altri una postazione del MP.
Perché si abbia questo comportamento, è necessario operare a monte :  suddividere gli impegni in uno scenario dipendente, e schedulare quest'ultimo. In questo caso gli impegni suddivisi sono ciascuno indipendente dall'altro, e quindi, se è il caso, possono occupare, in tempi diversi, postazioni diverse di un MP.
Riferirsi alla documentazione dello Split per una descrizione più completa di questo argomento.

# Note Tecniche

I flag di parallelismo rigido e multipostazione, ripresi dalla tabella BRM della risorsa generale, vengono copiati rispettivamente nei flag 23 e 24 dell'impegno risorse (S5IRIS0F), all'atto della rifasatura di questo archivio.
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL23)
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL24)


La seguente descrizione dell'implementazione standard del MP può essere utile per ispirarsi nell'impostazione di una strategia personale articolata.

Il programma che sovraintende a multipostazione è S5SMES_73, che possiede memorie private e viene richiamato con varie funzioni e metodi, in memorizzazione dei dati di input, controllo, aggiornamento e ritorno informazioni.
 :  : DEC T(MB) P(BCDSRC) K(S5SMES_73) L(1)


Le memorie private sono le seguenti : 
DSXRIS :  estensione orizzontale alle risorse (DSRISO)
DSXIRI :  estensione orizzontale agli impegni (DSIRIS)
DSISTA :  estensione verticale alle risorse :  per ogni risorsa MP si inseriscono tanti elementi quante sono le sue postazioni. Vi si memorizza l'istante di inizio disponibilità di ogni postazione. In DSXRIS, per ogni elemento, sono memorizzati i puntatori del primo e dell'ultimo elemento di questa memoria.

La memorizzazione dell'input in S5SMES_73 viene eseguita durante il caricamento delle risorse e degli impegni.

Al termine del caricamento dei dati di input vengono eseguite, in S5SMES_73 le seguenti verifiche di congruenza.
Viene controllato che, in caso di PR, almeno una risorsa tra quelle su cui l'impegno può essere eseguito, abbia NR maggiore o uguale a NS. Se ciò non accade, viene emesso un errore di segnalazione, e viene forzato il NS al valore massimo tra gli NR delle risorse possibili.
La presenza effettiva del MP viene attivata valorizzando a '1' £BCDFL(3). Se è impostato in tabella BRM ma nessuna risorsa ha NR>1 questo flag viene pulito.
La presenza effettiva del PR viene attivata valorizzando a '1' £BCDFL(4). Se impostato in tabella BRM ma è assente il MP o nessuna risorsa ha un NS>1 questo flag viene pulito.
Ricordo cha la schiera di flag £BCDFL, di 10 elementi, definita nella copy £BCDDS1, è sempre disponibile (in modifica o consultazione) a tutti i programmi di una sessione BCD.

Durante la scelta del miglior dettaglio da schedulare di un impegno (S5SMES_12E), S5SMES_73 viene richiamato in controllo, per ritornare, per ogni impegno, il dettaglio che può essere eseguito all'istante più basso e il valore di questo istante.

Durante la schedulazione del dettaglio selezionato (S5SMES_13), S5SMES_73 viene richiamato in aggiornamento, per avanzare l'istante di inizio disponibilità della (o delle, in caso di PR) postazione utilizzata.

Dato che S5SMES_73 possiede delle memorie private, viene richiamato, per ottenere informazioni, dal programma di consultazione S5SMES_DP che presenta, data una risorsa MP, come sono caricate le sue N postazioni. Le stesse funzioni e metodi possono essere richiamate da programmi personali di visualizzazione.


# Limitazioni del MP

Il MP funziona anche in presenza di batch con la solo limitazione che un batch occupi una sola postazione.

Il MP è trascurato nelle risorse a capacità infinita, e se è attivo il risparmio memoria.

La partenza mossa va usata con cautela, in quanto non è distinguibile per postazione, non essendo questa informazione presente nella dichiarazione.

Non è possibile il tiro di un dettaglio sulla stessa postazione del dettaglio tirante, in quanto non è implementata la possibilità di fissare, oltre il dettaglio da schedulare in tiro (e quindi la risorsa), anche la postazione su cui va eseguito.

Non è possibile il calcolo dell'attrezzaggio effettivo in quanto dovrebbe tener in considerazione, oltre alla risorsa, anche la postazione. Il motivo è tecnico :  la determinazione della postazione in cui viene eseguito il dettaglio, attualmente viene fatta all'atto del consolidamento del MP, che è successiva, in S5SMES_13, al calcolo dell'attrezzaggio, in quanto deve conoscere il tempo totale per avanzare l'occupazione della postazione. Come soluzione si dovrebbero separare le due funzioni, nel S5SMES_73, di determinazione postazione (da eseguire prima della tempificazione del dettaglio) e di consolidamento MP.

Queste limitazioni valgono, a maggior ragione, anche per il PR, dove, per ogni dettaglio, ci può essere più di una postazione occupata.
Inoltre non è attivato il controllo, nel Gantt di forzatura e congelamento (S5SMES_D4), il controllo che un dettaglio con NS>1 venga posizionato su una risorsa con NP>=NS, ma questo caso viene controllato successivamente, all'atto della rischedulazione, segnalato come errore non bloccante, e NS viene declassato a NP.







