# Gestione Calendari

## Gestione Calendari

In Negoziando è presente una Tabella che permette la gestione dei Calendari

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Tabelle>CALB - Calendari Base

Viene presentata la maschera contenente l'elenco dei calendari presenti nel sistema e sotto i soliti tasti funzionali di Negoziando. Premere F6 per inserire un nuovo calendario ed attribuire un codice alfanumerico di 3 caratteri. Premere Invio e aggiungere una descrizione del Calendario. A questo punto è possibile indicare gli orari di apertura e chiusura delle varie giornate della settimana. Sono presenti 6 caselline perchè è possibile indicare orari di apertura/chiusura per i 3 momenti della giornata, quindi mattina, pomeriggio, sera
Viene controllata l'esattezza e la sequenzialità degli orari inseriti, se viene riscontrata un'anomalia, verrà segnalata solo in fase di generazione del calendario, bloccandone l'elaborazione.

## Gestione Anagrafica Festività

Esiste anche una tabella per la gestione delle festività

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Calendari>Gestione Anagrafica Festività

Viene presentata la maschera con i soliti tasti funzionali, premendo F6=Inserisci é possibile aggiungere una nuova festività.
E' possibile gestire diversi tipi di festività : 

 * indicando solo il Codice Festività, la Descrizione, il Giorno ed il Mese è possibile inserire una festività che cade sempre nello stesso giorno e vale ovunque, come il Natale
 * Indicando l'Anno, il Codice Festività, il Giorno ed il Mese è possibile descrivere una festività che vale solo per il periodo indicato in quel determinato giorno/mese (Es. Pasqua 2008, Pasqua 2009)
 * Indicando Nazione, Codice Festività, Giorno e Mese è possibile indicare una festività che vale solo per una specifica nazione in quel determinato giorno/mese (Es. Festa della Repubblica)
 * Indicando Negozio, Anno, Giorno e Mese è possibile indicare una festività che vale solo per uno specifico negozio in quel periodo  in quel determinato giorno/mese
 * Indicando Negozio, Giorno e Mese è possibile indicare una festività che vale solo per uno specifico negozio in quel determinato giorno/mese (Es. Festa Patronale Reggio Calabria).
Questi dati verranno letti durante la fase di generazione del calendario del negozio e, in automatico, in quella data il negozio verrà segnalato come chiuso.

## Gestione Calendari Negozi

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Calendari>Gestione Calendari Negozi

In questa maschera viene visualizzato il calendario dei vari negozi. Alla selezione della funzione vengono richiesti il codice del Negozio e una data per applicare un filtro. Se non viene specificato nessun negozio, è possibile vedere il calendario di tutti i Negozi.
Da questa maschera è possibile inserire/modificare/cancellare un record dal calendario, ma anche : 

 * F8= impostare un Periodo di Chiusura. Verranno richieste le date del periodo che si vuole impostare e, una volta data la conferma, il Motivo della Chiusura. A questo punto le giornate di chiusura verranno visualizzate in blu. L'applicazione di massa delle chiusure è comunque condizionata all'assenza di Chiusure di Cassa registrate dal punto vendita. Nel caso in cui per una o più date siano presenti Chiusure di Cassa, verrà segnalato all'utente che in tali date non verrà aggiornato lo stato di Apertura/Chiusura del punto vendita.
 * F9= impostare un Periodo di Apertura. Verranno richieste le date del periodo che si vuole impostare, i relativi orari di Apertura/Chiusura e se si tratta di un'apertura straordinaria o meno.
 * F7=Generare il Calendario. Premendo il tasto apparirà una maschera dove viene rihiesto : 
 ** Codice Negozio
 ** Calendario Base. E' il calendario che abbiamo precedentemente inserito nella Tabella CALB, ed è da questo calendario che verranno prelevati gli orari di apertura
 ** Data Inizio e Data Fine del calendario da Generare
 * F11=Eliminare il Periodo

Se per il punto vendita sono presenti le informazioni relative alla Chiusura di Cassa per una certa data, la variazione del record sarà possibile solo limitatamente agli Orari di Apertura/Chiusura, ma
non per lo Stato di Apertura/Chiusura. Un messaggio informerà l'utente del limite relativo alla modifica.


## Visualizza Incassi (vedi Capitolo Visualizza Incassi)

Il programma di visualizzazione incassi è stato modificato per mostrare in rosso e con la scritta Chiuso le celle corrispondenti alle date di chiusura. Questa opzione è disponibile solo nella visualizzazione Giornaliera. E' stata aggiunta inoltre una funzione che visualizza l'incasso per Ore di Apertura.

## Configurazione Applicativa

 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Altri Parametri
Impostare a Sì la richiesta Controllo Orario per Calendario
Una volta attivata l'impostazione, all'apertura del programma di cassa verrà controllata l'esistenza del calendario del Negozio con gli orari di apertura per la giornata.
Se non esiste il calendario per quella giornata, apparirà un pannello in cui è necessario impostare l'orario di apertura del Negozio. Impostando l'orario viene scritto un record nel calendario che verrà poi trasferito in sede con le trasmissioni.

## Gestione Trasmissioni

La tabella dei calendari base viene distribuita dalla sede verso i negozi e viceversa (viene trasmessa a tutti i negozi)
La tabella delle festività viene distribuita dalla sede verso i negozi e viceversa (viene trasmessa a tutti i negozi)
La tabella dei calendari dei negozi viene distribuita dalla sede verso i negozi e viceversa (viene trasmessa solo al negozio di corrispondenza - Al negozio arriva solo il suo calendario e non quello di altri negozi)

## Controllo Chiusure di Cassa

 :  : R03 Dal Menu>Principale>Chiusure di Cassa>Cassa>Controllo Chiusure di Cassa

Dalla procedura di Controllo delle Chiusure di Cassa è sempre possibile modificare, se necessario, lo stato di Apertura/Chiusura di un Punto Vendita.
Premere F3 per modificare lo stato : 

 * Da Negozio Aperto a Negozio Chiuso
 * Da Negozio Chiuso a Negozio Aperto

E' anche possibile indicare delle annotazioni in merito all'apertura/chiusura, analogamente a quanto avviene nella Gestione Calendari Negozi.
Premere F6 per confermare la modificare dello stato di Apertura/Chiusura del Negozio/Data selezionato.

