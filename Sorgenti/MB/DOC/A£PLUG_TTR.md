# Riferimenti : 
 * A. Marazzi
 * A. Zanchi

# INTRODUZIONE
L'obiettivo è quello di arrivare con la massima efficienza alla attivazione di Sme.up presso un cliente.
 T(Le attività che portano a tale obiettivo sono)
- Road Map di conoscenza del cliente attraverso Audit
- Installazione automatica guidata
- Predisposizione ambiente di base
- Consigli operativi
-- gestione ambiente OS400
-- gestione ambiente Sme.up
-- gestione ambiente Loocup
- Documentazione attiva applicazioni
- Utilizzo di modelli


# AMBIENTE BASE PROPOSTO (SMEUP_FIL)
Tutte le notti la SMEUP_FIL viene rigenerata dalla ricompilazione dei SRCDB della SMESTD e SMEDEV per cui viene ripulita totalmente
In un secondo passaggio (pgm B£UT11ECL) alcuni file vengono "popolati"
## AUTORIZZAZIONI FONDAMENTALI
Vengono fornite tutte le classi di autorizzazioni previste
 * Il gruppo utenti "ADM" è abilitato a tutto
 * L'utente amministratore (es. SMEUPADM fornito dall'installazione) è iscritto al gruppo "ADM" quindi, appena collegato, è operativo a 360 gradi
## DEVIAZIONI
A seguito di alcuni aggiornamenti, alcune tabelle sono state "ridirette" su altri oggetti : 
 * tab. BAN deviata su oggetto "BA" (e quindi su "CN.BAN")
 * tab. BAP deviata su tabella "C5F" (dopo l'introduzione di Keep.up)
 * tab. CRW deviata su tabella "V5D" (quando Q9000 è in ambiente Sme.up)
## AZIENDA
## DEFINIZIONI TABELLE
Vengono forniti tutti i settori (e sottosettori) che Sme.up tratta in maniera esplicita, ovvero quelli che referenzia attraverso i suoi programmi.
Attualmente il TABDS00F viene ripreso direttamente da SMETAB.
 T( E' caratterizzato nei campi : )
- Archivio di appartenenza
- Tabella a elemento fisso
- Gestione subsettore
- Oggetto in subsettore
- Risalita al subsettore

 T(Non sono pre-impostati : )
- Condizionamento ricerca
- Funzione per autorizzazione


### DEFINIZIONI CAMPI TABELLE
Attualmente il TABDC00F viene ripreso direttamente da SMETAB

### DEFINIZIONI SOTTOSETTORI FONDAMENTALI

### ELEMENTI TABELLE FONDAMENTALI

### ELEMENTI TABELV0F
Il contenuto delle tabelle V§.. è conservato in TABELM0F di SMEMOD L'attività di ripristino schedulata recupera tale contenuto riempiendo il file TABELV0F di SMEUP_FIL

### DEFINIZIONE IN SMEMOD DEI SOTTSETTORI USATI (B£T£S)

### ATTRIBUTI BASE DI TUTTI GLI OGGETTI (OAV)

### ALTRI FILES A CONTENUTO FISSO

### NOMENCLATURE STANDARD
 Liberia di personalizzazione




## RESPONSABILI APPLICAZIONI (x documentazione)

| 
| .COL Txt="App" |
| ---|----|
| 
| .COL Txt="Resp." LunAut="1" |
| - A5 |   Calosi |
| - B£ |   Milani |
| - BR |   Milani |
| - C£ |   Visentin |
| - CQ|    Goffi |
| - C5 |   Calosi |
| - D0 |   Simonelli |
| - D5 |   Marazzi |
| - D9 |   Togni |
| - ED |   Avaldi. |
| - GM|    Archetti |
| - IG  |  Leali F. |
| - JA  |  Garatti |
| - JM  |  Lombardi |
| - LO  |  Garatti |
| - MM |  Goffi |
| - MP  |  Romuli |
| - MT  |  Milani |
| - M5  |  Magni |
| - PH  |  Avaldi |
| - P0  |  Milani |
| - P5  |  Bonzanini |
| - SF  |  Turetta |
| - S5  |  Galdini |
| - V5  |  Marazzi |
| - WE |  Foresti |
| 


# COMPITI DEI RESPONSABILI

- documentazione attiva (up doc)
- documentazione tabelle (F1)
- documentazione internet (AuthorIT)
- VALIDAZIONE modello (ambiente MOD)
- messaggi di secondo livello (MSGxx)
- proposta del criterio di codifica degli elementi di tabella
- elaborazione processi da copiare (es. c.lavoro)
- popolamento dati x demo


# STRUMENTI PER L'INSTALLATORE

- Corsi organizzati da SMEUP.SRL
- Documenti di visione (internet)
- Documento di installabilità (server)
- Documentazione tabelle ("F1")
- Documentazione attiva ("up doc")
- Installazione guidata ("loadrun")
- Modelli (B£AM70)


# SOSPESI

- Ricostruzione SMEDATxxx da SMEMOD o altro modello (vedi menu MOD0 in SMEMOD)
- Ci sta lavorando Daniele Dotti
- Creare pgm di controllo IN-congruenze all'interno dei file (?)
- Creare pgm di controllo IN-congruenze all'interno delle tabelle (di massa)
- Creare documento per indicazioni operative per : 
-- codifica elememti tabelle
-- scrittura pgm
-- procedure di Conversione / Istruzione / Avviamento
-- procedure di AS400
--- Impostazioni default
---- CHGCMDDFT
--- Configurazioni varie
---- TCP.IP
---- WEB-SERVER
---- MAIL-SERVER
--- Accensioni/Spegnimenti
-- procedure di BACK.UP
--- *Elenco librerie
--- *Periodicità
--- *LIB in SAVLIB
--- *SAVF
-- procedure di CLEAN.UP
--- CLEANUP
--- RGZPFM
--- File QHST*
-- procedure di TEST.UP
--- Librerie SME_TST
--- Librerie SMEDATTST
--- Creazione copia giornaliera
-- procedure di COMPORTAMENTO dal cliente
--- Rapportini di servizio
- Creare documento per indicazioni nomenclature std per : 
-- nomi src utilities in SME_xxx/SRC_UTI
-- nomi src files personali in SME_xxx/SRC_DB
-- nomi src programmi personali in SME_xxx/SRC
-- nomi src query in SME_xxx
-- modalità di segnare le modifiche nei pgm std personalizzati
-  Creare utility per verificare le tabelle usate in sme.up ricercando in : 
-- sorgenti programmi
-- definizione campi di tabelle
-- definizione campi di files
- Creare la mappa dei programmi che cablano elementi di tabella
-- per le note (tab.NSC ed NSI)
-- per le autorizzazioni (tab.B£P)
- Tools importa-processi (tabelle in drill-down)
- Tools esporta-processi (tabelle in drill-down)
- Attributi video

