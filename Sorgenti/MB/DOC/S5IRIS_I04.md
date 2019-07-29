# Programma Lancio
## B£BCD08
Nuovo PGM B£BCD08 :  guida interrogazione BCD di interrogazione. Riferirsi all'altro documento per come ricevere le informazioni e scegliere la sessione.
Alla fine questo programma conosce l'ambiente, la B§G e la sessione (problema di come farlo cieco :  forse anche se la tripletta precedente è unica farla comunque vedere, in modo da poter premere l'Invio.
In LDA mettere : 
1 - 15 mette la B§G (come B£BCD01)
16 -25 mette la sessione (adesso B£BCD01 mette la lunghezza di £TABS5X, anche se il £S5XDS, essendo la tabella di soli campi, è già lunga correttamente e non 100 come per quelle normali, e quindi si otterrebbe con %LEN(£S5XDS).

## B£BCD09
Lancia il nuovo PGM B£BCD09 con in LDA la B§G e dopo la sessione. Questo programma carica la parte standard della memoria dal file, mette la sessione nella schiera numeri, ricostruisce l'LDA come nella gestione (rimette la lunghezza), riempie S5X dal file, imposta il flag di interrogazione e lancia PGMX (normalmente S5SMIN) con un parametro in modo che sappia di essere in interrogazione e carichi le tabelle da file salvato e non dalle tabelle :  questo per essere coerenti e avere la situazione fotografata al momento del lancio...).
Da qui in poi dovrebbe essere normale. Lo script INT sa che è in interrogazione e come primo passo carica le memorie specifiche dal file. Questa azione si potrebbe fare anche in S5SMIN ma mi sembra più pulito farla dallo script per mantenere simmetria con la gestione.





