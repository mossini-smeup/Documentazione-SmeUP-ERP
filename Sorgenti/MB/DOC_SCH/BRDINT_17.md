## Richiesta Parametri

* **Documenti non assegnati** :  se selezionata, vengono inclusi nella matrice : 
** Sulle emesse :  le registrazioni che non sono attribuite ad una dichiarazione, anche quando non presentano un assoggettamento 8C (è per evidenziare che ci sono stati dei casi su quel soggetto in cui non sono state applicate).
** Sulle ricevute :  come per il passivo vengono incluse le registrazioni che non sono attribuite ad una dichiarazione, ma oltre a queste vengono inclusi anche i documenti che risultano da fatturare (cioè a cui non è ancora stato attribuito un numero di fattura) ed i documenti che sono fatturati ma non contabilizzati (cioè hanno il n° di fattura ma non sono ancora finiti in contabilità)

* **Data limite iniziale** :  definisce il momento all'interno dell'anno a partire da quale voglio vedere la situazione. Questa scelta ha i seguenti effetti : 
** Vengono escluse dalla matrice le dichiarazioni che a quella data - 1 giorno, sono arrivate a residuo 0, e le dichiarazioni che hanno data sospensione inferiore a tale data
** Sulla riga che nella colonna descrizione "dichiarazione" che normalmente riporta l'importo della dichiarazione non viene riportato tale valore ma il residuo della dichiarazione a quella data -1
** Negli utilizzi attribuiti alla dichiarazione vengono riportati solo gli utilizzi che hanno data >=  a quella indicata

* **Data limite finale** :  definire il momento all'interno dell'anno al quale voglio la situazione. Vengono quindi esclusi tutti i dati aventi data superiore (che siano dichiarazioni emesse, utilizzi, registrazioni o documenti).

* **Tipo contatto** :  di per suo non ha alcun effetto, serve solo per poter indicare il campo successivo "Soggetto"

* **Soggetto** :  mi permette di filtrare l'analisi per un singolo soggetto. Ha la partita iva, vengono elaborati cmq tutti i soggetti che hanno la stessa partita iva, viceversa il singolo codice.

* **Filtro soggetti** :  mi permette di filtrare l'analisi in base alla presenza di certi elementi rilevanti. Può assumere i seguenti valori : 
** 1. Solo con segnalazioni (che siano di errore o informative, filtra i soggetti che hanno almeno una segnalazione). E' l'unica opzione sensata per le emesse. Tutte le successive hanno senso solo sulle ricevute. Dovrebbe servire per verificare se ci sono errori o situazioni da tenere sotto controllo (es. il limite che si avvicina)
** 2. Solo con note da stampare o contabilizzare. Filtra i soggetti dove è presente almeno una nota d'accredito da stampare o contabilizzare. Dovrebbe servire in fase di fatturazione per verificare se ci sono note da collegare manualmente.
** 3. Solo con documenti da stampare o contabilizzare. Filtra i soggetti dove è presente almeno un documento da stampare o contabilizzare. Dovrebbe servire per verificare le quadrature con la stampa di controllo della fatturazione (v5fa01s)
** 4. Solo con dichiarazioni per operazione. Filtra i soggetti dove è presente almeno una dichiarazione per operazione. Dovrebbe servire in fase di fatturazione per verificare se ci sono note da collegare manualmente.

## Righe

* Solo una precisazione rispetto al fatto che vengono mostrati tutti i dati rilevanti per il periodo temporale elaborato di una partita iva (o di un soggetto che non ha partita iva, vedi dogane), in cui esiste almeno una dichiarazione per operazione o per limite importo

## Colonne

*  **Op** :  opzioni, da qui ho le opzioni principali di riga. Abbiamo essenzialmente queste possibilità che variano a seconda della riga.
** **Gestione assegnazione** :  apre la schermata che permette di attribuire o annullare l'attribuzione di un documento o una registrazione ad una certa dichiarazione.
** **Annulla assegnazione** :  in modo cieco (non ci sono altre schermate) viene annullata l'assegnazione di documento o una registrazione già attribuita
** **Assegna in automatico per limite importo** :  permette di assegnare un documento in base alla situazione in essere
** **Dati documento** :  permette di analizzare la composizione del documento. Se una fattura o una nota è composta da più bolle, qui è se ne vede l'elenco.
** **Controllo assoggettamenti pre-dichiarazione** :  permette di vedere quali erano gli assoggettamenti presenti sul documento prima dell'applicazione della dichiarazione. Se l'assegnazione viene annullata, gli assoggettamenti che vengono qui indicati, verranno ripristinati.
** Sulla riga della dichiarazione abbiamo poi tutte le azioni di gestione della dichiarazione.
* Non hanno opzioni : 
** Le righe che corrispondono a registrazioni di ciclo attivo. Le registrazioni di ciclo attivo contabilizzate non si possono più toccare. E' necessario scontabilizzarle per poter di nuovo operare in base ai riferimenti dei documenti.
** Le righe che corrispondono a registrazioni di ciclo passivo senza l'assoggettamento 8C. Se su una fattura di un fornitore non c'è l'assoggettamento 8C e questa fattura viene registrata non posso fare nulla su questa registrazione dal punto di vista delle dichiarazioni di intento.
* Al netto di questo nulla toglie che si può andare sulla colonna della registrazione o del documento e da li con tasto destro, gestire la registrazione o il documento.

*  **Descrizione** :  indica il significato della riga. Questi i valori possibili : 
** **Dichiarazione** :  identifica la dichiarazione inserita.
** **Documento da contabilizzare assegnato** :  indica un documento di ciclo attivo stampato, ma non contabilizzato, assegnato da una certa dichiarazione
** **Documento da stampare assegnato** :  indica un documento di ciclo attivo stampato, ma non contabilizzato, assegnato da una certa dichiarazione (prima di essere stampati in questo stato dovrebbero esserci le note di accredito e le bolle attribuire ad una dichiarazione per operazione)
** **Documento contabilizzato** :  indica un documento di ciclo attivo contabilizzato, che non è stato attribuito ad alcuna dichiarazione
** **Documento da contabilizzare non assegnato** :  indica un documento di ciclo attivo stampato, ma non contabilizzato, che non è stato attribuito ad alcuna dichiarazione
** **Registrazione non assegnabile** :  registrazione di ciclo passivo che non presenta alcun imponibile in 8C
** **Registrazione assegnata** :   registrazione di ciclo passivo assegnata ad una certa dichiarazione
** **Registrazione non assegnata** :  registrazione di ciclo passivo che avendo imponibile in 8C, non è stata attribuita ad alcuna dichiarazione
** **Residuo** :  la riga di residuo di una certa dichiarazione
** **Totale non assegnato** :  è il totale dei documenti e/o registrazioni di una certa partita iva o un certo soggetto che non sono stati assegnati ad alcuna dichiarazione.

*  **Data utilizzo** :  coincide con la data rilevante per la riga. Varia a seconda del campo descrizione : 
** Dichiarazione :  non valorizzata
** Documento :  se presente la data della bolla è la data della bolla, se non c'è la data della bolla, ma c'è la data fattura viene presa questa, se sono assenti entrambe viene presa la data limite finale dell'interrogazione.
** Registrazione :  corrisponde alla data operazione della fattura
** Residuo :  non valorizzata
** Totale non assegnato :  non valorizzata

* **Importo** :  Varia a seconda del campo descrizione : 
** Dichiarazione :  se non c'è una data limite iniziale è l'importo indicato sulla dichiarazione. Viceversa indica il residuo iniziale a quella data.
** Registrazione :  se c'è l'imponibile 8C, corrisponde a tale valore, viceversa all'imponibile con iva (cioè l'imponibile che si sarebbe potuto utilizzare, ma non è stato utilizzato)
** Documento :  se è assegnato è l'imponibile 8C, viceversa è dato dalla sommatoria di imponibile 8C e imponibile con iva (entrambi sono potenzialmente assegnabili ad una dichiarazione)
** Residuo :  è il residuo di una certa dichiarazione
** Totale non assegnato :  è il totale dei documenti e/o registrazioni di una certa partita iva o un certo soggetto che non sono stati assegnati ad alcuna dichiarazione.

* **% Utilizzo** :  presente solo sulla riga con descrizione residuo, indica la % di utilizzo che è stata fatta di una certa dichiarazione

* **N° fattura** :  si spiega da solo

* **Imponibile totale** :  data una riga di registrazione o di documento è il totale imponibile di quella registrazione/documento. Che sia 8C, Esente o con iva.

* **Imposta totale** :  data una riga di registrazione o di documento è il totale imposta di quella registrazione/documento.

* **Totale documento** :  data una riga di registrazione o di documento è il valore di quella registrazione/documento.

* **Tipo contatto** :  è il tipo contatto di contabilizzazione di un registrazione/documento o nel caso della dichiarazione quello utilizzato per inserire la dichiarazione.

* **Codice contatto** :  è il codice contatto di contabilizzazione di un registrazione/documento o nel caso della dichiarazione quello utilizzato per inserire la dichiarazione.

* **Ragione sociale** :  è la ragione sociale del precedente codice contatto

* **Registrazione contabile** :   si spiega da solo

* **Tipo e  numero documento di riferimento** :  è la testata di documento che fa da riferimento. Nota bene :  se non è flaggato il campo "singola testata" significa che in realtà il documento è composto da più documenti raggruppati in un'unica fattura. L'elenco di tali documenti è visibile ad esempio nella schermata di "gestione assegnazione"

* **Segnalazioni** :  segnalazioni di varia natura. Posso assumere tre colorazioni i diversi messaggi, qui elencati : 
** **Importo utilizzo <> importo origine** :  significa che l'imponibile 8c che risulta sulla registrazione o il documento d'origine non coincide + con l'imponibile 8c che risulta utilizzato in una dichiarazione. E' un errore che va compreso e sanato (es. annullando e riattribuendo la registrazione/documento se è corretto che l'imponibile sia cambiato).
** **Presente assoggettamento senza iva non associato a dichiarazione** :  significa che sul documento o sulla registrazione è stato utilizzato l'assoggettamento 8C ma che questo non è stato attribuito ad alcuna dichiarazione. E' una posizione che va sanata attribuendo la corretta dichiarazione.
** **Percentuale utilizzo > xxx %** :   presente solo sullo sulla riga di residuo evidenzia con colori sempre più accesi l'avvicinarsi della % di utilizzo al 100% se sfonda il 100% viene evidenziata in rosso vivo.
** **Percentuale utilizzo 100 %** :  presente solo sullo sulla riga di residuo evidenzia il raggiungimento del 100%.
* Nei primai due casi non viene colorata solo la cella segnalazioni, ma l'intera riga.

* **Singola testata** :  su una riga di documento evidenzia il fatto che la fattura è composta da una singola testata.

* **Applicazione parziale** :  su una riga di documento evidenzia il fatto che l'8C è stato applicato in maniera parziale e non sull'intero documento.
