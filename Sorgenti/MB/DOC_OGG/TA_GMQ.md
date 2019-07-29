# GMQ - Tipo giacenza
## OBIETTIVO
Identifica il massimo livello di dettaglio a cui si intende tenere, nelle varie aree, la giacenza di magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice del tipo giacenza.
 :  : FLD T$DESC Descrizione
 :  : FLD T$T,1 __Tipo/Parametro Codice 1/4__
Individuano gli oggetti che, insieme con articolo e magazzino, contribuiscono ad identificare la giacenza.
Se non viene impostato alcun campo, la giacenza sarà a livello di articolo/magazzino.
Se invece, ad esempio, nel primo codice si imposta l'oggetto fornitore e nel secondo l'oggetto lotto, la giacenza sarà a livello anche di fornitore/lotto.
 :  : FLD T$P,1.T$T,1 Parametro Codice 1
 :  : FLD T$P,2.T$T,1 Parametro Codice 2
 :  : FLD T$P,3.T$T,1 Parametro Codice 3
 :  : FLD T$P,4.T$T,1 Parametro Codice 4
 :  : FLD T$T,2.T$T,1 Tipo Codice 2
 :  : FLD T$T,3.T$T,1 Tipo Codice 3
 :  : FLD T$T,4.T$T,1 Tipo Codice 4
 :  : FLD T$T,5 __Tipo/Parametro Contenitore__
Individuano la natura dell'eventuale contenitore, nel caso in cui si voglia avere una vista della giacenza anche a livello di contenitore.
Attualmente l'unico oggetto ammesso è 'CZ' con parametro bianco
 :  : FLD T$P,5.T$T,5 Parametro Contenitore
 :  : FLD T$GMQA __Tipo giacenza secondario__
Se questo campo viene impostato, la giacenza di questo tipo è già presente in altri tipi, modificati con lo stesso movimento, e quindi non contribuisce alla giacenza totale.
_9_Esempio :  può essere un tipo giacenza in unità di misura alternativa, oppure una sintesi per tutti i fornitori di una giacenza tenuta anche a livello di fornitore singolo.
 :  : FLD T$GMQB __Giacenza in u.m. esterna__
Se questo campo viene impostato, nelle schede di magazzino relative a questi tipi giacenza, verrà trattata la quantità del movimento in unità di misura esterna.
 :  : FLD T$GMQC __Tipo giacenza alternativa collegata__
Permette la visualizzazione affiancata della giacenza alternativa di un articolo, se gestita opzione in tabella GM1.
Se presente il tipo giacenza, questo sarà quello alternativo. Se, al contrario, il tipo giacenza non è presente ma è presente l'area, verrà assunto il tipo giacenza in esame.
 :  : FLD T$GMQD __Area giacenza alternativa collegata__
Permette la visualizzazione affiancata della giacenza alternativa di un articolo, se gestita opzione in tabella GM1.
Se presente l'area giacenza questa sarà quella alternativa. Se non è presente l'area ma è presente il tipo giacenza, verrà assunta l'area giacenza in esame.
