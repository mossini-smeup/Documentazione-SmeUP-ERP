
# Gestione Fidelity Card

## Gestione Fidelity Card

## Introduzione

La gestione delle Carte Fedeltà (o Fidelity Card) consente di migliorare il rapporto con i propri clienti dando svariati benefici, quali, ad esempio :  miglioramento della fedeltà del cliente all'esercizio commerciale, aumento dell'importo dello scontrino medio, possibilità di veicolare promozioni ad hoc, profilare la propria clientela per identificarla con precisione.
Negoziando consente di attivare questa funzionalità mettendo a disposizione dell'utente numerosi servizi : 

 * Profilazione del cliente
 ** E' possibile decidere, in massima libertà, la tipologia di dati da raccogliere
 ** E' possibile definire se imputare questi dati durante il processo di emissione tessera (consigliato agli esercizi con bassa affluenza alla cassa o dotati di postazione fedeltà dedicata) o in un momento successivo
 ** E' possibile stampare il modulo contenente i dati del cliente per raccoglierne la firma
 * Produzione della tessera
 ** E' possibile produrre direttamente da Negoziando la tessera fedeltà o utilizzare tessere precedentemente stampate
 * Attribuzione di obiettivi al cliente
 ** E' possibile definire soglie di obiettivi (raccolta punti) al raggiungimento delle quali riconoscere sconti che possono essere variabili
 * Promozioni
 ** E' possibile attivare promozioni (prezzi e sconti) riservate alla clientela fidelizzata e fruibili immediatamente o solo al raggiungimento di target
 * Analisi dei dati
 ** E' possibile analizzare i dati di vendita relativi a tessere fedeltà
 * Comunicazione
 ** E' possibile estrarre indirizzi e-mail e numeri telefonici per poter inviare (tramite servizi esterni) comunicazioni promozionali

Le funzionalità di fidelizzazione possono essere abilitate sia localmente al negozio, che globalmente in tempo reale, attraverso l'utilizzo di Negoziando Infocenter Live.
- [Negoziando Infocenter Live](Sorgenti/MB/DOC_OPE/NGBASE_20)

## Struttura Codici Fidelity

Il **Codice Tessera Fidelity** viene identificato come un Codice a Barre di tipo EAN13 (XXKKKyyyyyyyC) così strutturato : 

 * XX Prefisso Tessere (2 caratteri)
 * KKK Codice Gruppo Fidelity (3 caratteri)
 * yyyyyyy Codice Fidelity (7 caratteri)
 * C Check Digit (carattere che viene attribuito tramite un calcolo basato sui valori numerici che lo precedono)

Ciò da la possibilità di gestire sino a 999 differenti gruppi di Fidelity Card e di poter descrivere su ognuno di essi comportamenti specifici (per ciascun gruppo è possibile gestire 9.999.999 tessere).
**Codice Cliente Fidelity è formato da 10 caratteri e comprende Codice Gruppo + Codice Fidelity.**

## Tabelle da Configurare

**Tabella CAMF** - Causali Movimenti Fidelity.
 La definizione di questa tabella serve per poter identificare correttamente i Movimenti Fidelity dei Clienti. E' obbligatorio definire tali Casuali e impostarle nella Configurazione di Negoziando se si intendono utilizzare le funzioni di Utilità del Menu Fidelity.
Definire Codice e Descrizione.
Nel caso di Inserimento Manuale di Movimenti è possibile specificare, tramite la richiesta Controllo Esistenza Scontrino, se i riferimenti dello Scontrino indicati sono corretti

**Tabella CNVF** - Convenzioni Fidelity.
Definire questa tabella se si intende gestire in Anagrafica Cliente l'attribuzione di un Codice Convenzione (utilizzabile anche nelle funzioni di Utilità).
Definire il  Codice, la Descrizione ed eventuali annotazioni. Per indicare una Validità delle Tessere definire o il Numero dei Giorni o la Data di Fine Validità. La Data di Validità è un valore facoltativo, ma, se impostata, determinerà la scadenza della Tessera.
A questo punto definire se la Convenzione è riservata ai Negozi di un determinato Elenco (Elenchi/Composizioni).

**Tabella MOTS** - Motivazioni Sconti di Cassa.
Definire tutti i tipi di Sconto gestiti in questa Tabella

**Tabella CABU** - Causali per Emissioni Buoni di Cassa

**Tabella OPCA** - Operazioni Registratore di Cassa
E' possibile utilizzare la definizione di Codici Operazione di Cassa per la concessione, tramite l'utilizzo dei Punti raccolti dal Cliente, di Sconti di Subtotale a valore (in alternativa alla definizione dei Parametri relativi all'Utilizzo dei Punti). I programmi di Cassa, dopo la lettura del Codice Operazione di Cassa, prima dell'inserimento della Riga di Sconto Subtotale controlleranno se il cliente ha raccolto i Punti Necessari all'utilizzo dello Sconto dando segnalazione di eventuale anomalia in caso di punti non sufficienti.

## Definizione Informazioni Personalizzate

**Tabella INFP - Informazioni Personalizzate**

Viene utilizzata nella Gestione Anagrafica per la raccolta di Informazioni non comprese tra le Standard di Negoziando. Bisogna selezionare l'Archivio Anagrafico di interesse e la Sequenza Richiesta (l'ordine col quale il programma visualizzerà il dato)

Definire : 

 * Descrizione
 * Sigla Parametro
 * Tipo Parametro. Può essere : 
 ** Carattere
 ** Numerico
 ** Data
 * Dimensione (se Tipo Parametro Data, obbligatoriamente 8)
 * Numero Decimali. (Facoltativo e solo se Tipo Parametro Numerico)
 * Obbligatorio/Facoltativo
 * Tipo Controllo. Può essere : 
 ** Nessuno
 ** Lista
 ** Tabella
 * Lista per Controlli. Se definito un Controllo di Tipo Lista, indicare i valori da accettare separati da | (Pipe)
 * Tabella per Controlli. Se definito un Controllo di Tipo Tabella, andrà definita la Tabella dei valori accettati in TABP - Tabelle Personalizzate
 * Numero Selezioni Tabella. Nel caso di Controllo di Tipo Tabella indicare quante selezioni è possibile effettuare.
Ad esempio, se volessimo raccogliere un elenco degli Sport praticati dal Cliente, potremmo definire una richiesta con un Controllo di Tipo Tabella, definire l'elenco degli Sport nella Tabella TABP e decidere di chiedere al Cliente 3 sport
 * Codice Controllo di Negoziando. Permette di effettuare un controllo su un dato che si sta inserendo, associandolo ad un dato che deve essere effettivamente presente
 * Sequenza Presentazione a Video. E' possibile indicare qui la sequenza in base alla quale il dato sarà visualizzato all'interno della maschera di Negoziando
 * Descrizione in Lingua SI/NO
 * Visualizza nei Filtri SI/NO. Se creo un campo nuovo, è possibile visualizzarlo all'interno di maschere di Parametri di Selezione ed utilizzarlo come Filtro ulteriore

**Tabella TABP - Tabelle Personalizzate**

Viene utilizzata nella Gestione Anagrafica per la raccolta di Informazioni non comprese nelle informazioni Standard di Negoziando, se definito un Controllo di Tipo Tabella.
Indicare Tipo Tabella, Codice e una Descrizione

## Definizione Obbligatorietà Campi

**Tabella OBBL - Definizione Richiesta/Obbligatorietà Campi**

Con la gestione di questa Tabella è possibile specificare la Richiesta e l'Obbligatorietà dei campi Standard di Negoziando
Selezionare :  _Tipo ARC - Tabella ANFDT - Aggiornamento Anagrafica Fidelity Card_
Viene presentato l'elenco dei Campi che vengono richiesti nella Gestione delle Informazioni Standard di Negoziando.
Utilizzare i tasti F8 e F9 per impostare se Richiedere il Campo e se renderlo Obbligatorio. Premere F6 per Confermare le selezioni


## Funzioni specifiche di Gestione Fidelity Card

_Dal Menu>Principale>Fidelity Card _si accede a tutta la gestione Fidelity e alle varie funzionalità dedicate : 

 * Anagrafica

 ** Aggiornamento Anagrafica Fidelity Card
 ** Analisi su Anagrafiche Fidelity
 ** Stampa Anagrafica Fidelity Card
 ** Stampa Tessere Fidelity

* Movimenti

 ** Movimenti Fidelity Card
 ** Stampa Movimenti Fidelity Card
 ** Visualizza Punti Fidelity
 ** Visualizza Movimenti di Magazzino per Codice Tessera

* Utilità

 ** Rinnovo Data Scadenza Tessere
 ** Sostituzione Tessera
 ** Annullamento Sostituzione Tessere
 ** Azzeramento Punteggio Tessere Non Movimentate
 ** Azzeramento Punteggio Tessere Per Gruppo
 ** Azzeramento Punti per Tessere Scadute
 ** Creazione Saldi Punteggio alla Data
 ** Invio Comunicazioni a Clienti
 ** Attivazione/Generazione Buoni di Cassa
 ** Assegnazione Scontrino a Anagrafica Fidelity

 * Configurazione : 

 ** Gestione Gruppi Fidelity
 ** Gestione Parametri Fidelity - Globali
 ** Gestione Parametri Fidelity - Articoli

## Menu Anagrafica

Con le funzioni presenti in questo menù è possibile gestire le Anagrafiche dei Clienti Fidelity.
N.B.In Negoziando le Fidelity Card possono essere utilizzate anche senza effettuare la raccolta delle informazioni Anagrafiche dei Clienti.

_Dal Menu>Fidelity Card>Anagrafica>Aggiornamento Anagrafica Fidelity Card_

Questa funzione permette di aggiornare i Dati Anagrafici dei Clienti Fidelizzati
Viene inizialmente proposto l'elenco dei Clienti
Sono poi a disposizione i normali tasti funzionali di gestione di Negoziando : 

 * Invio per la Modifica
 * F4 per la Cancellazione
 * F5 per la Visualizzazione
 * F6 per l'Inserimento
 * F9 per la Duplicazione di un record

e i seguenti tasti funzionali aggiuntivi : 

 * F7 per la Gestione degli Oggetti Multimediali (la foto del cliente, ad esempio)
 * F8 per Ordinare l'Elenco. L'Ordinamento a video potrà essere effettuato o per codice Tessera o per Cognome/Nome
 * F10 per la Stampa del Modulo. Per eventuali personalizzazioni utilizzare la funzione di Gestione delle Stampe Personalizzate (Nome Formato :  MODULOFIDELITY)
 * F11 per la Stampa della Tessera. E' possibile ottenere la stampa di Tessere in formati diversi in base al Gruppo di appartenenza della tessera. Specificare il Nome Formato in _Configurazione Tessere>Gestione Gruppi Fidelity_ (il nome del formato Standard è TESSEREFIDELITY).
 * F12 per la Generazione di Virtual Card. Attualmente Negoziando supporta tessere virtuali di tipologia Passbook, fruibili da tutti i dispositivi mobili Apple

Nella Gestione dell'Anagrafica vengono richiesti inizialmente i Dati Anagrafici del Cliente, poi vanno compilate le seguenti richieste : 

 * Codice Negozio. Sarà il negozio titolare dell'anagrafica.
 * Tessera Bloccata. Impostare SI se si intende impedire l'utilizzo della Tessera nei programmi di Cassa
 * Tessera di Riferimento. Impostare questo Codice se si desidera che le letture fatte per la Tessera vengano considerate come letture fatte sulla Tessera di Riferimento.E' il caso di un cliente in possesso di 2 o più tessere per le quali si desidera che i movimenti affluiscano tutti su un'unica tessera (quella di riferimento).
Viene impostato dalla funzione di Sostituzione Tessere (sulla Tessera Sostituta - ed è il Codice della Nuova Tessera). Se la Tessera Sostituita non è stata Bloccata in Cassa, alla Lettura del Codice della Tessera Sostituita viene forzata la Lettura della nuova Tessera.
Es :   sostituisco la tessera 100 con la 123, in cassa leggo la tessera 100,ma sarà come aver letto la tessera 123 per tutti i controlli e le scritture del DB.
 * Codice Convenzione. Si tratta di un codice della Tabella CNVF (vedi paragrafo Definizione Convenzioni).__ Impostando il Codice Convenzione viene impostata automaticamente la Data di Fine Validità della Tessera (se definita nella convenzione), a meno che non sia già specificata.
 * Codice Tessera Alternativo. Nel caso in cui il codice stampato sulla tessera in possesso del Cliente sia differente dal codice tessera standard è possibile indicare in questo campo tale numero di Tessera. Potrebbe essere il caso di una tessera emessa con un vecchio sistema, quindi non con Negoziando.
 * Accetta Invio Comunicazioni SI/NO
 * Data Rilascio Consenso
 * Tessera Sospesa. In Cassa non sarà possibile utilizzare letture che prevedono l'utilizzo di punti (es :  Lettura di un Articolo con Punti Negativi o Lettura di un OPCA di Sconto che prevede l'utilizzo di Punti). Chi usa questo Flag in realtà ha procedure esterne che lo fanno.
 * Codice Commento. E' possibile creare un Commento da_ Menu>Anagrafiche di Base>Gestione Commenti da stampare sullo Scontrino ad ogni acquisto con Fidelity

N.B. E' possibile definire quali saranno i campi da Richiedere e quali gli Obbligatori (vedi paragrafo Definizione Obbligatorietà)
Dopo la conferma sulle Informazioni Standard vengono richieste, se esistenti, le Personalizzate (vedi Definizione Informazioni Personalizzate)

## Analisi su Anagrafiche Fidelity

Questa funzione permette di effettuare diverse analisi sulle informazioni relative a Punti e Acquisti di un Elenco di Clienti con le relative informazioni anagrafiche.
Il Pannello Superiore è quello relativo ai Parametri di Selezioni Anagrafiche e permette di impostare un filtro in base alle selezioni indicate

In quello Centrale si trovano i Parametri di Selezione Movimenti dove è possibile indicare il Periodo da Interrogare specificando cosa si vuole analizzare : 

 * Solo Punti
 * Solo Acquisti
 * Entrambi

Nel Pannello Inferiore, quello dedicato ad Altri Parametri, è possibile indicare

 * Evidenzia Totale Punti/Acquisti del Cliente
 ** No
 ** Entrambi
 ** Solo Acquisti
 ** Solo Punti
 * Escludi Clienti senza Movimenti nel Periodo SI/NO
 * Considera Solo Punti con Causale. Selezionare la Causale dalla Tabella CAMF - Causali Movimenti Fidelity
 * Considera Solo Punti con Tipo Tessera

Dopo aver confermato apparirà l'analisi e sarà possibile Stamparla (F5) oppure Esportarla su Excel (F6). In base alle Selezioni Indicate saranno visibili dei Bottoni che permettono di Visualizzare in Dettaglio Punti e Acquisti.

## Stampa Anagrafica Fidelity Card

_Dal Menu>Fidelity Card>Stampa Anagrafica Fidelity Card_

Questa funzione permette la Stampa di un Elenco di Clienti con le relative informazioni anagrafiche.
Si tratta di una stampa Standard di Negoziando, vengono pertanto richieste le normali impostazioni iniziali delle Stampe ed è poi possibile filtrare l'elenco dei Clienti da stampare
(VEDI STAMPE PARAMETRICHE)

## Stampa Tessere Fidelity

_Dal Menu>Fidelity Card>Stampa Tessere Fidelity_

Questa funzione permette la Stampa di un Elenco di Tessere.
Viene inizialmente richiesto di indicare il Gruppo Tessere e il Range (Da Tessera a Tessera). Indicare i valori richiesti e premere Invio.

N.B. Per la Stampa NON è necessario che il Codice Tessera indicato sia presente nell'archivio Anagrafico. In base alle impostazioni dei Gruppi Fidelity sarà possibile stampare Tessere di Formati diversi.
Prima di effettuare la Stampa il programma verifica se le Tessere risultano già stampate in precedenza e chiede conferma se stampare comunque tutte le tessere o solo quelle mai stampate.

## Menu Movimenti

Per Gestione Movimenti Fidelity viene intesa la gestione dei Punti delle Tessere
Normalmente i Movimenti Fidelity vengono generati dal programma di gestione della Cassa a chiusura degli Scontrini dove è stata letta una tessera Fidelity (un movimento per i Punti da Attribuire e un eventuale movimento per i punti da scalare per ogni Scontrino)
I Movimenti Fidelity sono identificati per tipologia in base a un Codice Causale (vedi annotazioni specifiche Definizione Causali Movimenti Fidelity e Configurazione di Negoziando).

## Movimenti Fidelity Card

Questa funzione permette di gestire i Movimenti delle Tessere e di Aggiungerne/Cancellarne altri (se le condizioni lo permettono).  _Dal Menu>Principale>Fidelity Card>Movimenti>Movimenti Fidelity Card
All'attivazione della funzione è possibile specificare Codice Tessera, Codice Negozio e il range di Date per la determinazione di un periodo. Premendo Invio apparirà l'elenco dei Movimenti esistenti, in base alle Selezioni effettuate. Sono a disposizione i seguenti tasti funzionali di gestione di Negoziando : 

 * Invio per la Modifica
 * F4 per la Cancellazione
 * F6 per Inserimento

Premendo uno dei tasti funzione si entra nella gestione del Singolo Movimento. In caso di Inserimento o Modifica di un Movimento occorrerà indicare : 

 * Data Movimento. Viene proposta quella attuale, ma è possibile cambiarla
 * Causale Movimento. Selezionarla dalla Tabella CAMF - Causale Movimenti Fidelity
 * Codice Cassa
 * Numero Scontrino

 Confermare e a questo punto verrà richiesto il numero di Punti da Attribuire/Modificare più eventuali Annotazioni facoltative.

## Stampa Movimenti Fidelity Card

 _Dal Menu>Principale>Fidelity Card>Movimenti>Stampa Movimenti Fidelity Card_

Questa funzione permette la Stampa di un Elenco dei Movimenti Fidelity.Si tratta di una stampa Standard di Negoziando, vengono pertanto richieste le normali impostazioni iniziali delle Stampe ed è poi possibile filtrare l'elenco dei Movimenti da stampare

## Visualizza Punti Fidelity

 _Dal Menu>Principale>Fidelity Card>Movimenti>Visualizza Punti Fidelity_

Questa funzione permette la visualizzazione in dettaglio dei Punti di una Singola Tessera. Viene richiesto inizialmente di indicare la Tessera per la quale visualizzare i Movimenti.
E' possibile indicare solo il Codice Cliente Fidelity oppure il Codice Tessera completo di prefisso e Check Digit
Vengono poi visualizzati in dettaglio i Movimenti della Tessera.
Se il Movimento è originato dal programma di Cassa durante l'emissione Scontrini, col tasto F5 è possibile visualizzare lo Scontrino che ha attribuito i Punti.

## Visualizza Movimenti di Magazzino per Codice Tessera

 _Dal Menu>Principale>Fidelity Card>Movimenti>Visualizza Movimenti di Magazzino per Codice Tessera

Questa funzione permette di visualizzare i Movimenti di Magazzino generati utilizzando una Tessera Fidelity.
In alto a sinistra nella maschera specificare il Codice Tessera ed un eventuale Periodo di analisi. Una volta confermato, apparirà l'elenco dei Movimenti. Anche in questa funzione (sempre con il tasto F5) è possibile visualizzare lo Scontrino dal quale derivano.
Dalla maschera di visualizzazione è possibile modificare i parametri di selezione indicati precedentemente.

## Menu Utilità

Questo menu contiene funzioni generiche di utilità
Per la gestione di queste funzioni è necessario definire nella Configurazione di Negoziando i Codici Causali che dovranno essere utilizzati per la scrittura dei Movimenti (vedi annotazioni successive)

## Rinnovo Data Scadenza Tessere

 _Dal Menu>Principale>Fidelity Card>Utilità>Rinnovo Data Scadenza Tessere_

La funzione permette di rinnovare la Data di Scadenza delle Tessere.
Nel Pannello di Selezione Tessere è possibile scegliere quelle per le quali effettuare il rinnovo della Data tramite filtri (opzionali) su Codice Gruppo, Codice Convenzione, Codice Negozio, Range di Tessere
Viene inoltre richiesto se si vogliono rinnovare solo le Tessere Scadute o meno.
Definire nel secondo Pannello la nuova Data di Scadenza indicando una Data specifica oppure il Numero dei Giorni da considerare a partire dalla Data Odierna
Confermate queste selezioni verrà proposto l'elenco dei Clienti per i quali verrà modificata la Data di Scadenza delle Tessere
Con i tasti funzionali F7 e F8 sarà possibile Escludere/Includere dall'aggiornamento la singola Tessera o gruppi di Tessere (utilizzare i normali filtri della griglia per creare il gruppo da elaborare).
Premendo F6 verrà richiesta conferma dell'elaborazione e successivamente verrà data segnalazione di avvenuta elaborazione.


## Sostituzione Tessera

La funzione permette la sostituzione di una tessera con un'altra.  _Dal Menu>Principale>Fidelity Card>Utilità>Sostituzione Tessera
Indicare il Codice della Tessera da Sostituire e quello della Nuova e premere Invio
Verranno visualizzate le informazioni anagrafiche delle due tessere. Premere F6 per confermare la Sostituzione
Con questa funzione verrà impostato sulla vecchia tessera (Tessera da Sostituire) il codice Tessera di Riferimento e verranno generati automaticamente un movimento per lo Storno del totale dei
Punti dalla vecchia Tessera e un movimento per l'attribuzione del Totale dei Punti alla nuova.

## Annullamento Sostituzione Tessere

La funzione permette di annullare una errata Sostituzione.  _Dal Menu>Principale>Fidelity Card>Utilità>Annullamento Sostituzione Tessera
Indicare il Codice della Tessera per la quale effettuare l'annullamento della Sostituzione.
Verranno visualizzate le informazioni anagrafiche della tessera, premere F6 per confermare l'Annullamento della Sostituzione
__Attenzione, con questa funzione verranno sistemati gli archivi Anagrafici ma non verrà generato nessun Movimento relativamente ai Punti.

## Azzeramento Punteggio Tessere Non Movimentate

La funzione permette l'azzeramento dei Punti di Tessere non Movimentate da un certo periodo di tempo. _Dal Menu>Principale>Fidelity Card>Utilità>Annullamento Sostituzione Tessera_
Viene richiesto inizialmente di indicare il Gruppo di Tessere per le quali effettuare l'elaborazione.
Viene poi presentato l'elenco delle Tessere per le quali sarà effettuato l'azzeramento dei Punti.
N.B.Per determinare quali siano le tessere per le quali effettuare l'azzeramento, vengono utilizzate le informazioni esistenti nell'Anagrafica dei Gruppi __Numero Giorni di non Utilizzo per Azzeramento Punti (vedi Gestione Gruppi Fidelity)

Con i tasti funzionali F7 e F8 sarà possibile Escludere/Includere dall'azzeramento punti una singola tessera o gruppi di Tessere (utilizzare i normali filtri della griglia per creare il gruppo da elaborare).
Premere F6 per confermare l'elaborazione.
N.B. La funzione non cancella i Movimenti ma ne scrive di nuovi con il totale punti negativo.

## Azzeramento Punteggio Tessere Per Gruppo

La funzione permette di azzerare il punteggio di un gruppo di tessere. _Dal Menu>Principale>Fidelity Card>Utilità>Azzeramento Punteggio Tessere per Gruppo
Viene richiesto inizialmente di indicare il Gruppo di Tessere per le quali effettuare l'azzeramento e la Data di riferimento (la data entro la quale azzerare i movimenti, es. tutti i movimenti fino al 31-12-15)
Viene poi presentato l'elenco delle Tessere per le quali sarà effettuato l'azzeramento dei Punti.
Con i tasti funzionali F7 e F8 sarà possibile Escludere/Includere dall'azzeramento la singola Tessera o gruppi di Tessere (utilizzare i normali filtri della griglia per creare il gruppo da elaborare).
Premere F6 per confermare
N.B. La funzione non cancella i Movimenti ma ne scrive di nuovi con il totale punti negativo.

## Azzeramento Punti per Tessere Scadute

Con la funzione è possibile azzerare i punti delle tessere scadute.  _Dal Menu>Principale>Fidelity Card>Utilità>Azzeramento Punti Tessere Scadute
Questa funzione può essere usata nei casi di Tessere associate ad una Convenzione. Finita la Convenzione, la tessera potrebbe essere associata ad un'altra convenzione, ma si vogliono azzerare tutti i punti accumulati con quella precedente, ormai scaduta.
Viene richiesto il Codice Gruppo e la Data Limite Punti da Azzerare
Viene poi presentato l'elenco delle Tessere per le quali sarà effettuato l'azzeramento dei Punti.
Con i tasti funzionali F7 e F8 sarà possibile Escludere/Includere dall'azzeramento la singola Tessera o gruppi di Tessere (utilizzare i normali filtri della griglia per creare il gruppo da elaborare).
Premere F6 per confermare

## Creazione Saldi Punteggio alla Data

Questa funzione permette di creare record di Movimenti riepilogativi alla Data indicata. _Dal Menu>Principale>Fidelity Card>Utilità>Creazione Saldi Punteggio alla Data
Viene richiesto inizialmente di indicare il Gruppo di Tessere per le quali effettuare l'elaborazione e la Data di Riferimento entro la quale verrà creato il Saldo.
Con i tasti funzionali F7 e F8 sarà possibile Escludere/Includere dall'azzeramento la singola tessera o gruppi di Tessere (utilizzare i normali filtri della griglia per creare il gruppo da elaborare).
Premere F6 per conferma dell'elaborazione.
__N.B.La funzione crea il Record di Saldo dei Punti e cancella i Movimenti con data antecedente.__

## Invio Comunicazioni a Clienti

_Dal Menu>Principale>Fidelity Card>Utilità>Invio Comunicazioni a Clienti_

Per informazioni su questa funzionalità consultare il manuale Negoziando SMS Comunicazioni
  :  : DEC T(MB) P(DOC_OPE) K(NGBASE_XX) Negoziando SMS Comunicazioni

## Attivazione/Generazioni Buoni di Cassa

Per poter attivare la Gestione di Emissione/Attivazione dei Buoni è opportuno che nei Parametri Fidelity, nel Pannello Utilizzo Punti sia stata indicata la voce Produzione Buoni alla Richiesta di Modalità Utilizzo Sconti.
In Configurazione, _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Pannello Parametri per Emissione Buoni/Acconti  , è presente la richiesta Modalità di Rilascio Buoni ed è possibile decidere tra : 

 * Genera Nuovi Buoni di Cassa.
Impostare questa configurazione se in Negozio si vuole attivare la Generazione dei Buoni di Cassa. Premere _Menu>Principale>Fidelity Card>Utilità>Attivazione/Generazioni Buoni di Cassa_ e si aprirà la maschera nella quale bippare la Fidelity del Cliente. Apparirà una schermata che riporta in alto i Dati del Cliente, il riepilogo dei Punti Disponibili sulla Fidelity e il Numero Minimo/Massimo dei Punti Utilizzabili, prendendoli dai Valori definiti nei Parametri Fidelity nel Pannello di Utilizzo Punti. Sempre in base a questi Valori verrà proposto il Numero e l'Importo Massimo di Buoni Utilizzabili e il Numero Massimo di Punti.
Premere Invio Imposta Quantità Buoni e indicare la quantità di Buoni da Generare. L'Importo viene compilato in automatico dal Sistema, ma è possibile modificarlo, se rientra nell'Importo Massimo precedentemente definito.
Confermare la Stampa del Buono.

 * Attiva Buoni di Cassa Esistenti.
In questo caso il negozio avrà già a disposizione dei Buoni creati dalla Sede e dovrà semplicemente Attivarli per il Cliente Fidelity. Si tratta di Buoni Sconto a Valore Soggetti ad Attivazione.
(_Dal Menu>Principale>Registratori di Cassa>Buoni/Acconti>Generazione Buoni di Cassa _ sotto le Informazioni per Utilizzo Buoni alla voce Modalità di Attivazione selezionare Soggetto ad Attivazione).
A questo punto, come nell'altro caso, premere _Menu>Principale>Fidelity Card>Utilità>Attivazione/Generazioni Buoni di Cassa e si aprirà la stessa maschera di prima nella quale bippare la Fidelity del Cliente.
Premere F7 e attivare il Buono leggendone il Codice a Barre. E' possibile modificarne l'importo.
Questa stessa operazione può essere effettuata direttamente da un bottone di Cassa

## Associazione Scontrino a Anagrafica Fidelity

Questa funzione permette di assegnare uno Scontrino precedentemente emesso (senza aver effettuato la lettura di una Tessera) ad un'Anagrafica Fidelity. _Dal Menu>Principale>Fidelity Card>Utilità>Associazione Scontrino a Anagrafica Fidelity
Impostare la Configurazione di Negoziando (vedi note successive) se si desidera che questa assegnazione generi i Punti (calcolati sull'importo dello Scontrino) per l'Anagrafica selezionata.
Se in Configurazione è specificata l'assegnazione dei punti il programma richiede inizialmente di indicare un Operatore autorizzato alla funzione di Assegnazione Scontrino (vedi _Principale>Anagrafiche di Base>Gestione Tabelle>Tabella SOPR- Ruoli degli Operatori_)
Successivamente viene richiesto di indicare la Tessera a cui dovrà essere associato lo Scontrino e in seguito verranno richiesti i riferimenti dello Scontrino.
A questo punto il programma verifica se è possibile effettuare tale elaborazione (lo scontrino non deve essere già stato associato a qualche tessera, se è prevista la scrittura dei punti e lo scontrino prevede punti negativi il cliente deve avere i punti sufficienti, etc...) e, dopo richiesta di Conferma, procederà con l'operazione richiesta (e con l'eventuale scrittura dei Punti derivati dallo Scontrino).

## Menu Configurazione Tessere

Con le funzioni presenti in questo menu vengono gestiti i Gruppi di Tessere e i Parametri di Gestione delle Fidelity Card.

## Gestione Gruppi Fidelity

All'attivazione della funzione dal _Menu>Principale>Fidelity Card>Configurazione>Gestione Gruppi Fidelity vengono elencati i Gruppi Fidelity esistenti.
Sono poi a disposizione i normali tasti funzionali di gestione di Negoziando : 

 * Invio per la Modifica
 * F4 per la Cancellazione
 * F5 per la Visualizzazione
 * F6 per Inserimento
 * F8 per Ordinare la Visualizzazione
 * F9 per la Duplicazione di un record

Premere F6 per inserire un nuovo Gruppo ed attribuire un codice alfanumerico di 3 caratteri. Confermare e a questo punto compilare i seguenti parametri : 

 * Descrizione
 * Codice Parametro. Identifica i Parametri utilizzati per tessere appartenenti a questo Gruppo (vedi Gestione Parametri Fidelity)
 * Tessere Bloccate Da/A. Permette di bloccare l'utilizzo delle tessere indicate nei programmi di Cassa
 * Anagrafica Obbligatoria. Se impostato a Si, in Cassa non sarà possibile leggere una tessera se non è stata creata la relativa anagrafica. E' possibile scegliere tra : 
 ** Sì-Sempre
 ** Sì- Se Servizio Live Raggiungibile
 ** No
 * Nr. Punti Omaggio Nuova Tessera. Sono punti che verranno attribuiti automaticamente nel momento dell'inserimento dell'anagrafica del Cliente
 * Nr. Giorni Validità Tessere
 * Data Fine Validità Tessere
 * Nr. Giorni di Non Utilizzo per Azzeramento Punti
 * Nome Formato per Stampa Tessere. E' il nome della Stampa che verrà utilizzata nelle funzioni di gestione Anagrafiche e di Stampa Tessere (Tasto F11)
 * Programma Personalizzato Gestione Anagrafiche. Tabella FIPA - File e Percorsi

## Gestione Parametri Fidelity - Globali

 _ Dal Menu>Principale>Fidelity Card>Configurazione>Gestione Parametri Fidelity - Globali_. All'attivazione della funzione vengono elencati i parametri esistenti, premere F6 per inserire un nuovo Parametro attribuendo un codice alfanumerico di 3 caratteri e confermando. Al termine inserire una descrizione e premere di nuovo Invio. Premere F6 Inserisci per attribuire il Periodo di Validità delle Tessere
Verranno richiesti : 

 * Codice Negozio/Codice Società/Codice Elenco Negozi/Codice Elenco Fidelity. Sono informazioni facoltative e servono a limitare l'utilizzo dei parametri in base ai valori indicati.
__N.B. Definire uno solo tra questi valori__
 * Sequenza Esplorazione. Questo valore serve a definire quali parametri dovranno essere utilizzati nel caso una tessera appartenga contemporaneamente a più definizioni di date di Validità.

**ESEMPIO**. All'interno di un Parametro possiamo avere diversi Periodi che impostano determinate limitazioni : 

PERIODO 1 :  1/1/2000 AL 31/12/2099 con Sequenza esplorazione 999 (periodo illimitato)
PERIODO 2 :  1/1/2003 AL 31/12/2003 con Sequenza Esplorazione 10 su un determinato Gruppo Clienti Fidelity

La lettura di una tessera è senz'altro valida per il periodo 01/01/2000 - 31/12/2099 in quanto per questo periodo non sono state messe limitazioni su Negozio/Società/Elenchi, ma nel periodo 01/01/2003 - 31/12/2003 verrà prima verificato (sequenza esplorazione 10 più bassa) se la tessera letta appartiene a quel determinato Gruppo Clienti Fidelity  e in questo caso verranno applicate le impostazioni di tale
periodo piuttosto che quelle del periodo illimitato.

Dopo aver definito le Date di Validità si entra nella Gestione dei Periodi di Validità (Tasto F8). Premere F6 Inserisci per configurare il Periodo e compilare le Informazioni richieste che sono suddivise in diversi Pannelli : 

 * **Pannello Giorni/Ore**. Sono definiti i Giorni e gli Orari in cui la tessera può essere utilizzata (in automatico il sistema propone tutti i giorni della settimana senza limite d'orario)
 * **Pannello Prezzi**. Nel caso vengano gestiti Prezzi Diversi per i Clienti Fidelity è possibile specificare come effettuare la ricerca del prezzo. Indicare : 

 ** Sequenza Prezzi. E' possibile definire fino a 6 listini tra 7 disponibili nei quali ricercare il Prezzo da attribuire all'articolo che sta acquistando il Cliente Fidelity. I listini vengono identificati come : 

L= Listino Base di Vendita
U= Listino Ufficiale
1= Listino Fidelity 1
2= Listino Fidelity 2
3= Listino Fidelity 3
4= Listino Fidelity 4
5= Listino Fidelity 5
Potremmo impostare L1(ovvero Prezzi dal Listino Fidelity 1 e dal Listino Base di Vendita), L13 (ovvero Prezzi dal Listino Fidelity 3, dal Listino Fidelity 1 e dal Listino Base di Vendita) e così via.
I Listini Fidelity utilizzati sono definiti nella Configurazione di Negoziando_ dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Fidelity>Pannello Listini Promozionali Fidelity
 ** Modalità di Esplorazione Sequenza.Le selezioni possibili sono Minor Prezzo o Primo Prezzo. In base a questa selezione il Programma di Cassa utilizzerà o il Prezzo più Basso tra tutti i Listini definiti nella  Sequenza Prezzi o il Primo Prezzo trovato __partendo da destra__ utilizzando la Sequenza Prezzi indicata.
 ** % Sconto. E' possibile definire, in alternativa o in aggiunta, che l'utilizzo della Tessera porti a uno Sconto  sul Prezzo di Vendita
 ** Applica Sconto su Listino Promozione.  Serve ad escludere (indicando No) lo Sconto se l'Articolo è già in Promozione.
 ** Causale Sconti. Selezionare la Causale di Sconto che verrà scritta sui Movimenti di Magazzino (Tabella MOTS - Motivazioni Sconti di Cassa)

 * **Pannello Raccolta Punti**. Qui vengono definite le regole per la raccolta dei Punti e la successiva Scrittura dei Movimenti Fidelity. Indicare : 

 ** Numero Punti. Punti da assegnare ogni X Euro di Spesa.
 ** Moltiplicatore Punti. E' un coefficiente che consente di moltiplicare il punteggio di un singolo Articolo (se presente)
 ** Punti Extra Scontrino. Sono i punti da riconoscere su ogni scontrino emesso.
 ** Punti Extra Articolo. Sono i punti da riconoscere su ogni riga Articolo dello scontrino emesso.
 ** Attribuisci Punti Articolo. SI/NO. Gli eventuali Punti specifici per ogni Articolo sono Definiti sul Listino Prezzi di Vendita.
 ** Moltiplicatori Punti in funzione del Totale Scontrino. E' possibile definire degli obiettivi (per il Totale Scontrino) a raggiungimento dei quali i punti da assegnare vengano moltiplicati per un dato valore.
Definire gli obiettivi (Totale Scontrino maggiore di ) e i Moltiplicatori da utilizzare. Definire inoltre la modalità di attribuzione che potrà essere A Totale o A Scalare.
Nella modalità __A Totale__ i punti complessivi dello Scontrino verranno moltiplicati in base all'ultimo obiettivo raggiunto (utilizzando solo il moltiplicatore di quest'ultimo).
Es. Se ho impostato un Totale Scontrino Maggiore di 300,00 con un Moltiplicatore di 2, fino ad un totale di 300,00 verranno attribuiti 30 punti (se ad esempio abbiamo impostato 1 punto ogni 10 euro di spesa).
Se il totale Scontrino supera i 300,00 (anche solo 300,01 euro), i miei 30 punti verranno raddoppiati.
Nella modalità __A Scalare__ i punti verranno calcolati sulla base di soglie.
Es. Se ho impostato un Totale Scontrino Maggiore di 100,00 con moltiplicatore 2 e il mio scontrino è di 150,00 (avendo impostato in precedenza 1 punto ogni 10 euro di spesa) otterrò 10 punti calcolati sui 100 che ho definito come soglia. Sui restanti 50,00 calcolerà i 5 che spettano al cliente,ma li moltiplicherà per 2.

 * **Pannello Buoni Automatici**. E' possibile definire questi parametri per ottenere l'emissione di un Buono Automatico a chiusura di uno Scontrino. Definire : 

**Informazioni per Emissione Buoni**
 * Importo Minimo Scontrino. Il Buono verrà emesso solo nel caso di Scontrini per un importo = > all'importo definito
 * % di Sconto Automatico. E' la percentuale calcolata sull'importo dello Scontrino che determina l'importo del Buono da emettere
 * Codice Casuale. Si tratta di un codice della Tabella CABU - Causali per Emissione Buoni.

**Informazioni per Utilizzo Buoni**
 * Data/Giorni Inizio Utilizzo e Data/Giorni Fine Utilizzo. Definisce il Periodo in cui i Buoni automatici potranno essere utilizzati dai Clienti
 * Importo Minimo Scontrino. Il Buono potrà essere utilizzato solo nel caso di Scontrini di importo = > a quello definito.
 * % per Calcolo Importo Minimo Scontrino. La percentuale si riferisce all'Importo dello Scontrino col quale è stato emesso il Buono in questione.
Esempio :  50%  Se lo Scontrino che ha permesso l'emissione del Buono era di 300 Euro, lo Scontrino per l'Utilizzo del Buono dovrà essere di almeno 150 Euro.
 * Escludi Utilizzo Prezzi Promozionali. Indicare se per il calcolo dell'Importo Minimo dello Scontrino che utilizzerà il Buono occorre considerare o meno articoli già in promozione

**Pannello Dipendenti**. Qui vengono definite le informazioni nel caso di utilizzo di un gruppo tessere fidelity specifico per Dipendenti. Definire : 

 * Sconto Dipendenti. E' la percentuale di Sconto riservata ai Dipendenti.
· Importo/Periodo Limite. Permettono di limitare gli Acquisti del Dipendente a un certo importo in un certo periodo (Vedi Creazione Formula per Calcolo Data)
- [Creazione Formula per Calcolo Data](Sorgenti/MB/DOC_OPE/NGBASE_19)
 * Codice Causale. E' un Codice della Tabella MOTS (Motivi di Sconto) che verrà scritto sui Movimenti di Magazzino dello Scontrino.

**Pannello Utilizzo Punti**. Qui possono essere definite le modalità di utilizzo dei Punti per attribuzione di eventuali Sconti.
Nella parte di sinistra è possibile definire gli Sconti da applicare all'utilizzo dei Punti. Potranno essere : 

 * Sconti Calcolati. Es. Sconto di 1 Euro ogno 40 Punti Utilizzati
 * Sconti Specifici. In questo caso definire i valori per i Singoli Sconti. Esempio :  ¤ 3 per 5 Punti / ¤ 7 per 10 Punti / ¤ 15 per 20 Punti etc ...
 * Minimo Punti Necessari per Utilizzo Sconti
 * Numero Massimo Punti Utilizzabili per Sconti
 * Percentuale Massima di Sconto derivata dall'utilizzo dei Punti
 * Escludi Articoli in Promozione
 * Codice Causale. Codice della Tabella MOTS (Motivi di Sconto) che verrà scritto sui Movimenti di Magazzino dello Scontrino.
 * Messaggio per Riga Sconto .Messaggio da Stampare sullo Scontrino per identificare l'utilizzo degli Sconti
 * Modalità di utilizzo Sconti
 ** Sconto in Cassa
 ** Produzione Buoni
 ** Entrambi
 * Modalità Registrazione Sconti
 ** Reso Articolo
 ** Sconto di SubTotale
N.B. Gli Sconti sono sempre Sconti di SubTotale.
In Cassa occorrerà pertanto prima premere il relativo Tasto per poter accedere a tali sconti.

**Pannello Produzione Buoni**. Qui possono essere definite le modalità di produzione dei Buoni derivati dall'Utilizzo Punti (vedi richiesta Modalità utilizzo Sconti del pannello precedente). Definire : 

**Informazioni per Emissione dei Buoni**
 * Emissione Totale Buoni. SI/NO. Indicando SI, in fase di Produzione dei Buoni sarà obbligatorio emettere Tutti i Buoni in base ai punti accumulati dal Cliente
 * Azzera Residuo Punti dopo Emissione Buoni. Indicare SI per azzerare il Residuo Punti del Cliente dopo l'Emissione dei Buoni.
 * Codice Causale (da Tabella CABU - Causali per Emissioni Buoni di Cassa)

**Informazioni per Utilizzo dei Buoni (vedi Buoni Automatici di Fine Scontrino)**
 * Periodi di Utilizzo
 * Importo Minimo Scontrino
 * Escludi Utilizzo Prezzi Promozionali SI/NO

## Gestione Parametri Fidelity - Articoli

Questa funzione permette di attivare comportamenti specifici in base all'articolo in Vendita.
N.B.Per utilizzare questa funzione occorre aver precedentemente definito i Parametri Fidelity Globali.
La definizione degli Articoli viene effettuata per Elenchi di Articoli. Per creare questi elenchi _dal Menu>Principale>Anagrafiche di Base>Gestione Elenchi/Composizioni_
Le definizioni impostate con questa funzione valgono solo per i Prezzi (Sequenza, Modalità, Sconti etc) e per la Raccolta Punti (Punti Spesa, Moltiplicatori etc).
Per le altre definizioni (Buoni, Modalità Utilizzo Punti etc) valgono le impostazioni indicate nella Gestione Parametri Fidelity - Globali.
__Nel caso di vendite di Articoli non compresi in nessun Elenco di Articoli, anche per i Prezzi e per la Raccolta Punti valgono le definizioni delle impostazioni Globali.

All'attivazione della funzione dal _Menu>Principale>Fidelity Card>Configurazione>Gestione Parametri Fidelity - Articoli viene presentato un elenco delle combinazioni Parametro/Codice Negozio/ Codice Società/Codice Elenco Negozi/Codice Elenco Fidelity esistenti. Premere Invio per Selezionare la combinazione per la quale definire i comportamenti specifici in base agli Articoli in Vendita. Dopo la selezione della combinazione si entra nella Gestione dei gli Elenchi di Articoli e delle loro Date di Validità
Premere F6 Inserisci per aggiungere le Date di Validità. Queste richieste sono le stesse della Gestione Parametri Globali (vedi annotazioni precedenti)
Le richieste Codice Negozio, Codice Società, Codice Elenco Negozi e Codice Elenco Fidelity sono bloccate in base alle selezioni iniziali. In questa maschera va impostato il Codice Elenco Articoli creato in precedenza tramite la funzione Gestione Elenchi/Composizioni.
Premere F8 per passare alla Gestione dei Periodi.
Le informazioni richieste nella Gestione del Periodo di Validità sono le stesse della Gestione Parametri Fidelity - Globali, ma i Pannelli a disposizione sono soltanto quelli relativi a **Giorni/Ore, Prezzi e Raccolta Punti**(in quest'ultimo pannello sono però escluse le informazioni relative ai Molitplicatori di Punti in funzione del Totale dello Scontrino) .
Per la definizione delle informazioni dei singoli Pannelli vedi annotazioni della Gestione Parametri Globali.

## Definizione Stampa Messaggio di Cortesia a Chiusura Scontrino

In Cassa è possibile effettuare la stampa di un Messaggio di Cortesia specifico quando viene letta una Tessera Fidelity. _Dal Menu>Principale>Anagrafiche di Base>Gestione Commenti_
Premere F6 Inserisci per creare un nuovo messaggio attribuendogli un codice alfanumerico di 3 caratteri, confermare e aggiungere una Descrizione
A questo punto selezionare la Tipologia di Commento, che, in questo caso, sarà Commento per Stampa Informazioni Fidelity su Scontrino e definire un Numero Caratteri per Riga, che servirà al programma per sapere dove andare a capo.
N.B.Le informazioni relative a Stampa su Ordine Cliente, Documento 1 e 2 non sono utilizzate dalla funzione di Stampa Messaggio di Cortesia.
Premere Invio per inserire il Testo del Commento.

ll tasto F2 Inserisci Variabile permette di visualizzare l'elenco delle variabili disponibili da inserire all'interno del commento, es.

Sig. %COG_NOM%
Nome :   %Nome%
Cognome :  %COGNOME%
Numero tessera :   %NUMTES%
Situazione Punti : 
Data :  %DATSCT%

All'emissione dello scontrino, in base ai dati recuperati dalla lettura della Fidelity, le variabili verranno compilate con le informazioni del cliente. Per impostare il Commento occorre definirne il Codice in Configurazione, dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Parametri Casse - Slave>Pannello Codice Cassa e Registratore impostare la richiesta Codice Messaggi Clienti Fidelity

## Definizione Punti Specifici Articolo

Tramite la Gestione dei Listini di Vendita, dal _Menu>Principale>Anagrafiche di Base>Listini di Vendita>Gestione Listini di Vendita, è possibile specificare dei Punti da attribuire ad un Articolo in caso di vendita compilando le due richieste presenti in basso nella maschera del dettaglio dell'articolo : 

 * Nr. Punti Tessera Fidelity (e' possibile specificare anche Punti Negativi)
 * Applica Sconti Fidelity SI/NO

- [Gestione Listini di Vendita](Sorgenti/MB/DOC_OPE/NGBASE_21)

Oltre ai punti specifici è possibile definire se applicare o meno gli eventuali Sconti definiti nei Parametri della Fidelity.

## Configurazione di Negoziando

Dopo aver definito i Gruppi, i Parametri e le Tabelle, occorre impostare la Configurazione di Negoziando. _Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Gestione Fidelity.
La configurazione Fidelity risulta suddivisa in 4 pannelli : 

**Pannello Informazioni Fidelity**

 * Attiva Gestione. Impostare SI
 * Prefisso Tessere. Si tratta delle prime due cifre del Codice a Barre. I programmi di Cassa verificano proprio questi due caratteri per determinare se si tratta della lettura di una Tessera Fidelity.
 * Gestione Anagrafiche Solo Real Time SI/NO. Impostando SI, le Anagrafiche non verranno memorizzate sul DB locale
 * Controllo Punti Attivo SI/NO. Definisce se effettuare il Controllo sui Punti del Cliente nel caso di Lettura di un Articolo con Punti Negativi.
 * Range Inserimento Fidelity DA/A. Definire eventualmente questo Range se si intende limitare l'inserimento dei Clienti ai codici compresi nei limiti.
 * Elenco Tessere per le quali è Ammessa la Modifica
 * Numero Massimo Utilizzi Giornalieri della Tessera. Se definito, i programmi di Cassa non permetteranno l'utilizzo della Tessera oltre questo numero
 * Codice Sequenza Campo per Controllo Esistenza e Messaggio in Cassa per Mancata Esistenza. **Utilizzati in Cassa Master** .( Definire eventualmente il Codice Sequenza della Tabella delle Informazioni Personalizzate (INFP) se si desidera impedire l'utilizzo della Tessera in caso manchi un'informazione anagrafica. Definire anche il messaggio da emettere in Cassa).
 * Visualizza Importo Sconti SI/NO. Se impostato a SI, nel caso in cui venga utilizzato un Prezzo Particolare per il Cliente Fidelity, in Cassa verranno inserite 2 righe, una relativa all'Articolo con il Prezzo Normale e una di Sconto per la differenza tra i due Prezzi
 * Messaggio per Righe Sconti. Si riferisce alla richiesta sopra, identifica il Messaggio relativo alla Riga di Sconto che viene scritta.
 * Calcola Automaticamente Sconti di SubTotale SI/NO. Se nella Gestione dei Parametri della Fidelity sono stati definiti degli Sconti per Utilizzo dei Punti in Cassa Slave, alla pressione del tasto Subtotale il programma determina se il Cliente ha diritto a degli Sconti e ne propone l'applicazione nello Scontrino (vedi annotazioni sull'utilizzo della Fidelity in Cassa)
 * Richiesta Dati Anagrafici se Mancanti : 
 ** NO
 ** Inserimento Obbligatorio Parametri Obbligatori
 ** Inserimento Facoltativo Parametri Obbligatori
Con l'attivazione di questa richiesta, al momento della lettura della Card in Cassa Slave verrà effettuata la verifica sugli eventuali Dati Anagrafici Mancanti. Se impostato con l'Obbligatorietà la lettura della tessera non sarà ritenuta valida fino al completamento di tali dati anagrafici. Può succedere, ad esempio, che un dato obbligatorio risulti sbagliato (magari l'indirizzo mail), quindi il negozio sarà tenuto a richiederlo al Cliente per poterlo correggere.
 * Controlla Flag Dati Anagrafici Incompleti SI/NO
 * Imposta Data Emissione uguale a Data Primo Movimento SI/NO. Impostando SI a questa richiesta, nel momento in cui si sta inserendo l'Anagrafica, Negoziando verifica se il Cliente ha già dei Movimenti. E' possibile consegnare tessere ai Clienti,ma registrarle in un secondo momento. In questo caso la Data di Inserimento del Cliente diventa la data del Primo Movimento trovato. E' nella Gestione dei Gruppi Fidelity che gestisco l'Obbligatorietà dell'Anagrafica.
 * Calcola Punti nell'Associazione Scontrino/Tessera SI/NO. Indicando SI, verranno calcolati i punti spettanti per lo Scontrino nel momento dell'associazione di uno Scontrino già emesso a una Tessera Fidelity e verranno attribuiti al Cliente.
 * Crea Nuova Tessera nella Funzione di Sostituzione SI/NO. Se impostato a SI, la Tessera con la quale se ne sostituisce un'altra dovrà essere nuova, non dovrà esistere in Negoziando
 * Blocca Utilizzo Tessere Sostituite SI/NO. Se impostato a SI, la Tessera che viene sostituita non sarà più leggibile in Cassa
 * Richiedi Operatore nella Gestione Movimenti SI/NO

**Pannello Informazioni Fidelity (2)**

 * Attiva Identificazione Automatica Fidelity in Cassa SI/NO
 * Lunghezza Minima Codice
 * Lunghezza Massima Codice
 * Caratteri Iniziali
 * Caratteri Finali
 * Codice Tessera in Formato Standard SI/NO
 * Gruppo Fidelity (per Tessere non in Formato Standard). Selezionare il Gruppo Fidelity
 * Codice Articolo per Utilizzo Punti
 * Escludi Importi GIFT non Fiscali per Calcolo dei Punti Spesa SI/NO
 * Testo da Visualizzare se Tessera Sospesa
 * Testo da Visualizzare se Tessera Bloccata

**Pannello Listini Promozionali Fidelity**

Nel caso in cui per i Clienti Fidelity vengano utilizzati Prezzi di Vendita inferiori ai Prezzi Normali definire in questa videata quali Listini di Vendita utilizzare.E' possibile specificare fino a 5 Listini diversi.
N.B. Questa definizione vale per tutte le tipologie di Tessere Fidelity. Definire nelle informazioni specifiche dei Parametri Fidelity quale di questi Listini dovrà essere utilizzato nella lettura della tessera specifica _(Pannello Prezzi > Sequenza Prezzi)_

**Pannello Movimenti Fidelity**

In questa videata vanno indicate le Causali che dovranno essere utilizzate da Negoziando sia per la Scrittura dei Movimenti Fidelity per la registrazione dei Punti nella normale vendita da Scontrino, sia per
l'utilizzo delle funzioni di Utilità del Menu Fidelity. La causali sono quelle create in precedenza all'interno della Tabella CAMF - Causali Movimenti Fidelity (Vedi Definizione Causali Movimenti Fidelity).
E' anche possibile abilitare un Negozio alla modifica di Movimenti emessi da un altro Punto Vendita.

 * Causale per Vendite da Scontrino
 * Causale per Azzeramento Punti Tessere non Movimentate
 * Causale per Azzeramento Punti Tessere del Gruppo
 * Causale per Azzeramento Punti Tessere Scadute
 * Causale per Punti Omaggio Nuova Tessera
 * Causale per Scrittura Saldi Punteggio
 * Causale per Azzeramento Movimenti Tessere Sostituite
 * Causale per Scrittura Movimenti Tessere Sostituite
 * Causale per Utilizzo Punti
 * Causale per Scrittura Movimenti Associazione Scontrino/Tessera
 * Livello di Modifica Movimenti Fidelity. E' possibile indicare : 
 ** Tutti i  Movimenti non Trasmessi
 ** Solo Movimenti Proprio Nodo e non Trasmessi

## Configurazione di Negoziando - Fidelity On Line

La gestione delle Fidelity On Line permette di aggiornare (e di consultare) i Punti del Cliente subito dopo l'emissione dello Scontrino all'interno di qualsiasi negozio della catena.
Tramite il Servizio On Line si accede anche alle informazioni anagrafiche del Cliente.
Se viene attivata la Gestione della Fidelity Card On Line, dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Negoziando InfoCenter Live>Pannello Servizi Live impostare SI alla richiesta Attiva Richieste Fidelity

Trasmissione Movimenti Fidelity
- [Negoziando Infocenter Live](Sorgenti/MB/DOC_OPE/NGBASE_20)

## Utilizzo Fidelity Card nei Programmi di Cassa

Per utilizzare le Fidelity Card in Cassa occorre effettuare la Lettura della Tessera.
E' opportuno e indispensabile, nel caso siano attivi Prezzi Speciali o Punti specifici per Articolo, effettuare la lettura della Tessera come prima operazione dello Scontrino.
Nel Pannello riservato all'operatore verrà visualizzato il Cognome e il Nome del Cliente (se l'anagrafica è esistente).
Una volta effettuata la lettura, se la Tessera risulta attiva, sarà possibile : 

 * Utilizzare i Prezzi Speciali dei Listini Fidelity
 * Utilizzare gli Sconti definiti nei Parametri
 * Utilizzare gli Sconti di Subtotale definiti nella Tabella OPCA
 * Attivare la scrittura dei Movimenti (Punti) Fidelity (tenendo conto della Regola di Attribuzione, dei Punti Specifici Articolo, dei Punti Extra Scontrino, etc)

Se la Gestione On Line è attiva, tali Movimenti verranno scritti direttamente anche sul DB di Sede.

**N.B. Non utilizzare la lettura della tessera solo per visualizzare i Punti finora raccolti dal Cliente. La lettura della Tessera memorizza tale Codice, che verrà usato per l'emissione dello Scontrino secondo i parametri letti. Se la lettura viene effettuata erroneamente, utilizzare gli appositi tasti per la Pulizia delle informazioni dello Scontrino.

## Modalità On Line

Se la modalità in oggetto è attiva, le informazioni dei Clienti Fidelity vengono richieste al Server Centrale (normalmente in Sede) e risultano quindi sempre aggiornate all'ultimo Scontrino emesso per quel Cliente in qualsiasi Negozio abbia effettuato un acquisto o abbia utilizzato dei Punti.
Nel caso in cui ci siano problemi con la connessione al Server di Sede non sarà possibile utilizzare le Tessere emesse da altri Punti Vendita (se nella Gestione dei Gruppi viene impostato Anagrafica
Obbligatoria a SI), inoltre il programma di Cassa non sarà in grado di interrogare il numero di punti accumulati e non permetterà quindi operazioni che ne prevedono l'utilizzo. Sarà possibile invece accumulare i punti che verranno scritti nel Database del Negozio e verranno inviati al Server Centrale con le trasmissioni serali (vedi Gestione Trasmissioni)

GESTIONE TRASMISSIONI


## Utilizzo in Cassa dei Buoni per Clienti Fidelity

Nei Parametri per la Generazione dei Buoni esiste la richiesta Elenco Clienti per cui generare i Buoni. Se impostato un Elenco di Clienti Fidelity (Elenchi/Composizioni) verranno prodotti dei Buoni solo per quei clienti.
In Configurazione _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Pannello Altri Parametri 2 impostare SI alla Richiesta Ricerca Automatica Buoni per Clienti Fidelity
In Cassa passare la Fidelity, bippare gli articoli che il cliente sta acquistando e premere Subtotale. In questo momento il Sistema, in base alla configurazione impostata, effettuerà la Ricerca di Buoni disponibili per il Cliente, prima cercherà tutti i Buoni legati a delle Promozioni, poi i Buoni Sconto a Valore legati alla sua Fidelity.

## Utilizzo Fidelity Card in Cassa

Oltre a quanto precedentemente indicato per l'utilizzo delle Tessere in Cassa, sarà inoltre possibile : 

**Gestire le informazioni di "Utilizzo Punti" dei Parametri Fidelity**

Se nella Configurazione di Negoziando viene specificato SI alla richiesta Calcola Automaticamente Sconti di SubTotale e viene premuto il tasto Subtotale o se in Cassa, dopo aver premuto il tasto Subtotale viene premuto un Bottone specifico (che dovrà avere come caratteristica :  FCode ="DISCSUBTFIDELY"), verrà visualizzato un Pannello riepilogativo con lo Sconto massimo che è possibile concedere al Cliente. Premere F6 per confermare l'applicazione dello Sconto nello Scontrino o premere F7 per modificarlo (l'importo dello Sconto viene determinato sulla base dei Punti utilizzati, il nuovo valore indicato non potrà essere superiore a quello proposto dal sistema).

**Visualizzare il Totale dei Punti del Cliente** (senza memorizzare il Codice Tessera per lo Scontrino)

Definire nella tastiera di Cassa un Bottone specifico con la caratteristica FCode="DSPFIDPOINTS". Apparirà una maschera, bippare o digitare a mano il codice della Fidelity e premere Invio. A questo punto verrà visualizzato il dettaglio dei Punti

**Modificare le Informazioni Anagrafiche di un Cliente**

Definire nella tastiera di Cassa un Bottone specifico con le caratteristiche FCode="INTFUN" FAttr="MODANAGFIDELITY"
Digitare/bippare il codice Tessera e premere Invio. Verranno successivamente richieste le informazioni della funzione di Modifica della Gestione Anagrafica.

**Inserire in Anagrafica Nuovi Clienti**

Definire nella tastiera di Cassa un Bottone specifico con le caratteristiche FCode="INTFUN" FAttr="INSANAGFIDELITY"
Alla pressione del Bottone verranno richieste le informazioni della funzione di Inserimento della Gestione Anagrafica.

**Auditing**

E' possibile memorizzare tutte le modifiche (Inserimenti/Variazioni/Annullamenti) che vengono apportate ai record presenti nelle Tabelle dei Movimenti o delle Anagrafiche Fidelity.
Per attivare questa funzione impostare la Gestione dell'Auditing dal _Menu>Utilità>Gestione Auditing>Gestione Famiglie Auditing

(VEDI AUDITING)

**Stampe Movimenti di Magazzino Clienti Fidelity**

Nelle Stampe relative ai Dati del Venduto che utilizzano direttamente la tabella dei Movimenti di Magazzino è possibile impostare nei criteri di Selezione il range di Tessere Fidelity su cui effettuare
l'elaborazione.

**Generazione Virtual Card**

Per fornire una definizione di Virtual Card è opportuno fare riferimento all'implementazione svolta in Negoziando.
Attualmente Negoziando supporta le tessere virtuali di tipologia "Passbook".
Passbook è un'applicazione sviluppata da Apple con la quale si possono gestire biglietti di viaggio, carte fedeltà, coupon, biglietti per eventi e genericamente altre forme di Mobile Payment.
Di seguito verranno elencati i prerequisiti software che dovranno essere soddisfatti affinchè la generazione della Carta Fedeltà sia correttamente eseguita : 

__Prerequisiti Software__

 * Installazione del pacchetto OpenSSL
(http://slproweb.com/download/Win32OpenSSL_Light-1_0_1e.exe)
Nota bene :  OpenSSL potrebbe richiedere in fase di installazione, il seguente pacchetto "Visual C++ Redistributable 2008" da installare
http://www.microsoft.com/downloads/details.aspx?familyid=9B2DA534-3E03-4391-8A4D-074B9F2BC1BF
 * Registrazione da parte dell'azienda presso il sito Apple e scarico del certificato necessario alla firma elettronica da apporre alla Carta Fedeltà : 
 ** Registrazione/Accesso (se in possesso di un account) al sito https://developer.apple.com/devcenter/ios/index.action
 ** Accesso alla parte del sito "iOS Provisioning Portal"
 ** Recupero certificati dal sito Apple  : 
 *** Accedere alla sezione " Pass Type IDs" e selezionare "New Pass Type ID"
 *** Fornire le informazioni richieste e generare il Pass ID. Nota bene  :  il Pass ID appena generato, sarà collegato direttamente alla carta fedeltà, mediante un riferimento diretto all'interno del file Pass.json.
 *** Scaricare il certificato appena generato ed aggiungerlo al proprio KeyChain (applicazione disponibile su MAC/OS)
 *** All'interno dell'applicazione KeyChain, selezionare "Certificates " presente sotto "Categories"
Selezionare il Pass Type ID creato in precedenza, e mediante il tasto destro, selezionare "Export..." Salvare quindi il file avente estensione .p12 (es. Certificates.p12)
Lanciare i seguenti comandi OpenSSL  : (sostituire opportunamente il nome del file .P12 , oltre ovviamente alla password 12345)
_openssl pkcs12 -in Certificates.p12 -clcerts -nokeys -out passcertificate.pem -passin pass : 12345
Lanciare successivamente il seguente comando OpenSSL (sostituire opportunamente il nome del file .P12 , oltre ovviamente alla password 12345)
_openssl pkcs12 -in Certificates.p12 -nocerts -out passkey.pem -passin pass :  -passout pass : 12345
 *** Provvediamo infine a scaricare un ulteriore certificato, aprendo nuovamente lapplicazione MAC/OS "KeyChain" , selezionando "Certificates" e successivamente "Apple Worldwide Developer Relations Certification Authority", scorriamo i sotto elementi del nodo e selezioniamo WWDR. (Nota Bene  :  Se il nodo non dovesse contenere un elemento di nome WWDR, aprire il seguente link :http://www.apple.com/certificateauthority/ , scaricare il certificato .cer ed importarlo in keychain)
Selezioniamo quindi WWDR e con il tasto destro, richiamiamo la voce Export "Apple WorldWide Developer Relations Certification Authority"
Si aprirà una finestra, dove selezioneremo il nome file WWDR ed il formato "Privacy Enhanced Mail" (.pem).
 *** A questo punto, avremo a disposizione i seguenti 4 files  : 
- Certificates.p12
- Passcertificate.pem
- Passkey.pem
- WWDR.pem
Oltre alla password utilizzata per i comandi OpenSSL.
Conservare queste informazioni, richieste in fase di configurazione Negoziando.
Nota Bene :  la procedura sopra descritta andrà effettuata solo 1 volta e comunque fino all'ottenimento dei 4 file appena elencati

**Struttura della Carta Fedeltà in formato Passbook (.pkpass)**

Tecnicamente, la Carta Fedeltà in formato pkpass è composta da un file in formato ZIP contenente i seguenti file : 

 * **strip.png** (fornito dall'utente -> è lo sfondo grafico della carta fedeltà)
 * **strip@2x.png** (fornito dall'utente -> idem come sopra)
 * **icon.png** (fornito dall'utente -> è l'icona della carta fedeltà)
 * **icon@2x.png** (fornito dall'utente -> idem come sopra)
 * **logo.png** (fornito dall'utente -> logo della carta fedeltà)
 * **logo@2x.png** (fornito dall'utente -> idem come sopra)
 * manifest.json (generato da Negoziando)
 * **pas.json** (template fornito dall'utente - nel presente documento, è fornito un esempio completo della struttura del file) Nota Bene  :  il file pass.json può essere generato da appositi siti internet dedicati alla
generazione di passbook (es: http://passkit.com/samples/ )
All'interno del file, sarà possibile specificare le seguenti chiavi, che verranno sostituite dinamicamente, da Negoziando  : 
 ** %NOME% (è il nome del cliente)
 ** %COGNOME% (è il cognome del cliente)
 ** %PUNTI% (è il saldo punti tessera del cliente)
 ** %TESSERA% (è il codice tessera del cliente)
 ** %DATA_SCADENZA% (è la data di scadenza della tessera)
 ** %EMAIL% (è l'indirizzo email del cliente - se presente)
 * signature (generato da Negoziando)
N.B :  i file segnalati in grassetto devono obbligatoriamente essere presenti all'atto di generazione del passbook mediante tasto F12 dalla Gestione Anagrafica Fidelity.
I file non evidentiati verranno generati automaticamente da Negoziando.

## Configurazione Applicativa Negoziando

A questo punto è opportuno procedere con la configurazione Applicativa di Negoziando.
Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Virtual Card, premere INVIO e compilare i seguenti campi : 

 * Directory di Lavoro. Cartella nella quale dovranno essere presenti i file descritti nel paragrafo Struttura della Carta Fedeltà in formato Passbook (.pkpass)
 * Directory di Salvataggio. Cartella nella quale verrà salvato il file finale della carta fedeltà in formato .pkpass
 * Percorso File Certificato. E' il percorso del file WWDR.pem (vedi i 4 file evidenziati in alto)
 * Percorso File Signer. E' il percorso del file PassCertificate.pem (vedi i 4 file evidenziati in alto)
 * Percorso File Chiave Privata. E' il percorso del file PassKey.pem (vedi i 4 file evidenziati in alto)
 * Password Certificato. E' la password specificata nei comandi OpenSSL definiti in alto.
 * Percorso File Openssl.exe. E' il percorso del file openssl.exe utilizzato per i comandi in precedenza.

Premere INVIO per salvare i valori di configurazione.

**Generazione Carta Fedeltà (Tipo Passbook)**

Di seguito riportiamo un tutorial che vi guiderà attraverso tutte le fasi di creazione di una Carta Fedeltà (compatibile con l'App Passbook http://en.wikipedia.org/wiki/Passbook_(application)) emessa direttamente da Negoziando.

 * Dalla maschera Anagrafica Clienti Fidelity selezionare un nominativo dell'elenco e premere F12 Genera Virtual Card
 * Verranno richieste le due impostazioni qui riportate : 

 ** Invio Automatico Mail al Cliente
 ** Apri Cartella al Termine dell'Elaborazione

Impostare i flag nel modo più opportuno, ma è bene tener presente che se l'indirizzo email del cliente in anagrafica fidelity doverre essere errato, la Mail non giungerà a destinazione.
Premere INVIO per effettuare la generazione della Carta
Il file creato avrà estensione .pkpass.
Infine viene riportato un esempio del file pass.json (template) utilizzato per la realizzazione del pass di esempio.
Le parole in maiuscolo, rappresentano i campi dinamici, sostituiti da Negoziando in fase di generazione della Tessera Fedeltà  : 
{
"storeCard" : 
{
"auxiliaryFields" : 
[
{
"key" : "auxiliary1",
"label" : "Saldo Punti",
"value" : "%PUNTI%",
"textAlignment" : "PKTextAlignmentLeft"
},
{
"key" : "auxiliary2",
"label" : "Data Scadenza",
"value" : "%DATA_SCADENZA%",
"textAlignment" : "PKTextAlignmentNatural"}
],
"secondaryFields" : 
[
{
"key" : "secondary1",
"label" : "Cliente",
"value" : "%NOME% %COGNOME%",
"textAlignment" : "PKTextAlignmentLeft"
}
]
},
"passTypeIdentifier" : "pass.biz.negoziando.query",
"organizationName" : "Query SPA",
"backgroundColor" : "rgb(215,25,33)",
"labelColor" : "rgb(255,255,255)",
"barcode" : {
"message" : "%TESSERA%",
"messageEncoding" : "iso-8859-1",
"format" : "PKBarcodeFormatPDF417",
"altText" : "%TESSERA%"
},
"locations" :  [
{
"relevantText" : "Query Store Paderno Dugnano",
"longitude" : 9.1192436,
"latitude" : 45.579245
}
],
"serialNumber" : "%TESSERA%",
"logoText" : "Query",
"suppressStripShine" : true,
"teamIdentifier" : "77FGHJUR8K",
"formatVersion" : 1,
"description" : "Query Store Fidelity Card",
"foregroundColor" : "rgb(255,255,255)"
}

Inoltre, notare il valore delle seguenti chiavi  : 

 * "teamIdentifier"  :  identificativo dell'azienda, rilasciato da Apple.
 * "passTypeIdentifier"  :  identificativo presente nel certificato rilasciato da Apple.
 * "serialNumber"  :  identificativo univoco, che distingue ogni singola carta fedeltà generata.
