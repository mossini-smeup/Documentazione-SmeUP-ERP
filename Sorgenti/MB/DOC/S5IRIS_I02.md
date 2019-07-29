# Proposta di approccio
Suggerirei di fare subito la memorizzazione.
Poi fare dal B£BCD09 in avanti, per lanciarlo in 5250 cablando provvisoriamente la sessioine
al suo interno.
In questo modo si può provare il tutto in 5250  (soprattutto i tempi) e posticipando
la realizzazione di B£BCD08 di scelta sessione (da fare solo in grafica)

# Attività
Aggiungere l'ambiente alla tabella B§G.
E' un campo obbligatorio?
E' un campo libero oppure un elemento di tabella (ad esempio *CN/??)

Creare il file B£BCDM0F
Decidere i suoi logici.

Impostare in numeratore delle sessioni in CRN

Creare le /copy delle procedure per leggere e scrivere

Variare £BCDD1 :      (OK)
mettere N.sessione e Flag se interrogazione  (OK  £BCDNS  e £BCDTS)

In B£BCD02 :  clear dei due nuovi campi, e al puntatore 7 (%07) impostare il valore del flag
            interrogazione, che poi verra' testato nello script INT   IF(%07)

Nuovo pgm B£BCD08 di lancio (scelta sessione)
Nuovo pgm B£BCD09 che riceve la sessione, riempie le DS standard (£BCDDxxxx)
imposta sessione e flag interrogazione
Modifica S5SMIN per leggere S5X e S5B da file e non da tabella.
Modifica script INT per lancio se interrogazione : 
Nuovo pgm di caricamento memorie da file :  S5SMES_I1 per DS standard (per ora non mongolfiere
non standard)

Nuovo pgm XXXXXXX da lanciare dal programma S5SMES_25 per memorizzare DS Standard (per ora non
mongolfiere non standard :  serve un'exit)

Modifica PAR_SCP per gestione di nuovi parametri che gestiranno modalità salvataggio/interrogazione

Se interrogazione : 
Modifica S5SMES_D3 per impedire rischedulazione e salvataggio, e per portare in finestra a destra
i dati della S5X che si sta interrogando.

Modifica di S5SMES_D4 per impedire spostamenti e azioni (congelamenti, forzature, scongelamenti e
sforzature, rischedulazioni, salvataggi, ecc) e, se fosse possibile, riportare la situazioine delle
quantità residua attuale del S5IRIS (che potrebbe anche non esserci più). Capire come.
NB :  impedire azioni globali di congelamento a un istante.

Modifica di S5SMES_P4 (POPUP del D4) :  togliere le azioni di modifica, comprese quelle del gruppo
temporaneo (vedere bene se il batch è compreso)


Elenco programmi con mongolifiere standard che sono usate in interrogazione.
NB :  per ciascuno ho elencato la condizione di PAR_SCP per eseguirli

INDICI ***** FATTO *********************************************************************************
Programma S5SMES_20
Memoria :  schiere XXNUMW e XXESCL
Per provare si potrebbe, all'inizio,dopo aver ripristinato le memorie (indici compresi),
rilanciare S5SMES_20 che li ricalcola.
Il problema è che S5SMES_20 li calcola, li memorizza, li mostra me non li ritorna.
Si potrebbe aggiungere una funzione che torna le due schiere (magari anche la descrizione).
In questo modo si potrebbe aggiungere (provvisoriamente) un pgm che, dopo il ripristino degli indici
- richiama S5SMES_20 per farseli ritornare (sono quelli memorizzati) e li salva come OLD
- richiama S5SMES_20 per calcolarli
- richiama S5SMES_20 per farseli ritornare (sono quelli ricalcolati)
- confronta gli indici OLD con quelli calcolati (la cosa più veloce è stamparli)
NB :  non l'ho ancora visto bene, ma la funzione di ritorno degli indici potrebbe essere utile anche
nell'UNDO, per confrontare due schedulazioni diverse.

ANALISI MATERIALI
Programma S5SMES_40
Condizione (£BCDIM : 17 : 10)<>' '
Memorie :  DSMATE_1, DSMATE_2, DSMATE_3,
Memorizzare anche XXNUME. Se XXNUME<=30000 solo DSMATE_1, se XXNUME<=60000 anche DSMATE_2
se maggiore, anche DSMATE : _3 (lo si vede dalla procedura PR_OCMAT). Adesso non servirebbe più queso
marchingegno in quanto il limite dei 30000 è superato :  ci sentiamno di modificare il programma?

RISORSE SECONDARIE
Condizione (£BCDIM : 58 : 1)<>' ' OR (£BCDIM : 63 : 1)<>''
Programma S5SMES_47
Memorie :  schiere SVDISP (piena per SV$D) e SVORD (piena per SV$O)

RSV ....
Programma S5SMES_76
Condizione :  (£BCDIM : 109 : 1)='1'
Memorizzare direttamente le schiere X2CORS, X2CDOG e X2PGML (tutte :  sono di XXNELE elementi).
Bisogna poi memorizzare le DS di S5SMES_77x, in base alla schiera X2PGML. Occorre vedere bene
il prefisso del
Programma S5SMES_77
DSPINT estensione di DSDEGR (prima pulirlo all'interno del 77)   *
. in write memorizzarlo se primo campo non a zero
DSINTR riempito per NRINTR                                       *
DSOCRS riempito per NROCRS                                       *
DSIORS riempito per NRIORS                                       *
DSXRSC estensione di DSIORS                                      *

****************************************************************************************************

CROR MODIFICATI
Programma S5SMES_22        (DA TESTARE)
Condizione (£BCDIM : 107 : 1)<>' ' OR (£BCDIM : 109 : 1)='1'
Memoria :  DSIMIN (non serve il riempimento in quanto è un'estensione orizzontale di DSIRIS)

VPP esterno
Programma S5SMES_65        (FATTO)
Memoria :  DSVINC (non serve il riempimento in quanto è un'estensione orizzontale di DSDEGR)
Vedere bene se farlo :  c'è solo il flag se VPP fisso. Cambia però la forma della cella...)

NUMERI RISORSA
Programma S5SMES_75        (OK)
Memoria :  DSXRIS (non serve il riempimento in quanto è un'estensione orizzontale di DSRISO)
Vedere se memorizzarli :  servono solo nel 31 di presentazione memorie. Il calcolo indici (20) li
calcola di suo :  sì memorizzarlo

AZIONI SU GRUPPO DI TIRO ... mah ... vedere se il D4 lo presenta ....
Programma S5SMES_62        (DA TESTARE)
Impostazioni XMDVSCE :  è nell'F17 del D4 (farlo sempre?)
Memoria :  DSIMIN (non serve il riempimento in quanto è un'estensione orizzontale di DSIRIS)
Per sicurezza, quando si memorizza la DS, se *IN01 è OFF eseguire prima la COSMEM che la
costruisce

MULTIPOSTAZIONE E PARALLELISMO RIGIDO
Programma S5SMES_73        (FATTO)
Condizione £BCDFL(3)<>'' multipostazione
Memoria :  DSISTA (non serve il riempimento in quanto è un'estensione orizzontale di DSIRIS)
Condizione £BCDFL(4)<>'' parallelismo rigido
Memorie :  DSXRIS (non serve il riempimento in quanto è un'estensione orizzontale di DSRISO)
         DSXIRI (non serve il riempimento in quanto è un'estensione orizzontale di DSIRIS)

MFP ... per ora sospesa ...


****************************************************************************************************

BATCH
Programma S5SMES_50        (FATTO)  :  In SVI si usa la B§G -> BCH
Condizione (£BCDIM : 61 : 1)<>' '
Memoria :  DSBATC (non serve il riempimento in quanto è un'estensione orizzontale di DSIRIS)



S5SMES_T1 :  vedere come impostare l'istante di partenza (deve essere letto e non calcolato...)
Memorizzare e ritornare l'ora....
Funzione 'RIT'  (OK)
la usano
S5SMES_DF
S5SMES_DH
S5SMES_DM
S5SMES_D3
S5SMES_D4
S5SMES_D5
S5SMES_D9
Far vedere la data ora di lancio nel D3? Adesso dove usa questo istante?

