# Manuale di utilizzo dell'editor di Loocup
## Cenni generali
L'editor di Loocup ha il compito di permettere l'editazione degli script (> files SCP_*  ), delle note, delle regole del configuratore. A tale scopo mette a disposizione le principali funzioni di editing e di ricerca nel testo presenti negli altri editor. Per l'editing dei file di script l'editor mette a disposizione una visualizzazione coadiuvata da highlight; inoltre, sempre per questi tipi di files l'editing può essere effettuato avvalendosi di funzioni di wizard che facilitano la composizione sintattica delle specifiche.
## Cosa trovi nella finestra dell'editor
Dalla versione **2.0** dell'editor ogni pannello di testo aperto riporta una label che identifica il file che si sta editando. Se il pannello è aperto in scrittura la label avrà scritta blu, se il testo è read only la label avrà scritta rossa. Inoltre ad indicare la modalità read only del testo c'è una bordatura blu attorno all'area di visualizzazione del testo.
### Il menu di finestra
La finestra presenta un menu di due colori :  le voci nere sono le voci di menù generali di Loocup, mentre le voci di menù azzurre sono caratteristiche dell'editor
### La barra degli strumenti
Essa presenta dei bottoni per l'utilizzo rapido di alcune funzioni principali dell'editor :  il salvataggio, l'undo/redo e copia/taglia/incolla.
![LOCEDT_01](http://localhost:3000/immagini/MBDOC_OPE-LOCEDT_MAN/LOCEDT_01.png)### La barra dei bottoni
I bottoni posti alla base della finestra dell'editor forniscono svariate funzioni, nella parte sinistra sono riportate tutte le funzioni associate a tasti funzione attivi nell'editor. Nella parte destra sono disponibili alcune funzioni speciali che verranno spiegate più avanti nel documento nella sezione >"Concetti e funzioni avanzate".
![LOCEDT_02](http://localhost:3000/immagini/MBDOC_OPE-LOCEDT_MAN/LOCEDT_02.png)## Elementi di base
### Funzioni di editing
L'editor supporta le funzioni di copia/taglia/incolla attraverso, rispettivamente, i comandi **CTRL+C**, **CTRL+X** e **CTRL+V**, oltre che attraverso le voci di menù presenti in _9_Modifica. Sempre sotto il menù _9_Modifica sono presenti le voci di selezione di tutto il testo (**CTRL+A**), di parola, di riga e di paragrafo. Infine, per quanto riguarda le funzioni di editing di base, sono disponibili le funzioni di UNDO e REDO (rispettivamente **CTRL+Z** e **CTRL+Y**). Anche queste ultime sono utilizzabili attraverso le voci di menù _9_Annulla** e _9_Ripristina presenti sotto _9_Modifica, oppure tramite i bottoni _9_Undo e _9_Redo_n_ nella barra degli strumenti.
### Funzioni di ricerca/sostituzione
Le funzioni in questione sono richiamabili, tramite il menù _9_Ricerca oppure, alternativamente con **CTRL+F**, **CTRL+G**, **CTRL+R**. Più precisamente **CTRL+R** apre la finestra per la sostituzione, **CTRL+F** permette di impostare la ricerca e **CTRL+G** fornisce la funzione di "cerca ancora".
### Funzioni di visualizzazione
Per i tipi di testo con sintassi definita :  Script di configurazione, script di scheda, script di documentazione è possibile attivare una visualizzazione supportata da syntax highlight. La funzione è attivabile/disattivabile attraverso **CTRL+H**, attraverso la voce di menù _9_Highlight nel menù _9_Visualizza, oppure tramite il bottone _9_HL presente sulla barra degli strumenti dell'editor. Quando l'highlight è attivo, il bottone _9_HL risulta di colore giallo.
### Funzioni di salvataggio
E' possibile effettuare il salvataggio del testo che si sta editando attraverso varie vie. Innanzitutto ciò che indica che il testo che si sta editando è stato modificato è la colorazione gialla dell'icona in alto a sinistra (sotto il nome del file) rappresentante un disco floppy <img src="file : [SME.ICO]\LO\LOCEDT\f07.gif" width="16" height="16">. Per effettuare il salvataggio del documento è sufficiente cliccare su tale icona oppure, in alternativa, la stessa icona in basso a sinistra, o anche il tasto **F7**.
Il "Salva con nome" per rinominare il file avviene tramite il tasto **F6** o l'icona in basso a sinistra rappresentante un floppy sovrapposto ad un foglio di carta <img src="file : [SME.ICO]\LO\LOCEDT\f06.gif" width="16" height="16">.
Per l'eliminazione del file, si utilizza il tasto **F8** oppure, alternativamente, il bottone in basso a sinistra simile al "salva con nome" ma con una X rossa <img src="file : [SME.ICO]\LO\LOCEDT\f08.gif" width="16" height="16">.
## Concetti e funzioni avanzate
Oltre alle normali funzioni di un editor, l'editor di Loocup ne presenta alcune specifiche.
### F9 (compila)
Il tasto F9 ( icona <img src="file : [SME.ICO]\LO\LOCEDT\f09.gif" width="16" height="16"> ) presente solo nel caso in cui si stia compilando una regola del configuratore, permette di validare sintatticamente il contenuto del testo che si sta editando. La validazione avviene sulle basi della sintassi prevista per le regole del configuratore.
### F15 (esamina/copia)
Il tasto F15 ( icona <img src="file : [SME.ICO]\LO\LOCEDT\f15.gif" width="16" height="16"> ) permette di aprire (in lettura) sino a tre files e visualizzarli all'interno dell'editor (oppure quanti se ne vuole in finestre separate) per eventuali esigenze di confronto, copia, controllo. La finestra di servizio che si apre al richiamo del F15 permette di esprimere sia il file che si vuole aprire, sia la modalità di apertura che si vuole (in finestra o esterna).
I files che si sono aperti con la modalità F15 si chiudono con F12 ( icona <img src="file : [SME.ICO]\LO\LOCEDT\f12.gif" width="16" height="16"> ) nell'ordine inverso rispetto a come sono state aperti.
La navigazione fra un pannello e l'altro può avvenire con la combinazione di tasti **CTRL+ALT+TAB**.
### Wizard (Control+W)
Nei casi in cui l'editor stia gestendo un testo di tipo configurato (scripting di scheda, di configurazione o di documentazione) l'utente ha l'ausilio di un wizard che permette di comporre testo in maniera facilitata. Il wizard, una volta richiamato tramite **CTRL+W** mostra una finestra di input che richiede i dati per completare la specifica che si stava inserendo. Una volta riempiti i campi richiesti, tramite l'_9_OK il testo così composto verrà inserito nel testo che si sta editando.
### Preview (Control+P)
Quando l'editor sta gestendo dei file di documentazione è attiva la funzione di Preview (fra i bottoni in basso a destra oppure **CTRL+P**) che permette di avere un' anteprima del risultato visivo della documentazione che si sta componendo.
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


**(*)** :  nelle situazioni dove è previsto

## Utilizzo Shortcut stile WIKIPEDIA
In data 22/11/2006 è stata introdotta una nuova modalità di inserimento di elenchi in stile WIKI cioè usando semplici caratteri in modo da accelerare la creazione di documentazione.
Una volta che questa modalità diventerà abbastanza consolidata si provvederà ad inserire altre modalità e a uniformarle con l'editor.

### Elenchi puntati/numerati stile WIKI
Per iniziare un elenco basta  inserire a inizio riga la seguente serie di caratteri : 
' * '  (spazio-asterisco-spazio) e nome del valore del punto elenco (nel caso di elenchi puntati)
' - ' (spazio-diesis-spazio) e nome del valore del punto elenco (nel caso di elenchi numerati)

e man mano incrementare il numero di simboli se si vuole cambiare livelli. Per concludere l'elenco aggiungo uno spazio bianco.

Esempio elenco puntato : 

 ' * ' Primo punto

 ' ** ' Secondo punto con un testo molto lungo per testare i ritorni a capo ed eventuali problemi di

 ' *** ' Terzo punto

Diventa : 
 * Primo punto
 ** Secondo punto con un testo molto lungo per testare i ritorni a capo ed eventuali problemi di
 *** Terzo punto

Esempio elenco numerato : 
 ' - ' Primo punto elenco numerato

 ' -- ' Secondo punto elenco numerato

 ' - ' Terzo punto di nuovo di primo livello

Diventa : 
 - Primo punto elenco numerato
 -- Secondo punto elenco numerato
 - Terzo punto di nuovo di primo livello

### Titoli stile WIKI
I titoli hanno lo stesso comportamento degli elenchi con la differenza che si usa il simbolo di ! : 
' ! '  (spazio-punto esclamativo-spazio) e nome del titolo

Esempio : 
' ! ' Titolo livello 1

' !! ' Titolo livello 2

' !!! ' Titolo  livello 3

Diventa : 
 ! Titolo livello 1
 !! Titolo livello 2
 !! Titolo  livello 3
