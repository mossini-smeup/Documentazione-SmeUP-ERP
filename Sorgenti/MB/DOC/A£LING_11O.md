# Passi da eseguire per rendere traducibile un'installazione
- Definizione ambiti
- Impostazioni degli ambienti
- Impostazione estrazione globale (facoltativo ma consigliato)
- Impostazione tabella A£1
- Estrazione, preparazione, traduzione e generazione per ambiti personali

# Definizione degli ambiti

Obiettivo :  definire quali ambiti vengono gestiti su un'installazione, sia per guidare le estrazioni che per il reperimento delle traduzioni.

Come :  definendo le apposite schiere in una exit A£TR00_x, dove x verrà poi impostato nella tabella A£1 (campo T$A£1F). Fare riferimento alle exit di esempio A£TR00_* in A£SRC.

Cosa va specificato : 
 * Ambiti definiti :  al minimo ambito standard 00 ed ambito personalizzato 10.
 * Associazione librerie -> ambiti :  serve sia per sapere che ambito usare nelle nuove frasi estratte, sia per capire se una traduzione è utilizzabile in un ambiente.
 * Ambiti modificabili :  si consiglia di lasciare modificabili solo gli ambiti >=10, perchè l'ambito 00 è competenza di Sme.UP e viene aggiornato al prossimo rilascio.

## Scelte sugli ambiti

Nel caso di un'unica azienda da gestire in lingua è sufficiente l'ambito personalizzato 10, da associare alle librerie utente (SME_PER, SMEDATPER e simili).

Nel caso di più aziende con la stessa lingua sullo stesso iSeries sono possibili le seguenti strade : 
 * Tutte le traduzioni sono in un unico archivio, in una libreria comune (es. SMEDATGRU) :  in questo caso si consiglia di definire un ambito comune (10) e uno specifico per ogni azienda (es. 11 per azienda 1, 12 per azienda 2, ...), associandoli opportunamente alle diverse librerie.
 * Si mantengono le traduzioni su archivi diversi. In questo caso si possono definire solo ambiti 00/10 separati e indipendenti.

Il primo caso permette di non ripetere certe attività (es. la traduzione dei programmi personali comuni), il secondo dà più indipendenza (es. è possibile avere due livelli di aggiornamento di Sme.UP diversi).

# Impostazione degli ambienti

I file delle lingue devono stare nella libreria dati del cliente (es. SMEDATPER).

È necessario avere in linea le librerie degli oggetti compilati in lingua. La convenzione che seguiamo è SME_xxyy, con xx=lingua e yy=ambito. Le librerie di ambito 00 per le lingue supportate (es. SME_EN00, SME_FR00, ...) vengono distribuite, quelle di ambito >=10 (es. SME_EN10, ...) vanno create e popolate dal cliente.

Per quanto riguarda l'impostazione delle lingue sugli ambienti riferirsi all'help di tabella A£B.

**Nota : **
La libreria SMETRD è la libreria che viene distribuita con gli aggiormenti delle traduzioni standard. Essa serve solo in fase di aggiornamento di release e non deve essere in linea negli ambienti in lingua.

## Impostazioni sulla traduzione di tabelle

Le descrizioni di settori, sottosettori e campi delle tabelle sono estratti e tradotti - sempre.

Per quanto riguarda le descrizioni degli elementi di tabella, è necessario decidere settore per settore (non è possibile agire per sottosettori), agendo sull'opportuno flag nella definizione del settore. Possibilità : 
 * Traduzione statica :  deprecata.
 * Traduzione dinamica :  traduzioni attive, cioè la tabella viene salvata in italiano, estratta e tradotta a runtime in ambienti in lingua.
 * Non tradurre :  la tabella non viene tradotta.

L'impostazione del "non tradurre" è utile nei seguenti casi : 
 * Ambiente nativo in lingua, cioè le tabelle vengono salvate direttamente nella lingua finale.
 * Tabella non utilizzata, per limitare le frasi su cui lavorare.
 * Tabella utilizzata, ma solo da utenti italiani (esempio tabelle di configurazione, non visibili da utenti ma solo dal CED italiano).
 * Tabella per cui le descrizioni degli elementi non sono testo da tradurre (es. B£U).

Negli altri casi si consiglia di attivare la traduzione, tenendo sempre presente l'overhead in termini di prestazioni introdotto dalla traduzione.

Per un setup più agevole, rispetto all'entrare nelle definizioni di ogni settore, è possibile utilizzare l'apposita scheda presente nel menù Installazione del modulo A£LING.

# Impostazione di un'estrazione globale di frasi

Obiettivo :  definire quali file andranno scansiti per l'estrazione di frasi personali/personalizzate.

Come :  definendo le apposite schiere in una exit A£TR01_x1, dove x1 sarà poi un parametro di chiamata al programma che estrae le frasi. Si veda la exit di esempio A£TR01_X1 in A£SRC.

Cosa va specificato :  le combinazioni di libreria/file dei vari file di estrarre, suddivisi in diverse schiere (programmi, script, tabelle, ...).
E' possibile (anche se non obbligatorio) riportare tale suffisso in tabella A£1 (campo T$A£1J). In questo modo non sarà necessario indicarla nei vari lanci di estrazione.

# Impostazione tabella A£1

Configurare nel modo più opportuno per le proprie esigenze la tabella A£1

# Estrazione, preparazione, traduzione e generazione per ambiti personali
Una volta configurato correttamente, eseguire i 4 passi fondamentali : 
* estrazione delle frasi in italiano
* preparazione delle frasi da tradurre
* traduzione
* generazione degli oggetti in lingua
