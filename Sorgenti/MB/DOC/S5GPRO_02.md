# Ciclo di gestione dei progetti

## Procedura definizione progetto

Sono disponibili due aree di accesso ai progetti : 
* la gestione dei dati logistici (voce di menù Progetti o Gestione Progetti)
* la visualizzazione dei Gantt dei progetti attivi (voce di menù Schedulatore)

L'area "Progetti" permette di impostare i dati, definire le fasi, le aree di lavoro(CDL),  i tempi per la schematizzazione del progetto...
L'area "Schedulatore" lancia il motore di schedulazione per i progetti attivi mettendo in sequenza le attività, calcolando i tempi ed impegnando le risorse stabilite. Da questo si ottiene il Gantt di progetto.
Lo schedulatore è richiamabile anche dalla scheda richiamabile anche dall'area Progetti 

### Menù Progetti
Attivando il comando si accede all'ambiente di gestione progetto. Inizialmente presenta l'elenco dei progetti attivi/schedulabili. Tra i campi è presente il flag di "spunta" di fianco alla MF o MI nello schema iniziale del progetto che identifica che c'è una nota che posso editare, modificare, creare, cancellare. (Nota tecnica quando modifico una nota, ricordarsi di salvarla con "conferma").

Analizziamo i primi due pulsanti : 

**Crea nuovo progetto** :  attiva la procedura di creazione del progetto stesso, passando attraverso la definizione delle MF, MI, definizione tempi e risorse, etc.
**Scelta progetto** :  mi permette di scegliere una confermando (F6 o click sulla freccia verde) presenta la lista dei progetti attivi coinvolti nella attività di pianificazione dello schedulatore. Per capire se un progetto è schedulabile controllare sulla lista lo stato "Attivo". Partendo da questa lista è possibile analizzare il singolo progetto, modificarlo etc.

Selezionandone un record (doppio click sul progetto), si apre una nuova scheda in cui la sezione in alto mi illustra brevemente la schematizzazione del progetto selezionato (Macrofasi, Fasi, Milestone). Nella scheda del progetto selezionando una riga /fase si apre una sezione che illustra gli eventuali vincoli espressi tra le Macrofasi. Esiste inoltre anche una sezione che mostra le risorse assegnate per la fase scelta.

### Stati del progetto
Nella lista dei progetti gli stati 80/81/82 indicano che il progetto è in stato chiuso/concluso. Questo significa che lo schedulatore non considererà più le sue fasi. Per visualizzare solo i progetti attivi è quindi possibile filtrare per gli stati <80. Attenzione ai progetti in stato 00 (non creati/modelli).
Esistono due stati "speciali" /non attivi : 

* lo stato 04 nel caso in cui un progetto è stato inserito ma viene considerato come modello e quindi da non schedulare.
* lo stato 05 nel caso in cui un progetto è definito come progetto **interno**, in cui posso è possibile dichiarare le ore ma  tale progetto non deve essere tra quelli  schedulabili.


### Milestone
I Milestone (**MI**) devono avere un vincolo alle macrofasi(**MF**) altrimenti iniziano dalla data di avvio del progetto. La cosa migliore è definire sempre una data di inizio e fine. I milestone vengono indicati come di 8 ore (una giornata) per far si che siano visibili sul Gantt, anche se non ha nolto senso specificarne la durata.

Quando si crea un Milestone, occorre sempre esprimere come centro di lavoro il codice **00100** questo perchè il milestone deve essere considerato come un' attività da non attribuire a nessuna risorsa specifica. Un milestone risulta solo come un check di controllo per notificare all'operatore che in tale data la situazione deve essere quella stabilita in pianificazione dal progetto.
Attenzione a non vincolare un MI ad una Macrofase(MF) perchè si possono creare problemi di visualizzazione nel caso in cui la MF vada in ritardo. Quindi una MF non deve essere in grado di spostare una MI per questo è meglio non vincolarla.
**Nota** Le MF non devono avere una data di fine, mentre le MI devono averla.
**Vincoli** su MF :  una MF può avere il vincolo su più MF. Esempio :  la MF "verifica progettazione" potrebbe avere un vincolo sulla progettazione meccanica e progettazione elettrica.

### Gestione macrofasi
Per sospendere una MF devo specificare come stato il valore 81 . Lo schedulatore processerà il progetto ignorando la MF. Per renderla nuovamente attiva devo cambiare lo stato e mettere il valore 10 .
Per rifasare un progetto dopo le modifiche su MF, MI, Fasi etc. (qualsiasi modifica ma specialmente quelle che coinvolgono cambiamenti o cancellazione di risorse, ore, date, etc) devo eseguire il comando : 
"Rifasatura impegno progetti". La finestra che si aprirà, andrà compilata nel modo seguente : 

* Tipo Documento :  BC
* N° Documento :  inserire il codice commessa visto dal sistema (Es. BC090007)
* Impegni risorse :  contrassegnare con X
* Opzione "con pulizia" da contrassegnare con X"

e poi confermare con F6.


**NOTA** 
Quando si fanno delle modifiche nelle date o nelle fasi di un progetto in cui delle risorse erano già state assegnate, occorre "rifasare gli impegni dei progetti" cioè riassegnare le risorse indipendentemente da quanto già specificato nei progetti stessi. Per fare questo occorre lanciare il comando " rifasa impegno progetti", specificando come tipo di documento "BC" numero documento :  specificare il codice progetto o lasciare vuoto per considerarli tutti, e poi flaggare entrambe le pulizie dei dati precedenti. Successivamente posso lanciare lo schedulatore e veder che non dia errori. In tal modo i risultati dovrebbero essere corretti.


### Cancellazione fasi
Per cancellare una fase procedo come segue : 
- Seleziono MF
- scelgo la funzione dal pulsante **Modifica Macrofase**
- seleziono con codice 04 (Cancellazione)
- da pulsante nella videata sotto a destra scelgo Annulla


E' conveniente specificare sempre l'operatore quando si crea una MF (con le relative ore). Possibilmente fare in modo che la risorsa specificata non cambi neanche come numero, altrimenti devo dividere la MF in due MF.

### Gestione risorse e calendario
Dalla scheda principale in cui si vedono i progetti esiste un pulsante di Gestione dei centri di lavoro . Tramite questa funzione posso anche creare nuovi CDL/Aree di competenza. Ad esempio esiste il centro di lavoro Software per identificare chi si occupa di PLC e sviluppa il software. Parallelamente sono stati associati a questo CDL Software gli operatori che si occupano di sviluppare la parte software
Per fare aggiungere gli operatori ad un CDL si deve entrare nella funzione disponibile tramite il pulsante Gestione operatori .

Esiste una funzione di calendario per impostare i punti di ferie/sospenzione delle attività. Nel Calendario la sigla CDL identifica i "centro di lavoro" o aree di competenza mentre OPE indica le persone coinvolte nei progetti.

La gestione calendario risorse/CDL mi permette di fissare per tutto il gruppo di persone che fa parte dello stesso centro di lavoro (es. gruppo montatori meccanici, montatori elettrici, ufficio tecnico etc.) o per il singolo operatore l'orario di lavoro (es 8 ore) per settimana (specifico se sabato e domenica sono lavorativi e quante ore) ed eventualmente le ferie etc. Tutto ciò è uguale per tutti gli operatori del CDL.E' possibile definire il calendario della singola risorsa perchè il piano ferie può essere diverso e così anche le ore di lavoro (straordinari). Posso specificare le festività durante l'anno, escluse sabato e domenica, che rientrano già nella definizione del calendario settimanale. Il Calendario per operatore serve per definire le ferie, permessi etc, che sono specifici dell'operatore e non uguali per tutti.

### Sospensione risorse

Le risorse/OPE che non devono essere calcolati dallo schedulatore vanno sospesi. Per far questo basta impostare lo stato 80 alla risorsa da sospendere. Se uno di quelli che stai per sospendere erano già associati ad un progetto nell'entrare nello schedulatore ti viene segnalato nella gestione errori :  esiste un pulsante sulla destra che ti indica la presenza o meno di errori. Se presente l'errore e si vuole eliminarlo basta rifasare la singola macrofase per fare in modo che l'operatore sospeso non venga più considerato.

### Dichiarazioni

Esiste un'area "Dichiarazioni su fase" in cui è possibile dichiarare a consuntivo che un certo numero di ore è stato già effettuato su quella fase, specificando da quale operatore.
Al momento del calcolo dello schedulatore, verranno considerate le ore già dichiarate come fatte. Questo permette di fare rientrare quei progetti che sono già partiti e che posso schedulare comunque.
Va tenuto conto che la somma della dichiarazioni fatte, deve dare il valore temporale di durata della fase stabilità nela creazione del progetto.
Quando viene dichiarato il 100% delle ore allora termina la MF e scompare dal Gantt. Da sottolineare che la Dichiarazione su Fase è il modo per far "chiudere" le attività sulla fase stessa e far avanzare il progetto.

Durante le dichiarazioni occorre tenere conto delle seguenti due possibilità : 

* la fase è stata "eseguita" nelle ore stabilite come budget
* la fase è stata "eseguita" totalmente rispetto alle ore stabilite inizialmente (budget)

Nel primo caso va a vantaggio del progetto e tutto verrà anticipato. Nel secondo caso devo invece intervenire modificando le ore di budget della fase e dichiarare le ore effettivamente fatte a consuntivo. Così facendo aggiorno la schedulazione del progetto. Esiste un meccanismo di memorizzazione dei cambiamenti delle ore di budget che permette di tenere traccia dei vari accorgimenti che vengono man mano fatti differentemente a quanto stabilito inizialmente.

A livello di progetto posso impostare una MI per fissare l'intervallo di tempo necessario a fare gli ordini fornitore e avere in casa il materiale.
Siccome il picking può essere fatto in più riprese (se il materiale non è tutto disponibile preparo quello che ho e inizio l'assemblaggio meccanico ed elettrico), allora metto un altri MI per l'inizio dell'assemblaggio e non li lego alla conclusione della fase di picking.
Schedulatore

### Schedulatore
Finalità Schedulatore :  fornire uno strumento per pianificare l'attività entrante (nuove commesse) sia in fase di preventivazione che dopo l'acquisizione delll'ordine al fine di tenere sotto controllo lo
stato di avanzamento della commessa, simulando scenari differenti di gestione risorse per risolvere problemi di tempi di consegna.
Lo stato di avanzamento necessita il carico delle ore svolte da ogni singolo operatore coinvolto (assegnazione risorse) nel progetto da parte di qualche responsabile di reparto. Il progetto sarà aggiornato ogni volta che inserisco nel stime le ore già fatte dai diversi operatori. Se inserisco le ore settimanalmente, il progetto sarà aggiornato settimanalmente.

Questo strumento è anche utile per fare la raccolta ore ed il calcolo delle ore generale degli operatori al fine di quantificare il costo della commessa.


Per eseguire lo schedulatore premo sul pulsante Lancio Schedulatore -> F06 (per conferma dei parametri di schedulazione) -> Memorizza (per far eseguire ed aggiornare l'assegnazione risorse) -> Lista commesse e seleziono la commessa che voglio (doppio click) -> visualizzo il grafico delle fasi
Sul pannello a destra trovo i comandi per lo zoom in o zoom out del grafico.
Sulla riga delle icone di comando in alto trovo " mostra/nascondi note" che mi attiva la visualizzazione delle note delle singole MF quando passo sulla MF sul Gannt col mouse.
Cliccando sul bottone "key Progressivo" e poi MB3 posso selezionare cosa visualizzare sul grafico.
Cliccando sull'area libera del grafico -> MB3 -> Impostazioni -> Livello di presentazione  :  1- Fasi, 2- Sottofasi, Seleziono3° campo e confermo :  Sintesi
Sulla scheda "Sintesi Risorse" (elenco degli operatori col loro impegno nel progetto) seleziono un CDL (colonna a fianco dell'operatrore) -> MB3 -> o Grafico Gannt totale o Gannt CDL o Gannt operatrore
Gantt totale :  visualizza il Gantt di tutti gli operatori su tutti i progetti attivi.
Gantt CDL :  visualizza il grafico con l'impegno delle persone di quel CDL sul progetto corrente
Gantt operatore :  visualizza il Gantt dell'operatore illustrando il suo impegno nelle diverse fasi in tutti i pogetti atttivi

### Priorità progetti
Esiste il concetto di priorità (01 max - 99 minima) che permettere allo schedulatore di considerare prima le attività legate ai progetti con priorità maggiore. Il secondo parametro che prende in considerazione il motore di scheduling sono le date di consegna o le scadenze delle MI e delle attività che sono state assegnate nel progetto.


Lo schedulatore assegna automaticamente delle risorse secondo le indicazioni stabilite nella definizione iniziale del progetto.E' possibile introdurre forzatamente una risorsa tramite il pulsante Assegn risorsa forz. alla fase XXX presente nella scheda del progetto. Per far sì che lo schedulatore attribuisca le risorse (persone) alle fasi occorre uscire dalla videata principale dello schedulatore salvando l'impostazione o salvandola in uscita o utilizzando il comando di memorizza .


Nel gantt risorse/CDL se ho introdotto delle ferie a livello gruppo operatori(OPE) o centri di lavoro, la fase che va a interessare il periodo che comprende anche le ferie viene allungata oltre il periodo specificato. Per capire che il periodo non è lavorativo nelle prossime versioni dello schedulatore verrà introdotto un colore diverso sulla linea per capire che non c'è attività lavorativa durante quella fase.
Nella rappresentazione con l'elenco degli operatori la "Data Fine" indica quando la risorsa sarà disponibile. Attenzione :  non significa che sarà occupata per tutto l'arco di tempo da oggi alla data di fine. Potrebbe avere buchi di attività liberi nel periodo. Basta guardare i valori indicati di "H occupate" e "H di buco".
La somma delle Ore occupate più Ore di buco identidica le ore "lavorative" da oggi a "data fine" tenuto conto delle festività e delle ferie inserite nel calendario. Posso anche guardare il valore della variabile " % disponibilità".
"H carico" :  identifica le ore di lavoro che lo schedulatore ha attribuito all'operatore.
Tra le varie visuali risulta utile quella in cui sono presenti tutti gli operatori insieme per vedere subito a colpo d'occhio le settimane di disponibilità degli operatori.
