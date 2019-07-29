# GMU - Tipologia ubicazione
## OBIETTIVO
Impostare appartenenze specifiche per l'ubicazione (es. ubicazioni di FORNITORI, ARTICOLI, CENTRI DI LAVORO, ecc.) e quindi creare classificazioni di ubicazione (es.ubicazioni di CONTO DEPOSITO, MAGAZZINO, LINEA, COLLAUDO, ecc.)
Fissare eventualmente le dimensioni standard per il tipo di ubicazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice della tipologia
 :  : FLD T$DESC Descrizione
 :  : FLD T$KYC1 __Tipo codice di appartenenza__

 :  : FLD T$PAR1 __Parametro codice di appartenenza__

 :  : FLD T$ALTE __Altezza__

 :  : FLD T$LARG __Larghezza__

 :  : FLD T$LUNG __Lunghezza__

 :  : FLD T$PEMX __Peso massimo__

 :  : FLD T$GMUA __Area di appartenenza__
È un elemento della tabella GMR :  definisce l'eventuale area di appartenenza dell'ubicazione.
**NOTA** :  non necessariamente un'ubicazione appartiene ad un'area giacenza. In generale la stessa ubicazione può contenere giacenze da aree diverse.
 :  : FLD T$GMUB __Met.accesso giacenza x ubicazione__
È un elemento della tabella GMF :  definisce la vista di GMQUAN che guida il reperimento della giacenza dell'ubicazione, nella scansione per tipo ubicazione.
 :  : FLD T$GMUC __Met.accesso giacenza x articolo__
È un elemento della tabella GMF :  definisce la vista di GMQUAN che guida il reperimento della giacenza di un articolo nelle ubicazioni di questo tipo.
 :  : FLD T$GMUD __Domanda costruz.codice__
È un elemento della tabella B£F :  guida la costruzione del codice ubicazione in ubicazioni di questo tipo.
 :  : FLD T$GMUE __Causale di prelievo__
È un elemento della tabella GMC, a disposizione di eventuali programmi che eseguono un prelievo da questa ubicazione.
 :  : FLD T$GMUF __Causale di versamento__
È un elemento della tabella GMC, a disposizione di eventuali programmi che eseguono un versamento in questa ubicazione.
 :  : FLD T$GMUG __Categoria parametri__
È un elemento della tabella C£E. Se impostato, è la categoria di parametri che si possono associare alle ubicazioni di questo tipo. Se non impostato, le ubicazioni di questo tipo non avranno parametri associati.
 :  : FLD T$GMUH __Categoria parametri impliciti__
È un elemento della tabella C£I. Se impostato, è la categoria di parametri interni associata alle ubicazioni di questo tipo.
 :  : FLD T$GMUI __Pgm aggiustamento__
È il suffisso del pgm GMUB01D_x :  permette di gestire controlli e impostazioni personalizzate durante la gestione dell'anagrafico ubicazioni (Es. GMUB01D_Z).
 :  : FLD T$GMUL __Tipo date implicite__
Elemento della tabella C£JUB che specifica il significato delle date libere presenti nell'archivio.
 :  : FLD T$GMUO __Ubicazione MFP__
Definisce se è un'ubicazione gestita in MFP
