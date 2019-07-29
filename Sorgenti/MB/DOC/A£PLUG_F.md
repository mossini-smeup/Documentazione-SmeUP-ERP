# PLUG_UP - Sme.up Master
## SCOPO
Lo scopo di PLUG_UP è quello di : 

- proporre un modello Smeup semplice e generico;
- semplificare e far risparmiare tempo durante una nuova installazione.

Questo modello contiene delle parametrizzazioni assunte e preimpostate, molte delle quali sono spesso comuni a tutte le installazioni.

L'obiettivo di questo modello, oltre al vantaggio di poter partire da un ambiente pulito e funzionante, è quello di proporre delle convenzioni  di nomenclatura che, seppur discutibili, aiutano molto nella fase di lettura e di scambio di informazioni del modello stesso.

Sono contenuti nel contempo consigli e step da seguire per un'ottima installazione.

# POTENZIALI UTILIZZATORI
Gli utilizzatori di questo modello potrebbero essere : 

-  collaboratori che devono partire con clienti piccoli ai  quali  può far piacere trovare una modellizzazione preimpostata;
- collaboratori che devono partire con nuovi clienti e vogliono utilizzare alcune logiche preimpostate e utilizzare comunque un ambiente tabellare, ridotto ai minimi termini;
- collaboratori alle prese per le prime volte con Smeup, ai quali è utile sicuramente utilizzare logiche e procedure già collaudate.

# FUNZIONI E PROCESSI COPERTI
Per capire il modello di fabbrica che si informatizza con plug-up bisogna cominciare dalle aree di giacenza considerate. Infatti queste definiscono i luoghi dove puo' trovarsi il materiale e quindi le movimentazioni.
Date le movimentazioni  si possono individuare i processi che le eseguono (es. versamenti interni o spedizioni/ricevimenti, ...).

In questo modello base ci sono le seguenti aree (leggere help di  singolo elemento per capirne il significato)
 :  : DEC T(ST) K(GMR)
I tipi giacenza trattati sono : 
 :  : DEC T(ST) K(GMQ)

Quindi,  se  ne  deduce  che  l'azienda  qui  descritta esegue i seguenti processi logistici (documentati in modo specifico nel proseguio) : 

## CICLO INTERNO

- Collaudo materiali con esitazione dei lotti che segrega il materiale scartato nell'area "Scarto" ed i non conformi nell'area "non conformi"
-  Produzione, con 2 tipi ordine, uno che scarica gli impegni al versamento (tecnica Backflush) e l'altro che invece richiede lo scarico manuale dei documenti.

## CICLO ATTIVO

- Spedizione per vendita da documento (Ordine)
- Vendita a valore senza documento (Libera)
- Lavorazioni per clienti su materiali da loro forniti (C/to lavoro Att.)
- Ricevimento di resi cliente
- Ricevimento da Cliente di materiale in garanzia
- Spedizioni  a  Clienti di materiale proprio (C/to vis., etc)
- Ricevimento da Clienti di materiale in C/to visione, deposito

## CICLO PASSIVO

- Acquisto di materia prima
- Acquisto di lavorazioni parziali (C/to lavoro di fase)
- Acquisto di trasformazioni totali (C/to lavoro pieno)
- Spedizione in c/to garanzia verso fornitori
- Spedizioni  a  Fornitori di materiale proprio (C/to vis., etc)
- Ricevimento da Fornitori di materiali in C/to visione

## DATI DI BASE
L'azienda in oggetto ha l'anagrafica articoli, con 2 soli tipo articolo, uno gestito a magazzino e uno no (generico),
 :  : DEC T(ST) K(BRA)
e con una scheda tecnica semplicissima (un parametro solo).

I cicli sono composti solo di operazioni, senza testate. Sono gestite le operazioni base (tipo ciclo OPE)

Le risorse sono solo di tipo CDL
 :  : DEC T(ST) K(BRR)

Ci sono  solo tre (3) tipi distinta :  ART (base), PRO (ordine produzione), ROP (righe ordini passivi).
 :  : DEC T(ST) K(BRL)

Non sono gestite le matricole.
Non sono gestite le commesse.
Non sono gestite le risorse produttive secondarie.

### FLUSSO GESTIONE COLLAUDO MATERIALI
Il Collaudo materiali con esitazione dei lotti segrega il materiale scartato nell'area "01 Scarto" ed i non conformi nell'area "02 Non conformi".
Il Collaudo è previsto sia per le forniture esterne che per le forniture interne.

La gestione dei Lotti per articolo dipende dalla Classe funzionale ad esso assegnata.

Sono state introdotte 3 classi funzionali dell'articolo :  **, CF-1, CF-5. Le classi funzionali sono gestite nella tabella CQQ : 
 :  : DEC T(ST) K(CQQ)
 :  : DEC T(TA) P(CQQ) K(**) I(CLASSE FUNZIONALE >>)
 :  : DEC T(TA) P(CQQ) K(CF-1) I(CLASSE FUNZIONALE >>)
 :  : DEC T(TA) P(CQQ) K(CF-5) I(CLASSE FUNZIONALE >>)

All'atto del ricevimento, per gli  articoli  a cui è  stata  assegnata la  _9_Classe funzionale : 

- _9_**   non si crea alcun lotto
- _9_CF-5 si crea un lotto in free pass
- _9_CF-1 si crea un lotto con campionamento I-2A (Tabella CQP)

La_9_Classe funzionale viene  assegnata ad un articolo o attraverso la sua >Classe articolo(Tabella CLS), oppure, se l'articolo non ha alcuna>Classe articolo, viene assunta la_9_Classe funzionaledi default_9_**.

Nella>Classe articolodi default ,>**,è  stata  associata  la_9_Classe funzionale **, per cui se si assegna agli articoli la>Classe articolo '**', per ogni articolo non vengono creati lotti .
 :  : DEC T(TA) P(CLS) K(**) I(CLASSE ARTICOLO >>)

La tabella  che  sovrintende al_3_movimento dei materialirelativamente alla Gestione qualità è la CRP : 
 :  : DEC T(ST) K(CRP)

_7_IMPORTANTE :  l'impianto tabellare è predisposto per far sì che il passaggio dall'area  collaudo  avvenga solo per gli articoli che creano un lotto con piano di collaudo diverso da free pass.

 _7_Pertanto, se non si assegna nessuna  Classe funzionale particolare, l'area collaudo non viene toccata !

_2_DICHIARAZIONI DI COLLAUDO
L'esito del collaudo è influenzato dal_5_TIPO LOTTO, tabella CQL. (Nota :  l'esito esiste solo se esiste il lotto e non è in free pass!)
 :  : DEC T(ST) K(CQL)

I Tipo Lotto creati sono : 
 :  : DEC T(TA) P(CQL) K(**) I(Tipo Lotto >>)
 :  : DEC T(TA) P(CQL) K(AC) I(Tipo Lotto >>)
 :  : DEC T(TA) P(CQL) K(PR) I(Tipo Lotto >>)

I lotti di acquisto vengono assegnati al flusso tramite il tipo Riga della Bolla di ingresso materiali (Tabella V5BDP). Esempio : 
 :  : DEC T(TA) P(V5BDP) K(001) I(Tipo riga >>)

I lotti di produzione vengono assegnati al flusso tramite il tipo Ordine di Produzione nella Tabella P5T. Esempio : 
 :  : DEC T(TA) P(P5T) K(101) I(Ordine di Produzione >>)

- Per i_5_lotti di acquistol'attività di esitazione scarica l'area 00 di collaudo e carica : 
-- l'area 10 con la qty conforme,
-- l'area 02 con la qty non conforme,
-- l'area 01 con la qty scarto.

 :  : DEC T(TA) P(CRP) K(AC)

- Per i_2_lotti di produzione, che solitamente non vengono mai caricati nella area di collaudo, l'esitazione scarica l'area 10 solo per le qty scarto e non conforme, caricando le aree 01 e 02 rispettivamente. (NOTA :  sempre e solo se esiste il lotto ed è NO free pass!)

 :  : DEC T(TA) P(CRP) K(PR)

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(00) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(01) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(02) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)

### FLUSSO PRODUZIONE INTERNA
Gli Ordini di produzione vengono inseriti manualmente. Il versamento di produzione viene anch'esso fatto manualmente attraverso le attività sotto elencate. Il prelievo viene fatto manualmente o in automatico a seconda del Tipo di Ordine di produzione, e quindi di Tipo impegno materiali.
I documenti del Ciclo interno sono i seguenti : 
 :  : DEC T(TA) P(P5T) K(101) I(Ordine Produzione con Prelievo componenti al Versamento >>)
 :  : DEC T(TA) P(P5T) K(102) I(Ordine Produzione con Prelievo Manuale dei componenti   >>)
 :  : DEC T(TA) P(P5T) K(301) I(Ordine Produzione per Rilavorazione                     >>)

Le attività di versamento sono contenute nell'elemento MOVPRO della tabella B£H.
 :  : DEC T(TA) P(B£H) K(MOVPRO)
 :  : DEC T(ST) K(B£JGM)
 :  : DEC T(TA) P(B£JGM) K(P0005) I(Versamento produzione            >>)
 :  : DEC T(TA) P(B£JGM) K(P0010) I(Versamento + prelievo manuale    >>)
 :  : DEC T(TA) P(B£JGM) K(P0015) I(Versamento + prelievo automatico >>)

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(00) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(01) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(02) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)

### FLUSSO VENDITE /SPEDIZIONE  MATERIALI
La gestione  del VENDITE e SPEDIZIONE materiale prevede le seguenti attività : 

- Inserimento >PREVISIONE di vendita con : 

 :  : DEC T(TA) P(V5D) K(PA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5APA) K(001) I(Modello documento Tab.V5APA >>)
 :  : DEC T(TA) P(V5APA) K(051) I(Modello documento Tab.V5APA >>)
se vendita normale
 :  : DEC T(TA) P(V5BPA) K(001) I(Tipo Riga         Tab.V5BPA >>)
se vendita a valore
 :  : DEC T(TA) P(V5BPA) K(003) I(Tipo Riga         Tab.V5BPA >>)
se omaggio
 :  : DEC T(TA) P(V5BPA) K(002) I(Tipo Riga         Tab.V5BPA >>)

- Estrazione>ORDINE di venditada Previsione con : 

 :  : DEC T(TA) P(V5D) K(OA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5AOA) K(001) I(Modello documento Tab.V5AOA >>)
 :  : DEC T(TA) P(V5AOA) K(051) I(Modello documento Tab.V5AOA >>)
se vendita normale
 :  : DEC T(TA) P(V5BOA) K(001) I(Tipo Riga         Tab.V5BOA >>)
se vendita a valore
 :  : DEC T(TA) P(V5BOA) K(003) I(Tipo Riga         Tab.V5BOA >>)
se omaggio
 :  : DEC T(TA) P(V5BOA) K(002) I(Tipo Riga         Tab.V5BOA >>)
 :  : DEC T(TA) P(V5GCA) K(CA002) I(Flusso attività   Tab.V5GCA >>)
 :  : DEC T(TA) P(V5GCA) K(CA004) I(Flusso attività   Tab.V5GCA >>)

- Generazione>BOLLA spedizione materialea Cliente per vendita con : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(001) I(Modello documento Tab.V5ADA >>)
se vendita normale
 :  : DEC T(TA) P(V5BDA) K(001) I(Tipo Riga         Tab.V5BDA >>)
se vendita a valore
 :  : DEC T(TA) P(V5BDA) K(003) I(Tipo Riga         Tab.V5BDA >>)
se omaggio
 :  : DEC T(TA) P(V5BDA) K(002) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA102) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede lo scarico del materiale dall'area 10 'Magazzino Centrale'

- Inserimento>BOLLA libera a valoreper vendita a Cliente con : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(901) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(003) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA106) I(Flusso attività   Tab.V5GCA >>)
Essendo una gestione di materiale a valore, non viene movimentato alcun magazzino.

- Inserimento>BOLLA reso materialeda Cliente con : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(011) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(101) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA204) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede il carico del materiale in area 02 'Non Conforme'

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(02) I(Codice area >>)

### FLUSSO GESTIONE MATERIALE IN GARANZIA
La gestione del Materiale in Garanzia dei Clienti prevede le seguenti attività : 

- Inserimento>BOLLA ricevimento materialeda Cliente :  con

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(101) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(301) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA202) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede il carico del materiale in area 47 'Conto riparazione interno'.

- Estrazione >ORDINE riparazione materiale :  con

 :  : DEC T(TA) P(V5D) K(OP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5AOP) K(301) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BOP) K(012) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCP) K(?????) I(Flusso attività   Tab.V5GCA >>)
La registrazione dell'Ordine prevede la creazione di impegni.

- Generazione>BOLLA spedizione materialea Fornitore per riparazione da impegno ordine OP

  :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
  :  : DEC T(TA) P(V5ADP) K(301) D(Modello documento Tab.V5ADP >>) I(Modello documento Tab.V5ADP >>)
  :  : DEC T(TA) P(V5BDP) K(301) D(Tipo Riga         Tab.V5BDP >>) I(Tipo Riga         Tab.V5BDP >>)
  :  : DEC T(TA) P(V5GCP) K(CP305) I(Flusso attività   Tab.V5GCP >>)
 La registrazione della Bolla prevede lo scarico del materiale dall'area 47 e il carico dell'area 90 'Merce terzi c/o terzi' _2_e/o

- Emissione Ordine di Rilavorazione per riparazione materiale in sede

 :  : DEC T(TA) P(P5T) K(301) I(Tipo ordine       Tab.P5T >>)
 :  : DEC T(TA) P(P5I) K(P10) I(Impegno materiali Tab.P5I >>)

- Generazione>BOLLA ricevimento materialeriparato da Fornitore

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(302) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(302) I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP306) I(Flusso attività   Tab.V5GCP >>)
La registrazione della Bolla prevede lo scarico del materiale dall'area 90 e il carico dell'area 47.

- Generazione>BOLLA spedizione materialeriparato a Cliente :  o_9_in Garanzia, indicando_7_prezzo con Fattura(riparazione fuori garanzia)

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(103) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(302) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA206) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede lo scarico del materiale dall'area 47.

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(47) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(90) I(Codice area >>)

 * Manca flusso Spedizione  materiale a fornitore per riparazione
 * Manca flusso Ricevimento materiale da fornitore riparato

### FLUSSO MATERIALE IN PRESTITO D'USO
Questo flusso può essere usato di esempio per le movimentazioni di  materiali  di  terzi  presso  l'azienda, e per le movimentazioni di materiali dell'azienda presso terzi. Con "terzi" si intendono tutti i soggetti (es. fornitori, clienti) che interagiscono con l'azienda.

Per indicare la giacenza del materiale si usano : 

- area esterna, con tipo giacenza  "ente", quest'area  viene decrementata ad ogni ricevimento e incrementata a ogni spedizione (giacenza negativa = materiale da rendere al soggetto esterno, giacenza positiva = materiale che deve essere reso dal soggetto esterno)
- area interna, quest'area viene incrementata ad ogni ricevimento e decrementata ad ogni spedizione (giacenza positiva = materiale da rendere al soggetto esterno, giacenza negativa = materiale che deve essere reso dal soggetto esterno)

Le bolle di carico/scarico sono collegate dalla "gestione conti esterni a partita"  ed  i flussi prevedono il collegamento della bolla di scarico a quella di carico in questo modo con una stampa documenti V5 è anche possibile produrre un "registro di conto esterno".

Per i Flussi di prestito d'uso con_7_Fornitore, sono previste  le  seguenti attività : 

- Inserimento>BOLLA invio (carico) ns. materialea Fornitore con : 

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(401) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(401) I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP301) I(Flusso attività   Tab.V5GCP >>)
La  registrazione  della Bolla prevede lo scarico del materiale da area10 'Magazzino Centrale' ed il carico materiale in area 65 'Ns Proprietà presso Fornitori'

- Inserimento>BOLLA reso (scarico) ns. materialeda Fornitore con : 

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(402) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(402) I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP302) I(Flusso attività   Tab.V5GCP >>)
La registrazione  della Bolla prevede lo scarico  del materiale da area 65 ed il carico materiale in area 10.

- Inserimento>BOLLA entrata (carico) materialeda Fornitore con : 

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(403) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(403) I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP303) I(Flusso attività   Tab.V5GCP >>)
La registrazione della Bolla prevede il carico  del materiale nell'area 45 'C/to Visione interno'.

- Inserimento>BOLLA restituzione (scarico) materialea Fornitore con : 

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(404) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(404) I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP304) I(Flusso attività   Tab.V5GCP >>)
La registrazione della Bolla prevede lo scarico  del  materiale da area 45.

- Inserimento>BOLLA entrata (carico) materialeda Cliente con : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(101) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(201) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA202) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede il carico  del materiale nell'area 45 'C/to Visione interno'.

- Inserimento>BOLLA restituzione (scarico) materialea Cliente con : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(102) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(202) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA204) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede lo scarico  del  materiale da area 45.

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(65) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(45) I(Codice area >>)

### FLUSSO ACQUISTO/RICEVIMENTO MATERIALI
La gestione  del ACQUISTO e RICEVIMENTO materiale prevede le seguenti attività : 

- Inserimento>ORDINE di acquistocon : 

 :  : DEC T(TA) P(V5D) K(OP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5AOP) K(001) I(Modello documento Tab.V5AOP >>)
se acquisto normale
 :  : DEC T(TA) P(V5BOP) K(001) I(Tipo Riga         Tab.V5BOP >>)
se acquisto a valore
 :  : DEC T(TA) P(V5BOP) K(003) I(Tipo Riga         Tab.V5BOP >>)
se entrata omaggio
 :  : DEC T(TA) P(V5BOP) K(002) I(Tipo Riga         Tab.V5BOP >>)

- Generazione>BOLLA entrata materialeda Fornitore con : 

 :  : DEC T(TA) P(V5ADP) K(001) I(Modello documento Tab.V5ADP >>)
se entrata normale
 :  : DEC T(TA) P(V5BDP) K(001) I(Tipo Riga         Tab.V5BDP >>)
se entrata a valore
 :  : DEC T(TA) P(V5BDP) K(003) I(Tipo Riga         Tab.V5BDP >>)
se omaggio
 :  : DEC T(TA) P(V5BDP) K(002) I(Tipo Riga         Tab.V5BDA >>)

 :  : DEC T(TA) P(V5GCP) K(CP002) I(Flusso attività   Tab.V5GCP >>)
La registrazione della Bolla prevede il  carico del materiale dall'area 10 'Magazzino Centrale'

- Inserimento>BOLLA reso materialea Fornitore con : 

 :  : DEC T(TA) P(V5ADP) K(101) I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(101) I(Tipo Riga         Tab.V5BDP >>)

 :  : DEC T(TA) P(V5GCP) K(CP102) I(Flusso attività   Tab.V5GCP >>)
 :  : DEC T(TA) P(V5GCP) K(CP104) I(Flusso attività   Tab.V5GCP >>)
La registrazione della Bolla prevede lo scarico del materiale dall'area10.

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)

### FLUSSO GESTIONE C/TO LAVORO ATTIVO
La gestione del C/to lavoro attivo prevede le seguenti attività : 

- Inserimento>ORDINE c/to lavoro attivoper Cliente con : 

 :  : DEC T(TA) P(V5D) K(OA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(1..) I(Modello documento Tab.V5ADA -_7_MANCA>>)
 :  : DEC T(TA) P(V5BDA) K(2..) I(Tipo Riga         Tab.V5BDA -_7_MANCA>>)

- Inserimento>BOLLA ricevimento materialeda Cliente :  con

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(101) I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(201) I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA202) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede il carico del materiale in area 45 'Merce terzi c/o sede'.

- Generazione>BOLLA spedizione materialea Fornitore per lavorazione

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(3..) I(Modello documento Tab.V5ADP -_7_MANCA>>)
 :  : DEC T(TA) P(V5BDP) K(3..) I(Tipo Riga         Tab.V5BDP -_7_MANCA>>)
 :  : DEC T(TA) P(V5GCP) K(CP...) I(Flusso attività   Tab.V5GCP -_7_MANCA>>)
Nel caso vi sia solo materiale del cliente :  la registrazione della Bolla prevede lo scarico del materiale dall'area 45 e il carico dell'area 90 'Merce terzi c/o terzi'
se c'è anche materiale dell'azienda :  la registrazione della Bolla prevede lo scarico dei componenti dall'area10 e il carico dell'area 50 'C/Lavoro materiale'_2_e/o

- Emissione Ordine di Rilavorazione per riparazione materiale in sede

 :  : DEC T(TA) P(P5T) K(301) I(Tipo ordine       Tab.P5T >>)
 :  : DEC T(TA) P(P5I) K(P10) I(Impegno materiali Tab.P5I >>)

- Generazione>BOLLA ricevimento materialelavorato da Fornitore

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(302)   I(Modello documento Tab.V5ADP >>)
 :  : DEC T(TA) P(V5BDP) K(302)   I(Tipo Riga         Tab.V5BDP >>)
 :  : DEC T(TA) P(V5GCP) K(CP...) I(Flusso attività   Tab.V5GCP -_7_MANCA>>)
La registrazione della Bolla prevede lo scarico del materiale dall'area 90 e il carico dell'area 45, e, come sopra, l'eventuale scarico area 50.

- Generazione>BOLLA spedizione materialelavorato a Cliente : 

 :  : DEC T(TA) P(V5D) K(DA) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADA) K(102)   I(Modello documento Tab.V5ADA >>)
 :  : DEC T(TA) P(V5BDA) K(202)   I(Tipo Riga         Tab.V5BDA >>)
 :  : DEC T(TA) P(V5GCA) K(CA204) I(Flusso attività   Tab.V5GCA >>)
La registrazione della Bolla prevede lo scarico del materiale dall'area 45.

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(45) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(50) I(Codice area >>)
 :  : DEC T(TA) P(GMR) K(90) I(Codice area >>)

- Manca Ordine Cliente c/to lavoro
- Per il Ricevimento materiale cliente usato Documenti e Flusso per materiale in garanzia con fattura
- Manca Bolla  spedizione materiale a Fornitore
- Manca Flusso spedizione materiale a Fornitore
- Manca flusso Ricevimento materiale da fornitore lavorato
- Per la Spedizione materiale a cliente usato Documenti e Flusso per materiale in garanzia con fattura

### FLUSSO GESTIONE C/TO LAVORO PASSIVO
La gestione del C/TO LAVORO PASSIVO prevede le seguenti attività : 

- Inserimento>ORDINE di c/to lavoro passivocon : 

 :  : DEC T(TA) P(V5D) K(OP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5AOP) K(201) I(Modello documento Tab.V5AOP -_7_MANCA>>)
 :  : DEC T(TA) P(V5BOP) K(011) I(Tipo Riga         Tab.V5BOP -_7_MANCA>>)

- Generazione>BOLLA spedizione materialea fornitore con : 

 :  : DEC T(TA) P(V5D) K(DP) I(Tipo documento Tab.V5D >>)
 :  : DEC T(TA) P(V5ADP) K(201) I(Modello documento Tab.V5ADP >>)
per C/to Lavoro pieno : 
 :  : DEC T(TA) P(V5BDP) K(201) I(Tipo Riga         Tab.V5BDP >>)
per C/to Lavoro di fase
 :  : DEC T(TA) P(V5BDP) K(202) I(Tipo Riga         Tab.V5BDP >>)

 :  : DEC T(TA) P(V5GCP) K(CP202) I(Flusso attività   Tab.V5GCP >>)

_2_Movimentazione materiale

- Se lavorazione di fase, la registrazione della Bolla prevede il carico dell'assieme all'ultima fase nell'area 55 'C/Lavoro wip'
- Se lavorazione con componenti, la registrazione della Bolla prevede lo scarico dei componenti dall'area 10 'Magazzino Centrale' e il carico in area 50 'C/Lavoro'


- Inserimento>BOLLA ricevimento materialeda fornitore con : 

 :  : DEC T(TA) P(V5ADP) K(001) I(Modello documento Tab.V5ADP -_7_??>>)
per C/to Lavoro pieno : 
 :  : DEC T(TA) P(V5BDP) K(011) I(Tipo Riga          Tab.V5BDP >>)
 :  : DEC T(TA) P(V5L) K(R01)   I(Parametri C/lavoro Tab.V5L   >>)
per C/to Lavoro di fase
 :  : DEC T(TA) P(V5BDP) K(013) I(Tipo Riga          Tab.V5BDP >>)
 :  : DEC T(TA) P(V5L) K(R03)   I(Parametri C/lavoro Tab.V5L   >>)

 :  : DEC T(TA) P(V5GCP) K(CP...) I(Flusso attività   Tab.V5GCP -_7_MANCA>>)
La registrazione della Bolla prevede il carico dell'assieme  nell'area 10.

Le aree coinvolte sono quindi : 
 :  : DEC T(TA) P(GMR) K(10) I(Codice area >>)

- Manca Ordine Fornitore c/to lavoro
- Mancano Impegni c/lavoro su righe spedizione?
- Per il Ricevimento materiale cliente usato Documenti e Flusso per materiale in garanzia con fattura
- Per il Ricevimento materiale da Fornitore è stato usato modello Bolla Entrata da Fornitore
- Manca Flusso ricevimento c/lavoro da fornitore

# DEMAND PLANNING
Esiste il flusso HW10 che deve essere schedulato una volta sola ad inizio mese ( *MTHSTR) e
che esegue il calcolo delle previsioni con il metodo Holt Winters.
Questo metodo è ben documentato nella documentazione dinamica del modulo MP.
Il flusso HW10 crea, partendo dallo storico degli ultimi 24 mesi, la previsione per i prossimi 12 mesi.
Inoltre vengono creati gli indici £P1 dell'articolo che permettono anche di ottenere una scorta
statistica suggerita da inserire nel gruppo fonti dell'MRP contemporaneamente alla previsione Holt Winters. NOTA :  nel record mag/Articolo deve comparire il metodo £01 nel calcolo scorta !
## PIANIFICAZIONE
L' MRP è preceduto da un flusso (MRP-A) che lancia un flusso MPS di nome MP20
 :  : DEC T(ST) K(B£H)
che crea un piano di radice FC..... che copre un'orizzonte di 12 mesi . In questo piano viene caricato nella vista ORD tutto l'ordinato dei 12 mesi successivi. Viene ripresa la vista delle previsioni che sono state precedente calcolate con il metodo Holt Winters e che sono presenti
nella vista HW1 dell'ultimo piano con radice HW.
Viene eseguito il confronto con la vista delle forzature FOR con un operatore che sceglie tutto il contenuto di FOR se esiste il record , altrimenti sceglie tutto HW1 e mette in PRE.
A questo punto riprende l'ordinato corrente nella propria vista ORD e calcola il delta, se positivo, tra la vista PRE e la ORD , scrivendolo nella vista DEL.
Nel piano FC....., nella vista DEL ci sono le previsioni non consumate dall'ordinato corrente.
La fonte F10 (tabella M5F) considera poi questa vista e la include nel gruppo fonti dell'MRP in aggiunta agli ordini residui.

## MODULO DEI COSTI
### GESTIONE COSTI ARTICOLO
L'implementazione dei costi articolo prevede la gestione di 3 tipi costi e la loro memorizzazione su base annuale, sia per quanto riguarda gli articoli sia per quanto riguarda le aliquote dei centri di costo.
Non vengono gestite le ricariche dei costi e i costi alla fase.
Le procedure di calcolo sono quelle dei programmi standard : 
- [Calcolo costi](Sorgenti/MB/DOC/D0CALC)

- _2_Schede di costo. Le schede di costo utilizzate sono memorizzate nei sottosettori £C, £L e £Q della tabella IGI e i programmi standard di calcolo costi di Smeu.up si basano su queste sia in lettura sia in scrittura, quindi nel caso in cui i codici degli indici vengano cambiati occorrerà probabilmente creare dei nuovi programmi di calcolo.
- _2_Scheda articolo. La scheda dell'articolo suddivide i costi fra fissi e variabili e fra costi del livello e costi dei livelli inferiori; ognuno ha le seguenti componenti : 
-- Materiali
-- Lavorazioni esterne
-- Lavoro
-- Macchina
-- Attrezzaggio
-- Scarto

Sono inoltre presenti 3 costi industriali, 3 costi generali e 3 ricariche.

 :  : DEC T(ST) K(IGI£C) I(Scheda costo articolo Tab.IGI£C >>)

- _2_Scheda centri di costo. La scheda dei centri di costo presenta 6 aliquote : 
-- Lavoro variabile
-- Macchina variabile
-- Diversi variabili
-- Lavoro fisso
-- Macchina fissa
-- Diversi fissi

 :  : DEC T(ST) K(IGI£L) I(Scheda aliquote centri di costo Tab.IGI£L >>)

- _2_Scheda dei costi medi di acquisto. La scheda dei costi medi di acquisto ha le seguenti componenti : 
-- Quantità acquistata
-- Importo dell' acquistato
-- Quantità acquistata di conto lavoro
-- Importo dell'acquistato di conto lavoro
-- Costo medio
-- Costo medio di conto lavoro

 :  : DEC T(ST) K(IGI£Q) I(Scheda costi di acquisto Tab.IGI£Q >>)

- _2_Valorizzazione del ciclo. La tabella che determina come i tempi vengano moltiplicati per le varie aliquote e in che componente il costo debba essere salvato è la CSB (vedi help per la sua compilazione) e l'elemento utilizzato è DFT.

 :  : DEC T(ST) K(CSB) I(Struttura imp.aliquote Tab.CSB >>)
E' comunque possibile creare un altro elemento e scrivere le proprie logiche di calcolo senza dover personalizzare i programmi. Questo eventuale elemento andrà messo nella tabella TCO nel campo "Strut. attr. aliqu.".

_1_Modello del D0

-  _2_Contesti. La memorizzazione dei costi avviene sull'archivio D5COSO0F e quindi per la loro gestione occorre creare i contesti ed i temi adatti. Per gli articoli il contesto sarà AR mentre per i centri di costo sarà CC e i sottosettori dei loro temi sono stati tenuti separati : 

 :  : DEC T(ST) K(D5S) I(Contesti Tab.D5S >>)

- _2_Temi. I temi si sviluppano per tipo costo, permettendo in questo modo di poter gestire tutti i tipi costi che si vogliono, e per periodo di tipo A (anno) e entrambi, sia quello per gli articoli sia quello dei centri di costo, sono stati chiamati £01 e £02, in modo da poter utilizzare uno stesso tipo costo per entrambi gli oggetti, dato che nella tabella TCO si può specificare un solo tema.

 :  : DEC T(ST) K(D5OAR) I(Temi articolo Tab.D5OAR >>)
 :  : DEC T(ST) K(D5OCC) I(Temi centri di costo Tab.D5OCC >>)

- _2_Possibili variazioni. Nel caso in cui si volessero salvare i costi su base mensile bisogna cambiare il campo "Tipo periodo" da 'A' a 'P'.

Come numero di decimali visualizzati si è mantenuto il default di 2 (si ricorda che comunque per tutti i calcoli e le memorizzazioni avvengono con 6 decimali).
Se si volesse cambiarlo basta impostare il campo "Punti sep./decimali" con i valori desiderati (se si volesse cambiare l'impostazione solo su alcuni campi è possibile farlo impostando lo stesso campo negli elementi della tabella IGI che interessano).

- _2_Tipi costo. Tutti i tipi costo che si basano sulla valorizzazione del ciclo e della distinta esplodono la distinta di tipo ART e il ciclo di tipo ART. E' comunque possibile cambiare i tipi modificando i campi appositi nell'elemento della tabella TCO.

Sono stati creati i seguenti tipi costo : 
-- _2_ STD costo standard (- Articoli = Si - Centri di costo = Si). Viene di solito calcolato solo ad inizio anno e si basa su costi e aliquote di budget. Questo permette di avere un riferimento fisso durante tutto l'anno col quale per esempio calcolare i margini sulle vendite. E' anche il tipo costo impostato di default nella tabella D01 di parametrizzazione del modulo D0, cioè il tipo costo utilizzato nel caso in cui l'utente/programma non abbia specificato alcun tipo costo.
-- _2_CUR costo corrente (- Articoli = Si - Centri di costo = Si). E' un costo attuale che si basa sui costi realmente sostenuti, per quanto riguarda le materie prime, le lavorazioni esterne, quelle interne (tramite le aliquote) e i costi di struttura. Può essere calcolato quando si vuole e permette per esempio di vedere quanto i costi articoli si discostino dai costi standard previsti.
-- _2_MED costo medio acquisto (- Articoli = Si - Centri di costo = No). E' un costo creato dalla procedura "Situazione entrata fornitore". Contiene il totale degli importi e delle quantità acquistate sia per quanto riguarda le materie prime sia per le lavorazioni esterne ed i relativi costi medi. Può essere utilizzato per valorizzare il costo delle materie prime.
-- _2_LAE costo lavorazioni esterne (- Articoli = Si - Centri di costo = No). E' un costo dinamico che legge il listino 501/102 per Fornitore-Articolo-Fase. Serve per valorizzare le fasi del ciclo dichiarate esternamente o i materiali di conto lavoro pieno leggendo il costo dal listino del fornitore preferenziale dell'articolo. Per funzionare correttamente occorre che : 
--- sull'articolo sia presente il fornitore preferenziale
--- il listino abbia come valuta la valuta del fornitore preferenziale
--- nel caso di conto lavoro pieno la fase sia specificata come **

 :  : DEC T(ST) K(TCO) I(Tipi costo Tab.TCO >>)

- _2_Nature costo. Le nature costo rappresentano delle sintesi delle componenti di costo di un oggetto. Vengono fornite delle nature che rappresentano la maggior parte delle riaggregazioni di costo che si possono effettuare partendo dalla scheda costo standard. E' comunque possibile espandere a piacere questa tabella. In questa codifica il costo totale dell'articolo viene restituito dalla natura TC.

 :  : DEC T(ST) K(D0A) I(Nature costo Tab.D0A >>)

- _2_Livelli di costo. I livelli di costo sono obbligatori in quanto per recuperare univocamente un costo di un oggetto occorre fornire, oltre al tipo costo voluto, anche un livello di costo. I livelli implementati coprono molte delle possibili interrogazioni possibili. E' comunque possibile espandere a piacere questa tabella. In questa codifica il costo totale dell'articolo viene restituito dal livello 5, che di costo da utilizzare nel caso in cui l'utente/programma non abbia specificato alcun livello di costo.

 :  : DEC T(ST) K(D0B) I(Livelli di costo Tab.D0B >>)

- _2_Impostazioni di default. Nella tabella D01 sono presenti i valori di default che vengono utilizzati nel caso in cui l'utente/programma non abbia specificato dei valori obbligatori. Il tipo costo assunto è quello standard (STD), il livello assunto è quello del prezzo minimo di vendita (5).

 :  : DEC T(ST) K(D01) I(Parametrizzazione costi avanzati Tab.D01 >>)

- _2_Ricariche dei costi. In questo modello non vengono considerate eventuali ricariche dei costi. E' comunque possibile creare degli elementi (vedi help per aiuto sulla loro compilazione) che verranno automaticamente utilizzati nella procedura di calcolo costi.

 :  : DEC T(ST) K(CSR) I(Ricariche dei costi Tab.CSR >>)
 :  : DEC T(ST) K(CSA) I(Metodo attribuzione % Tab.CSA >>)

- _2_Lancio del calcolo. Nel programma di calcolo costi D0CA00G è stata creata una memorizzazione video di nome A0 con i parametri impostati per il calcolo del costo standard.Nel programma di situazione entrata fornitori è stata creata una memorizzazione video di nome A0 con i parametri impostati per il calcolo del costo medio di acquisto del 2005.

## INDICI QUALITATIVI
Gli indici per la valutazione dei processi aziendali sono divisi in 7 temi, contenuti in
 :  : DEC T(ST) K(D5OCN) I(TABELLA >>)
Ad ogni tema è associato un sottosettore della tabella IGI, i cui elementi sono gli indici ed i relativi parametri di calcolo.
Vengono qui di seguito descritte le sette tipologie di indici : 

### CUSTOMER SATISFACTION
La Customer Satisfaction è misurata mediante indici DINAMICI memorizzati nel _7_D5COSO, in particolare
 :  : DEC T(TA) P(D5S) K(CNCLI) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(Q06) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
Al tema_7_Q06sono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGIQ6) I(TABELLA >>)

Gli indici che concorrono a misurare la soddisfazione del cliente sono : 
 :  : DEC T(TA) P(IGIQ6) K(31) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(33) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(35) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(36) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(37) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(38) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ6) K(39) I(INDICE >>)
Il_9_Rispetto della data di consegna è dato dal rapporto, in percentuale, di
 :  : DEC T(TA) P(IGIQ6) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(03) I(PARAMETRO >>)
Per ogni ordine viene considerata la data di consegna confermata; un ordine può venire considerato puntuale anche se consegnato entro X giorni dalla data confermata (X parametro aggiuntivo).
La_9_Valutazione del ritardo medio di consegnaderiva da
 :  : DEC T(TA) P(IGIQ6) K(32) I(INDICE >>)
il quale è la media dei giorni di ritardo (considerando i soli giorni lavorativi) calcolata con
 :  : DEC T(TA) P(IGIQ6) K(04) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(02) I(PARAMETRO >>)
Tale dato non è utilizzabile nel calcolo dell'indice globale. Si utilizza quindi il pgm di calcolo_7_CQCAL_DIche mediante la funzione RITC associa all'indice calcolato un valore su base 0-100.
Le impostazioni sull'associazione RITARDO DI CONSEGNA - VALUTAZIONE RITARDO DI CONSEGNA si trovano in
 :  : DEC T(ST) K(IGV) I(TABELLA >>)
 :  : DEC T(ST) K(IGVQQ) I(SUBSETTORE >>)
 :  : DEC T(TA) P(IGVQQ) K(RITC) I(ELEMENTO >>)
La_9_Valutazione del tempo medio di risposta a clienteopera allo stesso modo :  utilizza il pgm di calcolo_7_CQCAL_DIe mediante la funzione RISC associa un valore numerico su base 100 al numero di giorni di
 :  : DEC T(TA) P(IGIQ6) K(34) I(INDICE >>)
Tale indicatore è ottenuto come media aritmetica di
 :  : DEC T(TA) P(IGIQ6) K(05) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(03) I(PARAMETRO >>)
La_9_Conformità alla quantità ordinatapuò essere calcolato sia a livello di ordini che di righe d'ordine e rileva le inesattezze di quantità consegnate al cliente. Si tratta di un rapporto percentuale fra
 :  : DEC T(TA) P(IGIQ6) K(06) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(07) I(PARAMETRO >>)
La_9_Conformità dell'ordinatoè il complemento a 100 della percentuale di resi da cliente per non conformità del prodotto; quest'ultima è calcolata come rapporto, in percentuale, tra
 :  : DEC T(TA) P(IGIQ6) K(08) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(09) I(PARAMETRO >>)
L'associazione TEMPO DI CONSEGNA - VALUTAZIONE TEMPO DI CONSEGNA si trova nella stessa tabella dell'associazione precedente, in particolare
 :  : DEC T(TA) P(IGVQQ) K(RISC) I(ELEMENTO >>)
La_9_Percentuale di reclami confermatiè calcolata tramite
 :  : DEC T(TA) P(IGIQ6) K(10) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(11) I(PARAMETRO >>)
L'_9_indice di reclamoconsidera il valore di
 :  : DEC T(TA) P(IGIQ6) K(12) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ6) K(13) I(PARAMETRO >>)
Tali indici sono visualizzabili anche nel_7_CQVEND :  l'indice globale che ne deriva si trova in
 :  : DEC T(ST) K(CRM) I(SETTORE >>)
 :  : DEC T(TA) P(CRM) K(VCLI) I(INDICE >>)
Questo valore è dato dalla media pesata di indici contenuti in
 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLCC) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLC2) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLC3) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLC4) I(SUBSETTORE >>)
In questo ambito è possibile modificare il peso di ciascun indice. Il collegamento tra_7_CQVENDe_7_D5COSOè contenuto in
 :  : DEC T(ST) K(CQ$) I(SETTORE >>)
 :  : DEC T(TA) P(CQ$) K(CLI) I(SUBSETTORE >>)

Nel contesto_7_CQVENDè possibile inserire, leggere e modificare anche indici STATICI. Essi sono memorizzati in
 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLC1) I(SUBSETTORE >>)

_7_ATTENZIONE!!
Affinché si possa leggere la valutazione di un dipendente sul CQVEND deve essere inserito almeno un giudizio di un indice statico per quel dipendente! La lettura del D5COSO deriva di conseguenza. Dal D5COSO non è invece possibile leggere gli indicatori statici ed il conseguente indice globale.

### INDICI DI VALUTAZIONE DEL PERSONALE
La valutazione di un Dipendente avviene tramite due tipologie di indicatori :  DINAMICI e STATICI.

- _1_DINAMICI. Sono indici che risultano da calcoli eseguiti sulle ore di presenza e di lavoro svolto. Viene utilizzato in input il computo delle ore mensili di ogni dipendente.
Questo tipo di indici è memorizzato nel_7_D5COSO, in particolare

 :  : DEC T(TA) P(D5S) K(CNCOL) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(£OC) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
 :  : DEC T(ST) K(D5OCN) I(SUBSETTORE >>)
Al tema_7_£OCsono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGI£2) I(TABELLA >>)
Innanzitutto è utile conoscere il monte ore di calendario. Questo si ottiene facendo il prodotto dei giorni lavorativi a calendario (se presenti) per il numero di ore lavoro giornaliere. In alternativa, si preferisce calcolare
 :  : DEC T(TA) P(IGI£2) K(52) I(ELEMENTO >>)
Queste sono date dalla somma di : 
 :  : DEC T(TA) P(IGI£2) K(01) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(03) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(04) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(05) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(06) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(07) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(08) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(09) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(12) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(16) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(17) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(18) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(19) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(20) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(21) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(22) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(30) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(31) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(32) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(33) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(36) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(38) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(40) I(ELEMENTO >>)
Tutti questi dati sono prelevati dal sistema di rilevazione delle presenze. Per praticità sono stati riassunti i permessi "dovuti" nell'elemento : 
 :  : DEC T(TA) P(IGI£2) K(51) I(ELEMENTO >>)
Uno degli indici fondamentali per la valutazione di un dipendente è l'indice di ASSENTEISMO, il quale però migliora approssimandosi allo zero. Poiché la valutazione del dipendente è fatta in base 100, si è scelto diutilizzare : 
 :  : DEC T(TA) P(IGI£2) K(55) I(INDICATORE >>)
il quale è dato dal rapporto fra
 :  : DEC T(TA) P(IGI£2) K(54) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(53) I(ELEMENTO >>)
Le>ORE LAVORABILIsono le ore disponibili a calendario private di
 :  : DEC T(TA) P(IGI£2) K(08) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(09) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(12) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(40) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(51) I(ELEMENTO >>)
i quali sono dovuti e non rientrano nel calcolo dell'assenteismo. Le>ORE LAVORATEcomprendono semplicemente
 :  : DEC T(TA) P(IGI£2) K(01) I(ELEMENTO >>)
come si può notare le>ORE STRAORDINARIEnon rientrano in questo calcolo. Un secondo indice di valutazione è
 :  : DEC T(TA) P(IGI£2) K(56) I(INDICATORE >>)
dato dal rapporto, espresso in percentuale, tra
 :  : DEC T(TA) P(IGI£2) K(14) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(01) I(ELEMENTO >>)
Questo tipo di indicatore dà un valore non utilizzabile nel calcolo dell'indice globale. Si utilizza quindi il pgm di calcolo_7_CQCAL_DIche mediante la funzione STRA associa all'indice calcolato un valore su base 0-100 e lo inserisce in
 :  : DEC T(TA) P(IGI£2) K(57) I(INDICATORE >>)
Le impostazioni sull'associazione INDICE STRAORDINARI - VALUTAZIONE STRAORDINARI si trovano in
 :  : DEC T(ST) K(IGV) I(TABELLA >>)
 :  : DEC T(ST) K(IGVQQ) I(SUBSETTORE >>)
 :  : DEC T(TA) P(IGVQQ) K(STRA) I(ELEMENTO >>)
Il terzo indice di valutazione dinamico è
 :  : DEC T(TA) P(IGI£2) K(58) I(INDICATORE >>)
dato dal rapporto, in percentuale, tra
 :  : DEC T(TA) P(IGI£2) K(41) I(ELEMENTO >>)
 :  : DEC T(TA) P(IGI£2) K(01) I(ELEMENTO >>)
Anche in questo caso, per il calcolo dell'indice globale non si utilizza questo indicatore ma si procede come nel caso precedente richiamando il pgm _7_CQCAL_DI, in particolare la funzione FORM la quale scrive
 :  : DEC T(TA) P(IGI£2) K(59) I(INDICATORE >>)
L'associazione INDICE DI FORMAZIONE - VALUTAZIONE FORMAZIONE si trova nella stessa tabella dell'associazione precedente, in particolare
 :  : DEC T(TA) P(IGVQQ) K(FORM) I(ELEMENTO >>)
Tali indici sono visualizzabili anche nel_7_CQVEND :  l'indice globale che ne deriva si trova in
 :  : DEC T(ST) K(CRM) I(SETTORE >>)
 :  : DEC T(TA) P(CRM) K(VDIP) I(INDICE >>)
Questo valore è dato dalla media pesata di indici contenuti in
 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLDD) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLD2) I(SUBSETTORE >>)
Il collegamento tra_7_CQVENDe_7_D5COSOè contenuto in
 :  : DEC T(ST) K(CQ$) I(SETTORE >>)
 :  : DEC T(TA) P(CQ$) K(DIP) I(SUBSETTORE >>)

- _1_STATICI. Sono indicatori che derivano da giudizi assegnati al dipendente sulla base di valutazioni qualitative.
Questi non sono scritti nel D5COSO ma solo nel_7_CQVEND, in particolare in

 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLD1) I(SUBSETTORE >>)
In questa tabella è possibile aggiungere altri indici o modificare il peso da attribuire a ciascuno di essi nel calcolo dell'indice globale (media pesata).
Gli indici presenti sono : 
 :  : DEC T(TA) P(CRLD1) K(ST01) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST02) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST03) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST04) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST05) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST06) I(INDICE >>)
 :  : DEC T(TA) P(CRLD1) K(ST07) I(INDICE >>)
A questi indici è possibile assegnare una valutazione periodica con giudizi in scala INSUFFICIENTE-SCARSO-SUFFICIENTE-DISCRETO-BUONO-DISTINTO-OTTIMO ai quali viene automaticamente associato un valore numerico.
Queste impostazioni possono essere variate mediante la tabella
 :  : DEC T(ST) K(CRI) I(SETTORE >>)
 :  : DEC T(ST) K(CRID1) I(SUBSETTORE >>)

_7_ATTENZIONE!!
Affinché si possa leggere la valutazione di un dipendente sul CQVEND deve essere inserito almeno un giudizio di un indice statico per quel dipendente! La lettura del D5COSO deriva di conseguenza. Dal D5COSO non è invece possibile leggere gli indicatori statici ed il conseguente indice globale.

### VALUTAZIONE FORNITORE
La valutazione di un fornitore avviene tramite due tipologie di indicatori :  DINAMICI E STATICI

- _1_DINAMICI. Sono indici derivanti da calcoli eseguiti sui dati relativi agli ordini, alle consegne ed alla qualità dei prodotti da fornitore.
Questi sono memorizzati nel_7_D5COSOin

 :  : DEC T(TA) P(D5S) K(CNFOR) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(Q01) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
 :  : DEC T(ST) K(D5OCN) I(SUBSETTORE >>)
Al tema_7_Q01sono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGIQ1) I(TABELLA >>)
Gli indici proposti sono qui elencati e brevemente descritti : 
 :  : DEC T(TA) P(IGIQ1) K(31) I(INDICE >>)
è calcolato come rapporto percentuale fra i parametri
 :  : DEC T(TA) P(IGIQ1) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(03) I(PARAMETRO >>)
É possibile considerare puntuale un ordine consegnato entro X giorni dalla data confermata presente sull'ordine (X parametro da aggiungere). Un ordine appartiene al periodo in questione se vi appartiene la data di consegna confermata dal fornitore.
 :  : DEC T(TA) P(IGIQ1) K(33) I(INDICE >>)
è ottenuta mediante la funzione_7_RITFche nel pgm_7_CQVEN_DIassocia un numero che va da 0 a 100 al valore di
 :  : DEC T(TA) P(IGIQ1) K(32) I(INDICE >>)
il quale risulta espresso in giorni. Questo viene calcolato con
 :  : DEC T(TA) P(IGIQ1) K(02) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(04) I(PARAMETRO >>)
I giorni di ritardo di un ordine sono calcolati considerando i soli giorni lavorativi che intercorrono tra la data di consegna confermata (eventualmente aumentata di X giorni) e la data di consegna effettiva presente sulla bolla. Si calcola quindi la media dei giorni di ritardo sul numero di ordini in ritardo, sempre all'interno del periodo considerato. Le impostazioni sull'associazione RITARDO MEDIO DI CONSEGNA - VALUTAZIONE DEL RITARDO si trovano in
 :  : DEC T(ST) K(IGV) I(TABELLA >>)
 :  : DEC T(ST) K(IGVQQ) I(SUBSETTORE >>)
 :  : DEC T(TA) P(IGVQQ) K(RITF) I(ELEMENTO >>)
Altri indicaatori sono
 :  : DEC T(TA) P(IGIQ1) K(35) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ1) K(36) I(INDICE >>)
Il_9_Rispetto della quantità, sia essa_9_attesao_9_dichiarata, viene calcolato mediante il raffronto fra le quantità risultanti dall'ordine, dalla bolla di consegna e dalla registrazione dell'effettivo controllo.
 :  : DEC T(TA) P(IGIQ1) K(11) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(12) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(13) I(PARAMETRO >>)
Il rispetto della quantità è il rapporto percentuale fra ciò che si è effettivamente ricevuto e ciò che ci si aspettava di ricevere dall'ordine e dalla bolla.
Si hanno poi gli indici relativi alle conformità/non conformità : 
 :  : DEC T(TA) P(IGIQ1) K(38) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ1) K(39) I(INDICE >>)
La percentuale di_9_Conformi in lavorazione per conformità da fornitorederiva dal complemento a 100 della NC percentuale riconosciuta in produzione dovuta a NC dei pezzi ricevuti dal fornitore e calcolata con
 :  : DEC T(TA) P(IGIQ1) K(07) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(08) I(PARAMETRO >>)
La percentuale di_9_Conformi al cliente per conformità da fornitoreè calcolata con il complemento a 100, considerando le NC riconosciute e rese o reclamate dal cliente ed attribuibili al fornitore, confrontate con la quantità spedita
 :  : DEC T(TA) P(IGIQ1) K(09) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(10) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(42) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ1) K(43) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ1) K(45) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ1) K(46) I(INDICE >>)
Tali indici sono calcolati con
 :  : DEC T(TA) P(IGIQ1) K(13) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(14) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(15) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(17) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ1) K(18) I(PARAMETRO >>)
I parametri derivano dal controllo eseguito sul lotto. La>quantità controllataè la base per il calcolo delle percentuali. Tali indici sono visualizzabili anche nel_7_CQVEND :  l'indice globale che ne
deriva si trova in
 :  : DEC T(ST) K(CRM) I(SETTORE >>)
 :  : DEC T(TA) P(CRM) K(VFOR) I(INDICE >>)
Questo valore è dato dalla media pesata di indici contenuti in
 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLFF) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLFD) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLF3) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLF4) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLF5) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLF6) I(SUBSETTORE >>)
Il collegamento tra_7_CQVENDe_7_D5COSOè contenuto in
 :  : DEC T(ST) K(CQ$) I(SETTORE >>)
 :  : DEC T(TA) P(CQ$) K(FOR) I(SUBSETTORE >>)

- _1_STATICI. Sono indicatori che derivano da giudizi assegnati al fornitore sulla base di valutazioni qualitative.
Questi non sono scritti nel D5COSO ma solo nel_7_CQVEND, in particolare in

 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLFS) I(SUBSETTORE >>)
In questa tabella è possibile aggiungere altri indici o modificare il peso da attribuire a ciascuno di essi nel calcolo dell'indice globale (media pesata).
Gli indici presenti sono : 
 :  : DEC T(TA) P(CRLFS) K(ST01) I(INDICE >>)
 :  : DEC T(TA) P(CRLFS) K(ST02) I(INDICE >>)
 :  : DEC T(TA) P(CRLFS) K(ST03) I(INDICE >>)
 :  : DEC T(TA) P(CRLFS) K(ST04) I(INDICE >>)
A questi indici è possibile assegnare una valutazione periodica con giudizi in scala INSUFFICIENTE-SCARSO-SUFFICIENTE-DISCRETO-BUONO-DISTINTO-OTTIMO ai quali viene automaticamente associato un valore numerico.
Queste impostazioni possono essere variate mediante la tabella
 :  : DEC T(ST) K(CRI) I(SETTORE >>)
 :  : DEC T(ST) K(CRID1) I(SUBSETTORE >>)

_7_ATTENZIONE!!
Affinché si possa leggere la valutazione di un fornitore sul CQVEND deve essere inserito almeno un giudizio di un indice statico per quel fornitore! La lettura del D5COSO deriva di conseguenza. Dal D5COSO non è invece possibile leggere gli indicatori statici ed il conseguente indice globale.

### VALUTAZIONE DEL PROCESSO DI PRODUZIONE
Il Processo Produttivo è misurato mediante indici DINAMICI memorizzati nel _7_D5COSO, in particolare
 :  : DEC T(TA) P(D5S) K(CNAZI) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(Q02) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
Al tema_7_Q02sono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGIQ2) I(TABELLA >>)

Un primo sottoprocesso da valutare è la_9_LAVORAZIONE, che deve evitare di generare prodotti NC e, se accade, deve evitare di spedirli al cliente, riconoscendoli prontamente mediante dei controlli.
Tale valutazione si articola nei seguenti indicatori : 
 :  : DEC T(TA) P(IGIQ2) K(31) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(32) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(33) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(34) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(35) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(36) I(INDICE >>)
L'_9_Efficienza del lavoroè calcolata sia a livello totale, che parzializzata per la manodopera diretta (MOD) e indiretta (MOI); in ogni caso è data da un rapporto percentuale fra i parametri elencati, considerati due a due : 
 :  : DEC T(TA) P(IGIQ2) K(05) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(06) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(02) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(03) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(04) I(PARAMETRO >>)
Le>Ore lavorate, presenti sul P5????, comprendono il tempo utilizzato per tutte le attività connesse con la lavorazione. Le>Ore di presenzasono registrate dal sistema di rilevazione della presenza.
La_9_Produttivitàriguarda esclusivamente la manodopera diretta :  è uguale al rapporto percentuale fra
 :  : DEC T(TA) P(IGIQ2) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(07) I(PARAMETRO >>)
Le>Ore prodottesono dedicate esclusivamente alle attività di lavorazione e sono presenti sul P5????.
La_9_Capacità dei controlli in produzioneè il complemento a 100 della percentuale di NC spedite a cliente, calcolata mediante
 :  : DEC T(TA) P(IGIQ2) K(08) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(15) I(PARAMETRO >>)
L'_9_Efficacia del processosi rileva attraverso i controlli qualità in produzione e viene misurata come complemento a 100 della percentuale di NC
 :  : DEC T(TA) P(IGIQ2) K(09) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(10) I(PARAMETRO >>)
Un secondo sottoprocesso rilevato è quello relativo a_9_IMMAGAZZINAMENTO E
_2_CONSERVAZIONE.
 :  : DEC T(TA) P(IGIQ2) K(41) I(INDICE >>)
Anche questo indice è calcolato con una funzione che valuti la situazione di magazzino mediante
 :  : DEC T(TA) P(IGIQ2) K(39) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ2) K(40) I(INDICE >>)
Entrambi gli indicatori sono calcolati utilizzando
 :  : DEC T(TA) P(IGIQ2) K(11) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(12) I(PARAMETRO >>)
e sono l'uno l'inverso dell'altro.
Tali dati non sono utilizzabili nel calcolo dell'indice globale. Si utilizza quindi il pgm di calcolo_7_CQCAL_DIche mediante la funzione MAGA associa all'indice di copertura delle scorte un valore su base 0-100.
Le impostazioni sull'associazione COPERTURA SCORTE - VALUTAZIONE COPERTURA SCORTE si trovano in
 :  : DEC T(ST) K(IGV) I(TABELLA >>)
 :  : DEC T(ST) K(IGVQQ) I(SUBSETTORE >>)
 :  : DEC T(TA) P(IGVQQ) K(MAGA) I(ELEMENTO >>)
Il terzo sottoprocesso, considerato in questo ambito, è inerente al processo di_9_SPEDIZIONEed è misurato da
 :  : DEC T(TA) P(IGIQ2) K(42) I(INDICE >>)
Si tratta di un indice semplice dato dal rapporto percentuale fra
 :  : DEC T(TA) P(IGIQ2) K(13) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ2) K(14) I(PARAMETRO >>)
Tali indici sono visualizzabili anche nel_7_CQVEND :  l'indice globale che ne deriva si trova in
 :  : DEC T(ST) K(CRM) I(SETTORE >>)
 :  : DEC T(TA) P(CRM) K(VPRO) I(INDICE >>)
Questo valore è dato dalla media pesata di indici contenuti in
 :  : DEC T(ST) K(CRL) I(SETTORE >>)
 :  : DEC T(ST) K(CRLPP) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLP2) I(SUBSETTORE >>)
 :  : DEC T(ST) K(CRLP3) I(SUBSETTORE >>)
In questo ambito è possibile modificare il peso di ciascun indice.
Il collegamento tra_7_CQVENDe_7_D5COSOè contenuto in
 :  : DEC T(ST) K(CQ$) I(SETTORE >>)
 :  : DEC T(TA) P(CQ$) K(PRO) I(SUBSETTORE >>)

### VALUTAZIONE DEL PROCESSO DI MANUTENZIONE
Il Processo di Manutenzione è misurato mediante indici DINAMICI memorizzati nel _7_D5COSO, in particolare
 :  : DEC T(TA) P(D5S) K(CNAZI) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(Q03) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
Al tema_7_Q03sono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGIQ3) I(TABELLA >>)
La valutazione di questo processo avviene mediante i seguenti indicatori : 
 :  : DEC T(TA) P(IGIQ3) K(31) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ3) K(33) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ3) K(34) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ3) K(35) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ3) K(36) I(INDICE >>)
Il_9_Grado di affidabilità degli impianti è calcolato come complemento a 100 del Grado di invecchiamento degli impianti, ottenuto dal rapporto, espresso in percentuale, dei seguenti due parametri
 :  : DEC T(TA) P(IGIQ3) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ3) K(02) I(PARAMETRO >>)
La_9_Valutazione dell'efficienza della manutenzione programmataè un valore calcolato con il pgm_7_CQCAL_DI; questo utilizza la funzione_7_MAGAper dare una valutazione in base 100 a
 :  : DEC T(TA) P(IGIQ3) K(32) I(INDICE >>)
il quale viene calcolato come semplice rapporto tra
 :  : DEC T(TA) P(IGIQ3) K(03) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ3) K(04) I(PARAMETRO >>)
Le impostazioni sull'associazione EFFICIENZA MANUTENZIONE PROGRAMMATA - VALUTAZIONE MANUTENZIONE PROGRAMMATA si trovano in
 :  : DEC T(ST) K(IGV) I(TABELLA >>)
 :  : DEC T(ST) K(IGVQQ) I(SUBSETTORE >>)
 :  : DEC T(TA) P(IGVQQ) K(MANP) I(ELEMENTO >>)
IL_9_Livello di utilizzo degli impiantiutilizza in ingresso
 :  : DEC T(TA) P(IGIQ3) K(05) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ3) K(06) I(PARAMETRO >>)
ed è l'incidenza percentuale del parametro 05 sul 06.
La_9_Valutazione della manutenzione straordinariaderiva dal pgm_7_CQCAL_DI che con la funzione_7_MANP associa un valore compreso fra 0 e 100 (100 valore ottimo) al valore
 :  : DEC T(TA) P(IGIQ3) K(07) I(PARAMETRO >>)
Le impostazioni sull'associazione MANUTENZIONE STRAORDINARIA - VALUTAZIONE MANUTENZIONE STRAORDINARIA si trovano nella medesima tabella del caso precedente, in particolare in
 :  : DEC T(TA) P(IGVQQ) K(MANS) I(ELEMENTO >>)
La_9_Valutazione dei costi di manutenzionerichiama il solito pgm ed associa utilizza la funzione COMA per associare un valore 0-100 a
 :  : DEC T(TA) P(IGIQ3) K(08) I(PARAMETRO >>)
Le impostazioni sono nella tabella dei casi precedenti, in particolare
 :  : DEC T(TA) P(IGVQQ) K(COMA) I(ELEMENTO >>)

### VALUTAZIONE PROCESSO DI GESTIONE DELLA DOCUMENTAZIONE
 Il Processo di Gestione della Documentazione è misurato mediante indici  DINAMICI memorizzati nel_7_D5COSO, in particolare
  :  : DEC T(TA) P(D5S) K(CNAZI) I(CONTESTO >>)
  :  : DEC T(TA) P(D5OCN) K(Q05) I(TEMA >>)
 In particolare quest'ultimo si trova nel
  :  : DEC T(ST) K(D5O) I(SETTORE >)
 Al tema_7_Q05sono associate le quantità (fino a 99) contenute in
  :  : DEC T(ST) K(IGIQ5) I(TABELLA >>)
 Il processo è valutato mediante due indici, più precisamente : 
  :  : DEC T(TA) P(IGIQ5) K(31) I(INDICE >>)
  :  : DEC T(TA) P(IGIQ5) K(32) I(INDICE >>)
 L'_9_Indice di modifica documentiè ottenuto dal rapporto fra
  :  : DEC T(TA) P(IGIQ5) K(01) I(PARAMETRO >>)
  :  : DEC T(TA) P(IGIQ5) K(03) I(PARAMETRO >>)
 L'_9_Indice nuovi documentiè calcolato come rapporto tra
  :  : DEC T(TA) P(IGIQ5) K(02) I(PARAMETRO >>)
  :  : DEC T(TA) P(IGIQ5) K(03) I(PARAMETRO >>)

### COST OF QUALITY
I Costi della Qualità sono memorizzati nel _7_D5COSO, in particolare
 :  : DEC T(TA) P(D5S) K(CNAZI) I(CONTESTO >>)
 :  : DEC T(TA) P(D5OCN) K(Q07) I(TEMA >>)
In particolare quest'ultimo si trova nel
 :  : DEC T(ST) K(D5O) I(SETTORE >)
Al tema_7_Q07sono associate le quantità (fino a 99) contenute in
 :  : DEC T(ST) K(IGIQ7) I(TABELLA >>)
In questo ambito sono riassunti i costi sostenuti per la gestione della qualità e delle non qualità. È dato dalla somma di
 :  : DEC T(TA) P(IGIQ7) K(31) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ7) K(32) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ7) K(33) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ7) K(34) I(INDICE >>)
 :  : DEC T(TA) P(IGIQ7) K(35) I(INDICE >>)
Il_9_Costo controllo qualitàriguarda sia i controlli in accettazione che quelli in produzione. Si considerano : 
 :  : DEC T(TA) P(IGIQ7) K(01) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(02) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(07) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(22) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(10) I(PARAMETRO >>)
Il_9_Costo della strumentazionecomprende
 :  : DEC T(TA) P(IGIQ7) K(03) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(25) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(21) I(PARAMETRO >>)
Il_9_Costo degli auditè dato dal prodotto di
 :  : DEC T(TA) P(IGIQ7) K(04) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(23) I(PARAMETRO >>)
Il_9_Costo delle Non Conformitàè legato a
 :  : DEC T(TA) P(IGIQ7) K(11) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(12) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(13) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(14) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(15) I(PARAMETRO >>)
 :  : DEC T(TA) P(IGIQ7) K(08) I(PARAMETRO >>)
Il_9_Costo delle azioni correttiveè ottenuto mediante
  :  : DEC T(TA) P(IGIQ7) K(06) I(PARAMETRO >>)
  :  : DEC T(TA) P(IGIQ7) K(24) I(PARAMETRO >>)

 :  : DEC T(TA) P(B£H) K(D510) I(Flusso estrazione Tab.B£H >>)
Il Flusso di estrazione articolato in alcuni passi di selezioni consente l'estrazione nel d5coso0f degli indici Aziendali
