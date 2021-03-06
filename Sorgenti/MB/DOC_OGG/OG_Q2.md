## Cos'è un Q2

L'oggetto Q2 identifica l'elenco delle colonne di dati e la loro modalità di presentazione, all'interno di matrici di dati (nel senso matematico del termine) costituite da un elenco di righe facenti riferimento ad istanze della medesima classe (un elenco di articoli, di clienti, di movimenti di magazzino ecc.)

Il fatto di identificare tale insieme di colonne in un oggetto permette vari vantaggi : 
* Dare la possibilità all'utente di scegliere quale schema utilizzare per un certa elaborazione di output .
* Dare la possibilità di sfruttare questa possibilità su elaborazioni completamente differenti che hanno in comune il fatto di elaborare istanze della medesima classe.
* Rendere disponibile, come per tutti gli altri oggetti di smeup, una serie di funzionalità di base, fra cui la funzione di gestione che permette di inserire/modificare/cancellare istanza della classe.

## La codifica degli schemi

La gestione dell'oggetto Q2 si basa sulla struttura ramificata comune a tutti gli oggetti Qx. Per tale motivo esistono varie nature di schemi definite in modo eterogeneo (per fare un esempio confrontando la gestione dei Qx con le interfacce degli oggetti smeup, per queste, mentre posso avere attivi o gli articoli di smeup o gli articoli di un'altra applicazione, per gli oggetti Qx è come se avessi la possibilità di avere contemporaneamente sia gli articoli smeup che gli articoli di altre applicazioni nella medesima interfaccia. L'univocità del codice in tale struttura viene garantita dal fatto che ad ogni istanza, rispetto al suo codice originale, viene/vengono anteposti uno o due caratteri di prefisso, univoci per ogni fonte.

In smeup si possono trovare sia istanze di schema fornite dallo standard che istanze di schema creati appositamente nell'ambiente cliente. Di seguito ne vengono descritte le principali forme.

## Gli schemi fissi distribuiti dallo standard

Ci sono vari schemi già predefiniti e distribuiti dallo standard. Questi, fra l'elenco delle istanze degli schemi selezionabili, questi possono essere riconosciuti dai prefissi "T/" e "Q/" (esclusi quelli che nel terzo carattere riportano una "X" es. Q/X01).

L'esistenza di due prefissi è dovuta alle due differenti modalità tecniche di implementazioni di tali strutture. Ognuna di esse presenta propri punti di forza/debolezza e quando si è in procinto di creare un nuovo schema, la scelta dell'ulta piuttosto dell'altra tecnica andrà effettuata sulla base di questi punti.

* Gli schemi **"T/ - Da script SCN_NAV"**
** Punti di forza
*** La loro implementazione è particolarmente veloce :  è sufficiente compilare le righe di uno script (con la possibilità di essere aiutati da un wizard) del file SCP_NAV
*** Di per sè la definizione dello schema è inoltre molto semplice essendo di fatto nient'altro che un elenco di campi dell'archivio di appartenenza della classe o di attributi
*** Permette di indicare l'utilizzo di colonne aggiuntive in maniera semplificata
*** Il fatto che la sua definizione sia limitata o a campi dell'archivio o ad attributi, di fatto lo rende molto adatto a risolvere in modo ottimizzato estrazioni di dati tramite SQL.
** punti di debolezza
*** le semplificazione e la strutturazione di questa forma di schemi costituisce anche il suo unico debolezza :  non possono in fatti essere implementate eccezioni o deviazioni all'interno di tale struttura. Quando risultano necessarie queste funzionalità si possono utilizzare gli schemi "Q/"
* Gli schemi da **"Q/ - Da pgm B£IQ2_xx"**
** Punti di forza
*** Gli schemi Q/ nascono per sopperire alle debolezze degli schemi "T/" :  essi sono infatti costruiti da pgm RPGLE che può quindi applicare qualsiasi tipologia di logica di costruzione. Si pensi alla necessità di nascondere/visualizzare colonne in base a certe condizioni dell'ambiente (come i valori della tabella B£2) o alla necessità di calcolare informazioni che non possono essere reperite tramite l'utilizzo degli attributi. In questi pgm può essere inoltre interessante sfruttare la possibilità di passare un parametro "SchPar" (si veda la documentazione della /COPY £IQ2) attraverso il quale far recepire al pgm delle informazioni che permettono di fare assumere al pgm differenti comportamenti.
*** Una particolarità di questi schemi è anche la possibilità di poter ritornare a fronte di una sola istanza più righe di matrice o al contrario (se può risultare opportuno) nessuna riga.
** Punti di debolezza
*** Il principale punto di debolezza degli schemi Q/ può sussistere nelle performance :  data la libertà di comportamento concessa a questa struttura, nell'utilizzare questa forma di schema, per ogni riga della matrice dovrà essere effettuata una chiamata alla £IQ2 passando in input l'istanza nel campo £IQ2ID e/o l'intera DS di riferimento nel campo £IQ2IN.

## Creare nuovi schemi nell'ambiente cliente

A fianco degli schemi distribuiti dallo standard possono essere implementati degli schemi creati appositamente nell'ambiente cliente.

Mentre per gli schemi standard sussistono esclusivamente due forme di definizione degli schemi, per gli schemi dell'ambiente cliente esistono varie nature di definizione (tutte riconoscibili dai differenti prefissi). Va però notato, che la maggiore parte di queste nature esiste esclusivamente per recepire forme di definizione degli schemi sussistenti in passato, ma che oggi sono da considerarsi superate.
Fatta questa considerazione anche gli schemi creabili nell'ambiente cliente possiamo prendere in considerazioni esclusivamente due particolari nature :  gli schemi "S/" e gli schemi "Q/X".

Questi due forme di definizione degli schemi presentano gli stessi vantaggi degli schemi standard T/ e Q/ con queste differenze : 
* Gli schemi **"S/ - Da Script SCP_QRY"** invece che essere definiti nei file script SCP_NAV degli schemi T/ sono contenuti negli script SCP_QRY o SCP_QRYPER che dovranno essere definiti in una delle librerie di personalizzazione dell'ambiente cliente.
* Gli schemi **"Q/X - Da exit B£IQ2_xx_U"** invece si fondamento esattamente sulla stessa struttura degli schemi Q/ con la differenza di essere costruiti attraverso pgm di exit invece che dai pgm standard.

## Gestire uno schema "S/ - Da script SCP_QRY"

Questi schemi vengono definiti all'interno di uno script nel file SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).
Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN.
Quando si vuole quindi implementare un nuovo schema sarà innanzitutto necessario : 
* Verificare se esiste già uno file sorgente SCP_QRY nella libreria di personalizzazione dell'ambiente.
** In caso contrario crearlo (copia ad esempio quello della DEV)
** In caso affermativo verificando la presenza del sorgente corrispondente alla classe interessata (facendo le dovute considerazioni sul tipo/parametro)
** Se opportuno prendere in considerazione la possibilità di sfruttare le istruzioni dello script INC.SCP per includere in differenti script le stesse istruzioni
Fatto questo si può passare alla compilazione dello script. In questo senso è' importante notare che all'interno di questi script possono essere definiti, non solo gli schemi, ma anche tutte quelle informazioni utilizzabili poi nella costruzione di query in ambiente cliente. Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati alla definizione di uno schema. Possono essere catalogati come tali i seguenti tag : 

* SCH :  definisce uno schema
* SCH.FLD :  definisce una colonna dello schema
* G.SET.MAT :  definisce il o i setup della matrice

Per il tag SCH.FLD ricopre un ruolo particolarmente importante il nome della colonna :  indicando infatti in esso il nome di uno dei campi dell'archivio, o di un oav automaticamente verrà definito quale sarà il contenuto delle celle della colonna e come tale colonna va definita. L'intestazione, l'oggetto, la lunghezza, salvo vengano volutamente sovrascritte negli attributi del tag verranno automaticamente derivate dalla definizione del campo dell'archivio o dell'attributo.
Viceversa è possibile definire delle informazioni di differente natura, il cui codice può essere libero, ed i cui valori possono essere reperiti tramite l'applicazione di funzioni alle informazioni di base (costituite a loro volta dai campi del archivio di riferimento e dagli oav della classe). Sarà così possibile informazioni applicando formule quali decodifiche, attributi di attributi, formule SQL.

E' inoltre obbligatorio indicare sempre nello schema la colonna che identifichi l'istanza della classe di riferimento (es. per gli articoli il codice articolo). Tale identificazioni può avvenire alternativamente in questi modi : 
* Attribuendo come nome di colonna il codice speciale "K01"
* Attribuendo alla colonna per l'attributo TYP il medesimo valore "K01"
Si noti che nel caso la chiave corrisponda a più campi chiave è possibili indicarli in unica colonna tramite la funzione CNC (cioè CONCAT). Si faccia l'esempio per le righe di documento : 
SCH.FLD NAM(K01) FUN(CNC) PAR(R§NDOC,R§NRIG)

Per quel che riguarda l'utilizzo del G.SET.MAT, questo è opzionale ed in sua assenza verrà applicato come un default.
Quando invece sorge la necessità di aggiungere proprie specificità si ricordano queste considerazioni : 
* L'utilizzo degli attributi di raggruppamento ed ordinamento, vanno utilizzati con particolare attenzione in quanto su matrici con paginazione potrebbero produrre risultati ingannevoli se anche il caricamento dei dati non avviene secondo il medesimo criterio indicato in questi attributi.
* Di sfruttare il più possibile l'attributo Parent, che permette di riprendere una serie di attributi, con la possibilità di specificare solo quelli specifici dello schema. L'elenco dei parent è contenuto nello script di scheda J3_SET_STD. In particolare si citano  come valori di questo attributo i codici A01 (Matrice di default con raggruppamento) A08 (matrice di default senza raggruppamento e senza totali) ed A09 (matrice di default senza raggruppamento e senza totali).
* Va infine fatta questa considerazione in merito all'utilizzo delle funzioni :  le funzioni di decodifica e di oav (qualora derivati), quando non sono applicate alle istanze della classe le decodifiche risultano maggiormente vantaggiose dal punto di vista delle performance, se applicate tramite la funzionalità di setup delle colonne aggiuntive della matrice (si veda l'attributo "Formulas" del tag G.SET.MAT).Questo perchè in estrema sintesi, mentre le colonne aggiuntive applicano le funzioni alla DISTINCT dei codici presenti nella matrice, le funzioni le applicano ad ogni singola riga.
Si prenda questo esempio :  data una matrice con 300 articoli, in cui sono presenti 4 tipologie di articolo, per effettuare la decodifica del tipo articolo, se venisse usata la funzione DEC la routine di decodifica potrebbe essere eseguita 300 volte, mentre al contrario tramite la matrice di aggiornamento esclusivamente 4 volte.

Fa infine notato che dopo qualsiasi modifica allo script, per vederne l'effetto sarà necessario ricollegarsi o ricaricare l'ambiente.

## Gestire uno schema "Q/ - Da pgm B£IQ2_xx"

Questi schemi, come detto sono definiti attraverso il programma B£IQ2_XX. Eventuali differenze a livello di parametro sono gestite all'interno del B£IQ2_XX. Unica eccezione sono gli schemi su oggetti ID, in questo caso il pgm richiamato è il B£IQ2_IDxx, dove xx corrisponde alle prime due lettere del file. Le differenze per i vari file che corrispondono a tali iniziali sono gestite all'interno del pgm.

Gli schemi Q/ che possono essere aggiunti nell'ambiente cliente, possono esserlo implementando programmi secondo la seguente codifica fissa : 
* B£IQ2Ixx_U per gli oggetti ID (es. per IDCALANN0F creo B£IQ2ICA_U)
* B£IQ2_XX_U per tutti gli altri oggetti (es. per AR creo B£IQ2_AR_U)
* B£IQ2XXXXU per tutti gli oggetti ID non databases (es. per IDBRDISTDS creo B£IQ2CICLU)
Risulta inoltre necessario al fine di evitare la sovrapposizione con gli schemi dello standard, attribuire ai propri schemi codici con iniziale "X".

Di seguito viene riportato il link al sorgente di esempio delle exit ed ad al pgm di gestione degli schemi standard dei calendari.
 :  : DEC T(MB) P(SMESRC) K(B£IQ2_XX_U) D(Sorgente Pgm di Esempio) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£IQ2_IDCA) D(Sorgente Pgm Standard Gestione File che iniziano per CA) L(1)

Fra le istanze definibili a standard, di particolare rilievo è l'istanza avente codice Q/DFT. Se presente questo sarà lo schema utilizzato di default in tutte le query che non prevedono a loro volta uno schema di default specifico.

Va infine notato che dopo qualsiasi modifica ai pgm, per vederne l'effetto sarà necessario ricollegarsi o ricaricare l'ambiente.

### Gestire uno schema "T/ - Da script SCP_NAV"

Questi schemi vengono definiti esclusivamente per lo standard all'interno di uno script nel file SCP_NAV. Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN. NOTA BENE :  che esista o meno lo script di riferimento, per qualsiasi oggetto sussiste l'istanza **T/CD*** che identifica lo schema minimale dato da codice e descrizione.
Quando esistono, sono inoltre di rilievo le istanze : 
* T/DFT - Default, in assenza della compresenza di uno schema Q/DFT rappresenta lo schema di default di tutte le query che non prevedono a loro volta uno schema di default specifico.
* T/Q3 - Filtro, se indicato, identifica i campi che verranno presentati nella scheda di gestione del filtro di job
All'interno dello script i tag utilizzati sono tre : 

* SCH.SCH :  definisce lo schema
* SCH.FLD :  definisce una colonna
* G.SET.MAT :  definisce il setup della matrice

All'interno dei comandi SCH.FLD è necessario indicare quale colonna visualizzare; è possibile indicare il nome di un campo del file master per l'oggetto dello schema oppure una colonna aggiuntiva. Ad esempio il comando SCH.FLD Name="L5CDOC_" presenterà la descrizione del campo L5CDOC mentre il comando SCH.FLD Name="L5SOGG_I_05_I_T$V§PA" visualizzerà la regione a cui appartiene la provincia dell'ente. Nel caso in cui venga specificata una colonna aggiuntiva non è necessario adeguare il setup, questo verrà adeguato automaticamente dal programma.
E' inoltre possibile impostare il parametro ESql con cui è possibile indicare un'operazione sql il cui risultato verrà riportato nella colonna.
Esempio :  SCH.FLD Name="R5SAL" Txt="Saldo" ESql="R5IMPO-R5IMPA"
Il parametro  Hdd="1" farà in modo che la colonna sia nascosta.
Omettendo l'attributo Txt verrà ripresa di default la descrizione del campo del file.

E' inoltre obbligatorio indicare sempre nello schema la colonna che identifichi l'istanza della classe di riferimento (es. per gli articoli il codice articolo). Tale identificazioni può avvenire alternativamente in questi modi : 
* Attribuendo come nome di colonna il codice speciale "ID_LI"
* Attribuendo come nome di colonna il codice speciale "ID_OG"
Si noti che nel caso la chiave corrisponda a più campi chiave, non sarà necessario aggiungere ulteriori indicazioni. Per il solo fatto di identificare la colonna in questo modo, nelle sue celle verrano riportate tutte le chiavi pertinenti.

Va infine rilevato che sono previsti inoltre i seguenti codici speciali di colonna : 
* ID_DE, per gli oggetti che non appartengono ad archivi, identifica automaticamente la decodifica dell'oggetto (senza l'applicazione di colonne aggiuntive)
* ID_TP, identifica automaticamente una colonna nel cui contenuto verrà riportato fisso il codice della classe dell'oggetto.

Per quel che riguarda l'utilizzo del G.SET.MAT, questo è opzionale ed in sua assenza verrà applicato come un default.
Quando invece sorge la necessità di aggiungere proprie specificità si ricordano queste considerazioni : 
* L'utilizzo degli attributi di raggruppamento ed ordinamento, vanno utilizzati con particolare attenzione in quanto su matrici con paginazione potrebbero produrre risultati ingannevoli se anche il caricamento dei dati non avviene secondo il medesimo criterio indicato in questi attributi.
* Di sfruttare il più possibile l'attributo Parent, che permette di riprendere una serie di attributi, con la possibilità di specificare solo quelli specifici. In particolare si citano  come valori di questo attributo i codici A08 ed A09.

Va infine notato che dopo qualsiasi modifica allo script, per vederne l'effetto sarà necessario ricollegarsi o ricaricare l'ambiente.

## Forme obsolete di definizione degli schemi

Come accennato al punto precedente oltre a quelle descritte in precedenza, esistono varie modalità di definizione degli schemi che esistono solo per recepire modalità di definizione presenti in passato, ma ad oggi considerate ormai superate (mancando di varie funzionalità sussistenti nelle nuove strutture). Appartengono a questa categoria : 
* Gli schemi "I/" :   Vengono definiti tramite l'oggetto SP, che a sua volta è definito tramite la tabella INT. Avevano un forte utilizzo in 5250, mentre in loocup hanno lo svantaggio di non poter definire l'oggettizzazione delle colonne.

## Forme deprecate di definizione degli schemi

Come accennato al punto precedente oltre a quelle descritte in precedenza, esistono varie modalità di definizione degli schemi che esistono solo per recepire modalità di definizione presenti in passato, ma ad oggi considerate deprecate. Appartengono a questa categoria : 
* Gli schemi "P/" :   Questi schemi, vengono gestiti attraverso programmi aventi codice NomeFile_M dove Nome file indica il nome del file master dell'oggetto su cui la lista è definita senza il finale 0F. Questa forma è precedente all'implementazione degli schemi Q/ che di fatto ne hanno costituito una versione aggiornata.

## Sospendere/Ripristinare istanze e/o fonti di schema

Vista la molteplicità delle forme di schemi possibilità è stata prevista la possibilità attraverso un exit fissa, avente codice B£IQ5G_U, di poter disattivamente gli schemi o direttamente le fonti stesse degli schemi, secondo una proprio logica personale. Attraverso tale funzionalità è inoltre possibile ripristinare anche quelle forme di schema sono state ritenute deprecate. Si veda il sorgente del pgm B£IQRB che contiene nelle schiere l'elenco di tutte le fonti disponibili, con l'indicazione anche della caratteristica di deprecabilità, nonchè il sorgente di esempio dell'exit B£IQ5G_U).

 :  : DEC T(OJ) P(*PGM) K(B£IQRB)
 :  : DEC T(MB) P(SMESRC) K(B£IQ5G_U) I(Esempio Sorgente Exit B£IQ5G_U) L(1)




# Generalità

Le funzionalità dello schema possono essere applicate anche esternamente alla struttura delle query. Quindi un servizio generico che elenca un insieme di righe basate sulle istanze di una stessa classe può sfruttare le funzionalità degli schema.

Tali funzionalità si appoggiano alla /COPY £IQ2 ed alle istanze della classe Q2.
 :  : DEC T(MB) P(QILEGEN) K(£IQ2) L(1)
 :  : DEC T(OG) P() K(Q2) L(1)

# Utilizzo

Nel servizio di esecuzione gli schemi possono quindi essere utilizzati attraverso i seguenti richiami : 

* **Inizializzazione**, questo richiamo va eseguito una sola volta per ogni richiamo del servizio.
>     C                   EVAL      £IQ2FU='INZ'
     C                   EVAL      £IQ2ME=' '
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=ParametridiInput
     C                   EXSR      £IQ2


Nella funzione di inizializzazione i parametri di input possono essere vari e permettono di sfruttare varie funzionalità. Per un maggior dettaglio si rimanda alla documentazione della /COPY £IQ2.

* **Completamento**, questo richiamo va eseguito una sola volta per ogni richiamo del servizio.
>     C                   EVAL      £IQ2FU='CMP'
     C                   EVAL      £IQ2ME='SCH'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=ParametridiInput
     C                   EXSR      £IQ2


Nella funzione di completamento, vengono compilate gli attributi dei campi delle schema che non sono state esplicitamente indicate, risalendo alle caratteristiche del campo/attributo di riferimento (es. se non ho indicato nello schema la descrizione o la lunghezza del campo).

* **Griglia**, permette di avere in ritorno l'xml della griglia della matrice corrispondente alle colonne dello schema.
>     C                   EVAL      £JAX_AGRI_I
     C                   EVAL      £IQ2FU='FMI'
     C                   EVAL      £IQ2ME='EXB'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=Parametridiinput
     C                   EXSR      £IQ2
     C                   EVAL      £JAXCP=£IQ2OU
     C                   EXSR      £JAX_ADD
     C                   EVAL      £JAX_AGRI_F


* **Riga**, permette di avere in ritorno l'xml di una riga di matrice, avendo in input il record o il codice dell'oggetto di riferimento.
>     C                   EVAL      £IQ2FU='FMC'
     C                   EVAL      £IQ2ME='LOO'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2ID=CodiceOggetto
     C                   EVAL      £IQ2IN=RecordOggetto
     C                   EXSR      £IQ2
     C                   EVAL      £JAXCP=£IQ2OU
     C                   EXSR      £JAX_ADD


* Per le righe va però fatta anche la seguente considerazione :  se lo schema potrebbe essere completamente riconducibile ad una select SQL. In caso affermativo è possibile avere in restituzione la stringa di selezione corrispondente e tramite le funzionalità della £SQLD avere la query completa attraverso l'accesso SQL. Va però notato che lo schema potrebbe non essere riconducibile ad una select sql e che in questo caso, sarà necessario appoggiarsi alla succitata funzione di riga. Per verificare se uno schema è riconducibile ad una stringa SQL o meno è sufficiente verificare se a seguito della chiamata, che permette di avere indietro la select risulta vera la condizione riportata.

>     C                   EVAL      £IQ2FU='FMT'
     C                   EVAL      £IQ2ME='SQL'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=Parametridiinput
     C                   EXSR      £IQ2

      * Se mi è stato ritornato qualcosa verifico se tutti i campi sono stati risolti
>     C                   IF        £IQ2OU<>' '
     C                   DO        *HIVAL        $X
     C                   IF        £IQR2I($X)=' '
     C                   EVAL      *IN35=*OFF
     C                   LEAVE
     C                   ENDIF
     C                   EVAL      £IQ2C=£IQR2D($X)
     C                   IF        £IQ2CDI='1'
     C                   EVAL      *IN35=*ON
     C                   LEAVE
     C                   ENDIF
     C                   ENDDO
     C                   ENDIF


* **Setup**, associato allo schema può essere previsto un xml di setup. Per accodare quest'ultimo all'xml della matrice va eseguito il seguente richiamo (nella routine in cui viene costruito il setup della matrice, che se assente va aggiunto).
NOTA BENE :  è importante che nel programma in questione venga impostato un attributo Context che includa il codice dello schema stesso vista l'importanza che ricopre nella definizione delle colonne. Per questo è opportuno che nel contesto venga ad esempio accodata la stringa \Q2\CodiceSchema\.
>     C                   EVAL      £IQ2FU='FMS'
     C                   EVAL      £IQ2ME='EXB'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=Parametridiinput
     C                   EXSR      £IQ2
     C                   EVAL      £JAXCP=£IQ2OU


* **Popup**, associato allo schema può essere inoltre previsto anche un popup. Nel caso, quest'ultimo va accodato all'xml di popup ritornato dal servizio.

>      C                   EXSR      £JAX_APOP_I

       * [...]
>     C                   EVAL      £IQ2FU='FMP'
     C                   EVAL      £IQ2ME='EXB'
     C                   EVAL      £IQ2OG=ClasseOggetto
     C                   EVAL      £IQ2SC=CodiceSchema
     C                   EVAL      £IQ2IN=Parametridiinput
     C                   EXSR      £IQ2
     C                   EVAL      £JAXCP=£IQ2OU

       * [...]
>      C                   EXSR      £JAX_APOP_F

