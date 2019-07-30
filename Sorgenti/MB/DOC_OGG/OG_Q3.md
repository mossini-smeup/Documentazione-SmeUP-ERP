## Cos'è uno Q3

L'oggetto Q3 identifica i campi, i valori degli stessi e le modalità con cui devono essere applicati come filtri, all'interno di matrici di dati (nel senso matematico del termine) costituite da un elenco di righe facenti riferimento ad istanze della medesima classe (un elenco di articoli, di clienti, di movimenti di magazzino ecc.)

Il fatto di identificare tale insieme di dati in un oggetto permette vari vantaggi fra i quali : 
* Costruire ed utilizzare funzionalità di filtro in modo semplice e veloce
* Dare la possibilità di sfruttare questa possibilità su elaborazioni completamente differenti che hanno in comune il fatto di elaborare istanze della medesima classe.
* Rendere disponibile, come per tutti gli altri oggetti di smeup, una serie di funzionalità di base, fra cui la funzione di gestione che permette di inserire/modificare/cancellare istanza della classe.

## Il filtro di job
All'interno delle istanze dei filtri di una classe va fatta innanzitutto un'importante distinzione fra il così detto filtro di job e tutti gli altri filtri.

Il filtro di job è un'entità che esiste sempre per tutti le classi che fanno riferimento ad un archivio (es. esiste per gli articoli, ma no esiste per i valori fissi V2). L'istanza di Q3 che identifica questo particolare filtro è il filtro avente codice E/*JOB.  Attraverso il filtro di job è possibile filtrare l'elaborazione, in varie modalità, per qualsiasi campo dell'archivio di appartenenza (o se non per tutti per i campi che sono stati previsti nello schema avente codice T/Q3 della classe stessa).

Questo filtro può essere applicato a qualsiasi elaborazione con queste convenzioni : 
* La sua impostazione deve essere sempre richiamabile dalla funzione di lancio ed anche di esecuzione, se quest'ultima si esplicita con una funzionalità interattiva. Non è quindi convenuto che un'elaborazione possa impiegare questo filtro, senza che dalla stessa vi sia la possibilità di modificarne i valori.
* Il suo richiamo avviene normalmente attraverso l'utilizzo del tasto funzione F13 che viene visualizzato ed reso disponibile, appunto nelle funzionalità di lancio/esecuzione delle elaborazioni che ne fanno utilizzo.

Nella funzioni standard di richiesta parametri A08 o UIR, tramite attributo specifico è prevista la possibilità di attivare il tasto F13, mentre per l'attivazione/utilizzo all'interno del servizio di esecuzione si rimanda allo specifico capitolo di documentazione.

## I filtri delle query
A fianco del filtro di job possono essere creati una serie di filtri aggiuntivi che possono utilizzati essenzialmente nella struttura delle query (quindi non liberamente in qualsiasi servizio). Attraverso esso ad una query può essere associato un filtro di default che avrà la duplice possibilità di attivare la richiesta dei corrispondenti campi di filtro all'utente e contemporaneamente l'applicazione automatica di tali scelte al risultato.

Questi filtri vengono definiti all'interno di uno script nel file SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).
Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN.
Quando si vuole quindi implementare un nuovo schema sarà innanzitutto necessario : 
* Verificare se esiste già uno file sorgente SCP_QRY nella libreria di personalizzazione dell'ambiente.
** In caso contrario crearlo (copia ad esempio quello della DEV)
** In caso affermativo verificando la presenza del sorgente corrispondente alla classe interessata (facendo le dovute considerazioni sul tipo/parametro)
** Se opportuno prendere in considerazione la possibilità di sfruttare le istruzioni dello script INC.SCP per includere in differenti script le stesse istruzioni
Fatto questo si può passare alla compilazione dello script. In questo senso è' importante notare che all'interno di questi script possono essere definiti, non solo gli schemi, ma anche tutte quelle informazioni utilizzabili poi nella costruzione di query in ambiente cliente. Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati alla definizione di uno filtro. Possono essere catalogati come tali i seguenti tag : 

* QRY :  query - attraverso questo tag verrà definita la query. In tale tag è prevista l'indicazione filtro utilizzato dalla query attraverso l'attributo DftFlt
* FLT :  definisce un istanza di filtro
* FLT.FLD :  definisce il campo di filtro

Per il tag FLT.FLD ricopre un ruolo particolarmente importante il nome del campo :  indicando infatti in esso il nome di uno dei campi dell'archivio, o di un oav automaticamente verrà definito su quale informazione dell'istanza verrà applicato il controllo del filtro. L'intestazione, l'oggetto, la lunghezza, salvo vengano volutamente sovrascritte negli attributi del tag verranno automaticamente derivate dalla definizione del campo dell'archivio o dell'attributo.

Compilate queste informazioni, utilizzando la query nelle sezioni UQR (si veda il modulo LOSUIR) sarà automatica l'attivazione della richiesta all'utente dei campi di filtro e l'utilizzo degli stessi nel risultato della query.

 :  : DEC T(TA) P(B£AMO) K(LOSUIR) L(1)


## Utilizzo di un filtro di job in un servizio - generalità

Il filtro di job, è una funzionalità di filtro generico, applicabile a qualsiasi attributo di un certo oggetto.

Qualora la funzionalità del filtro di job sia attiva nella scheda è presentato il tasto funzione **F13**.

Tali funzionalità si appoggiano alla /COPY £IQ3, ed all'istanza E/*JOB della classe Q3.
 :  : DEC T(MB) P(QILEGEN) K(£IQ3) L(1)
 :  : DEC T(OG) P() K(Q3) L(1)

### Specifiche

La funzionalità del filtro di job è presente nelle query, ma può essere applicata in qualsiasi servizio generico che elenca un insieme di righe basate sulle istanze di una stessa classe.

Va innanzitutto detto che il richiamo dello stesso è disponibile inoltre nelle funzionalità di richiesta configurazione del modulo UIR. In questo modo già nella richiesta di configurazione del servizio è possibile predisporre il filtro.

Nel servizio di esecuzione il filtro di job può essere controllato attraverso la /COPY £IQ3,
attraverso i seguenti richiami : 

* **Inizializzazione**, viene verificato se il filtro è stato effettivamente impostato o meno. Questo richiamo va eseguito una sola volta per ogni richiamo del servizio.
>     C                   EVAL      £IQ3FU='CAR'
     C                   EVAL      £IQ3ME='VAL'
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3

      * Se è non è presente alcun campo di filtro si spegne un indicatore di riferimento
>     C                   IF        £IQR3I(1)=' '
     C                   EVAL      XINQ3=*OFF

      * Viceversa lo si accende e si inizializza il filtro
>     C                   ELSE
     C                   EVAL      XINQ3=*ON
     C                   EVAL      £IQ3FU='CTR'
     C                   EVAL      £IQ3ME='RECINI'
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3
     C                   ENDIF


* A seguire a seconda che le righe della selezione vengano accedute attraverso l'SQL o attraverso una scansione RPG è possibile : 
** SQL
*** E' necessario verificare se il filtro implica l'applicazione di una JOIN. In caso affermativo sarà necessario considerare la relativa JOIN nella propria SELECT.
*** E' necessario verificare se il filtro implica l'applicazione di una WHERE. In caso affermativo sarà necessario considerare la relativa JOIN nella propria SELECT.
** RPG
*** Eseguire per ogni riga letta tramite la scansione RPG il controllo della compatibilità del record rispetto al filtro.
** Comuni
*** Sia che la scansione sia RPG che SQL è necessario testare anche i filtri per attributo ed in questo caso è necessario eseguire una chiamata specifica alla £IQ3 per ogni instanza letta.

NOTA BENE :  si aggiunge che nel caso si renda opportuno è possibile forzare che in un particolare contesto il filtro venga ancora limitato ai soli campi dell'archivio, senza che vengano inclusi altri database e gli attributi calcolati. Per fare questo è necessario intervenire sul richiamo della gestione del filtro : 
* Se l'azione viene costruita tramite la funzione POP/F13 nel campo £IQ3IN deve essere passata la stringa Att(1) (es. £IQ3IN='Att(1)')
* Se invece era stato previsto un richiamo specifico alla scheda Q3 è necessario che in questa chiamata venga prevista fra i parametri di input il medesimo parametro (es. INPUT(Att(1))

* **Ritorno Stringa JOIN SQL**,
>     C                   EVAL      £IQ3FU='CARFMT'
     C                   EVAL      £IQ3ME='SQL_JOIN'
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3
     C                   EVAL      XJOIN=£IQ3OU


* **Ritorno Stringa WHERE SQL**,
>     C                   EVAL      £IQ3FU='CARFMT'
     C                   EVAL      £IQ3ME='SQL'
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3
     C                   EVAL      XWHERE=£IQ3OU


Entrambe le funzioni, tornano la variabile £IQ3OU nel caso la condizione non sussista.

* **Controllo del singolo record per i campi del file**,
>     C                   EVAL      £IQ3FU='CTR'
     C                   EVAL      £IQ3ME='RECCHK'
     C                   EVAL      £IQ3ID=CodiceOggetto
     C                   EVAL      £IQ3IN=DSdelRecord
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3


* **Controllo del singolo record su filtri per attributi**,
>     C                   EVAL      £IQ3FU='CHK'
     C                   EVAL      £IQ3ME='FLT'
     C                   EVAL      £IQ3ID=CodiceOggetto
     C                   EVAL      £IQ3IN=DSdelRecord
     C                   EVAL      £IQ3OG=ClasseOggetto
     C                   EVAL      £IQ3FL='E/*JOB'
     C                   EXSR      £IQ3


Entrambe le funzioni, tornano l'indicatore 35 acceso quando l'istanza non supera le condizioni previste dai filtri.

Inoltre si aggiunge che volendo ottimizzare l'esecuzione di tali controlli, è possibile attraverso quando riportato a seguire verificare se esistono o meno filtri sul campo dei file o sugli attributi. Queste istruzioni vanno eseguite dopo la funzione CTR/RECINI.
>     C                   CLEAR                   XIN               1
     C                   CLEAR                   XAT               1
     C                   DO        *HIVAL        $X                5 0
     C                   IF        £IQR3I($X)=' '
     C                   LEAVE
     C                   ENDIF
     C                   EVAL      £IQ3C=£IQR3D($X)
     C                   IF        £IQR3V($X)=' '
     C                   ITER
     C                   ENDIF
     C                   IF        £IQ3CDI='1'
     C                   EVAL      XAT='1'
     C                   ELSE
     C                   EVAL      XIN='1'
     C                   ENDIF
     C                   ENDDO

In questo esempio le variabili XAT e XIN mi permettono rispettivamente di comprendere se sono attivi filtri su attributi (per i quali dovrò eseguire la chiamata CHK/FLT) o filtri su campi (per i quali dovrò eseguire la chiamata CTR/RECCHK).

Infine per aggiungere come popup di servizio sempre, la funzione di richiamo del filtro, tramite il tasto F13. Per questo nell'xml di popup va effettuato il richiesto che permette di avere in ritorno il relativo xml da accodare.

* **Invio xml popup F13**,
>      C                   EXSR      £JAX_APOP_I

       * [...]
>      C                   EVAL      £IQ3FU='POP'
      C                   EVAL      £IQ3ME='F13'
      C                   EVAL      £IQ3OG=Classe Oggetto
      C                   EVAL      £IQ3FL='E/*JOB'
      C                   EXSR      £IQ3
      C                   IF        £IQ3OU<>' '
      C                   EVAL      £JAXCP=£IQ3OU
      C                   EXSR      £JAX_ADD
      C                   ENDIF

       * [...]
>      C                   EXSR      £JAX_APOP_F

