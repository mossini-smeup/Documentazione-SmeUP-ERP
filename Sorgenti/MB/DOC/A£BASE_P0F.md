## Premessa
All'inizio della fase di analisi dei processi è opportuna una riunione di kick off in cui il management indirizzi le linee strategiche e gli obiettivi da raggiungere con il progetto.
È auspicabile avere una formalizzazione degli obiettivi, in modo che ci possano fare da riferimento in tutte le fasi del progetto (in particolare sarebbe utile che ciascun Process Owner descrivesse gli obiettivi di business che il nuovo sistema dovrà contribuire a raggiungere, quali le cose più carenti e quali quelle presenti e considerate irrinunciabili nel sistema corrente).

In questa fase sono previsti dei corsi rivolti al personale IT, ai Process Owner e ai Key Users, basati sull'insegnamento dei fondamentali di Sme.up, le funzionalità delle applicazioni e dei moduli interessati al progetto.

L'analisi dei processi può avvenire, sia come descrizione generale del processo e delle funzionalità da implementare, che per differenza rispetto al sistema corrente.
In quest'ultimo caso è necessario che SME.up conosca il sistema corrente e che il personale interno (IT o Key User) possa dare una completa descrizione del sistema e delle sue particolarità e personalizzazioni rispetto allo standard.
## Documenti di analisi utente
### Obiettivi del sistema
Documento emesso dal P.O. con la descrizione di strategie e obiettivi di business che il sistema deve contribuire a raggiungere e la specificazione delle funzionalità ritenute imprescindibili nel nuovo sistema (quelle che nel vecchio erano carenti o mancanti oppure quelle che nel vecchio erano buone e non devono andare perse).
Il mantenimento di questo documento è a cura del P.M.C.
**Un esempio di Obiettivi è visibile nella cartella degli allegati di progetto.**

### Descrizione delle funzionalità richieste (Business Requirements -BR-)
Rappresenta la formalizzazione delle necessità per ogni business area interessata (in accordo con gli obiettivi enunciati dal Process Owner).
Ogni richiesta viene numerata con un prefisso indicante il processo e una numerazione progressiva (fungerà da riferimento nelle fasi successive). All'elenco delle richieste possono essere allegati esempi di output (screenshot, report, ecc...) già esistenti, da mantenere o riprodurre nel nuovo sistema oppure esempi di layout di output richiesti e da creare.
Questo documento è compilato dal K.U. e approvato dal P.O. e dal P.M.C.
**Un esempio di Business Requiremet è visibile nella cartella degli allegati di progetto.**

### Stato avanzamento lavori
Lo stato di avanzamento viene emesso, con la frequenza concordata con il cliente, dal P.M.S. ed è composto del gantt di progetto con indicate le attività completate e il grado di completamento per quelle in corso, fornendo peraltro il consuntivo alla data delle giornate spese.
**Un esempio di stato avanzamento dei lavori è visibile nella cartella degli allegati di progetto.

### Glossario
Si tratta di una breve descrizione dei termini specifici utilizzati in azienda e dall'applicazione, compilata sia dal personale del Cliente che da quello SME.up, con l'obiettivo, ciascuno per la parte di propria competenza, di stabilire una terminologia comune e di migliorare la comunicazione e il trasferimento di conoscenze.
**Un esempio di glossario è visibile nella cartella degli allegati di progetto.**

### Verbale di accettazione approvato dal Capo Progetto Cliente
>N.B. :  la modalità di implementazione usata in SME.up è tipicamente una modalità per prototipi interattiva, pertanto la chiusura vera e propria della fase di analisi processi sarà molto avanti; per contro, prima della chiusura definitiva della fase, molte funzioni e customizzazioni potranno essere già state realizzate nella versione definitiva.
**Questa nota si applica a tutte le fasi di analisi, sviluppo e customizzazione.**


### Analisi personalizzazioni e interfacce
In questa fase rientrano : 

- Analisi della migrazione dati : 
-- quali dati migrare (e quali inserire manualmente o non migrare)
-- come completare le informazioni richieste da Smeup e mancanti in origine (completamenti manuali o con regole da introdurre nella conversione)
-- quali alias per la trascodifica di informazioni specifiche predisporre
-- definizione della sequenza della migrazione
-- definizione della modalità elaborazione per la creazione dell'ambiente di test partendo dai dati presenti nel sistema corrente
- Analisi delle interfacce : 
-- quali interfacce attivare e quali informazioni scambiare
-- la frequenza
-- mappatura dati e regole per completare le informazioni richieste da Smeup e/o dai sistemi interfacciati
-- quale sistema è l'owner del dato, modalità di confronto e riconciliazione informazioni (es. anagrafici, giacenze, ...)
-- alias per eventuali trascodifiche
- Analisi personalizzazioni : 
-- verificare sempre in prima battuta se ci sono soluzioni alternative dentro lo standard od utilizzando delle exit
-- descrivere la soluzione proposta presentando anche dei layout (input / output) o dei modellini di elaborazione, considerando anche il punto di vista dell'utilizzatore
-- definire il tipo e frequenza di elaborazione
-- stabilire le politiche di autorizzazione
- Documenti tecnici
con riferimento al B.R. viene fornita una sintetica descrizione della soluzione, con riferimento agli input, agli output ed alla logica di elaborazione.
Informazioni aggiuntive possono eventualmente essere : 
-- modalità di elaborazione (interattivo, batch, coda lavori, ...)
-- modalità di stampa (utente, programma, ...)
-- profili di autorizzazione (a livello di gruppo utenti) previsti.
**Un esempio di Analisi tecnica è visibile nella cartella degli allegati di progetto.**
>N.B. :  spesso è più efficiente realizzare direttamente un prototipo della soluzione piuttosto che stilare un documento formale, in questi casi si concorda con il PMC che la documentazione tecnica è rappresentata direttamente dalla customizzazione e dallo sviluppo specifico.
Le utility di documentazione dinamica permettono di avere un output (documentazione programmi, documentazione tabelle) con la medesima funzionalità della documentazione tecnica.
- >Stato avanzamento lavori
- >Glossario
- >Verbale di accettazione approvato dal Capo Progetto Cliente
- >Rapporti attività SME.up

