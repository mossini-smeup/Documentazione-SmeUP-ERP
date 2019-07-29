# Obiettivo
  Raccogliere un insieme di tabelle e di esempi per ragionare sulle taglie e colori
  premettendo che ad oggi (2004) SME.up non si qualifica come un software che gestisce
  Taglie e Colori in termini generali ma solo per contesti specifici mediante i concetti
  impliciti nella configurazione. Quindi di seguito presentiamo solo piccoli esempi da discutere

  Useremo la taglia sia nella configurazione che come sviluppo quantità solo per esemplificazione
  Nella realtà si sceglierà una delle due strade

# Tabelle e dati
## Tabelle specifiche da predisporre
  - Collezioni (XC1 C1)
  - Colori     (XC1 C2)
  - Taglie     (XC1 C3)

## Nuovi oggetti
### Creare Domande, Questionario, Modello di configurazione
    Sett. Elemento Descrizione            Contenuto
  - B£CCF DOM01    COLLEZIONE             *GRUPPO  TAXC1C1  101 03 101 CFDOM002
  - B£CCF DOM02    COLORE                 *GRUPPO  TAXC1C2  101 03 105 CFDOM003
  - B£CCF DOM03    TAGLIA                 *GRUPPO  TAXC1C3  101 03 106
  - B£F   OA01     Questionario           CFDOM001
  - BRC   OA01     Questionario           2     1AOA01
  - C£Q   T01      Taglie                 Liberamente

### Creare sezioni listini e griglie
    Sett. Elemento Descrizione            Contenuto
  - C£VVE T01
  - C£VVE T02
  - C£VVE T03
  - C£VVE T04

### Creare tipo riga e forme di presentazione
    Sett. Elemento Descrizione            Contenuto
  - B£Q            Taglie/Colori          Programma V5DO05D_TA
  - V5BCA TAG      Taglie/Colori          Usa B£Q TAG e il resto a piacere

# Programmi
  - Visualizzatori di lista righe e di riga
  - Flussi di pre-cancellazione post-modifica ecc.
  - Analisi disponibilità orizzontale
    NB. I programmi sono presenti nel file MOD_TAG di SMEUP_DEM

# Esempi di utilizzo
## Articolo
    Creare un articolo "T01" con modello di configurazione OA01 e inserire una configurazione

## Distinta base
    Creare una distinta con : 
    - Articolo variabile in funzione del colore
    - Quantità in funzione della taglia

## Listini e prezzi
    Definire le seguenti sezioni
    - Prezzo base per articolo
    - Prezzo per configurazione
    - Maggiorazione per colore
    - Sconto/Maggiorazione per taglia

## Ordini clienti
    Caricare e gestire righe di un documento
    Il programma facilita l'immissione e la gestione delle righe scrivendo la taglia sulla riga
    La taglia (alternativa alla fase del conto lavoro) sarà utilizzata nella disponibilità

## Disponibilità
    Richiamare la disponibilità dell'articolo T01 con sintesi per oggetto
    Usare come oggetto la configurazione
    Usare F17 per definire la forma desiderata.
    - Se scelgo la fase vedo le taglie (corrispondenti alle fasi di conto lavoro)
    - Posso vedere la forma orizzontale

