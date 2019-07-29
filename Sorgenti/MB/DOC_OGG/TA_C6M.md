# C6M - Eccezioni su riclassifiche Contabili
 :  : DEC T(ST) K(C6M)
## OBIETTIVO
Definire delle eccezioni rispetto alla struttura standard nella  determinazione delle linee di riclassifica.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Descrizione**
Il codice elemento deve presentare una struttura particolare : 
- I primi due caratteri indicano il sottosettore della tabella C5N
- I terzo carattere determina se l'elemento è intestato ad un mastro o ad un conto contabile :  se questo carattere è
una "M" significa che i caratteri successivi indicheranno un mastro, mentre al contrario esso rappresenta il primo
carattere del codice del conto contabile.
 :  : FLD T$DESC **Descrizione**
Descrive l'eccezione.
 :  : FLD T$C6MA **Linea di Riclassifica**
Definisce la linea di riclassifica che voglio attribuire all'eccezione.
 :  : FLD T$C6MB **Causale**
Se indicata implica che l'eccezione sarà attivata solo quando il conto/mastro indicato nel codice elemento sarà utilizzato in concomitanza con tale causale.
 :  : FLD T$C6MC **Società Intercompany**
Se indicata implica che l'eccezione sarà attivata solo quando il conto/mastro indicato nel codice elemento sarà utilizzato in concomitanza con tale società intercompany.
 :  : FLD T$C6MD **Società Origine**
Se indicata implica che l'eccezione sarà attivata solo quando il conto/mastro indicato nel codice elemento sarà utilizzato in concomitanza con tale società origine.
