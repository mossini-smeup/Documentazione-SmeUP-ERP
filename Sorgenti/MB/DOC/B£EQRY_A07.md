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

