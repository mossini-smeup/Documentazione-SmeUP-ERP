# Scopo
 * Emissione della richiesta dai programmi di gestione del Q9000 con indirizzamento all'ente preposto per la gestione fino alla definitiva evasione.
 * Gestione degli impegni di work flow previsti dal tipo richiesta.
 * Stampa del documento
 * Consuntivazione dei tempi e costi per l'evasione della richiesta con attribuzione degli stessi all'ente di addebito
 * Gestione dello stato di evasione della richiesta


# Definizioni
## Richiesta di intervento
Con la Richiesta di Intervento si può gestire qualsiasi azione che preveda : 
 * Fase Immissione
 **  descrizione dell'azione richiesta
 **  indirizzamento al gestore, data di evasione proposta, ente emittente
 * Fase Gestione
 **  asseganzione di un responsabile di gestione
 **  asseganzione di una priorità di evasione
 * Fase Evasione
 **  descrizione delle azioni effettuate
 **  esito ed efficacia delle azioni eseguite
 **  consuntivazione tempi, costi ed attribuzione ad un'ente di addebito eventuale
 **  stato finale e data della richiesta

Esempi di richieste di intervento sono :  Azioni Correttive e Preventive, Richieste di Progetto, Sperimentazione, Validazione, Modifica, Deroga per prodotti non conformi, Assistenza Esterna al prodotto, Richieste di lavoro generiche, Richiesta di documentazione, ecc..

# Tabelle utilizzate dal modulo : 
### CRR - TIPO RICHIESTA INTERVENTO
Classificare le tipologie delle richieste di intervento. Associare ad ogni tipologia di richiesta il profilo di posizione ottimale a cui il responsabile per l'assegnazione delle richieste dovrebbe riferirsi nella scelta della persona responsabile per l'evasione.
Personalizzare le descrizioni dei campi in funzione della tipologia delle richieste di intervento.
Definire il contenitore delle note strutturate da utilizzare per il tipo di richiesta specifico
 :  : DEC T(ST) K(CRR)

### CRQ - FORMATI VIDEO RICHIESTE INTERVENTO
Abilita la gestione/visualizzazione dei vari formati video componenti la RI.
 :  : DEC T(ST) K(CRQ)

### B£G - TIPO GRIGLIA CONTROLLI
Descrivere il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(B£G)

### B§A - PRIORITÀ DELL'INTERVENTO
Descrive la priorità di una Richiesta di Intervento (alta,media,bassa...)
 :  : DEC T(ST) K(B§A)

### *CNTT - CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. la  richiesta di intervento (direzione tecnica, direzione commerciale, ecc..)
 :  : DEC T(ST) K(*CNTT)

### CQ*QZ - DESCRIZIONE VALORI RICHIESTE
Descrive i dati  di base della richiesta di intervento (obbiettivo, soluzione proposta,ecc..)
 :  : DEC T(ST) K(CQ*QZ)

### CRO   - STATO EVASIONE
Descrive lo stato di evasione della richiesta di intervento (evaso, da definire, ecc..)
 :  : DEC T(ST) K(CRO)

### CQW - VALUTAZIONE DEL CONTROLLO
Descrive l'esito della soluzione adottata. Per ogni elemento della tabella si deve indicare un coefficiente di valutazione
 :  : DEC T(ST) K(CQW)

### WFA - PROCESSO WORKFLOW
Stabilisce quale processo di Workflow si occuperà di gestire i vari passi della vita della richiesta
 :  : DEC T(ST) K(WFA)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Classificazione tipi di intervento
 * Classificazione procedure di riferimento
 * Classificazione delle priorità di evasione
 * Classificazione degli stati della richiesta
 * Inserimento tabelle relative al modulo

## Attività periodica
 * Immissione Richieste di intervento
 * Gestione Richieste di intervento
 * Evasione Richieste di intervento
 * Stampa Richieste di intervento
