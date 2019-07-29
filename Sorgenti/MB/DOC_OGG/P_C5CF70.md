## Obiettivo
Attraverso questa voce di menù è possibile visualizzare l'elenco delle non conformità presenti nel sistema. A seconda che il parametro venga passato o meno con un parametro nel richiamo del programma nella lista vengono presentati tutte le non conformità presenti o solo quelle che hanno come destinatario l'utente che interroga.

## Formato lista

### Testate
Selezionando la voce di menù viene visualizzato il formato lista all'interno del quale è possibile visualizzare le testate delle non conformità presenti caratterizzate da : 
* Numero della registrazione contabile che origina la conformità,
* Soggetto intestatario
* Numero/data del documento (fattura fornitore)
* Numero/data di protocollazione

_1_NOTA BENE :  in entrata vengono visualizzate le non conformità aperte. Per passare a quelle chiuse va premuto il tasto funzione F19.

![C5C040_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5CF70/C5C040_001.png)
### Lista
Tramite le impostazioni è poi possibile visualizzare il dettaglio delle singole non conformità pendenti sulla registrazione, con un schema di presentazione composto da
* Tipo fonte
* Codice/Data Raggruppamento
* Oggetto Derivato
* Destinatario della non conformità
* Tipo non Conformità
* P = Indica se la registrazione origine è provvisoria
* B = Indica il blocco pagamento della rate della registrazione
* N = Indica se sono presenti delle note sulla singola non conformità

Sempre tramite le impostazioni è comunque possibile tramite gli schemi decidere quali dati presentare nel dettaglio.

### Opzioni


- Per le testate delle non conformità sono disponibili le seguenti opzioni : 
-- X - Dettaglio :  permette di aprire il dettaglio della non conformità
-- F - Lettera fornitore :  permette di inviare una lettera di segnalazione al fornitore
-- I1 - Invio e-mail (Tutte) :  permette di inviare le mail di tutte le non conformità ai rispettivi destinatari
-- I2 - Invio e- mail (Solo aperte) :  permette di inviare le mail di tutte le non conformità aperte ai rispettivi destinatari
-- R- Registrazione :  permette di visualizzare la registrazione di prima nota che ha generato la non conformità
-- M - Registrazione :  permette di modificare la registrazione di prima nota che ha generato la non conformità
- Per le singole non conformità sono invece presenti le seguenti opzioni : 
-- C - Conferma azione correttiva :  consente di visualizzare e confermare le azioni correttive disponibili
-- V - Visualizza azione correttiva :  consente di visualizzare in dettaglio la non conformità
-- S - Stampa azione correttiva :  consente di stampare il dettaglio la non conformità
-- L - Lettera Fornitore :  consente di generare una lettera da inviare al fornitore
-- N - Gestione note :  consente di entrare in gestione delle note associate alla non conformità
-- 05 - Non conformità :  consente di visualizzare in dettaglio la non conformità
-- R- Registrazione :   permette di visualizzare la registrazione di prima nota che ha generato la non conformità
-- M- Registrazione :   permette di modificare la registrazione di prima nota che ha generato la non conformità
-- A - Riapri non conformità :  questa opzione permette di riaprire una non conforità chiusa


### Tasti funzionali
 * F13 - Parzializzazioni :  consente di accedere alla videata delle parzializzazioni
 * F17 - Impostazioni :   consente di accedere alla videata delle impostazioni
 * F19 - NC Chiuse :  consente di visualizzare tutte le non conformità chiuse

### Impostazioni
Attraverso le impostazioni della gestione non conformità è possibile definire i seguenti parametri : 

- Dettaglio in lista :  permette di visualizzare il dettaglio delle non conformità all'intenro del formato lista
- Destinazione :  permette di visualizzare le sole non conformità dirette a uno specifico destinatario
- Non confomrità :  permette di visualizzare solo le non conformità di un determinato tipo, ad esempio solo le differenze prezzo o le differenze quantità.
- Schema dettaglio :  permette di definire uno schema di visualizzazione da associare al dettaglio delle non conformità.


## Formato dettaglio
Attraverso il comando 5 è possibile visualizzare il dettaglio della non conformità : 

![C5C040_003](http://localhost:3000/immagini/MBDOC_OGG-P_C5CF70/C5C040_003.png)
Per fare in modo che una registrazione scompaia dall'elenco delle registrazioni con non conformità è necessario chiudere tutte le non conformità contenute nella registrazione.

## Azioni correttive
Per ciascuna tipologia di non conformità sono definite delle azioni correttive che è possibile visualizzare e confermare tramite il comando C.

### Note comuni alle azioni correttive di tutte le non conformità
* Tutte le azioni correttive ad esclusione di "gira ad altro buyer", "assegna da altra lista", "gira a fornitore" , e quella che lo riportano esplicitamente nella descrizione, comportano, lo sblocco del pagamento. Quest'ultimo è da notare viene effettivamente applicato solo qual'ora, tutte le non conformità pendenti sulla registrazione siano state chiuse.
*  Gira a fornitore :  comporta la creazione automatica di un documento di attesa, non che di una non conformità di "attesa documenti". La contabilizzazione di tale documento comporterà automaticamente, la chiusura di tale non conformità non che lo sblocco del pagamento del documento originale. Nel caso in cui la non conformità fosse una differenza prezzo, come prezzo verrà ripristinato il prezzo originale, per fare in modo che sommando poi valori del documento originale e del documento successivo quadri tutto.
* Aggiorna valori :  permette di andare ad aggiornare il prezzo di una serie di dati :  bolla/ordine/listino. Alla conferma di quest'azione viene richiesto quali elementi si voglia aggiornare. Per la bolla è da notare che non viene aggiornato il prezzo effettivo che era già stato aggiornato.

### Mancanti
Nel caso in cui alla registrazione di una fattura si rileva la mancanza delle bolle associate viene generata una non conformità di tipo "Mancanti". Le azioni correttive associate a questa tipologia di non conformità sono : 
 * Assegna da altra lista :  permette di assegnare la non conformità ad un altro responsabile.
 * Chiudi senza sblocco pagamento :  chiude la non conformità ma non sblocca il pagamento della fattura.
 * Chiudi con sblocco pagamento :  chiude la non conformità e sblocca il pagamento.
 * Nuova registrazione giroconto :  crea una registrazione che storna il conto mancati
 * Attesa nota credito :  genera un documento di attesa nota credito, chiude la non conformità "Mancanti" e apre una non conformità di tipo "Attesa documenti".
.
### Differenza prezzo
Nel caso in cui alla registrazione di una fattura si rileva una differenza prezzo tra bolla e fattura viene generata una non conformità di tipo "Differenza prezzo". Le azioni correttive associate a questa tipologia di non conformità sono : 
 * Gira ad altro buyer :  permette di assegnare la non conformità ad un altro responsabile.
 * Chiudi NC e blocca pagamento :  chiude la non conformità ma non sblocca il pagamento della fattura.
 * Chiudi NC e sblocca pagamento :  chiude la non conformità e sblocca il pagamento.
 * Aggiorna valori origine (Bol/Ord/Lis) :  aggiorna gli importi presenti sulla fonte origine.
 * Gira a fornitore (nota) :  permette di generare un documento di attesa che può essere una nota credito nel caso in cui l'importo fatturato sia superiore a quello atteso e riportato dalla bolla oppure una nota debito nel caso in cui l'importo fatturato sia inferiore a quello atteso. In questo caso viene chiusa la non conformità "Differenza prezzo" e viene aperta una non conformità di tipo "Attesa documenti".

### Differenza quantità
Nel caso in cui alla registrazione di una fattura si rilevi una differenza di quantità tra bolla e fattura viene generata una non conformità di tipo "Differenza quantità". Le azioni correttive associate a questa tipologia di non conformità sono : 
 * Gira ad altro buyer :  permette di assegnare la non conformità ad un altro responsabile.
 * Chiudi NC e blocca pagamento :  chiude la non conformità ma non sblocca il pagamento della fattura.
 * Chiudi NC e sblocca pagamento :  chiude la non conformità e sblocca il pagamento.
 * Aggiorna valori origine (Bol/Ord/Lis) :  aggiorna le quantità presenti sulla fonte origine. Quindi nel caso in cui l'origine sia una bolla aggiorna la bolla, se invece si tratta di un ordine aggiorna l'ordine.
 * Gira a fornitore (nota) :  permette di generare un documento di attesa che può essere una nota credito nel caso in cui la quantità fatturata sia superiore a quella ricevuta e attestata dalla bolla oppure una nota debito nel caso in cui la quantità fatturata sia inferiore a quella ricevuta. In questo caso viene chiusa la non conformità "Differenza quantità" e viene aperta una non conformità di tipo "Attesa documenti".

### Attesa documenti
Questo tipo di non conformità si riscontra nel momento in cui si è in attesa di un documento da parte del fornitore che generalmente è una nota credito o una nota debito generata dalla chiusura di un'altra non conformità. Le azioni correttive associate a questa tipologia di non conformità sono : 
 * Chiudi e assegna da altra lista :  permette di assegnare la non conformità ad un altro responsabile.
 * Chiudi senza sblocco pagamento :  chiude la non conformità ma non sblocca il pagamento della fattura.
 * Chiudi con sblocco pagamento :  chiude la non conformità e sblocca il pagamento.
 * Chiudi con ricezione documento in attesa  :  permette di chiudere la non conformità, registrare il documento in attesa e sbloccare il pagamento. Selezionando questa opzione verrà visualizzato il data entry della contabilità che consente la registrazione del documento in prima nota.
 * Chiudi con annullamento documento in attesa :  permette di chiudere la non conformità annullando l'attesa documento. Anche in questo caso si ha lo sblocco del pagamento.

### Differenza modalità pagamento
Nel caso in cui ci sia una differenza tra modalità pagamento riportata su un ordine o su una bolla e modalità pagamento riportata in fattura viene generata una non conformità di tipo "Differenza modalità pagamento". Le azioni correttive associate a questo tipo di non conformità sono : 
 * Chiudi e assegna ad altra lista :  permette di assegnare la non conformità ad un altro responsabile.
 * Chiudi senza sblocco pagamento :  chiude la non conformità ma non sblocca il pagamento della fattura.
 * Chiudi con sblocco pagamento :  chiude la non conformità e sblocca il pagamento.
 * Modifica registrazione  :  modifica la tipologia di pagamento sulla registrazione contabile e sblocca il pagamento.
 * Aggiorna fonte origine :  modifica la tipologia di pagamento sul documento origine e sblocca il pagamento.
