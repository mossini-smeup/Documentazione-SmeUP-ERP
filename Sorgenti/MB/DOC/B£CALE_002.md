# Generalità
Il modulo "CALE" permette di costruire e di gestire il calendario della disponibilità di una Risorsa in funzione della sua periodicità, in particolare da la possibilità all'utente di definire i codici orario che devono essere rispettati per quel "Tipo Risorsa".
Le funzioni a disposizione sono le seguenti : 
 * Gestione dei calendari
 ** Annuale
 ** Settimanale
 ** delle Eccezioni

e le operazioni di : 
 * Interrogazione
 * Stampa
 * Definizione della Periodicità.

I calendari a disposizione sono strutturati in modo diverso : 
 * Calendario Annuale, è suddiviso per mesi e giorni (matrice di 12 righe per 31 colonne);
 * Calendario delle Eccezioni, è di tipo mensile;
 * Calendario Settimanale, definisce i giorni lavorativi della settimana con l'aggiunta di 5 possibili giorni speciali.

![B£CALE_013](http://localhost:3000/immagini/B£CALE_002/BXCALE_013.png)
Per come è strutturato, è possibile definire un calendario di disponibilità per la singola risorsa oppure per una tipologia di risorse, evitando il meccanismo di dover ripetere più volte la definizione dello stesso per le risorse simili (con la stessa disponibilità). Nello schema di dettaglio è possibile vedere come sono collegati i calendari di base, quali tabelle sono relazionate, le risorse collegate e le funzioni disponibili.

# Impostazione dell'anno
Le informazioni necessarie per costruire il Calendario della disponibilità vengono recuperate con il metodo della risalita.
Tale criterio prevede la lettura del calendario Annuale e, se non esiste il codice orario, di quello delle Eccezioni e, se anche in questo caso non vi è un valore significativo, di quello Settimanale.
Nel Settimanale si trovano le informazioni di base, cioè il Codice Orario, il Numero di risorse disponibili, le Percentuali di utilizzo e il codice dei Giorni Speciali per la risorsa in esame.
Procedendo in questo modo, secondo lo schema della risalita, si ottiene il principio di ereditarietà delle informazioni.
Si veda lo schema seguente : 
![B£CALE_014](http://localhost:3000/immagini/B£CALE_002/BXCALE_014.png)
La proiezione del calendario Annuale (mese, giorno) fornisce il Codice Orario con la massima priorità rispetto a quello delle Eccezioni e della Settimana, nel senso che tutte le risorse fanno riferimento a tale codice.

## Il Calendario Annuale
Il calendario Annuale è formato dalla matrice che specifica per mese/giorno il Codice Orario : 

![B£CALE_015](http://localhost:3000/immagini/B£CALE_002/BXCALE_015.png)I valori accettati sono i seguenti : 
 * >F indica un giorno festivo;
 * >1, 2, 3, 4, 5 indica l'applicazione del relativo Giorno Speciale.

Un qualsiasi carattere nella colonna "DET" di dettaglio permette di visualizzare il codice orario per tutti i giorni del mese in esame.
A questo punto non resta che compilare la matrice, inserendo per ogni mese i codici validi per i giorni festivi (carattere F) oppure speciali (solo codici numerici), facendo attenzione al fatto che il codice inserito è il primo applicato a tutte le risorse aziendali.
Per comodità di compilazione si indicano solo i giorni festivi e speciali, ossia quelli con un Codice Orario diverso da quello ordinario settimanale, mentre si lasciano "blank" tutti gli altri campi.

# Impostazione della settimana
Nei dati settimanali si indica, per ogni Risorsa, il Codice Orario dei giorni standard e di quelli speciali.
Sfruttando il metodo della risalita è possibile far ereditare a un gruppo di risorse il caledario settimanale definito per una risorsa specifica di riferimento (risorsa collegata), in modo da variare soltanto il calendario della risorsa di riferimento per variare contemporaneamente il calendario di tutte le risorse appartenenti al gruppo.

## Il Calendario Settimanale
Il calendario settimanale descrive il comportamento della settimana tipica e contiene i seguenti codici : 
 * il Tipo Risorsa;
 * la Risorsa;
 * la Risorsa Collegata;
 * il Codice Orario;
 * la Percentuale del coefficiente di utilizzo;
 * la Quantità di risorse impiegate.
Inoltre è possibile definire i Giorni Speciali (max 5) le cui caratteristiche sono impostate nella tabella OLG.

**Esempio di impostazione del calendario settimanale di una risorsa**
![B£CALE_016](http://localhost:3000/immagini/B£CALE_002/BXCALE_016.png)
Nell'orario Settimanale si specificano per Tipo e Codice Risorsa i seguenti dati : 
 * Risorsa Collegata, solo se la risorsa appartiene ad un gruppo con caratteristiche simili ( in questo caso i Codici Orario si lasciano "blank" dato che le informazioni necessarie si prenderanno da quest'ultima);
 * Codice Orario, dei giorni settimanali;
 * Giorni Speciali, con relativa descrizione e codice orario (nella determinazione della disponibilità risorsa, se presenti nel calendario annuale dei giorni speciali (1, 2, 3, 4, 5), nel calendario settimanale saranno considerati i codici orari assegnati ai rispettivi giorni speciali).

# Eccezioni
Il calendario delle Eccezioni è nato per descrivere tutte quelle situazioni che non possono essere coperte dalla definizione del calendario settimanale e dell'anno con i giorni festivi e quelli speciali.
Ci si riferisce cioè a tutte quelle situazioni che non possono essere previste.
Ad esempio se si hanno i seguenti valori : 

![B£CALE_017](http://localhost:3000/immagini/B£CALE_002/BXCALE_017.png)>Esempio 1 :  dato che nel calendario annuale il codice è blank e nelle Eccezioni il codice orario è stato definito come giorno di Inventario, seguendo lo schema di risalita verrà applicato quest'ultimo.

![B£CALE_018](http://localhost:3000/immagini/B£CALE_002/BXCALE_018.png)>Esempio 2 :  in questo secondo esempio il calendario di disponibilità della risorsa riporterà il codice di manutenzione.
La gestione delle Eccezioni permette di assegnare a ogni singola risorsa un calendario specifico e univocamente legato a quest'ultima. Non solo, ma si possono definire per la coppia (Tipo Risorsa e Codice Risorsa) dei Periodi in cui valgono le Eccezioni rispetto a quanto specificato nel Calendario Annuale.

**Formato Inserimento Eccezioni per Risorsa**
![B£CALE_019](http://localhost:3000/immagini/B£CALE_002/BXCALE_019.png)
# Interrogazione
L'interrogazione permette di visualizzare graficamente la disponibilità di una risorsa in un priodo di tempo : 
![B£CALE_020](http://localhost:3000/immagini/B£CALE_002/BXCALE_020.png)
# Stampa disponibilità risorse
Consente di stampare il grafico della diponibilità della risorsa nel periodo preso in considerazione : 
![B£CALE_021](http://localhost:3000/immagini/B£CALE_002/BXCALE_021.png)
# Set'n play distribuzione quantità
In Sme.up la periodicità permette di descrivere periodi di ampiezza costante (giorni, settimane, mesi) e periodi di ampiezza variabile (n giorni + m settimane + p mesi).
Uno degli utilizzi è nella gestione del Master Production Schedule (MPS), dove i periodi hanno ampiezza variabile (giorni nel breve, settimane nel medio, mesi nel lungo termine).
Un tema conseguente è quello di poter inserire delle quantità cumulate per periodo e distribuirle nei componenti del periodo stesso (es. :  inserire quantità mensili e distribuirle nei giorni lavorativi o nelle settimane del mese).
Questo strumento permette di verificare : 
 * come vengono costruiti i periodi dati (risorsa, periodicità, periodo iniziale);
 * la distribuzione, nei vari periodi, delle quantità inserite.

![B£CALE_022](http://localhost:3000/immagini/B£CALE_002/BXCALE_022.png)
Con le opzioni di sinistra è possibile : 
 * verificare la descrizione di dettaglio del periodo (vedi esempio)
 * data una quantità settimanale o mensile inserita nel periodo, verificare la sua distribuzione nei vari periodi (vedi esempio).

![B£CALE_023](http://localhost:3000/immagini/B£CALE_002/BXCALE_023.png)
**Esempio distribuzione quantità mensile nei periodi**
![B£CALE_024](http://localhost:3000/immagini/B£CALE_002/BXCALE_024.png)
# Tabelle particolari
Le tabelle a cui fa riferimento il Calendario sono OLG, A£Q e TRG : 
 * O L G (Orario di Lavoro Giornaliero). Contiene i possibili orari definiti dall'utente secondo le proprie esigenze. Sono quindi codificati i possibili orari normali (turno normale 8-17, doppio turno, 3 turni, festivo, ecc...), ma anche le possibili eccezioni. Ogni elemento della tabella contiene, oltre alla descrizione dettagliata del singolo elemento, l'orario di inizio e di fine di ogni intervallo, che costiuisce il codice orario (sono possibili fino a 6 intervalli). Si noti che gli orari sono espressi in Centesimi e non in ore (es. :  le ore sei e mezza vengono indicate con 6,50).
 * A £ Q. la tabella in esame elenca le Periodicità disponibili che possono essere scelte, aggiunte, adattate, a seconda delle necessità aziendali. Si noti che nella tabella in esame non esiste un vincolo sul periodo :  qualunque combinazione scelta viene accettata e applicata di conseguenza.
 * T R G. questa tabella mostra l'elenco del Tipo Risorsa che dev'essere scelto con la relativa descrizione.

# Ricalcolo calendario
La funzione di Ricalcolo del calendario, utilizzata solo dallo Schedulatore PF400, nasce per risolvere i problemi di Performance del ciclo produttivo e permette di collegare il calendario con tutte le risorse appartenenti alla fase di schedulazione.
Tutte le volte che si crea un nuovo calendario, bisogna fare in modo che questo sia visto dal tipo di risorsa e per questo motivo si utilizza tale funzione.
