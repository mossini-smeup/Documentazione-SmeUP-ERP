# Scopo
 * Gestione degli indici dinamici
 * Rappresentazione grafica degli indici
 * Stampa degli indici

# Definizioni
 * _2_Indici dinamici, sono indici che risultano da calcolazioni eseguite in automatico dal programma sulla base dei dati in archivio del tipo : 
 ** andamento della qualità delle forniture,
 ** andamento delle tempistiche di consegna,
 ** sensibilità all'aspetto qualitativo del prodotto, rispetto della certificazione del prodotto consegnato e obbligo di conservazione dei documenti secondo le prassi stabilite,
 ** .........
Per questo tipo di indici il programma apre i diversi archivi disponibili : 
 ** Non Conformità
 ** Audit
 ** Lotti
 ** Documentazione
 ** Strumenti di misura
 ** Fmea
 ** Personale
 ** Richieste di Intervento
 * _2_Area, rappresenta un macro raggruppamento dei temi di interesse per le valutazioni  effettuate con indici dinamici, ad esempio Area Contabilità, Area Produzione, Area Vendite, Area Zonale, Area Assicurazione Qualità, Area Magazzini, ecc.. (tabella IGA)
 * _2_Tema, identifica con un codice un insieme di dati legati ad un argomento comune, ad esempio tema delle verifiche sugli audit, tema della gestione delle non conformità, tema della fmea, ecc.. (tabella IGT). È utilizzazto per indici dinamici.
 * _2_Livello di sintesi, specifica a quale preciso fattore fare riferimento per la ricerca dei dati relativi ad un indice dinamico, ad esempio articolo, articolo/fornitore, ecc.. (tabella IGS)

![IG_REPT_01](http://localhost:3000/immagini/IGREPT/IG_REPT_01.png)
# Tabelle utilizzate dal modulo

### IGA - AREA INDICI DI GESTIONE
Codifica l'Area di provenienza di un indice dinamico
 :  : DEC T(ST) K(IGA)

### IGT - TEMATICHE INDICI DI GESTIONE
Codifica il Tema dell'Area di provenienza di un indice dinamico
 :  : DEC T(ST) K(IGA)

### IGS - LIVELLI SINTESI IND.  GESTIONE
Codifica il Livello di Sintesi dell''Area/Tema di provenienza di un indice dinamico
 :  : DEC T(ST) K(IGS)

### PER - TABELLA PERIODI
Codifica il Periodo di riferimento da cui prelevare i valori per il calcolo degli indici dinamici
 :  : DEC T(ST) K(PER)

### CQY - TIPO GRIGLIA  CONTROLLI
Descrive il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(CQY)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Classificazione, area, tema, livello di sintesi, periodo.
 * Inserimento tabelle
 * Associazione degli indici ad un tema
 * Creazione dei legami area/tema/livello di sintesi
 * Inserimento programmi di calcolo per indici dinamici
 * Simulazione formule

## Attività periodica
 * Manutenzione tabelle
 * Manutenzione legami
 * Stampa indici
 * Aggiornamento indici
