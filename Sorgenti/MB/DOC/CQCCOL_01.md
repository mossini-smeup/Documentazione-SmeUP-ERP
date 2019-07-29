# Scopo
 * Classificazione delle informazioni relative alle modalità' di esecuzione dei controlli
 * Gestione delle fasi di controllo in accettazione dei materiali (acquisto, c/lavoro, ...)
 * Gestione delle fasi di controllo durante il ciclo di produzione, e sul prodotto finito
 * Definizione  del campionamento per ogni fase e/o in  relazione alla  classificazione funzionale del materiale
 * Definizione delle fasi di controllo esterno (griglia di riferimento per il fornitore) ed interno (in regime di collaudo od autocontrollo)
 * Gestione del livello di modifica della fase del ciclo correlato al livello di modifica del disegno
 * Tempificazione e costificazione delle operazioni di collaudo

# Definizioni
 * Fase di Lavorazione; identifica attraverso una sigla la fase del processo di lavorazione della parte (** identifica l'accettazione materiali senza ciclo di produzione)
 * Ciclo di collaudo/controllo; è costituito da fasi di collaudo, ogni fase di collaudo è il controllo di una caratteristica (ad esempio il ciclo di collaudo di un cubo è costituito da 3 fasi, fase 1, controllo larghezza, fase 2 controllo lunghezza, fase 3 controllo profondità)
 * Fase di collaudo; identifica attraverso una sigla (normalmente un progressivo) lo specifico controllo

# Tabelle utilizzate dal modulo : 
### CQ4 - OBBLIGATORIETÀ CONTROLLI
Identifica l'obbligo del cotrollo e/o della registrazione
  :  : DEC T(ST) K(CQ4)

### CQT - TIPO DI MISURA
Individua il tipo di misurazioni (dimensionale, di peso, ...) ed i conseguenti parametri di riferimento (dimensionale nominale, valore minimo, tolleranza +, ...), permette di associare la sigla del piano di campionamento da applicare nel controllo
 :  : DEC T(ST) K(CQT)

### CQI -  CLASSI IMPORTANZA CARATTERISTICA
Identifica, in funzione dell'importanza della caratteristica da controllare, il livello L.Q.A. accettazione del lotto
 :  : DEC T(ST) K(CQI)

### CQD - DIFETTI
Codifica i difetti riscontrabili nei controlli
 :  : DEC T(ST) K(CQD)

### CQO - TIPO DI CONTROLLO
Identifica se il controllo è interno od esterno, ed il regime (collaudo od autocontrollo), condiziona le stampe delle griglie di controllo
 :  : DEC T(ST) K(CQO)

### CQ0 - TIPO DOCUMENTO - GESTIONE
Codificare le procedure interne e/o esterne utilizzate in azienda per la gestione delle procedure di qualità.
 :  : DEC T(ST) K(CQ0)

### CQM - PROCEDURE MANUALE QUALITÀ
Legare alla procedura un responsabile emittente e la data di emissione.
 :  : DEC T(ST) K(CQM)

### CQP - PIANO CONTROLLO QUALITÀ
Definire la struttura della tabella del piano di campionamento, stabilendone le intestazioni delle colonne e le tipologie dei campi.
 :  : DEC T(ST) K(CQP)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * classificazione delle tipologie
 * classificazione delle criticità, LQA e modalità di campionamento
 * classificazione delle procedure di riferimento
 * inserimento delle tabelle relative al modulo
 * inserimento dei cicli di collaudo di accettazione (fase lavorazione **)
 * inserimento dei cicli di collaudo di produzione (fase di lavorazione specifica)
 * stampa delle griglie di riferimento per i controlli eseguiti direttamente dai fornitori
 * stampa delle griglie di riferimento per i controlli di produzione eseguiti in regime di autocontrollo


## Attività periodica
 * manutenzione dei cicli di collaudo per le parti in uso (eventualmente usando l' indice di modifica, previsto nella definizione del ciclo di collaudo)
 * manutenzione dei cicli di collaudo per le nuove parti


# Gestione ciclo di collaudo (flusso informativo)
![CQ_CCOL_01](http://localhost:3000/immagini/CQCCOL_01/CQ_CCOL_01.png)
# Gestione ciclo di collaudo (flusso funzionale)
![CQ_CCOL_02](http://localhost:3000/immagini/CQCCOL_01/CQ_CCOL_02.png)