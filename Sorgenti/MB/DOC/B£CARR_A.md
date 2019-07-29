# Obiettivo
Il carrello è uno strumento applicativo che consente di gestire raggruppamenti di oggetti e funzioni e le loro reciproche interazioni.
Nato dall'esigenza iniziale di gestire dei "Preferiti" in LoocUp esso ne estende enormemente le potenzialità perchè può essere infatti "ancorato" non solo al proprio utente (istanze di TAB£U) ma ad una qualunque istanza di un qualunque oggetto che ne diventa il suo possessore (Owner) e con cui si identifica univocamente. Ogni istanza dunque può agganciare un proprio carrello...

![B£CARR_001](http://localhost:3000/immagini/B£CARR_A/BXCARR_001.png)
E' possibile in questo modo per esempio associare : 
 * Ad un cliente l'elenco degli articoli preferenziali da lui richiesti o l'elenco degli agenti che ne gestiscono i contatti
 * Ad un fornitore l'elenco dei clienti che rifornisce
 * Ad un magazzino i folder relativi agli operatori e alle loro qualifiche
 * Ad un archivio l'elenco degli utenti ai quali è consentita la modifica dei dati
 * Ad un ordine di workflow l'elenco delle persone abilitate all'avanzamento dell'ordine, ecc...

In breve, esso risulta utile ogni qualvolta si ha l'esigenza di associare ad un oggetto liste di oggetti e funzioni.

# Carrello e Looc.up
Le funzioni del carrello sono attive e disponibili anche senza Looc.up., ma si tenga conto che sono state pensate per la presenza di tale applicazione, in quanto sfruttano le funzioni di navigazione, di Drag&Drop e di Popup e inoltre in Looc.up resta attiva la gestione "carrello preferiti".
Le due gestioni hanno alcune similitudini, ma i preferiti sono e resteranno solo del CLIENT e senza estensioni nell'organizzazione delle cartelle stesse.

# Definizioni
 * Cartella :  Insieme di oggetti. Ad esempio : 
 ** Tutti gli agenti che partecipano ad una convention
 ** I clienti da sollecitare.
 ** Una mailing list.
 ** Tutte le funzioni da eseguire a fine mese.
 ** Le schede più importanti.
 * Cartella omogenea :  Cartella contenente solo oggetti dello stesso tipo. Ad esempio solo clienti o solo articoli ecc. Il suo nome deve essere preceduto dal tipo oggetto.
 * Cartella eterogenea : Cartella che contiene oggetti di tipo diverso. Ad esempio un cliente, 10 articoli, un documento ecc.
 * Carrello :  Insieme di cartelle associate ad un oggetto proprietario. Ad esempio
 ** Un utente
 ** Un cliente (le cartelle potrebbero essere KIT di articoli di vendita abituale)
 * Carrello utente (Preferiti) :  Il carrello che ha come proprietario l'utente che sta eseguendo l'applicazione.

# Convenzioni
 * Un carrello ha un proprietario (un qualsiasi oggetto). Ne consegue che una proprietà di un qualsiasi oggetto è quella di possedere un carrello.
 * Un carrello contiene una o più cartelle
 * Una cartella contiene oggetti
 * In una cartella si inseriscono i singoli elementi (non riferimenti virtuali)
 * Gli elementi sono memorizzati in B£MEDE quindi le istanze sono al massimo quelle contenute in 30.000 caratteri
 * La cartella è identificata da un IDOJ, quindi in prospettiva potrà diventare un oggetto.
