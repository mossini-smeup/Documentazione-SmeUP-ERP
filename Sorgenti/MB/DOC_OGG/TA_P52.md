# P52 - Param.produz.a dispon.chiamata
 :  : DEC T(ST) K(P52)
## OBIETTIVI
Contiene i parametri che guidano la gestione della produzione a disponibilità chiamata (pdc). Per PDC si intende la particolare modalità operativa che, senza la codifica di ordini di produzione, è legata dinamicamente ad una domanda in continua evoluzione. È legata ugualmente alla natura fisica dello stato della produzione stessa (quantità del materiale nelle varie ubicazioni) e degli eventi che si verificano (spostamenti tra ubicazioni, sia per alimentazione di un centro, verso un'ubicazione a monte di esso, sia per effetto di una lavorazione, da un'ubicazione a monte ad una a valle.).
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P52A __Impegno risorse per contenitore__
Definisce il tipo impegno risorse a cui verranno intestati gli impegni risorse pdc.
Il tipo origine di questi impegni deve essere un contenitore.
 :  : FLD T$P52B __Parametro ubicazione precedente__
Definisce il parametro in cui sono codificate le ubicazioni a monte delle risorse.
 :  : FLD T$P52C __Parametro ubicazione suiccessiva__
Definisce il parametro in cui sono codificate le ubicazioni a valle delle risorse.
 :  : FLD T$P52D __Area di wip interno__
Definisce l'area di magazzino, all'interno dell'azienda, in cui si trovano le giacenze che vengono considerate dalla pdc.
 :  : FLD T$P52E __Gruppo fonti domanda__
È il gruppo fonti che costituisce la domanda della pdc :  verosimilmente dovrà contenere un fabbisogno per giorno.
Un approccio possibile è impostare un gruppo fonti che contenga, come unica fonte, il fabbisogno giornaliero.
 :  : FLD T$P52F __Modalità di avanzamento__
Definisce il modo con cui si decide la priorità di avanzamento nel corso della pdc.
Essa opera per contenitori. Si possono avere i seguenti valori : 
-     F - viene avanzato per primo il contenitore più vecchio (con il numero più basso)
-     V - viene avanzato per primo il contenitore più vicino all'arrivo (a pari vicinanza viene comunque avanzato per primo il contenitore con quantità maggiore :  in questo modo viene ridotto il numero di contenitori da movimentare).
 :  : FLD T$P52T __Variazione cicli__
Se impostato, è possibile variare il ciclo del contenitore (le alternative devono essere nell'ambito dello stesso gruppo risorse).
 :  : FLD T$P52G __Area di wip esterno__
Definisce l'area di magazzino, all'esterno dell'azienda, (normalmente le aree di conto lavoro di fase), in cui si trovano le giacenze che vengono considerate dalla pdc.
 :  : FLD T$P52H __Prefisso contenitori pianificati__
È un carattere che viene assunto come prefisso dei contenitori pianificati, nel processo di generazione degli impegni risorse a disponibilità chiamata per contenitore. Se non impostato viene assunto il carattere 'X'.
 :  : FLD T$P52I __Tipo contenitore rilasciato__
Definisce il tipo contenitore che verrà assunto all'atto della creazione di un contenitore rilasciato.
 :  : FLD T$P52J __Causale avanzamento__
Definisce la causale di avanzamento della dichiarazione attività, generata automaticamente all'atto dello spostamento di un contenitore quando attraversa, nel suo ciclo logistico, una o più risorse.
 :  : FLD T$P52K __Tipo collegamento schedulazione__
Definisce la modalità con cui la pdc è collegata alla schedulazione : 
-     ' '  -  nessun collegamento
-     '1'  -  collegamento a livello di risorsa
-     '2'  -  collegamento a livello di gruppo risorsa
 :  : FLD T$P52L __Tipo giacenza materiale in wip__
Definisce, insieme con l'area di wip interno, la sezione dell'archivio giacenze in cui si costruisce la quota di componenti in wip. Deve essere un tipo giacenza solo per articolo, con impostato nell'oggetto contenitore 'AR'.
 :  : FLD T$P52M __Causale di prelievo__
Se impostata, viene assunta per il prelievo dei componenti alla fase, durante lo spostamento dei materiali. In mancanza viene assunta la causale dai parametri logistici. Deve avere tipo movimento 'PD' (prelievo per disponibilità chiamata).
 :  : FLD T$P52N __Tipo quantità per contenitore__
Definisce come è reperita la quantità per contenitore, usata nella pianificazione dei nuovi contenitori nella PDC.
Può assumere i seguenti valori : 
-     ' '  -  Quantità impostata specificamente nei parametri logistici di magazzino/articolo (parametro C05)
-     '1'  -  Quantità per il contenitore standard
-     '2'  -  Lotto multiplo dell'articolo
 :  : FLD T$P52S __Sempre quantità per contenitore__
Se impostato, anche l'ultimo contenitore verrà pianificato per la quantità del contenitore.
 :  : FLD T$P52O __Ubicazione porto__
Se impostata, viene assunta come ubicazione post dell'ultima risorsa, se manca l'ubicazione post nella risorsa stessa.
 :  : FLD T$P52P __Schedulazione automatica__
Se impostato, dopo ogni transazione che coinvolge un avanzamento, verranno ricostruiti gli impegni risorse rischedulati, vale a dire con le date di schedulazione compattate 'al più presto'. Se non impostato, gli impegni risorse verranno soltanto ridotti della quantità avanzata (ed eventualmente eliminati se l'avanzamento è totale), mentre le date di schedulazione rimarranno le precedenti, fissate all'ultima schedulazione.
 :  : FLD T$P52Q __Tipo quantità multipla__
Definisce se e come arrotondare ad un multiplo la quantità per contenitore, nella pianificazione dei nuovi contenitori nella PDC.
La quantità viene arrotondata al multiplo immediatamente superiore; è cura dell'utente impostare che il multiplo sia un sottomultiplo della quantità per contenitore (in caso di incongruenze ha la priorità quest'ultimo valore).
Può assumere i seguenti valori : 
-     ' '  -  Nessun arrotondamento
-     '1'  -  Quantità reperita da parametri logistici di magazzino/articolo (parametro C06)
-     '2'  -  Lotto multiplo dell'articolo
 :  : FLD T$P52R __Causale di scarto__
Definisce la causale con cui si dichiarano le attività di scarto.
