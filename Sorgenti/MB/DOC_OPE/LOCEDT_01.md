# Introduzione

L'editor di Loocup ha il compito di permettere l'editazione di tutte le parti testuali dello Sme.up. A tale scopo mette a disposizione le principali funzioni di editing e di ricerca nel testo presenti negli altri editor. Eccezion fatta per la gestione delle note strutturate, l'editor mette a disposizione una visualizzazione coadiuvata dall'evidenziazione dei comandi (hilight) e di uno strumento di aiuto alla composizione  sintattica delle specifiche (wizard).
Ogni pannello di testo aperto riporta una etichetta che identifica il file che si sta editando :  se il pannello è aperto in scrittura l'etichetta avrà scritta blu, se il testo è in sola lettura l'etichetta avrà la scritta rossa. Inoltre ad indicare la modalità sola lettura del testo c'è una bordatura blu attorno all'area di visualizzazione del testo.
La finestra di Text editor è costituita da : 
 * una menu bar di due colori :  le voci nere sono le voci di menù generali di Loocup, mentre le voci di menù azzurre sono caratteristiche dell'editor;
 * una tool bar superiore coni bottoni per l'utilizzo rapido di alcune funzioni principali dell'editor :  il salvataggio, l'undo/redo e copia/taglia/incolla;
 * tool bar inferiore, posta alla base della finestra dell'editor, con bottoni che forniscono svariate funzioni : 
 ** nella parte sinistra sono riportate tutte le funzioni associate a tasti funzione attivi nell'editor;
 ** nella parte destra sono disponibili alcune funzioni speciali che verranno spiegate più avanti.

# Operazioni del text editor
Possiamo suddividere le funzionalità dell'editor di testi in due gruppi :  quelle comuni a tutti i tipi di testo e quelle dipendenti dal tipo di testo che si sta gestendo.
Le funzioni specifiche sono
 * Funzioni di visualizzazione
 * Compila
 * Wizard
Le funzioni specifiche sono attivate automaticamente :  il componente aggiungerà dei pulsanti appositi nella barra in basso.

## Funzioni di editing
L'editor supporta le funzioni di copia/taglia/incolla attraverso, rispettivamente, i comandi **CTRL+C**, **CTRL+X** e **CTRL+V**, oltre che attraverso le voci di menù presenti in _9_Modifica. Sempre sotto il menù _9_Modifica sono presenti le voci di selezione di tutto il testo (**CTRL+A**), di parola, di riga e di paragrafo. Infine, per quanto riguarda le funzioni di editing di base, sono disponibili le funzioni di UNDO e REDO (rispettivamente **CTRL+Z** e **CTRL+Y**). Anche queste ultime sono utilizzabili attraverso le voci di menù _9_Annulla** e _9_Ripristina presenti sotto _9_Modifica, oppure tramite i bottoni _9_Undo e _9_Redo_n_ nella barra degli strumenti.

## Funzioni di ricerca/sostituzione
Le funzioni in questione sono richiamabili, tramite il menù _9_Ricerca oppure, alternativamente con **CTRL+F**, **CTRL+G**, **CTRL+R**. Più precisamente **CTRL+R** apre la finestra per la sostituzione, **CTRL+F** permette di impostare la ricerca e **CTRL+G** fornisce la funzione di "cerca ancora".

## Funzioni di visualizzazione
Per i tipi di testo con sintassi definita :  Script di configurazione, script di scheda, script di documentazione è possibile attivare una visualizzazione supportata da syntax highlight. La funzione è attivabile/disattivabile attraverso **CTRL+H**, attraverso la voce di menù _9_Highlight nel menù _9_Visualizza, oppure tramite il bottone _9_HL presente sulla barra degli strumenti dell'editor. Quando l'highlight è attivo, il bottone _9_HL risulta di colore giallo.

## Funzioni di salvataggio
E' possibile effettuare il salvataggio del testo che si sta editando attraverso varie vie. Innanzitutto ciò che indica che il testo che si sta editando è stato modificato è la colorazione gialla dell'icona in alto a sinistra (sotto il nome del file) rappresentante un disco floppy. Per effettuare il salvataggio del documento è sufficiente cliccare su tale icona oppure, in alternativa, la stessa icona in basso a sinistra, o anche il tasto **F7**.
Il "Salva con nome" per rinominare il file avviene tramite il tasto **F6** o l'icona in basso a sinistra rappresentante un floppy sovrapposto ad un foglio di carta.
Per l'eliminazione del file, si utilizza il tasto **F8** oppure, alternativamente, il bottone in basso a sinistra simile al "salva con nome" ma con una X rossa.

## Compila (Ctrl+K)
Questa azione è presente solo nel caso in cui si stiano gestendo le regole del configuratore.
Consente di verificare tutte le regole presenti in un'unica operazione.

## F15 (esamina/copia)
Il tasto F15 permette di aprire (in lettura) sino a tre files e visualizzarli all'interno dell'editor (oppure quanti se ne vuole in finestre separate) per eventuali esigenze di confronto, copia, controllo. La finestra di servizio che si apre al richiamo del F15 permette di esprimere sia il file che si vuole aprire, sia la modalità di apertura che si vuole (in finestra o esterna).
I files che si sono aperti con la modalità F15 si chiudono con F12 nell'ordine inverso rispetto a come sono state aperti.
La navigazione fra un pannello e l'altro può avvenire con la combinazione di tasti **CTRL+ALT+TAB**.

## Wizard (Control+W)
Questa azione è disponibile in tutti gli script dove è definita una sintassi.
Utilizzando il comando wizard il componente cercherà se nella riga è presente un elemento di definizione della sintassi e

## Preview (Control+P)
Non implementata

## Ricapitolando le funzioni definite nell'editor
 :  : PAR F(01) L(PUN)
- Copia :     CTRL+C
- Taglia :     CTRL+X
- Incolla :     CTRL+V
- Sotituisci :     CTRL+R
- Cerca :     CTRL+F
- Cerca ancora :     CTRL+G
- Seleziona tutto :     CTRL+A
- Syntax highlight :     CTRL+H
- Salva con Nome :     F6
- Salva :     F7
- Elimina :     F8
- Compila :     F9 (*)
- Esamina/Copia :     F15
- Richiamo Wizard :     CTRL+W (*)
- Preview :     CTRL+P (*)

