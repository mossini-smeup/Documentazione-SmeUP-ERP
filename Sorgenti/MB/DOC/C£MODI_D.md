Esistono diversi sistemi di aggancio e di lettura dei modelli dinamici e il principale, che chiameremo modulo di 'Navigazione Standard' del modello, si attiva dal modulo C£MODI dell'applicazione C£. Esso presenta come tutti i moduli diverse sezioni principali, in cui quella 'base' contiene la navigazione nel modello.

# Navigazione Standard
Si suddivide in tre sottosezioni : 
 * Modelli dinamici
 * Struttura
 * Errori

## Modelli Dinamici
Scopo di questa sezione è di consentire la navigazione base sul file.
Ogni sottosezione è riservata ad elementi strutturali del file :   scenario, contesto, tipi soggetto / oggetto e istanze.
Dall'alto a sinistra si fissano questi elementi e si esegue un'indagine diretta sul file delle relazioni.
Le frecce impostate in figura indicano il percorso dei dinamismi.

![C£MODI_032](http://localhost:3000/immagini/C£MODI_D/CXMODI_032.png)
_2_Scenari
In alto a sinistra compare l'elenco degli scenari attivi cioè utilizzati nel file C£MODI0F con qualche relazione.
Di fianco l'elenco di tutti gli scenari disponibili, fissati nell'oggetto fisso V2MDI00.

_2_Contesti
Selezionando lo scenario e seguendo il percorso tracciato dalle frecce, vengono caricati tutti i contesti utilizzati.
Il legame tra scenario e Tipo contesto è attualmente cablato su una schiera del servizio C£SER_03; nel caso dello scenario 'Applicazioni', per esempio, il tipo contesto corrispondente è la tabella TAB£A delle applicazioni. Questo indica che il contesto deve essere una applicazione.
Scenari, vincoli tra scenario e contesto e tra contesto e tipo soggetto sono attualmente cablati all'interno di programmi o oggetti fissi e non sono modificabili dall'utente.
Con l'etichetta di destra "tutti i contesti" si caricano tutti gli elementi del tipo contesto collegati allo scenario.

Selezionando il contesto vengono caricate due sottosezioni : 
 - la prima, in basso a sx, indica la data in cui è stato fatto l'ultimo caricamento del file delle relazioni rispetto al contesto selezionato;
 - la seconda, in centro, visualizza l'elenco dei tipi soggetto e dei tipi oggetto o entrambi, utilizzati rispetto a scenario e contesto selezionati.

_2_Tipo (Soggetto / Oggetto)
Nella sezione centrale si possono vedere : 
 * tutti i tipi soggetto collegati allo scenario / contesto selezionati;
 * tutti i tipi oggetto.

Con "Tipo soggetto" si intendono tutte le entità che il programma di costruzione del modello dinamico ricerca come _1_soggetto di una relazione (es. :  per un'applicazione le tabelle o gli archivi che si ritengono significativi per descrivere la customizzazione di un modello o di una implementazione), mentre con tipo oggetto si intendono tutte le entità che il programma ha trovato in relazione al soggetto e vengono definite come _1_oggetto della relazione (es. :  per l'applicazione di cui sopra, si tratta degli oggetti applicativi di Sme.up in relazione con i soggetti definiti in precedenza).

Dalla figura si evince che esistono delle relazioni aventi come soggetti elementi delle tabelle C£E e C£L. Per sapere quali sono i soggetti di tali relazioni, selezionando la tabella C£E, sulla destra compare l'elenco degli elementi usati come soggetto in qualche relazione.

_2_Istanze (Lista Soggetti/Lista Oggetti)
Selezionando nella sezione centrale un soggetto / oggetto, nella sezione di destra vengono presentate tutte le istanze del tipo selezionato con una relazione.
Il dinamismo tra sezione centrale e sezione di dx è di uno a uno, ossia la sezione "Tipo Soggetto" carica la sezione "Lista Soggetti", il "Tipo Oggetto" la "Lista Oggetti" e la sezione "Entrambi" la "Lista Ent.".

### Struttura
La sezione struttura consente di indagare sui tipi di relazioni impostate e risponde alle domande : 
 * Quali Tipi di oggetto sono in relazione tra di loro all'interno di uno scenario?
 * Esiste una relazione tra il tipo oggetto x e il tipo oggetto y nello scenario?
Ancora le frecce tracciano il percorso dei dinamismi.

![C£MODI_034](http://localhost:3000/immagini/C£MODI_D/CXMODI_034.png)
In alto a sinistra compaiono solo gli scenari attivi e, selezionandone uno, viene lanciata la ricerca di tutti i tipi soggetto utilizzati nel file delle relative relazioni.
A sua volta la scelta di un tipo soggetto attiva la ricerca di tutti i tipi oggetto in relazione col tipo soggetto selezionato.
In tal modo è facile conoscere se sussistono relazioni tra due tipologie di oggetti, anche se a questo livello non è possibile capirne il tipo (cioè il verbo che la qualifica).

### Errori
La sezione "Errori" raccoglie per ogni scenario gli errori di esistenza (in un soggetto esistono relazioni verso oggetti non più esistenti). L'individuazione di errori in relazioni può essere molto utile per rilevare rimozioni indebite di elementi.
Esistono due strumenti di indagine : 
1) Lista di Errori

![C£MODI_030](http://localhost:3000/immagini/C£MODI_D/CXMODI_030.png)
Gli errori vengono presentati in una matrice dopo aver selezionato scenario e contesto e possono essere ordinati per : 
 * _1_errore, in questa presentazione la matrice è raggruppata, in base all'origine dell'errore,per : 
 ** errore nell'_2_oggetto, vengono mostrati i valori degli elementi "oggetto" trovati in relazione con un soggetto ma che non hanno il loro corrispondente nell'archivio anagrafico o nellatabella di riferimento (es. in un soggetto :  archivio anagrafico articoli; per il quale si vogliono tracciare le relazioni con il tipo articolo potrebbe essere presente un record dove si fa riferimento ad un oggetto :  tipo articolo; XYZ che manca nella tabella BRA)
 ** errore nel _2_soggetto, vengono mostrati i valori degli elementi "soggetto" che hanno relazione con un oggetto ma che non hanno il loro corrispondente nell'archivio anagrafico o nella tabella di riferimento
 ** errore nel _2_tipo oggetto , vengono mostrati i valori degli oggetti applicativi Smeup che sono richiamati nelle relazioni con soggetti ma che non hanno il loro corrispondente nell'archivioanagrafico o nella tabella di riferimento

 * _1_soggetto, in questa presentazione la matrice è raggruppata, per tipo e descrizione del soggetto

 * _1_verbo, in questa presentazione la matrice è raggruppata, in base al verbo del soggetto : 
 ** possiede
 ** utilizza in database
 ** successivo
 ** ecc ...

2) Analisi degli Errori

![C£MODI_031](http://localhost:3000/immagini/C£MODI_D/CXMODI_031.png)Con questo strumento è possibile filtrare gli errori secondo rotture diverse (rottura per origine, tipologia soggetto / oggetto, soggetto / oggetto e verbi soggetto e oggetto).

### Tasti Funzionali
In tutte e tre le sezioni sono previsti dei bottoni visibili in basso di fianco alla barra dei comandi : 
 * _2_F9 Richiesta :  rilancia in automatico la ricostruzione o la cancellazione del modello dinamico dopo aver impostato scenario e contesto. La ricostruzione registra anche la data dell'aggiornamento in modo da tenere traccia della data dell'ultimo aggiornamento del file delle relazioni.

## Menù di Pop up
In ogni sezione e sottosezione del modulo base di navigazione è attivata sulle voci dell'albero un'estensione del menù dei popup contenente attualmente le seguenti voci : 
 * _3_Fuoco su contesto; questa azione ha effetto solo se viene selezionato il contesto ed apre la scheda del modello dinamico specifica del contesto
 * _3_Fuoco su tipo; questa azione ha effetto sul tipo soggetto o sul tipo oggetto a seconda dei casi (nota, anche se viene selezionata un'istanza il sistema presenta la scheda del tipo dell'istanza selezionata) ed apre la scheda del modello dinamico del tipo soggetto/oggetto. Questa scheda presenta una matrice dove in verticale ci sono sutte le istanze del tipo selezionato ed in orizzontale tutti i contesti attivi; l'incrocio può avere uno dei seguenti valori : 
 ** _7_Esplosione; l'istanza selezionata figura come "soggetto", cioè da questa partono delle relazioni verso altri oggetti
 ** _7_Implosione; l'istanza selezionata figura come "oggetto" cioè a questa arrivano relazioni da altri soggetti
 * _3_Fuoco su oggetto; questa azione ha effetto solo se viene selezionata una singola istanza di un soggetto o di un oggetto, si apre la scheda del modello dinamico specifica dell'oggetto

![C£MODI_033](http://localhost:3000/immagini/C£MODI_D/CXMODI_033.png)
### Scheda Fuoco su Contesto
![C£MODI_027](http://localhost:3000/immagini/C£MODI_D/CXMODI_027.png)La scheda "Fuoco su contesto" contiene una sottosezione (nel riquadro rosso) che esplode la cartella personale di Work del carrello. Essa può essere alimentata attraverso le voci di pop up del carrello. Il tasto "add" aggiunge l'elemento selezionato nella sezione soprastante all'elenco della work. Gli elementi possono anche essere aggiunti tramite Drag and Drop.
Ogni elemento della work trascinato sul Cestino viene eliminato dalla stessa.
Il tasto 'X' attiva, dopo richiesta di conferma,  la funzione di svuotamento cartella di work.
Il tasto '>>' attiva il caricamento dei dati nella sezione centrale relativi a tutti gli oggetti presenti nella cartella di Work.

### Scheda Fuoco su Tipo
![C£MODI_029](http://localhost:3000/immagini/C£MODI_D/CXMODI_029.png)
### Scheda Fuoco su Oggetto
![C£MODI_028](http://localhost:3000/immagini/C£MODI_D/CXMODI_028.png)
## Modelli Dinamici di Applicazioni
E' stata allestita per ogni singola applicazione una scheda specifica che ne esplica il modello dinamico. Dal menù delle Applicazioni, selezionandone una e portando in primo piano la scheda con etichetta 'Modelli Dinamici', si presenta una finestra di navigazione simile alla seguente : 

![C£MODI_020](http://localhost:3000/immagini/C£MODI_D/CXMODI_020.png)
Nei frame "Tipo soggetto" e "Tipo oggetto" sono contenute le tipologie di soggetto e oggetto utilizzate dal modello relativamente all'applicazione corrente (BR in figura). Selezionandone una, verranno caricate le istanze nei frame in basso. Il dinamismo quindi dall'istanza si sposta sull'elenco delle relazioni che la coinvolgono, esplose nella finestra centrale. Se si seleziona un elemento contenuto nell'albero delle relazioni, nel frame a destra vengono esplose le relazioni di quest'ultimo in un albero ricorsivo.
Sono attivati anche per questa scheda tasti funzionali per ricostruire in tempo reale il modello e i popup di accesso ai fuochi.
