# Generalità
In Sme.up la gestione della distinta base permette di definire e mantenere l'associazione tra diversi componenti ed un assieme, a sua volta l'assieme può essere trattato come componente di un livello superiore creando così una gerarchia tra gli oggetti della distinta base.
## Tipi distinte
In Sme.up è possibile costruire e gestire più tipologie di distinte. Queste possono essere riferite ad articoli ma anche a qualsiasi altro oggetto definito sul sistema.
Potremo pertanto usare le funzioni della distinta base per gestire organigrammi piuttosto che organizzazioni commerciali dei clienti ecc.

Esempi di tipi distinte possono essere i seguenti : 

- Materiali
- Attrezzature
- Componenti di un ordine di produzione
- Elenco documenti
- Impianti
- Alternative di un articolo
- Ricambi associati ad un ricambio


Il tipo distinta è codificato nella tabella BRL che ne definisce tutte le caratteristiche principali di comportamento.
La distinta che descrive la composizione base di un prodotto si chiama "ART" e rappresenta la distinta tecnica.

_3_Nota bene :  in Sme.up la distinta di tipo ART è quella fondamentale e gestita di default in tutti i moduli di Sme.up che trattano in qualche modo la distinta (es. esplosione distinta all'interno dell'MRP).

## Gestione distinta
Per attivare la gestione della distinta si parte dal seguente formato guida : 

![BR_02_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRDI01/BR_02_01.png)
da notare che sotto al solito campo per le opzioni esiste un secondo campo in cui inserire : 

- _3_IM, se si vuole gestire la distinta in implosione (nella lista successiva vengono presentati i padri dell'oggetto in input)
- _3_ES, se si vuole gestire la distinta in esplosione (nella lista successiva vengono presentati i figli dell'oggetto in input).

Se il campo è vuoto si assume esplosione.

Dopo aver inserito i dati di input si accede al formato successivo dove vengono presentati gli oggetti collegati a quello in input (padri se implosione, figli se esplosione) : 

![BR_02_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRDI01/BR_02_02.png)
Il formato della lista dipende da una impostazione fissata nella tabella BRL (tipo distinta) e può essere : 

- _3_Sintetico, come da esempio precedente, dove vengono visualizzati i dati principali di una gestione distinta e di uso comune nella maggior parte dei casi
- _3_Completo, vedi esempio successivo, dove vengono presentati dati aggiuntivi, (in emulazione5250 la visualizzazione completa è su 2 righe, mentre in formato grafico ci si sposta con la barra di scorrimento orizzontale)
- _3_Esteso, dove vengono presentati i dati in un formato a 132 colonne


![BR_02_03](http://localhost:3000/immagini/MBDOC_OGG-P_BRDI01/BR_02_03.png)
Il tasto F15 serve per passare da un tipo di visualizzazione all'altro.

Utilizzando le normali opzioni standard si accede al formato di dettaglio dove sono
presentati tutti i campi per la gestione di un singolo legame di distinta : 

![BR_02_04](http://localhost:3000/immagini/MBDOC_OGG-P_BRDI01/BR_02_04.png)
### Descrizione dei campi

- _2_Sequenze (Sequenza 1 , Sequenza 2), Sono definibili per un tipo distinta due diverse sequenze, una come prefisso e l'altra come suffisso. Esse impongono un ordinamento diverso da quello per codice e permettono di associare più volte lo stesso componente in un assieme, nel caso in cui intervengono in operazioni diverse o hanno date di validità differenti.
- _2_Periodo di validità (Data inizio validità , Data fine validità), Definisce se un legame di distinta deve essere considerato in un particolare intervallo di tempo, assegnandogli di conseguenza un periodo di validità. Le date di inizio e di fine sono comprese. Se un componente si usa fino ad oggi, la data di validità del suo sostituto deve essere da domani. Se non vengono inserite le date, il componente assume validità assoluta.
- _2_Stato del legame, Permette di indicare la significatività del legame. Nella tabella BRL è possibile stabilire lo stato "minimo" per la validità di un legame
- _2_Criterio di selezione, Se compilato permette di definire la validità del legame, il criterio di selezione è descritto nella tabella BRS dove sono indicati i programmi specifici di selezione ed i relativi parametri da utilizzare dato un criterio. Dato il criterio di selezione si può accedere (inserendo un carattere nel campo a lato) ad una mappa in cui inserire i parametri per la selezione.
- _2_Operazione impiego, Indica l'operazione nella quale si utilizza il componente. La funzione di questo campo è collegata  alla gestione cicli (si veda l'apposita documentazione).
- _2_Coefficiente di impiego, Indica la quantità, nell'unità di misura dell'oggetto, del componente presente nell'assieme. Questa quantità è sempre riferita al fabbisogno per una singola unità dell'assieme a cui appartiene.
- _2_Quantità lotto, Permette di aumentare la quantità necessaria di n. unità, senza intervenire sul coefficiente d'impiego. _3_Esempio :  Coefficiente di impiego = 5, Qtà per lotto = 9, Ordine di produzione da 1000; il fabbisogno è 5009 (= 5 X 1000 + 9). Potrebbe indicare la qtà scartata ad ogni avviamento della produzione.
- _2_Percentuale di rettifica d'impiego, Indica la percentuale del componente che viene consumata durante la lavorazione (es. quantità del componente scartata mediamente durante la lavorazione). Le quantità vengono aumentate della percentuale indicata per sopperire a tale perdita.
- _2_Rettifica tempo, Indica al sistema di pianificazione il numero di giorni con cui anticipare la richiesta di disponibilità del componente. Tale numero sostituisce il lead time tipico dell'assieme definito nei parametri di pianificazione. Calcola l'arretramento degli impieghi a partire dalla  data di fine pianificata per l'ordine di produzione dell'assieme superiore. In pianificazione si usa per differenziare la data di fabbisogno di un componente rispetto alla data normalmente calcolata che è uguale a DATA DI FABBISOGNO DELL'ASSIEME meno LEAD TIME DELL'ASSIEME.
- _2_Disegno, Solo descrittivo. Permette di indicare un disegno di riferimento.
- _2_Posizione, Solo descrittivo. Permette di indicare la posizione del componente all'interno del disegno di riferimento.
- _2_Legame interno/esterno, Indica se un legame deve essere escluso o incluso quando si chiede una scansione di conto lavoro. Ciò permette ad esempio di non inviare un certo componente in conto lavoro in quanto montato successivamente all'interno.
- _2_Tipo legame, Normalmente viene determinato dal tipo parte articolo, è possibile forzarlo a fittizio, fittizio per produzione o fittizio per lavorazione esterna (fittizio significa che durante l'esplosione di distinta il sistema lo attraversa per andare ai suoi componenti).
- _2_Rilevanza per ricambi, Indica che il legame è significativo dal punto di vista dei ricambi. Utilizzabile per parzializzare le stampe e/o le interrogazioni.
- _2_Nota, Solo descrittivo. Permette di inserire un commento o una qualsiasi informazione libera.
- _2_Note strutturate, Ad ogni legame si possono associare delle note secondo la gestione standard.
- _2_Altri valori, Questo campo permette di attivare la compilazione di altri campi in cui scrivere valori aggiuntivi :  valori di quantità, di lunghezza, ulteriori coefficienti di impiego.


### Gestioni dal formato guida

- _2_Metodi di ricerca, In qualsiasi punto nel quale va indicato un codice di oggetto, si possono utilizzare alcuni particolari metodi di ricerca del codice :  oltre ai tradizionali "!", che permette di ricercare nell'elenco ordinato per codice, e al "?" che permette la ricerca ordinataper descrizione, è possibile ricercare con il comando "/" solamente tra i codici che hanno già associato una distinta. Tali metodi di ricerca si estendono ovunque si debba selezionare una distinta, non solo nella gestione.
- _2_Manutenzione in esplosione/implosione, È possibile procedere alla manutenzione delle distinte in due modi :  attivando la funzione di esplosione si agisce nella direzione dei componentidi un assieme; al contrario attivando l'implosione, si risale agli assiemi a cui è associato il componente.  Se non si specifica tale opzione si agisce di default in esplosione.
- _2_Modifica, cancellazione e visualizza, Sono le classiche funzioni di gestione, proprie del formato guida. La funzione visualizza permette di visualizzare l'esplosione o l'implosione di un assieme. Su schermo vengono presentati tutti i componenti con il relativo coefficiente d'impiego, ma non si può intervenire su di essi. Per ognuno di essi è possibile effettuare delle operazioni, tramite il comando di funzione riga, la cui spiegazione è contenuta nell'apposito paragrafo. La funzione modifica permette di modificare i componenti di un assieme, oltre che a visualizzarli. La funzione cancellazione elimina tutti i componenti contenuti nell'assieme indicato, chiedendo naturalmente una conferma dopo aver visualizzato quali legami si stanno per cancellare.
- _2_Taglia e incolla, Mediante questa funzione è possibile eliminare uno o più componenti da una distinta e portarli in un'altra distinta.
La copia può essere effettuata con o senza selezione, nel primo caso vengono visualizzati gli oggetti da trasferire mentre nel secondo caso il trasferimento viene effettuato di massa.
Nel caso siano già presenti alcuni componenti nella distinta di destinazione, si apre una particolare modalità di inserimento per gestire i componenti comuni ad entrambi gli assiemi, che prevede le seguenti opzioni : 
-- Aggiunta :  affianca il nuovo componente a quello già presente assegnandogli un diverso numero di sequenza
-- Sostituzione :  sostituisce il componente inserendo il coefficiente d'impiego di quello entrante
-- Somma coefficiente impiego :  somma il coefficiente d'impiego del componente già presente con quello entrante
-- No sostituzione :  non modifica il coefficiente d'impiego del componente presente
- _2_Copia, Permette di duplicare una distinta verso un'altra. In modo simile alle funzioni di Taglia/Incolla possiamo indicare se aggiungere, sostituire, sommare o non sostituire, quando un componente è già presente nella distinta.
- _2_Mirror, Permette di eseguire la comparazione tra due distinte. Esse vengono visualizzate in contemporanea e sono distinguibili in quanto una delle due viene evidenziata. Quando sono presenti componenti comuni ad entrambe, essi vengono affiancati, per poter notare le differenze.
Tale confronto può essere eseguito in esplosione/implosione anche tra distinte di diversa tipologia.


### Gestioni dalla lista
Nel formato di lista della distinta base, dove, a seconda se si gestisce in esplosione o implosione, sono elencati i componenti o gli assiemi, è possibile compiere delle operazioni su una singola riga, cioè su un singolo legame.

A livello di riga si agisce solamente sul componente e sulle caratteristiche del legame a quel livello di distinta.

Oltre alle consuete funzioni di modifica, copia, cancellazione e visualizzazione si segnalano le seguenti opzioni particolari : 

- _2_Copia + svuo (Copia con svuotamento) :  Copia in un nuovo legame annullando la quantità del legame originale fino all'eliminazione, e visualizza il vecchio e il nuovo legame
- _2_Modifica + C (Copia e modifica) :  Visualizza e permette di modificare sia il legame originale che quello da creare
- _2_Esplosione/Implosione :  Permette di passare ad un livello successivo senza perdere quello in corso a cui si ritorna mediante F12. Se la distinta è cambiata, prima di cambiare di livello il sistema chiede se si vogliono confermare le modifiche effettuate


## Utilizzi in Sme.up
La distinta costituisce uno degli elementi fondamentali di SME_up. È utilizzata in particolare in : 

- Calcolo del costo standard
- Calcolo dei fabbisogni
- Generazione degli impegni di un ordine di produzione
- Pianificazione MRP

## Note particolari
Distinta in manutenzione :  è possibile che il programma impedisca l'accesso ad una distinta in quanto un altro utente sta modificando la stessa distinta. Attendere fino a quando la distinta si libera. La caduta di sistema può lasciare la distinta bloccata. Per sbloccare la distinta si può lanciare un programma di utilità. Questo programma è raggiungibile dal menù principale della Contabilità : 
 * C5 KEEP_up General ledger > Contabilità Generale  > Gestione Contabilità >  Gestione Log
 * Il programma presenta una lista di possibili log, quelli che interessano la gestione distinte iniziano per _3_BK_BRDIST, selezionare quello di interesse, il sistema presenta la lista dei record bloccati per manutenzione, con l'opzione 04 cancellare quello da sbloccare. **Nota**, può succedere che non si vedano elementi che iniziano per _3_BK_BRDIST, questo capita quando la tabella _3_B§L non è aggiornata
 * In alternativa, da riga comandi lanciare il programma _3_TSTG81, Funzione = GESLOCK, Metodo = 04, selezionare "Tipo vincolo" = 1 (pessimistico), il sistema presenta la lista dei record bloccati per manutenzione, con l'opzione 04 cancellare quello da sbloccare
