# Generalità
In Sme.up abbiamo raggruppato tutte le possibili modalità di interrogazione di un documento in un'unica funzione generale da cui si possono lanciare diverse interrogazioni specifiche con diverse modalità di accesso.
	
# Formato iniziale
Come per la gestione anche l'interrogazione ha modalità comuni a tutti i tipi documento con piccole particolarità dovute alle varie implementazioni.

Per comodità di esposizione presenteremo l'interrogazione di ordini di vendita, da questa sarà possibile estrapolare il parallelo con la gestione degli altri documenti.

Le varie interrogazioni partono dal seguente formato iniziale : 

![V5_03_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_01.png)
La scelta guida le varie modalità di interrogazione : 

- _1_Documento, permette l'interrogazione a partire dalla testata di un documento
- _1_Righe documento, permette l'interrogazione dei dati legati ad una riga documento
- _1_Magazzino articolo, per interrogare i documenti riferiti ad un articolo in un plant (magazzino). _7_Nota, il magazzino è significativo solo se è attiva la gestione multiplant  (Tabella M51).
- _1_Ente, per interrogare i documenti intestati ad un ente
- _1_Navigazione, è l'interrogazione più ricca di funzionalità aggiuntive e di capacità di adattamento alle esigenze specifiche dell'utente.

	
# Interrogazione per documento

![V5_03_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_02.png)
Dato un documento sono possibili le seguenti funzioni : 
## Funzioni
Apre la finestra delle funzioni oggetto del documento : 

![V5_03_03](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_03.png)## Dettaglio testata
Apre l'interrogazione di dettaglio della testata : 

![V5_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_01_01.png)
## Valori documento
Presenta su una finestra i valori complessivi del documento (quantità nelle unità di misura interna ed esterna, importi in valuta corrente o del documento o alternativa, ecc.) : 

![V5_03_05](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_05.png)
## Elenco righe
Presenta la lista delle righe del documento nella forma standard di visualizzazione usata dall'utente nella gestione documenti : 

![V5_03_06](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_06.png)
_2_Nota; con il tasto F17 si possono modificare le impostazioni di visualizzazione della lista righe
## Elenco righe in forma estesa
Presenta le righe del documento con la possibilità, attraverso il tasto F13, di modificare la formapresentata (cambio dello schema campi, presentazione anche dei movimenti e/o delle note se esistenti) : 

![V5_03_07](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_07.png)
## Sintesi conti spese tasse
È la stessa interrogazione già illustrata nel documento V5DOCU Gestione documenti V5.
## Movimenti di magazzino
Presenta i movimenti collegati al documento in esame.
## Packing list
Se attiva la gestione delle packing list per ordine.
## Sintesi packing list
Lista pesi e dimensioni : 

![V5_03_08](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_08.png)
	
# Interrogazione per righe documento
Data una riga documento sono possibili molte funzioni di cui una parte sono già note, e non saranno spiegate nel dettaglio; tratteremo in particolare le seguenti funzioni : 

- _1_Distinta del documento, si applica nel caso di conto lavoro pieno ed è la distinta associata alla riga documento, la distinta può essere fisicamente memorizzata oppure derivata dinamicamente dalla distinta di produzione dell'articolo nella riga documento (se impostato il riepilogo la lista di distinta visualizzata è sommarizzata a livello articolo)

- _1_Distinta memorizzata, vedi sopra

- _1_Dettaglio impegni, materiali richiesti

- _1_Ordine produzione origine, se la riga documento relativa al conto lavoro di fase è la visualizzazione della testata ordine produzione da cui deriva

- _1_Spedizioni collegate, sono le spedizioni di invio materiali in conto lavoro collegate a questa riga documento (_2_Nota, la funzione 5 visualizza le righe derivate cioè le righe di consegna sul conto lavoro, mentre la funzione 9 visualizza le righe di spedizione)

- _1_Analisi copertura impegni, verifica in base ad un gruppo fonti definito (vedi documenti pianificazione MRP) se il fornitore ha già il materiale richiesto per soddisfare il conto lavoro oppure se e quanto ne manca.

- _1_Richieste di acquisto, se la riga ordine deriva da una richiesta di acquisto questa viene visualizzata.

	
# Interrogazione per articolo
Questa è una interrogazione tipicamente statistica che per un articolo, se richiesta la sintesi righe, presenta una finestra di sintesi con i totali ordinati, ricevuti, ecc..

![V5_03_09](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_09.png)
mentre, se richiesto il dettaglio righe, presenta l'elenco delle righe : 

![V5_03_10](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_10.png)	
# Interrogazione per ente
Come l'interrogazione per articolo, quella per ente prevede una serie di informazioni statistiche a livello ente : 

![V5_03_11](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_11.png)
## Funzione 1 :  tutti documenti
Presenta tutti i documenti dell'ente : 

![V5_03_12](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_12.png)
## Funzione 2 :  documenti
Viene richiesto obbligatoriamente il livello, presenta i documenti del livello in input : 

![V5_03_13](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_13.png)
Per ciascun documento si possono visualizzare (opzione ?) : 

- _1_% = Funzioni documento, lista delle funzioni del documento (F10)
- _1_05 = interrogazione, interrogazione della testata
- _1_MO = Movimenti di magazzino, eventuali movimenti eseguiti
- _1_FM = Forma estesa righe, lista delle righe nella forma estesa

## Funzione 3 :  righe articolo
Richiede obbligatoriamente il livello, se è attiva la gestione multiplant viene richiesto anche il magazzino (plant); presenta, in ordine di articolo, tutte le righe documento congruenti per livello e magazzino : 

![V5_03_14](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_14.png)
Livello e magazzino possono essere cambiati direttamente (viene rilanciata l'interrogazione).

Inserendo un articolo ci si può posizionare nella lista.

Con il tasto F18 (Proteggi/Sproteggi) si possono attivare i campi in  testa alle colonne con cui cambiare il significato e la presentazione di : 

- date
- quantità
- valori.

## Funzione 4 :  righe data
Richiede obbligatoriamente il livello; se è attiva la gestione multiplant viene richiesto anche il magazzino (plant); presenta, in ordine di data consegna confermata, tutte le righe documento congruenti per livello e magazzino : 

![V5_03_15](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_15.png)
Livello e magazzino possono essere cambiati direttamente (viene rilanciata l'interrogazione).

Inserendo una data ci si può posizionare nella lista.

Con il tasto F18 (Proteggi/Sproteggi) si possono attivare i campi in  testa alle colonne con cui cambiare il significato e la presentazione di : 

- date
- quantità
- valori.


## Funzione 5 :  sintesi impegni
Presenta, se esistenti, gli impegni materiali associati alle righe documento sintetizzati per articolo (la funzione è valida ad esempio per righe di conto / lavoro).
	
# Navigazione
Questa tipologia di interrogazione permette una scelta iniziale di modalità di consultazione più articolata rispetto alle precedenti con possibilità di definire delle memorizzazioni video richiamabili in cui sono predefiniti i parametri di : 

- consultazione/interrogazione
- impostazioni (quali schemi dati e valori utilizzare, se visualizzare righe derivate e/o origine)
- parzializzazioni (di testata e riga)

Sulla lista di risposta all'interrogazione è possibile una ulteriore navigazione scegliendo una delle funzioni possibili nel campo di input a sinistra della riga  (le funzioni presentate sono sensibili al contesto, quindi potranno essere a seconda che ci si trovi in un ordine o una bolla di conto lavoro di acquisto o di vendita).

Una ulteriore possibilità di navigazione è data dai campi di input in testa alla lista cambiando i quali si cambiano i dati presentati.

Per semplicità di esposizione percorreremo un solo ramo dato da una consultazione / presentazione,tenendo però presente che le modalità possono essere applicate per tutte le consultazioni / presentazioni.

Se la videata della navigazione è vuota il sistema presenta automaticamente la lista delle possibili consultazioni : 

![V5_03_16](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_16.png)
la scelta della consultazione porta direttamente alla lista di selezione del tipo di interrogazione (_2_Nota, per certe consultazioni esiste un solo tipo interrogazione, in questi casi il sistema assume direttamente il tipo di interrogazione e continua con il passo successivo).

Se è stata richiesta la consultazione per Documento, i tipi interrogazione sono i seguenti : 

![V5_03_17](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_17.png)
_2_Nota, per certe consultazioni nella lista dei tipi interrogazione può venire visualizzata una (T) (vedi ad esempio i tipi interrogazione per ente) significa che si tratta di un'interrogazione che parte dalla testata documento, negli altri casi vengono trattate solo le righe.

Scelto il tipo interrogazione si possono compilare i campi per indirizzare l'interrogazione (es. se si tratta di interrogazione per Ente potrà essere inserito un fornitore od un cliente a secondadel tipo documento inserito inizialmente), se i campi di selezione sono bianchi la lista parte dai record iniziali.

Fondamentale per ottenere una interrogazione utilizzabile è la definizione delle impostazioni : 

![V5_03_18](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_18.png)
si impostano : 

- _1_Schema, definisce i campi carattere da presentare nell'interrogazione
- _1_Schema valori, definisce i campi numerici da presentare
- _1_Formato esteso, consigliabile per avere il maggior numero di informazioni visualizzate
- _1_Righe derivate - origine, se si vogliono visualizzare anche le righe derivate e/o righe origine , è anche possibile impostare schemi e schemi valori specifici per righe derivate e origine

Date le impostazioni si possono inserire le parzializzazioni e si ottiene la visualizzazione del risultato : 

![V5_03_19](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_19.png)
cambiando i dati nei campi in testa alla lista si passa alla visualizzazione di altri dati :  es. nel precedente formato cambiando il N. documento  si passa alla visualizzazione delle righe (e righe derivate) di un altro documento.

Con la opportuna opzione nel campo _2_? si possono attivare altre funzioni di navigazione nei dati : 

![V5_03_20](http://localhost:3000/immagini/MBDOC_OGG-P_V5SI01/V5_03_20.png)
Con il tasto _2_F11 si può lanciare la stampa della lista visualizzata.

Con i tasti _2_F13 / F14 si può accedere nuovamente alle parzializzazioni (riga / testata) per modificarle e rilanciare l'interrogazione

Col tasto _2_F17 si possono cambiare le impostazioni (es. lo schema valori) e rilanciare l'interrogazione.

Col tasto _2_F20 ci si posiziona alla fine della lista (utile quando la lista ha un numero elevato di righe).
