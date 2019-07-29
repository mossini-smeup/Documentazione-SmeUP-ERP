# Scopo
 * Gestione dell'emissione, approvazione, rilascio e distribuzione di un documento.
 * Gestione del livello di modifica del documento emesso
 * Gestione  controllata della  distribuzione della documentazione
 * Visualizzazione e stampa della documentazione


# Definizioni
 * Stato Documento; identifica con un codice lo stato del documento che ad esempio può essere una prima stesura, rilasciato, ecc.. (vedi tabella CQ2)
 * Livello di modifica superiore; identifica il valore del livello superiore dell'esponente di modifica per la definizione della validità del ciclo
 * Livello di modifica inferiore; identifica il valore del livello inferiore dell'esponente di modifica
 * Livello di modifica; Viene utilizzato per ricercare gli ordini di produzione, acquisto, conto lavori e vendita, emessi prima della variazione del livello di modifica e ancora da evadere e per controllare in fase di movimentazione del lotto per il magazzino della corrispondenza del livello di modifica ultimo rilasciato.
 * Tipo di modifica; identifica  un codice che fornisce informazioni relative al tipo di modifica a cui è stato sottoposto il documento. Un documento può essere evaso definitivamente, da rivedere ecc.... (vedi tabella CQ*MD)
 * Azione sulla prossima Emissione; fornisce un'indicazione sull'azione che deve essere svolta alla successiva emissione del documento.
 * Problematica; descrizione sintetica della problematica affrontata con il documento in oggetto
 * Obbiettivo/Soluzione Proposta; descrizione sintetica dell' obbiettivo o della soluzione proposta da colui che emette il documento in oggetto
 * Soluzione adottata; descrizione sintetica della soluzione adottata da colui che evade il documento in analisi
 * Documento Origine; documento che ha originato l'emissione del documento che si sta analizzando. Ad esempio se una richiesta di modifica da un progetto avesse portato un alla modifica dei disegni del progetto, il campo "Docum. Origine" avrebbe offerto la possibilità di collegarsi in interrogazione con tale richiesta di modifica di progetto
 * Ente emittente; identifica con un codice l'ente/area operativa che emette il documento (tabella *CN)
 * Matricola responsabile emissione; identifica il codice dell'operatore, appartenente all'ente/area operativa specificata con il campo "ente emittente", responsabile dell'emissione del documento (tabella *CN)
 * Tipo codice; identifica con un codice un tipo oggetto del sistema informativo ad esempio AR=articolo, CL=cliente, ecc.. (tabella *CN)
 * Parametro; è una specifica del tipo di codice, ad esempio il tipo codice può essere una tabella il parametro specifica di che tabella si tratta
 * Codice elemento; identifica con un codice un oggetto del sistema informativo ad esempio articolo 0001, cliente NAPPI CRISTIANO, ecc..
 * Domanda; identifica con un codice lo stato della domanda, questo codice serve per pilotare la visualizzazione dei documenti (tabella A£D)
 * Codice risposta; identifica con un codice la risposta, questo codice può anche essere utilizzato per  modificare lo stato del documento impostato con il campo "Domanda"  (tabella A£R)
 * Stato risposta; identifica con un codice lo stato della  risposta immesso con il campo "Codice risposta", viene utilizzato in genere per effettuare delle parzializzazioni sui documenti da interrogare, gestire, ecc..
 * Lista; identifica il tipo lista , viene utilizzato in genere per effettuare delle parzializzazioni sui documenti da interrogare, gestire, ecc..
 * Tipo Contenuto; identifica con un codice un contenitore  che è un raccoglitore di informazioni identificate da tre chiavi, ad esempio il contenitore AUD è il contenitore degli esiti controlli audit caratterizzato dalle tre chiavi griglia/audit/progressivo (tabella NSC)

# Tabelle utilizzate dal modulo : 
### CQ* Controlli generici
Questa tabella è prevista per contenere alcuni valori che sono condizioni dell'applicazione o per qualsiasi uso simile l'utente voglia farne.
Ogni subsettore ha un significato specifico. Per questa tabella non si prevedono sottodefinizioni, quindi si deve utilizzare solo per verificare la correttezza di un dato e/o per decodificare un codice. In particolare è possibile associare un sub-settore ai significati particolari di qualche tabella. Se ad esempio si dice che il contenuto possibile di una scelta di tabella sono 6 parole/valori non gestibili con la tecnica dei limiti, si fa riferimento ad un sub-settore. La ricerca con "!" o "?" fornisce un dettaglio maggiore.
il subsettore MD identifica il tipo di modifica del documento
il subsettore ST identifica lo stato di evasione del documento
  :  : DEC T(ST) K(CQ*)

### CQ2 Stato Rilascio/Approvazione
Questa tabella contiene gli stati in cui può trovarsi un documento in relazione all'emissione, approvazione, rilascio. Per questo sono stati creati tre sottosettori della stessa tabella associati ciascuno ad una opportuna classe di autorizzazione
il subsettore EM identifica gli stati per l'emissione
il subsettore AP identifica gli stati per l'approvazione
il subsettore RI identifica gli stati per il rilascio
 :  : DEC T(ST) K(CQ2)

### *CNTT CODICI OGGETTI APPLICATIVI
è utilizzato per selezionare ente/area operativa/responsabile dell'emissione e il  tipo codice
 :  : DEC T(ST) K(*CNTT)

### CQ0  Tipo Documento
codifica il tipo di documento
 :  : DEC T(ST) K(CQ0)

### A£D Domande
codifica il tipo di Domanda del documento
 :  : DEC T(ST) K(A£D)

### A£R Risposte
codifica il tipo di Risposta del documento
 :  : DEC T(ST) K(A£R)

### NSC Note Strutturate Contenitori
codifica il tipo di Contenitore
 :  : DEC T(ST) K(NSC)

### NSL Liste Distribuzione
Questa tabella codifica i tipi di lista di distribuzione. I suoi sottosettori identificano un particolare tipo di lista, ad esempio il sottosettore CL identifica la lista  clienti, il sottosettore FO identifica la lista  fornitori, ecc... Nella tabellaNSC c'è un campo che rimanda a questi sottosettori per la scelta della lista.
 :  : DEC T(ST) K(NSL)

### DIP - PERSONALE ANAGRAFICA-DIPENDENTI
Codifica le matricole dei dipendenti.
 :  : DEC T(ST) K(DIP)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * classificazione delle tipologie di documento per la specificazione dei parametri di riferimento
 * classificazione delle tipologie di lista per la gestione della distribuzione
 * inserimento delle tabelle relative al modulo
 * gestione autorizzazioni
 * emissione del documento
 * approvazione del documento
 * rilascio del documento
 * distribuzione del documento

## Attività periodica
 * emissione del documento a livello di modifica superiore
 * gestione dell'emissione di nuove tipologie di documento
