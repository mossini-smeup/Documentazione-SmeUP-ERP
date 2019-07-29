# Costo Dinamico

Il costo dinamico è un costo che viene sempre calcolato al momento della richiesta.

Pertanto, nella definizione di questi tipi costo, è necessario tenere presente le seguenti considerazioni : 
* il processo di calcolo deve essere semplice.
* non produce log di errori
* non produce la documentazione di calcolo
* potrebbe variare tra una elaborazione e la successiva pur con gli stessi parametri di calcolo
* utilizzandolo come tipo costo all'interno del calcolo di un altro tipo costo potrebbe rallentarne il processo

Per definire un costo dinamico è necessario implementare nella tabella TCO il campo "Gestione eccezioni".
Può essere scelta una tre le seguenti modalità di calcolo del costo.
* >Acquisto medio
* >Acquisto medio con risalita
* >Acquisto ultimo
* >Acquisto ultimo con risalita
* >Vendita  medio
* >Vendita  medio con risalita
* >Vendita  ultimo
* >Vendita  ultimo con risalita
* >Ultimo da documenti
* >Medio da documenti
* >Listino
* >Ricalcolato dinamicamente
* >Righe documento
* >Ordini produzione
* >Lotto
* >Medio fiscale
* >Utente

## Acquisto medio
E' un costo relativo all'oggetto "AR" articolo.
Restituisce come costo il valore di acquisto medio determinato dal programma di calcolo delle statistiche di magazzino.
Il programma di calcolo delle statistiche si basa sui costi effettivi e previsti presenti sui movimenti di magazzino (£GMS).

## Acquisto medio con risalita
Stessa modalità di calcolo di Acquisto medio,  dove però nelle statistiche se non presente il costo effettivo di magazzino, assume come costo effettivo il costo previsto

## Acquisto ultimo
Stessa modalità di calcolo di Acquisto medio dove però restituisce il costo ultimo

## Acquisto ultimo con risalita
Stessa modalità di calcolo di Acquisto medio con risalita dove però restituisce il costo ultimo

## Vendita  medio
Stessa modalità di calcolo di Acquisto medio ma su Vendita

## Vendita  medio con risalita
Stessa modalità di calcolo di Acquisto medio con risalita ma su Vendita

## Vendita  ultimo
Stessa modalità di calcolo di Acquisto ultimo ma su Vendita

## Vendita  ultimo con risalita
Stessa modalità di calcolo di Acquisto ultimo con risalita ma su Vendita

## Ultimo da documenti
E' un costo relativo all'oggetto "AR"articolo.
Restituisce come costo il valore dell'ultimo documento relativo alla data richiesta.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi ai documenti da elaborare.

## Medio da documenti
E' un costo relativo all'oggetto "AR" articolo.
Restituisce come costo il valore medio dei documenti nel periodo richiesto.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi ai documenti e al periodo da elaborare.

## Listino
E' un costo relativo all'oggetto "AR" articolo.
Restituisce come costo il valore di listino valido alla data richiesta.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi al listino da elaborare.
Se non viene indicato alcun un ente di defalut viene assunto l'ente preferenziale dell'articolo.
Nel parametro di eccezione la "valuta listino" ha il seguente significato : 
* >*BLANKS Se non reperisce fornitore abituale va con fornitore generico (**) e forza la
  valuta presente nella tabella B£2
* >1 Se non reperisce fornitore abituale va con fornitore generico (**) e forza la
  valuta *BLANKS
* >2 Se reperisce fornitore abituale ricerca sul listino con quel fornitore e con la
  valuta della tabella B£2, se non reperisce il fornitore abituale usa il fornitore
  generico (**) sempre con la valuta della tabella B£2
* >3 Se reperisce fornitore abituale ricerca sul listino con quel fornitore e con la
  valuta *BLANKS, se non reperisce il fornitore abituale usa il fornitore generico (**)
  sempre con la valuta *BLANKS

## Ricalcolato dinamicamente
E' un costo relativo all'oggetto "AR" articolo.
Lancia il calcolo del costo. Attivo solo sul cacolo della versione V2R2.

## Righe documento
E' un costo relativo all'oggetto "DR" Righe documento.
Resitituisce come costo il valore della riga del documento. Viene specificato in un apposito flag se il costo è effettivo o previsto.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi al documento.

## Ordini produzione
E' un costo relativo all'oggetto "OR" Ordine produzione. Nella richiesta del costo è obbligatorio indicare la fase.
Restituisce come costo il valore medio di tutti i documenti che fanno riferimento all'ordine di produzione e fase richiesti.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi ai documenti da elaborare.

## Lotto
E' un costo relativo all'oggetto "LO". Solo per costi di acquisto e lavorazione esterna.
Restituisce come costo il valore medio di tutti i documenti che fanno riferimento al lotto. (Mediante il file CQGELO)
Se conto lavoro nella richiesta del calcolo è obbligatorio indicare la fase.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi ai documenti da elaborare.
Se ad ogni entrata viene generato il lotto per ciascuna riga, il costo del lotto è il valore della corrispondente riga del documento
Se ad ogni entrata viene generato il lotto per ciascun articolo, il costo del lotto è il valore medio delle righe del documento con articolo corripondente all'articolo del lotto.
In ogni caso il costo del lotto è facilmente rintracciabile perchè fa riferimento ad uno specifico documento di entrata merce.

## Medio fiscale
E' un costo relativo all'oggetto "AR" articolo.
Restituisce come costo il valore medio dei costi di valorizzazione fiscale.
Può essere calcolato con modalità LIFO, FIFO, Al costo.
* LIFO è la vedia del costo di tutti gli strati lifo che determinano la giacenza e il valore lifo del periodo
* FIFO è la vedia del costo di tutti gli strati fifo che determinano la giacenza e il valore fifo del periodo
* Al costo è il costo medio memeorizzato nello strato del periodo.
Nel "parametro eccezione" della tabella TCO devono essere indicati i parametri relativi al magazzino fiscale da elaborare.

## Utente
E' un costo a totale disposizione dell'utente. Può pertanto essere relativo a qualsiasi oggetto.
Restituisce come costo il valore calcolato dal programma fisso di exit B£G55S_U.
Nel "parametro eccezione" della tabella TCO può essere parametrizzata la chiamata al programma di exit.
