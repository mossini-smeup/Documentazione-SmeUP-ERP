In generale i motivi per cui qualcosa non si vede tradotto sono : 
* non ho configurato correttamente la struttura (exit e tabelle)
* l'ambiente non è configurato in lingua
* l'oggetto non è configurato per essere tradotto
* le frasi non sono state estratte
* le frasi non sono state tradotte

## Ho configurato correttamente l'ambiente?
Andare nella scheda del modulo A£LING, selezionare "situazione ambiente" e verifica che sia tutto ok,
* in "controlli configurazione" vengono segnalati degli errori?
* la libreria che contiene i dati da tradurre (lib dati per tabelle, lib sorgenti per servizi, ecc.) ha un ambito assegnato? Tale ambito figura tra i consentiti?
* la lingua in cui si vuole tradurre risulta tra le lingue supportate?

## L'ambiente è configurato in lingua?

## L'oggetto associato alla frase di cui vogliamo la traduzione, è correttamente configurto per essere tradotto?
Dipende di quale oggetto stiamo parlando.
Per le tabelle è possibile controllare da "controlli configurazione" il tab "definizioni tabelle".
Per DSPF, PRTF e MSGF, bisogna controllare di avere in linea la libreria degli oggetti tradotti SME_xx_yy relativa all'ambito corretto.
Ricordiamo che le descrizioni degli oggetti (Articoli, clienti, ecc.) non vengono tradotti tramite il modulo A£LING.

## Le frasi sono state estratte/preparate e tradotte?
Sempre dalla scheda del modulo A£LING è necessario selezionare "traduzione" e cercare la frase incriminata.
Se la frase non compare nel contesto corretto (se sto cercando la traduzione di un elemento di tabella, devo trovare quella frase associata a quel contesto), significa che non è stata correttamente estratta o preparata.
Se la frase compare ma non ha la traduzione, allora non è stata tradotta.
