# Gestione Legami
## Obiettivo
Avere uno strumento di gestione dei legami di entità.
Per legame si intente una relazione caratterizzata da alcuni attributi.
L'applicazione realizzata consente di effettuare tutte le operazioni di gestione dei legami attraverso un unico formato video che presenta una serie di opzioni disponibili all'utente.
## Formato Guida

![C£LG01_01](http://localhost:3000/immagini/MBDOC_OGG-P_C£LEG0/CXLG01_01.png)Le opzioni sono sottomesse alle autorizzazzioni, consentendo a diversi utenti di effettuare solo le operazioni per cui sono abilitati.

## Requisiti
Per poter accedere in modo corretto alle funzioni si deve precisare quale è il TIPO LEGAME che si vuole gestire; Il TIPO LEGAME è codificato nella tabella C£U (si veda eventualmente la descrizione della tabella C£U).
Il tipo legame suddetto può anche essere precisato prima ancora di entrare nell'applicazione e, in questo caso, deve essere passato all'applicazione come parametro (CALL C£LG01G PARM('tipo legame')). Con questa possibilità la gestione sarà personalizzata in funzione di quel tipo di legame senza però poter modificarne il tipo fino al termine dell'applicazione.

## Azioni
Scelto il TIPO DOCUMENTO è possibile effettuare diverse scelte : 
 - precisare opzione, e campi presentati a video :  in questo caso, in base all'opzione scelta, si passerà, pigiando il tasto d'INVIO, direttamente al dettaglio dell'applicazione. Per immettere i vari codici è possibile passare alla fase di ricerca con i caratteri "?" o "!" oppure interrogare l'archivio (legami già immessi) con il carattere "/".
 - precisare solo l'opzione :  si passerà ad un nuovo formato che mostra una lista di legami presenti nell'archivio, ove l'utente può selezionare con una "X" il legame che vuole utilizzare; è chiaro che l'opzione di immissione '01' non potrà essere utilizzata (non si può immettere un documento già immesso).
 - precisare tutti i campi a video ma non l'opzione :  anche in questo caso si passerà ad un formato contenente la lista ma con la possibilità di inserire vicino al legame da gestire una opzione di quelle definite precedentemente.

Ulteriori possibilità per l'utente sono l'utilizzo dei tasti funzionali F03 per uscire incondizionatamente dall'applicazione, F04 per decodificare i campi immessi (per decodifica si intende un controllo dei campi immessi e una eventuale visualizzazione di descrizioni relative al codice inserito) e F13 per le parzializzazioni.

## Formato Parzializzazioni
![C£LG01_02](http://localhost:3000/immagini/MBDOC_OGG-P_C£LEG0/CXLG01_02.png)Scelto il TIPO LEGAME nel formato GUIDA è possibile entrare nelle parzializzazioni premendo F13.
Anche dalla videata nel formto LISTA è possibile accedere alle parzializzazioni sempre premendo il tasto funzionale F13.
Il tipo legame appare nel titolo della videata delle parzializzazioni; come si può notare osservando il formato video per parzializzare l'archivio è necessario precisare due elementi :  un ordinamento e almeno un codice nei campi delle parzializzazioni.
L'ordinamento precisa secondo quali campi (entità 1 o 2) deve essere ordinato l'archivio quando si passerà nel formato lista.
Una volta effettuata la parzializzazione premendo INVIO si ritornerà alla videata di partenza e apparirà evidenziata
la scritta 'F13 Parzializ.attive'.
Ricordiamo che in molti campi delle parzializzazione è prevista la ricerca in tabelle digitando il '?' o il '!'.

## Formato Lista

![C£LG01_03](http://localhost:3000/immagini/MBDOC_OGG-P_C£LEG0/CXLG01_03.png)La lista visualizza l'elenco dei legami presenti nell'archivio. Sono riportate solo le caratteristiche principali con un campo di scelta per indicare l'operazione con cui agire su quel particolare legame, entrando direttamente nel dettaglio.

### Note operative
L'utente è in grado di comprendere se tale elenco è parziale o completo in funzione dell'indicazione di 'Parzializzazioni attive' a piede del formato. Come nel formato Guida, anche dalla Lista è possibile passare alla gestione delle parzializzazioni (F13).
Nel campo disponibile nella parte sinistra superiore delle videata é possibile definire il punto di partenza (alfabetico) dell'elenco.
Nel caso in cui il Formato Guida non specifichi l'opzione le operazioni disponibili in lista sono le medesime del formato guida; viceversa l'utente può solamente interrogare un legame dell'operazione sul legame.
## Formato Dettaglio
![C£LG01_04](http://localhost:3000/immagini/MBDOC_OGG-P_C£LEG0/CXLG01_04.png)