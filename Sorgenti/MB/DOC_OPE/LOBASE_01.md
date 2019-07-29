# Scopo di questa guida
Scopo di questa guida è quello di illustrare : 
 * cosa è LOOC.up;
 * come è composta e come funziona l'interfaccia grafica;
 * quali sono e come funzionano i tasti;
 * quali sono e come funzionano i componenti;
 * quali sono e come effettuare le operazioni di base.

# A chi è rivolta
L'audience di riferimento sono tutti gli utenti di LOOC.up.

# Prerequisiti
I prerequisiti all'uso di questa guida sono la familiarità con le interfacce Windows e con le applicazioni Sme.Up.

# Installazione
Fare riferimento al Manuale Applicativo ed in particolare al paragrafo "Installazione client Looc.up"
- [Installazione client Looc.UP](Sorgenti/MB/DOC/LOBASE_031)

# Porte utilizzate da Loocup / Sme.UP Provider
- [Looc.UP - Porte comunicazione](Sorgenti/MB/DOC/LOBASE_000)

# Attivazione in Windows
All'avvio di LoocUp viene presentata la seguente finestra di identificazione : 
![LOBAS_01](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_01.png)
Per accedere, bisogna riempire i seguenti campi : 
 * Sistema :  nome iSeries a cui si vuole accedere, può essere indifferentemente :  l'indirizzo IP o il nome del server iSeries;
 * Utente :  nome utente iSeries con cui collegarsi;
 * Password :  password dell'utente iSeries;
 * Ambiente (facoltativo) :  nome dell'ambiente applicativo (sistema informativo) a cui ci si collega; se ve ne è uno solo, questo viene preso come default.

**NOTA : ** per poter utilizzare la gestione stampe e dei lavori è necessario che venga indicato il nome del server iSeries e non l'indirizzo IP.

Dopo l'avvenuta autenticazione da parte del sistema vengono avviati i moduli di LoocUp evidenziati nella system tray della barra delle applicazioni di Windows : 
 * Il modulo base di Loocup
 * Il gestore della scheda
 * Il gestore dell'emulazione

![LOBAS_09](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_09.png)
Per un corretto funzionamento di LoocUp tutti i moduli devono essere attivi. Nel caso in cui una delle tre componenti si arresti si consiglia di chiudere e riavviare l'applicazione.

Per una descrizione dettagliata delle tre componenti fare riferimento al manuale applicativo.
- [Documentazione applicazione](Sorgenti/MB/DOC/LOBASE)

Durante la fase di avvio viene inoltre visualizzata la finestra dei suggerimenti.

# Finestra dei suggerimenti
La finestra dei suggerimenti propone all'utente, in modo casuale, una voce del Glossario o del dizionario degli Acronimi utilizzati nell'ambiente Smeup.
![LOBAS_02](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_02.png)
## Apertura
Viene visualizzata di default all'avvio di LooUp. L'utente può riaprire in qualunque momento la finestra selezionando il pulsante "Suggerimenti" nella finestra Informazioni su LoocUp che si ottiene dal menù a tendina "Help > About".
![LOBAS_04](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_04.png)
## Configurazione
L'apertura della finestra all'avvio di LoocUp è configurabile dall'utente selezionando/deselezionando il Checkbox presente nella finestra stessa : 
![LOBAS_06](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_06.png)
oppure selezionando/deselezionando il checkBox presente nella finestra Informazioni su LoocUp : 
![LOBAS_07](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_07.png)
## Nuovo elemento
Selezionando il pulsante **Un altro...** viene proposto all'utente una nuova voce del Glossario o degli Acronimi utilizzati nell'ambiente Smeup.

## Dettaglio
Selezionando il pulsante **Saperne di più...** si accede alla scheda di approfondimento dell'elemento visualizzato.
![LOBAS_08](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_08.png)
# Versione di LoocUp
Selezionando il link  **Help - Versione modulo corrente** si apre una finestra con informazioni riguardanti : 
 * la versione in uso di LoocUp;
 * la versione della componente grafica in uso.

![LOBAS_05](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_05.png)
# Informazioni su LoocUp
Selezionando il link  **Help - About** si apre la finestra Informazioni su LoocUp.
![LOBAS_04](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_04.png)
Informazioni visualizzate riguardano : 
 * la versione in uso di LoocUp;
 * la versione, il tipo di rilascio e la data di rilascio dei tre moduli che compongono LoocUp;
 * la versione della Java Virtual Machine (JVM) installata.

# Chiusura normale
E' possibile chiudere l'applicazione LoocUp

 - selezionando il pulsante con la X bianca in cerchio rosso : 

![LOBAS_12](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_12.png) * con il tasto funzione **F23**;
 * selezionando la voce di menu **File -> Exit**
 * selezionando la voce Esci del popup che compare cliccando con il tasto destro del mouse sull'icona di Loocup Base Module (Loocup Java Client) presente nella barra di sistema. La barra di sistema o system tray è quella parte dello schermo in basso a sinistra che l'orologio e le icone di alcune applicazioni.

# Chiusura anomala
In caso di errore dell'applicazione e nell'impossibilità di chiuderla seguendo la procedura normale, LoocUp può essere arrestato chiudendo i singoli moduli dalla system tray oppure utilizzando le funzionalità del Task Manager di Windows.

## Chiusura dalla system tray
I tre moduli presenti nella system tray devono essere arrestati singolarmente
 * posizionando il puntatore del mouse sull'icona del modulo;
 * aprendo con il tasto destro del mouse il menu relativo al modulo;
 * selezionando la voce **chiudi**.

![LOBAS_10](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_10.png)Per un corretto funzionamento di LoocUp tutti i moduli devono essere attivi :  pertanto in caso di errore o di arresto di uno dei moduli è consigliabile la loro chiusura prima di riavviare LoocUp.

## Chiusura da Task Manager
Qualora nessuna delle precedenti procedure sia efficace è possibile arrestare LoocUp dalla finestra Task Manager di Windows : 
 * aprire la finestra del Task Manager (premere contemporaneamente i tasti  Cntrl + Alt + Canc);
 * selezionare il tab **Applicazioni**;
 * selezionare in sequenza i moduli di LoocUp attivi e cliccare sul pulsante **Termina operazione

![LOBAS_11](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_11.png)
# Struttura di una finestra di LoocUp
Nella seguente immagine possiamo avere una visione d'insieme degli elementi grafici.
![LOBAS_13](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOBAS_13.png)
Di seguito diamo una definizione degli elementi grafici principali

## Barra del titolo - Title Bar
Permette di avere informazioni su : 
 * collegamento :  sistema a cui si è collegati, ambiente, utente;
 * programma :  nome programma, tipo di operazione che si effettua (nella finestra di Emulazione);
 * lavoro :  il numero di lavoro associato all'istanza di LoocUp.

Il colore della Title Bar permette di capire su quale finestra avviene l'interazione, il colore dipende dalla configurazione dell'aspetto di Windows in uso.

Nel componente Emulatore la title bar permette di accedere a funzionalità tipiche dell'emulazione (Rif. Capitolo "Emulatore").

## Barra di testa -  Header Bar
Permette di avere informazioni su : 
 * collegamento :  sistema a cui si è collegati, ambiente;
 * programma :  nome programma, tipo di operazione che si effettua;
 * oggetto in gestione :  icona che rappresenta l'oggetto su cui si effettuano le operazioni (il soggetto dell'interazione);
 * componente LOOC.up :  icona del componente di LOOC.up attualmente in uso e la sua decodifica.

## Barra dei menu - Menu Bar
Permette di accedere alle funzioni generali di LoocUp e alle funzioni proprie del componente in uso.
Le voci in colore nero sono quelle predefinite, mentre quelle in blu sono specifiche del componente.
Le voci possono inoltre dipendere da
 * utente
 * ambiente
 * azienda
 * autorizzazioni

## Barra degli strumenti -  Tool Bar
Permette di accedere alle funzioni generali di LoocUp e alle funzioni proprie del componente in uso attraverso l'uso dei bottoni.

## Barra di stato - Status Bar
Permette di avere informazioni su : 
 * stato del sistema;
 * parametri della funzione che si sta richiamando;
 * nome del programma ed nome del video (solo se emulatore);
 * altre informazioni tipiche del componente che la ospita.

## Menù di Popup - Popup Menu
Il Popup menu è accessibile cliccando con il tasto destro del mouse su un campo tipizzato, cioè un campo che Looc.Up riconosce come contenente oggetti applicativi di Sme.Up.
Il menù di popup permette di accedere a : 
 * funzioni di visualizzazione, inserimento, copia, modifica, ecc., tipiche dell'oggetto che si sta manipolando;
 * scheda dell'oggetto;
 * funzioni di LOOC.up specifiche dell'oggetto;
 * funzioni di SME.up specifiche dell'oggetto.

# Componenti grafici
Di seguito diamo una definizione dei componenti grafici principali.

## Scheda
![LOCEXD_01](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOCEXD_01.png)Definiamo scheda un insieme di sezioni disposte sul video. Ogni sezione può contenere subsezioni rappresentate da un "TAB".
Una subsezione può rappresentare uno fra i seguenti componenti grafici : 
 * albero
 * bottoniera
 * cruscotto
 * grafico
 * immagine
 * input panel
 * label (etichetta)
 * lista immagini
 * matrice
 * semaforo
 * testo

Essendo una scheda un componente grafico può essere a sua volta inserita in una subsezione di un'altra scheda.

## Albero
![TRE003](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/TRE003.png)L'albero è la componente grafica che visualizza le informazioni in forma gerarchica. Un albero si compone di due tipi di sottostrutture fondamentali : 
 * il nodo che contiene informazioni;
 * l'arco che stabilisce un collegamento gerarchico fra due nodi.

Si parla allora di un nodo padre dal quale esce un arco orientato che lo collega ad un nodo figlio. Ogni nodo che non presenta archi uscenti, è detto foglia.

## Matrice
![LOCEXB_049](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOCEXB_049.png)La matrice è la componente grafica che visualizza le informazioni in formato tabellare a due dimensioni.

## Grafico
![EXA_01](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/EXA_01.png)I grafici sono rappresentazioni di dati numerici. I grafici facilitano la comprensione e il confronto dei numeri da parte dell'utente, per questo motivo sono diventati un modo molto usato di rappresentare i dati numerici.
I dati di una matrice possono essere rappresentati su grafici di tipo diverso in cui i valori sono visualizzati come linee, barre, colonne, sezioni di torta e così via.

## Semaforo
![LOCSEM_01](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOCSEM_01.png)Indicatore grafico su tre livelli che fornisce una valutazione di criticità di una informazione basata su un valore numerico.
 * verde :  situazione non critica
 * arancio :  situazione di attenzione
 * rosso :  situazione critica

## Cruscotto
![LOCGAU_01](http://localhost:3000/immagini/MBDOC_OPE-LOBASE_01/LOCGAU_01.png)Rappresenta in modo grafico un valore numerico associando al valore una misura di criticità con la logica della componente semaforo.

## Input panel
L'Input Panel (o Pannello di Input) è uno strumento che permette di inserire e modificare in una singola sottosezione, dati eterogenei.

# Finestra di emulazione
 L'emulatore è uno dei componenti principali di LoocUp. La sua funzione è quella di consentire l'utilizzo dei programmi SME.up dotati di interfaccia 5250.
