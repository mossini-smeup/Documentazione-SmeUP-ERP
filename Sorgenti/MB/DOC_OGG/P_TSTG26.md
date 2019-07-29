# Interfaccia Ente / Articolo

## Gestione archivi attraverso funzione / metodo
### Funzione  :  IMP Impostazione parametri
 * _2_Metodo   :  PAR Impostazione Permette la deviazione di alcune funzioni/metodi dall'archivio BRARES0F (Dati articolo per esterno Cliente/Fornitore), agli archivi alias, listini, movimentazioni, etc.. Esiste la possibilità di memorizzare tali deviazioni d'archivio attraverso memorizzazione utente. La modalità di applicazione indicherà l'archivio su cui attingere i dati; il parametro d'applicazione, gestibile attraverso un punto esclamativo od interrogativo, indicherà una prima selezione dei dati legata all'applicazione stessa.
 * _2_Metodo   :  MDV Scelta memorizzazioni Permette la selezione delle memorizzazioni utente precedentemente memorizzate attraverso il metodo PAR.

## Gestione archivi attraverso prefisso barra su codice
Tale gestione archivi è raggiungibile anche attraverso l'inserimento di una doppia barra o barra punto interrogativo come prefisso, sia nel codice articolo che nel codice ente ( //A01  /?A01 ).
La gestione, invece, delle memorizzazioni utente (precedentemente caricate), attraverso l'inserimento del prefisso barra punto esclamativo, sempre su codice articolo od ente (/!A01).
Esiste infine, la possibilità di richiamare direttamente una memorizzazione utente, attraverso l'inserimento del prefisso barra + nome memorizzazione (sempre di un carattere per le memorizzazioni utente), sia nel codice articolo che ente (/xA01 oppure /x000001).
Ricapitolando : 
    // oppure /? Nei primi 2 caratteri del campo codice art. o ente permette la gestione archivi e la memorizzazione.
2° /!           Nei primi 2 caratteri apre la memorizzazione multipla per utente inerente la gestione archivi precedentemente caricata.
3° /x          Nei primi 2 caretteri (x indica il nome della memorizzazione) per l'esecuzione immediata.

## Funzioni / metodi Standard

N.B. :  Tutte le seguenti Funzioni e Metodi, senza nessuna precedente IMPostazione di PARametri o memorizzazioni(MDV), oppure senza nessun inserimento di prefissi barre
(//  /?  /!  /x) su codici articolo/ente, vengono elaborate sull'archivio BRARES.

### Funzione :  RES   Restituire
 * _2_Metodo : '   '  Mancante fra articolo interno/esterno.
 ** Dato il codice ente e codice articolo interno :  restituisce il codice articolo esterno (alias) .
 ** Dato il codice ente e codice articolo esterno (alias) :  restituisce il codice articolo interno.
 * _2_Metodo : 'ARI' Dato il codice ente e codice articolo esterno (alias) :  restituisce il codice articolo interno.
 * _2_Metodo : 'ARE'  Dato il codice ente e codice articolo interno :  restituisce il codice articolo esterno (alias).
 * _2_Metodo : 'DAT' Dato il codice ente e codice articolo interno :  restituisce la DS del record letto.
 * N.B. L'eventuale inesistenza del record è indicata dal messaggio d'errore BAS0013 senza accensione dell'indicatore 35.

### Funzione : 'VAL'  Validare
 * _2_Metodo  : 'ENT'  Validità articolo/ente. Dato il codice ente e codice articolo interno :  verifica l'esistenza del record.
 * N.B. L'eventuale inesistenza del record è indicata dal messaggio d'errore BAS0071 con accensione dell'indicatore 35.

### Funzione :  PRE  Presentare
 * _2_Metodo : 'ARC' Dati articolo/ente archivio Dato il codice ente e codice articolo interno :  visualizza dati contenuti in archivio (solo per BRARES).
 * _2_Metodo : 'DS'   Dati articolo/ente contenuti in DS Dato il codice ente e codice articolo interno :  visualizza dati contenuti nella DS di output.
 * N.B. L'eventuale inesistenza del record è indicata dal messaggio d'errore BAS0013 con accensione dell'indicatore 35.

### Funzione :  RIC Ricercare
 * _2_Metodo : '   '  Mancante fra articolo/ente
 ** Dato il codice ente :  entra in ricerca su lista articoli interni.
 ** Dato il codice articolo  :  entra in ricerca su lista enti.
 * _2_Metodo : 'ENT' Dato il codice articolo interno :  entra in ricerca su lista enti.
 * _2_Metodo : 'AR1' Dato il codice ente  :  entra in ricerca su lista codice articolo interno.
 * N.B.  Accensione dell'indicatore 36 di ricerca.

### Funzione :  ENP Ente preferenziale
Questa funzione fa come input un codice articolo interno ed un tipo ente.
Ritorna un ente e le informazioni dell'archivio (DS di BRARS) articolo - ente.
 * _2_Metodo  :  PR1 Ente preferenziale per articolo interno Restituisce il codice ente con maggior priorità sull'articolo.
 * _2_Metodo  :  PR2 Lista Enti preferenziali per articolo interno Entra in ricerca su lista enti preferenziali. Se scelto un ente accende l'indicatore 36 di ricerca effettuata.
 * _2_Metodo  :  PR3 Ritorno Enti prenziali per articolo interno. E' come il metodo PR2 con la differenza che invece di presentare la lista enti, li ritorna sequenzalmente. Per iniziare la scansione si deve pulire il messaggio, valorizzato a 'CONT' quando viene tornato un ente, e a 'FINE' al termine della scansione. Il modo di trattare la priorità non valorizzata, dipende da come è impostato il campo della tabella generale BR1.
 :  : DEC T(CS) P(T-BR1) K(T$BR1O) R(1)

## Funzione :  GES Gestione in lista
 * _2_Metodo : '   '  Mancante fra articolo/ente
 ** Dato il codice ente :  entra in gestione su lista articoli interni.
 ** Dato il codice articolo :  entra in gestione su lista enti.
 * _2_Metodo : 'ENT' Dato il codice articolo interno :  entra in gestione su lista enti.
 * _2_Metodo : 'AR1' Dato il codice ente :  entra in gestione su lista codice articolo interno.
