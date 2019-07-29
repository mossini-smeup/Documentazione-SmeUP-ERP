# D5S - Contesti per oggetto
 :  : DEC T(ST) K(D5S)
## OBIETTIVO
Creare contesti per l'archivio D5COSO.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Ha lunghezza di 12 caratteri e indica tipo e parametro dell'oggetto che si vuole gestire nel D5COSO. Di conseguenza, i primi 2 caratteri indicano l'oggetto e gli altri 10 l'eventuale parametro.
Esempi di contesti validi sono : 
- AR  :  articolo
- CNCLI  :  cliente
- TABRA  :  elemento tabella BRA (tipi AR)
- TAV5BCP  :  elemento tabella V5B sottosettore CP
 :  : FLD T$DESC Descrizione
 :  : FLD T$D5SA **S/S temi**
È il sottosettore della tabella D5O in cui sono presenti i temi validi per il contesto.
Si consiglia di mantenere i temi dei vari contesti separati.
