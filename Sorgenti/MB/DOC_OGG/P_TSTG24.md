# Gestione movimenti di magazzino
# Obiettivo
Eseguire movimenti di magazzino e ricalcolare la relativa giacenza
# Funzioni

- _2_INZ Inizializzazione. Si possono eseguire tre diversi tipi di inizializzazione : 
-- _3_RECRecord
L'inizializzazione di tipo REC esegue l'interfaccia articoli, riprende data/ora del giorno e completa i seguenti campi nel caso in cui non siano valorizzati :  Descrizione articolo, UM interna, Data registrazione, Data/Utente Inserimento, Data/Utente aggiornmanto, Magazzino(se gestione monomagazzino).
Ritorna Errore se non va a buon fine l'interfaccia articolo.
-- _3_TRA Transazione
L'inizializzazione di tipo TRA incrementa il numero transazione M§NRTR all'interno dello stesso lotto di transazioni M§BATC. Esegue poi l'inizializzazione REC
-- _3_LOT Lotto
L'inizializzazione di tipo LOT incrementa da numeratore CRNGM/NRTR con controllo nel file GMTRAN il lotto di transazione M§BATC. Esegue poi ripettivamente le inizializzazioni TRA e REC.
Ritorna Errore se non va a buon fine la ripresa del numeratore.
In ogni caso l'inizializzazione non pulisce il record GMTRAN ma si limita a completare i campi di cui sopra.
- _2_VER Verifica
  Si possono eseguire due diversi tipi di verfica;
-- _3_REC Record
Esegue l'interfaccia articoli e ritorna errore se non va a buon fine la lettura dell'interfaccia o se l'articolo è stato definito da NON movimentare a magazzino
-- _3_ERP Record pendenti
Non Gestita
- _2_SCR Scrittura record
Esegue le seguenti funzioni
-- _3_INZLOT  Inizializzazione lotto
-- _3_INZTRA  Inizializzazione transazione
-- _3_INZREC  Inizializzazione record
-- _3_VERREC Verfica record
-
Se l'articolo è da movimentare a magazzino scrive il GMTRAN _1_ATTENZIONE :  Scrive in GMTRAN anche se l'articolo NON esiste.
- _2_APP Applicazione transazioni
  Si possono eseguire quattro diveri tipi di applicazioni : 
-- _2_ALL Tutto
    Legge tutto quello che è presente nel file GMTRAN e esegue i movimenti
-- _2_LOT Lotto
Legge tutto quello che nel GMTRAN è identificato con lo stesso lotto M§BATC e esegue i movienti
-- _2_LOTB Lotto Barch
Esegue il tipo LOT ma in modo batch
-- _2_TRA Transazione
Legge tutto quello che nel GMTRAN è identificato con lo stesso lotto M§BATC e lo stesso numero di transazione M§NRTR e esegue i movimenti
_1_Esecuzione movimenti
Legge i records del GMTRAN filtrati come sopra. Per ogni record esegue il programma di applicazione movimento (GMMOVI, GMMOAR e GMQUAN). Se l'esito è andato buon fine cancella il GMTRAN altrimenti ritorna il codice di errore con relativo messaggio. Se e solo se non è stato riscontrato alcun errore esegue una seconda volta la lettura del GMTRAN con la stessa logica di cui sopra per comprendere tutti quei records che sono stati aggiunti da eventuali programmi di aggiustamento collegati alle causali. Poichè nel processo possono essere letti diversi records del GMTRAN se l'esito del processo è senza errori viene restituito il primo GMTRAN letto, se l'esito è negativo viene restituito l'ultimo messaggio di errore trovato.
_1_ATTENZIONE :  Se durante il processo in cui ci sono molti GMTRAN anche una sola delle applicazioni movimenti non va a buon fine, il processo comunque continua per tutti i restanti record ma viene restutito il codice di errore. Inolte non viene eseguito il secondo giro che comprende eventuali GMTRAN da programmi di aggiustamento causale.
Prestare pertanto particolare attenzione quando si vogliono eseguire azioni post-applicazione su un singolo movimento controllate dall'esito.  Se si esegue un processo che comprende più movimenti contemporaneamente, come esmpio LOT, o non si specifica univocamente la transazione M§BARC + M§NRTR il codice di errore di un solo movimento produce l'effetto di non eseguire alcuna azione post nonostante all'interno del processo ci siano movimenti andati a buon fine.
- _2_SEA Scrittura e appricazione
Esegue la funzione SCR.  Se andata a buon fine esegue poi la funzione APP. Si possono eseguire quattro diveri tipi di transazioni che corrispondono a quella della funzione APP.
_1_ATTENZIONE la funzione SCR scrive il GMQUAN anche se l'articolo NON esiste. Poi però non viene eseguita la funzione APP.
- _2_AGG Aggiornamento record
Non Gestita

