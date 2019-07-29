# Scopo
 * Emissione della richiesta dai programmi di gestione del Q9000 con indirizzamento all'ente preposto per l'evasione
 * Gestione della Lista di distribuzione della richiesta
 * Stampa del documento
 * Consuntivazione dei tempi e costi per l'evasione della richiesta con attribuzione degli stessi all'ente di addebito
 * Gestione dello stato di evasione della richiesta


# Definizioni
## Richiesta di intervento
esempi di richieste di intervento sono :  Azioni Correttive e Preventive, Richieste di Progetto, Sperimentazione, Validazione, Modifica, Deroga per prodotti non conformi, Assistenza Esterna al prodotto, Richieste di lavoro generiche, ecc..

# Tabelle utilizzate dal modulo : 
### CQZ - TIPO RICHIESTA INTERVENTO
Classificare le tipologie delle richieste di intervento. Associare ad ogni tipologia di richiesta il profilo di posizione ottimale a cui il responsabile per l'assegnazione delle richieste dovrebbe riferirsi nella scelta della persona responsabile per l'evasione.
Personalizzare le descrizioni dei campi in funzione della tipologia delle richieste di intervento.
Definire il contenitore delle note strutturate da utilizzare per il tipo di richiesta specifico
 :  : DEC T(ST) K(CQZ)

### CQY - TIPO GRIGLIA CONTROLLI
Descrivere il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(CQY)

### CQ*PR - PRIORITÀ DELL'INTERVENTO
Descrive la priorità di una Richiesta di Intervento (alta,media,bassa...)
 :  : DEC T(ST) K(CQ*PR)

### *CNTT - CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. la  richiesta di intervento (direzione tecnica, direzione commerciale, ecc..)
 :  : DEC T(ST) K(CQY)

### CQ*QZ - DESCRIZIONE VALORI RICHIESTE
Descrive i dati  di base della richiesta di intervento (obbiettivo, soluzione proposta,ecc..)
 :  : DEC T(ST) K(CQ*QZ)

### CQ*ST - STATO EVASIONE
Descrive lo stato di evasione della richiesta di intervento (evaso, da definire, ecc..)
 :  : DEC T(ST) K(CQ*ST)

### CQW - VALUTAZIONE DEL CONTROLLO
Descrive l'esito della soluzione adottata. Per ogni elemento della tabella si deve indicare un coefficiente di valutazione
 :  : DEC T(ST) K(CQW)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Classificazione tipi di intervento
 * Classificazione procedure di riferimento
 * Classificazione delle priorità di evasione
 * Inserimento tabelle relative al modulo

## Attività periodica
 * Immissione Richieste di intervento
 * Gestione Richieste di intervento
 * Evasione Richieste di intervento
 * Stampa Richieste di intervento
