## Obiettivo
La funzione premette di costruire un codice, parlante; a partire da una serie di domande a cui l'utente deve dare risposta. La domanda successiva può essere prefissata nel flusso oppure può derivare dalla risposta data alla domanda precedente. In funzione delle risposte viene costruita una matrice base (9 righe di 99 caratteri) che sarà utilizata per l'inserimento in anagrafica del codice creato e di altre caratteristiche (es. per un articolo alla fine del processo potremmo avere :  Codice, Descrizione, Classe materiale, Classe funzionale, ecc...).
Oltre alla caratterisitche interne all'archivio la funzione può guidare l'inserimento anche di altre caratteristiche esterne (parametri).

La costruzione guidata del codice inizialmente è stata sviluppata per l'anagrafico articoli e poi è stata estesa ad altri oggetti (es. Enti, Commesse,  Matricole, Ubicazioni, Colli, ....), per tutti gli oggetti in cui è prevista la costruzione del codice, la documentazione dell'archivio di riferimento (es. BRARTI0F per  gli articoli, BRENTI0F per gli enti) elenca i campi che vengono impostati partendo dalla matrice riultante.

## Descrizione del processo
 * nella tabella guida dell'oggetto (es. BRA per gli articoli, BSA per le commesse) deve essere presente il campo "Domanda costruzione codice"
 * il campo di cui sopra deve essere un elemento della tabella B£F che rimanda ad un sottosettore della tabella B£C e ad un elemento di questo sottosettore
 * l'elemento di tabella B£C (con sottosettore) richiamato rappresenta la prima domanda che il sistema presenta in fase di creazione del codice
 * la tabella B£C prevede diversi metodi / parametri per la gestione delle domande
 * la risposta alla domanda compila una matrice origine, in funzione di come la B£C è parametrizzata parti della matrice origine possono finire nella matrice di destinazione
 * l'impostazione della tabella B£C stabilisce anche se ci sarà una domanda successiva e come questa viene derivata (derivazione fissa, derivazione dalla risposta precedente)
 * alla fine del processo viene proposto il formato di gestione del dettaglio con i campi preimpostati partendo dalla matrice di destinazione

### Documentazione di dettaglio
Per le indicazioni di dettaglio far riferimento alla documentazione delle tabelle guida : 
 :  : DEC T(ST) K(B£F)
 :  : DEC T(ST) K(B£C)

### API - Funzioni costruzione/controllo stringa - B£C
 :  : INI
 :  : CMD CALL TSTB£C
 :  : FIN

## Passi da eseguire
 * Creare i passi di costruzione del codice nella tabella B£C (ogni passo costituisce un elemento della tabella)
 * Associare un flusso ai passi costruiti creando un elemento nella tabella B£F specificando all'interno di esso qual'è la domanda iniziale
 * Associare il flusso costruito alla tabella guida della tipologia dell'oggetto (es. per un articolo nella tabella BRA, campo 'Domanda cost.codice')
 * Simulare la creazione utilizzando funzione/metodo COS/PAS in TSTB£C

### Salvataggio parametri
Per salvare i parametri associati all'articolo creato, inserire un passo di flusso nella creazione dell'articolo, chiamando il pgm B£B£C10 con funzione APP.

### Inserimento descrizioni da descrizioni estese
 * Durante la costruzione del codice inserire una descrizione fittizia
 * Per calcolare le descrizioni estese dell'articolo appena creato inserire un passo di flusso nella creazione dell'articolo chiamando il pgm C£FU01X con funzione/metodo DESC/CALENT.
