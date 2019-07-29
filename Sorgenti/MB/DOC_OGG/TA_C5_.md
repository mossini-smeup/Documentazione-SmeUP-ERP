# C5* - Controlli generali
 :  : DEC T(ST) K(C5*)
## OBIETTIVO
Questa tabella è prevista per contenere alcuni valori che sono condizioni dell'applicazione o per qualsiasi uso simile l'utente voglia farne.
## SOTTOSETTORI
Ogni subsettore ha un significato specifico. Per questa tabella non si prevedono sottodefinizioni, quindi si deve utilizzare solo per verificare la correttezza di un dato e/o per decodificare un codice.
In particolare, è possibile associare un subsettore ai significati particolari di qualche tabella.
_9_Esempio : 
Se si dice che il contenuto possibile di una scelta di tabella sono 6 parole/valori non gestibili con la tecnica dei limiti, si fa riferimento ad un subsettore. La ricerca con "!" o "?" fornisce un dettaglio maggiore.
Per il dettaglio dei sottosettori utilizzati vedere nella gestione tabelle ricercando sul campo Subsettore.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive l'elemento
 :  : FLD T$PARS **Parametri**
Il significato di questo campo varia a seconda del subsettore ed il suo contenuto può essere gestito tramite il pgm di exit B£TC5_.
Significati specifici per sottosettore : 
C5*PA - Tipo protocollo
Pos. 01-01 --> Controllo consecutività :  se valorizzato inibisce i controlli di consecutività sulle registrazioni contabili, per le quali è stato utilizzato questo tipo protocollo.


