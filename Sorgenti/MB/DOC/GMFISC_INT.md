# Generalità
L'obiettivo principale di questo modulo è quello di fornire situazioni valorizzate, di fine esercizio, della giacenza di magazzino (sintesi valorizzate).
Una tipica applicazione è la "Giacenza Fiscale di Fine Anno", valorizzata con le modalità previste dalla propria azienda : 

- _9_valorizzazione LIFO
- _9_valorizzazione FIFO
- _9_valorizzazione al COSTO(standard, ultimo di acquisto, etc.)


_2_ ATTENZIONE :  Se si ha una  valorizzazione del magazzino  per LIFO o FIFO è necessario  procedere  alla>GENERAZIONE SINTESI  DI MAGAZZINO ogni anno (le valorizzazioni LIFO /FIFO non danno risultati affidabili per periodi diversi dall'anno).

# Metodi di valorizzazione
In Sme.up sono possibili due metodi per ottenere queste sintesi : 

- _3_Attraverso chiusure periodiche dei magazzini (tipicamente chiusure di fine mese)

![GM_FISC_01](http://localhost:3000/immagini/GMFISC_INT/GM_FISC_01.png)Si ricorda che l'esecuzione di una chiusura periodica di magazzino non comporta un blocco della revisione dei movimenti, se si desidera bloccare la movimentazione bisogna manualmente inserire il blocco nella tabella B£4 con elemento *VMM o adottare un blocco attraverso date variabili.
 :  : DEC T(TA) P(B£4) K(*VMM)


- _3_Attraverso la ricostruzione della giacenza alla data di fine esercizio partendo dalla giacenza corrente

![GM_V001_02](http://localhost:3000/immagini/GMFISC_INT/GM_V001_02.png)
Nell'applicazione sono fornite tutte le funzioni per : 

- creare le sintesi di magazzino
- valorizzare le sintesi memorizzate (utilizzando diversi tipi costi e con diverse modalità di valorizzazione)
- stampare le sintesi valorizzate (le stampe possono essere anche usate ai fini fiscali)
- aggiornare i costi nell'archivio dei costi
- stampare i movimenti di carico / scarico magazzino nel periodo
- gestire manualmente i valori e le quantità memorizzati nelle sintesi di magazzino

Con quest'applicazione si possono anche gestire delle simulazioni (es. utilizzando diversi tipi costo), ogni simulazione può essere memorizzata separatamente a fronte di uno specifico scenario.
Sono fornite anche funzioni di massa per la gestione degli scenari (modifica, copia, cancellazione).

_2_Nota con questo modulo è anche possibile ottenere la valorizzazione di giacenze di articoli dettagliata per configurazione o per uno qualsiasi degli altri oggetti applicativi di Sme.up con cui si può caratterizzare una giacenza (UB = Ubicazione, LO = Lotto, D8 = Data registrazione, MT = Matricola, OP/OO/FA = Fase di cliclo di lavoro, CM = Commessa, EM =  Esponente di modifica, CF = Configurazione, CL/FO/CN = Ente, CC = Centro di costo, TA_UMS = Unità di misura esterna).

La valorizzazione per oggetto di riferimento pretende che nella tabella di personalizzazione della gestione materiali (GM1) sia attivata la funzione degli scenari in valorizzazione fiscale e che nella tabella degli scenari (GM3) sia attivata la gestione per oggetto di riferimento.

# Archivi utilizzati
 :  : DEC T(OJ) P(*FILE) K(GMSIAN0F)
 :  : DEC T(OJ) P(*FILE) K(IGREPT0F)

# Generazione sintesi di magazzino
Con  questa attività viene generato un archivio (>GMSIAN0F) che sintetizza,  per_3_PERIODO(solitamente l'ANNO) e_3_ARTICOLO(quantità in entrata e uscita) e relativo valore.
>N.B. :  la sintesi, per avere dati attendibili e confrontabili, deve essere  lanciata quando non vengono registrati movimenti di magazzino.
Accanto all'articolo è possibile definire un ulteriore >oggetto di riferimento (es. :  configurazione), definibile sullo scenario.

## Sintesi da chiusura periodica di magazzino
Ogni movimento di carico e scarico del magazzino, se ha valenza fiscale, viene classificato secondo la sua tipologia (es. :  i movimenti di traferimento tra un'ubicazione e l'altra non hanno valenza fiscale in quanto non modificano il saldo di magazzino e la tipologia di carico / scarico può essere versamento di acquisto, prelievo di produzione, rettifica inventariale, ecc...).

Ad ogni chiusura di magazzino tutti i movimenti effettuati, successivi alla chiusura precedente, vengono rilevati, classificati e sommarizzati algebricamente nell'archivio degli indici storici IGSTOR0F, dove  l'AREA, il TEMA e la SINTESI vengono recuperati dalla tabella GM1.

Dopo l'analisi e la validazione degli indici storici, un programma specifico costruisce la sintesi di magazzino relativa al nuovo esercizio, sommarizzando i dati raccolti nell'archivio "Indici storici" nell'esercizio in corso (cioè relativi alle chiusure periodiche successive all'ultimo esercizio chiuso).

## Sintesi da situazione giacenza
 - La funzione costruisce la sintesi del nuovo periodo, partendo dalla giacenza attuale ed elaborando a ritroso tutti i movimenti di magazzino relativi alle aree di giacenza con rilevanza fiscale fino alla data di fine esercizio. Se alla fine dell'esercizio la giacenza risulta superiore all'esercizio precedente, la differenza viene riportata come carico del periodo oppure come scarico.
 - La prima operazione è la ricostruzione della foto giacenza alla data di fine esercizio e l'operazione successiva consiste nella sintesi della giacenza a livello articolo. La parte ulteriore di elaborazione è la stessa della costruzione sintesi da giacenza.
La costruzione sintesi da foto è necessaria quando si voglia valorizzare il magazzino per articolo / altro oggetto di riferimento (es. :  per articolo / configurazione).

## Creazione Sintesi
Le sintesi possono essere generate per>Scenari diversi, consentendo, ad esempio, di gestire oggetti di riferimento diversi o aree di aggregazione dei movimenti diverse.
L'opzione >MULTISCENARIO è attivabile dalla Tabella GM1 e, in caso contrario, viene assunto come scenario di default l'elemento '*'.
 :  : DEC T(TA) P(GM1) K(*)

Per ottenere questa sintesi bisogna quindi : 
 * verificare  che nella tabella GM3 esista l'elemento >'*' di default e, se previsto, creare altri scenari
 :  : DEC T(TA) P(GM3) K(*)
 :  : DEC T(ST) K(GM3)

 * creare tipo costo da utilizzare nella generazione della Sintesi
 :  : DEC T(ST) K(TCO)

 * creare periodo per la generazione della Sintesi
 :  : DEC T(ST) K(PER)

 * accedere alle voci di menu e selezionare quella prevista dalla propria gestione : 
 ** Creazione Sintesi magazzino da chiusura
 ** Creazione Sintesi magazzino da giacenza attuale

Dopo essere stata generata, la Sintesi di magazzino può essere gestita per eventuali modifiche.

# Stampa e valorizzazione sintesi
 La Valorizzazione Fiscale si ottiene valorizzando la Sintesi di magazzino.
 Tale Valorizzazione è possibile in due forme : 
 * >VALORIZZAZIONE SEMPLICE(produce solo una stampa del magazzino valorizz.)
 * >VALORIZZAZIONE ESTESA  (consente la stampa, visualizzazione o trasf. PC)

La valorizzazione della sintesi è possibile per Scenario/Magazzino Fiscale  e Periodo. _7_La valorizzazione non viene memorizzata in alcun archivio.

E' possibile selzionare se il metodo di valorizzazione deve essere_9_LIFO, _9_FIFOo a_9_COSTO MEDIO.In questo ultimo caso è possibile selezionare il Tipo costo da utilizzare.
 :  : DEC T(ST) K(TCO)

Con lo stesso archivio di Sintesi di magazzino è possibile ottenere diversi  metodi di valorizzazione fiscale, per eventuali diversi Guppi fiscali. Tali Gruppi sono definiti attraverso  l'oggetto di raggruppamento dello Scenario (un attributo dell'articolo).
