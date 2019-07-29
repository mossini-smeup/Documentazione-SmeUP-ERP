# G.SUB.SCH Sottosezione Scheda

All'interno di una sezione è possibile definire una sottosezione che contiene un'intera scheda.

# Dati

A questa sottosezione sono associate le funzioni dati relative al caricamento di scheda definita
esternamente o internamente allo script della scheda stessa.

Al che per non far proliferare il numero di membri relativi alle schede l'utilizzo della
scheda definita internamente torna utile quando si voglio impostare delle sezioni dinamiche,
la cui visualizzazione è condizionata da variabili presenti nel scheda madre :  infatti le
specifiche condizionali funzionano solo con valori predeterminati al momento del caricamento
della scheda. Perciò se definisco una sottoscheda ad essa posso passare parametri della scheda
madre che non sono predeterminati per la madre ma lo sono per la sottoscheda.

# Setup

Questo tipo di sottosezione non supporta un setup specifico, perciò viene solitamente utilizzata l'istruzione di setup di default (G.SET.DFT)

