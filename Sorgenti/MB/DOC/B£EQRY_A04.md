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

