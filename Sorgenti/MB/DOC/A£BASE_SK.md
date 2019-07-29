# LA MAILING LIST DELLE NEWS
Esistono tre mailing list, tutte gestite tramite sottosettori della tabella XNW presente solo sull'ambiente gestionale : 
 * L1 = Lista distribuzione NEWS (Partner e Clienti)
 * L2 = Lista distribuzione Note Tecniche Interne (Partner)
 * L9 = Lista distribuzione Spot

# A NEWS OR A NTI ? THAT IS THE QUESTION
Il primo problema (amletico) che si presenta è : 
**DECIDERE SE QUELLO CHE SI STA PER SCRIVERE E' UNA NEWS O UNA NTI.**
Posto che la comuncazione non è un difetto, e quindi è meglio una NEWS in più che una in meno, di seguito diamo le regole per cui una comunicazione è una NTI.

Una NTI è : 
 * La correzione di un errore nostro, che evidentemente non è opportuno abbia eccessiva pubblicità (in quanto implicitamente si comunicherebbe l'errore). Se l'errore non è nostro (ad esempio un problema di Sistema Operativo) di cui diamo la soluzione, è invece una NEWS. Anche il cambiamento di comportamento di un componente tecnico è una NEWS.
 * Una comuncazione interna (apertura progetti, loro stato di avanzamento) che ai clienti non interessa, sia per non "ingolfarli", sia per non impegnarci (un progetto potrebbe non arrivare alla conclusione). Quello che non risponde a queste regole è una NEWS. Non farsi scrupolo di comunicare all'esterno informazioni troppo tecniche :  tener presente che esiste un buon numero di clienti che crea programmi e schede, per cui è interessato ad implementi (o cambiamenti) tecnici.


# SCRIVERE UNA NEWS
Per effettuare una news di una modifica bisogna seguire i seguenti passi : 
* Collegarsi in 5250 all'ambiente opportuno
![A£BASE_031](http://localhost:3000/immagini/A£BASE_SK/AXBASE_031.png) * Per aggiungere una nuova news, inserire 01 nel campo "Opzioni"
 * Inserire il "Tipo Rapp. Segnalazione" : 
 ** NWS viene usato per news inviate anche ai clienti
 ** NTI solo per i collaboratori.
 * Compilare i campi relativi all'immissione : 
 ** Stato :  compilato automaticamente con 00 per l'immissione della news in stato rilasciabile :  se non si desidera rilasciarla (ad esempio perchè la sua  compilazione è in corso) , lo si imposta a 95 :  in questo caso non viene vista da chi rilascia le news.

Le news non vengono automaticamente inviate ai destinatari, ma valutate prima del rilascio.
 * Data di emissione  :  compilata automaticamente
 ** Tema  :  indica la tipologia di news : 
 *** APP utilizzato per news di carattere generale inviate anche a personale non tecnico
 *** TEC utilizzato per news inviate solo a personale tecnico
 ** Modulo  :  indica l'applicazione a cui l'oggetto della news appartiene
 ** Rilascio  :  indica la versione corrente di Sme.Up
 ** Autore  :  inserire l'autore della news, secondo il formato iniziale del nome, spazio, cognome :  esempio "F. Rossi"
 ** Titolo  :  titolo della news (cercare di sintetizzarlo in modo che sia falcilmente individuabile nelle liste e nei titoli delle Email
 ** Testo  :  indica l'operazione da eseguire per inserire la descrizione della news :  GC seguito da Invio apre l'editor in cui inserire la descrizione della news.

Concluso l'inserimento della descrizione, F06 per confermare. Una volta che tutti i campi sono stati inseriti, premere F06 per confermare e immettere la news per l'accettazione.

# COMPILAZIONE DEL TESTO
Si consiglia di essere formali :  usare come soggetto sempre la terza persona singolare neutra :  non scrivere, ad esempio, "Ho realizzato, abbiamo realizzato" ma "E' stato realizzato".

Non scrivere mai date generiche ("oggi") ma specificare espilcitamente la data.

All'inizio far capire bene in poche parole il contenuto dell'intervento (specie in una News, in quanto è una novità e non una correzione).

Segnalare sempre tutti gli oggetti coinvolti nella news, dividendoli in : 
 * oggetti nuovi
 * oggetti modificati
 * oggetti solo ricompliati
separati per programmi, schede, tabelle, ecc....

Se la news fa riferimento ad una **PTF**, essa va citata in testa alla news; la lista degi oggetti coinvonti va riportata solo nella PTF, che deve contenere la descrizione estesa dell'intervento eseguito.
In questo caso è sufficiente che la news riporti una breve descrizione che dia comunque un'idea della modifica.

Da un punto di vista della formattazione va tenuto presente che l'HTML (mail e archivio) tratta gli spazi con larghezza diversa da quella del 5250, è quindi sbagliato incolonnare il testo della news come appare nel 5250. Per vedere l'effetto finale, è possibile portare temporanemente lo stato a '10' :  a questo punto la news è già visibile nella lista news nel formato finale. E' possibile vedere l'effetto in tempo reale :  una modifica nelle note, appena memorizzata (con F10) viene recepita nel dettaglio della lista news al primo refresh (F05).

Le parole non devono essere suddivise, ma si deve andare a capo con l'intera parola.

Mettere le virgole :  non si deve leggere in apnea!!!

Si consiglia di spaziare i paragrafi, per motivi di leggibilità, con righe vuote.
A questo proposito va tenuto presente che le righe vuote vengono mantenute nell'HTML solo se è presente il carattere * nella colonna 'F' all'estrema destra della riga. Per inserire una riga di questo tipo, è sufficiente inserire il carattere * nell'opzione della riga che si vuole riportare come vuota.
