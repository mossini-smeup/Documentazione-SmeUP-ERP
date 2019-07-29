## Cos'è un Q4

L'oggetto Q4 identifica i campi ed il loro verso (ascendente/discendente) attraverso cui viene definito l'ordinamento di caricamento, all'interno di matrici di dati (nel senso matematico del termine) costituite da un elenco di righe facenti riferimento ad istanze della medesima classe (un elenco di articoli, di clienti, di movimenti di magazzino ecc.)

Il fatto di identificare tale insieme di dati in un oggetto permette vari vantaggi fra i quali : 
* Dare la possibilità di sfruttare questa possibilità su elaborazioni di query
* Rendere disponibile, come per tutti gli altri oggetti di smeup, una serie di funzionalità di base, fra cui la funzione di gestione che permette di inserire/modificare/cancellare istanza della classe.

## La codifica degli ordinamenti

La gestione dell'oggetto Q4 si basa sulla struttura ramificata comune a tutti gli oggetti Qx. Per tale motivo esistono varie nature di ordinamenti definite in modo eterogeneo (per fare un esempio confrontando la gestione dei Qx con le interfacce degli oggetti smeup, per queste, mentre posso avere attivi o gli articoli di smeup o gli articoli di un'altra applicazione, per gli oggetti Qx è come se avessi la possibilità di avere contemporaneamente sia gli articoli smeup che gli articoli di altre applicazioni nella medesima interfaccia. L'univocità del codice in tale struttura viene garantita dal fatto che ad ogni istanza, rispetto al suo codice originale, viene/vengono anteposti uno o due caratteri di prefisso, univoci per ogni fonte.

In smeup si possono trovare sia istanze di ordinamento fornite dallo standard che istanze di ordinamenti creati appositamente nell'ambiente cliente. A differenza degli schemi per i quali gli schemi possono avere natura eterogenea a standard esistono essenzialmente due nature, una pero lo standard e una per quelle dell'ambiente cliente.

## Gli ordinamenti standard - "T/"
Questi ordinamenti aventi prefisso "T/" vengono definiti esclusivamente per lo standard all'interno di uno script nel file SCP_SET. Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a Q4TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Q4TipoOggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro Q4CNCLI e quindi il Q4CN. Tramite il suddetto script, solo gli oggetti che appartengono ad un archivio è possibile definire degli ordinamenti standard. E' importante notare che fra le istanze di particolare rilievo è l'istanza T/DFT :  se presente rappresenta l'ordinamento di default di tutte le query che non prevedono a loro volta uno ordinamento di default specifico.
NOTA BENE :  per tutti gli altri oggetti o cmq in assenza dell'indicazione di un ordinamento specifico, nei pgm standard di elaborazioni delle query viene applicato l'ordinamento per codice.

Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati alla definizione di un ordinamento. Possono essere catalogati come tali i seguenti tag : 

* ORD.ORD :  definisce un ordinamento
* ORD.FLD :  definisce un campo di ordinamento

Per il tag ORD.FLD ricopre un ruolo particolarmente importante il nome del campo, in esso va infatti indicato il codice della campo dell'archivio di riferimento che si vuole utilizzare come chiave di ordinamento.

## Gli ordinamenti dell'ambiente cliente - "S/"
Questi ordinamenti vengono definiti all'interno di uno script nel file SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).
Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN.
Quando si vuole quindi implementare un nuovo s sarà innanzitutto necessario : 
* Verificare se esiste già uno file sorgente SCP_QRY nella libreria di personalizzazione dell'ambiente.
** In caso contrario crearlo (copia ad esempio quello della DEV)
** In caso affermativo verificando la presenza del sorgente corrispondente alla classe interessata (facendo le dovute considerazioni sul tipo/parametro)
** Se opportuno prendere in considerazione la possibilità di sfruttare le istruzioni dello script INC.SCP per includere in differenti script le stesse istruzioni
Fatto questo si può passare alla compilazione dello script. In questo senso è' importante notare che all'interno di questi script possono essere definiti, non solo gli schemi, ma anche tutte quelle informazioni utilizzabili poi nella costruzione di query in ambiente cliente. Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati alla definizione di uno filtro. Possono essere catalogati come tali i seguenti tag : 

* QRY :  query - attraverso questo tag verrà definita la query. In tale tag è prevista l'indicazione filtro utilizzato dalla query attraverso l'attributo DftOrd
* ORD :  definisce un istanza di ordinamento
* ORD.FLD :  definisce il campo di ordinamento

Per il tag ORD.FLD ricopre un ruolo particolarmente importante il nome del campo, in esso va infatti indicato il codice della campo dell'archivio di riferimento che si vuole utilizzare come chiave di ordinamento.













