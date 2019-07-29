**Sistemati**

_1_Versione 1.0.d
 1. Aumentato Numero di Decimali di una cella numerica da 2 a n

_1_Versione 1.0.e
 2. Eliminato AV se generazione foglio excel con tabella pivot correlata con piu' di 8000 righe

_1_Versione 1.0.f
 3. Interfacciamento diretto via OLE per eliminare componenti Officepartnet e risolvere
    problemi di AV sporadici
 4. Eliminata gestione modelli
 5. E' possibile selezionare il nome del file da salvare
 6. Inserita gestione colonne nascoste
 7. I titoli delle colonne sono ora descrittivi

_1_Versione 1.0.g
 8. Inserita gestione date definite senza separatori nell'Xml

_1_Versione 1.1.m
 9. Eliminata Creazione Tabella Pivot
10. Eliminata Richiesta Salvataggio Foglio Excel
11. Nascosta Finestra

## Rilascio 21/10/2005

- Cambiato l'agoritmo di compilazione di Excel in fase di esportazione per migliorarne le performance. I tempi di sono abbassati da 2-3 minuti per circa 2000 record, a 10-12 secondi.
- Le date nell'esportazione in Excel ora vengono formattate come date e non più come stringhe. Questo permette sorting e filtering corretto.
- Risolto un problema che aggiungeva una virgola (in fondo al numero) anche nei numeri privi di virgola durante l'esportazione in Excel.
- Risolto un problema nell'esportazione in Excel. In alcuni casi, con totalizzazioni abilitate, veniva perso l'ultimo record.

