## Definizione
La gestione delle dichiarazioni di intento nel modulo "Spedizioni e Ricevimenti" viene effettuato attraverso due azioni : 

* Utilizzare il corretto assoggettamento in fattura;
* Riportare i riferimenti della dichiarazione o delle dichiarazioni impiegate per l'utilizzo dell'esenzione.

## Configurazione Tabelle
* **V51** :  attivando il campo descrittivo "Stampa controllo fatture" il sistema in sede di prestampa, stampa e ristampa genererà uno spool all'interno del quale ci sarà scritta una *D accanto ai documenti dei clienti dei quali sono presenti dichiarazioni d'intento per importo, è opportuno verificare che non ci siano collegamenti o invii mail automatici sugli spool prodotti con la stampa fatture;
* **V62** :  in questa tabella verrà configurata la modalità secondo la quale si vorrà gestire le dichiarazioni d'intento ricevute.
* **IVA** :  spuntando il flag "Controllo dichiarazioni di Intento" nel codice assoggettamento dedicato in modo che il sistema possa capire quando vi è il bisogno di agganciare una dichiarazione d'intento. E' inoltre fondamentale che sia impostato il campo "Non Soggetta".

## Primo Utilizzo
Se sono già arrivate dichiarazioni d'intento per importo prima dell'aggiornamento dei programmi è necessario lanciare il programma BRUT14A per ricostruire gli utilizzi pregressi.

**NOTA BENE** :  è prerequisito per questa funzione che i documenti stampati, ma non contabilizzati, vengano contabilizzati.
**NOTA BENE 2** :  si consiglia di effettuare inoltre questa verifica :  da una parte prendere la stampa di log del programma BRUT14B e dell'altra la scheda di controllo degli utilizzi (citata a seguire). Cercando " W " nella stampa si dovrebbe trovare corrispondenza perfetta con le righe della scheda che hanno nel campo "Descrizione" il valore "Registrazione non assegnata".

## Vertenze tecniche
E' importante che eventuali logiche personali introdotte nei pgm V5FA01CL, V5FA02CL e V5FA01S, vengano poi riportate (se necessario) nei pgm V5FA00E, BRBRO2_SM, BRIN13L, BRDINT_17, in particolare per quel che riguarda il trattamento di testate e righe (utilizzo particolare di campi/tabelle o flag non previsti dallo standard). Queste considerazioni si possono omettere, solo nel caso in cui fra le modalità descritte a seguire si scelga la modalità "Solo controllo".

## Modalità di Applicazione
Prima di descrivere in che modo sarà possibile intervenire sulle dichiarazioni d'intento è opportuno evidenziare che tutte le modifiche necessarie sulle associazioni non saranno possibili una volta che avremo contabilizzato le fatture, in quei casi, prima di effettuare qualsiasi operazione dovrò andare a togliere le fatture oggetto di modifica dalla contabilizzazione, solo dopo questo passaggio potrò nuovamente collegare o scollegare i documenti e, successivamente, ricontabilizzare le fatture.

Le suddette azioni possono concretizzarsi nelle seguenti modalità : 

- In fattura :  questa modalità prevede che in fase di stampa fattura venga calcolata ed applicata l'esenzione ad ogni documento. Sulla base di tale applicazione verranno inoltre scritti in automatico i riferimenti della dichiarazione.
- Manuale :  questa modalità prevede che tramite apposita scheda di controllo l'utente possa collegare manualmente una fattura ad una o più dichiarazioni. Nel momento in cui verrà applicata l'attribuzione, la fattura verrà resa esente ed in stampa fattura verranno stampati i riferimenti della dichiarazione.
- Prestampa :  questa modalità prevede solo che nella pre-stampa, stampa e ristampa, venga segnalata la presenza di dichiarazioni per importo.

Si può anche decidere di non attivare nulla, in questo caso gli utenti, dovranno occuparsi in autonomia di controllare ad ogni fatturazione la presenza ed i limiti delle dichiarazioni e, dove opportuno, potranno procedere con la modifica degli assoggettamenti e l'inserimento dei riferimenti delle dichiarazioni all'interno delle note.

Ognuna di queste scelte corrisponde ad un valore indicabile nella tabella V62 nel campo "Dichiarazioni di intento", di default non è attivo nulla.

_1_NOTA BENE :  Dalla tabella V62 è inoltre importante valutare e decidere quale data inizio validità prendere in considerazione, fra queste due alternative : 
* Data acquisizione dell'agenzia :  è la data in cui l'agenzia acquisisce la dichiarazione
* Data di protocollo :  è la data in cui viene registrata la dichiarazione nel sistema e che dovrebbe corrispondere alla data di verifica della dichiarazione ricevuta.
Si sottolinea che di default viene utilizzata la prima, che tende a "favorire" il cliente che ha emesso la ricevuta.

## _1. Modalità In fattura_
Eseguendo l'emulazione stampa fatture, sia normale che interattiva, a seconda della funzione che intendiamo lanciare e rispettando le istruzioni della modalità automatica selezionata nella tabella V62 il sistema si comporta nei seguenti modi : 

* **Prestampa** :  in questa fase il programma non considera la situazione aggiornata della disponibilità di plafond e tutte le prestampe verranno emesse con IVA. Tuttavia i riferimenti della dichiarazione d'intento che verrebbe agganciata alla fattura vengono scritti ed evidenziati all'interno del documento, questi saranno poi riportati anche nella fattura vera e propria qualora ci siano le condizioni di plafond. Se attivato il flag nella tabella V51 **"Stampa Controllo Fatture"** potremo verificare in modo immediato le fatture su cui si attiverà il controllo delle dichiarazioni d'intento, per fare ciò andremo ad aprire lo spool di stampa del file di controllo e vedremo il simbolo **"*D"** accanto all'importo dell'imposta qualora per quel cliente avessimo registrato una dichiarazione d'intento per importo. Se si usa la stampa interattiva, i documenti in questa condizione particolare verranno invece evidenziati con un colore diverso. Questo vale anche per tutte le condizioni di stampa riportate a seguire.

![V5SP10_05](http://localhost:3000/immagini/V5SPRID_10/V5SP10_05.png)
* **Stampa** :  lanciando questa funzione verranno controllate una fattura alla volta e quando sentirà la presenza di una dichiarazione d'intento per importo andrà ad applicare l'assoggettamento di esenzione IVA fino al momento in cui il plafond risulta essere sufficiente per coprire il totale imponibile IVA. Quando sarà possibile indicare l'esenzione a tutto l'importo il sistema scriverà l'assoggettamento in testata, in modo da permettere a tutte le righe del documento di ereditare l'assoggettamento. Viceversa, qualora solo una parte della quota imponibile può essere inclusa nel plafond, il sistema andrà ad aggiornare una riga alla volta e oltre a modificare in ogni riga l'assoggettamento, registrerà l'utilizzo del plafond. E' importante specificare che l'imponibile oggetto di controllo includerà solo quella quota d'importo imponibile IVA, se all'interno di un documento dovessero esistere righe con assoggettamento esente per altri motivi (imposta di bollo, ecc..) non verranno comprese nell'imponibile totale. Una volta effettuata la stampa, il file di controllo presenterà la **"*D"** accanto ai documenti che effettivamente sono stati associati ad una dichiarazione d'intento.

* **Ristampa** :  questa funzione ripete esattamente e nello stesso ordine le istruzioni della funzione stampa e permette la replica delle fatture, comprese quelle che hanno agganciato una dichiarazione d'intento. Anche effettuando la ristampa verrà presentato un file controllo con la **"*D"** esclusivamente accanto ai documenti associati.

### Note di accredito e Dichiarazioni per singola operazione
Le due casistiche in oggetto sono escluse dall'applicazione automatica, per esse andrà applicata in ogni caso la modalità manuale, descritta a seguire. Quindi se anche si sceglie la modalità automatica, sarà necessario che qualcuno all'interno dell'azienda in fase di fatturazione si occupi di verificare le eventuali modifiche da apportare manualmente, in merito alle note di accredito e le dichiarazioni per singola operazione.

### Assoggettamenti presenti sugli ordini
Si aggiunge inoltre che in questa modalità è importante che i documenti da stampare arrivino con l'assoggettamento originale previsto per l'operazione e non già con l'esenzione applicata. Qualora sui propri archivi relativi agli ordini sia già stata applicata l'esenzione (cosa non prevista dallo standard, ma possibile in presenza delle dichiarazioni di intento per periodo), è necessario che esenzione venga annulla al fine di poter produrre i documenti da stampare con l'assoggettamento previsto per il tipo di operazione.
Se questo non avviene può succedere che la fattura venga stampata con l'esenzione anche quando non è più presente un plafond. Non è infatti previsto alcun automatismo all'inverso, per il quale in caso di splafonamento venga riapplicato l'assoggettamento originale.

## _2. Modalità Manuale_
La modalità manuale sarà accessibile in due modi distinti : 

* cliccando F14 sulla testata di un qualsiasi documento e selezionando la voce "Controllo Dichiarazioni di Intento";
* dal comando di gestione posto a sinistra delle righe quando ci troveremo all'interno di schede che hanno come oggetto le dichiarazioni d'intento.

_Modalità Manuale attraverso la scheda di controllo_

Una delle schede che permette la gestione manuale delle dichiarazioni d'intento è la _Scheda di controllo.
Questa scheda, qualora avessimo ricevuto e registrato almeno una dichiarazione d'intento, le raggrupperà per partita IVA seguita da denominazione sociale del cliente e per ognuno di questi sarà possibile leggere gli importi delle dichiarazioni e delle fatture ad esse agganciate, evidenziando inoltre la quota residua e la percentuale di utilizzo. Le dichiarazioni d'intento saranno riportate complete di numero di protocollo e data di ricezione. Oltre a questi dati, per favorire un ulteriore controllo in sede di stampa fatture, la scheda permette di conoscere : 

* il numero della fattura che viene scritta nella colonna dedicata;
* l'importo totale dell'imponibile;
* segue la colonna dove vi è scritta la quota d'imposta;
* dopo le colonne sopra riportate ne troviamo una quarta contenente i valori totali delle precedenti.

E' opportuno sottolineare che questa scheda potrà tuttavia presentare squadrature con la presenza di bolli poichè avviando solo la prestampa fatture potrebbero essere accorpate tutte le bolle che presentano caratteristiche comuni e, in conseguenza a ciò, l'imposta di bollo sarà unica per quel gruppo di documenti.

Sempre in questa scheda, accanto ad ogni riga, è presente un bottone di comando che permette di assegnare o togliere l'assegnazione. Selezionando il comando _"Gestione assegnazione"_ potremo intervenire collegando o scollegando le dichiarazioni al documento di riga.

_Funzione "Gestione assegnazione"_

Una volta entrati in questa funzione, nel frontespizio leggeremo le seguenti voci : 

* **Imponibile con IVA**, è la quota d'importo fattura alla quale viene applicata l'IVA normalmente, è un campo popolato nel caso in cui esistano importi superiori al plafond residuo;
* **Senza IVA in dich**, è la quota d'importo fattura che rientra nell'esenzione mediante dichiarazione d'intento;
* **Senza IVA non in dich**, è la quota d'importo fattura che erroneamente non è stata associata ad una dichiarazione d'intento pur presentando l'assoggettamento pertinente;
* **Altri importi esenti**, sono altre quote d'importo della fattura che sono esenti per assoggettamenti diversi da quello dedicato alle dichiarazioni d'intento (ad es. il bollo);
* **Totale imponibile**, è la quota che effettivamente sarà soggetta ad IVA.

Sotto la sezione soprariportata viene descritta la dichiarazione con i propri dettagli : 

* **Inizio validità**, è la data più recente tra la data di emissione e la data d'inizio dell'anno oggetto di dichiarazione;
* **Fine validità**, è la data che determina il termine di utilizzo della dichiarazione, sia per scadenza naturale che per sospensione voluta dal dichiarante;
* **Il numero di protocollo**;
* **La tipologia di dichiarazione** (se è fino a raggiungimento di un importo o per singola operazione);
* **L'importo di plafond totale**;
* **La quota di plafond utilizzata**;
* **La quota di plafond residua**.

Sotto queste voci saranno presenti i riferimenti dei documenti che compongono la fattura o la nota di credito e nelle righe sottostanti ci saranno le dichiarazioni d'intento attive per il cliente.
Selezionando con **S** le dichiarazioni il sistema popolerà il campo "Senza IVA in dich" con la sommatoria degli importi di quelle righe che hanno un importo inferiore al plafond residuo, inoltre in queste scriverà l'assoggettamento dedicato all'esenzione da dichiarazione. Se esistono quote imponibili, ma che presentano un errore di assegnazione o con assoggettamento d'esenzione indicato prima dell'assegnazione, viene popolato ed evidenziato in blu il campo "Errore Senza IVA in dich" e, nella colonna note della scheda di controllo, verrà scritto il motivo per il quale non è stato incluso nella quota "Senza IVA in dich".


Aggiungiamo poi che selezionando la categoria "documenti non associati" dal campo presente nella parte superiore della scheda è possibile visualizzare anche quei documenti che ancora non sono stati collegati ad alcuna dichiarazione d'intento.

La modalità appena descritta è l'unico modo per associare o dissociare le dichiarazioni d'intento d'esenzione per singola operazione.
Lo stesso trattamento viene applicato alle note di credito.

## _3. Modalità Prestampa_
Impostando questa modalità nella tabella V62 a seconda delle azioni che intendiamo compiere otterremo : 

* in fase di Prestampa il sistema genererà il file di controllo che si aprirà con uno spool dove sarà scritta la "*D" accanto a quei documenti che possono essere collegati ad una dichiarazione;
* in fase di Stampa e Ristampa il file di controllo scriverà la "*D" accanto ai documenti effettivamente agganciati.

Sarà poi l'utente che dovrà modificare l'assoggettamento entrando nelle righe interessate all'esenzione e indicando nelle note di fattura i riferimenti della dichiarazione d'intento.

## Forzature
Qualora sorga la necessità di forzare dei particolari importi e non l'intero documento o comunque secondo il criterio automatico, è possibile operare in questi due differenti modi : 
* Se si vuole che venga attribuita solo una specifica parte del documento, in questo caso va applicato l'assoggettamento corrispondente all'articolo 8C, manualmente sulle testate o sulle righe per le quali si vuole che venga applicata l'esenzione. Così facendo solo per gli imponibili risultanti con tale assoggettamento verrà eseguita l'assegnazione, mentre gli imponibili con imposta non verranno più presi in considerazione.
 * Se invece si vuole che un documento sia completamente escluso dall'esenzione, pur risultandone idoneo, nel caso della modalità automatica sarà necessario che prima venga stampato una prima volta, con applicazione dell'esenzione e successivamente tramite procedura riportata a seguire, annullare tale applicazione. Un'alternativa consiste nel sospendere temporaneamente la dichiarazione di intento per data, prima della stampa del documento, ripristinandola poi dopo l'effettuazione della stampa.
* Se si vuole che NON venga attribuita una determinata riga del documento, è possibile agire sul FLAG46 di riga . Impostando tale flag (dal gruppo flag presente sul tipo riga o manualmente), la riga  non verrà presa in considerazione per l'assegnazione.


## Annullamento
L'annullamento è quell'azione che elimina il legame esistente tra una fattura o una nota di credito e la dichiarazione d'intento ripristinando gli assoggettamenti originali del documento.
Per effettuare ciò è possibile attraverso questi strumenti : 

* Scheda di controllo :  per annullare l'assegnazione è sufficiente cliccare sul bottone di gestione posto sulla sinistra di ogni riga e selezionare _"annulla assegnazione"_. In questo modo potremo effettuare l'annullamento un documento alla volta;
* In funzioni aggiuntive, cliccando sulla voce "Controllo Dichiarazioni di Intento" che viene lanciato cliccando F14 dalla testata del documento in questione;
* Mediante l'utilizzo dell'actions "Ricalcolo Utilizzo Documenti".

E' inoltre bene sapere che gli assoggettamenti presenti sui documenti prima dell'applicazione dell'esenzione vengono salvati (archivio BRDINO0F) e che tali dati sono interrogabili, dopo l'applicazione della dichiarazione attraverso l'opzione di riga "Controllo assoggettamenti pre-dichiarazione".

## Note su gestione pre-post fatturazione
Si precisa inoltre questo :  prima che la fattura venga stampata, l'associazione manuale viene fatta per singola bolla, ma dopo aver stampato la fattura, l'associazione si sposta sull'intera fattura. Per questo eventuali eventi successivi, come l'annullamento della stampa o l'annullamento anche parziale delle dichiarazioni possono comportare delle modifiche rispetto alla situazione pre-stampa. Questo in funzione del fatto che dopo la stampa il riferimento è stato spostato sulla fattura, perdendo quindi i riferimenti originali sulle singole bolle.

## Gestione e Controllo delle Note d'Accredito
Le note di accredito possono essere analizzate principalmente attraverso la scheda di controllo. Tuttavia è inoltre possibile attivare dei flussi oggetto (di post-inserimento e/o modifica) basati sul programma funizzato V5DI01X, che permettano di richiamare la gestione delle dichiarazioni direttamente alla conferma dell'inserimento o della modifica di una nota di accredito. Questo al fine di ricordare all'utente, l'eventuale esenzione da applicare. Questo risulta opportuno solo qualora gli utenti che si trovino ad inserire le note abbiamo competenza su tale argomento. Altrimenti si consiglia di usare solo la scheda di controllo da utilizzare prima di ogni fatturazione.

## Visualizzazione attraverso la scheda "Dichiarazioni d'intento"
Un'altra scheda che permette la visualizzazione di tutte le dichiarazioni d'intento emesse e ricevute è la scheda _"Dichiarazione d'intento"** raggiungibile dal modulo **BR Dati di base nell'applicazione "Dichiarazione d'intento". Una volta visualizzata la matrice contenente l'elenco delle dichiarazioni da noi emesse o ricevute, cliccando sul bottone di gestione posto all'inizio di ogni riga e selezionando il comando "Modifica" il sistema lancerà una finestra che permetterà di informarci sia sui termini in cui abbiamo ricevuto o spedito la dichiarazione che sull'utilizzo della stessa.


