# Modalità inserimento testate/righe nelle richieste di movimentazione
La struttura delle richieste di movimentazione può essere di 2 tipi : 
 * **Testata** (Key N.Testata) / **Righe** (key N.Testata + N. Riga, oppure identificativo riga)
 * solo **Righe** (key identificativo riga)

Sulle righe l'identificativo è la chiave principale, il N. testata / N. riga è una chiave multipla (ad esempio nel caso in cui una richiesta si sdoppia perchè ha delle assegnazioni in luoghi diversi).
Quando dai vari oggetti (documento / ordine produzione / impegni produzione) si esegue la funzione di assegnazione di una riga si imposta sempre la causale di testata (GMO = Tipo richiesta di movimentazione) in essa c'è, tra i vari campi, il numeratore richieste movimentazione, se esso è blank si intende che __non__ si deve creare la testata.
Vi sono infine campi che servono per la riga : 
 * l'origine documento, che stabilisce l'oggetto intestatario (cfr Impostazione chiavi GMRRIM). QWuesto campo è solo proposto, in linea di principio potrebbero esserci, sotto la stessa richiesta righe di origine diversa anche se la gestione successiva potrebbe risultare non proprio chiara
 * il tipo riga richiesta (GMZ), ch eguida l'inseirmento della riga di richiesta

Il numeratore dell'identificativo riga deve essere totalmente numerico (7.0), è fissato nella tabella GM1, dove è pure impostato il passo delle righe (nel caso ci sia la testata, se questa non esiste il campo è blank e il numero riga è 0).

Per l'inizializzazione delle testate e delle righe vi sono le routines apposite : 
 * per la testata **£GMW**, attenzione è cura del programma lanciante decidere se la testata va creata o meno, si devono impostare : 
 ** £GMOTO, il tipo testata, da tabella GMO
 ** £GMOMG, il magazzino di competenza
 ** £GMONR, il numero testata (opzionale, se blank viene creato un nuovo numero)
 * per le righe **£GMZ**, anche in questo caso bisogna impostare se è un'inizializzazione con o senza testata (funzione CLEAR/CLEARN) dal richiamo
 ** £GMZNR,
 *** nel caso di inizializzaizone con testata è il numero della testata, da cui si aggancia il tipo richiesta (GMO)
 *** nel caso di inizializzaizone senza testata è direttamente il tipo richiesta
 ** £GMZTR, tipo riga (Tab. GMZ), opzionale, se impostato vale questo, se è blank viene assunto quello impostato nella GMO.
