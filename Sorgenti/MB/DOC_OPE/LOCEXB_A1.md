# Matrice in generale

## Introduzione
Una matrice è una rappresentazione di dati in forma tabellare. E' un componente fortemente configurabile, sia in termini funzionali che di aspetto grafico.
La matrice può anche essere vista come una normale tabella dove una cella può anche rappresentare un oggetto.

Esistono sostanzialmente due tipi di matrici, differenziate dal fatto che siano dotate o meno della possibilità di aggiornare i dati in esse contenuti, infatti da qui la distinzione tra : 

- "**Matrice di visualizzazione**" :  non modificabile, rappresenta semplicemente i dati in forma tabellare.

![LOCEXB_077](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_077.png)
- "**Matrice di aggiornamento**" :  contentente uno o più campi modificabili (sono definiti dallo sviluppatore).

![LOCEXB_048](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_048.png)E' possibile vedere dall'immagine quando un campo è modificabile :  cliccando all'interno di una cella della matrice, lo sfondo di questa diventerà bianco e il testo sarà evidenziato in blu.

## Iniziare con le matrici

### Tipizzazione componente
Tipizzazione è sinonimo di oggettizzazione, ovvero, quando un campo è associato ad un oggetto applicativo si dice tipizzato od oggettizzato.
La tipizzazione è indicata mediante dei colori, in generale si utilizzano questi tre colori : 
* Bianco :  nessuna tipizzazione. Queste celle contengono descrizioni non oggettizzate. Il menù di PopUp su questa cella, quindi, consentirà solamente di copiare o incollare la cella.
* Giallo :  indica che il contenuto del campo è un oggetto Sme.UP. Le azioni possibili su questa cella dipenderanno dal tipo di oggetto contenuto. Cliccando su una cella contentente un oggetto Sme.UP è, in ogni caso, possibile accedere alla scheda dell'oggetto stesso.
* Verde :  indica che la cella contiene un valore numerico.

La tipizzazione di una matrice può essere per colonna o per cella; può essere definita a livello di cella, quando la colonna contiene oggetti eterogenei. Ogni cella, in questo caso, avrà uno specifico menù di popup. Tipicamente l'oggettizzazione è effettuata per colonna, quindi nella stessa colonna è presente sempre lo stesso Tipo/Parametro oggetto; in questo caso l'icona del tipo è presente accanto all'intestazione della colonna.

### Terminologia ed Elementi grafici
Una matrice è composta da vari elementi, quali colonne, righe, celle, testate delle colonne e altre parti opzionali. Di conseguenza, è necessario adottare un lessico comune per la totale comprensione del componente stesso.

![LOCEXB_049](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_049.png)
**Colonna**
Insieme di celle sviluppato in verticale.

**Riga**
Insieme di celle orizzontali che definisce un record.

**Intestazione colonna (o titolo)**
Definisce la tipologia della colonna, descrive il contenuto delle celle sottostanti. E' un elemento opzionale, cioè può essere visualizzato o non visualizzato.
E' composta da una cella che generalmente si presenta con sfondo grigio e al cui interno è possibile trovare l'icona del tipo oggetto contenuto nella colonna, la descrizione della colonna e un pulsante che consente di filtrare il contenuto.

**Filtro**
E' un pulsante presente all'interno dell'intestazione della colonna che permette di filtrarne il contenuto. E' un bottone opzionale, non sempre attivo.

**Zona per i raggruppamenti (opzionale)**
E' un'area grigia presente sopra l'area delle intesazioni. Se non è visualizzata basterà cliccare con il tasto destro del mouse su una qualsiasi intestazione di clonna e scegliere Raggruppamenti -> Abilita

![LOCEXB_053](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_053.png)Questa parte del componente matrice consente di raggruppare la matrice in base ai valori presenti nelle colonne. Per fare questo è sufficiente trascinare le intestazioni delle colonne in questa zona definendo in questo modo dei gruppi di record : 

![LOCEXB_054](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_054.png)
**Cella**
Le celle possono contenere testi (stringhe alfabetiche o alfanumeriche), numeri oppure oggetti SmeUP. Nel caso in cui la cella contenga un oggetto SmeUP è possibile riportare alla sua sinistra anche l'icona associata all'oggetto. La cella può anche contenere elementi grafici quali barre o diagrammi a torta.

**Zona dei setup**
All'interno di quest'area sono presenti i pulsanti identificativi delle diverse visualizzazioni, ovvero dei diversi setup impostati per la matrice. Selezionando il relativo pulsante sarà possibile attivare il setup desiderato.

**Pulsantiera**
In quest'area sono riportati tutti i pulsanti disponibii per la matrice visualizzata. I bottoni presenti possono essere generici di scheda, generici di matrice oppure specifici della singola matrice.


## Paginazione dei dati

Attraverso questa funzione è possibile caricare un numero limitato di record all'apertura di una matrice. La Paginazione è in genere attiva per matrici contenenti un numero molto elevato di record e consente di facilitarne e velocizzarne il caricamento.
Nei casi in cui sia attiva la funzionalità della paginazione, è evidenziata una barra di stato di colore rosso nella parte superiore della matrice. Questo segnala all'utente che non tutti i record che compongono la matrice sono stati caricati e visualizzati.

![LOCEXB_082](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_082.png)
La barra segnaletica rossa è visualizzata finchè non sono stati caricati tutti i record.
Per caricare e visualizzare ulteriori record è sufficiente selezionare il pulsante Page Down o digitare il pulsante 'Segue' posto ai piedi della matrice.
Attenzione :  il bottone viene visualizzato solo se il fuoco è applicato alla matrice.

![LOCEXB_081](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_081.png)
Una particolarità della paginazione, riguarda l'impostazione del limite iniziale di dati caricabili. Sostanzialmente il numero di righe caricate per ogni pagina è definito dallo sviluppatore a livello di impostazione iniziale della matrice.
Lo standard, inoltre, prevede che ogni paginazione carichi il doppio dei dati della paginazione precedente. Ovvero, se su una matrice è stato definito un caricamento iniziale di 1000 righe, paginando verrebbe caricato un numero doppio di record, e quindi altri 2000 record, alla successiva paginazione invece sarebbero 4000 e così via.

## Esportazioni

Attraverso le voci presenti all'interno del PopUp è possibile esportare i dati visualizzati in altri formati : 

![LOCEXB_062](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_062.png)
Le esportazioni disponibili sono visualizzate all'interno della voce "Visualizza come" del popup della matrice stessa. Le esportazioni disponibili sono : 

- Excel
- PDF
- Grafico
- CSV


## Popup

All'interno della matrice sono disponibili diversi popup che variano in funzione del punto in cui vengono chimati. Abbiamo infatti un popup generico di matrice, il popup di colonne, il popup di riga, ecc.
Per accedere al popup generale della matrice è sufficiente cliccare con il tasto destro del mouse sul tab della matrice o selezionare il relativo pulsante : 

![LOCEXB_093](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_093.png)
![LOCEXB_092](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_092.png)
Le funzioni disponibili per l'utente all'interno del popup della matrice sono : 
 * Aggiorna. Aggiorna l'intera sezione in cui è contenuta la matrice.
 * Ricarica dati. Ricarica i dati visualizzati all'intenro della matrice.
 * Ingrandisci. Espande a pagina intera la sezione in cui è contenuta la matrice.
 * Impostazioni. Permette di accedere alla gestione dei setup della matrice.
 * Visualizza come. Permette di esportare i dati contenuti nella matrice in diversi formati.
 * Stampa della sezione. Permette di stampare il contenuto della matrice.
 * Screenshot della sezione. Esegue uno screenshot dei dati visualizzati.

Nei capitoli successivi di questo documento verranno analizzate le funzioni disponibili all'interno degli altri popup disponibili.

## Shortcut

I tasti funzionali più significativi sulla matrice : 
 * F09 :  esplode completamente una matrice in cui siano presenti dei gruppi
 * F10 :  implode completamente una matrice in cui siano presenti dei gruppi
 * F17 :  apre il Gestore setup

I comandi rapidi sul componente sono : 
 * ALT+D :  se digitato nel momento in cui è selezionanta una riga apre il dettaglio del record
 * CTRL+F10 :  mostra le colonne nascoste della matrice
 * CTRL+F :  permette di aprire un box all'interno del quale è possibile digitare una stringa che verrà poi ricercata ed evidenziata all'interno delle celle della matrice.
 * CTRL+C :  se digitato quando sono selezionati uno o più record ne esegue la copia
 * CTRL+V :  permette di incollare righe copiate se la matrice è di aggiornamento.


## Setup

Il componente Matrice è uno dei componenti più flessibili di Looc.UP in quanto consente di modificare rapidamente e facilmente il suo aspetto e la sua visualizzazione. La gestione vera e propria del setup avviene attraverso l'utilizzo del "Gestore dei setup", il quale consente di aprire una guida in cui viene indicato il settaggio dei diversi parametri che portano l'utente alla personalizzazione della matrice.
E' possibile associare a ogni matrice più setup utente.

### Utilizzo del Gestore dei setup

E' possibile accedere al Gestore dei setup tramite il comando F17, oppure selezionando all'interno del popup di matrice 'Impostazioni >> Setup utente >> Gestione' o ancora premendo il pulsante apposito.
Il gestore dei setup si presenta in questo modo : 

![LOCEXB_064](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_064.png)
Nella parte superiore vengono elencati i setup definiti dall'utente se presenti, mentre dal pulsante delle opzioni a destra è possibile agire sui setup creandoli, modificandoli, cancellandoli, ecc. Per creare un nuovo setup è necessario selezionare l'opzione0 'Aggiunta'; così facendo si aprirà la guida per la parametrizzazione del setup : 

![LOCEXB_065](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_065.png)
Come è possibile vedere, la guida per la definizione del setup si compone di più schede :  vediamo le principali impostazioni per la creazione del setup limitandoci a considerare le caratteristiche relative all'interfaccia grafica ed escludendo le personalizzazioni tecniche. La nostra analisi si limiterà, quindi, al contenuto della prima scheda della guida.

- Mostra totali :  è possibile richiedere la visualizzazione dei totali per le colonne contenenti dei numeri. I valori possibili sono Yes/No, il valore di default è No. Se è richiesta la visualizzazione dei totali è possibile cliccare con il tasto dx sull'intestazione delle colonne contenenti valori numerici e visualizzare le 'Totalizzazioni'. Il risultato dell'operazione compare in una barra ai piedi della matrice.
- Mostra gruppi :  abilitando questo campo si crea l'area dei raggruppamenti sopra la matrice. E', quindi, possibile raggruppare la matrice per uno dei suoi campi trascinando la colonna di raggruppamento nello spazio che si è creato.
- Mostra titoli gruppi :  imposta la visualizzazione o meno dei titoli dei gruppi creati. I valori possibili sono Yes/No. Il valore di default è Yes.
- Mostra filtri :  definisce se mostrare o meno i filtri sulla matrice. I filtri sono rappresentati dalle freccette poste a lato dell'intestazione della colonna (funzionano come i filtri Excel)
- Mostra griglia :  permette di visualizzare o meno la griglia della matrice. I valori possibili sono Yes/No. Il valore di default è Yes.


![LOCEXB_073](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_073.png)

- Mostra intestazioni colonne :  permette di visualizzare o meno le intestazioni delle colonne. I valori possibili sono Yes/No. Il valore di default è Yes.



- Mostra colonna indici :  se impostato sul SI permette di inserire una colonna iniziale che riporta un numero progressivo per ogni riga :  in questo modo è possibile contare i record presenti. I valori possibili sono Yes/No. Il valore di default è No.


![LOCEXB_075](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_075.png)

- Evidenzia record corrente :  permette di evidenziare o meno il record attualmente attivo. I valori possibili sono Yes/No. Il valore di default è Yes.


![LOCEXB_078](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_078.png)

- Mostra icone :   questo attributo abilita /disabilita la visualizzazione delle icone nella matrice. I valori possibili sono Yes/No. Il valore di default è No.
- Mostra le icone di testata :  questo attributo abilita /disabilita la visualizzazione delle icone nella testata delle colonne della matrice. I valori possibili sono Yes/No. Il valore di default è No.
- Espansione iniziale :  tramite il parametro è possibile visualizzare una matrice in cui siano presenti raggruppamenti completamente aperta nel momento in cui viene aperta la sezione. I valori possibili sono Yes/No. Il valore di default è Yes.
- Fissa colonne sinistra / destra :  permette di scorrerre le colonne della matrice tenendone fisse x a dx e/o y a sinistra. Ad esempio se si vogliono tenere fisse le prime due colonne si dovrà scrivere 2 nel campo 'Fissa colonne sinistra'.  I valori possibili sono numeri. Il valore di default è non definito.
- Nome FONT :  specifica quale carattere deve essere utilizzato per visualizzare l'etichetta. Il valore è una stringa di caratteri. Cliccando sull'icona alla sinistra del campo è possibile aprire l'elenco dei font disponibili e selezionare quello desiderato.
- Colore FONT :  specifica il colore con il quale mostrare il testo dell'etichetta. Non è obbligatorio, il valore di default è nero.
- Colore sfondo :  specifica il colore dello sfondo delle celle.
- Colori righe alternate :  permette di colorare in modo alternato le righe : 


![LOCEXB_066](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_066.png)

- Dimensione FONT :  definisce la dimensione del font. Non è obbligatorio, il default segue le impostazioni del video.
- Autofit colonne :  permette di variare la larghezza delle colonne adattandola al contenuto.
- Subtotali incolonnati :  se attivo e se sono presenti dei raggruppamenti è possibile visualizzare il valore totale del gruppo sull'etichetta del gruppo stesso.


Impostati i settaggi desiderati dall'utente è possibile confermare facendo click su OK. A questo punto comparirà la schermata dei parametri del salvataggio : 

![LOCEXB_067](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A1/LOCEXB_067.png)
Nel campo 'Codice' è possibile indicare il nome desiderato per il salvataggio. Confermando apparirà nella zona sottostante la matrice un pulsante con il nome assegnato al setup. Premendo questo pulsante è possibile visualizzare la matrice con il settaggio definito. Per ritornare al settaggio di default è sufficiente cliccare sul pulsante 'Default'.

Per modificare un setup è possibile aprire il Gestore dei setup, selezionare il setup che si vuole modificare e quindi premere 'Modifica' nella pulsantiera di destra.



