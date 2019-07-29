### Funzioni e metodi

- GCR Gestione carrelli.
-- CRE Crea un nuovo carrello contenente la cartella Appunti (*LAST). Se il carrello da creare esiste già, ritorna errore.
-- CPY Copia un intero carrello (= tutte le sue cartelle) in un altro. Se il carrello origine non esiste o se il carrello destinazione esiste già, ritorna errore.
-- DEL Cancella un intero carrello (= tutte le sue cartelle). Se il carrello da cancellare non esiste, ritorna errore.
-- DEC Decodifica. Verifica l'esistenza di un carrello. Se esiste ritorna tipo e codice dell'oggetto proprietario del carrello, altrimenti ritorna errore.
-- CLR Cancella tutte le cartelle di un carrello tranne la cartella Appunti. Se non trova il carrello o se contiene solo la cartella Appunti, ritorna errore.
-- MOD Modifica l'oggetto proprietario di un carrello, ossia trasferisce un carrello ad un nuovo proprietario. Se il carrello origine non esiste o se il carrello destinazione esiste già, ritorna errore.
-- ATT Attributi (SV)
-- SCA.POS Scansione - Posizionamento. Inizializza la scansione di tutti i carrelli esistenti.
-- SCA.LET  Scansione - Lettura. Ritorna in sequenza tipo e codice di tutti i carrelli esistenti. Alla fine accende l'indicatore di errore.

- GCT Gestione cartelle : 
-- CRE Crea una nuova cartella nel carrello indicato, che può anche non esistere ancora. Se la cartella da creare esiste già, ritorna errore.
-- CPY Copia contenuto e descrizione di una cartella in un'altra cartella. Se la cartella origine non esiste, ritorna errore.
Se non si impostano alcuni dei codici di destinazione (carrello o cartella), vengono assunti uguali ai codici origine. Se i codici origine e destinazione sono tutti uguali, ritorna errore.
Il carrello destinazione può essere lo stesso di origine o un altro, ed in questo caso può anche non esistere ancora.
Se la cartella destinazione non esiste viene creata, altrimenti viene modificata.
-- DEL Cancella una cartella. Se la cartella da cancellare non esiste, ritorna errore.
-- DEC Decodifica. Verifica l'esistenza di una cartella. Se esiste ritorna codice e descrizione della cartella, oltre a tipo e codice dell'oggetto proprietario del carrello. Se non esiste, ritorna errore.
-- CLR Cancella il contenuto di una cartella, ossia tutti i suoi elementi. Se la cartella da svuotare non esiste, ritorna errore.
-- MOD Modifica la descrizione di una cartella. Se la cartella non esiste, ritorna errore.
-- MOV Sposta e/o Rinomina una cartella, ossia copia contenuto e descrizione nella cartella destinazione e poi cancella la cartella origine. Se la cartella origine non esiste, ritorna errore.
Se non si impostano alcuni dei codici di destinazione (carrello o cartella), vengono assunti uguali ai codici origine. Se i codici origine e destinazione sono tutti uguali, ritorna errore.
Il carrello destinazione può essere lo stesso di origine o un altro, ed in questo caso può anche non esistere ancora.
Se la cartella destinazione non esiste viene creata, altrimenti viene modificata.
-- ATT Attributi (SV)
-- SCA.POS   Scansione - Posizionamento. Inizializza la scansione delle cartelle presenti nel carrello indicato.
-- SCA.LET   Scansione - Lettura. Ritorna in sequenza codice e descrizione di tutte le cartelle presenti nel carrello indicato. Alla fine accende l'indicatore di errore.

- GEL Gestione elementi : 
-- CRE Scrive un elemento in una cartella. Sia il carrello che la cartella possono anche non esistere, ed in tal caso vengono creati.
Se la cartella è la cartella Appunti e se contiene già un altro codice dello stesso tipo e parametro, il nuovo codice sostituisce quello precedente.
Se la cartella può contenere solo elementi di un determinato tipo-parametro e l'elemento da aggiungere non è omogeneo, ritorna errore.
Se l'elemento da aggiungere è già presente nella cartella (stesso tipo, parametro e codice), il contenuto della cartella non viene modificato, senza segnalare errore.
Se nella cartella non c'è più spazio per inserire ulteriori elementi, ritorna errore.
In tutti gli altri casi l'elemento viene aggiunto in coda a quelli presenti.
-- DEL  Cancella un elemento da una cartella. Se la cartella non esiste o se non contiene l'elemento da cancellare, ritorna errore.
-- DEC  Decodifica. Verifica l'esistenza di un elemento in una cartella. Se esiste ritorna codice e descrizione dell'elemento, oltre alla descrizione della cartella. Se non esiste, ritorna errore.
-- SCA.POS   Scansione - Posizionamento. Inizializza la scansione degli elementi presenti nella cartella indicata.
-- SCA.LET   Scansione - Lettura. Ritorna in sequenza codice e descrizione di tutti gli elementi presenti nella cartella indicata. Alla fine accende l'indicatore di errore.

### Ricerca cartelle
Qualunque sia la funzione richiesta, se il primo carattere del nome cartella è "?" o "!", al suo posto viene invece eseguita la ricerca delle cartelle presenti nel carrello indicato.
In particolare, se il nome cartella ricevuto ha un prefisso (ossia contiene un punto), vengono presentate per la scelta solo le cartelle che hanno lo stesso prefisso. Ad esempio se ricevuto "?ABC.XYZ", vengono presentate solo le cartelle il cui nome inizia con "ABC." .
Se invece il nome cartella ricevuto non contiene un prefisso vengono presentate tutte le cartelle, con e senza prefisso.
In ogni caso non è previsto il posizionamento.
