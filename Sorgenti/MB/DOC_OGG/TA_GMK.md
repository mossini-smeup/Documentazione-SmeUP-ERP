# GMK - Passi elaborazione Motore Inferenziale (£GMI)
## OBIETTIVO
Descrivere i passi di elaborazione eseguiti dal motore inferenziale nelle assegnazioni.
L'assegnazione può essere per la determinazione dell'ubicazione di versamento o per la prenotazione di una giacenza per il prelievo.
Le assegnazioni vengono eseguite dal motore inferenziale attraverso l'elaborazione dei programmi presenti negli elementi della tabella GMK.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$GMKA __Tipo passo__
È un elemento fisso B£TGMK che definisce il tipo di oggetto inserito nel programma metodo
 :  : FLD T$GMKB __Programma/Metodo__
È un oggetto che determina il comportamento del motore inferenziale nell'esecuzione del passo
 :  : FLD T$GMKC __Parametro__
Contiene i parametri di funzionamento del programma. I parametri possono essere esplicitati nella visualizzazione della tabella
 :  : FLD T$GMKD __Passo succ.- Subset.__
È un sottosettore della tabella GMK dove si trova il passo successivo che il motore inferenziale deve eseguire, dopo il completamento del passo corrente.
 :  : FLD T$GMKE __Passo succ.- Elemen.__
È l'elemento della tabella GMK che rappresenta il passo successivo che il motore inferenziale deve eseguire, dopo il completamento del passo corrente.
