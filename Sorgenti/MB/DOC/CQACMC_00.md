# Scopo
 * Il modulo si occupa di codificare e gestire gli strumenti di misura presenti in azienda
 * Scadenzario strumenti
 * Gestione delle tarature, Studio MSA strumenti
 * Report


# Definizioni
## Categorie Strumenti di Misura
 Le categorie sono un raggruppamento omogeneo di strumenti.
Hanno la funzione di descrivere caratteristiche comuni a più matricole e di definirne i principali comportamenti di default
  esempio :  intervallo giorni e tipologia di taratura, numero decimali gestiti, portata minima-massima.

## Matricole Strumenti di Misura
La matricola è il nome assegnato a ogni singolo strumento gestito.
Definisce i fondamentali dati anagrafici, specifica lo stato attuale dello strumento, l'ubicazione ,il responsabile assegnatario, l'ente di taratura, le date, ecc.

## Taratura Strumenti
E' il registro dei controlli effettuati, a scadenza, su ogni singolo strumento per garantirne il regolare funzionamento.
I controlli possono essere Esterni (da Ente certificato) o effetuati internamente nel qual caso è possibile inserire e analizzare tutti i valori registrati.

## MSA Strumenti di Misura
Il Measurement System Analisys (MSA) è un insieme di procedure utilizzate in ambito qualità e finalizzate a individuare e isolare i componenti di variabilità insiti in un processo di misurazione che possono influenzare o inficiare i risultati stessi delle misure.


# Tabelle utilizzate dal modulo : 
### CR3 - Inizializzazione strumenti di misura
Tabella obbligatoria a elemento singolo
Definisce il setup essenziale del modulo, numeratori, tipi ciclo di collaudo assunti, note, parametri e stato iniziale
 :  : DEC T(TA) P(CR3) K(*)

### CR2 - Default strumenti di misura
Tabella obbligatoria
Definisce alcuni comportamenti di default divisi per tipo strumento, va compilata e legata alla tabella del tipo strumento
 :  : DEC T(ST) K(CR2)

### CQS - Tipo Strumento
Tabella obbligatoria
Definsce le famiglie di strumento e ne caratterizza i principali comportamenti di default
 :  : DEC T(ST) K(CQS)

### CQG - Grandezza misurata
Grandezza misurata serve anche da controllo di congruenza con strumento e unità di misura indicato sui piani di controllo
 :  : DEC T(ST) K(CQG)

### CQH - Unità di misura
Unità di misura
 :  : DEC T(ST) K(CQH)

### *CNTT - CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. la  richiesta di intervento (direzione tecnica, direzione commerciale, ecc..)
 :  : DEC T(ST) K(*CNTT)

### CRNMS - Numeratori
 :  : DEC T(ST) K(CRNMS)

### CQ*CP - Classe di precisione
 :  : DEC T(ST) K(CQ*CP)

### CRY   - Tipo studio MSA
Descrive il tipo di studio valori e operatori obbligatori
 :  : DEC T(ST) K(CRY)

### CQECC - Stato attuale strumento
Descrive l'esito della taratura
 :  : DEC T(ST) K(CQECC)

### CQ*CS - Colore Strumento
Non obbligatoria. Serve a dare l'immediata evidenza dello stato strumento
 :  : DEC T(ST) K(CQ*CS)

### CQ*US - Utilizzo Strumento
Non obbligatoria. Indica l'utilizzo a cui è destinato lo strumento
 :  : DEC T(ST) K(CQ*US)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Classificazione tipi di strumento
 * Classificazione procedure di riferimento
 * Classificazione delle grandezze misurate
 * Classificazione delle unità di misura
 * Impostazione numeratori e default modulo
 * Inserimento tabelle relative al modulo
 * Classificazione delle categorie strumenti
 * Immissione Matricole Strumenti

## Attività periodica
 * Gestione Matricole Strumenti
 * Scadenzario Strumenti
 * Taratura Strumenti
 * MSA Strumenti
 * Stampa e interrogazioni
