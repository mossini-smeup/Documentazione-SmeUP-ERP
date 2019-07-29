# Documentazione Rilasci V2.R3

## Versione V2R3M071026-01Y Stable (Rilasciata il 24-06-2008)

- Modificata la gestione del NOTIFY(YES) nelle ACTION. Spostata la gestione completamente sull'evento UNDO.

## Versione V2R3M071026-01W Stable (Rilasciata il 09-06-2008)

- Modificata la gestione dei popup oggetto e di riga nel SFL.
- Aggiunta la possibilità di mostrare immagini e altri contenuti nelle G18. Riferirsi alla documentazione specifica.

## Versione V2R3M071026-01S Stable (Rilasciata il 15-04-2008)

- Risolto un problema sulla risoluzione dei titoli delle finestre che contengono altre variabili.

## Versione V2R3M071026-01R Stable (Rilasciata il 28-03-2008)

- I titoli delle finestre vengono definiti dinamicamente sulla base delle impostazioni della variabile *TITFIN, definibile nell'SCP_CLO.

## Versione V2R3M071026-01Q Stable (Rilasciata il 04-03-2008)

- E' ora possibile definire un timer di pressione dei tasti nelle schermate. E' possibile definire nel campo W$£FUN un valore del tipo TIMER(N)|KEY(P) dove N rappresenta il numero di secondi di attesa e P il bottone da premere di default.

## Versione V2R3M071026-01O Stable (Rilasciata il 21-02-2008)

- Modificato l'algoritmo di paginazione e posizionamento nei SFL.

## Versione V2R3M071026-01L Stable (Rilasciata il 09-01-2008)

- Aggiunta la possibilità di specificare uno stile (grassetto, corsivo etc.) per i caratteri di base dei campi.

## Versione V2R3M071026-01L Stable (Rilasciata il 21-12-2007)

- Modificata la funzione di scrittura dei log di sistema in modo da limitare ad un massimo di 10MB la dimensione di ogni file di log. I file vengono salvati con estensione .BAK e riscritti nuovamente.
- Aggiunta la gestione dell'esportazione in matrice per i SFL tramite la pressione di CTRL+F6.
- Aggiunta la gestione di griglie per la formattazione di G18 omogenee nell'esportazione in matrice.

## Versione V2R3M071026-01H Stable (Rilasciata il 14-12-2007)

- Risolto un errore che si poteva verificare quando il sistema riceveva uno schema di griglia in xml non valido.

## Versione V2R3M071026-01F Stable (Rilasciata il 06-12-2007)

- Aggiunta la gestione degli shortcut di carrello nei campi di input/output. E' possibile utilizzare le combinazioni ALT+C, ALT+O, ALT+W per copiare un oggetto nel carrello e la combinazione ALT+V per incollare l'ultimo oggetto dal carrello.

## Versione V2R3M071026-01E Stable (Rilasciata il 30-11-2007)

- Risolto un problema che faceva in modo di costruire i bottoni non più in ordine di tasto funzione.
- Aggiunta la funzionalità di sorting dell'XML nelle liste di nodi.

## Versione V2R3M071026-01D Stable (Rilasciata il 26-11-2007)

- Modificati i log di sistema. Sono stati normalizzati i tracciati e centralizzata la posizione in cui vengono salvati (la cartella application data dell'utente windows).

## Versione V2R3M071026-01B Stable (Rilasciata il 09-11-2007)

- Modificato l'aspetto de campi di Input/Output quando protetti (impossibile modificare il contenuto), in modo da essere identici ad un campo di tipo Label.

## Versione V2R3M071026-01A Stable (Rilasciata il 26-10-2007)

- Aggiunta la gestione degli errori del nuovo parser. In caso di XML errato, il sistema tenta di correggerlo. In caso di fallimento viene informato l'utente che può scegliere se visualizzare o meno il file.

