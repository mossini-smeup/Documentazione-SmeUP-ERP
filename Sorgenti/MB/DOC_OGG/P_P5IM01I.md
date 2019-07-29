# Impegni Materiali			
## Generalità
Gli impegni materiali rappresentano la lista dei componenti da utilizzare nella esecuzione di un ordine per la realizzazione di un prodotto di livello superiore.

Come ordine intendiamo : 

- _2_ordine di produzione in cui la lavorazione viene fatta internamente, gli impegni materiali in questo caso sono detti _3_impegni interni
- _2_ordine di conto lavoro, dove la lavorazione viene eseguita da un fornitore esterno (terzista) con l'utilizzo parziale o totale di componenti forniti dall'azienda, in questo caso gli impegni materiali sono detti _3_impegni esterni


Esistono delle funzioni di creazione e ricalcolo degli impegni materiali che possono venir lanciate automaticamente alla creazione e alla modifica degli ordini.
## Formato di lancio
L'interrogazione viene lanciata dal seguente formato : 

![P5_11_01](http://localhost:3000/immagini/MBDOC_OGG-P_P5IM01I/P5_11_01.png)
Si possono interrogare gli impegni per : 

- _2_articolo, inserire anche il plant e specificare se si vogliono gli impegni interni o quelli esterni
- _2_ordine di produzione
- _2_documento, di conto lavoro (inserire tipo documento, numero documento, numero riga)


## Formato di lista
Fatte le opportune selezioni si ottiene una lista tipo la seguente : 

![P5_11_02](http://localhost:3000/immagini/MBDOC_OGG-P_P5IM01I/P5_11_02.png)
Se la selezione era stata per Articolo, spostando il cursore su una riga e premendo il tasto F15 si ottiene la visualizzazione degli impegni del documento a cui la riga selezionata è riferita.

Se la selezione era stata per Ordine o Documento, spostando il cursore su una riga e premendo il tasto F15 si ottiene la visualizzazione degli impegni dell'articolo (plant) a cui la riga selezionata è riferita.

## Opzioni di riga
Sulla riga sono possibili diverse opzioni : 

![P5_11_03](http://localhost:3000/immagini/MBDOC_OGG-P_P5IM01I/P5_11_03.png)
Interrogazione del dettaglio dell'impegno.

Funzioni (F10) dell'oggetto a cui la riga è riferita (Ordine Produzione, Riga Documento, Articolo).

Funzioni (F10) dell'impegno materiali.

Analisi copertura impegni, viene mostrata la finestra di impostazione per l'analisi evadibilità dell'ordine (riga documento) a cui l'impegno appartiene.

Spedizioni collegate, è valido solo per impegni esterni e mostra le bolle di spedizione collegate al documento.
