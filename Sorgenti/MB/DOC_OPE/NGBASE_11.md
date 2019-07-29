# Gestione Commenti

## Gestione Commenti

Questa funzionalità di Negoziando permette di gestire correttamente i Commenti utilizzati da Negoziando in varie funzioni (Stampa Scontrini in Cassa Slave, Gestione WorkFlow etc...)

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Commenti

All'attivazione della funzioneviene presentato l'elenco dei Commenti esistenti in Negoziando
Sono a disposizione i normali tasti di Negoziando per Inserimento, Modifica, Visualizzazione, Cancellazione e Duplicazione.

## Richiesta Informazioni di Testata

All'attivazione delle funzioni di gestione vengono richieste le informazioni di Testata del Commento selezionato

 * Descrizione Commento
 * Tipologia del Commento, che può essere : 
 ** Commento per Gestione Attività W.F. Documenti
 ** Commento per Gestione Attività W.F. Ordini Fornitori
 ** Commento per Invio Comunicazioni a Clienti Fidelity
 ** Commento per Invio Mail W.F. Documenti
 ** Commento per Invio Mail W.F. Ordini Fornitori
 ** Commento per Stampa Documenti Ritiro Prodotti Usati
 ** Commento per Stampa Informazioni Buoni su Scontrino
 ** Commento per Stampa Informazioni Fidelity su Scontrino
 ** Commento per Stampa Informazioni Tessere Regalo su Scontrino
 ** Commento per Stampa Messaggi Cortesia su Scontrino
 ** Libero

E' possibile indicare un Numero di Caratteri per Riga, per cui Negoziando, in fase di digitazione del Testo del Commento, controllerà la lunghezza dei caratteri della singola Riga rispetto al numero specificato e ne darà eventuale segnalazione con richiesta di Conferma

## Richiesta Informazioni di Riga - Commenti Normali

Digitare il testo del Commento e premere F6 per Conferma. Durante la digitazione è possibile utilizzare il tasto F2 per l'inserimento nel testo dei valori variabili.
Es. Variabile %DATOGGI% = Data Attuale. Utilizzando questo valore all'interno del commento, il sistema imposterà in automatico la data corrente all'interno del commento
Le variabili utilizzabili cambiano in base alla Tipologia del Commento selezionato. Se la Tipologia di Commento non prevedere l'utilizzo di Variabili il tasto F2 non viene attivato.

## Richiesta Informazioni di Riga - Commenti per Invio Mail Gestione Work Flow (vedi capitolo)

In questo caso le informazioni di Riga vengono distinte in tre gruppi : 

 * Destinatari
 * Oggetto
 * Testo della Mail
Fornire le indicazioni richieste e premere F6 per Conferma.Per questa tipologia di Commento premendo F2 è possibile inserire, oltre ai valori variabili, anche informazioni delle Tabelle del Database.

## Richiesta Informazioni di Riga - Commenti Attività Gestione Work Flow

Per questa tipologia di Commento non è prevista l'indicazione di un testo, ma vengono richieste informazioni specifiche.
Indicare le singole informazioni e premere Invio per Conferma.
P.S. Anche in questo caso è previsto l'utilizzo del tasto F2 per l'inserimento di valori variabili e di campi delle Tabelle del Database.
