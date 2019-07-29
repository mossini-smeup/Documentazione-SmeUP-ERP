# INTERVENTI SU UN OGGETTO
Perchè un oggetto possa essere gestito appieno tramite G99 vanno modificati : 
 * Il guida :  diventa un deviatore tra il vecchio guida (vecchia gestione) e il nuovo guida generico B£G99D (nuova gestione). Ad esempio :  BRAR01G è un deviatore che rimanda al vecchio guida (ridenominato BRAR01G2) per la vecchia gestione, al B£G99D con tipo 'AR' per la nuova.
 * Il lista :  con la nuova gestione deve passare per la £G99, sia per elencare le azioni eseguibili su un oggetto, sia per eseguirle.
 * Il deviatore, per quanto riguarda le azioni di gestione :  con la nuova gestione si auto-devia sulla £G99, in ESE-GES. Sarà la £G99 a decidere se richiamarlo per effettuare l'azione o meno.
Il deviatore deve inoltre tornare, all'inserimento/copia, il codice dell'oggetto creato in £FUNK1 e una segnalazione in caso di mancata creazione (£FUNCM=£F03/£F12 oppure £FUNMS valorizzato e diverso da 'ESEG').
 * Bisogna eliminare le chiamate dirette al dettaglio dell'oggetto, sostituendole con quelle al relativo deviatore.

NOTA BENE :  E' necessario chiamare una replica opportuna, sia nel B£GES0 che nelle sostituzioni, per evitare che eventuali chiamate al deviatore fatte nei flussi generino ricorsione!

# ALTRE LINEE GUIDA SULLA GESTIONE OGGETTI
Per ogni oggetto : 
 * Non dovrebbero essere effettuate chiamate dirette al suo pgm di dettaglio, ma bisognerebbe sempre passare per il relativo deviatore. Questo garantisce consistenza sui controlli su chi e quando può accedere all'oggetto.
 * Tutti i controlli sull'istanza dell'oggetto (esempio di bontà del codice in fase di inserimento, no duplicati, ...) dovrebbero essere fatti dal pgm di dettaglio, con un ritorno adeguato in termini di messaggi di errore.

# INTEGRAZIONE CON IL WORKFLOW
Perchè un oggetto (es. AR) sia integrato con il WF, in modo che sia il motore di workflow a guidarne la gestione, sono necessari i seguenti interventi : 
 * L'oggetto deve essere integrato con la G99 (guida, lista, deviatore);
 * Deve essere definito l'attributo J/W01 sul tipo oggetto (workflow attivi su oggetto);
 * Il dettaglio dell'oggetto deve "spegnere" la modifica dello stato se questo è gestito a WF (va testato l'attributo J/W02 su OG//AR); ricordarsi di aggiornare gli attributi del tipo OG.
 * La scheda dell'oggetto deve presentare la sottoscheda WFOGGE con in chiave 1 l'oggetto, se questo è gestito a WF (va testato l'attributo J/W01 di AR//codice).
 * il pgm WFAZB£_05 deve gestire il cambio stato sull'oggetto.

Per l'utilizzo di oggetti sotto WF vedi il documento : 
- [Integrazione con gli oggetti](Sorgenti/MB/DOC/WFBASE_029)

# OGGETTI CON INSERIMENTO "COMPLESSO"

Alcuni oggetti possono chiedere la compilazione di diversi campi prima di far partire l'inserimento.
Ad esempio l'oggetto DQ chiede la compilazione di una griglia di 3 oggetti e di un livello di modifica.
Per gestire questa casistica sono necessari i seguenti interventi : 
 * Definire una DS specifica nella £G99DS.
 * Trattare i campi della DS specifica nel guida B£G99D.
 * Gestire il passaggio di questa DS dal deviatore (a cui arriva in £FUND2) al programma di dettaglio.
 * In caso di workflow aggiungere la casistica per il colloquio tra creazione/esecuzione del processo (programmi WFDV01X e WFAZB£_02).

# OGGETTI INTEGRATI CON G99/WF E NOTE SPECIFICHE
## AR - Articoli
## CN - Enti
## DO/DR - Documenti e righe.
Azioni speciali - 'RI', '13' :  nel WF sono gestite rispettivamente come 02 e 03, quindi vengono presentate ogni volta che un utente è autorizzato su 02 e 03.

La gestione degli oggetti 'DR' sotto workflow è speciale :  è ereditata dal 'DO' corrispondente, quindi se un 'DO' è gestito a WF la gestione dei suoi 'DR' è sottoposta ai vincoli dello stesso WF.

## NC - Non conformità
Integrato con WF tranne la gestione in lista (CQNC01R, che parte dalle azioni utente?)

## CM - Commesse

## H3 - Nuove richieste di intervento

## Altri oggetti da integrare
Oggetti per cui può essere interessante un'integrazione : 
 * OR
 * RI
 * CE
 * LO?
 * RA - qualcosa c'è, ma vengono sostituite dalla nuova gestione V5.
