# Scopo
 * Fornire un supporto per la determinazione della conformità o non conformità degli elementi del sistema qualità tramite la : 
 ** Gestione di Liste di Riferimento
 ** Gestione in forma pesata del livello qualitativo delle varie attività
 ** Gestione della Documentazione dei risultati dell'Audit
 ** Gestione delle caratteristiche critiche
 ** Emissione di Azioni Correttive
 ** Gestione risultati audit in indici dinamici (vedi riferimento FU/INDI).

# Definizioni
## AUDIT
Sistema di verifica il cui fine primario è quello di fornire agli Enti responsabili dell'Azienda, una costante e precisa visuale di ogni settore produttivo interno ed esterno all'azienda e della validità dell'organizzazione in tema di : 
 * livello qualitativo, pesato, e suo andamento nel tempo,
 * interventi necessari per eliminare carenze in atto.

Gli Audits relativi alla verifica dei processi produttivi devono essere diretti a valutare la conformità esecutiva : 
 * dei processi produttivi,
 * delle apparecchiature di controllo,
 * del prodotto finito od in corso di lavorazione.

Gli Audits relativi alla verifica della reale Funzionalità delle norme di "Assicurazione Qualità" devono essere diretti a valutare se : 
 * ogni Ente applica ed esegue correttamente le attività stabilite;
 * le Norme in atto risultano costantemente valide nel tempo sia sotto l'aspetto operativo al fine di introdurre, in tempo utile, eventuali necessari correttivi.

Il "CONTROLLO QUALITÀ'" dell'Azienda è l'Ente responsabile di condurre e coordinare gli Audits.

## Liste di riferimento
Ogni Audit deve essere predisposto su un apposita "Lista di riferimento" per potere verificare la conformità di attività fondamentali come : 
 * documentazioni,
 * mezzi di controllo,
 * mezzi di produzione,
 * materiale,
 * prodotto,
 * fornitori,
 * clienti,
 * processi speciali.

Le liste in forma pesata, devono evidenziare tutte le caratteristiche del prodotto, del processo produttivo e del fatto organizzativo che possono influenzare, se non in condizioni ottimali, la validità del prodotto finale.

## Gruppo di lavoro
operante a tempo parziale, è da intendersi come un assieme di due o più persone, con esperienze diversificate, maggiormente specializzate nel settore da esaminare che sovrintendono alla stesura delle "Liste di riferimento".
Tanto più elevata sarà la validità del "Gruppo di lavoro", tanto più efficaci risulteranno le "Liste di riferimento" emesse. È quindi necessario definire lo skill dell'Auditor (è prevista dalla normativa).

Il Gruppo Di Lavoro "GDL" si occuperà di : 
 * Emettere le "Liste di riferimento" per i  settori interessati o per la verifica dell'organizzazione, definire le caratteristiche da esaminare e valutare.
 * Stabilire il punteggio ottimale di ogni caratteristica per determinare il "punteggio complessivo possibile" per il settore in esame.
 * Delegare uno o più dei propri componenti per eseguire, con il responsabile dell'area, l'esame del settore interessato e valutare obiettivamente tutte le caratteristiche indicate sulle "Liste di riferimento" per individuare il "Punteggio complessivo reale" del settore stesso.
 * Trasmettere, in forma documentata, i risultati dell'Audit al responsabile dell'Azienda ed al responsabile del settore interessato segnalando le cause che hanno dato luogo a casi di "criticità".
 * Rifare l'Audit del settore dopo eventuali interventi correttivi.

Il Servizio Controllo Qualità "SCQ"   si occuperà di : 
 * Gestire e programmare gli Audits e garantire la continuità di quanto stabilito.
 * Riunire il "Gruppo di lavoro" per definire le "Liste di riferimento" ed eseguire gli Audits.
 * Informare, prima di dare inizio all'Audit, il responsabile del settore da esaminare.

Il Responsabile del settore sottoposto a verifica si occuperà di : 
 * Intraprendere o richiedere gli interventi correttivi necessari per risolvere le cause delle "criticità" emerse in fase di Audit.
 * Riproporre al "Gruppo di lavoro" i casi  ritenuti critici, per la loro complessità, al fine di promuovere adeguate "Azioni correttive".

## Importanza caratteristica
 :  : DEC T(ST) K(CQJ)
questo campo tabellato (tabella CQJ) permette di valutare ogni caratteristica per il grado di importanza che riveste in Funzione di una possibile incidenza sull'affidabilità del prodotto finale e quindi sui costi che potrebbero derivare da prodotti non soddisfacenti per il cliente. Si possono distinguere  : 
 * Caratteristica fondamentale
É una caratteristica che, se disattesa (mancante o in condizioni non ottimali o possibile causa di non corrispondenza del prodotto), può portare a : 
 ** un rischio per la sicurezza delle persone siano esse interne  od esterne all'Azienda,
 ** notevoli "costi aggiuntivi" interni, per scarti o non  conformità,
 ** una non FUnzionalità del prodotto con pesante insoddisfazione del cliente e possibili "costi aggiuntivi" esterni.

 * Caratteristica importante
É una caratteristica che, se disattesa, può portare a : 
 ** casi di imperfetto comportamento del prodotto,
 ** scarsa soddisfazione del cliente,
 ** costi aggiuntivi interni per messa a punto prodotto.

 * Caratteristica secondaria
É una caratteristica che, se disattesa, pur non incidendo apprezzabilmente sul comportamento del prodotto può, se rilevata, togliere limpidezza all'immagine.

# Tabelle utilizzate dal modulo : 
### CQY - TIPO GRIGLIA  CONTROLLI
Descrive il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(CQY)

### CQJ - IMPORTANZA ARGOMENTO
Classificare le classi di importanza  ed assegnare ad ognuna un "peso", che verrà utilizzato successivamente a fini statistici.
  :  : DEC T(ST) K(CQJ)

### CQW - VALUTAZIONE CONTROLLO
Definire le classi di valutazione per i punti controllati della GRIGLIA di RIFERIMENTO dell'AUDIT. Le classi di valutazione sono di tipo descrittivo, ad esse saranno poi associati dei valori numerici di riferimento.
 :  : DEC T(ST) K(CQW)

### CQ* Controlli generici
Questa tabella è prevista per contenere alcuni valori che sono condizioni dell'applicazione o per qualsiasi uso simile l'utente voglia farne.
Ogni subsettore ha un significato specifico. Per questa tabella non si prevedono sottodefinizioni, quindi si deve utilizzare solo per verificare la correttezza di un dato e/o per decodificare un codice. In particolare è possibile associare un sub-settore ai significati particolari di qualche tabella. Se ad esempio si dice che il contenuto possibile di una scelta di tabella sono 6 parole/valori non gestibili con la tecnica dei limiti, si fa riferimento ad un sub-settore. La ricerca con "!" o "?" fornisce un dettaglio maggiore.
 :  : DEC T(ST) K(CQ*)

### DIP - PERSONALE ANAGRAFICA-DIPENDENTI
Codifica le matricole dei dipendenti.
 :  : DEC T(ST) K(DIP)

### *CNTT CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. l'Audit.
 :  : DEC T(ST) K(*CNTT)

### CQM - MANUALE QUALITÀ
Codificare le procedure interne e/o esterne utilizzate in azienda per la gestione delle procedure di qualità.
Legare alla procedura un responsabile emittente e la data di emissione.
 :  : DEC T(ST) K(CQM)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Classificazione delle tipologie
 * Classificazione delle classi d'importanza, e di valutazione
 * Classificazione delle  procedure di riferimento
 * Inserimento tabelle relative al modulo
 * Emissione delle liste di riferimento

## Attività periodica
 * Aggiunta, modifica alle liste di riferimento
 * Pianificazione attività di audit con la creazione dei legami
 * Stampa scadenziario audit
 * Inserimento valutazioni Audit
 * Emissione Azioni Correttive
 * Stampa risultati Audit

# Gestione Audit e Verifiche Ispettive (flusso Funzionale)
![CQ_AUDT_01](http://localhost:3000/immagini/CQAUDT_01/CQ_AUDT_01.png)