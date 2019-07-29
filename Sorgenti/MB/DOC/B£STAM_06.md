## ASPETTI GENERALI DEI DOCUMENTI

### SETUP

- Setup batch/interattivo/modificabile
- Suddivizione fra setup di base e specifico
- Definizione del setup di base
-- Formato foglio
-- Orientamento
-- Bordi
-- Bianco/nero o colore
-- Numeri di pagina
-- Definizione destinazione
-- Definizione nome file
-- Definizione sovrascrittura
-- Accessibilità alle risorse
--- Codifica di immagini e icone
--- Accessibilità di immagini e icone


### DATI

- Identizicazione prerequisiti servizi AS
-- Definizione setup di programma


### PARAMETRIZZAZIONE

- Definizione delle variabili di Loocup coinvolte


### PROCESSO

- Ripetitività
- Flusso
- Processo seriale o parallelo
- Definizione dei files di log
- Definizione dei files temporanei
- Emissione dell'errore
- Debuggabilità
- Elaborazione post-generazione
-- Stampa automatica
-- Apertura file generato
-- Invio per e-mail


### FUNZIONI

- Manutenzione ordinaria
-- Gestione dei file generati :  eliminazione, visualizzazione, etc.
- Stampa su carta
-- G87 e LPD_PDF
-- ...


### VEDI ANCHE
- [Gestione Spool to STMF](Sorgenti/MB/DOC_OGG/P_TSTG87)

## STAMPE DOCUMENTI DI TESTO
### ASPETTI GENERALI DELLE STAMPE DI TESTO
**Definizione chiara della sintassi**

- Elementi gestiti
-- Paragrafi
-- Liste
-- Tabelle
-- Titoli
-- Immagini
-- Allineamento testo
-- Testo colorato/grassetto/italic
-- Link di vario tipo
-- Copertina
-- Header e footer di pagina
-- ...


**Stampe PDF**

**INTRODUZIONE**
- [PDF Setup](Sorgenti/MB/DOC/LOCFRM_PD)
**SETUP SPECIFICO**
- [PDF Setup](Sorgenti/MB/DOC/LOCFRM_PDS)


- Ricorsività sui link o files di indice?
- SETUP SPECIFICO
-- Livelli di sviluppo
-- Sviluppo dei link in documento unico o multiplo
-- Cartella immagini
-- Copertine
-- Header e footer
-- Indice
-- Visibilità numeri sezione


**Stampe LTX**
- [LATEX - Da doc. attiva a PDF](Sorgenti/MB/DOC/LOCFRM_LT)

- Analisi dei prerequisiti per la generazione
- Lancio batch
- Semaforo su generazione
- SETUP SPECIFICO
-- Console di generazione
-- Generazione non interattiva

**Stampe Wiki**

- Sintassi da utilizzare
- Gestione dei caratteri non consentiti nei nomi files (£, etc.)
- Operazione sui files generati (eliminazione, etc.)
- Accessibilità dei files generati
- SETUP SPECIFICO
-- IP Server
-- Utente
-- Password
-- Utente Wiki di aggiornamento


### STAMPE REPORT
**INTRODUZIONE**
- [Introduzione](Sorgenti/MB/DOC/LOCREP_INT)
**SETUP SPECIFICO**
- [Setup del Report](Sorgenti/MB/DOC/LOCREP_STP)


 T(Altri aspetti in sospeso)
- Parametrizzazione icone, loghi, etc.
- Utilizzo di template avanzati
- Sensibilità ai setup sui dati anche nelle generazioni da F così come nei "Visualizza come"
- Prerequisiti del servizio dei dati :  chiamata con restituzione struttura


### STAMPE SPOOL
Stampe H53
- [Funzione di generazione PDF](Sorgenti/MB/DOC_OGG/P_TSTH53)
