# Generalità
In un sistema informativo è necessario poter gestire oltre alle informazioni codificate (es. articoli, distinte, righe ordine, ecc.) anche delle informazioni non codificate o di natura testuale (note, riferimenti a documenti esterni, commenti, ecc..) che non sono codificabili ma possono essere ricondotte ad uno o più oggetti applicativi gestiti nel sistema (es. note di un ordine, note di un cliente, ecc...).
In Sme.up esiste uno strumento comune per la gestione delle note che può essere collegato ad un oggetto qualsiasi.

# Struttura
Le note sono organizzate in contenitori e capitoli : 

- Contenitore; definito nella tabella NSC, descrive a quale oggetto il tipo di nota è associato, e se la nota si può sviluppare in più capitoli oppure se è costituita da un solo capitolo.
- Capitoli; le note associate ad un oggetto potrebbero essere di natura varia (note tecniche, note commerciali, note destinate alla produzione, note da stampare in fattura, ecc...). Ciascuna di queste potrebbe avere caratteristiche diverse, le caratteristiche di ciascun capitolo sono definite in un elemento di un sottosettore della tabella NSI richiamato dal contenitore.

![B£_07_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£AMC0/BX_07_01.png)
# Gestione
Se, in fase di customizzazione, ad un oggetto è stata associata la gestione delle note questa può essere attivata direttamente dai formati di gestione dei vari oggetti.

Se ad un oggetto sono collegati più capitoli viene chiesto di selezionare il capitolo su cui agire : 

![B£_07_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£AMC0/BX_07_02.png)
Se non sono state previste impostazioni particolari (es. programmi specifici di gestione o di controllo) tutte le note hanno lo stesso formato di gestione : 

![B£_07_03](http://localhost:3000/immagini/MBDOC_OGG-P_B£AMC0/BX_07_03.png)
## Funzioni Disponibili
Il formato di input è diviso in 3 parti : 
1.Colonna di sinistra; contiene il campo dove inserire le opzioni di editazione delle righe
2.Colonna centrale; dove scrivere fisicamente le note testuali
3.Colonna di destra; per utilizzare un flag di condizionamento riga

Le 3 colonne possono essere attivate/disattivate attraverso i tasti F17 F18 F19.

### Copia/Cancellazione/Inserimento
Per la creazione e la modifica di un testo sono a disposizione le funzioni di base di un editor di testi.
Nella colonna 'Opzioni' possiamo : 

- C/ CC copiare una singola riga o un blocco di righe
- P prima
- A dopo
- E/EE cancellare una singola riga o un blocco di righe
- IN inserire n righe


### Gestione appunti

- preparazione appunti :  nel programma di gestione delle informazioni si definisce un contenitore per gli appunti e per uno specifico capitolo  si inseriscono gli appunti di utilizzo frequente
- ripresa da appunti :  immettendo R sulla riga comandi delle note si possono riprendere gli appuntio dallo specifico contenitore degli appunti oppure dalle note in archivio di un oggetto.

### Gestione con programma specifico
Mettendo una "G" sulla riga comandi è possibile attivare un  programma specifico di gestione dellariga come descritto nella tabella NSI, che può ad esempio controllare l'immissione del testo sulla riga.

### Condizionamenti riga
Nella colonna di destra impostando opportunamente il flag di condizionamento si può decidere ad esempio dove (in quale documento cartaceo) far stampare la riga,

![B£_07_04](http://localhost:3000/immagini/MBDOC_OGG-P_B£AMC0/BX_07_04.png)
Questa funzionalità può essere anche usata in alternativa alla suddivisione in capitoli delle note(in questo caso le varie note saranno fisicamente scritte in un unico capitolo generico in cui il flag di destra decide se e dove stampare la riga).

# Funzione generalizzata di gestione note
Per la gestione note si può anche utilizzare la seguente funzione generalizzata : 

![B£_NOTE_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£AMC0/BX_NOTE_01.png)
da cui poi si passa alla gestione di dettaglio come visto in precedenza

# Annotazioni aggiuntive
Il gestore note dovrà poter essere richiamato : 
 * direttamente da un utente abilitato mediante una chiave di menu'
 * dal formato di manutenzione stessa mediante un comando potremo passare al gestore.

Per facilitare la stampa saranno costruite alcune routine richiamabili facilmente il modo parametrico e che gestiscono direttamente le emissioni. In tal modo quando si produce ad esempio il documento di stampa ciclo sarà possibile richiamare una routine in modo parametrico e avremo incorporata nella stampa il dettaglio delle note, con o senza intestazioni. La funzione di stampa potrà in particolare essere richiamata dall'esterno per stampare ad esempio tutte le note presenti in un contenitore per uno o per più tipi di informazione.

# Esempio
Si supponga di voler descrivere le attrezzature necessarie in un centro di lavoro per un articolo. Per l'attrezzatura vogliamo inserire il codice, una breve descrizione e tre valori numerici che possono essere caratteristici dell'attrezzatura (esempio temperatura di riscaldamento ecc.)
 * Decidiamo di utilizzare l'archivio DATI CENTRI DI LAVORO.
 * Descriviamo un tipo contenitore che chiamiamo ACL dove descriviamo che la prima chiave è "RI" (Risorsa) e la
seconda è "AR" (Articolo).
 * Descriviamo il tipo di informazione "IAT" (Informazioni attrezzi) con INTESTAZIONE : 
>Codice    Descrizione   Val.1   Val.2   Val.3

A questo punto è attiva una struttura che, dati contenitore e tipo informazione, mi richiede i due oggetti necessari (articolo e centro) gestendo tutte le funzioni di controllo e ricerca standard e permette l'associazione delle informazioni in modo semplice.

# Tabelle collegate
## NSC Contenitori Note
 :  : DEC T(ST) K(NSC)
## NSA Note strutturate - Archivi/Cartelle
 :  : DEC T(ST) K(NSA)
## NSI Tipo informazioni
 :  : DEC T(ST) K(NSI)
