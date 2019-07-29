# Chiamate
Descriviamo di seguito a grandi linee i principali compiti che deve svolgere un servizio di aggiornamento nelle varie fasi in cui viene chiamato dal client.

## Setup
Appena dopo la creazione della matrice (generazione della matrice di visualizzazione EXB) viene effettuata una chiamata al servizio di aggiornamento per impostare correttamente le modalità di aggiornamento previste.

Il servizio viene chiamato con : 

- Funzione (£UIBME) *SETUP
- Campo £UIBPA valorizzato con quanto specificato nell'attributo UpdPar nella riga G.SET.MAT della matrice. Il contenuto di tale campo è libero e può servire a passare informazioni per il corretto setup del servizio stesso, oltre che dati aggiuntivi (non contenuti nella riga di matrice) al momento dell'aggiornamento.


Il servizio deve restituire un XML contenente informazioni su : 

- Autorizzazione ad effettuare le operazioni di inserimento/modifica/cancellazione
-- £JayAutIns ='1' per abilitare l'inserimento
-- £JayAutUpd ='1' per abilitare l'update
-- £JayAutDel ='1' per abilitare la cancellazione
- Elenco dei campi trattati dal servizio, quali sono aggiornabili, quali sono campi chiave (quindi modificabili solo all'immissione), eventuale valore di default da proporre all'immissione... Il nome dei campi trattati deve corrispondere con la definizione dei nomi di colonna nella matrice di visualizzazione (EXB)!
-- £JayFldLst  :  schiera delle definizioni aggiuntive dei campi
-- £JayDSFld   :  ds per rimappatura degli elementi della schiera, così composta : 
--- £JayFNM  :  Nome Colonna
--- £JayFIO  :  Tipo di Gestione B=Input-Output/ O=Output / I=Input (trattato a tutti gli effetti come B) / H=Nascosto / K=Modificabile solo all'immissione
--- £JayFOB  :  Obbligatorio
--- £JayFNT  :  Controllo Tipo Oggetto 1=No / 2=Viene eseguito da Loocup
--- £JayFNC  :  Se valorizzato disabilita il controllo di consistenza del campo
--- £JayFAR  :  (autoenter o avanzamento record) Quando si conferma la cella viene richiamato il servizio di update con funzione *CHECK e nome del campo nel tag FLD di £UIBSS
--- £JayFLL  :  Lunghezza Campi Numerici
--- £JayFDD  :  Decimali Campi Numerici
--- £JayFFM  :  Formato (LC/UC)
--- £JayFOG  :  Tipo/parametro oggetto
--- £JayFDV  :  Valore di default per l'inserimento
--- £JayDES  :  Va indicato il nome del campo di cui il campo in oggetto costituisce la descrizione in questo modo, verrà automaticamente compilato
- Aggiornamento con controllo/conferma oppure diretto.
-- £JayAutChk  :  se valorizzato abilita il pulsante check
- Inizializzazione record in inserimento
-- £JayIniRow  :  se valorizzato abilita viene eseguita la chiamata con funzione *INIT per inizializzare i campi se viene eseguito un nuovo inserimento
-- £JayFirIns  :  attiva la riga di inserimento automatica
-- £JayAllIns  :  se attivo chiama il servizio di aggiornamento con TUTTI i record della matrice come nuovi inserimenti. Utile per riprese da Excel.
- Presenza di eventuali altri tasti funzione, il cui comportamento sarà a discrezione del servizio.
-- £JayCmd     :  comando
-- £JayCmdDes  :  descrizione comando
- Altri parametrizzazioni
-- £JayDisCon  :  Disabilita Controlli di Consistenza su tutti i campi
-- £JayDisTip  :  Disabilita Controlli su Consistenza su Tipo Oggetto di tutti i campi
-- £JayDisObb  :  Disabilita Controlli di Obbligatorietà su tutti i campi


## Inizializzazione
Se abilitata dal setup viene eseguita questa chiamata per inizializzare i campi di un nuovo record.

- Funzione (£UIBME) *INIT
- Vanno riempite le schiere con £JayVBef / £JayNumBef con i valori alfa/numerici di ogni colonna con i valori di default. Riempite tali schiere va eseguita la routine £JAY_INIT


## Aggiornamento
All'atto dell'aggiornamento vero e proprio il servizio viene chiamato con : 

- Funzione (£UIBME) *UPDATE
- Campo £UIBPA valorizzato in maniera analoga al caso del *SETUP
- Campo £UIBD1 contenente i dettagli dell'operazione di aggiornamento, descritti di seguito


Un'operazione di aggiornamento è un insieme di operazioni elementari, dette Line, ognuna relativa a una riga di matrice.
Ogni Line è identificata da : 

- Id, Identificativo Line :  parte da 0 ad ogni sessione (ogni volta che si ricarica la matrice), identifica univocamente l'operazione
- Op, Tipo operazione :  inserimento / modifica / cancellazione
- Before :  valori dei campi della matrice prima dell'operazione e numero di riga (ID). Vengono passati solo i campi trattati dal servizio di aggiornamento, cioè quelli dichiarati all'atto del *SETUP
- After :  valori dei campi modificati dall'utente


A seconda del tipo di operazione vengono o meno passati i valori Before e After, cioè : 

- Inserimento :  non sono passati valori Before, nei valori After compaiono tutti i campi immessi dall'utente. Nel caso di immissione di un record di dati, ad esempio, verranno sicuramente passati tutti i campi necessari a costruire la chiave del record da scrivere, oltre ad eventuali altri campi.
- Modifica :  vengono passati sia Before (usati per capire che cosa modificare) che After.
- Cancellazione :  solo i valori Before, utilizzati per individuare cosa cancellare.


Il servizio deve effettuare una scansione su tutte le Line ricevute, per ognuna di esse un insieme-tipo di passi svolti dal servizio potrebbe essere : 

- (Modifica / cancellazione) Individua l'entità (ad esempio il record) su cui operare; (inserimento) verifica ad esempio che il record non esista già, se non sono ammessi duplicati
- (Modifica) Effettua controlli di consistenza sui valori presenti in matrice all'atto dell'inserimento e quelli da modificare
- (Inserimento / modifica) Esegue vari controlli sui valori immessi dall'utente (tipo, obbligatorietà, altri controlli specifici)
- (Inserimento / modifica) Completa, se possibile, i campi non immessi (es. decodifiche)
- Esegue eventualmente la scrittura/cancellazione.


Esempi di scelte che vanno operate sul comportamento del servizio : 

- Decidere quali controlli deve effettuare (consistenza, tipo, obbligatorietà...)
- Decidere se effettuare l'operazione anche in presenza di errori o meno
- Decidere, in caso di più Line, se effettuare una scrittura per ogni Line oppure se scrivere una volta per tutte, eventualmente dopo aver effettuato ulteriori controlli globali
- Modificare altre righe della matrice oltre a quelle richieste dal client (in pratica "aprire" nuove Line)


Alla fine il servizio deve restituire un XML contenente informazioni per il client sugli esiti delle operazioni. Per ogni Line deve indicare : 

- Esito dell'operazione (eseguita :  Upd="Yes")
- Valori dei campi da visualizzare in matrice dopo l'operazione (può specificare solo i campi modificati oppure tutti)
- Eventuali messaggi di errore, di record o di campo


# Altre chiamate (da fare/completare)
## Check
Valorizzando a '1' la variabile £JayAutChk nel SETUP della matrice si abilita un pulsante di controllo, la cui pressione fa partire una chiamata del tutto analoga a un *UPDATE ma con funzione *CHECK.
Si può condizionare quindi il servizio per non eseguire la scrittura ma solo i controlli quando la funzione è *CHECK.

## Exit
L'uscita dalla matrice (F12) innesca una chiamata con funzione *EXIT, che può essere gestita dal servizio per eventuali deallocazioni od operazioni simili.

## Cmd (in sviluppo)
