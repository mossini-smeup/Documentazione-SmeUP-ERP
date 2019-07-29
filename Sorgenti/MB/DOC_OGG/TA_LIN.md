# LIN - Lingua
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$LINA __Calcolo delle traduzioni__
Permette di specificare se, nel caso che un passo di un flusso richieda il calcolo delle descrizioni, tale calcolo deve essere fatto per questa lingua. Possiamo avere : 
- 1    =    Aggiorna solo le descrizioni sull'archivio delle descrizioni estese.
- 2    =    Aggiorna anche la descrizione base dell'oggetto (per gli oggetti, esempio AR=Articolo) per cui è prevista.

La descrizione in questa lingua sarà la descrizione dell'oggetto.
 :  : FLD T$LINB __Codice lingua OS/400__

 :  : FLD T$LINC __Lingua base__
Indica la lingua da utilizzare in mancanza del valore per la lingua stessa.
_9_Esempio :  nell'utilizzo multilingua, quando vengono riprese le costanti da presentare a video (o per la costruzione dei file video) se manca la descrizione per il tedesco, si riprende l'inglese.
