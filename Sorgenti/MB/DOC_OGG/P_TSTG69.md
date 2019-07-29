# GESTIONE LETTERE

## OBIETTIVI
Gestire nel modo più semplice e libero la scrittura di una lettera contenente delle variabili.

## FUNZIONI/METODI
 *  DOC - Documentazione
 **  V/P - Video/Stampa (SV). Esplode a video o in stampa la documentazione delle lettere
 * INZ - Inizializzazione
 ** LET/MSK/VAR - Lettera/Maschera/Variabili. Inizializzazione per l'esecuzione della funzione RIT per il recupero delle righe che compongono la lettera (LET) delle maschere (MSK) e delle variabili (VAR)
 * RIT - Ritorno
 ** LET/MSK/VAR - Lettera/Maschera/Variabili. Preceduto dal lancio della funzione INZ permette di scandire le righe con che compongono appunto la lettera (LET) delle maschere (MSK) e delle variabili (VAR)
 * RIP - Ripresa
 ** LET/MSK - Lettera/Maschera. Dati in input i codici di riferimento della lettera permette di scrivere il default delle lettere e delle maschere nelle relative note al fine di poter modificarne a piacimento la composizione
 * CHK - Controllo maschera. Data in input una variabile controlla se questa sia una maschera
 * AZI - Azioni su note
 ** GC/IC/AC - Gestione/Interrogazione/Cancellazione. Dati in input i codici di riferimento della lettera permette di applicare le funzioni specifiche delle note
 * CAR - Caricamento codici di lettera
 ** INZ/RIT - Inizializzazione/Ritorno. Permette di scandire tutti i codici lettera.
 * REP - Ripresa riferimenti lettera. Dati in input i codici di riferimento della lettera ritorna i dati di riferimento della lettera (descrizione, contenitore note ecc.)
 * ELS - Elaborazione stringa. Data in input una stringa (£G69S1) permette di lanciarne l'analisi al fine di convertire le eventuali variabili in essa presenti, riprendendone i valori tramite l'esecuzione della routine £G69SR.

## DESCRIZIONE FUNZIONAMENTO
Tramite questa routine è in sostanza possibile modificare il layout di stampa di una serie di lettere gestite da pgm standard.

La composizione di tali lettere è definita all'interno dei pgm della £G69, ma il loro layout può essere modificato generando in sostituzione alla struttura definita come default delle apposite note.

All'interno di tale struttura sono presenti alcuni caratteri speciali che permettono di identificare le variabili gestite nella lettera : 
**_&_** ---> indica l'inizio della definizione di una variabile a posizione fissa
**§** ---> indica l'inizio della definizione di una variabile a posizione variabile
Ad essi dovrà far seguito il codice della variabile, il cui termine di definizione sarà indicato da uno spazio vuoto, a meno che per la lettera non ne sia specificata una lunghezza fissa.
Tali caratteri potranno perciò essere comunque utilizzati liberamente all'interno della lettera purchè non siano seguiti da un testo che corrisponda al codice di una variabile o di una maschera, nel qual caso è comunque sufficiente far seguire al carattere speciale i caratteri "**co**".
I codici delle variabili di base sono fissi e sono elencati anch'essi all'interno dei pgm della £G69. E' da tenere in considerazone il fatto che tali elenchi hanno valore solo documentativo e che un codice variabile diventa tale solo se viene gestito all'all'interno della routine £G69SR :  quest'ultima è la routine definita in ogni pgm di stampa tramite la quale viene determinato il valore che una variabile deve assumere.

Al concetto di variabile si affianca il concetto di maschera, questa è in sostanza una variabile composta da una o più variabili e da un'eventuale parte di testo che verrà scritta nella lettera solo se almeno una delle variabili avrà valore non nullo.
Mentre le variabili sono fisse a pgm le maschere potranno essere modificate, infatti come per il layout della lettera anche per esse è previsto un default a cui potranno essere sovrapposte delle note.

Tramite le maschere è possibile inoltre definire delle funzioni che si basano sul valore di una variabile di base. Le funzioni sono identificabili tramite il carattere **%** messo di seguito ai caratteri del codici della variabile (senza spazi). Le funzioni disponibili sono le seguenti : 
**- %OAV + tipoParametroOggetto +' : '+Codice OAV**--> permette di inserire come valore un attributo della variabile.
**- %OAD + tipoParametroOggetto +' : '+Codice OAD**--> permette di inserire come valore __la descrizionedi un attributo della variabile.

All'interno delle routine le lettere sono indentificabili tramite un codice cui sono legate inoltre una serie di informazioni di riferimento anche queste definite nei pgm della £G69 : 
  - la descrizione del codice
  - struttura di default della lettera
  - il contenitore delle eventuali note
  - la documentazione delle variabili
  - struttura di default delle maschere
  - eventuale lunghezza fissa delle variabili

E' comunque possibile far rientrare nella gestione eventuali lettere personalizzare :  è infatti possibile creare un pgm B£G69G1_X (di cui è disponibile un esempio) nel quale elencare i riferimenti delle proprie lettere.

## STRUTTURA
La £G69 è composta da 3 programmi :  B£G69G0, B£G69G1, B£G69G2.

Il B£G69G0 gestisce la documentazione delle lettere (viene richiamato quando viene utilizzata la funzione DOC) tramite esso è possibile visualizzare e gestire le lettere e le maschere ad esse associate.

Il B£G69G1 gestisce in sostanza il ritorno delle informazioni della lettera :  dalle informazioni informazioni specifiche (descrizione, contenitore note) alla righe che compongono la lettera.

Il B£G69G2 gestisce invece l'elaborazione di una riga della lettera :  tramite essa viene scannerizzato ogni singolo carattere alla ricerca delle eventuali variabili o maschere da transcodificare, i quali valori verranno recuperati tramite l'esecuzione della routine £G69SR che dovrà essere definita internamente al pgm specifico di stampa della lettera.


## SVILUPPI FUTURI
- Poter far gestire alla £G69 anche la scrittura del file di stampa.
- Implementare le funzioni disponibili.
